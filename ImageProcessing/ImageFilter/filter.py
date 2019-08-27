import cv2

dataset = cv2.CascadeClassifier('data.xml')

cap = cv2.VideoCapture(0)
mask = cv2.imread('mask_1.png')
while True:
    boolean, image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = dataset.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),5)

        face = image[y:y+h,x:x+w,:]
        mask = cv2.resize(mask,(face.shape[0],face.shape[1]))
        image[y:y + h, x:x + w, :] = mask

    # cv2.imshow('result',image)
    cv2.imshow('result', image)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()