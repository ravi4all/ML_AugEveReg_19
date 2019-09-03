import numpy as np
import cv2

dataset = cv2.CascadeClassifier('data.xml')

face_1 = np.load('face_1.npy')
face_2 = np.load('face_2.npy')

face_1 = face_1.reshape(200,-1)
face_2 = face_2.reshape(200,-1)

facesData = np.concatenate([face_1,face_2])

font = cv2.FONT_HERSHEY_COMPLEX

users = {0:"Ravi",1:"Unknown"}

labels = np.zeros((len(facesData),1))
labels[200:,:] = 1.0

# print(facesData.shape,labels.shape)

def dist(x1,x2):
    return np.sqrt(sum((x2 - x1)**2))

def knn(train,target,k=5):
    n = train.shape[0]
    distance = []
    for i in range(n):
        distance.append(dist(train[i],target))

    distance = np.asarray(distance)
    sortedIndex = np.argsort(distance)
    print(distance.shape,sortedIndex)
    lab = labels[sortedIndex][:k]
    arr,count = np.unique(lab,return_counts=True)
    return arr[np.argmax(count)]

cap = cv2.VideoCapture(0)

while True:
    boolean, image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = dataset.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),5)
        face = gray[y:y+h,x:x+w]
        face = cv2.resize(face, (50,50))
        face = face / 255.
        # print(face.flatten().shape)
        pred = knn(facesData, face.flatten())
        name = users[int(pred)]
        cv2.putText(image, name, (x, y), font, 1, (0, 255, 255), 2)

    # cv2.imshow('result',image)
    cv2.imshow('result', image)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
