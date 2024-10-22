from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Racing")

replay_game = "yes"

while replay_game == "yes": 
    screen.clear()
    line_turtle = Turtle()
    line_turtle.penup()
    line_turtle.hideturtle()
    line_turtle.goto(220, -200)
    line_turtle.setheading(90)

    for _ in range(20):
        line_turtle.pendown()
        line_turtle.forward(10)
        line_turtle.penup()
        line_turtle.forward(10)

    turtle_number = screen.numinput(title = "Total Turtle count", prompt = "How many turtles would you like to race? Pick a number between 2 and 15.")
    while turtle_number not in range(2,16):
        turtle_number = screen.numinput(title = "Total turtle count", prompt = "Please enter a valid number between 2 and 15: ")

    turtle_list = []
    color_list = ['red', 'yellow', 'blue', 'pink', 'purple', 'orange', 'cyan', 'black', 'brown', 'green', 'magenta', 'gray', 'violet', 'turquoise', 'navy']
    assigned_colors = []

    for x in range(int(turtle_number)):
        new_turtle = Turtle(shape = "turtle")
        turtle_list.append(new_turtle)

    y = 180
    for x in turtle_list:
        random_color = random.choice(color_list)
        x.fillcolor(random_color)
        assigned_colors.append(random_color)
        color_list.remove(random_color)
        x.penup()
        x.goto(x=-220,y = y)
        y -= (400 - 40) / (len(turtle_list) - 1) 


    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? Enter a color:\n" + "\n".join(assigned_colors)
    ).lower()
    while user_bet not in assigned_colors:
        user_bet = screen.textinput(
            title="Invalid color choice",
            prompt=f"Enter a valid color:\n" + "\n".join(assigned_colors)
        ).lower()
        

    is_race_on = True

    while is_race_on:
        for turtle in turtle_list:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > 220:
                is_race_on = False
                winning_color = turtle.fillcolor()
                break  # End the for loop whe

    print(winning_color)

    if user_bet == winning_color:
        print(f"Congratulations, you have won the game. The color was indeed {winning_color}")
    else:
        print(f"You have lost the game. The winning turtle was {winning_color}")
        
    replay_game = screen.textinput(title = "Replay Game Option", prompt = "Would you like to replay the game? Enter 'Yes' or 'No': ").lower()
    while replay_game not in ['yes','no']:
        replay_game = screen.textinput(title = "Replay Game Option", prompt = "Invalid input. Enter 'Yes' or 'No': ").lower()
    

print("Thanks for playing!")

screen.exitonclick()