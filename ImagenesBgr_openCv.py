import cv2
import numpy as np

# El primer argumento "shape" que es el tamanio y la cantidad de dimensiones, Usamos 3 como son 3 colores RGB para formar un pixel
# Con numpy creamos una matriz de ceros de 300x300x3
bgr = np.zeros((600, 600, 3), dtype=np.uint8)

print(bgr)
bgr[:,:,:] = (255, 0, 190)
print(bgr)

cv2.imshow('RGB', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()