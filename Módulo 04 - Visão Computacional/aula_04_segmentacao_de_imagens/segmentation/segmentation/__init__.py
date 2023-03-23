import cv2

cv2.imshow("ImShow", cv2.imread('./segmentation/img/watershed.jpg'))

cv2.waitKey(0)

cv2.destroyAllWindows()