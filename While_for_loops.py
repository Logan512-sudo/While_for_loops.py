# While loop = execute some code WHILE some condition remains true

name = input("enter your name: ")

# iteration = loop    iterate(verb)loop over something
while name == "":
    print("you did not enter your name")
    name = input("Enter your name:")
# infinite loops are bad

print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative:")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")



food = input("Enter a food you like (q to quit)")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit)")\
    
print("bye")



num = input("Enter a # between 1 - 10:")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")



# for loops = execute a block of code a fixed number of times
#       You can iterate over a range, string, sequence, etc.\

#credit_card = "1234-5678-9012-3456"

#for x in credit_card:
   # print(x)


for x in range(1, 21):
    if x == 13:
        break
       # continue
    #if x == 15:
        #continue
   # if x == 18:
       # continue
    else:
        print(x)



#create a list of famouse horror movie characters
horror_characters = ["Freddy Kruger", "Jason Vorhees", "Michael Myers", "Pennywise", "Chucky"]
#iterate through the list and print each character 

for x in horror_characters
    print(x)