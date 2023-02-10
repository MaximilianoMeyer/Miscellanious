#!/usr/bin/python
#coding: utf-8

import cv2
import requests
import pandas as pd

# Carrega a imagem
img = cv2.imread("image.jpg")

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem, verifique se o caminho está correto")
    exit()

# Calcula o hash da imagem para busca
img_hash = cv2.img_hash.PHash_create()
hash = img_hash.compute(img)
hash = str(hash[0])

# Faz a busca por referências da imagem no Google
try:
    response = requests.get(f"https://www.google.com/searchbyimage?image_url={hash}")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer requisição ao Google: {e}")
    exit()

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrai as referências da primeira página
    references = []
    for reference in response.text.split("<a href="):
        if "url?q=" in reference:
            references.append(reference.split("url?q=")[1].split("&sa=U&")[0])

    # Salva as referências em um arquivo CSV
    df = pd.DataFrame({"references": references})
    df.to_csv("referencias.csv", index=False)
else:
    print("Não foi possível encontrar resultados no Google")

# Extrai os metadados da imagem
metadata = {
    "shape": img.shape,
    "dtype": img.dtype
}

# Salva os metadados em um arquivo CSV
df = pd.DataFrame({"metadata": metadata})
df.to_csv("metadata.csv", index=False)
