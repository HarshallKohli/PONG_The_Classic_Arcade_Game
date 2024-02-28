from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# TODO 1 : Creating the screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Game of Pong")
screen.tracer(0)

# TODO 2 : Creating the paddle

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))  # TODO 3: Creating another paddle
ball = Ball()              #TODO 4: Creating the ball and making it move
scoreboard= Scoreboard()   #TODO 8: The scoreboard

screen.listen()
screen.onkey(r_paddle.go_up, "Up")   #allowing movement of right and left paddle
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # TODO 5: Detecting collision with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #TODO 6: Detecting collision with the paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() >320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x() 

    #Detect when ball misses the right paddle
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when ball misses the left paddle
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
