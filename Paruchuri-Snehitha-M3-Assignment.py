#sp2995
#Snehitha Paruchuri

import random

# Generate random dimensions for the grid
l = random.randint(5, 20)  # Random length
w = random.randint(5, 20)  # Random width

# Display the grid dimensions
print(f"Grid dimensions: Length = {l}, Width = {w}")

# Generate a random position (s1, s2) for the treasure
s1 = random.randint(1, l)  # Row position
s2 = random.randint(1, w)  # Column position

# Initialize attempt counter
attempts = 0

# Guess the row position
print("Guess the row position of the treasure:")
while True:
    row_guess = int(input("Enter your row guess: "))
    attempts += 1
    if row_guess < s1:
        print(f"You guessed too low for the row position, try again! {attempts} attempts used!")
    elif row_guess > s1:
        print(f"You guessed too high for the row position, try again! {attempts} attempts used!")
    else:
        print(f"You guessed correctly! {attempts} attempts used, now try to guess the column position!")
        break

# Guess the column position
print("Guess the column position of the treasure:")
while True:
    col_guess = int(input("Enter your column guess: "))
    attempts += 1
    if col_guess < s2:
        print(f"You guessed too low for the column position, try again! {attempts} attempts used!")
    elif col_guess > s2:
        print(f"You guessed too high for the column position, try again! {attempts} attempts used!")
    else:
        print(f"You guessed the position of the treasure correctly! {attempts} attempts used!")
        break

