import cv2

# Poner que camara estoy utilizando, 0 por ejemplo es la camara de la notebook
captura = cv2.VideoCapture(0)

# Con esto vamos a gragar nuestro video, primero el nombre, xx, framerate, tamanio
salida = cv2.VideoWriter('VideoSalido.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

# Mientras este ujsandose la camara
while(captura.isOpened()):
	# Devuelve 2 argumentos, una bool (cuando ya tenemos la imagen leida) y la imagen en si
	ret, imagen = captura.read()
	# Si tenemos una imagen vamos a visualizarla
	if ret==True:
		cv2.imshow('Video', imagen)
		# Guardamos la imaghen
		salida.write(imagen)
		# Cuando usemos una maquina de 64 bits usamos esto Y ORD es la tecla que usamos para deterner el procesamiento
		if cv2.waitKey(1) & 0xFF == ord('s'):
			break

captura.release()
# Finalizamos la grabacion
salida.release()
cv2.destroyAllWindows()
