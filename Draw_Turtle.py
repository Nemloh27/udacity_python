import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square(some_turtle):

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    
    some_turtle.circle(100)

    
def draw_art():

    hector = turtle.Turtle()
    hector.shape("turtle")
    hector.speed(2)

    #rachel = turtle.Turtle()    
    #rachel.shape("arrow")
    #rachel.color("yellow")

    for i in range(1,37):
        draw_square(hector)
        hector.right(10)


draw_art()


window.exitonclick()
