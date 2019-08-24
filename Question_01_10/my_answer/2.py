import cv2
import numpy as np

def Gray(img):

    blue = img[:, :, 0]
    green = img[:, :, 1]
    red = img[:, :, 2]

    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue

    img[:, :, 0] = y
    img[:, :, 1] = y
    img[:, :, 2] = y

    return img

img_org = cv2.imread('imori.jpg', 1)
img_gray = Gray(img_org)

cv2.imshow('result', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
