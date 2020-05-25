import cv2

img = cv2.imread("images/download.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow("Orig Image", img)
cv2.imshow("Grey Image", imgGray)
cv2.imshow("Blur Image", imgblur)
cv2.waitKey(0)
