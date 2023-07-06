import cv2

# read image
img = cv2.imread ('48.jpg')
kok = 255
# perform negation
img_neg = kok - img

# show original and negated images side by side
cv2.imshow("Original Image", img)
cv2.imshow("Negated Image", img_neg)
cv2.waitKey(0)