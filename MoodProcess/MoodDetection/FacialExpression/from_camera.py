import torch
import cv2

from MoodProcess.MoodDetection.FacialExpression.FaceExpression import EmotionDetector
from MoodProcess.MoodDetection.InsightFace.models.utils import special_draw
from MoodProcess.MoodDetection.Retinaface.Retinaface import FaceDetector


class WebcamEmotionDetector:
    def __init__(self, device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):
        print('loading ...') 
        self.face_detector = FaceDetector(face_size=(224, 224), device=device)
        self.emotion_detector = EmotionDetector(device=device)


    def run(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        cap.set(3, 1280)
        cap.set(4, 720)
        print('type q for exit')
        while cap.isOpened():
            ret , frame = cap.read()
            if ret == False:
                raise Exception('the camera not recognized: change camera_index param to ' + str(0 if camera_index == 1 else 1))
            faces, boxes, scores, landmarks = self.face_detector.detect_align(frame)
            if len(faces.shape) > 1:
                emotions, emo_probs = self.emotion_detector.detect_emotion(faces)
                for i, b in enumerate(boxes):
                    b = b.numpy().astype(int)
                    special_draw(frame, b, landmarks[i], name=emotions[i], score=emo_probs[i])

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()