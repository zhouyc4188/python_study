import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray","brown","pink","light blue"]
for n in range(500):
    t.pencolor(random.choice(colors))
    size = random.randint(20,40)
    x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90) 
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size): 
        t.forward(m*2)
        t.left(90)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90) 
