import numpy as np

def binary_scale_image(img, T):
    img_width = img.shape[1]
    img_height = img.shape[0]

    bin_img = np.zeros([img_height, img_width], dtype=np.uint8)
    for y in range(img_height):
        for x in range(img_width):
            if img[y,x] > T:
                bin_img[y,x] = 255
            else:
                bin_img[y,x] = 0

    return bin_img