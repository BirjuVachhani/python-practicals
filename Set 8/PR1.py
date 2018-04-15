import turtle

p=turtle.Turtle()

def rec():
    p.forward(100)
    p.right(30)
    p.forward(100)
    p.right(150)
    p.forward(100)
    p.right(30)
    p.forward(100)
    p.right(150)

for i in range(36):
    rec()
    p.right(10)

turtle.exitOnClick()
