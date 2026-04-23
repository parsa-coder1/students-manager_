import json

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def add_student(students, next_id):
    name = input("name: ")
    age_input = input("age: ")
    if age_input.isdigit():
        age = int(age_input)
    else:
        print("invalid age!")
        return next_id
    class_name = input("class name: ")
    grade = input("grade: ")

    if any(s["name"] == name and s["class"] == class_name for s in students):
        print("this student already exists!")
        return next_id
    
    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "class": class_name,
        "grade": grade
    }

    students.append(student)
    return next_id + 1


def show_students(students):
    if not students:
        print("no student found!")
        return
    
    for s in students:
        print(f"id: {s['id']} | name: {s['name']} | age: {s['age']} | class_name: {s['class']} | grade: {s['grade']}")


def update_student(students):
    student_id = int(input("enter student's id to update: "))

    for s in students:
        if s["id"] == student_id:
            new_name = input("enter new name (leave empty to keep previous)")
            new_age_input = input("enter new age (leave empty to keep previous)")
            if new_age_input:
                new_age = int(new_age_input)
            else:
                print("invalid new age!")
                return next_id
            new_class_name = input("enter new class name (leave empty to keep previous)")
            new_grade = input("enter new grade (leave empty to keep previous)")

            if new_name:
                s["name"] = new_name

            if new_age:
                s["age"] = new_age

            if new_class_name:
                s["class"] = new_class_name

            if new_grade:
                s["grade"] = new_grade

            print("updated successful!")
            return

    print("no student found!")


def delete_student(students):
    student_id = int(input("enter student's id to remove: "))

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("removed successful!")
            return
        
    print("no student found!")


def search_student(students):
    name = input("enter name to search: ")

    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"id: {s['id']} | name: {s['name']} | age: {s['age']} | class_name: {s['class']} | grade: {s['grade']}")
            found = True

    if not found:
        print("no student found!")


# main program 


students = load_data()

if students:
    next_id = max(s["id"] for s in students) + 1
else:
    next_id = 1

while True:

    print("\n=== student manager ===")
    print("1. add student")
    print("2. show students")
    print("3. update student")
    print("4. delete student")
    print("5. search student")
    print("6. exit")

    choice = input("choose: ").strip()

    if choice == "1":
        next_id = add_student(students, next_id)
        save_data(students)

    elif choice == "2":
        show_students(students)

    elif choice == "3":
        update_student(students)
        save_data(students)

    elif choice == "4":
        delete_student(students)
        save_data(students)

    elif choice == "5":
        search_student(students)

    elif choice == "6":
        print("goodbye!")
        break

    else:
        print("invalid choice!")
        