  import streamlit as st
import cv2
import numpy as np
from src.face_utils import   detect_faces, encode_faces, draw_faces
from src.recognize import load_known_faces, recognize_faces

st.title("人脸识别系统")

uploaded_file = st.file_uploader("上传图片", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 检测
    face_locations = detect_faces(rgb_image)

    # 编码
    encodings = encode_faces(rgb_image)

    # 识别
    known_encodings, known_names = load_known_faces()
    names = recognize_faces(encodings, known_encodings, known_names)

    # 画框+标注
    for (top, right, bottom, left), name in zip(face_locations, names):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    st.image(image, channels="BGR", caption="识别结果")