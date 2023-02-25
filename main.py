import turtle
import pandas

# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# data setup
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []

# main loop of the game
while len(guessed_states) != 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(
            title="Guess the state!", prompt="What is another state? ").title()
    else:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)}/50", prompt="What is another state? ").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

# Create a list with all the states not guessed
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)

states_to_learn = [
    state for state in all_states if state not in guessed_states]

learn = {
    "states": states_to_learn
}

stl = pandas.DataFrame(learn)
stl.to_csv("states_to_learn.csv")
