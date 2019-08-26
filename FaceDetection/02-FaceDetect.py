import cv2

# Assertion error if system is unable to find xml file or image
dataset = cv2.CascadeClassifier('data.xml')

img = cv2.imread('bahubali.jpg')
faces = dataset.detectMultiScale(img)
# faces - it will have an array [[x,y,w,h]] of face
# print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)

while True:
    cv2.imshow('result',img)
    if cv2.waitKey(10) == 27:
        break