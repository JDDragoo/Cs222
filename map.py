def square(x):
    return x * x
numbers = [1,2,3,4,5]
squares = map(square, numbers)
print(list(squares))

fruits = ["apple","banana","cherry"]
WordLengths = list(map(len, fruits))
print(WordLengths)


def ConvertToUpper(n):
    return n.upper()
names = ["alice", "Bob", "carol", "Dave", "eve"]
print(list(map(ConvertToUpper, names)))