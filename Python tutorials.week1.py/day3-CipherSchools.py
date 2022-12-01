#string formatting python3
#{} - placeholders sign
name = "Ayushi"
age = 20
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
a ="python"
print(a[0:2])  # output-(py )stop argument always taken as -1  

#step argument
print("ayushi"[0::-1])

#Exercise
name = input("Enter name: ")
reverse = name[-1::-1]
print(f"reverse of the number is {reverse}")

#string methods
a = "AyUSHi BhuTAnI"
print(a.upper())
print(len(a))
print(a.lower())
print(a.title())
print(a.count("A"))   #count() is used for case sensitive cases

#Exercise
name, char = input("Enter your name, a single character comma separated: ").split(",")
name = name.lower()
char = char.lower()
print(f"length of your name is {len(name)}")      #if user enter character after comma providing space it will not guve correct output 
print(f"character count: {name.count(char)}")

#strip method
name = "   Ayushi   "
dots = ".............."
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
print(name.replace(" ", "") + dots)    
# one more way :
"  Harshit  " (space removal from both sides)--> "Harshit" (converting into lowercase) --> "harshit" -->(counting number of times a char appeared) 
print(name.strip().lower().count(char.strip().lower()))




