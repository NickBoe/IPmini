import cv2
import math
import numpy as np


class Rotate:
    # Image import
    src = cv2.imread('lena.png', 0)
    rows, cols = src.shape

    # Show original/source image
    cv2.imshow('Original', src)

    # Rotation angle
    angle = 30
    q = angle * float(math.pi / 180)

    # Rotation point
    x = 256
    y = 56

    # Forward mapping function
    def forMap(img, x, y, q):

        rows, cols = img.shape
        imgForward = np.zeros(shape=(int(rows), int(cols)), dtype=np.uint8)

        for row in range(rows):
            for col in range(cols):
                fRow = int((col - x) * math.sin(q) + (row - y) * math.cos(q) + y)
                fCol = int((col - x) * math.cos(q) - (row - y) * math.sin(q) + x)

                if 0 < fRow < rows and 0 < fCol < cols:
                    imgForward[fRow, fCol] = img[row, col]
                else:
                    pass

        return imgForward

    # Show forward mapping
    ForMapping = forMap(src, x, y, q)
    cv2.imshow("Forward mapped", ForMapping)

    # Backward mapping function
    def backMap(self, img):

        imgBackward = np.zeros((self.rows, self.cols), dtype=np.uint8)

        for row in range(self.rows):
            for col in range(self.cols):
                bRow = int(-math.sin(self.q) * (col - self.x) + math.cos(self.q) * (row - self.y) + self.y)
                bCol = int(math.cos(self.q) * (col - self.x) + math.sin(self.q) * (row - self.y) + self.x)

                if 0 < bRow < self.rows and 0 < bCol < self.cols:
                    imgBackward[row, col] = self.src[bRow, bCol]
                else:
                    pass

        return imgBackward


# Show backward mapping
def output():
    cv2.imshow('Backward Mapping', Rotate.backMap(Rotate, Rotate))
    cv2.waitKey(0)
    cv2.destroyAllWindows


if __name__ == '__main__':
    output()
