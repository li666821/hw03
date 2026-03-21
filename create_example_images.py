from PIL import Image
import os

# 确保examples目录存在
if not os.path.exists("examples"):
    os.makedirs("examples")

# 创建示例图片1
img1 = Image.new('RGB', (400, 300), color='white')
img1.save("examples/example1.jpg")

# 创建示例图片2
img2 = Image.new('RGB', (400, 300), color='lightgray')
img2.save("examples/example2.jpg")

print("示例图片创建完成")