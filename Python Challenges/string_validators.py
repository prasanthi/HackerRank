if __name__ == '__main__':
    string = input()
    # "any()" function -> returns True if any element of an iterable is True
    # i.e, we need to return true even one character matches the criteria.
    # "isalnum()" -> Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
    print(any([s.isalnum() for s in string]))
    # "isalpha()" -> Returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.
    print(any([s.isalpha() for s in string]))
    # "isdigit()" -> Returns true if all characters in the string are digits and there is at least one character, false otherwise.
    print(any([s.isdigit() for s in string]))
    # "islower()" -> Returns true if all cased characters 4 in the string are lowercase and there is at least one cased character, false otherwise.
    print(any([s.islower() for s in string]))
    # "isupper()" -> Returns true if all cased characters 4 in the string are uppercase and there is at least one cased character, false otherwise.
    print(any([s.isupper() for s in string]))
