import cv2
from cv2 import imshow

img = cv2.imread("Image-and-Video-Processing/galaxy.jpg", 1)


print(type(img))
print(img)
print(img.shape)
print(img.ndim)


cv2, imshow("Galaxy", img)

cv2.waitKey(9000)
cv2.destroyAllWindows()
