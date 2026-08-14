import random

def play_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("Choose a difficulty:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        max_number = 50
        attempts = 10
        difficulty = "Easy"

    elif choice == "2":
        max_number = 100
        attempts = 7
        difficulty = "Medium"

    elif choice == "3":
        max_number = 200
        attempts = 5
        difficulty = "Hard"

    else:
        print("Invalid choice!")
        return

    secret_number = random.randint(1, max_number)
    score = 100

    print(f"\nDifficulty: {difficulty}")
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts!")

    for attempt in range(1, attempts + 1):

        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue

            if guess == secret_number:
                bonus = (attempts - attempt) * 10
                score += bonus

                print("\n🎉 Congratulations!")
                print(f"You guessed the number in {attempt} attempts.")
                print(f"The number was {secret_number}.")
                print(f"Your score: {score}")
                return

            elif guess < secret_number:
                print("📉 Too low!")
            else:
                print("📈 Too high!")
                
            score -= 10

            print(f"Attempts remaining: {attempts - attempt}")
            print(f"Current score: {max(0, score)}")

        except ValueError:
            print("Please enter a valid number.")

    print("\n❌ Game Over!")
    print(f"The correct number was {secret_number}.")
    print("Your final score:", max(0, score))


while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing! 👋")
        break