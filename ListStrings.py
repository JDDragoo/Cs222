def main():
    students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    print(len(students))

    print(students[1] [1])
    
    for s in students: #Nested loop
        for c in s:
            print(c)
    afc =       [["Colts", "Titans", "Jaguars", "Texans"],
                ["Patriots", "Jets", "Dolphines", "Bills"],
                ["Steelers", "Bengals", "Ravens", "Browns"],
                ["Broncos", "Chargers", "Chiefs", "Raiders"]]
    print(len(afc[0][2][3]))


main()