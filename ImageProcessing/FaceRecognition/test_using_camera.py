import cv2
import numpy as np
import pickle

dataset = cv2.CascadeClassifier('data.xml')
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX

file = open('weights.pkl','rb')
weights = pickle.load(file)

users = {0:"Ravi",1:"Unknown"}

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x,w):
    z = np.dot(x,w)
    return sigmoid(z)

while True:
    boolean, image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = dataset.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),5)
        # face = image[y:y + h, x:x + w, :]
        face = gray[y:y+h,x:x+w]
        face = cv2.resize(face, (50,50))
        face = face / 255.
        pred = round(predict(face.flatten(), weights))
        name = users[int(pred)]
        cv2.putText(image, name, (x, y), font, 1, (0, 255, 255), 2)

    # cv2.imshow('result',image)
    cv2.imshow('result', image)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()