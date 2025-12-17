from random import randint
import art

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")

def check_difficulty():
    level = input("Choose difficulty 'easy' or 'Hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(art.logo)
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 to 100")
    answer = randint(1,100)


    turns = check_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} turns to guess")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses")
            return
        elif guess!= answer:
            print("guess again")

game()