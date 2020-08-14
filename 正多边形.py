import turtle
def draw_dbx(n):
    turtle.up()
    turtle.goto(-200,100)
    turtle.down()
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor("white")
    turtle.colors = ["black"]
    x = (n - 2) * 180 / n
    for i in range(n) :
        print("===aaa==")
        turtle.forward(100)
        turtle.right(180 - x)



draw_dbx(2)
draw_dbx(-2)
draw_dbx(-3)
draw_dbx(-4)
draw_dbx(-5)
draw_dbx(-6)
draw_dbx(-7)
draw_dbx(-8)
draw_dbx(-9)
draw_dbx(10)
draw_dbx(-11)
draw_dbx(-12)
















#input("请输入边数: ")




#n = 8














 
