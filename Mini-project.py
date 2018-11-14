import cv2
import numpy

#Load the source image
src = cv2.imread("lena.png")

rows, cols, c = src.shape
# x1 = x + y · Bx
# y1 = y + x · By
Bx = 0.0
By = 0.5

n = 1/(1-Bx*By)
#applying the forward mapping (shape = y-values, x-values, channel)
imgForward = numpy.ndarray(shape = (int (cols + rows*By), int (rows + cols*Bx), 3))
#shape should be equal to src.shape, then do np.pad (add extra room depending on the shearing factors)
imgBackward = numpy.ndarray(shape = (int (cols + rows*By), int (rows + cols*Bx), 3))

#for loops creating new sheared image (forward mapping)
for row in range(rows):
    for col in range(cols):
        imgForward[int (row+col*By), int(col+row*Bx)] = src[row,col]/255
        imgBackward[int (n*(row+col*-By)), int (n*(col+row*-Bx))] = src[row, col]/255

#1*3 array instead of 1*2 array
cv2.imshow("Forward mapping", imgForward)
cv2.imshow("Backward mapping", imgBackward)

cv2.waitKey(0)
