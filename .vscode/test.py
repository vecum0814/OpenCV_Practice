import cv2

cap = cv2.VideoCapture('running.mp4')

while True:
    ret, img = cap.read()

    if ret == False:
        break

    cv2.imshow('result', img)

    if cv2.waitKey(1) == ord('q'):
        break
