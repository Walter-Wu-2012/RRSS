from torch.utils.data import DataLoader

from Database.usingdatabase import add_info, del_info
from MoodProcess.MoodPrediction.MoodDataLoader import MoodDataLoader
from MoodProcess.MoodPrediction.MoodPredictionNet import MoodPredictionNet
from MoodProcess.MoodPrediction.TestDataLoader import getTestData
from MoodProcess.MoodPrediction.dataload import TrainDataloader
import torch
from datetime import datetime, date, timedelta
import torch.nn as nn
import torch.optim as optim

if __name__ == '__main__':

    del_info('prediction', user_ID=6)

    model = MoodPredictionNet()
    model.loadModel()

    model.eval()
    with torch.no_grad():
        schedule, futureschedule, index, endtime = getTestData('mood_index_interpolation', '6')

        schedule = schedule.unsqueeze(dim=0).permute(0, 3, 2, 1).to(torch.float32)
        futureschedule = futureschedule.unsqueeze(dim=0).permute(0, 3, 2, 1).to(torch.float32)
        index = index.unsqueeze(dim=0).permute(0, 3, 2, 1).to(torch.float32)

        pre_newindex = model(schedule, futureschedule, index)

    pre_newindex = pre_newindex.permute(0, 3, 2, 1).cpu().numpy().squeeze()

    s = pre_newindex.shape
    td = timedelta(seconds=1800)
    # print(s)

    for i in range(s[0]):
        for j in range(s[1]):
            d = pre_newindex[i,j]
            add_info("prediction", User_ID=6, Time=endtime.strftime('%Y-%m-%d %H:%M:%S'), Stress=d[0], Chaotic=d[1], Happiness=d[2], Energy=d[3], Focus=d[4])
            endtime = endtime + td
