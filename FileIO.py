def main():
    try:
        StudentList = open("Students.txt", 'r') # r = read, w = write
        students = StudentList.readlines()
        StudentList.close()
        #print(students)
        fileOutput = open("output.txt", 'a') # a = appending
        for s in students:
            #print(s)
            parts = s.split(',')
            #print(parts[0])
            if parts[2] == "Math":
                print(s)
            fileOutput.write(parts[1] + "'s GPA is " + parts[3] + "\n")
            fileOutput.close()
    except FileNotFoundError:
        print("File not Found")
main()