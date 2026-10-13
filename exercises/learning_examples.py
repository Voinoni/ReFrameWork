#----------Level 2----------User Input
name = input("What is your name? ")
print("Hello", name)
#----------Level 3----------Math Operations
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#----------Level 4----------If Statements
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

#----------Level 5----------For Loops
for i in range(1, 6):print(i)

#----------Level 6----------List
servers = ["Server1", "Server2", "Server3"]

for server in servers:

    print(server)
print("testtttt")

#----------Level 7----------Functions
def greet(name):
    print("Hello", name)

greet("Adam")
greet("Florin")

#----------Level 8----------Check Even or Odd
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#--------------------Level 9---------------------Working with Files
file = open(r"C:\Work\Python Scripts-test\notes.txt", "r")

content = file.read()

print(content)

file.close()

#--------------------Level 10---------------------Real DevOps Example
import os

print("Current Directory:")
print(os.getcwd())

#--------------------Level 11---------------------Show Files in a Folder
import os

files = os.listdir()

for file in files:
    print(file)

#--------------------Level 12---------------------