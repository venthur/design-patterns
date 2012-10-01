#!/usr/bin/env python

from abc import abstractmethod


class FlyBehaviour(object):

    @abstractmethod
    def fly(self):
        pass


# Actual Fly behaviours
class FlyWithWings(FlyBehaviour):

    def fly(self):
        print 'Flying with wings.'


class FlyNoWay(FlyWithWings):

    def fly(self):
        print "Can't fly."


class QuackBehaviour(object):

    @abstractmethod
    def quack(self):
        pass


# Actual Quack behaviours
class Quack(QuackBehaviour):

    def quack(self):
        print 'Quack!'


class MuteQuack(QuackBehaviour):

    def quack(self):
        print '*silence*'


class Squeek(QuackBehaviour):

    def quack(self):
        print 'Squeek!'


class Duck(object):
    """This is not a concrete duck."""

    def __init__(self):
        self.quackBehaviour = QuackBehaviour()
        self.flyBehaviour = FlyBehaviour()

    # the setters allow for changing of behaviour at runtime
    def setFlyBehaviour(self, fb):
        self.flyBehaviour = fb

    def setQuackBehaviour(self, qb):
        self.quackBehaviour = qb

    # performX doesn't handly the X directly but delegates it to the behaviour
    def performFly(self):
        self.flyBehaviour.fly()

    def performQuack(self):
        self.quackBehaviour.quack()


# Here we go, the actual ducks!
class MallardDuck(Duck):

    def __init__(self):
        self.quackBehaviour = Quack()
        self.flyBehaviour = FlyWithWings()


class RubberDuck(Duck):

    def __init__(self):
        self.quackBehaviour = MuteQuack()
        self.flyBehaviour = FlyNoWay()


if __name__ == '__main__':
    md = MallardDuck()
    md.quack()
    md.fly()


