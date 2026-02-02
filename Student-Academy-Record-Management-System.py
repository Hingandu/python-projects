# this dictionary is where all students are stored
students = {}

# this is the function that calculates and returns the grade
# it receives the average marks and decides which grade to give
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


# this is the main while loop that keeps the program running
# the program will only stop when the user chooses option 6
while True:

    # this prints the menu so the user can see the options
    print("""
1. Add Student
2. View Students
3. Student Report
4. Update Marks
5. Delete Student
6. Exit
""")

    # this asks the user to choose an option from the menu
    ch = input("Choose option: ")

    # this is the part that adds a new student
    if ch == "1":

        # this asks for the student basic information
        sid = input("Enter student ID: ")
        name = input("Enter student name: ")
        cls = input("Enter class: ")

        # this dictionary is for storing subjects and their marks
        subjects = {}

        # this is the for loop that runs 3 times to enter 3 subjects
        for i in range(3):
            sub = input("Enter subject name: ")
            mark = int(input("Enter marks: "))
            subjects[sub] = mark  # this saves the subject and its marks

        # this saves the student details inside the main students dictionary
        students[sid] = {
            "name": name,
            "class": cls,
            "subjects": subjects
        }

        print("Student added")

    # this is the part that shows all students
    elif ch == "2":

        # this loop goes through all students and prints ID and name
        for sid, s in students.items():
            print("ID:", sid, "Name:", s["name"])

    # this is the part that shows a full student report
    elif ch == "3":

        # this asks for the student ID
        sid = input("Enter student ID: ")

        # this checks if the student exists
        if sid in students:
            s = students[sid]

            # this calculates the total marks by adding all subject marks
            total = sum(s["subjects"].values())

            # this calculates the average marks
            avg = total / len(s["subjects"])

            # this prints student details
            print("Name:", s["name"])
            print("Class:", s["class"])

            # this is the loop that shows subjects and marks
            # it goes through each subject one by one and prints it
            for sub, m in s["subjects"].items():
                print(sub, "=", m)

            print("Average:", avg)
            print("Grade:", grade(avg))
        else:
            print("Student not found")

    # this is the part that updates marks for a subject
    elif ch == "4":

        # this asks for student ID and subject name
        sid = input("Enter student ID: ")
        sub = input("Enter subject name: ")

        # this checks if the student and subject exist before updating
        if sid in students and sub in students[sid]["subjects"]:
            students[sid]["subjects"][sub] = int(input("Enter new marks: "))
            print("Marks updated")
        else:
            print("Student or subject not found")

    # this is the part that deletes a student
    elif ch == "5":

        # this asks for the student ID
        sid = input("Enter student ID: ")

        # this checks if the student exists and removes them
        if sid in students:
            del students[sid]
            print("Student deleted")
        else:
            print("Student not found")

    # this is the part that exits the program
    elif ch == "6":
        print("Goodbye From Emmanuel Hing'andu")
        break
