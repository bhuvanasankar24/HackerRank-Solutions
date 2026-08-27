if __name__ == '__main__':
    students=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[name, score]
        students.append(student)
        scores.append(score)
    scores=set(scores)
    li=list(scores)
    li.sort()
    second_lowest_score = li[1]
    result=[]
    for student in students:
        if student[1]== second_lowest_score:
            result.append(student[0])
    result.sort()
    for name in result:
        print(name)
