#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def __str__(self):
        slist = []
        slist.append('Name: {:s}'.format(self.name))
        slist.append('ID: {:d}'.format(self.tid))
        slist.append('Race time: {:d}'.format(self.totaltime))
        return '\n'.join(slist)

    def add_time(self, sport, time):
        self.d[sport] = time
        self.totaltime = sum(self.d.values())

    def get_time(self, sport):
        return self.d[sport]


def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)


if __name__ == '__main__':
    main()
