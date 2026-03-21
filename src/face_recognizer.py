import face_recognition
import numpy as np
from PIL import Image, ImageDraw

def detect_faces(image_path):
    """检测图片中的人脸"""
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

def extract_face_features(image_path):
    """提取人脸特征"""
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

def draw_face_boxes(image_path, face_locations):
    """在图片上绘制人脸框"""
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    for (top, right, bottom, left) in face_locations:
        draw.rectangle([(left, top), (right, bottom)], outline=(0, 255, 0), width=2)
    
    return image

def compare_faces(known_encodings, unknown_encoding, tolerance=0.6):
    """比对人脸"""
    return face_recognition.compare_faces(known_encodings, unknown_encoding, tolerance)

def get_face_distance(known_encodings, unknown_encoding):
    """计算人脸距离"""
    return face_recognition.face_distance(known_encodings, unknown_encoding)