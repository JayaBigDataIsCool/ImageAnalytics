import cv2

capvid = cv2.VideoCapture(0)

capvid.set(3, 640)
capvid.set(4, 480)

while True:
    success, img = capvid.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
