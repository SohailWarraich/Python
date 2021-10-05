import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt

min_HSV = np.array([0, 58, 30], dtype = "uint8")
max_HSV = np.array([33, 255, 255], dtype = "uint8")
# Get pointer to video frames from primary device
image = cv2.imread("D:/Python GIT/Python/rock_climbing.jpg")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)

skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)
maskImage=np.hstack([image,skinHSV])
cv2.imshow("Orignal_Image",image)
cv2.imshow("Mask_image",skinHSV)


# cv2.imwrite("D:/Python GIT/Python/rock_hsv.jpg", np.hstack([image, skinHSV]))

cv2.waitKey(0)
cv2.destroyAllWindows()
