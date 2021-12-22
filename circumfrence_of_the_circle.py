#!/usr/bin/env python3
# Created by: Shahd Elsaman
# Created on: December 2021
# This program calculates the circumference of a circle
#     with user input


import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("Circumference is {} mm².".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
