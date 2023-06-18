import random
import turtle 

tela = turtle.Screen()
tela.title("Pong Weezer por @JoaoAHaupt")
tela.bgcolor("#189bcc") #Blue Album 
tela.setup(width=1000, height=800)
tela.tracer(0)

# Taco 1
taco_1 = turtle.Turtle()
taco_1.speed(0)
taco_1.shape("square")
taco_1.color("black")
taco_1.shapesize(stretch_wid=5, stretch_len=1)
taco_1.penup() # Tira o marcador do turtle
taco_1.goto(-450, 0)

# Taco 2
taco_2 = turtle.Turtle()
taco_2.speed(0)
taco_2.shape("square")
taco_2.color("black")
taco_2.shapesize(stretch_wid=5, stretch_len=1)
taco_2.penup() # Tira o marcador do turtle
taco_2.goto(450, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup() # Tira o marcador do turtle
bola.goto(0, 0)
bola.dx = 0.25
bola.dy = -0.25


def taco_1_up():
    y = taco_1.ycor() #Retorna a cordenada de y
    y += 20
    taco_1.sety(y)


def taco_1_down():
    y = taco_1.ycor() #Retorna a cordenada de y
    y -= 20
    taco_1.sety(y)



tela.listen()
tela.onkeypress(taco_1_up, "w")
tela.onkeypress(taco_1_down, "s")




#Loop do jogo
while True:
    tela.update() 
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    if taco_1.ycor() > 350:
        taco_1.sety(350)
    if taco_1.ycor() < -350:
        taco_1.sety(-350)
    
    taco_2.sety(bola.ycor())
    if taco_2.ycor() > 350:
        taco_2.sety(350)
    if taco_2.ycor() < -350:
        taco_2.sety(-350)

    # bater na borda 
    if bola.ycor() > 400:
        bola.sety(400)
        bola.dy *= -1
    elif bola.ycor() < -400:
        bola.sety(-400)
        bola.dy *= -1
    
    if bola.xcor() > 500 or bola.xcor() < -500:
        bola.goto(0, 0)
        bola.dx *= -1

    if bola.xcor() > 450 and bola.xcor() > taco_2.xcor() and(bola.ycor() < taco_2.ycor() + 40 and bola.ycor() > taco_2.ycor() - 40): 
        bola.setx(450)
        bola.dx *= -1

    
    if bola.xcor() < -450 and (bola.ycor() < taco_1.ycor() + 40 and bola.ycor() > taco_1.ycor() - 40): 
        bola.setx(-450)
        bola.dx *= -1
    



    
    




