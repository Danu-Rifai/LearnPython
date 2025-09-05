import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("cyan")

# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.speed(3)

# Draw a heart shape
my_turtle.begin_fill()

my_turtle.left(50)
my_turtle.forward(133)
my_turtle.circle(50, 200)  # Draw the left half of the heart
my_turtle.right(140)
my_turtle.circle(50, 200)  # Draw the right half of the heart
my_turtle.forward(133)

my_turtle.end_fill()

# Hide the turtle after drawing
my_turtle.hideturtle()

# Wait for a click to close the window
screen.exitonclick()
