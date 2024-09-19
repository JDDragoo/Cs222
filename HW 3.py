def main():
    try:
        student_file = open("studentsFiles.txt", 'r')
        students = student_file.readlines()
        student_file.close()

        students_dict = {}
        for line in students:
            student_data = line.split(',')
            student_id = student_data[0]
            students_dict[student_id] = student_data[1:]
        
        while True:
            print("\nChoose An Option:")
            print("1) Search by Last Name")
            print("2) Search by Major")
            print("3) Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                search_field(students_dict, "Last name", 0)
            elif choice == '2':
                search_field(students_dict, "Major", 2)
            elif choice == '3':
                print("Quitting Process...")
                break
            else:
                print("Invalid Input... Select a choice")

    except FileNotFoundError:
        print("File Was Not Found")

def search_field(students, field_name, index):
    search_term = input(f"Enter {field_name} to search for: ")
    found = False
    for student_id, info in students.items():
        if info[index] == search_term:
            print(f"ID: {student_id}, Last Name: {info[0]}, First Name: {info[1]}, Major: {info[2]}, GPA: {info[3]}")
            found = True
        if not found:
            print(f"No student was found with the things requested")


main()