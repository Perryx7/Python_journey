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



def add_student (students, student_name, grade_student):
     students[student_name] = grade_student

     return students

def upgrade_grade():
      pass  # TODO: implement upgrade  logic
def display_student():
       pass  # TODO: implement display  logic
def main():
    students = {}
    print("Welcome to the Student Grade Tracker!")

    while True : 
         choice = get_menu_choice()

         if choice == "1" : 
              
              student_name = input("Enter a name ")
              student_grade = int(input("Enter the grade: "))
              
              if not student_name : 
                   print("The name can't be empty")
              elif student_grade < 0 or student_grade > 20 :
                   print("Enter a valid grade ")
              else:
                   add_student(students, student_name, student_grade)
                   print(students)

        #  elif choice == "2" :

        #       name_update = input("Enter the name of the students you want to update the grade") 

        #       if name_update not in students : 
        #            print("the student don't exit ")
        #       else:
        #            new_note = int(Enter a new note)

         
         
              #add_student(students, student_name, grade_student)

 



if __name__ == "__main__":
    main()