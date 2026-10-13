#-----------------level 30 -----------------------Print only even numbers from 1 to 20.
for i in range(1, 21):
    if i > 1:
        if i % 3:
            print(i)

#-----------------level 32 -----------------------Print only even numbers from 1 to 20.
total = sum(range(1, 101))
print("sum is", total)

#------------------seccond method
total2 = 0

for i in range(1, 101):
    total2 += i

print(total2)

#-----------------level 33 -----------------------Find Largest Number in List
numbers = [5, 7, 99, 13, 42]
bignumbre = 0
for i in numbers:
    if i > bignumbre:
        bignumbre = i

# print largest number
print(bignumbre)

#-----------------level 34 -----------------------Create a Login System rules user=admin , pass=admin123
username = input("Username: ")
password = input("Password: ")
boleanUser = False
boleanPass = False

if username == "admin":
    boleanUser = True

if password == "admin123":
    boleanPass = True

if boleanUser == True & boleanPass == True:
    print("Welcome Admin")
else:
    print("Invalid credentials")

#-----------------level 35 -----------------------Server Status Checker -> Print only stopped servers.
servers = {
    "web01": "Running",
    "web02": "Stopped",
    "db01": "Running",
    "app01": "Stopped"
}
for server, status in servers.items():
    if status == "Stopped":
        print(server, "-", status, "- needs attention!!")

#-----------------level 36 -----------------------Function Practice - Output should be 25
def square(number):
    return number + 20

print(square(5))

#-----------------level 38 -----------------------Count Characters: 1. Ask user for a word. 2. Output Length: 16
word = input("Enter word:")
print("Length is:", len(word))

#-----------------level 39 -----------------------Generate Server Names Expected output: web01,web02,web03,web04,web05
import random
name = "web0"
for i in range(1, 6):
    #name = random.choice(name)
    print(f"{name}{i:02d}")
    #print(name)
#----------------------done-----------------------------------------------------------------------------------------