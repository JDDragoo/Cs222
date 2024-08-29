def main():
    students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    print(len(students))

    #print(students[1] [1])
    
    for s in students: #Nested loop
        for c in s:
            print(c)
main()