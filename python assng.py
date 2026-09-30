def student_grade():
    try:
        name = input("Enter student's name: ")
        marks = float(input("Enter student's marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")

        elif marks >= 90:
            grade = "A"
            print("Student Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)

        elif marks >= 80:
            grade = "B"
            print("Student Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)

        elif marks >= 70:
            grade = "C"
            print("Student Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)

        elif marks >= 60:
            grade = "B"
            print("Student Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)

        else:
            grade = "F"
            print("Student Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)

    except Exception as e:
        print("Error:", e)
        print("Please enter a valid number for marks.")


student_grade()
