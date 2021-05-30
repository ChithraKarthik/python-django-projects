import random

computer_choice = random.choice(['rock','paper','scissor'])

user_input = input("'Rock' , 'Paper', 'Scissor'...! type any one : ")

input1 = { 'R':'rock', 'P':'paper', 'S':'scissor'}

your_choice = input1[user_input.strip()[0].upper()]
print(" I am : " + user_input)
print(" You are : " + computer_choice)

win = { 'rock':'paper', 'paper':'scissor','scissor':'rock'}

if computer_choice == your_choice:
    print ("Play one more time")
elif win[computer_choice] == your_choice:
    print(" I are win")
else:
    print("Computer win")
