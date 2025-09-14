# students grade tracker
# Ask the user to enter student names and their grades.
# Allow them to:
# Add a student with a grade
# Update a grade
# Display all students and their grades
# Example: { "Alice": 15, "Bob": 12 }


def get_menu_choice():
    """Display menu and get user choice."""
    print("\n" + "-"*25)
    print("STUDENT GRADE TRACKER")
    print("-"*25)
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Display all students")
    print("4. Exit")
    print("-"*25)

    
    choice = input("Choose an option (1-4): ").strip()
    return choice



def add_students(students):
    """Add multiple students until user types 'stop'."""
    while True:
        student_name = input("Enter a name (or type 'stop' to finish): ").strip()
        if student_name.lower() == "stop":
            break

        if not student_name:
            print("❌ The name can't be empty")
            continue

        grade_input = input("Enter the grade (0-20): ")

        if grade_input.isdigit():   # ✅ check if is a valid number
            student_grade = int(grade_input)
            if 0 <= student_grade <= 20:
                students[student_name] = student_grade
                print(f"✅ {student_name} added with grade {student_grade}")
            else:
                print("❌ Enter a valid grade between 0 and 20")
        else:
            print("❌ Please enter numbers only for the grade")


def upgrade_grade(students):
    
    name_student = input("Enter the name of the student  you want to update:  ")

    if name_student not in students : 
         print("student not found")
    else:
         updated_grade = int(input("enter the new grade: "))
         students[name_student] =updated_grade
            
def display_student(students):
    """Display all the students."""
    if not students:   # if the dictionnary is empty
        print("⚠️ No students")
    else:
        for student, grade in students.items():
            print(f"Student: {student}, Grade: {grade}")

def main():
    students = {}
    print("Welcome to the Student Grade Tracker!")

    while True : 
         choice = get_menu_choice()

         if choice == "1" :            
             add_students(students)
            
                  
         elif choice == "2" : 
              upgrade_grade(students)
          
         elif choice == "3" : 
              display_student(students)
         elif choice == "4" :
              break
              





 



if __name__ == "__main__":
    main()