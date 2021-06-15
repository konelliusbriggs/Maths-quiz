import random

# functions used to check input is valid

# main routine goes here
 
# initialise variables
rounds_played = 0
 
# main function goes here

# get input from user etc...
print("** Welcome to the Lucky Unicorn Game! **")
print("Feeling lucky? Come try it!")
print()
 
need_instructions = yes_no("Have you played Lucky Unicorn before? ")
 
if need_instructions == "no":
 show_instructions()
 
balance = num_check("How much would you coins would you like to play with? ", 1, 10)
 
play_again = ""
while play_again == "":
  play_again = input("Press <Enter> to Play, Good luck!").lower()

  # Increase # of rounds played 
  rounds_played += 1
 
  # Print round number 
  print()
  print("*** Round #{} ***".format(rounds_played))

  chosen_num = random.randint(1 , 100)
  
  if 1 <= chosen_num <= 5:
    chosen = "Unicorn"
    chose_dec = "*"
    balance += 4

  # If the random # is is between 6 and 36
  # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "Donkey"
    chose_dec = "D"
    balance -= 1

  # The token is either a horse or a zebra 
  # In both cases, subtract $0.50 from balance 
  else:
    # If the chosen number is even
    # Item to a horse
    if chosen_num % 2 == 0:
      chosen = "Horse"
      chose_dec = "H"

    # Otherwise set it to a zebra 
    else:
      chosen = "Zebra"
      chose_dec = "Z"

    balance -= 0.5
  
  print()
  feedback = "You got a {}, your new balance is ${:.2f}".format(chosen, balance)
  statement_generator ("feedback, chose_dec")

  if balance < 1:
    play_again = "exit"
    print("That's the end of the road for you, Try again when you get lucky!")
  else:
    play_again = input("Press Enter to keep on playing, or 'exit' to quit")

print()
print("You ended with ${:.2f},Tough luck!".format(balance))



# Functions go here...
def num_check(question, low, high): 
  error = "Please enter a whole number between 1 and 10\n"

  valid = False 
  while not valid:
    try:
      # Ask the quesion
      response = int(input (question))
      # If the amount is too low / too high give 
      if low <= response <= high:
        return response 

      # Output an error 
      else:
        print(error)

    except ValueError:
      print(error)
 
def yes_no(question):
 valid = False
 while not valid:
  response = input (question).lower()
  
  if response == "yes" or response == "y":
    response = "yes"
    return response
  
  elif response == "no" or response == "n":
    response = "no"
    return response
  
  else:
    print("Please answer yes/no")
 
def show_instructions():
  print("** How To Play **")
  print()
  print("choose what level of maths you would like to play")
  print()
  print("level 1 addition")
  print()
  print("level 2 multiplication ")
  print()
  print("level 3 division")
  print()
  print("level 4 HARDEST ALL THE LEVELS")
  print("")
  return ""



