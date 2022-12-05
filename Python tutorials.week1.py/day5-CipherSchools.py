age = int(input("Enter your age: "))
if age>0 and age<=3:
    print("ticket price: Free")
elif age>3 and age<=10:
    print("ticket price: 150")
elif age>10 and age<=60:
    print("ticket price: 200")
else:
    print("ticket price: 250")

# in keyword
# if with in
a = "Ayushi"
a = a.lower()
if 'a' in a:
    print("a is present")
else:
    print("not present")    

# check empty string or not - important
a = "abc"
if a:    #this will be  true when str is not empty
    print("string is not empty")
else:
    print("string is empty")    

name =input("")
if name:
    print(f"your name is {name}")
else:
    print("you didn't type anything")    

# loops  - while,for 
# print(10*"hello world\n")
i = 1
while i <=10:
    print(f"hello world {i}")
    i = i + 1

#sum of first 10 numbers
i = 1
count = 0
while i <= 10 :
   count = count + i 
   i = i + 1
print(count)

#Exercise 1
n = int(input("Enter a number: "))
i = 1
count = 0
while i <= n :
    count = count + i
    i = i+1
print(f"Sum of numbers is {count}") 

#Exercise 2
n = input("Enter number: ")     # len attribute works only for strings

total = 0
i = 0
while i < len(n):
    total += int(n[i])
    i = i+1
print(f"sum of digits of number is {total}")    

#Exercise3
name = input("enter your name: ")
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
     
    i += 1
     
       



