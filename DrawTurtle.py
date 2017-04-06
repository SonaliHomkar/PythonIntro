import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    # draw a circle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(1,37):
        draw_square(brad)    
        brad.right(10)
    
    brad.right(90)
    brad.forward(200)
    # draw a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("red")
    #angie.circle(100)


    #draw triangle
    

    window.exitonclick()

draw_art()
