#!/usr/bin/env python


from threading import Thread
import time


# I've only implemented the virtual proxy from the book as the other two
# examples where Java specific.

class Icon(object):
    """Icon 'Interface'."""

    def getIconWidth(self):
        pass

    def getIconHeight(self):
        pass

    def paintIcon(self, c, g, x, y):
        print self


class ImageProxy(Icon):
    """Virtual Proxy for Icon"""

    def __init__(self, url):
        self.imageUrl = url
        self.imageIcon = None
        self.retrieving = False

    def getIconWidth(self):
        if self.imageIcon is None:
            return 800
        else:
            return self.imageIcon.getIconWidth()

    def getIconHeight(self):
        if self.imageIcon is None:
            return 600
        else:
            return self.imageIcon.getIconHeight()

    def paintIcon(self, c, g, x, y):
        # if we don't have the image yet show a substitute, download the real
        # one, and paint it
        if self.imageIcon is None:
            print "Loading CD cover, please wait..."
            if not self.retrieving:
                self.retrieving = True
                def get_image():
                    time.sleep(1)
                    self.imageIcon = Icon()
                    self.imageIcon.paintIcon(c, g, x, y)
                t = Thread(target=get_image)
                t.start()
        # if we have it already, paint it
        else:
            self.imageIcon.paintIcon(c, g, x, y)


if __name__ == '__main__':
    ip = ImageProxy('foo')
    ip.paintIcon(1, 2, 3, 4)
    time.sleep(2)
    ip.paintIcon(1, 2, 3, 4)
