str = "she is a good girl"
print(str.replace(" ","_"))
print(str.find("is"))

#find method
string = "she is a good girl and is beautiful"
a = int(string.find("is"))
print(string.find("is", a+1)) 

#center method results in output "**  **"
name = "Ayushi"
print(name.center(10,"*"))   #len(name)=6 + 2(number of asterics we want to put in)

name = input("Enter your name: ")
print(name.center(len(name)+4,"*"))  # 4 bcz we want to add 2(*) on both sides 

# string are immutable in python
string = "string"
a = string.replace('t','T')
print(a)
print(string)
#assignment operators
name = "harsh"
name += "it"          (name = name + "it")
print(name)
age  = 23
age*= 2
print(age)

#conditional statements
age = int(input("Enter your age: "))
if age>= 14:
    print("you are eligible")

#pass is used when u do not want to add anything in your block
a = int(input("enter: "))
if a >=12:
    pass

#if-else statements
a = int(input("enter: "))
if a >=12:
    print("play")
else:
    print("sorry") 

import random
winning_number = random.randint(1,100)
guess = int(input("guess your number: "))
print(f"winning number is :{winning_number}")
if guess == winning_number:
    print("YOU WIN !!!")
elif guess >= winning_number :
    print("too high")
else:
    print("too low")    

#and/or operator
name = 'abc'
age = 19
if name == 'abc' and age == 19:
    print("true")
else:
    print("false")    

name = 'abc'
age = 19
if name == 'abc' or age == 23:
    print("true")
else:
    print("false")   

#Exercise 1
print("MOVIE-COCO")
name, age = input("Enter your name and age comma separated: ").split(",")
age = int(age)
if (name[0]=='A' or name[0]=='a') and age > 19:
    print("You can watch coco")
else:
    print("Sorry, you can't watch coco")              