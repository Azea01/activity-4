# This Python program demonstrates how to create, modify and use python lists.
# It illustrates also how to create and use python tuples.

# Name :  joe Akakpo
# Class:  ISQA 3900
# Date :  September 24,2021
from statistics import mean


def remove(names):
    print(
        "Initial List of Names\n ['maria','maria','will','sam','maria','kahn','sam','barry','george','hank',"
        "'belinda','maria','karthik']\n")

    print("List of unique names after running through the de-duplicator program")

    final_list = []
    for num in names:
        if num not in final_list:
            final_list.append(num)
    return final_list


names = ['maria', 'maria', 'will', 'sam', 'maria', 'kahn', 'sam', 'barry', 'george', 'hank', 'belinda', 'maria',
         'karthik']

print(remove(names))


def main():
    grades = getScores()
    grade = mean(grades)
    abcGrade = getGrade(grade)
    print("\nScores: ", grades)
    print("Total: ", sum(grades))
    print("Average Score: ", grade)
    print("Letter grade: ", abcGrade)


def getScores():
    grades = []
    while True:
        grade = int(input("Enter test score(-1 to quit): "))
        if grade == -1:
            return grades
        grades.append(grade)
        for grade in grades:
            if grade < 0 or grade >= 101:
                print("You must enter integer values >=0 and <=100 or -1 to quit. Try again.")
                grades.remove(grade)


def getGrade(grade):
    best = 100
    if grade >= best - 8:
        return 'A'
    elif grade >= best - 12:
        return 'B+'
    elif grade >= best - 18:
        return 'B'
    elif grade >= best - 22:
        return 'C+'
    elif grade >= best - 30:
        return 'C'
    elif grade >= best - 40:
        return 'D'

    else:
        return 'F'


main()

