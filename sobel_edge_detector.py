import numpy as np
from math import sqrt

def sobel(img):
	img_width = img.shape[1]
	img_height = img.shape[0]
	kernel_mat=(np.array([[-1,-2,-1],[0,0,0],[1,2,1]]))

	img2 = img.copy()
	img3 = img.copy()

	for i in range(1,img_height-1):
		for j in range(1,img_width-1):
			x=img2[i+1,j-1]*kernel_mat[2,0]+img2[i+1,j]*kernel_mat[2,1]+img2[i+1,j+1]*kernel_mat[2,2]+(img2[i-1,j-1]*kernel_mat[0,0]+img2[i-1,j]*kernel_mat[0,1]+img2[i-1,j+1]*kernel_mat[0,2])

			y=(img2[i-1,j+1]*kernel_mat[0,0]+img2[i,j+1]*kernel_mat[0,1]+img2[i+1,j+1]*kernel_mat[0,2])+(img2[i-1,j-1]*kernel_mat[2,0]+img2[i,j-1]*kernel_mat[2,1]+img2[i+1,j-1]*kernel_mat[2,2])

			img3[i-1,j-1]=sqrt(x**2+y**2)
	return img3
