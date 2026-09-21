# students names will be dupliacted 

students=[]

# course name should be unique
courses=set()

while True:
    print("=============== Student Management System =================")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Show Courses ")
    print("5. Exit ")

    choice=input("Enter Choice :: ")

    if choice=="1":
        sid=int(input("Enter Student ID :: "))
        name=input("Enter Student Name :: ")
        course=input("Enter Course Name :: ")
        marks=int(input("Enter Marks :: "))

        student_id=(sid,)
        student={
            "id":student_id,
            "name":name,
            "course":course,
            "marks":marks
        }

        students.append(student)
        courses.add(course)
        print("Student Record added Successfully ")

    elif choice=="2":
        if not students:
            print("NO Data Of Any Student is Found ")
        else:
            for s in students:
                print("=========================================================")
                print()
                print("ID is :: ",s["id"][0])
                print("Name is :: ",s["name"])
                print("Course is :: ",s["course"])
                print("Marks is :: ",s["marks"])

    elif choice=="3":
        search_id=int(input("Enter Student ID to search Student :: "))
        found=False

        for s in students:
            if s["id"][0]==search_id:
                print("Student Found !!! ")
                print(s)
                found=True
                break
            if not found:
                print("Student Not Found ")

    elif choice=="4":
        print("======= Courses Details =========")
        for c in courses:
            print(c)
        print()
    elif choice=="5":
        print("Thank You ")
        break
    else:
        print("Invalid Choice ")










