import ui
import random 


computer_choice = (random.randint(1, 3))

 #global constants
ROCK = 1
SCISSORS = 2
PAPER = 3

def rock_choice_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'You Tie, I picked Rock.'
    elif computer_choice == 2:
        view['answer_label'].text = 'You Win,I picked Scissors'
    elif computer_choice == 3:
        view['answer_label'].text = 'You lose, I picked Paper'

def paper_choice_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'You Win, I picked Rock'

    elif computer_choice == 2:
        view['answer_label'].text = 'You lose, I picked Scissors'

    elif computer_choice == 3:
        view['answer_label'].text = 'You Tie, I picked Paper'

def scissors_choice_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'You lose, I picked Rock'

    elif computer_choice == 2:
        view['answer_label'].text = 'You Tie, I picked Scissors'

    elif computer_choice == 3:
        view['answer_label'].text = 'You Win, I picked Paper'

view = ui.load_view()
view.present('sheet')
