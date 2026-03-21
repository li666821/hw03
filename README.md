# hw03
基于face_recognition和Streamlit的人脸识别系统

## 项目结构
```
hw03/
├── src/
│   └── face_recognizer.py  # 人脸检测和识别核心功能
├── tests/  # 测试目录
├── examples/  # 示例图片目录
├── app.py  # Streamlit应用主文件
├── requirements.txt  # 依赖包
└── README.md  # 项目说明
```

## 功能说明

### 1. 人脸检测
- 使用face_recognition库检测图片中的人脸位置
- 返回人脸在图片中的坐标位置（top, right, bottom, left）

### 2. 人脸特征提取
- 提取人脸的128维特征向量
- 用于后续的人脸识别和比对

### 3. 人脸框绘制
- 在原始图片上绘制绿色的人脸框
- 直观展示检测结果

### 4. 可选：人脸比对
- 可与已知人脸库进行比对识别
- 计算人脸之间的相似度

## 如何准备人脸库（可选）

如果需要实现人脸识别功能，可以按照以下步骤准备人脸库：

1. 在项目根目录创建 `known_faces` 目录
2. 在该目录中存放已知人物的图片，每张图片包含一个清晰的人脸
3. 为每个人物创建一个子目录，目录名为人物姓名
4. 在Streamlit应用中添加加载已知人脸库的代码

## 运行与访问方式

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 系统依赖
- **dlib**: face_recognition的底层依赖
  - Windows: 需要Visual Studio C++编译器和CMake
  - Linux: 需要gcc/g++和CMake
  - macOS: 需要Xcode命令行工具和CMake

### 3. 运行应用
```bash
streamlit run app.py
```

### 4. 访问方式
- 运行命令后，Streamlit会自动打开浏览器
- 默认访问地址：http://localhost:8501

## 使用说明

1. 在Web界面中选择操作方式：
   - **上传图片**：上传本地图片进行人脸检测
   - **使用示例图片**：使用系统提供的示例图片

2. 系统会自动：
   - 检测图片中的人脸
   - 绘制人脸框
   - 提取人脸特征
   - 显示检测结果和特征信息

3. 查看结果：
   - 原始图片和带有人脸框的结果图片
   - 检测到的人脸数量
   - 提取的人脸特征数量和维度

## 技术栈
- **face_recognition**: 基于dlib的人脸识别库
- **Streamlit**: 快速构建Web应用的Python库
- **Pillow**: 图像处理库
- **numpy**: 科学计算库