from PIL import Image
from matplotlib import cm
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

from numpy.core.fromnumeric import mean


def compress(fileName):
    data = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)/255
    # test = np.arange(0, 100, 1).reshape((10, 10))
    # data = data[200:-200, 200:-200]
    arraySize = 28
    row = int(np.floor(data.shape[0]/arraySize))
    col = int(np.floor(data[0].shape[0]/arraySize))
    newData = np.zeros((arraySize, arraySize))
    for i in range(arraySize):
        for j in range(arraySize):
            newData[i, j] = np.sum(
                data[i*row:(i+1)*row, j*col:(j+1)*col])/(row*col)
    # plt.imshow(1-newData)
    # plt.colorbar()
    # plt.show()
    return 1-newData


# compress("shoe.jpg")
