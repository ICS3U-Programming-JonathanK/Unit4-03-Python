#!/usr/bin/env python3

# Created by: Jonathan
# Created on: May 25, 2021
# This program asks the user for a whole number. It
# then calculates the square of the number given starting from 0


def main():
    # initialize the counter
    counter = 0

    # get the user number as a string
    user_number_string = input("Enter a whole number: ")
    try:
        user_number_int = int(user_number_string)
    except ValueError:
        print("")
        print("Please enter a valid number")

    else:
        # calculates the square of each number from 0 to the user number
        for counter in range(user_number_int + 1):
            power_of_two = counter**2
            print("{}^2 = {}".format(counter, power_of_two))
        if (user_number_int >= 0):
            print("")
            print("{}^2 = {}".format(user_number_int, power_of_two))
        else:
            print("")
            print("{0} is not a valid number".format(user_number_int))
    finally:
        print("")
        print("Thank you for your input")


if __name__ == "__main__":
    main()
