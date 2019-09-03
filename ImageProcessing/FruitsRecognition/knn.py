import numpy as np
import cv2

data = np.load('data.npy')
labels = np.load('labels.npy')

data = data.reshape(data.shape[0], -1)

def dist(x1,x2):
    return np.sqrt(sum((x2 - x1)**2))

def knn(train,target,k=5):
    n = train.shape[0]
    distance = []
    for i in range(n):
        distance.append(train[i],target)

    distance = np.asarray(distance)
    sortedIndex = np.argsort(distance)
    lab = labels[sortedIndex][:k]
    arr,count = np.unique(lab,return_counts=True)
    return arr[np.argmax(count)]

cap = cv2.VideoCapture(0)

while True:
    boolean, image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # for x,y,w,h in faces:
    #     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),5)
    #     face = gray[y:y+h,x:x+w]
    #     face = cv2.resize(face, (50,50))
    #     face = face / 255.
    #     pred = knn(facesData, face.flatten())
    #     name = users[int(pred)]
    #     cv2.putText(image, name, (x, y), font, 1, (0, 255, 255), 2)

    # cv2.imshow('result',image)
    cv2.imshow('result', image)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()