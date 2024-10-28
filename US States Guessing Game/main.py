import turtle
import pandas as pd
import string

screen = turtle.Screen()

screen.title("U.S States Game")
image = 'US States Game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv('US States Game/50_states.csv')

guessed_states = []
all_states = state_data["state"]

def plot_on_shape(chosen_state):
        state = state_data[state_data['state'] == chosen_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x),int(state.y))
        t.write(chosen_state)
        guessed_states.append(chosen_state)

while len(guessed_states) < 50:
    
    answer_state = string.capwords(screen.textinput(title= f"{len(guessed_states)}/50 Guessed Correct", prompt= "What is the state you are guessing?\nEnter State name or 'Exit' to leave: "))
    if answer_state == "Exit":
        break
    while answer_state not in state_data["state"].to_list() or answer_state in guessed_states:
        answer_state = string.capwords(screen.textinput(title= f"{len(guessed_states)}/50 Guessed Correct", prompt= "Incorrect choice! (Repeat or Invalid Entry)\nEnter a valid state or 'Exit' to leave: "))
        if answer_state == "Exit":
            break
    if answer_state == "Exit":
        break
    plot_on_shape(answer_state)


remaining_states = all_states[~all_states.isin(guessed_states)]

remaining_states.to_csv('US States Game/Remaining_states.csv', index=False)

print(f"Total remaining states: {len(remaining_states)}")

turtle.mainloop()