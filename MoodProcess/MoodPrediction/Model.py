import torch
import torch.nn as nn
import torch.nn.functional as F

from MoodProcess.MoodPrediction.ScheduleIndex import ScheduleIndex
from MoodProcess.MoodPrediction.MoodPredictionNet import MoodPredictionNet


class Model(nn.Module):
    def __init__(self, embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size):
        super(Model, self).__init__()
        self.schedule_index = ScheduleIndex(embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size)
        # self.schedule_index.loadModel()

        self.mood_prediction_net = MoodPredictionNet(6, 5)

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, sentence, vector, time, timestamp, feedback):
        schedule_out, timestamp = self.schedule_index(sentence, vector, time, timestamp, feedback)
        timestamp = torch.tensor(timestamp, dtype=torch.float32).to(self.device).unsqueeze(dim=1)
        # print('schedule_out shape', schedule_out.shape)
        # print('timestamp shape', timestamp.shape)
        mood_prediction = self.mood_prediction_net(schedule_out, timestamp)
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