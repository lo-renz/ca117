#!/usr/bin/env python3

class Lamp(object):

    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        if self.on is False:
            self.on = True

    def turn_off(self):
        if self.on is True:
            self.on = False

    def toggle(self):
        if self.on is True:
            self.on = False
        elif self.on is False:
            self.on = True


def main():
    lamp1 = Lamp()

    assert(not(lamp1.on))
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.toggle()
    assert(lamp1.on)
    lamp1.turn_off()
    lamp1.turn_off()
    assert(not(lamp1.on))

    lamp2 = Lamp(True)

    assert(lamp2.on)
    lamp2.toggle()
    assert(not(lamp2.on))


if __name__ == '__main__':
    main()
