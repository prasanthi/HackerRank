def count_substring(string, sub_string):
    occurances = 0
    # Iterate until the length of the main string
    for i in range(len(string)):
        # Search for the substring in the main string
        if (string[i:i+len(sub_string)] == sub_string):
            # if there are any matches increment the count
            occurances += 1
        # return the count of occurances of substring
    return (occurances)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
