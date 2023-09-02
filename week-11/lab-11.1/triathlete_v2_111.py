#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.racetime = {}

    def add_time(self, sport, time):
        self.racetime[sport] = time
        self.totaltime = sum(self.racetime.values())

    def get_time(self, sport):
        return self.racetime[sport]

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.totaltime)


def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)


if __name__ == '__main__':
    main()
