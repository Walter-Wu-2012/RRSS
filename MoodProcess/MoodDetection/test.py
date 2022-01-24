import numpy as np
from PIL import Image
from MoodProcess.MoodDetection.FacialExpression.FaceExpression import EmotionDetector
from MoodProcess.MoodDetection.FacialExpression.from_camera import WebcamEmotionDetector
from MoodProcess.MoodDetection.Retinaface.Retinaface import FaceDetector


def testonimage():
    face_detector = FaceDetector(face_size=(224, 224))
    emotion_detector = EmotionDetector()
    imagepath = "input1.jpg"
    img = Image.open("imgs\\" + imagepath)
    img = np.array(img)

    faces, boxes, scores, landmarks = face_detector.detect_align(img)
    image = Image.fromarray(faces.cpu().numpy()[0])
    image.show()
    list_of_emotions, probab = emotion_detector.detect_emotion(faces)
    print(list_of_emotions)

if __name__ == '__main__':

    # testonimage()

    detector = WebcamEmotionDetector()
    detector.run()

