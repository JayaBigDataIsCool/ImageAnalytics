import cv2

capvid = cv2.VideoCapture("images/somg.mp4")

while True:
    success, img = capvid.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break