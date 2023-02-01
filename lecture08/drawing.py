import turtle

def draw_square(fred: turtle.Turtle, length: int) -> None:
    fred.forward(length)
    fred.left(90)
    fred.forward(length)
    fred.left(90)
    fred.forward(length)
    fred.left(90)
    fred.forward(length)
    fred.left(90)

def main() -> None:
    bob = turtle.Turtle()
    cali = turtle.Turtle()
    draw_square(bob, 100)
    draw_square(cali, 200)
    draw_square(bob, 300)
    draw_square(bob, 400)
    turtle.done()

main()