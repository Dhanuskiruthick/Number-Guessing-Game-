# specific imports
import modules.inputs as inp
import modules.logic as log

def start():
    print("\n--- GUESSING GAME ---\n")

    max_val = inp.get_range()
    target, tries = log.setup_game(max_val)

    print(f"\nI picked a number between 1 and {max_val}.")
    print(f"You get {tries} tries.\n")

    while tries > 0:
        guess = inp.get_guess()

        if guess is None:
            print("Enter a valid number.")
            continue

        result = log.check_guess(target, guess)

        if result == "WIN":
            print(f"\n🎉 You got it! The number was {target}.")
            return
        
        tries -= 1
        print(f"{result}. Tries left: {tries}")

    print(f"\nOut of tries! The number was {target}.")


if __name__ == "__main__":
    start()
