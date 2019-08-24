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

def thresh(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255

    return img

img = cv2.imread('imori.jpg', 1).astype(np.float32)

out = thresh(Gray(img))

cv2.imshow('result', out)
cv2.waitKey()
cv2.destroyAllWindows()
