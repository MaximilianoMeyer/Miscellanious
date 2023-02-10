#!/usr/bin/python
#coding: utf-8

import numpy as np
import pyautogui
import time

# Captura a tela do jogo e retorna o valor de pixel de uma determinada posição
def capture_screen(x, y):
    return np.mean(pyautogui.screenshot().getpixel((x, y)))

# Decide se o dino deve pular ou não
def decide(screen_value):
    if screen_value < 100:
        pyautogui.press("space")

# Inicia o jogo
print("Starting the game in 3 seconds...")
time.sleep(3)

# Executa o jogo indefinidamente
while True:
    # Captura o valor de pixel de uma posição específica da tela
    screen_value = capture_screen(100, 500)
    # Usa o valor de pixel para decidir se o dino deve pular ou não
    decide(screen_value)
