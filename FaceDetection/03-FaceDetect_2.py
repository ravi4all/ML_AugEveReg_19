import cv2

# Assertion error if system is unable to find xml file or image
dataset = cv2.CascadeClassifier('data.xml')

images = ['img_0.jpg', 'img_1.jpg', 'img_2.jpg']

for i in range(len(images)):
    img = cv2.imread(images[i])

    faces = dataset.detectMultiScale(img,1.28)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 5)

    while True:
        cv2.imshow('result', img)
        if cv2.waitKey(10) == 27:
            break

    cv2.imwrite('resultImg_{}.jpg'.format(i),img)