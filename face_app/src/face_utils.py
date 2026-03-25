import face_recognition
import cv2

def detect_faces(image):
    """检测人脸位置"""
    face_locations = face_recognition.face_locations(image)
    return face_locations


def encode_faces(image):
    """提取128维特征"""
    encodings = face_recognition.face_encodings(image)
    return encodings


def draw_faces(image, face_locations):
    """画框"""
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    return image