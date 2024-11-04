import random

print("\nWelcome to Rock Paper Scissors".center(50))

user_Score = 0
comp_Score = 0
ties = 0

name = input("\nEnter Your Name here : ")
print(f"\nHello {name}! Get ready to play.")

print("""
      Winning Rules :
1- Paper vs Rock = Paper wins
2- Paper vs Scissors = Scissors wins
3- Scissors vs Rock = Rock wins
""")

while True:
    print("\nChoices are: \n1. Rock\n2. Paper\n3. Scissors")
    try:
        user_choice = int(input("Enter Choice (1 for Rock, 2 for Paper, 3 for Scissors, 0 to Quit): "))
        if user_choice == 0:
            print("\nGame Over!")
            break
        
        match user_choice:
            case 1:
                choice = "Rock"
            case 2:
                choice = "Paper"
            case 3:
                choice = "Scissors"
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

        print(f"User choice is: {choice}")
        
        computer_choice = random.randint(1, 3)
        match computer_choice:
            case 1:
                comp_choice = "Rock"
            case 2:
                comp_choice = "Paper"
            case 3:
                comp_choice = "Scissors"

        print(f"Computer choice is: {comp_choice}")

        if choice == comp_choice:
            print("It's a tie!")
            ties += 1
        elif (choice == "Rock" and comp_choice == "Scissors") or (choice == "Scissors" and comp_choice == "Paper") or (choice == "Paper" and comp_choice == "Rock"):
            print("You win this round!")
            user_Score += 1
        else:
            print("Computer wins this round!")
            comp_Score += 1

        print(f"\nCurrent Scores:\n{name}'s Score: {user_Score} | Computer's Score: {comp_Score} | Ties: {ties}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nFinal Scores:")
print(f"{name}'s Score: {user_Score} | Computer's Score: {comp_Score} | Ties: {ties}")

if user_Score > comp_Score:
    print(f"Congratulations, {name}! You won the game!")
elif user_Score < comp_Score:
    print("Computer won the game! Better luck next time.")
else:
    print("It's a draw! Well played.")
