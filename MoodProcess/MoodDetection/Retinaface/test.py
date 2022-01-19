import numpy as np
from PIL import Image
import Retinaface

if __name__ == '__main__':

    img = Image.open('imgs/input2.jpg')
    img = np.array(img)
    detector = Retinaface.FaceDetector()
    faces, boxes, scores, landmarks = detector.detect_align(img)
    image = Image.fromarray(faces.cpu().numpy()[0])
    image.show()
