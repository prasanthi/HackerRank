if __name__ == '__main__':
    # Enter Number of students
    n = int(input())
    # Initialise a dictionary to enter students grades and marks
    student_marks = {}
    # Save the records of names and marks entered into student_marks dictionary data type
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # query_name contains the students name entered by user whose average percentage marks needs to be finded out.
    query_name = input()
    avgMarks = 0.00
    #Iterate over the dictionary student_marks
    for names,grades in student_marks.items():
        # check for query_name in the dictionary
        if(names == query_name):
            # Find out average of the grades
            avgMarks = sum(grades)/ float(len(grades))
    # As we need the average correct to two decimal places use "%.2f"
    print ("%.2f" % avgMarks)
