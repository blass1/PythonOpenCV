import cv2
import numpy as np

# Leo la imagen
bgr = cv2.imread("bgr_imagen.jpg")

# Separo la imagen en 3 canales de colores en forma de listas

canal1 = bgr[:,:,0]
canal2 = bgr[:,:,1]
canal3 = bgr[:,:,2]

# Las muestro separadas por canales
cv2.imshow('BGR', np.hstack([canal1,canal2,canal3]))

# Convierto de BGR a RGB
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

canal1 = rgb[:,:,0]
canal2 = rgb[:,:,1]
canal3 = rgb[:,:,2]

# Las muestro separadas por canales
cv2.imshow('RGB', np.hstack([canal1,canal2,canal3]))

cv2.waitKey(0)
cv2.destroyAllWindows()