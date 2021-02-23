import cv2
import numpy as np
import os
directory = "dataset/HR/"


for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # print(os.path.join(directory, filename))
        inputImage = cv2.imread(os.path.join(directory, filename))
        # resized = cv2.copyMakeBorder(inputImage, 0, 160, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        resized = cv2.resize(inputImage, (1280, 1280), interpolation=cv2.INTER_AREA)
        # filename = "re_" + filename
        cv2.imwrite(os.path.join(directory, filename), resized)
    else:
        continue
