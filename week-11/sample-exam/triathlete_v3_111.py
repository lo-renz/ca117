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

    def __eq__(self, other):
        return self.totaltime == other.totaltime

    def __lt__(self, other):
        return self.totaltime < other.totaltime

    def __gt__(self, other):
        return self.totaltime > other.totaltime


def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)


if __name__ == '__main__':
    main()
