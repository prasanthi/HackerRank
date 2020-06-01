if __name__ == '__main__':
    # Enter number of Commands
    N = int(input())
    # Consider a list
    List = []
    # Iterate till it reaches the number of Commands N
    for i in range(N):
        # Split all the Commands inorder to perform operations accordingly
        Commands = input().split()
        # Check if the command type is insert
        if (Commands[0] == "insert"):
            # Insert the element at the given position into the list by using "insert()" method
            List.insert(int(Commands[1]),int(Commands[2]))
        # Check if the command type is print
        elif (Commands[0] == "print"):
            # Print the list by using the "print()" function
            print (List)
        # Check if the command type is remove
        elif (Commands[0] == "remove"):
            # Search the element in the list that needs to be removed and remove the element by using "remove()" method
            List.remove(int(Commands[1]))
        # Check if the command type is append
        elif (Commands[0] == "append"):
            # Add the given element at the end of the list by using "append()" method
            List.append(int(Commands[1]))
        # Check if the command type is sort
        elif (Commands[0] == "sort"):
            # Sort the list by using "sort()" method
            List.sort()
        # Check if the command type is pop
        elif (Commands[0] == "pop"):
            # Remove and return the element by using "pop()" method
            List.pop()
        # Check if the command type is reverse
        elif (Commands[0] == "reverse"):
            # Reverse the list by using "reverse()" method.
            List.reverse()
