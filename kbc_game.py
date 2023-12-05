
import sys

user_name = input("Enter your name to start the game: ")


questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        'correct_answer': 'C. Paris',
        'amount': 1000
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A. Mars', 'B. Jupiter', 'C. Saturn', 'D. Venus'],
        'correct_answer': 'A. Mars',
        'amount': 5000
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Dolphin'],
        'correct_answer': 'B. Blue Whale',
        'amount': 10000
    },
    {
        'question': 'What is the capital city of Australia?',
        'options': ['A. Sydney', 'B. Melbourne', 'C. Canberra', 'D. Perth'],
        'correct_answer': 'C. Canberra',
        'amount': 20000
    },
    {
        'question': 'Which is the largest ocean in the world?',
        'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Pacific Ocean', 'D. Arctic Ocean'],
        'correct_answer': 'C. Pacific Ocean',
        'amount': 50000
    },
    {
        'question': 'What is the currency of Japan?',
        'options': ['A. Yen', 'B. Won', 'C. Yuan', 'D. Ringgit'],
        'correct_answer': 'A. Yen',
        'amount': 100000
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['A. Charles Dickens', 'B. William Shakespeare', 'C. Jane Austen', 'D. Mark Twain'],
        'correct_answer': 'B. William Shakespeare',
        'amount': 200000
    },
    {
        'question': 'Which gas makes up the majority of Earth\'s atmosphere?',
        'options': ['A. Oxygen', 'B. Carbon Dioxide', 'C. Nitrogen', 'D. Hydrogen'],
        'correct_answer': 'C. Nitrogen',
        'amount': 500000
    },
    {
        'question': 'In which year did Christopher Columbus reach the Americas?',
        'options': ['A. 1492', 'B. 1588', 'C. 1620', 'D. 1776'],
        'correct_answer': 'A. 1492',
        'amount': 1000000
    },
    {
        'question': 'What is the capital of Brazil?',
        'options': ['A. Rio de Janeiro', 'B. Brasília', 'C. Sao Paulo', 'D. Salvador'],
        'correct_answer': 'B. Brasília',
        'amount': 2000000
    }
]



def display_question(question_data):
    # random.shuffle(questions)
    print(question_data['question'])
    for option in question_data['options']:
        print(option)
    user_answer = input('Your answer: ')
    return user_answer.strip().upper()


def kbc_game():
    total_amount = 0
    for question_data in questions:
        print('\nAmount: Rs. {}'.format(question_data['amount']))
        user_answer = display_question(question_data)
        if user_answer == question_data['correct_answer'][0]:
            print('Correct!\n')
            total_amount += question_data['amount']
        else:
            print('Incorrect! The correct answer was {}\n'.format(question_data['correct_answer']))
            print(f'Your total winning is Rs. {total_amount}')
            sys.exit()

    print(f'Congratulations! {user_name} you have completed the game.')
    print('Total amount won: Rs. {}'.format(total_amount))
    return

if __name__ == "__main__":
  print(f"Hi {user_name} Welcome to Kaun Banega Crorepati!")
  kbc_game()


