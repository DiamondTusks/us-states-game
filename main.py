import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="What's another states name? ")).title()
    if answer_state == "Exit":
        # states_not_guessed = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_not_guessed.append(state)
        ## replaced lines above with 1 line below (list comprehension)
        states_not_guessed = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

