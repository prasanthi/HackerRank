def split_and_join(line):
    # write your code here
    # "split(" ")" method -> splits a string into a list by using space as delimiter
    split_line = line.split(" ")
    # "join()" method -> joins each element of an iterable (such as list, string and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.
    # ""-".join()" method -> "-" is used as we need a hypen seperator between strings
    join_line = "-".join(split_line)
    return join_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
