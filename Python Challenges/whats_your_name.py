def print_full_name(a, b):
    # print the string in the given format
    # "sep" parameter -> to specify separation of strings
    print("Hello ", a," ",b,"! You just delved into python.",sep='')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
