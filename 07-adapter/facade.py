#!/usr/bin/env python


# Imagine a bunch of low level classes for each component of the home theater,
# like a class for the amp, the tuner, etc.


class HomeTheaterFacade(object):

    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self, movie):
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd(self.dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play()

    def endMovie(self):
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()


if __name__ == '__main__':
    homeTheater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

    homeTheater.watchMovie('Raiders of the lost ark')
    homeTheater.endMovie()

