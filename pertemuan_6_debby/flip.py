import cv2

img = cv2.imread('20.jpg')

flip_img = cv2.flip(img, 1)

cv2.imshow('Original Photo', img)
cv2.imshow('Flip Photo', flip_img)
cv2.waitKey(0)
cv2.destroyAllWindows()