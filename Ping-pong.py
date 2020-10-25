import turtle



#tela

tela = turtle.Screen()
tela.bgcolor("black")
tela.title("\ PING_PONG \ "* 4)
tela.setup(width=800, height=600)
tela.tracer(1)

#contagem dos pontos
player1 = 0
player2 = 0

#player1

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=5, stretch_len=1)
player.penup()
player.goto(-350,0)

#maquina
maquina = turtle.Turtle()
maquina.speed(0)
maquina.shape("square")
maquina.color("yellow")
maquina.shapesize(stretch_wid=5, stretch_len=1)
maquina.penup()
maquina.goto(350,0)

#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("blue")
bola.penup()
bola.goto(0, 0)
bola.dx = 2
bola.dy = -2

#pontos
pontos = turtle.Turtle()
pontos.speed(0)
pontos.color("green")
pontos.penup()
pontos.hideturtle()
pontos.goto(0, 260)
pontos.write("player 1: 0 player 2 : 0", align="center", font=("courier", 24, "normal"))



#comtrole player
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)
    if player.ycor()> 260 :
        player.sety(260)


def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)
    if player.ycor()< -260 :
        player.sety(-260)


def maquina_up():
    y = maquina.ycor()
    y += 20
    maquina.sety(y)
    if maquina.ycor()> 260 :
        maquina.sety(260)


def maquina_down():
    y = maquina.ycor()
    y -= 20
    maquina.sety(y)
    if maquina.ycor()< -260 :
        maquina.sety(-260)


tela.listen()
tela.onkeypress(player_up, "Up")
tela.onkeypress(player_down, "Down")
tela.onkeypress(maquina_up, "w")
tela.onkeypress(maquina_down, "s")

while True:
    tela.update()
    
    #move_bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #limite da bola
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        player1 += 1
        pontos.clear()
        pontos.write(f"player 1: {player1} player 2 : {player2}", align="center", font=("courier", 24, "normal"))

    if bola.xcor()< -390:
        bola.goto(0, 0)
        bola.dx *= -1
        player2 += 1
        pontos.clear()
        pontos.write(f"player 1: {player1} player 2 : {player2}", align="center", font=("courier", 24, "normal"))

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < maquina.ycor() + 50 and bola.ycor() > maquina.ycor() -50):
        bola.setx(340)
        bola.dx *= -1
    
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < player.ycor() + 50 and bola.ycor() > player.ycor() -50):
        bola.setx(-340)
        bola.dx *= -1
