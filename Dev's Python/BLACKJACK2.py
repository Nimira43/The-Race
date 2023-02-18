import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)
    return rand_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(compcards, usercards):
    if user_score == 0:
        return "You win with a blackjack"
    elif computer_score == 0:
        return "Computer has a Blackjack "
    elif user_score == computer_score :
        return "PUSH"
    elif user_score > 21:
        return "YOU burst,computer win "
    elif computer_score > 21:
        return "computer burst,you win"
    elif user_score > computer_score :
        return "You win"
    else:
        return "computer win"


user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"Your cards are {user_card} and score is {user_score}")
    print(f"Computer's first card: {computer_card[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        hit = input("Type 'Y' to hit and 'N' to stand\n").upper()
        if hit == "Y":
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)
    print(f"computer cards: {computer_card}")
    print(f"compute score: {computer_score}")

print(compare_scores(computer_score, user_score))