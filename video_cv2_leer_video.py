import cv2

# Nombre del video a leer
captura = cv2.VideoCapture('videoSalida.avi')

# Mientras este ujsandose la camara
while(captura.isOpened()):
	# Devuelve 2 argumentos, una bool (cuando ya tenemos la imagen leida) y la imagen en si
	ret, imagen = captura.read()
	# Si tenemos una imagen vamos a visualizarla
	if ret==True:
		cv2.imshow('Video', imagen)
		# Cuando usemos una maquina de 64 bits usamos esto Y ORD es la tecla que usamos para deterner el procesamiento
		if cv2.waitKey(30) & 0xFF == ord('s'):
			break
	else: break

captura.release()
cv2.destroyAllWindows()
