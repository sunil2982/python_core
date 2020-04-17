import turtle

obj=turtle.Turtle()

sides = int(input("how many sides of polygone you want to drow"))
print("do you want to  drow polygone into polygone?")

ans=input("yes or no?")
if  ans.upper() == "YES" :
    for steps in range(sides):
        obj.forward(100)
        obj.right(360/sides)
        for steps in range(sides):
            obj.forward(50)
            obj.right(360/sides)
else:
     for steps in range(sides):
        obj.forward(50)
        obj.right(360/sides)            
        

turtle.done()