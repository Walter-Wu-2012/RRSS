import time
import numpy as np
import cv2
def get_picture():
    cap = cv2.VideoCapture(0)
    print("is camera on？ {}".format(cap.isOpened()))
    t = time .localtime()
    name = str(t.tm_year) + str(t.tm_mon) + str(t.tm_mday) + str(t.tm_hour) + str(t.tm_min) + str(t.tm_sec)

    ret, frame = cap.read()
    if not ret:
        print("Failed to get image, please check")
    cv2.imwrite("{}.png".format(name), frame)
    print("get the picture and save it as {}.png".format(name))
    cap.release()


if __name__ == '__main__':
    get_picture()


