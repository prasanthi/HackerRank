# Enter your code here. Read input from STDIN. Print output to STDOUT
#Mat size must be N X M. ( N is an odd natural number, and M is 3 times N.)
n,m = map(int,raw_input().split())
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
