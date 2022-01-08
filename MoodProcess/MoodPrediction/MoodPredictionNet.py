import torch
import torch.nn as nn
import torch.nn.functional as F


class MoodPredictionNet(nn.Module):
    def __init__(self):
        super(MoodPredictionNet, self).__init__()

        self.conv_sti1 = nn.Conv2d(133, 256, 3, 1, 1)
        self.conv_sti2 = nn.Conv2d(256, 512, 3, 1, 1)
        self.conv_sti3 = nn.Conv2d(512, 256, 3, 1, 1)
        self.conv_sti4 = nn.Conv2d(256, 128, 3, 1, 1)

        self.conv_bm1 = nn.Conv2d(5, 32, 3, 1, 1)
        self.conv_bm2 = nn.Conv2d(32, 64, 3, 1, 1)
        self.conv_bm3 = nn.Conv2d(64, 128, 3, 1, 1)

        self.conv_px1 = nn.Conv2d(256, 128, 3, 1, 1)

        self.fc1 = nn.Conv2d(128, 128, 1, 1)
        self.fc2 = nn.Conv2d(128, 128, 1, 1)
        self.fc3 = nn.Conv2d(128, 5, 1, 1)
        self.fc4 = nn.Conv2d(14, 7, 1, 1)

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, past_event,future_event,past_mood):
        event = torch.cat([past_event, future_event], dim=3).to(torch.float32)

        # preprocess events
        sti = F.relu(self.conv_sti1(event))

        sti = F.relu(self.conv_sti2(sti))
        sti = F.relu(self.conv_sti3(sti))
        sti = F.relu(self.conv_sti4(sti))

        # chunk sti into past and future piece
        sti = sti.chunk(2,dim=3)
        past_sti = sti[0]
        future_sti = sti[1]

        # preprocess past mood
        basic_m = F.relu(self.conv_bm1(past_mood.to(torch.float32)))
        basic_m = F.relu(self.conv_bm2(basic_m))
        basic_m = F.relu(self.conv_bm3(basic_m))

        # concatenate past sti and past mood as past_x
        # process past_x
        past_x = torch.cat([past_sti, basic_m], dim=1)
        past_x = F.relu(self.conv_px1(past_x))

        # concatenate past x and future sti as x
        # process x
        x = torch.cat([past_x,future_sti], dim=3)


        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        x = x.permute(0, 3, 2, 1)
        x = self.fc4(x)
        x = x.permute(0, 3, 2, 1)

        return x

    def saveModel(self):
        name = "Prediction.model"
        torch.save(self.state_dict(), name)
        print('save Prediction net')

    def loadModel(self):
        name = "Prediction.model"
        state_dict = torch.load(name, map_location=self.device)
        self.load_state_dict(state_dict, strict=False)
        print('load Prediction net')