gradenum = int(input("What was your test percentage???"))

if gradenum >= 95:
    print("A+")
elif gradenum >= 90 and gradenum < 95:
    print("Your grade is an *A*")
elif gradenum >= 80 and gradenum < 90:
    print("Your grade is a *B*")
elif gradenum >= 70 and gradenum < 80:
    print("Your grade is a *C*")
elif gradenum >= 60 and gradenum < 70:
    print("Your grade is a *D*")
elif gradenum >= 0 and gradenum < 60:
    print("Your grade is an *F*")
    print("You failed the test.")