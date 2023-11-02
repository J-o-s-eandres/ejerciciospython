import cv2


clasificador = cv2.haarcascades + "haarcascade_frontalface_default.xtml"

face_cascade = cv2.CascadeClassifier(clasificador)


img = cv2.imread ("/img/cara.jpg")

faces = face_cascade.detectMultiScale(img)


for (x,y,w,h) in faces:
    img = cv2.rectangle (img,(x, y), (x + w, y + h),(255, 0, 0),2)


cv2.imshow("Deteccion Facial", img)

cv2.waitKey(0)