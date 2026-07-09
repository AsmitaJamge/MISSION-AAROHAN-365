# Guess the Lucky Number using Functions

# Function to check the guessed number
def check_lucky_number(guess):
    lucky_number = 7

    if guess == lucky_number:
        return "🎉 Congratulations! You guessed the Lucky Number."
    else:
        return "❌ Try Again!"

# Main Program
print("====== Guess the Lucky Number ======")

guess = int(input("Enter your guess: "))

result = check_lucky_number(guess)
print(result)