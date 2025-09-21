import cv2
from PIL import Image
import sys
import os

def remove_white_background(input_path, threshold=110):
    # 检查文件是否存在
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    # 构造输出路径：原文件名 + "_output.png"
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_output.png"

    # 读取图像（灰度）
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Cannot read image '{input_path}'")
        return

    # 二值化
    img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]

    # 转换为 RGBA 格式
    img = Image.fromarray(img).convert("RGBA")
    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    img.save(output_path, "PNG")
    print(f"Saved output to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    remove_white_background(input_file)