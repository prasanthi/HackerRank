if __name__ == '__main__':
    name_scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in name_scores:
            name_scores[score].append(name)
        else:
            name_scores[score] = [name]
    sorted_namescore = sorted(name_scores.keys())
    solution = name_scores[sorted_namescore[1]]
    for i in sorted(solution):
        print (i)
