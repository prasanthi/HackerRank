if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    #create a tuple t with integer_list element use "tuple()" function
    t = tuple(integer_list)
    # Inorder to create a hash for tuple use "hash()" function
    print (hash(t))
