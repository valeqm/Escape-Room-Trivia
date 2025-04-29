import os
from unittest.mock import patch
from project import clear, print_ascii_header, get_user_choice, start_game, get_question, play_question, trivia_game, rock_paper_scissors, number_guessing_game, hangman_game, generate_certificate

def test_clear():
    with patch('os.system') as mock_clear:
        clear()
        mock_clear.assert_called_once_with('cls' if os.name == 'nt' else 'clear')

def test_print_ascii_header():
    with patch('builtins.print') as mock_print:
        print_ascii_header()
        mock_print.assert_any_call("=======================================")
        mock_print.assert_any_call("         ESCAPE ROOM TRIVIA")
        mock_print.assert_any_call("=======================================")

def test_get_user_choice():
    with patch('builtins.input', return_value='1'):
        choice = get_user_choice("Choose an option:", ["easy", "medium", "hard"])
        assert choice == "easy"

    with patch('builtins.input', return_value='2'):
        choice = get_user_choice("Choose an option:", ["easy", "medium", "hard"])
        assert choice == "medium"

def test_start_game():
    with patch('builtins.input', return_value='1'):
        level, category = start_game()
        assert level in ['easy', 'medium', 'hard']
        assert category in [9, 10, 11, 17]

def test_get_question():
    level = 'easy'
    category = 9
    question = get_question(level, category)
    assert "question" in question
    assert "correct" in question
    assert "options" in question
    assert len(question["options"]) == 4

def test_play_question():
    question_data = {
        "question": "What is 2 + 2?",
        "correct": "4",
        "options": ["3", "4", "5", "6"]
    }
    with patch('builtins.input', return_value='2'):
        result = play_question(question_data)
        assert result == 1

    with patch('builtins.input', return_value='3'):
        result = play_question(question_data)
        assert result == 0

def test_trivia_game():
    with patch('project.get_question', return_value={"question": "What is 2 + 2?", "correct": "4", "options": ["3", "4", "5", "6"]}), \
         patch('project.play_question', return_value=1), \
         patch('builtins.input', return_value=''):
        result = trivia_game('easy', 9)
        assert result == '0P'

def test_rock_paper_scissors():
    with patch('project.get_user_choice', return_value='rock'):
        result = rock_paper_scissors('easy')
        assert result == 'S' 

def test_number_guessing_game():
    with patch('random.randint', return_value=50):
        with patch('builtins.input', return_value='50'):
            result = number_guessing_game('easy')
            assert result == 'C'

def test_hangman_game():
    with patch('random.choice', return_value='dog'):
        with patch('builtins.input', side_effect=['d', 'o', 'g']):
            result = hangman_game('easy')
            assert result == '5'

def test_generate_certificate():
    output_file = "certificate.pdf"
    generate_certificate("Test Player")
    assert os.path.exists(output_file)
