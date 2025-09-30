import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("🎮 Guess a number between 1 and 100! (Enter 'q' to quit)")

    while True:
        guess = input("Your guess: ")
        if guess == "q":
            print("Goodbye!")
            break

        if not guess.isdigit():
            print("⚠️ Enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < number:
            print("⬆️ Too low! Try again.")
        else:
            print("⬇️ Too high! Try again.")

if __name__ == "__main__":
    guess_number()
