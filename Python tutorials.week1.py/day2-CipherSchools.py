#EXERCISE 1...
#OUTPUT1 - this is \\ double backslash
print("this is \\\\ double backslash")
#OUTPUT2 - these are /\/\/\/\/\ mountains
print("these are /\/\/\/\/\/\ mountains")
#OUTPUT3 - he is    awesome(use escape sequences)
print("he is \t awesome")
#OUTPUT4 - \" \n \t \'
print(" \\\" \\n \\t \\\' ")

#shortcut (for printing escape sequences as normal raw text)
print(r"line a \n line b ")   #r = row string
#Printing unicodes through google.. replacing + by 000
print("\U0001F602")
print("\U0001F35F")

#Python as CALCULATOR   #float division - /, integer division - //
print(4/2)    #float division
print(4//2)   #integer division
print(2//4)   #0 - integer division

print(round(2**0.5,4))

# solving equations on the basis of associativity rule and precedence:
# parentheses
# exponents - right to left
# %, /, //, * - left to right
# (+, - ) left to right

print(2**3**2)   #2**9 = 2^9 = 512

#variable rules:
#special characters should not be used
#first character of a variable should not be a number but numbers can be used in between words
#_ and @ can be used at the start of a variable 
#conventions:
#snake case writing - user_one_name (more suitable for python)
#camel case writing - userOneName (more suitable in java)

first_name = "Ayushi"
last_name = "Bhutani"
full_name = first_name + " "+ last_name 
print(full_name)
print(3*( first_name + " ") )

#input from the user is always taken as a string unless int() function is used
number_one = int(input("enter first number: "))
number_two = int(input("enter second number: "))
print("total is: " + str(number_one + number_two))
number1 = str(2)
number2 = float(3)
number3 = int(4)
print(number2 + number3)

name , age = "Ayushi" , "17"
print("hello " + name + " your age is " + age)


