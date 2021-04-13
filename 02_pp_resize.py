import cv2
import numpy as np
import os

directory = "dataset/HR/"
out_directory = "dataset/RESIZE/"

size_demo = (1280, 1280)
size = (640, 640, 3)


def is_image_file(filename):
    suffix_img_names = {"bmp", "jpg", "jpeg", "png"}
    return str.lower(filename.split(".")[-1]) in suffix_img_names


def resize(img):
    height, width = img.shape[:2]

    blank_image = np.zeros(size, np.uint8)
    blank_image[:, :] = (255, 255, 255)

    l_img = blank_image.copy()

    x_offset = y_offset = 0
    # Here, y_offset+height <= blank_image.shape[0] and x_offset+width <= blank_image.shape[1]
    l_img[y_offset:y_offset + height, x_offset:x_offset + width] = img.copy()
    return l_img


if __name__ == '__main__':
    for filename in os.listdir(directory):
        if is_image_file(filename):
            inputImage = cv2.imread(os.path.join(directory, filename))
            resized = resize(inputImage)
            filename = "re_" + filename[:-4] + ".jpg"
            cv2.imwrite(os.path.join(out_directory, filename), resized)
