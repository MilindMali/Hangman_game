
from hangman import words, LOGO, HANGMANPICS
from replit import clear

stages=HANGMANPICS[::-1]

import random
chosen_word=random.choice(words)

print(LOGO)

print("the choosen word is: ",chosen_word)

list_1=[]
for i in range(len(chosen_word)):
  list_1.append("_")

print(list_1)

end_of_game=False

lives=6

while not end_of_game:

  guess = input("Guess a letter: ").lower()

  clear()
  
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter == guess:
      list_1[position]=letter

  print(list_1)
  
  if '_' not in list_1:
    end_of_game=True
    print("you win")

  if guess not in list_1:
    lives-=1
    print(stages[lives])
    
    if lives==0:
      end_of_game=True
      print('You Lose')

  print("Number of lives remained",lives)
  
