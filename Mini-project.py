import cv2
import math
import numpy as np

class Rotate:
    #Image import
    src = cv2.imread('lena.png', 0)
    rows, cols = src.shape

    #Rotation angle in radians
    angle = 22.5
    rad = angle * float(math.pi / 180)

    # Rotation point
    x = 50
    y = 40

    # Forward mapping function
    def forMap(self, x, y, rad):

        rows, cols = self.shape
        imgForward = np.zeros(shape=(int(rows), int(cols)), dtype=np.uint8)

        for row in range(rows):
            for col in range(cols):
                fCol = int(((col - x) * math.cos(rad)) - ((row - y) * math.sin(rad)) + x)
                fRow = int(((col - x) * math.sin(rad)) + ((row - y) * math.cos(rad)) + y)

                if fCol < cols and fRow < rows and fCol > 0 and fRow > 0:
                    imgForward[fRow, fCol] = self[row, col]
                else:
                    pass

        return imgForward

    ForMapping = forMap(src, x, y, rad)
    cv2.imshow("Forward mapped", ForMapping)

    # Backward mapping function
    def backMap(self, img):

        imgBackward = np.zeros((self.rows, self.cols), dtype=np.uint8)

        for row in range(self.rows):
            for col in range(self.cols):
                bCol = int(((col - self.x) * math.cos(self.rad) + (row - self.y) * math.sin(self.rad))+self.x)
                bRow = int((-(col - self.x) * math.sin(self.rad) + (row - self.y) * math.cos(self.rad))+self.y)

                if bCol < self.cols and bRow < self.rows and bCol > 0 and bRow > 0:
                    imgBackward[row, col] = self.src[bRow, bCol]
                else:
                    pass

        return imgBackward

    def showImage(name, self):
        cv2.imshow(name, self.src)

def output():
    Rotate.showImage('Original', Rotate)
    cv2.imshow('Backward Mapping', Rotate.backMap(Rotate, Rotate))
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    output()
