import turtle

def draw_rectangle(some_turtle,length):
    for i in range(1,4):
        some_turtle.forward(length)
        some_turtle.right(120)

def draw_rectangle_first(some_turtle,length):
    for i in range(1,4):
        some_turtle.forward(length)
        some_turtle.left(120)
        

window = turtle.Screen()
    
                            
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("green")
brad.speed(2)

#brad.begin_fill()
draw_rectangle_first(brad,300)
#brad.end_fill()




brad.forward(150)
brad.left(120)
brad.color("red")
draw_rectangle(brad,150)


brad.forward(75)
brad.left(120)
brad.color("blue")
draw_rectangle(brad,75)

brad.forward(37.5)
brad.left(120)
brad.color("red")
draw_rectangle(brad,37.5)




brad.right(120)
brad.forward(37.5)
brad.color("blue")
brad.right(120)
brad.forward(37.5)
brad.left(120)
brad.color("red")
draw_rectangle(brad,37.5)



window.exitonclick()
