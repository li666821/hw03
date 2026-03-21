import streamlit as st
import os
from src.face_recognizer import detect_faces, extract_face_features, draw_face_boxes
from PIL import Image
import numpy as np

# 设置页面配置
st.set_page_config(
    page_title="人脸识别系统",
    page_icon="👤",
    layout="wide"
)

# 标题
st.title("人脸识别系统")
st.write("基于face_recognition和Streamlit的人脸检测与识别")

# 侧边栏
st.sidebar.title("操作选项")
option = st.sidebar.selectbox(
    "选择操作",
    ["上传图片", "使用示例图片"]
)

# 示例图片路径
EXAMPLE_IMAGES = {
    "示例1": "examples/example1.jpg",
    "示例2": "examples/example2.jpg"
}

# 确保examples目录存在
if not os.path.exists("examples"):
    os.makedirs("examples")
    # 创建默认示例图片（如果不存在）
    if not os.path.exists("examples/example1.jpg"):
        # 创建一个简单的示例图片
        img = Image.new('RGB', (400, 300), color='white')
        img.save("examples/example1.jpg")
    if not os.path.exists("examples/example2.jpg"):
        img = Image.new('RGB', (400, 300), color='lightgray')
        img.save("examples/example2.jpg")

# 处理图片
if option == "上传图片":
    uploaded_file = st.file_uploader("选择图片", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # 保存上传的图片
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # 显示原始图片
        st.subheader("原始图片")
        st.image(uploaded_file, width=500)
        
        # 检测人脸
        st.subheader("检测结果")
        with st.spinner("正在检测人脸..."):
            face_locations = detect_faces("temp_image.jpg")
            
        if face_locations:
            st.write(f"检测到 {len(face_locations)} 个人脸")
            
            # 绘制人脸框
            result_image = draw_face_boxes("temp_image.jpg", face_locations)
            st.image(result_image, width=500)
            
            # 提取特征
            face_encodings = extract_face_features("temp_image.jpg")
            st.write(f"提取到 {len(face_encodings)} 个人脸特征")
            st.write(f"特征维度: {len(face_encodings[0])} 维")
        else:
            st.write("未检测到人脸")

elif option == "使用示例图片":
    example_choice = st.sidebar.selectbox("选择示例图片", list(EXAMPLE_IMAGES.keys()))
    image_path = EXAMPLE_IMAGES[example_choice]
    
    # 显示原始图片
    st.subheader("原始图片")
    st.image(image_path, width=500)
    
    # 检测人脸
    st.subheader("检测结果")
    with st.spinner("正在检测人脸..."):
        face_locations = detect_faces(image_path)
        
    if face_locations:
        st.write(f"检测到 {len(face_locations)} 个人脸")
        
        # 绘制人脸框
        result_image = draw_face_boxes(image_path, face_locations)
        st.image(result_image, width=500)
        
        # 提取特征
        face_encodings = extract_face_features(image_path)
        st.write(f"提取到 {len(face_encodings)} 个人脸特征")
        st.write(f"特征维度: {len(face_encodings[0])} 维")
    else:
        st.write("未检测到人脸")

# 运行说明
st.sidebar.markdown("### 运行说明")
st.sidebar.markdown("1. 选择操作方式：上传图片或使用示例图片")
st.sidebar.markdown("2. 系统会自动检测人脸并提取特征")
st.sidebar.markdown("3. 查看检测结果和特征信息")

# 依赖说明
st.sidebar.markdown("### 依赖说明")
st.sidebar.markdown("- face_recognition: 人脸检测和识别")
st.sidebar.markdown("- streamlit: Web界面")
st.sidebar.markdown("- Pillow: 图像处理")
st.sidebar.markdown("- numpy: 数据处理")

# 系统依赖说明
st.sidebar.markdown("### 系统依赖")
st.sidebar.markdown("- dlib: face_recognition的底层依赖")
st.sidebar.markdown("- C++编译器: 编译dlib")
st.sidebar.markdown("- CMake: 构建dlib")