import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock, paper, scissors]
# Win Conditions

# -> rock beats scissors
# -> paper covers rock
# -> scissors cut paper

user = int(input("What Do you choose ? 0 = Rock , 1 = Paper , 2 = Scissors\n"))
print(images[user])

comp = random.randint(0, 2)
print("Computer Chose: ")
print(images[comp])

if user >= 3 or user < 0:
    print("You typed an invalid number")
elif user == 0 and comp == 2:
    print("You Win !")
elif comp == 0 and user == 2:
    print("You Loose !")
elif comp > user:
    print("You Loose !")
elif user > comp:
    print("You Win !")
elif comp == user:
    print("Its a tie !")
