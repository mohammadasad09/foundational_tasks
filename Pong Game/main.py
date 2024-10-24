from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor('black')
screen.setup(width = 800,height = 600)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

game_ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(left_paddle.move_up, "a")
screen.onkey(left_paddle.move_down,"s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down,"Down")



game_is_on = True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()
    
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    
    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()
    
    if game_ball.xcor() > 380:
        game_ball.reset_position()
        scoreboard.l_point()
        
        
    if game_ball.xcor() < -380:
        game_ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()