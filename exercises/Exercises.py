#-----------------level 15 -----------------------Sum Two Numbers
#num1 = int(input("First number: "))
#num2 = int(input("Second number: "))

#result = num1 + num2

#print("Result:", result)

#-----------------level 16 -----------------------Password Checker
#password = input("Enter password: ")

#if password == "admin123":
#    print("Access granted")
#else:
#    print("Access denied")

#-----------------level 17 -----------------------Multiplication Table
#number = int(input("Enter number: "))

#for i in range(1, 11):
#    print(number, "x", i, "=", number * i)

#-----------------level 18 -----------------------Count Down
#for i in range(20, 0, -1):
#    print(i)

#print("Launch!")
#-----------------level 19 -----------------------Find Largest Number
#a = 15
#b = 99

#if a > b:
#    print(a, "is larger")
#else:
#    print(b, "is larger")

#-----------------level 21 -----------------------Count Files in path
#import os

#files = os.listdir()

#print("Total files:", len(files))

#-----------------level 22 -----------------------Find Python Files
#import os
#py_files = [file for file in os.listdir() if file.endswith(".py")]

#for file in py_files:
#    print(file)

#print(f"\nTotal Python files: {len(py_files)}")

#---------------------------------------------------
#import os
#This is an important Python concept:
#print(os.getcwd()) # Shows where Python is looking
#print(os.listdir()) # Lists files in that location
#---------------------------------------------------


#-----------------level 23 -----------------------Function Calculator
#def add(a, b):
#    return a + b

#result = add(5, 10)

#print(result)

#-----------------level 24 -----------------------Average Score
#scores = [80, 90, 70, 100]

#average = sum(scores) / len(scores)

#print("Average:", average)
#-----------------level 25 -----------------------Guess the Number
#secret = 7

#guess = int(input("Guess number: "))

#if guess == secret:
#    print("Correct!")
#else:
#    print("Wrong!")

#-----------------level 26 -----------------------Star Pyramid ⭐
#for i in range(1, 6):
#    print("*" * i)

#-----------------level 26 -----------------------Reverse Pyramid ⭐⭐⭐
#for i in range(5, 0, -1):
#    print("*" * i)

#-----------------level 26 -----------------------FizzBuzz (Famous Interview Question)
#for i in range(1, 21):

#    if i % 15 == 0:
#        print("FizzBuzz")

#    elif i % 3 == 0:
#        print("Fizz")

#   elif i % 5 == 0:
#        print("Buzz")

#    else:
#        print(i)

#-----------------level 30 -----------------------Mini DevOps Inventory
#servers = {
#    "web01": "Running",
#    "web02": "Stopped",
#    "db01": "Running"
#}

#for server, status in servers.items():
#    print(server, "-", status)
#-----------------------------------------------------------------------
#Challenge Project: 1. Asks for your name, 2. Asks how many servers you have , 3.Prints "Hello Adam You have 5 servers to manage"
#-----------------------------------------------------------------------
name = input("What is your name ")
nrServers = int(input("how many servers you have"))

print("Hello", name, "You have", nrServers, "servers")

if nrServers > 10:
    print("Large environment")
else:
    print("Small environment")

