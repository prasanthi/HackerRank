if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
# Logic given in problem without using List Comprehensions
# ar = []
# p = 0
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [i,j,k]
#                 p+=1
# print (ar)
#List comprehensions allow us to transform one list or other sequence into a new list. They provide a concise syntax for completing this task, limiting our lines of code.
#List comprehensions follow the mathematical form of set-builder notation or set comprehension, so they may be particularly intuitive to programmers with a mathematical background.
# Using List Comprehensions modified the above code.
arr = [[i, j, k]for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k!=n]
print(arr)
