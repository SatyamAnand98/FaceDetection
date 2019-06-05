from __future__ import division
import cv2
import glob
img = cv2.imread("galaxy.jpg",1)
# images = glob.glob("*.jpg")
# for image in images:
#     imgs = cv2.imread(image,1)
#     res = cv2.resize(imgs,(100,100))
#     cv2.imshow("Hey",res)
#     cv2.waitKey(500)
#     cv2.destroyAllWindows()
#     cv2.imwrite("resized"+image,res)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
res = cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
cv2.imwrite("Galaxyresized.jpg",res)
cv2.imshow("Galaxy",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
