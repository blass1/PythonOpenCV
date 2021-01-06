import cv2
import os

dataPath = 'G:/Developer/Conocimiento/Python/CV2/ReconocimientoFacial/Data'
imagePaths = os.listdir(dataPath)
print('dataPath= ', dataPath)
print('imagePaths= ', imagePaths)

# Creo un objeto EigenFaceRecognizer de opencv
face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Leo el modelo xml
face_recognizer.read('modeloEigenFace.xml')

# Capturo el video de Test que voy a utilizar
cap = cv2.VideoCapture('VideoTest/BlasTest0.mp4')
#cap = cv2.VideoCapture('VideoTest/AleTest0.mp4')
#cap = cv2.VideoCapture('VideoTest/AleTest2.avi')

# Detector de rostros, clasificador
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
	# Leo el cuadro(frame) y devuelve True si existe, sino salgo del ciclo
	ret, frame = cap.read()
	if ret == False: break
	# Transformo en escala de grises el frame
	grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = grayFrame.copy()

	faces = faceClassif.detectMultiScale(grayFrame, 1.3, 5)

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h, x:x+w]
		# Hay que redimensionar a 150x150 ya que usamos esa resolucion para entrenar el reconocedor de rostros
		rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
		# Predict, predice una etiqueta y la confianza asociada (por ejemplo, la distancia) para una imagen de entrada determinada
		result = face_recognizer.predict(rostro)

		cv2.putText(frame, f'Prdiccion: {result}', (x,y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
		
		# EigenFaces, los valores mas bajos o cercanos a 0 querra decir que el rostro a identificar tiene mucha similitud de los entrenados
		# En este metodo encontras valores de semejansa en los miles. El valor de 5700 no se aplica en todos los casos, depende de la BD con la que entrenes
		# Hay que experimentar y probar valores
		if result[1] < 5700:
			cv2.putText(frame, f'{imagePaths[result[0]]}', (x, y-25), 2, 1.1, (0,255,0), 1, cv2.LINE_AA)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
		else:
			cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0,0,255), 1, cv2.LINE_AA)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

	cv2.imshow('frame', frame)
	# Display a frame for 1 ms
	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()