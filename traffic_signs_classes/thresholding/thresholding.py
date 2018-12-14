import cv2;
import numpy as np;

im_in = cv2.imread("12.jpg", cv2.IMREAD_GRAYSCALE);
imagem = cv2.imread("arte1.jpg", cv2.IMREAD_GRAYSCALE);
 
th, im_th = cv2.threshold(im_in, 50, 255, cv2.THRESH_BINARY);


# Create new image
new_image = cv2.bitwise_and(imagem,im_th)

cv2.imshow("Thresholded Image", new_image)
cv2.waitKey(0)
