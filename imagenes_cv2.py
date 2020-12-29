import cv2

# Con el segundo parametro en 1 es color, si lo pones en 0 es en escala de grises
imagen = cv2.imread('logo.png', 0)

# Muestra la imagen
cv2.imshow("Prueba", imagen)

# Guardar la imagen en formato de archivo con el nombre que queramos
cv2.imwrite('grises.jpg', imagen)

# Espera una determinada cantidad de segundos cuando se toca cualquier tecla, si esta 0 es eterno el tiempo
cv2.waitKey(0)

# Cerra todas las ventanas
cv2.destroyAllWindows()
