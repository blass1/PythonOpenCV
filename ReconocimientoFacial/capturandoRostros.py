import cv2
import os
import imutils

personName = 'Ana'
dataPath = 'G:/Developer/Conocimiento/Python/CV2/ReconocimientoFacial/Data'
personPath = dataPath + '/' + personName

# En caso de que no exista la carpeta se crea automaticamente
if not os.path.exists(personPath):
	print('Carpeta creada: ', personPath)
	os.makedirs(personPath)

archivoConExtension = personName + '.avi'

# Este es el video donde vamos a extraer los rostros
cap = cv2.VideoCapture(archivoConExtension)

# O con video styreaming
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
	# Devuelve 2 argumentos, ret true si existe la lectura del arhivo y el cuadro
	ret, frame = cap.read()
	# Si no existe termina
	if ret == False: break
	# Redimensiona el cuadro
	frame = imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
		rostro = auxFrame[y:y+h, x:x+w]
		rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)
		count = count + 1
	cv2.imshow('frame', frame)

	k = cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

cap.release()
cv2.destroyAllWindows()