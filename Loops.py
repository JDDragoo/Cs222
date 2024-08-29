for counter in range(10):
    print(counter)
    if counter == 5: #This breaks and stops continuing 
        break



for counter in range(10):
    if counter == 5:
        continue #Skips only for that one point
    print(counter)
