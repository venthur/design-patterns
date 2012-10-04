#!/usr/bin/env python


import random


class State(object):

    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass


class NoQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print 'You inserted a quarter.'
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print "You haven't inserted a quarter."

    def turnCrank(self):
        print "You turned, but there's no quarter."

    def dispense(self):
        print "You need to pay first"


class HasQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print 'You cannot insert another quarter.'

    def ejectQuarter(self):
        print "Quarter returned"
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print "You turned..."
        if random.randint(0, 10) == 0 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print "No gumball dispensed"


class SoldState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "Please wait, we're already giving you a gumball."

    def ejectQuarter(self):
        print "Sorry, you already turned the crank."

    def turnCrank(self):
        print "Turning twice doesn't get you another gumball!"

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print "Oops, out of gumballs!"
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class WinnerState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "Please wait, we're already giving you a gumball."

    def ejectQuarter(self):
        print "Sorry, you already turned the crank."

    def turnCrank(self):
        print "Turning twice doesn't get you another gumball!"

    def dispense(self):
        print "YOU'RE A WINNER! You get two gumballs for your quarter"
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print "Oops, out of gumballs!"
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class SoldOutState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "You can't insert a quarter, the machine is sold out"

    def ejectQuarter(self):
        print "Can't eject, you haven't inserted a quarter yet"

    def turnCrank(self):
        print "You turned, but there are no gumballs"

    def dispense(self):
        print "No gumball dispensed"


class GumballMachine(object):

    def __init__(self, numberGumballs):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        self.count = numberGumballs
        if numberGumballs > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
        self.state = state

    def releaseBall(self):
        print "A gumball comes rolling out the slot..."
        if self.count != 0:
            self.count -= 1

    def getSoldOutState(self):
        return self.soldOutState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def getWinnerState(self):
        return self.winnerState

    def getCount(self):
        return self.count

    def __str__(self):
        return "Inventory: %i gumballs" % self.getCount()


if __name__ == '__main__':
    gumballMachine = GumballMachine(5)

    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print gumballMachine

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print gumballMachine

    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()


    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()



