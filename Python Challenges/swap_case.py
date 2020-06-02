def swap_case(s):
    # "swapcase()" method -> method converts all uppercase characters to lowercase and vice versa of the given string, and returns it.
    return (s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
