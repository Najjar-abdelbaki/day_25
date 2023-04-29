import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
screen = turtle.Screen()
screen.title("U . S . GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

guss_state =[]

while len(guss_state) < 50:

    answer = screen.textinput(f"{len(guss_state)}/50 states correct", "what's another state's name")
    answer = answer.title()

    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guss_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing.txt")
        break

    if answer in states:
        x = data[data.state == answer]

        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(x.x), int(x.y))
        tim.write(answer)
        guss_state.append(answer)

