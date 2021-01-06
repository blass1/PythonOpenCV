import cv2
import numpy as np

# Leo la imagen
bgr = cv2.imread("bgr_imagen.jpg")

# Convierto de BGR a RGB
gris = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Las muestro separadas por canales
cv2.imshow('GRISES', gris)

cv2.waitKey(0)
cv2.destroyAllWindows()