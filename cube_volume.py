#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the area of a cube


def vol(length):
    # This functions calculates volume

    volume = length**3
    return volume


def main():
    # This function receives input

    # Input
    while True:
        length_str = input("Enter Length (cm): ")
        try:
            length_int = float(length_str)
        except Exception:
            print("\nThat is not a number you dunce! try again")
            print("")
        else:
            if length_int <= 0:
                print("\nlength value must be a positive you dunce! try again")
                print("")
            else:
                break

    # Call Functions
    volume = vol(length_int)

    # Output
    print("")
    print("Volume is {0}cm^3".format(volume))
    print("\nDone")


if __name__ == "__main__":
    main()
