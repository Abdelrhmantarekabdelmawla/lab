import cv2

im1 = cv2.imread("elephant.jpg")
im1 = cv2.resize(im1, (1280,720))
cv2.imshow("ele", im1)
cv2.waitKey(0)
cv2.imwrite("resized.png",im1)