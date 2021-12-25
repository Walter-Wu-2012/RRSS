import torch
import torch.nn as nn
import torch.nn.functional as F

from MoodProcess.MoodPrediction.ScheduleIndex import ScheduleIndex
from MoodProcess.MoodPrediction.MoodPredictionNet import MoodPredictionNet


class Model(nn.Module):
    def __init__(self, embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size):
        super(Model, self).__init__()
        self.schedule_index = ScheduleIndex(embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size)
        self.schedule_index.loadModel()

        self.mood_prediction_net = MoodPredictionNet(5, 5)

    def forward(self, sentence, vector, time):
        schedule_out = self.schedule_index(sentence, vector, time)
        # print ('schedule_out shape', schedule_out.shape)
        mood_prediction = self.mood_prediction_net(schedule_out)
        # print('mood_prediction shape', mood_prediction.shape)

        return mood_prediction

    def saveModel(self):
        self.schedule_index.saveModel()
        self.mood_prediction_net.saveModel()
        print('save model net')

    def loadModel(self):
        self.schedule_index.loadModel()
        self.mood_prediction_net.loadModel()
        print('load schedule net')