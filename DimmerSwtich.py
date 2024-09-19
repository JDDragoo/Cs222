class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    def show(self):
        print(self.switchIsOn)
        print(self.brightness)

def main():
    d0 = DimmerSwitch()
    d1 = DimmerSwitch()
    d1.turnOn()
    for counter in range(20): #This is showing the countermeger that it can't pass 10 becuase we set it up to not go higher than 10
        d1.raiseLevel()

    d1.raiseLevel()
    d1.raiseLevel()
    d1.raiseLevel()
    d0.show()
    d1.show()

main()