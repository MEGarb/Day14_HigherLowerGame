import os
import random
import art
from data import data


def retrieves_data():
    """Returns a randomly generated entry from the data.  Returned in a dictionary."""

    return random.choice(data)


def new_game(scr, orig):
    """Resets variables for a new game.  Resets score to 0 as int.  Returns orig is returned in a dictionary."""
    scr = 0
    orig = retrieves_data()
    return scr, orig


def compare_choices(a_choice, b_choice):
    if a_choice.get("follower_count") == b_choice.get("follower_choice"):
        return True


a_choice = {}
b_choice = {}
score = 0
highest_score = -25
another_game = True
while another_game:
    score, a_choice = new_game(score, a_choice)

    winning_round = True
    while winning_round:
        os.system('cls')
        print(art.logo)
        b_choice = retrieves_data()

        if compare_choices:
            b_choice = retrieves_data()

        if score > 0:
            print(f"You are correct! Your current score is {score}.")
        elif highest_score > 0:
            print(f"The highest score this session has been {highest_score}. See if you can top it!")

        print(f"Option A:  {a_choice.get('name')}, a {a_choice.get('description')}, from {a_choice.get('country')}")
        print(art.vs)
        print(f"Option B:  {b_choice.get('name')}, a {b_choice.get('description')}, from {b_choice.get('country')}")
        player_choice = input("Select the option that has the most Instagram followers.  Enter either 'A' or 'B':  ").\
            lower()

        if (player_choice == 'a' and a_choice.get('follower_count') > b_choice.get('follower_count')) or \
                (player_choice == 'b' and a_choice.get('follower_count') < b_choice.get('follower_count')):
            score += 1
            a_choice = b_choice
        else:
            winning_round = False

    print("Unfortunately you are  wrong.")
    if score > highest_score:
        highest_score = score
    if input("Would you like to play again? 'Y' or 'N':  ").lower() == 'n':
        another_game = False
