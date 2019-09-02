import cv2
import numpy as np
import os

path = 'fruitsImages'
imageLength = []
data = []
for root,folder,files in os.walk(path):
    imageLength.append(len(files))
    for file in files:
        imgPath = root + '/' + file
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        data.append(gray)

data = np.asarray(data)
data = data / 255

labels = np.zeros((len(data),1))
for i in range(len(imageLength) - 1):
    slice_1 = imageLength[i]
    slice_2 = imageLength[i+1] + slice_1
    labels[slice_1:slice_2] = float(i)

np.save('data.npy',data)
np.save('labels.npy',labels)
