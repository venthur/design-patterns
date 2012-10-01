#!/usr/bin/env python


class Subject(object):
    """The 'observable' base class."""

    def __init__(self):
        self.observers = []

    def registerObserver(self, o):
        self.observers.append(o)

    def removeObserver(self, o):
        self.observers.remove(o)

    def notifyObservers(self):
        for i in self.observers:
            i.update()


class Observer(object):
    """The observer base class."""

    def __init__(self, subject):
        self.subject = subject
        self.subject.registerObserver(self)

    def update(self):
        pass


# Concrete implementations
class WeatherData(Subject):

    def __init__(self):
        Subject.__init__(self)
        self.temp = 25.2
        self.humidy = 50.2

    def getTemperature(self):
        return self.temp

    def getHumidy(self):
        return self.humidy


class CurrentConditionsDisplay(Observer):

    def update(self):
        print self.subject.getTemperature()


class ForecastDisplay(Observer):

    def update(self):
        print self.subject.getTemperature() + 10


if __name__ == '__main__':
    wd = WeatherData()
    ccd = CurrentConditionsDisplay(wd)
    fcd = ForecastDisplay(wd)

    wd.notifyObservers()
    # change some vaues and notify the observers
    wd.temp = 27.0
    wd.humidy = 10.0
    wd.notifyObservers()

