# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Xsize = 1920
Ysize = 1080
CTUsize = 64

import numpy as np
import cv2
import math

filePath = r'/home/zxc/TC/GX010016_1646223722211.txt'
timeList = []
levelList = []
level = 1;
lastFrame = 0;
lastY = 0;
ti = np.zeros([math.ceil(Xsize / CTUsize), math.ceil(Ysize / CTUsize)], dtype=np.uint8)
li = np.zeros([math.ceil(Xsize / CTUsize), math.ceil(Ysize / CTUsize)], dtype=np.uint8)
for line in open(filePath):

    line = line.strip('\n')
    line = line.split(' ')

    [frameNum, x, y, time] = map(int, line)
    x = int(x / CTUsize)
    y = int(y / CTUsize)
    if frameNum > lastFrame:
        lastFrame = frameNum
        lastY = 0
        timeList.append(ti)
        levelList.append(li)
        level = 1
        ti = np.zeros([math.ceil(Xsize / CTUsize), math.ceil(Ysize / CTUsize)], dtype=int)
        li = np.zeros([math.ceil(Xsize / CTUsize), math.ceil(Ysize / CTUsize)], dtype=int)

    elif y < lastY:

        level = level + 1

    ti[x, y] = time
    li[x, y] = level
    lastY = y
    lastFrame = frameNum
