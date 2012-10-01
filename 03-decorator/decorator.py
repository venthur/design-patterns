#!/usr/bin/env python


class Beverage(object):

    def __init__(self):
        self.description = "Unknown Beverage."

    def cost(self):
        return 0.0

    def getDescription(self):
        return self.description


class CondimentDecorator(Beverage):

    pass


class Espresso(Beverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):

    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return .89


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return .20 + self.beverage.cost()




if __name__ == '__main__':
    beverage = Espresso()
    print beverage.getDescription() + ' $' + str(beverage.cost())

    beverage = HouseBlend()
    beverage = Mocha(beverage)
    print beverage.getDescription() + ' $' + str(beverage.cost())



