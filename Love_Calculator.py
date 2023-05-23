# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_name = name1 + name2
both_name = both_name.lower()
t = both_name.count("t")
r = both_name.count("r")
u = both_name.count("u")
e = both_name.count("e")
true = t + r + u + e

l = both_name.count("l")
o = both_name.count("o")
v = both_name.count("v")
e = both_name.count("e")
love = l + o + v + e

Love_Score = int(str(true) + str(love))

if (Love_Score < 10)  or (Love_Score > 90):
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif (Love_Score >= 40) and (Love_Score <= 50):
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")