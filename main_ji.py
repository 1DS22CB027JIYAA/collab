import random


input_list = ["rock","paper","scissor"]
computer_input = random.choice(input_list)
user_points = 0
computer_points = 0

if user_input==computer_input:
    print("draw")
    
elif (computer_input=="rock"&&user_input=="scissor")||(computer_input=="paper"&&user_input=="rock")||(computer_input=="scissor"&&user_input=="paper"):
    print("computer won")
    computer_points+=1
    print(f"computer points:{computer_points} user points:{user_points}")

else:
    print("user won")
    user_points+=1
    print(f"computer points:{computer_points} user points:{user_points}")






















