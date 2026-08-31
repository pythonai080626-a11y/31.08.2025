
random_number = get_random_number(1, 100)

print('Welcome to the number guessing game!')

guesses = 0

while True:
    guesses += 1

    user_guess = get_user_guess(1, 100)

    if user_guess == random_number:
        print(f'Congratulations! You guessed the number {random_number} in {guesses} guesses')
        break

    message = get_game_message(user_guess, random_number)

    print(message)

print('Game over! see you again soon')


