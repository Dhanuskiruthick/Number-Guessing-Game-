# Project: Simple Number Guessing Game

**Theme:** Entertainment & Media

## About This Project
For my Python project, I decided to build a classic "Guess the Number" game. I chose the **Entertainment & Media** theme because games are a great way to understand programming logic.

Instead of just writing a simple script, I wanted to make it smarter. The game asks you to set a range (like 1 to 100), and it automatically calculates how many attempts you should get based on how hard the range is.

## How I Designed It (Modular Approach)
I followed the Top-Down design principle for this project. Instead of writing all the code in one file, I split it into smaller, manageable pieces. This makes the code cleaner and easier to fix if something breaks.

Here is how I organized my folders:

```text
Guessing-Game/
│
├── main.py                # This is the file you need to run
├── requirements.txt       # (Empty, as I used standard libraries)
├── README.md              # Project documentation
│
├── modules/               # I kept my logic separate here
│   ├── __init__.py        # Required to make Python recognize the folder
│   ├── inputs.py          # Handles user typing and errors
│   └── logic.py           # Handles the math and game rules
│
└── screenshots/           # Proof that the code works

Key Features
Smart Attempts: The game doesn't just give you 5 tries every time. If you choose a huge number like 1000, the code gives you extra attempts to make it fair.

Error Handling: I used try-except blocks in the input module. So, if a user types "abc" instead of a number, the game won't crash—it just asks them to try again.

Clean Interface: The game tells you if your guess was "Too High" or "Too Low" to help you narrow down the answer.

How to Run the Code
Download the project folder.

Open your terminal or command prompt.

Navigate to the folder where main.py is located.

Run this command:

Bash
python main.py

Future Plans
Right now, it's a single-player game. In the future, I plan to add a scoring system where you get more points for guessing correctly in fewer tries, or maybe a "Computer vs. Player" mode