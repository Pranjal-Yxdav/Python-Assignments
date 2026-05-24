import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game")
print("Type 'exit' to quit\n")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user == "exit":
        print("\nGame Over!")
        print("Final Score -> You:", user_score, "| Computer:", computer_score)
        break

    if user not in choices:
        print("❌ Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("🤝 It's a draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("✅ You win!")
        user_score += 1
    else:
        print("❌ You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)
    print("-" * 30)