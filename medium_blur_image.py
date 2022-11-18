import numpy as np

def medium_blur_image(img):
    img_width = img.shape[1]
    img_height = img.shape[0]
    mid_blur = np.zeros([img_height, img_width], dtype=np.uint8)

    members=[img[0,0]]*9
    for y in range(1,img.shape[0]-1):
        for x in range(1,img.shape[1]-1):
            members[0] = img[y-1,x-1]
            members[1] = img[y,x-1]
            members[2] = img[y+1,x-1]
            members[3] = img[y-1,x] 
            members[4] = img[y,x]
            members[5] = img[y+1,x]
            members[6] = img[y-1,x+1]
            members[7] = img[y,x+1]
            members[8] = img[y+1,x+1]

            members.sort()
            mid_blur[y,x]=members[4]
    return mid_blur