from datetime import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F

class lstm(nn.Module):
    def __init__(self, embedding, embedding_dim, hidden_dim, vocab_size, output_size, batch_size):
        super(lstm, self).__init__()

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        # self.device = torch.device("cpu")

        self.batch_size = batch_size

        self.hidden_dim = hidden_dim

        self.word_embeddings = embedding

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_dim,
                            num_layers=2,
                            dropout=0.5,
                            batch_first=True).to(self.device)

        # The linear layer that maps from hidden state space to output space



    # output stimu:[32, 5], time:[32, 3], timestamp:[32, 1] (batch size: 32)
    def forward(self, sentence):
        #data process

        embeds = self.word_embeddings(sentence)
        embeds = embeds.to(self.device)

        # mood from text
        h0 = torch.zeros(2, sentence.size(0), self.hidden_dim).requires_grad_().to(self.device)
        c0 = torch.zeros(2, sentence.size(0), self.hidden_dim).requires_grad_().to(self.device)

        lstm_out, h = self.lstm(embeds, (h0, c0))
        # get info from last timestep only
        lstm_out = lstm_out[:, -1, :]
        # print ('LSTM layer output shape', lstm_out.shape)

        # Dropout
        # lstm_out = F.dropout(lstm_out, 0.5)

        return lstm_out