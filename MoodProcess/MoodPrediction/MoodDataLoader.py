import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import dataset
from Database.SqlExecuter import UsingMysql
from datetime import datetime, date, timedelta

from Database.usingdatabase import get_table
from MoodProcess.MoodPrediction.lstm import lstm



class MoodDataLoader(dataset.Dataset):

    def __init__(self, table, user):
        super(MoodDataLoader, self).__init__()
        self.timelist = self.getTotalList(table, user)
        self.table = table
        self.user = user

    def __getitem__(self, index):
        time = self.img_info[index]
        starttime = time - timedelta(days=7)+timedelta(seconds=1810)
        endtime = time + timedelta(days=7)+timedelta(seconds=1810)

        data = get_table(self.table, time1= starttime,time2= endtime, user_ID= self.user)
        schedule = np.zeros([14, 48, 5])
        index = np.zeros([14, 48, 5])

        sentenceslist = []
        for i in range(data):
            sentenceslist.append(data[i]['Title'] + ' ' + data[i]['Description'])
            j = int(i / 48)
            k = i % 48
            schedule[j, k, 0] = float(data[i]['Importance'])
            schedule[j, k, 1] = float(data[i]['Difficulty'])
            schedule[j, k, 2] = float(data[i]['Comment'])
            schedule[j, k, 3] = float(data[i]['Lasting_period'])
            schedule[j, k, 4] = float(data[i]['feedback'])

            index[j, k, 0] = float(data[i]['Stress'])
            index[j, k, 1] = float(data[i]['Chaotic'])
            index[j, k, 2] = float(data[i]['Happiness'])
            index[j, k, 3] = float(data[i]['Energy'])
            index[j, k, 4] = float(data[i]['Focus'])

        schedule = torch.from_numpy(schedule)
        index = torch.from_numpy(index)

        # print(len(sentences))
        sentenceslist = self.transSentence(np.array(sentenceslist))
        sentences = np.zeros([14, 48, sentenceslist.shape[1]])
        for i in range(14):
            sentences[i, :, :] = sentenceslist[i * 48:(i + 1) * 48, :]
        # oldweeks, newweeks = self.twoD2threeD(sentences)
        schedule = torch.cat((sentences, schedule), dim=2)

        return schedule[:7,...], schedule[7:,...], index[:7,...], index[7:,...]



    def __len__(self):
        return len(self.timelist)




    def getTotalList(self, table, user):
        with UsingMysql(log_time=True) as um:
            sql = "select Time from "+table+" where User_ID="+int(user)+" order by Time DESC limit 1"
            um.cursor.execute(sql)
            endtime = um.cursor.fetchone()['Time']

            sql = "select Time from " + table + " where User_ID=" + user + " order by Time ASC limit 1"
            um.cursor.execute(sql)
            starttime = um.cursor.fetchone()['Time']

        gap = (endtime - starttime).total_seconds()/3600

        if gap<=(2*7*24):
            return False

        starttime = starttime + timedelta(days=7)
        endtime = endtime - timedelta(days=7)

        timelist = []
        # starttime = starttime + timedelta(seconds=1800)
        while(starttime<endtime):
            timelist.append(starttime)
            starttime = starttime + timedelta(seconds=1800)

        return timelist

    def read_glove_vecs(self, glove_file):

        with open(glove_file, 'r', encoding='utf-8') as f:
            words = set()
            word_to_vec_map = {}
            for line in f:
                line = line.strip().split()
                curr_word = line[0]
                words.add(curr_word)
                word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)

            i = 1
            words_to_index = {}
            index_to_words = {}
            for w in sorted(words):
                words_to_index[w] = i
                index_to_words[i] = w
                i = i + 1
        return words_to_index, index_to_words, word_to_vec_map

    def sentences_to_indices(self, X, word_to_index, max_len):

        m = X.shape[0]  # number of training examples
        X_indices = np.zeros((m, max_len))
        for i in range(m):  # loop over training examples
            sentence_words = X[i].lower().split()
            j = 0
            for w in sentence_words:
                # Set the (i,j)th entry of X_indices to the index of the correct word.
                X_indices[i, j] = word_to_index[w]
                # Increment j to j + 1
                j = j + 1

        return X_indices

    def pretrained_embedding_layer(self, word_to_vec_map, word_to_index, non_trainable=True):
        num_embeddings = len(word_to_index) + 1
        embedding_dim = word_to_vec_map["cucumber"].shape[0]  # dimensionality of GloVe word vectors (= 50)

        # Initialize the embedding matrix as a numpy array of zeros of shape (num_embeddings, embedding_dim)
        weights_matrix = np.zeros((num_embeddings, embedding_dim))

        # Set each row "index" of the embedding matrix to be the word vector representation of the "index"th word of the vocabulary
        for word, index in word_to_index.items():
            weights_matrix[index, :] = word_to_vec_map[word]

        embed = nn.Embedding.from_pretrained(torch.from_numpy(weights_matrix).type(torch.FloatTensor),
                                             freeze=non_trainable)

        return embed, num_embeddings, embedding_dim

    def transSentence(self, sentences):
        word_to_index, index_to_word, word_to_vec_map = self.read_glove_vecs('datasets/glove.6B.50d.txt')
        maxLen = len(max(sentences, key=len).split())
        X_indices = self.sentences_to_indices(sentences, word_to_index, maxLen)

        embedding, vocab_size, embedding_dim = self.pretrained_embedding_layer(word_to_vec_map, word_to_index,
                                                                          non_trainable=True)

        hidden_dim = 128
        output_size = 5
        batch_size = 32
        model = lstm(embedding, embedding_dim, hidden_dim, vocab_size, output_size, batch_size)
        X_indices = torch.tensor(X_indices).type(torch.LongTensor)
        lstmout = model.forward(X_indices)

        return lstmout

    def twoD2threeD(self, twoD):
        twoDshape = twoD.shape
        old = torch.zeros([7, 48, twoDshape[1]])
        new = torch.zeros([7, 48, twoDshape[1]])

        for i in range(7):
            old[i, :, :] = twoD[i * 48:(i + 1) * 48, :]

        for i in range(7, 14):
            new[(i - 7), :, :] = twoD[i * 48:(i + 1) * 48, :]

        return old, new



if __name__ == '__main__':
    with UsingMysql(log_time=True) as um:
        # sql = "select * from Mood_index order by id DESC limit 1"
        table = 'Mood_index'
        user = '6'
        sql = "select Time from " + table + " where User_ID=" + user + " order by id DESC limit 1"
        # sql = "select * from Mood_index where User_ID=6 order by id ASC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()['Time']

        sql = "select Time from " + table + " where User_ID=" + user + " order by id ASC limit 1"
        # sql = "select * from Mood_index where User_ID=6 order by id ASC limit 1"
        um.cursor.execute(sql)
        starttime = um.cursor.fetchone()['Time']

        gap = (endtime - starttime).total_seconds()/3600

        print(gap)

        timelist = []
        while (starttime < endtime):
            timelist.append(starttime)
            starttime = starttime + timedelta(seconds=1800)

        print(timelist)
