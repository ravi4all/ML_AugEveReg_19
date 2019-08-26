import cv2

img = cv2.imread('img_1.jpg')
# print(img)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    cv2.imshow('result',img)
    cv2.rectangle(img,(250,100),(250+180,100+150),(0,255,255),5)
    cv2.putText(img,'MS Dhoni',(250,100),font,1,(0,0,0),2)
    if cv2.waitKey(10) == 27:
        break