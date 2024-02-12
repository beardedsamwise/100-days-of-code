from art import logo, vs
from game_data import data
import random
import os

game_over = False
score = 0

list_length = len(data)

def get_randint():
  return random.randint(0, list_length)

def guess():
  return input("Who has more follows? Type 'A' or 'B'': ").upper()
  
while not game_over:
  valid_guess = False

  data_1 = data[get_randint()]
  data_2 = data[get_randint()]
  if data_1 == data_2:
    data_2 = data[get_randint()]
  print(logo)
  print(f"Your current score is: {str(score)}")
  print(f"Compare A: {data_1.get('name')}, a {data_1.get('description')}, from {data_1.get('country')}")
  print(vs)
  print(f"Against B: {data_2.get('name')}, a {data_2.get('description')}, from {data_2.get('country')}")

  your_guess = guess()
  
  while not valid_guess:
    if your_guess == "A" or your_guess == "B":
      valid_guess = True
    else:
      print("You didn't select a value option...")
      your_guess = guess()


  if your_guess == "A" and data_1.get('follower_count') > data_2.get('follower_count') or your_guess == "B" and data_1.get('follower_count') < data_2.get('follower_count'):
    score += 1
    os.system('clear')
  else:
    os.system('clear')
    print(logo)
    print(f"Sorry! That's incorrect! Your final score is: {str(score)}")
    game_over = True
  
