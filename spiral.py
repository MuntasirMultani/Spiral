from turtle import Turtle, Screen

# Set up the screen
s = Screen()
s.bgcolor("white")
s.title("More than just a circle")

# Create a turtle object
sketch_pen = Turtle()
sketch_pen.pencolor("red")
sketch_pen.speed("fastest")
sketch_pen.pensize(1)

# Initialize length and angle
length, angle = 0, 0

# Move the turtle to the starting position
sketch_pen.penup()
sketch_pen.goto(0, 200)
sketch_pen.pendown()

# Draw a spiral pattern
while True:
    sketch_pen.forward(length)
    sketch_pen.right(angle)
    length += 1
    angle += 2

    # Exit condition
    if angle == 270:
        break

# Hide the turtle cursor after drawing
sketch_pen.hideturtle()

# Wait for user click to exit
s.exitonclick()