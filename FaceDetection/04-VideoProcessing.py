import cv2

dataset = cv2.CascadeClassifier('data.xml')
video = cv2.VideoCapture('video_1.mp4')

while True:
    boolean, frames = video.read()
    frames = cv2.resize(frames,None,None,0.5,0.5)
    if boolean:
        faces = dataset.detectMultiScale(frames)
        for x, y, w, h in faces:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 255), 5)
        cv2.imshow('result',frames)
        if cv2.waitKey(10) == 27:
            break

cv2.destroyAllWindows()