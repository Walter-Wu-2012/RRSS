import csv
import datetime
import random

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from MoodProcess.MoodPrediction.lstm import lstm


def read_glove_vecs(glove_file):

    with open(glove_file, 'r',encoding='utf-8') as f:
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
            X_indices[i, j] = word_to_index[w]
            # Increment j to j + 1
            j = j + 1

    return X_indices

def pretrained_embedding_layer(word_to_vec_map, word_to_index, non_trainable=True):
    num_embeddings = len(word_to_index) + 1
    embedding_dim = word_to_vec_map["cucumber"].shape[0]  #  dimensionality of GloVe word vectors (= 50)

    # Initialize the embedding matrix as a numpy array of zeros of shape (num_embeddings, embedding_dim)
    weights_matrix = np.zeros((num_embeddings, embedding_dim))

    # Set each row "index" of the embedding matrix to be the word vector representation of the "index"th word of the vocabulary
    for word, index in word_to_index.items():
        weights_matrix[index, :] = word_to_vec_map[word]

    embed = nn.Embedding.from_pretrained(torch.from_numpy(weights_matrix).type(torch.FloatTensor), freeze=non_trainable)

    return embed, num_embeddings, embedding_dim

def transSentence(sentences):
    word_to_index, index_to_word, word_to_vec_map = read_glove_vecs('datasets/glove.6B.50d.txt')
    maxLen = len(max(sentences, key=len).split())
    X_indices = sentences_to_indices(sentences, word_to_index, maxLen)

    embedding, vocab_size, embedding_dim = pretrained_embedding_layer(word_to_vec_map, word_to_index, non_trainable=True)

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
        old[i, :, :] = twoD[i*48:(i+1)*48,:]

    for i in range(7,14):
        new[(i-7), :, :] = twoD[i*48:(i+1)*48,:]

    return old, new

def TrainData(filename, dt):
    dt = datetime.datetime.strptime(dt, "%Y/%m/%d %H:%M")
    dt = dt + datetime.timedelta(days=-7)
    oldweek = np.zeros([7,48,5])
    newweek = np.zeros([7, 48, 5])
    oldindex = np.zeros([7,48,5])
    newindex = np.zeros([7, 48, 5])
    sentences = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i = 0
        flag = False
        for row in csvReader:
            r1 = datetime.datetime.strptime(row[1], "%Y/%m/%d %H:%M")
            # print(r1.strftime("%Y/%m/%d %H:%M"))
            # print(dt.strftime("%Y/%m/%d %H:%M"))
            if r1==dt:
                flag = True
                # print('match {}'.format(row[1]))

            if flag and i<7*96:

                if i<7*48:
                    j = int(i / 48)
                    k = i % 48
                    oldweek[j,k,0]=float(row[4])
                    oldweek[j,k, 1] = float(row[5])
                    oldweek[j,k, 2] = float(row[6])
                    oldweek[j,k, 3] = float(row[7])
                    oldweek[j,k, 4] = float(row[8])

                    oldindex[j,k, 0] = float(row[9])
                    oldindex[j,k, 1] = float(row[10])
                    oldindex[j,k, 2] = float(row[11])
                    oldindex[j,k, 3] = float(row[12])
                    oldindex[j,k, 4] = float(row[13])
                else:
                    j = int(i/48)-7
                    k = i % 48
                    newweek[j,k, 0] = float(row[4])
                    newweek[j,k, 1] = float(row[5])
                    newweek[j,k, 2] = float(row[6])
                    newweek[j,k, 3] = float(row[7])
                    newweek[j,k, 4] = float(row[8])

                    newindex[j,k, 0] = float(row[9])
                    newindex[j,k, 1] = float(row[10])
                    newindex[j,k, 2] = float(row[11])
                    newindex[j,k, 3] = float(row[12])
                    newindex[j,k, 4] = float(row[13])
                i=i+1
                sentences.append(row[2]+' '+row[3])
            elif flag and i>=7*96:
                break

    oldweek = torch.from_numpy(oldweek)
    newweek = torch.from_numpy(newweek)
    oldindex = torch.from_numpy(oldindex)
    newindex = torch.from_numpy(newindex)

    # print(len(sentences))
    sentences = transSentence(np.array(sentences))
    oldweeks, newweeks = twoD2threeD(sentences)
    oldweek = torch.cat((oldweeks,oldweek),dim=2)
    newweek = torch.cat((newweeks, newweek), dim=2)

    # print(oldweek.shape)
    # print(newweek.shape)
    # print(oldindex.shape)
    # print(newindex.shape)

    return oldweek, newweek, oldindex, newindex


def TestData(filename, dt):
    dt = datetime.datetime.strptime(dt, "%Y/%m/%d %H:%M")
    dt = dt + datetime.timedelta(days=-7)
    oldweek = np.zeros([7, 48, 5])
    newweek = np.zeros([7, 48, 5])
    oldindex = np.zeros([7, 48, 5])
    sentences = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i = 0
        flag = False
        for row in csvReader:
            if row[1] == dt.strftime("%Y/%m/%d %H:%M"):
                flag = True

            if flag and i < 7 * 96:

                if i < 7 * 48:
                    j = int(i / 48)
                    k = i % 48
                    oldweek[j, k, 0] = float(row[4])
                    oldweek[j, k, 1] = float(row[5])
                    oldweek[j, k, 2] = float(row[6])
                    oldweek[j, k, 3] = float(row[7])
                    oldweek[j, k, 4] = float(row[8])

                    oldindex[j, k, 0] = float(row[9])
                    oldindex[j, k, 1] = float(row[10])
                    oldindex[j, k, 2] = float(row[11])
                    oldindex[j, k, 3] = float(row[12])
                    oldindex[j, k, 4] = float(row[13])
                else:
                    j = int(i / 48) - 7
                    k = i % 48
                    newweek[j, k, 0] = float(row[4])
                    newweek[j, k, 1] = float(row[5])
                    newweek[j, k, 2] = float(row[6])
                    newweek[j, k, 3] = float(row[7])
                    newweek[j, k, 4] = float(row[8])
                i = i + 1
                sentences.append(row[2] + ' ' + row[3])
            elif flag and i >= 7 * 96:
                break

    oldweek = torch.from_numpy(oldweek)
    newweek = torch.from_numpy(newweek)
    oldindex = torch.from_numpy(oldindex)

    # print(len(sentences))
    sentences = transSentence(np.array(sentences))
    oldweeks, newweeks = twoD2threeD(sentences)
    oldweek = torch.cat((oldweeks, oldweek), dim=2)
    newweek = torch.cat((newweeks, newweek), dim=2)

    # print(oldweek.shape)
    # print(newweek.shape)
    # print(oldindex.shape)

    return oldweek, newweek, oldindex

def TrainDataloader(batchsize, filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        row1 = next(csvReader)
        total = len(open(filename).readlines())

    shift = random.randint((7*48), total-(7*48))
    dt = datetime.datetime.strptime(row1[1], "%Y/%m/%d %H:%M")
    dt = dt + datetime.timedelta(hours=+(0.5 * shift))
    oldweek, newweek, oldindex, newindex = TrainData(filename, dt.strftime("%Y/%m/%d %H:%M"))
    oldweek = oldweek.unsqueeze(0)
    newweek = newweek.unsqueeze(0)
    oldindex = oldindex.unsqueeze(0)
    newindex = newindex.unsqueeze(0)

    for i in range(1,batchsize):
        shift = random.randint(7*48,total-7*48)
        # print(shift)
        dt = datetime.datetime.strptime(row1[1], "%Y/%m/%d %H:%M")
        dt = dt + datetime.timedelta(hours=+(0.5*shift))
        # print(dt)
        oldweek1, newweek1, oldindex1, newindex1 = TrainData(filename, dt.strftime("%Y/%m/%d %H:%M"))
        oldweek = torch.cat([oldweek,oldweek1.unsqueeze(0)],dim=0)
        newweek = torch.cat([newweek, newweek1.unsqueeze(0)],dim=0)
        oldindex = torch.cat([oldindex, oldindex1.unsqueeze(0)],dim=0)
        newindex = torch.cat([newindex, newindex1.unsqueeze(0)],dim=0)

    print(oldweek.shape)

    return oldweek, newweek, oldindex, newindex


def TestDataloader(batchsize, filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        row1 = next(csvReader)
        total = len(open(filename).readlines())

    shift = random.randint((7*48), total-(7*48))
    dt = datetime.datetime.strptime(row1[1], "%Y/%m/%d %H:%M")
    dt = dt + datetime.timedelta(hours=+(0.5 * shift))
    oldweek, newweek, oldindex = TestData(filename, dt.strftime("%Y/%m/%d %H:%M"))
    oldweek = oldweek.unsqueeze(0)
    newweek = newweek.unsqueeze(0)
    oldindex = oldindex.unsqueeze(0)

    for i in range(1,batchsize):
        shift = random.randint(7*48,total-7*48)
        # print(shift)
        dt = datetime.datetime.strptime(row1[1], "%Y/%m/%d %H:%M")
        dt = dt + datetime.timedelta(hours=+(0.5*shift))
        # print(dt)
        oldweek1, newweek1, oldindex1 = TestData(filename, dt.strftime("%Y/%m/%d %H:%M"))
        oldweek = torch.cat([oldweek,oldweek1.unsqueeze(0)],dim=0)
        newweek = torch.cat([newweek, newweek1.unsqueeze(0)],dim=0)
        oldindex = torch.cat([oldindex, oldindex1.unsqueeze(0)],dim=0)

    print(oldweek.shape)

    return oldweek, newweek, oldindex


if __name__ == '__main__':

    TrainDataloader(4, 'datasets/train_new.csv')

    # TrainData('datasets/train_new.csv', '2022/01/09  22:30')