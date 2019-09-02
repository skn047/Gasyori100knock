import cv2

def BGR2RGB(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img

def Red(img):
    b = img[:, :, 0].copy() 
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    out = cv2.imread('out.jpg')
    
    # img[:, :, 0] = 0
    # img[:, :, 1] = 0
    # img[:, :, 2] = r

    img[img[:, :, 2] > 0][2] = out[img[:, :, 2] > 0][2]

    print(out.shape)
    a = img[:, :, 2] > 10
    b = img > 10

    return img
    
img_BGR = cv2.imread('imori.jpg')
img_RGB = BGR2RGB(img_BGR)
img_red = Red(img_BGR)

# cv2.imshow('result', img_RGB)
cv2.imwrite('red.png', img_red)
