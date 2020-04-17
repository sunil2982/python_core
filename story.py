#initializing variables
girlname = " "
boyname = " "
girl_desc = " "
boy_desc = " "
walk_desc =  " "
animal = " "
gift = " "
answer = " "

#taking input from user
girlname=input("enter a girl name")
girlname=girlname.capitalize()
boyname = input("input a boy name")
boyname = boyname.capitalize()
girl_desc= input("enter name of flower")
girl_desc =girl_desc.lower()
boy_desc = input("enter the type of boy")
boy_desc = boy_desc.lower()
walk_desc = input("enter how you dance ")
walk_desc =walk_desc.lower()
animal =input("enter the name of animal you have ride on")
animal = animal.lower()
answer = input("what would you say to some one who gives you car??")
answer = answer.lower()
gift = input("what  you want most")
gift = gift.lower()
    
# print("once upone  a time ")
# print("their is a girl whos name was {}".format(girlname)

#story printing
print("\nOnce upon a time,")
print("there was a girl named " + girlname + ".")
print("One day, " + girlname + " was walking like doing" + walk_desc + " down the street.")
print("Then she met a " + boy_desc + " boy named " + boyname + ".")
print("He said, 'You are really  beautiful like a" + girl_desc + "!'")
print("She said '" + answer + ", " + boyname + ".'")
print("Then they both rode away on a " + animal + " and lived happily ever after.")