import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
# For each person, enter one numeric face id
# face_id = input('\n Enter user ID end press <Enter> ==>  ')
print("\n Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0


def empty(area):
    pass


# Create Control Bar
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 42, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)
cv2.createTrackbar("t_contrast", "Parameters", 0, 127, empty)
cv2.createTrackbar("Area", "Parameters", 100, 60000, empty)


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


while (True):
    ret, img = cam.read()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # count += 1
    # Save the captured image into the datasets folder
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    t_contrast = cv2.getTrackbarPos("t_contrast", "Parameters")

    img = apply_brightness_contrast(img, 0, t_contrast)
    # contour
    # imgContour = img.copy()
    # imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    # imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    # imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    # kernel = np.ones((5, 5))
    # imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    # big_imgCanny = cv2.Canny(imgGray, 42, 80)  # phone 42
    # big_imgDil = cv2.dilate(big_imgCanny, kernel, iterations=1)

    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    # SNAP = input('\n Capture <Enter> ==>  %s' % count)

    if k == 27:
        break
    elif k == ord('a'):
        count += 1
        cv2.imwrite("dataset/Image" + str(count) + ".jpg", img)
        print("SNAP %d" %count)
    elif count >= 150:  # Take 30 face sample and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
