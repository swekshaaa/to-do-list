import turtle
tasks = []

screen = turtle.Screen()
screen.title("To-Do List")
screen.bgcolor("lightpink")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-250, 250)
def gettask():
    task = screen.textinput("New Task", "Enter your task:")
    if task:
        tasks.append(task)
        updatetasks()
def updatetasks():
    pen.clear()
    pen.goto(-250, 250)
    for i, task in enumerate(tasks):
        pen.write(f"{i+1}. {task}", font=("Arial", 12))
        pen.goto(-250, 250 - (i + 1) * 30)
def drawbutton():
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(200, -250)
    button.pendown()
    button.fillcolor("green")
    button.begin_fill()
    for a in range(2):
        button.forward(100)
        button.left(90)
        button.forward(50)
        button.left(90)
    button.end_fill()
    button.penup()
    button.goto(250, -235)
    button.color("white")
    button.write("Add Task", align="center", font=("Arial", 11, "bold"))

def clickhandler(x, y):
    if 200 < x < 300 and -250 < y < -200:
        gettask()
drawbutton()
screen.onclick(clickhandler)
screen.mainloop()
