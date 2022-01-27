import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os


class FaceDataLoader(Dataset):
    def __init__(self, filename, image_dir, resize_height=256, resize_width=256, repeat=1):



    def __getitem__(self, index):

        return img, label

    def __len__(self):

        return data_len

    def

    def load_data(self, path, resize_height, resize_width, normalization):
        '''
        加载数据
        :param path:
        :param resize_height:
        :param resize_width:
        :param normalization: 是否归一化
        :return:
        '''
        image = image_processing.read_image(path, resize_height, resize_width, normalization)
        return image

    def data_preproccess(self, data):
        '''
        数据预处理
        :param data:
        :return:
        '''
        data = self.toTensor(data)
        return data


if __name__ == '__main__':
