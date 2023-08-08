import cv2
import os
import numpy as np

#el path de la imagen y imread para leer la imagen
img=cv2.imread("C:/Saul/fondos de pantalla/1.png")

img = cv2.resize(img, (500, 500))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("Imagen", img)
cv2.imshow("Image", imgGray)
cv2.waitKey(0)