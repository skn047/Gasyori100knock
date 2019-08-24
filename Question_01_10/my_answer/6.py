import cv2
import numpy as np

def DecColor(img):

    blue = img[..., 0].copy()
    green = img[..., 1].copy()
    red = img[..., 2].copy()

    for c in (blue, green, red):
        c[(c >= 0) & (c < 64)] = 32
        c[(c >= 64) & (c < 128)] = 96
        c[(c >= 128) & (c < 192)] = 160
        c[(c >= 192) & (c < 256)] = 224

    out = np.zeros_like(img)

    out[..., 0] = blue
    out[..., 1] = green
    out[..., 2] = red

    return out

img = cv2.imread('imori.jpg', 1)
out = DecColor(img)

cv2.imshow('result', out)
cv2.waitKey()
cv2.destroyAllWindows()
