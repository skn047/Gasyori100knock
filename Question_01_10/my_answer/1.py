import cv2

def BGR2RGB(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img

img_BGR = cv2.imread('imori.jpg')
img_RGB = BGR2RGB(img_BGR)

cv2.imshow('result', img_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
