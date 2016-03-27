# Rachel Ilan Mar. 26 2016
# Bisection search
upper_bound = 100
lower_bound = 0
guess = 50
user_input = ""
success = "Game over. Your secret number was: "
question = "Is your secret number "
message = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate" \
          " the guess is too low. Enter 'c' to indicate I guessed correctly. "
bad_input_message = "Sorry, I did not understand your input."

print "Please think of a number between " + str(lower_bound) + " and " + \
      str(upper_bound) + "!"

while user_input != "c" and lower_bound < upper_bound:
    user_input = raw_input(question + str(guess) + "?\n" + message)
    if user_input not in ["l", "h", "c"]:
        print bad_input_message
        continue
    if user_input == "l":
        lower_bound = guess
    elif user_input == "h":
        upper_bound = guess
    elif user_input == "c":
        print success, guess
    guess = (upper_bound + lower_bound)/2




