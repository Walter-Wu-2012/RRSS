from torch.utils.data import DataLoader

from MoodProcess.MoodPrediction.MoodDataLoader import MoodDataLoader
from MoodProcess.MoodPrediction.MoodPredictionNet import MoodPredictionNet
from MoodProcess.MoodPrediction.dataload import TrainDataloader
import torch
import torch.nn as nn
import torch.optim as optim

if __name__ == '__main__':

    epoch = 10
    numOneEpoch = 1
    batchsize = 16
    model = MoodPredictionNet()
    model.loadModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.002)

    model.train()

    md = MoodDataLoader('mood_index_interpolation', '6')
    dataloader = DataLoader(md, batch_size=16, shuffle=True)

    for i in range(epoch):
        running_loss = 0
        for oldschedule, newschedule, oldindex, newindex in dataloader:
            oldschedule = oldschedule.permute(0, 3, 2, 1).to(torch.float32)
            newschedule = newschedule.permute(0, 3, 2, 1).to(torch.float32)
            oldindex = oldindex.permute(0, 3, 2, 1).to(torch.float32)
            newindex = newindex.permute(0, 3, 2, 1).to(torch.float32)

            optimizer.zero_grad()

            # 2) make a prediction
            pre_newindex = model(oldschedule, newschedule, oldindex)

            # 3) calculate how much we missed
            # print(pre_newindex.shape)
            # print(newindex.shape)
            loss = criterion(pre_newindex, newindex)

            # 4) figure out which weights caused us to miss
            loss.backward()

            # 5) change those weights
            optimizer.step()

            # 6) log our progress
            running_loss += loss.item()
            # print(loss.item())
        model.saveModel()
        print('epoch:{} loss:{}'.format(i, running_loss / (numOneEpoch*len(dataloader))))

    # for i in range(epoch):
    #     for j in range(numOneEpoch):
    #         oldweek, newweek, oldindex, newindex = TrainDataloader(batchsize, 'datasets/train_new.csv')
    #         oldweek = oldweek.permute(0,3,2,1)
    #         newweek = newweek.permute(0,3,2,1)
    #         oldindex = oldindex.permute(0,3,2,1)
    #         newindex = newindex.permute(0,3,2,1).to(torch.float32)
    #
    #         optimizer.zero_grad()
    #
    #         # 2) make a prediction
    #         pre_newindex = model(oldweek, newweek, oldindex)
    #
    #         # 3) calculate how much we missed
    #         print(pre_newindex.shape)
    #         print(newindex.shape)
    #         loss = criterion(pre_newindex, newindex)
    #
    #         # 4) figure out which weights caused us to miss
    #         loss.backward()
    #
    #         # 5) change those weights
    #         optimizer.step()
    #
    #         # 6) log our progress
    #         running_loss += loss.item()
    #
    #     print('epoch:{} loss:{}'.format(i, running_loss / numOneEpoch))