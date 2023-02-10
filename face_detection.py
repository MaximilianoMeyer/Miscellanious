#!/usr/bin/python
#coding: utf8

import cv2
import os

# Carregar o classificador de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Armazenar as imagens de referência
known_faces = []
known_names = []

# Carregar as imagens de referência
for name in os.listdir('faces'):
    for filename in os.listdir(f'faces/{name}'):
        image = cv2.imread(f'faces/{name}/{filename}')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(face) > 0:
            (x, y, w, h) = face[0]
            roi_gray = gray[y:y+h, x:x+w]
            known_faces.append(roi_gray)
            known_names.append(name)

# Carregar a imagem de entrada
input_img = cv2.imread('aline.jpg')
gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.3, 5)

# Verificar se há um rosto na imagem de entrada
if len(face) > 0:
    (x, y, w, h) = face[0]
    roi_gray = gray[y:y+h, x:x+w]
    # Comparar o rosto da imagem de entrada com as imagens de referência
    for known_face, known_name in zip(known_faces, known_names):
        result = cv2.matchTemplate(roi_gray, known_face, cv2.TM_CCOEFF_NORMED)
        if result >= 0.5:
            print(f'Acesso liberado para {known_name}')
            break
    else:
        print('Acesso negado')
else:
    print('Acesso negado')
