import requests
import html
import random
import time
import os
from fpdf import FPDF
from PIL import Image

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_header():
    print(GREEN + BOLD)
    print("=======================================")
    print("         ESCAPE ROOM TRIVIA")
    print("=======================================")
    print(RESET)

def get_user_choice(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("\nChoose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print(RED + "\nInvalid choice. Try again.\n" + RESET)

def start_game():
    clear()
    print_ascii_header()
    difficulty_levels = ['easy', 'medium', 'hard']
    categories = {
        'General Knowledge': 9,
        'Books': 10,
        'Film': 11,
        'Science': 17
    }

    level = get_user_choice("Select Difficulty:", difficulty_levels)
    print(" ")
    category_name = get_user_choice("Select Category:", list(categories.keys()))
    category_id = categories[category_name]

    print(f"\nYou chose {level.upper()} - {category_name.upper()}")
    input("\nPress Enter to start the game...")
    return level, category_id

def get_question(level, category):
    url = f"https://opentdb.com/api.php?amount=1&category={category}&difficulty={level}&type=multiple"
    while True:
        try:
            res = requests.get(url)
            q = res.json()["results"][0]
            correct = html.unescape(q["correct_answer"])
            incorrect = [html.unescape(i) for i in q["incorrect_answers"]]
            options = incorrect + [correct]
            random.shuffle(options)
            return {
                "question": html.unescape(q["question"]),
                "correct": correct,
                "options": options
            }
        except:
            pass

def play_question(question_data):
    clear()
    print_ascii_header()
    while True:
        print(BOLD + GREEN + "Question:\n" + RESET)

        options = question_data["options"]
        selected=get_user_choice(question_data["question"] + "\n",options)
        if selected == question_data["correct"]:
            print(GREEN + "\nCorrect! 🎉" + RESET)
            return 1
        else:
            print(f"\nWrong! ❌ The correct answer was: {GREEN}{question_data['correct']}{RESET}")
            return 0


def trivia_game(level, category):
    lives=3
    for i in range(6):
        question = get_question(level, category)
        answer=play_question(question)
        if answer==0:
            lives -=1
            if lives==-1: 
                print(BOLD + RED + "\nYou lose. No Clue" + RESET)
                return
            print("\nLIVES: ", lives*"❤️ ")
        else:
            print("\nLIVES: ", lives*"❤️ ")
        if i!=5:
            input("Press Enter to continue the game...")
    if lives>=0: return '0P'

def rock_paper_scissors(level):
    choices = ["rock", "paper", "scissors"]
    if level=='easy':w=2
    elif level=='medium':w=3
    else: w=4
    count=0
    clear()
    print_ascii_header()
    print(BOLD + GREEN + f"You have to win {w} times to pass\n" + RESET)
    while True:
        user=get_user_choice("Rock, Paper, Scissors? ",choices)
        comp = random.choice(choices)
        print(f"You chose: {user}")
        print(f"Computer chose: {comp}")

        if user == comp:
            print("It's a tie!\n")
            print(BOLD + GREEN + f"You won {count} times\n" + RESET)
        elif (user == "rock" and comp == "scissors") or \
            (user == "scissors" and comp == "paper") or \
            (user == "paper" and comp == "rock"):
            print("You win this round!\n")
            count += 1
            print(BOLD + GREEN + f"You won {count} times\n" + RESET)
            if count==w:return "S"
        else:
            print("You lose this round!\n")
            print(BOLD + GREEN + f"You won {count} times\n" + RESET)

def number_guessing_game(level):
    number = random.randint(1, 100)
    if level=='easy':tries =12
    elif level=='medium':tries =8
    else: tries =4

    clear()
    print_ascii_header()
    print(BOLD + GREEN + "🎲 Welcome to the Number Guessing Game!" + RESET)
    print(BOLD + GREEN + "I'm thinking of a number between 1 and 100..."+ RESET)
    print(BOLD + GREEN + f"Try to guess it in {tries} tries!\n"+ RESET)

    while True:
        guess = input("Your guess: ")
        tries -= 1
        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue
        guess = int(guess)

        if guess < number:
            print("⬆️ Too low!")
        elif guess > number:
            print("⬇️ Too high!")
        else:
            print(f"✅ You got it! The number was {number}.\n")
            return "C"
        if tries==0:
            print(BOLD + RED + "You lose. No Clue" + RESET)
            break
        
def hangman_game(level):

    word_list = {
    "easy": ["cat", "dog", "fish", "bird", "apple"],
    "medium": ["computer", "python", "hangman", "difficult", "programming"],
    "hard": ["encyclopedia", "unbelievable", "cryptocurrency", "metamorphosis", "photosynthesis"]
    }

    word_to_guess = random.choice(word_list[level])

    guessed_letters = []
    max_attempts = 15
    attempts_left = max_attempts
    word_display = ['_' for _ in word_to_guess]

    clear()
    print_ascii_header()
    print(BOLD + GREEN + f"Welcome to Hangman! Your word is {len(word_to_guess)} characters long." + RESET)
    
    while attempts_left > 0 and '_' in word_display:
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}\n")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(YELLOW + "\nPlease enter a single letter." + RESET)
            continue
        
        if guess in guessed_letters:
            print(YELLOW + f"\nYou've already guessed '{guess}'" + RESET)
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(GREEN + f"\nGood guess! '{guess}' is in the word." + RESET)

            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display[i] = guess
        else:
            print(YELLOW + f"\nOops! '{guess}' is not in the word." + RESET)
            attempts_left -= 1

    if '_' not in word_display:
        print(f"\n✅ Congratulations! You've guessed the word: {''.join(word_display)}\n")
        return "5"
    else:
        print(BOLD + RED + "\nYou lose. No Clue" + RESET)

def generate_certificate(name):

    image_path = "certificate.png"
    image = Image.open(image_path)
    width_px, height_px = image.size
    width_mm = width_px * 0.264583
    height_mm = height_px * 0.264583
    pdf = FPDF(orientation="P", unit="mm", format=[width_mm, height_mm])
    pdf.add_page()
    pdf.image(image_path, x=0, y=0, w=width_mm, h=height_mm)
    pdf.set_font("Times", style="B", size=45)
    pdf.set_text_color(0, 0, 0)
    text_width = pdf.get_string_width(name)
    x_centered = ((pdf.w-text_width) / 2)-50
    pdf.text(x=x_centered, y=110, txt=name)
    pdf.output("certificate.pdf")

def main():
    level, category = start_game()

    clues = []

    CLUE1 = rock_paper_scissors(level)
    clues.append(CLUE1)
    print(CYAN + 'CLUE: ' + str(CLUE1) + RESET)
    input("Press Enter to continue the game...")

    CLUE2 = hangman_game(level)
    clues.append(CLUE2)
    print(CYAN + 'CLUE: ' + str(CLUE2) + RESET)
    input("Press Enter to continue the game...")

    CLUE3 = number_guessing_game(level)
    clues.append(CLUE3)
    print(CYAN + 'CLUE: ' + str(CLUE3) + RESET)
    input("Press Enter to continue the game...")

    CLUE4 = trivia_game(level, category)
    clues.append(CLUE4)
    print(CYAN + 'CLUE: ' + str(CLUE4) + RESET)
    input("Press Enter to continue the game...")

    clear()
    print_ascii_header()
    code_attempt = input(BOLD + CYAN + "\nEnter the code to escape: " + RESET)

    correct_code = "CS50P"  

    time.sleep(1)
    clear()
    print_ascii_header()

    if code_attempt == correct_code:
        clues_found = sum(1 for clue in clues if clue is not None)
        if clues_found >= 3 and level=='hard':
            print(BOLD + CYAN + "\n🌟 SPECIAL CONGRATULATIONS! You solved the Escape Room on the hardest mode! 🌟\n" + RESET)
            print("As a reward, you’ve earned a certificate of completion.")
            player_name = input("Enter your name for the certificate: ")
            generate_certificate(player_name)
        else:
            print(BOLD + GREEN + "\n🎉 Congratulations! YOU ESCAPED THE ROOM! 🎉\n" + RESET)
    else:
        print(BOLD + RED + "\n❌ Incorrect code. Better luck next time!\n" + RESET)

    print("\nThanks for playing Escape Room Trivia!")

if __name__ == "__main__":
    main()
