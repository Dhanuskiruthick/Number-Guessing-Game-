def get_range():
    while True:
        num = input("Enter the maximum number (e.g. 100): ")

        # Check if it's a number
        if not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)
        if num > 1:
            return num
        else:
            print("Number must be greater than 1.")

def get_guess():
    guess = input("Enter your guess: ")

    if guess.isdigit():
        return int(guess)
    else:
        return None
