dogsPer = 10
bunsPer = 8

people = int(input("Enter the amount of people at the cookout: "))
dogsPerPerson = int(input("Enther the amount of hot dogs each person will eat: "))

totalAmount = people * dogsPerPerson
hotDogAmount = (totalAmount + dogsPerPerson - 1) // dogsPer
totalBuns = totalAmount
bunPack = (totalBuns + bunsPer - 1) // bunsPer
totalHotDogsAvailable = bunPack * dogsPer
leftOverDogs = totalHotDogsAvailable - totalAmount
totalBunsAvailable = bunPack * bunsPer
leftOverBuns = totalBunsAvailable - totalAmount

print(f"Minimum number of packages of hot dogs needed: {hotDogAmount}")
print(f"Minimum number of packages of bun needed: {bunPack}")
print(f"Number of left over hot dogs: {leftOverDogs}")
print(f"Number of buns left over: {leftOverBuns}")