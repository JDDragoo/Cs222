class Person:
    def _init__(self, name, age):
        self.name = name
        self.__age = age #This makes it a private variable two double underscores makes a variable private and won't print
    def show(self):
        print(self.name)
        print(self.__age)
def main():
    p0 = Person("Alice", 23)
    p1 = Person("Bob", 25)
    p0.show()
main()