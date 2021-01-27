#固定size的圖片每x度旋轉一次
import os
from cv2 import cv2
from PIL import Image
import numpy as np
import argparse

# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
 
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
 
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # 返回旋转后的图像
    return rotated

# input_path
img_path = r'D:\dataset\automatic-optical-defect-detection\generate_dataset\train'  # 輸入資料夾
# output_path
out_path = r'D:\dataset\automatic-optical-defect-detection\generate_dataset\rotate_train'

for fold in os.listdir(img_path):
    fold_path = os.path.join(img_path, fold)
    for img_name in os.listdir(fold_path):
        img_path = os.path.join(fold_path, img_name)
        img = =cv2.imread(img_path)
        #圖片旋轉
        for degree in (-90, 90, 15):
            img_rotate = rotate(img , degree)
            cv2.imshow(img_name, img_rotate)
            cv2.waitKey(0)