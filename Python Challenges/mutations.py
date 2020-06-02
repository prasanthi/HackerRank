def mutate_string(string, position, character):
    # Covert string into a list.
    string_list = list(string)
    # Iterate over the list till the length of the list.
    for i in range(len(string_list)):
        # Check whether i is equal to position given.
        if (i == position):
            # Assign the character that needs to be changed in the specified position.
            string_list[i] = character
    # join and make the list to string.
    return ("".join(string_list))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
