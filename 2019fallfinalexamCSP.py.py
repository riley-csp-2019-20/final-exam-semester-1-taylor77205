#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Taylor Smith
#Date
#12-19-19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries


#create turtle
import turtle as trtl

shape="arrow"
pen=trtl.Turtle(shape =shape)
pen.speed(0)
pen.color("blue")
position=0
pen.size=5 

#movement functions
def up():
    pen.setheading(90)
    pen.forward(10)

def down():
    pen.setheading(270)
    pen.forward(10)

def right():
    pen.setheading(00)
    pen.forward(10)

def left():
    pen.setheading(180)
    pen.forward(10)

#reset
def space():
     pen.up()
     pen.goto(0,0)
     pen.left(100)
     pen.position()
     
     pen.heading()

     pen.reset()
     pen.position()

     pen.heading()
     pen.speed(0)


#make pen bigger 
def letter_O():
    pen.pensize(15)

#make pen smaller
def letter_p():
    pen.pensize(2)

'''#pen up, pen down
def letter_u():
     True
     pen.pendown()
        pen.penup()
     True
     pen.up()
        pen.pendown()
'''
   
#color/drawing functions



#create screen
wn=trtl.Screen()
#bind to keypresses
wn.onkeypress(letter_O,"O")
wn.onkeypress(letter_p,"P")
#wn.onkeypress(letter_u,("U")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(space,"space")
#listen
wn.listen()

#mainloop
wn.mainloop()