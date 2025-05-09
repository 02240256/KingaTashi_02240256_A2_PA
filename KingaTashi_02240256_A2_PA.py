import random

score_guess_game = 0

def guess_number_game():
    print("-- Guess Number Game ---")
    target_number = random.randint(1, 10)
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == target_number:
            print("Correct!")
            global score_guess_game
            score_guess_game += 1
        else:
            print("Wrong! The number was:", target_number)
    except:
        print("Invalid input. Please enter a number.")

score_rps = 0

def rock_paper_scissors_game():
    print("--- Rock Paper Scissors Game ---")
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    player = input("Enter rock, paper, or scissors: ").lower()
    global score_rps
    if player not in options:
        print("Invalid choice.")
        return
    print("Computer chose:", computer)
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        score_rps += 1
    else:
        print("You lose.")

score_trivia = 0

def trivia_pursuit_game():
    print("--- Trivia Pursuit Game ---")
    question = "What is a program or set of instructions that a computer can execute called?\n(a) Algorithm\n(b) Software\n(c) Script\n"
    answer = input(question + "Your answer: ").lower()
    global score_trivia
    if answer == "b":
        print("Correct!")
        score_trivia += 1
    else:
        print("Sorry. The correct answer was b. Software.")

pokemon_binder = []

def pokemon_card_binder_manager():
    while True:
        print("\n--- Pokemon Card Binder ---")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            card = input("Enter Pokemon card name: ")
            pokemon_binder.append(card)
            print("Card added.")
        elif choice == "2":
            pokemon_binder.clear()
            print("Binder reset.")
        elif choice == "3":
            print("Current cards:", pokemon_binder)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def show_overall_score():
    print("--- Overall Score ---")
    print("Guess Number Game score:", score_guess_game)
    print("Rock Paper Scissors wins:", score_rps)
    print("Trivia correct answers:", score_trivia)

# Main menu loop
while True:
    print("Select a function (0-5):")
    print("1. Guess Number game")
    print("2. Rock paper scissors game")
    print("3. Trivia Pursuit Game")
    print("4. Pokemon Card Binder Manager")
    print("5. Check Current Overall score")
    print("0. Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        guess_number_game()
    elif choice == "2":
        rock_paper_scissors_game()
    elif choice == "3":
        trivia_pursuit_game()
    elif choice == "4":
        pokemon_card_binder_manager()
    elif choice == "5":
        show_overall_score()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
