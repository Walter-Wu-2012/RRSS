import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import torch
import torch.nn as nn
import torch.utils.data
import torch.optim as optim

from MoodProcess.MoodPrediction.ScheduleIndex import ScheduleIndex


def read_glove_vecs(glove_file):
    with open(glove_file, 'r') as f:
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


def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)]
    return Y


def read_csv(filename):
    phrase = []
    vector = []
    time = []
    gt = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        for row in csvReader:
            phrase.append(row[0]+" "+row[1])
            vector.append([float(row[2]),float(row[3]),int(row[4])])
            time.append([int(row[5]), float(row[6]), float(row[7])])
            gt.append([float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12])])

    phrase = np.asarray(phrase)
    vector = np.asarray(vector)
    time = np.asarray(time)
    X = {'phrase':phrase, 'vector':vector, 'time':time}
    Y = np.asarray(gt)

    return X, Y
# def read_csv(filename):
#     phrase = []
#     emoji = []
#
#     with open(filename) as csvDataFile:
#         csvReader = csv.reader(csvDataFile)
#
#         for row in csvReader:
#             phrase.append(row[0])
#             emoji.append(row[1])
#
#     X = np.asarray(phrase)
#     Y = np.asarray(emoji, dtype=int)
#
#     return X, Y

def sentences_to_indices(X, word_to_index, max_len):
    """
    Converts an array of sentences (strings) into an array of indices corresponding to words in the sentences.
    """

    m = X.shape[0]  # number of training examples

    # Initialize X_indices as a numpy matrix of zeros and the correct shape
    X_indices = np.zeros((m, max_len))

    for i in range(m):  # loop over training examples

        # Convert the ith sentence in lower case and split into a list of words
        sentence_words = X[i].lower().split()

        # Initialize j to 0
        j = 0

        # Loop over the words of sentence_words
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


def train(model, trainloader, test_loader, criterion, optimizer, epochs=10):
    model.to(device)
    running_loss = 0

    train_losses, test_losses, accuracies = [], [], []
    for e in range(epochs):

        running_loss = 0

        model.train()


        for sentences, vector, time, labels in trainloader:

            print(labels.shape)
            sentences, vector, time, labels = sentences.to(device), vector.to(device), time.to(device), labels.to(device)

            # 1) erase previous gradients (if they exist)
            optimizer.zero_grad()

            # 2) make a prediction
            pred = model.forward(sentences, vector, time)

            # 3) calculate how much we missed
            loss = criterion(pred, labels)

            # 4) figure out which weights caused us to miss
            loss.backward()

            # 5) change those weights
            optimizer.step()

            # 6) log our progress
            running_loss += loss.item()

        print(running_loss / len(train_loader))


        # else:
        #
        #     model.eval()
        #
        #     test_loss = 0
        #     accuracy = 0
        #
        #     # Turn off gradients for validation, saves memory and computations
        #     with torch.no_grad():
        #         for sentences, labels in test_loader:
        #             sentences, labels = sentences.to(device), labels.to(device)
        #             log_ps = model(sentences)
        #             test_loss += criterion(log_ps, labels)
        #
        #             ps = torch.exp(log_ps)
        #             top_p, top_class = ps.topk(1, dim=1)
        #             equals = top_class == labels.view(*top_class.shape)
        #             accuracy += torch.mean(equals.type(torch.FloatTensor))
        #
        #     train_losses.append(running_loss / len(train_loader))
        #     test_losses.append(test_loss / len(test_loader))
        #     accuracies.append(accuracy / len(test_loader) * 100)
        #
        #     print("Epoch: {}/{}.. ".format(e + 1, epochs),
        #           "Training Loss: {:.3f}.. ".format(running_loss / len(train_loader)),
        #           "Test Loss: {:.3f}.. ".format(test_loss / len(test_loader)),
        #           "Test Accuracy: {:.3f}".format(accuracy / len(test_loader)))

    # # Plot
    # plt.figure(figsize=(20, 5))
    # plt.plot(train_losses, c='b', label='Training loss')
    # plt.plot(test_losses, c='r', label='Testing loss')
    # plt.xticks(np.arange(0, epochs))
    # plt.title('Losses')
    # plt.legend(loc='upper right')
    # plt.show()
    # plt.figure(figsize=(20, 5))
    # plt.plot(accuracies)
    # plt.xticks(np.arange(0, epochs))
    # plt.title('Accuracy')
    # plt.show()


# def predict(input_text, print_sentence=True):
#   labels_dict = {
# 		0 : "❤️ Loving",
# 		1 : "⚽️ Playful",
# 		2 : "😄 Happy",
# 		3 : "😞 Annoyed",
# 		4 : "🍽 Foodie",
# 	}
#
#   # Convert the input to the model
#   x_test = np.array([input_text])
#   X_test_indices = sentences_to_indices(x_test, word_to_index, maxLen)
#   sentences = torch.tensor(X_test_indices).type(torch.LongTensor)
#
#   # Get the class label
#   ps = model(sentences)
#   top_p, top_class = ps.topk(1, dim=1)
#   label = int(top_class[0][0])
#
#   if print_sentence:
#     print("\nInput Text: \t"+ input_text +'\nEmotion: \t'+  labels_dict[label])
#
#   return label

if __name__ == '__main__':

    X_train, Y_train = read_csv('datasets/train.csv')
    X_test, Y_test = read_csv('datasets/test.csv')

    word_to_index, index_to_word, word_to_vec_map = read_glove_vecs('datasets/glove.6B.50d.txt')

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    maxLen = len(max(X_train['phrase'], key=len).split())
    X_train_indices = sentences_to_indices(X_train['phrase'], word_to_index, maxLen)

    X_test_indices = sentences_to_indices(X_test['phrase'], word_to_index, maxLen)

    embedding, vocab_size, embedding_dim = pretrained_embedding_layer(word_to_vec_map, word_to_index, non_trainable=True)

    hidden_dim = 128
    output_size = 5
    batch_size = 32
    # print ('Embedding layer is ', embedding)
    # print ('Embedding layer weights ', embedding.weight.shape)

    model = ScheduleIndex(embedding, embedding_dim, hidden_dim, vocab_size, output_size, batch_size)
    # criterion = nn.CrossEntropyLoss()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.002)
    epochs = 100

    train_dataset = torch.utils.data.TensorDataset(torch.tensor(X_train_indices).type(torch.LongTensor),torch.tensor(X_train['vector']), torch.tensor(X_train['time']),
                                                   torch.tensor(Y_train).type(torch.float32))
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size)

    test_dataset = torch.utils.data.TensorDataset(torch.tensor(X_test_indices).type(torch.LongTensor),torch.tensor(X_test['vector']), torch.tensor(X_test['time']),
                                                  torch.tensor(Y_test).type(torch.float32))
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size)

    train(model, train_loader, test_loader, criterion, optimizer, epochs)

    model.saveModel()

    model.loadModel()


    #
    # # test_loss = 0
    # # accuracy = 0
    # # model.eval()
    # # with torch.no_grad():
    # #     for sentences, labels in test_loader:
    # #         sentences, labels = sentences.to(device), labels.to(device)
    # #         ps = model(sentences)
    # #         test_loss += criterion(ps, labels).item()
    # #
    # #         # Accuracy
    # #         top_p, top_class = ps.topk(1, dim=1)
    # #         equals = top_class == labels.view(*top_class.shape)
    # #         accuracy += torch.mean(equals.type(torch.FloatTensor))
    # # model.train()
    # # print("Test Loss: {:.3f}.. ".format(test_loss / len(test_loader)),
    # #       "Test Accuracy: {:.3f}".format(accuracy / len(test_loader)))
    # # running_loss = 0
    # #
    # # print("------------------------------------")
    # # predict("I hate you")
    # # predict("I want a pizza")
    # # predict("Lets see the game")
    # # predict("I love you Lisa")
    # # predict("This is the best day of my life")
    # # print("\n------------------------------------")