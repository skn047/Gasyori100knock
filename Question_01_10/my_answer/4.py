import cv2
import numpy as np

def otsu(img):
    best_th = 0
    max_value = 0

    for th in range(256):
        w1 = 0
        w2 = 0
        m1 = 0
        m2 = 0

        for w in range(img.shape[0]):
            for h in range(img.shape[1]):
                if img[w][h][0] < th:
                    w1 += 1
                    m1 += img[w][h][0]
                elif img[w][h][0] >= th:
                    w2 += 1
p                    m2 += img[w][h][0]

        if w1 > 0 and w2 > 0:
            m1 = int(m1 / w1)
            m2 = int(m2 / w2)
            value = w1 * w2 * (m1-m2) * (m1-m2)

            if value > max_value:
                max_value = value
                best_th = th

    print(best_th)
    return best_th

def thresh(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255

    return img

def Gray(img):

    blue = img[:, :, 0]
    green = img[:, :, 1]
    red = img[:, :, 2]

    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue

    img[:, :, 0] = y
    img[:, :, 1] = y
    img[:, :, 2] = y

    return img

img = cv2.imread("imori.jpg", 1).astype(np.float32)
th = otsu(Gray(img))
out = thresh(Gray(img), th=th)

cv2.imshow('result', out)
cv2.waitKey()
cv2.destroyAllWindows()
