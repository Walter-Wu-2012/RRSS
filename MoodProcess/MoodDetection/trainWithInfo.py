import numpy as np
from PIL import Image
from MoodProcess.MoodDetection.FacialExpression.FaceExpression_modified import EmotionDetector
from MoodProcess.MoodDetection.Retinaface.Retinaface import FaceDetector
from MoodProcess.MoodDetection.FaceDataLoader import FaceDataLoader

import torch
import torch.nn as nn
import torch.nn.functional as F

class FaceInfoNet(nn.Module):
    def __init__(self):
        super(FaceInfoNet, self).__init__()

        self.fc1 = nn.Linear(9,20) #几个输入得问一下
        self.fc2 = nn.Linear(20,20)
        self.fc3 = nn.Linear(20,5)

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, emotions,weather,location):
        x = torch.cat([emotions, weather, location], dim=0).to(torch.float32)

        x = F.relu(self.fc1)
        x = F.relu(self.fc2)
        x = self.fc3

        return x

    def saveModel(self):
        name = "FaceInfo.model"
        torch.save(self.state_dict(), name)
        print('save FaceInfo net')

    def loadModel(self):
        name = "FaceInfo.model"
        state_dict = torch.load(name, map_location=self.device)
        self.load_state_dict(state_dict, strict=False)
        print('load FaceInfo net')


if __name__ == '__main__':

    epoch = 10
    numOneEpoch = 1
    batchsize = 16
    model = FaceInfoNet()
    model.loadModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.002)

    model.train()

    #dataloader
    face_detector = FaceDetector(face_size=(224, 224))
    emotion_detector = EmotionDetector()

    facedata = FaceDataLoader(face,batchsize=1,shuffle=True)



    for i range(epoch):
        running_loss = 0

        for emotion, weather, location, moodindex in facedata:

            optimizer.zero_grad()

            pre_moodindex = model(emotion, weather, location)

            loss = criterion(pre_moodindex, moodindex)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

    model.saveModel()
    print('epoch:{} loss:{}'.format(i, running_loss / (numOneEpoch * len(dataloader))))