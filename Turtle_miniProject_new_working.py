import turtle

def draw_triangle(some_turtle,length):
    for i in range(1,4):
       some_turtle.forward(length)
       some_turtle.right(120)
       
      

def draw_inner_triangle(brad,trilen):
    brad.forward(trilen/2)
    brad.right(60)
    brad.forward(trilen/4)
    brad.left(120)
    brad.begin_fill()
    draw_triangle(brad,trilen/4)
    brad.end_fill()


    for i in range(1,3):
        brad.right(120)
        brad.forward(trilen/4)

        brad.right(120)
        brad.forward(trilen/4)

        brad.left(120)
        brad.begin_fill()
        draw_triangle(brad,trilen/4)
        brad.end_fill()


    brad.right(120)
    brad.forward(trilen/4)

    brad.right(60)
    brad.forward(trilen/2)

window = turtle.Screen()
    
                            
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("red")
brad.speed(2)



trilen = 150
# 1st triangle
brad.left(60)
draw_triangle(brad,trilen)
draw_inner_triangle(brad,trilen)

# 2nd triangle
draw_triangle(brad,trilen)
draw_inner_triangle(brad,trilen)
# 3rd triangle
brad.backward(trilen*2)
brad.right(60)
brad.forward(trilen)

brad.left(60)
draw_triangle(brad,trilen)
draw_inner_triangle(brad,trilen)

window.exitonclick()
