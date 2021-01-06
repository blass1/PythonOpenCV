# Este archivo nos sirve para los 3 metodos, angenfaces, fisherfaces y lbph
import cv2
import os
import numpy as np

dataPath = 'G:/Developer/Conocimiento/Python/CV2/ReconocimientoFacial/Data'
# Listamos las carpetas dentro de data
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

# Tenemos que identificar cada rostro y poder vincular las imagenes (facesData) con las labels (0,1,2..)
labels = []
facesData = []
label = 0

# Todas las imaganes de la persona Blas tienen la etiqueta 0
# Ruta de los directorios con sus nombres donde se leearan las imagenes
for nameDir in peopleList:
	personPath = dataPath + "/" + nameDir
	print (f"Leyendo las imaganes del directorio {nameDir}")
	
	# Leemos cada uno de los rostros de cada de las personas, listdir es una lista de todos los archivos del directorio y la recorremos
	for fileName in os.listdir(personPath):
		print("Rostro: ", nameDir + "/" + fileName)
		# agrego un objeto "label" a la lista de etiquetas "labels" para identificar a quien pertenece cada imagen
		labels.append(label)
		# Con openvc leo el archivo imagen en escala de grises, osea"0" y lo agrego a la lista "facedata" donde se guardaran las imagenes
		facesData.append(cv2.imread(personPath + "/" + fileName, 0))
		image = cv2.imread(personPath + "/" + fileName, 0)
		# Muestro por pantalla la imagen actual
		#cv2.imshow('image', image)
		#cv2.waitKey(10)
	label = label + 1

#cv2.destroyAllWindows()

#print('labels = ', labels)
#print('Numnero de etiquetas 0: ', np.count_nonzero(np.array(labels)==0))
#print('Numnero de etiquetas 1: ', np.count_nonzero(np.array(labels)==1))

face_recognizer = cv2.face.FisherFaceRecognizer_create()


# Empezamos a entrenarlo con el array donde estan los rostros y las estiquetas de cada imagen
# El argumento de la funcion pide que sean numpys arrays
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Guardamos el modelo obtenido con con su nombre para poder usarlo en otro script y no tenerlo que volver a entrenar
# Puede ser XML o YAML
face_recognizer.write('modeloFisherFace.xml')
print("Modelo almacenado..")


