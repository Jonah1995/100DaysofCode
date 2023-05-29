import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hand_list = [rock, paper, scissors]

user_hand = int(input("Rock, Paper, or Scissors? Type 0 for rock, 1 for paper, or 2 for scissors."))
print(hand_list[user_hand])

comp_hand = random.randint(0, 2)
print("computer chose:")
print(hand_list[comp_hand])

if user_hand == comp_hand:
  print("tie")
else:
  if user_hand == 0 and comp_hand == 1:
    print("You lose.")
  elif user_hand == 0 and comp_hand == 2:
    print("You win.")
  elif user_hand == 1 and comp_hand == 0:
    print("You win.")
  elif user_hand == 1 and comp_hand == 2:
    print("You lose.")
  elif user_hand == 2 and comp_hand == 0:
    print("You lose.")
  elif user_hand == 2 and comp_hand == 1:
   print("You win.") 