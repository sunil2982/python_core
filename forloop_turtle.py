import turtle
numsides = int(input("how many sides you want ??"))
tut=turtle.Turtle()
for step in range(numsides):
    tut.forward(step+100)
    tut.right(360/numsides)
    for step in range(numsides):
        tut.forward(step+70)
        tut.right(360/numsides)



turtle.done()