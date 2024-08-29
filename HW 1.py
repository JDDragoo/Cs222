#Part 1

weight = float(input("Enter your weight in pounds: "))
height = float(input("ENter your hieght in inches: "))

bmi = (weight * 703) / (height ** 2)

if bmi < 18.5:
   type = "Underweight"
elif 18.5 <= bmi <= 25:
   type = "Optimal Weight"
else:
   type = "Overweight"

print(f"your bmi is: {bmi: .2f}")
print(f"your body type is considered: {type}")




#Part 2

total = 0
for number in range (2, 101, 2):
   total += number

print(f"Sum of even numbers from 2 to 200: {total}")



#Part 3

a = int(input("Starting number: "))
b = int(input("Ending number: "))

total = 0

for number in range (a, b + 1):
    if number % 2 != 0:
        total += number
print(f"Sume of odd numbers from A to B: {total}")



#Part 4

target = float(input("Enter the target value: "))
static = 0
while static < target:
    static = float(input("Enter the current stock pricing: "))
else:
    print("The shares can be sold now")


#Part 5

tuition = 8000

for year in range(1, 6):
    print(f"Year {year}: Semester: ${tuition: .2f}")
    tuition *= 1.03
