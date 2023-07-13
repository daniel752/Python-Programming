from random import randrange
from pynput.keyboard import Key


def code_cracker():

    # generating a random 5 digit pin code for the user to guess
    pin_code = randrange(10000, 100000, 1)
    # user's starting points
    points = 100
    print("Welcome to the pin cracker game!")
    guess = 0
    number_of_clue = 0
    msg = []

    def random_clue():
        # generating a random clue for the user
        clue_number = randrange(1, 7, 1)
        return clue_number

    def print_points(points):
        # show user the remaining points
        print("Points left: ", points)

    def end_game(points):
        # end game screen
        print("\nWrong, see ya!")
        print_points(points)

    def yes_or_no(f, n):
        # func that gets f (function) and n (int number) and returns yes or no
        if f:
            msg = "Yes"
            return msg
        msg = "No"
        return msg

    def check_if_greater(correct_num):
        # func to check if user's guess is lower than the random pin code
        temp = int(input("Enter a number to check if the correct number is greater: "))
        return correct_num > temp

    def check_if_smaller(correct_num):
        # func to check if user's guess is higher than the random pin code
        temp = int(input("Enter a number to check if the correct number is smaller: "))
        return correct_num < temp

    def print_msg_to_func(msg, f):
        # func to the sum/sub clues
        if f >= 0:
            msg = "Sum = " + str(f)
            return msg
        msg = "Sub = " + str(f)
        return msg

    # lambda function for the sum of digits from the random pin
    sum_of_digits = lambda number: 0 if number == 0 else (number % 10) + sum_of_digits(number // 10)

    # lambda function for the sub of digits from the random pin
    sub_of_digits = lambda number: 0 if number == 0 else sub_of_digits(number // 10) - number % 10

    def show_string_by_func(msg, f):
        # function for odd/divided by 3 digits
        msg = f
        return msg

    # lambda function for odd digits
    check_odd_digit = lambda num: num % 2 != 0

    def odd_digits(correct_num):

        # func to show odd digits in pin code
        print("odd digits: ", end="")
        msg = list('     ')
        i = 4
        while (correct_num != 0):
            if check_odd_digit(correct_num % 10):
                correct_num //= 10
                msg[i] = "X"
                i -= 1
            else:
                correct_num //= 10
                msg[i] = "-"
                i -= 1
        return msg

    # lambda function for digits divided by 3
    check_divide_by_3 = lambda num: num % 3 == 0

    def divided_by_3(correct_num):

        # func to show digits divided by 3
        print("digits divided by 3: ", end="")
        msg = list('     ')
        i = 4
        while (correct_num != 0):
            if check_divide_by_3(correct_num % 10):
                correct_num //= 10
                msg[i] = "X"
                i -= 1
            else:
                correct_num //= 10
                msg[i] = "-"
                i -= 1
        return msg

    def clues(clue):

        # function for the switch and case of clues
        if clue == 1:
            return yes_or_no(check_if_greater(pin_code), pin_code)
        elif clue == 2:
            return yes_or_no(check_if_smaller(pin_code), pin_code)
        elif clue == 3:
            return print_msg_to_func(msg, sum_of_digits(pin_code))
        elif clue == 4:
            return print_msg_to_func(msg, sub_of_digits(pin_code))
        elif clue == 5:
            return show_string_by_func(msg, odd_digits(pin_code))
        elif clue == 6:
            return show_string_by_func(msg, divided_by_3(pin_code))

    while points > 0 and (guess != pin_code and guess != Key.enter):
        """
        Loop for running the game
        stop if: guess == correct random number / guess == enter / points == 0
        """
        number_of_clue += 1
        print("Clue #", number_of_clue)
        print(clues(random_clue()))
        points -= 10
        print_points(points)
        guess = input("Guess or press Enter for exit: ")
        if guess == "":
            end_game(points)
            return
        else:
            guess = int(guess)
            print()
        while guess < 10000 or guess >= 100000 and guess != Key.enter:
            guess = int(input("Your guess need to be in range (10,000-100,000): "))
        if guess == Key.enter:
            end_game(points)
        if guess == pin_code:
            print("Yes, correct!")
            print_points(points)
            return
        if points == 0:
            end_game(points)
