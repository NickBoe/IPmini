import cv2
import numpy

src = cv2.imread("lena.png", 0)

#Forward mapping method
def forMap (img, Bx, By):
    rows, cols = img.shape
    #Canvas ensuring correct window size
    imgForward = numpy.ndarray(shape = (int (rows + cols*abs(By)), int (cols + rows*abs(Bx))))

    #For loops to go through all rows and collums
    for row in range(rows):
        for col in range(cols):
            #Apply the forward mapping algorithm
            fCol = int (col+row*Bx)
            fRow = int (row+col*By)
            imgForward[fRow, fCol] = img[row,col]/255

    return imgForward

#Backward mapping method
def backMap (img, Bx, By):
    rows, cols = img.shape
    #Canvas ensuring correct window size in accordance to the img.shape parameters
    imgBackward = numpy.ndarray(shape = img.shape)
    n = int(1/(1-Bx*By))

    #For loops to go through all rows and collums
    for row in range(rows):
        for col in range(cols):
            #Apply the backward mapping algorithm
            bCol = int(n*(col+row*-Bx))
            bRow = int(n*(row+col*-By))
            imgBackward[bRow, bCol] = img[row, col]

    return imgBackward

#Shearing factors
Bx = 0.3
By = 0.2

ForMapping = forMap(src, Bx, By)
BackMapping = backMap(ForMapping, Bx, By)

cv2.imshow("Original", src)
cv2.imshow("Forward mapped", ForMapping)
cv2.imshow("Backward mapped", BackMapping)

cv2.waitKey(0)