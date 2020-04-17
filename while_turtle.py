import turtle

obj = turtle.Turtle()
lineLenght = 0
penColor ="black"
lineAngle=0
# counter= 0
# lineLenght=int(input("how long line you want to drow?, Enter 0 to end this"))
# penColor=input('what color of pen you want to use "red","blue","black","green" ??')
# lineAngle=int(input("what angle  you want to drow line:(0-360)"))
lineLenght=int(input("how long line you want to drow?, Enter 0 to end this"))
penColor=input('what color of pen you want to use "red","blue","black","green" ??')
lineAngle=int(input("what angle  you want to drow line:(0-360)"))

while lineLenght != 0:
    
    obj.forward(lineLenght)
    obj.pencolor(penColor)
    obj.right(lineAngle)

    lineLenght=int(input("how long line you want to drow?, Enter 0 to end this"))

    if lineLenght !=0:
        penColor=input('what color of pen you want to use "red","blue","black","green" ??')
        lineAngle=int(input("what angle  you want to drow line:(0-360)"))

print("good job")


turtle.done()