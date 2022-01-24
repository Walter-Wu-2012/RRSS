import numpy as np
from PIL import Image
import Retinaface

def alignImage(imagepath):
    img = Image.open("imgs\\"+imagepath)
    img = np.array(img)
    detector = Retinaface.FaceDetector()
    faces, boxes, scores, landmarks = detector.detect_align(img)
    image = Image.fromarray(faces.cpu().numpy()[0])
    # image.show()
    image.save("imgsAlign\\"+imagepath)


if __name__ == '__main__':

    alignImage("input2.jpg")
