class Solution(object):


 if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

        second_lowest_score = sorted(set(student[1] for student in students))[1]

        students_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_score]

        students_with_second_lowest.sort()
        for name in students_with_second_lowest:
            print(name)
