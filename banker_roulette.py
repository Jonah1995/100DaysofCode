# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

choice = random.randint(0, num_items - 1)
person = names[choice]

print(person + " is going to buy the meal today!")