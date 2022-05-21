import math


def cube_volume(length):
    # this function calculates the volume of a cube

    # process
    volume = length**3

    return volume


def main():
    # this function accepts cube length

    # input
    while True:
        length_str = input("Enter Length (cm): ")
        try:
            length = float(length_str)
        except Exception:
            print("That is not a number, please input a number!")
            print("")
        else:
            if length <= 0:
                print("You have not inputted a valid base length, please input"" a positive number!")
                print("")
            else:
                break
    print("\nDone.")


if __name__ == "__main__":
    main()
