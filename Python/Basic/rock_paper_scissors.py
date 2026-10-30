import random
def get_choices():
  # take input from user
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  # computer choices
  options = ["rock", "paper", "scissors"]
  # computer picks randomly
  computer_choice = random.choice(options)
  # store both choices
  choices = {"player": player_choice, "computer": computer_choice}
  
  return choices
def check_win(player, computer):
  # show both choices
  print(f"You chose {player}, computer chose {computer}")
  # check if its a tie
  if player == computer:
    return "It's a tie!"

  # when player chooses rock
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."

  # when player chooses paper
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose."

  # when player chooses scissors
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose."
# get choices from both
choices = get_choices()
# check who wins
result = check_win(choices["player"], choices["computer"])
# show the result
print(result)
