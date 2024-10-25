from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
from high_score_manager import HighScoreManager


score_manager = HighScoreManager('Snake Game/high_score.txt')
maximum_score = score_manager.get_max_score()


replay_game = 'yes'
while replay_game == 'yes':
    screen = Screen()
    screen.clear()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()

    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food) < 20:
            score.increase_score()
            food.refresh()
            snake.extend()
        if snake.head.xcor()> 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
        
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                
        if score.counter > maximum_score:    
            with open("Snake Game/high_score.txt", 'a') as file:  
                file.write(f"{score.counter}\n")
            maximum_score = score.counter
            score.high_score = maximum_score
            score.update_scoreboard()
    
    replay_game = screen.textinput("Replay the game", f"Game over! Your final score is {score.counter}\nYour highest score is {maximum_score}\nWould you like to replay the game? Enter 'yes' or 'no': ").lower()
    while replay_game not in ['yes','no']:
        replay_game = screen.textinput("Invalid Replay Input","Invalid input. Enter 'yes' or 'no': ").lower()
    
screen.exitonclick()
