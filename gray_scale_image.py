import numpy as np

def gray_scale_image(img):
    img_width = img.shape[1]
    img_height = img.shape[0]

    img_gray = np.zeros([img_height, img_width], dtype=np.uint8)

    for y in range(img_height):
        for x in range(img_width):
            img_gray[y,x]=img[y,x,2]*0.3+img[y,x,1]*0.59+img[y,x,0]*0.11

    return img_gray