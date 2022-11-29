#string formatting python3
#{} - placeholders sign
# name = "Ayushi"
# age = 20
print("hello "+ name +" your age  is " + str(age))   #python 2
print("Hello {} your age is {}".format(name,age))  #python 3
print(f"Hello {name} your age is {age+2}")         #python 3.6

#Exercise
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
avg = (a+b+c)/3
print(f"average of {a},{b},{c} is {avg}")  #or

a,b,c =input("Enter first number, enter 2 number,enter 3 number comma separated: ").split(",")
print(f"average of three numbers is : {(int(a)+int(b)+int(c))/3}")

#string indexing:
# a = " "
# if you don't know the length of your string and want to print the last character - print([-1])

#strinf slicing(select sub sequences)
a  "python"
print(a[0:2])  # output-(py )stop argument always taken as -1  

#step argument
print("ayushi"[0::-1])