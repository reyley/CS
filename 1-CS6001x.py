# Rachel Ilan Mar. 26 2016


# week 2

# Bisection search
def bisection_search():
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


# Counting Vowels

def counting_vowels(s):
    n_vowels = 0
    for char in s:
        if char in "aeiou":
            n_vowels += 1

    print "Number of vowels:", n_vowels


# Quiz problem 4:

def isPalindrome(aString):
    '''
    aString: a string
    '''
    for i in range(len(aString)/2):
        if aString[i] != aString[-i-1]:
            return False
    return True


# Quiz problem 6:

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    flattened_list = []
    for thing in aList:
        if type(thing) == list:
            flattened_list += flatten(thing)
        else:
            flattened_list.append(thing)
    return flattened_list

# Quiz problem 7:

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersecrt = {}
    difference = {}
    for key in (d1.keys() + d2.keys()):
        if key in d1 and key in d2:
            intersecrt[key] = f(d1[key], d2[key])
        elif key in d1:
            difference[key] = d1[key]
        else:
            difference[key] = d2[key]
    return intersecrt, difference


# Quiz problem 8:

def satisfiesF_On2(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    index = 0
    while index < len(L):
        if f(L[index]):
            index += 1
        else:
            L.pop(index)
    return len(L)

def f(a=1, b=2):
    pass

def satisfiesF_On(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    index = 0
    while index < len(L):
        if f(L[index]):
            index += 1
        else:
            L[index] = L[-1]
            L.pop()
    return len(L)


def item_order(order):
    order_dict = {"salad": 0, "hamburger": 0, "water": 0}
    order = order.split(" ")
    for food in order:
        if food in order_dict:
            order_dict[food] += 1
    return "salad:" + str(order_dict["salad"]) + " hamburger:" + \
           str(order_dict["hamburger"]) + " water:" + str(order_dict["water"])
