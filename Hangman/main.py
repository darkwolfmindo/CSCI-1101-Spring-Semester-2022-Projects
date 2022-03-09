import re

# Get answer
answer_characters = ["A","N","S", "W", "E", "R"]

# Store known or unknown letters
answer_guesses = []

# Determine which characters are known before starting the game
for current_answer_character in answer_characters:
  if re.search("^[A-Z]$", current_answer_character):
    answer_guesses.append(False)
  else:
    answer_guesses.append(True)

# Logic of playing the game
guessed_letter = []
num_of_incorrect_guesses = 0

while num_of_incorrect_guesses < 5 or False in answer_guesses:
  print("-----------------")
  print("Guessed Letters: ", end = "")

  for current_guessed_letter in guessed_letter:
    print(f"{current_guessed_letter}", end = "")

  print()

  print(f"Number of incorrect guesses remaining: {5 - num_of_incorrect_guesses}")

  print()

  for answer_index in range(len(answer_characters)):
    if answer_guesses[answer_index]:
      print(answer_characters[answer_index], end = "")
    else:
      print("_", end = "")

print()

letter = input("Enter a letter: ")

letter = letter.upper()

if letter not in guessed_letter:
  pass
  
print("-----------------")