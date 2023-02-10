#!/usr/bin/python
#coding: utf-8

import turtle
import time

# Definição das constantes
screen = turtle.Screen()
snake = turtle.Turtle()
food = turtle.Turtle()
snake.speed(0)
food.speed(0)
snake.shape("square")
food.shape("circle")
snake.color("green")
food.color("red")
snake.penup()
food.penup()

# Variáveis globais
speed = 20
snake_positions = []
food_spawned = False

# Função para gerar comida aleatória
def spawn_food():
    global food_spawned
    if not food_spawned:
        x = snake.xcor()
        y = snake.ycor()
        food.goto(x, y)
        food_spawned = True

# Função para movimentar a cobra
def move():
    global food_spawned
    snake.forward(speed)
    x = snake.xcor()
    y = snake.ycor()
    snake_positions.append((x, y))
    if food_spawned and snake.distance(food) < 20:
        food_spawned = False
    else:
        snake.clearstamps(1)
        snake_positions.pop(0)
    for i, pos in enumerate(snake_positions):
        snake.goto(pos)
        snake.stamp()

# Função para mudar a direção da cobra
def change_direction(x, y):
    snake.setheading(snake.towards(x, y))

# Ligação dos eventos
screen.listen()
screen.onkeypress(lambda: change_direction(food.xcor(), food.ycor()), "Up")

# Loop do jogo
while True:
    screen.update()
    spawn_food()
    move()
    time.sleep(0.2)
