import torch
import torch.nn as nn
import torch.nn.functional as F

class ScheduleIndex(nn.Module):
    def __init__(self, embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size):
        super(ScheduleIndex, self).__init__()

        self.batch_size = batch_size

        self.hidden_dim = hidden_dim

        self.word_embeddings = embedding

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_dim,
                            num_layers=2,
                            dropout=0.5,
                            batch_first=True)

        # The linear layer that maps from hidden state space to output space
        self.fc = nn.Linear(hidden_dim, output_dim)

        self.fc_time = nn.Linear(3, 16)
        self.fc_time2 = nn.Linear(16, 1)

        self.fc_vector = nn.Linear(4, 16)
        self.fc_vector2 = nn.Linear(16, 32)
        self.fc_vector3 = nn.Linear(32, 4)

        self.fc_vector = nn.Linear(4, 16)
        self.fc_vector2 = nn.Linear(16, 32)
        self.fc_vector3 = nn.Linear(32, 4)

        self.fc_final = nn.Linear(9, 5)

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, sentence, vector, time):

        #data process
        vector = torch.tensor(vector,dtype=torch.float32).to(self.device)
        time = torch.tensor(time,dtype=torch.float32).to(self.device)

        sentence = sentence.to(self.device)
        embeds = self.word_embeddings(sentence)

        # mood from text
        h0 = torch.zeros(2, sentence.size(0), self.hidden_dim).requires_grad_().to(self.device)
        c0 = torch.zeros(2, sentence.size(0), self.hidden_dim).requires_grad_().to(self.device)

        lstm_out, h = self.lstm(embeds, (h0, c0))
        # get info from last timestep only
        lstm_out = lstm_out[:, -1, :]
        # print ('LSTM layer output shape', lstm_out.shape)

        # Dropout
        lstm_out = F.dropout(lstm_out, 0.5)

        fc_out = self.fc(lstm_out)
        # print ('FC layer output shape', fc_out.shape)
        # print ('FC layer output ', fc_out)

        #add time and vector(importance, difficulty, comment)
        t = self.fc_time2(self.fc_time(time))
        vector = torch.cat([vector,t],dim=1)
        vector = self.fc_vector3(self.fc_vector2(self.fc_vector(vector)))
        out = torch.cat([fc_out,vector],dim=1)
        out = self.fc_final(out)
        # out = F.softmax(out, dim=1)
        # print ('Output layer output shape', out.shape)
        return out

    def saveModel(self):
        name = "Schedule.model"
        torch.save(self.state_dict(), name)
        print('save schedule net')

    def loadModel(self):
        name = "Schedule.model"
        state_dict = torch.load(name, map_location=self.device)
        self.load_state_dict(state_dict, strict=False)
        print('load schedule net')