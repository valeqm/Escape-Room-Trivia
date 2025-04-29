# Escape Room Trivia

This code is for the final project of [CS50 Python](https://cs50.harvard.edu/python/2022/).

## Description
**Escape Room Trivia** is an interactive terminal-based game where you select the difficulty and category of the games you want to play.  
You must complete **4 different games** to "escape the room":

- **Rock Paper Scissors**  
- **Hangman**  
- **Number Guessing**  
- **Trivia**

Each game gives you part of a code needed to escape. Win all challenges to complete the escape!


## Project Structure
```
project/
│
├── project.py
├── test_project.py
├── certificate.png
├── README.md
└── requirements.txt
```


## Libraries Used
- **requests**: To make API calls to fetch trivia questions.
- **html**: To decode HTML entities from API responses.
- **random**: To shuffle options and generate random numbers or choices.
- **time**: To manage delays in the game for better user experience.
- **os**: To clear the terminal screen.
- **fpdf**: To generate a personalized certificate upon winning.
- **Pillow (PIL)**: To manipulate images for the certificate.
- **pytest**: To write and run test cases for different parts of the code.


## How It Works

### Utility Functions
- **clear()**  
  Clears the terminal screen depending on the operating system.

- **print_ascii_header()**  
  Displays the game title in ASCII art style.

- **get_user_choice(prompt, options)**  
  Displays a list of choices based on a prompt and validates user input.

- **start_game()**  
  Displays the welcome message, difficulty options, and category options. Returns the selected level and category for the game.


### Games

#### 1. Trivia Game (3 functions)
- **get_question(level, category)**  
  Fetches a trivia question from the [Open Trivia Database](https://opentdb.com/api_config.php) API.

- **play_question(question_data)**  
  Displays a trivia question and checks if the user's answer is correct.

- **trivia_game(level, category)**  
  Manages the trivia game logic, tracks lives (you have 3 lives), and returns a part of the escape code if successful.


#### 2. Rock Paper Scissors
- **rock_paper_scissors(level)**  
  You need to win a set number of rounds (depending on difficulty) against the computer to pass.


#### 3. Number Guessing Game
- **number_guessing_game(level)**  
  Try to guess a randomly chosen number between 1 and 100 within a limited number of tries depending on the difficulty.


#### 4. Hangman Game
- **hangman_game(level)**  
  Classic hangman game with words depending on difficulty. You have 15 chances to guess the word correctly.


### Certificate
- **generate_certificate(name)**  
  After successfully completing all games on hard mode, you can generate a **PDF certificate** with your name to celebrate your escape!


### Main Function
- **main()**  
  Starts the whole game and organizes the flow from one game to another until you escape or fail.


## Display Example
When you start the game, the terminal would look like this:

```
=======================================
         ESCAPE ROOM TRIVIA
=======================================

Select Difficulty:
1. easy
2. medium
3. hard

Choose an option: 
```


## How to Install

1. Download the folder:
   ```bash
   git clone https://github.com/valeqm/Escape-Room-Trivia.git
   ```

2. Navigate into the project folder:
   ```bash
   cd Escape-Room-Trivia
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python project.py
   ```


## Author  

**Valeria Q.M** 

