import numpy as np
import cv2
import pickle

img = cv2.imread('test_img.jpg')
data = cv2.CascadeClassifier('data.xml')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

font = cv2.FONT_HERSHEY_COMPLEX

file = open('weights.pkl','rb')
weights = pickle.load(file)

users = {0:"Ravi",1:"Unknown"}

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x,w):
    z = np.dot(x,w)
    return sigmoid(z)

face_comp = data.detectMultiScale(gray)
for x, y, w, h in face_comp:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 5)

    face = gray[y:y + h, x:x + w]
    face = cv2.resize(face, (50, 50))
    face = face/255.
    pred = round(predict(face.flatten(), weights))
    name = users[int(pred)]
    cv2.putText(img,name,(x,y),font,1,(0,255,255),2)

cv2.imwrite('test_result.jpg',img)