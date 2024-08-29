def main():
    midterm = [90, 80, 100, 75, 82, 80]
    #index     0,  1,   2,  3,  4

    print(midterm[1]) #printing out the element for the input at the index, List printing index

    for m in midterm:
        print(m)

    print((len(midterm))) #shows the length, this would be 5 things in the list

    print(max(midterm)) #this shows the highest or max number

    midterm.append(93) #adds the information to the end of the list

    midterm.insert(2, 70) #this is putting number 70 into the second index

    print(midterm)

    midterm.remove(80) #this is how you remove something from a list, it will remove the first instance

    print(midterm)

    print(midterm[2:4]) #printing 2 to 4 so you would be printing the elements of the index but not including 4

    print(midterm[3:]) #print the index from 3 and beyond

    print(midterm[ :2]) #start at zero and go up to but not including index 2

main()