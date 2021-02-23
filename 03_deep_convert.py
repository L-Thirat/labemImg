import cv2
import numpy as np


def empty(area):
    pass


# Create Control Bar
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("threshold_red", "Parameters", 248, 255, empty)
cv2.createTrackbar("threshold_green", "Parameters", 255, 255, empty)
cv2.createTrackbar("threshold_blue", "Parameters", 255, 255, empty)
cv2.createTrackbar("t_light", "Parameters", 80, 255, empty)
cv2.createTrackbar("t_contrast", "Parameters", 90, 255, empty)


def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf


from os import walk

mypath = "C:/Users/thirat/Documents/git/labelImg/dataset/HR/"
lst_filenames = []
for (_, _, filenames) in walk(mypath):
    for file in filenames:
        if ".jpg" in file:
            lst_filenames.append(file)

i = 0
while True:
    threshold_red = cv2.getTrackbarPos("threshold_red", "Parameters")
    threshold_green = cv2.getTrackbarPos("threshold_green", "Parameters")
    threshold_blue = cv2.getTrackbarPos("threshold_blue", "Parameters")
    t_contrast = cv2.getTrackbarPos("t_contrast", "Parameters")
    t_light = cv2.getTrackbarPos("t_light", "Parameters")

    frame = cv2.imread(mypath + lst_filenames[i])
    # Convert BGR to HSV
    hsv = apply_brightness_contrast(frame, t_light, t_contrast)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

    # define range of a color in HSV
    lower_hue = np.array([0, 0, 0])
    upper_hue = np.array([threshold_red, threshold_green, threshold_blue])

    # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsv, lower_hue, upper_hue)

    resized = cv2.resize(hsv, (640, 640), interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', resized)
    # cv2.imshow('mask', mask)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    cv2.imwrite(mypath + "/bw/80c90_" + lst_filenames[i], hsv)

    # elif k == ord('a'):
    #     # cv2.imwrite(mypath + "/mask/" + lst_filenames[i], mask)
    i += 1
