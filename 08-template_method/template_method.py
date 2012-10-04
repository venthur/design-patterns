#!/usr/bin/env python


class CaffeineBeverage(object):

    def prepareReceipe(self):               # the template method
        self.boilWater()                    # concrete operation
        self.brew()                         # primitive operation
        self.pourInCup()                    # concrete operation
        if self.customerWantsCondiments():  # hook
            self.addCondiments()            # primitive operation

    def boilWater(self):
        print 'Boiling water.'

    def pourInCup(self):
        print 'Pouring in cup.'

    def brew(self):
        pass

    def addCondiments(self):
        pass

    def customerWantsCondiments(self):
        # default implementation, can be overwritten
        return True


class Tea(CaffeineBeverage):

    def brew(self):
        print 'Steeping the tea'

    def addCondiments(self):
        print 'Adding lemon'


class CoffeeWithHook(CaffeineBeverage):

    def brew(self):
        print 'Dripping coffee through filter.'

    def addCondiments(self):
        print 'Adding sugar and milk'

    def customerWantsCondiments(self):
        answer = raw_input('Would you like milk and sugar with your coffee? (y/n)? ')
        if answer.lower().startswith('y'):
            return True
        else:
            return False


if __name__ == '__main__':
    tea = Tea()
    coffee = CoffeeWithHook()

    print 'Making tea...'
    tea.prepareReceipe()
    print 'Making coffee...'
    coffee.prepareReceipe()
