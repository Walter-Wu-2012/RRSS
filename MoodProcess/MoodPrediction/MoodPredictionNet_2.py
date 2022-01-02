import torch
import torch.nn as nn
import torch.nn.functional as F


class MoodPredictionNet(nn.Module):
    def __init__(self, n_input, n_output):
        super(MoodPredictionNet, self).__init__()
        self.predict = nn.Linear(n_input, n_output, bias=False)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, x):
        out = self.predict(x)
        return out

    def saveModel(self):
        name = "Prediction.model"
        torch.save(self.state_dict(), name)
        print('save Prediction net')

    def loadModel(self):
        name = "Prediction.model"
        state_dict = torch.load(name, map_location=self.device)
        self.load_state_dict(state_dict, strict=False)
        print('load Prediction net')