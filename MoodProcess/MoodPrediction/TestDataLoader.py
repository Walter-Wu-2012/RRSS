import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import dataset, DataLoader
from Database.SqlExecuter import UsingMysql
from datetime import datetime, date, timedelta
from MoodProcess.MoodPrediction.lstm import lstm


def read_glove_vecs(glove_file):
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


def sentences_to_indices(X, word_to_index, max_len):
    m = X.shape[0]  # number of training examples
    X_indices = np.zeros((m, max_len))
    for i in range(m):  # loop over training examples
        sentence_words = X[i].lower().split()
        j = 0
        for w in sentence_words:
            # Set the (i,j)th entry of X_indices to the index of the correct word.
            w = w.split('.')[0].split(',')[0]
            if j < max_len:
                X_indices[i, j] = word_to_index[w]
            # Increment j to j + 1
            j = j + 1

    return X_indices


def pretrained_embedding_layer(word_to_vec_map, word_to_index, non_trainable=True):
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


def transSentence(sentences):
    word_to_index, index_to_word, word_to_vec_map = read_glove_vecs('datasets/glove.6B.50d.txt')
    maxLen = len(max(sentences, key=len).split())
    # print(sentences)
    X_indices = sentences_to_indices(sentences, word_to_index, maxLen)

    embedding, vocab_size, embedding_dim = pretrained_embedding_layer(word_to_vec_map, word_to_index,
                                                                           non_trainable=True)

    hidden_dim = 128
    output_size = 5
    batch_size = 32
    model = lstm(embedding, embedding_dim, hidden_dim, vocab_size, output_size, batch_size)
    X_indices = torch.tensor(X_indices).type(torch.LongTensor)
    lstmout = model.forward(X_indices)

    return lstmout


def twoD2threeD(twoD):
    twoDshape = twoD.shape
    old = torch.zeros([7, 48, twoDshape[1]])
    new = torch.zeros([7, 48, twoDshape[1]])

    for i in range(7):
        old[i, :, :] = twoD[i * 48:(i + 1) * 48, :]

    for i in range(7, 14):
        new[(i - 7), :, :] = twoD[i * 48:(i + 1) * 48, :]

    return old, new

def getLastTime(table, user):
    with UsingMysql(log_time=True) as um:
        sql = "select Time from " + table + " where User_ID=" + user + " order by Time DESC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()['Time']

    return endtime

def getFutureSchedule(time, user):

    # endtime = time + timedelta(days=7) + timedelta(seconds=1810)
    td = timedelta(seconds=1800)

    sentenceslist = []
    schedule = np.zeros([7, 48, 5])
    for i in range(7*48):
        time = time+td*i
        s = getschedule(time, user)

        sentenceslist.append(s['Title'] + ' ' + s['Description'])
        j = int(i / 48)
        k = i % 48
        schedule[j, k, 0] = float(s['Importance'])
        schedule[j, k, 1] = float(s['Difficulty'])
        schedule[j, k, 2] = float(s['Comment'])
        schedule[j, k, 3] = float(s['Lasting_period'])
        schedule[j, k, 4] = float(s['feedback'])

    schedule = torch.from_numpy(schedule)

    sentenceslist = transSentence(np.array(sentenceslist)).cpu()
    sentences = torch.zeros([7, 48, sentenceslist.shape[1]])
    for i in range(7):
        sentences[i, :, :] = sentenceslist[i * 48:(i + 1) * 48, :]

    schedule = torch.cat((sentences, schedule), dim=2)

    # print(schedule.shape)

    return schedule



def getLastSaveTime(user):
    with UsingMysql(log_time=True) as um:
        sql = "select Time from mood_index_interpolation where User_ID=" + user + " order by Time DESC limit 1"
        um.cursor.execute(sql)
        endtime = um.cursor.fetchone()
        # print(endtime)
        if endtime==None:
            endtime= datetime.datetime.strptime('1977-01-01 00:00', "%Y-%m-%d %H:%M")
        else:
            endtime = endtime["Time"]

    return endtime

def getschedule(time, user):
    with UsingMysql(log_time=True) as um:
        sql = "select * from schedule where User_ID=" + user + " and Time<='"+str(time)+ "' and Time2>='"+str(time)+"'  order by Time DESC limit 1"
        # print(sql)
        um.cursor.execute(sql)
        rows = um.cursor.fetchall()

    if len(rows)==0:
        if time.hour>=8 and time.hour<=23:
            timecounter = time.replace(hour=8)
            timecounter = timecounter.replace(minute=0)
            gap = (time - timecounter).total_seconds() / 3600
            schedule={'Title':'Free time', 'Description':'nothing to do', 'Importance':1, 'Difficulty':1, 'Comment':6, 'Lasting_period':gap, 'feedback':0}
        else:
            timecounter = time.replace(hour=23)-timedelta(days=1)
            timecounter = timecounter.replace(minute=0)

                # print(time)
                # print(timecounter)
                # print('---------')
            gap = (time - timecounter).total_seconds() / 3600 - 0.5
            schedule = {'Title': 'Sleep', 'Description': 'Just for sleeping', 'Importance': 1, 'Difficulty': 1,
                        'Comment': 1, 'Lasting_period': gap, 'feedback': 0}
    else:
        lastperiod = (time - rows[0]['Time']).total_seconds()/3600-0.5
        schedule = {'Title': rows[0]['Title'], 'Description': rows[0]['Description'], 'Importance': rows[0]['Importance'], 'Difficulty': rows[0]['Difficulty'],
                    'Comment': rows[0]['Comment'], 'Lasting_period': lastperiod, 'feedback': rows[0]['feedback']}
    return schedule


def getTestData(table, user):
    time = getLastTime(table, user)
    starttime = time - timedelta(days=7) + timedelta(seconds=3610)
    endtime = time

    # data = get_table(self.table, time1= starttime,time2= endtime, user_ID= self.user)
    with UsingMysql(log_time=True) as um:
        sql = "select * from " + table + " where User_ID=" + user + " and Time between  '" + str(
            starttime) + "'  and  '" + str(endtime) + "'"
        # print(sql)
        um.cursor.execute(sql)
        data = um.cursor.fetchall()
    schedule = np.zeros([7, 48, 5])
    index = np.zeros([7, 48, 5])
    # print(len(data)/48)
    #
    sentenceslist = []

    for i in range(len(data)):
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

    # print(schedule.shape)

    schedule = torch.from_numpy(schedule)
    index = torch.from_numpy(index)

    # print(len(sentences))
    sentenceslist = transSentence(np.array(sentenceslist)).cpu()
    sentences = torch.zeros([7, 48, sentenceslist.shape[1]])
    for i in range(7):
        sentences[i, :, :] = sentenceslist[i * 48:(i + 1) * 48, :]
    # oldweeks, newweeks = self.twoD2threeD(sentences)
    schedule = torch.cat((sentences, schedule), dim=2)

    futureschedule = getFutureSchedule(time + timedelta(seconds=1800), '6')

    return schedule, futureschedule, index, endtime


if __name__ == '__main__':

    schedule, futureschedule, index, endtime = getTestData('mood_index_interpolation', '6')