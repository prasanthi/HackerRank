def print_formatted(number):
    # your code goes here
    # Inorder match the space between the values according to given condition that "Each value should be space-padded to match the width of the binary value of ."
    width = len(str(bin(number))[2:])
    for i in range(1,number+1):
        # "oct()" -> used to find the octal value
        # "hex()" -> used to find the hexadecimal value
        # As we need capitalized hexadecimal use "upper()" method
        # "bin()" -> used to find the binary values
        # "rjust()" -> right align the values according to the calculated width and space
        print(str(i).rjust(width,' '), oct(i)[2:].rjust(width,' '), hex(i)[2:].upper().rjust(width,' '), bin(i)[2:].rjust(width,' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
