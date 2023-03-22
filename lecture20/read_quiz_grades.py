f = open("data/quiz_grades.csv", "r")
quiz1 = []
quiz2 = []
f.readline() # read the header and discard it
for line in f:
    cols = line.split(",")
    quiz1.append(float(cols[0]))
    quiz2.append(float(cols[1]))
f.close()

f = open("data/best_quiz_grade.csv", "w")
for i in range(len(quiz1)):
    best_grade = max(quiz1[i], quiz2[i])
    f.write(f"{best_grade:.1f}\n")
    # f.write(str(best_grade) + "\n") # alternative conversion to str
f.close()
