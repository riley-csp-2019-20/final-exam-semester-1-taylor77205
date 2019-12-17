import turtle as trtl 

shape = "arrow"
player = trtl.Turtle(shape = shape)
player.speed(0)
player.penup()


shape = "circle"
circle = trtl.Turtle(shape = shape)
circle.penup()

def up():
    player.setheading(90)
    player.forward(10)
    circle.setheading(90)
    circle.forward(10)
    

def down():
    player.setheading(270)
    player.forward(10)
    circle.setheading(270)
    circle.forward(10)

def right():
    player.setheading(00)
    player.forward(10)
    circle.setheading(00)
    circle.forward(10)

def left():
    player.setheading(180)
    player.forward(10)
    circle.setheading(180)
    circle.forward(10)

wn=trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")

wn.listen()


wn.mainloop()