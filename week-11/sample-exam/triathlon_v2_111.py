#!/usr/bin/env python3

def sort_on(t):
    return t.name

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        slist = []
        slist.append('Name: {:s}'.format(self.name))
        slist.append('ID: {:d}'.format(self.tid))
        return '\n'.join(slist)

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, t):
        self.d[t.tid] = t

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid in self.d.keys():
            return self.d[tid]
        return None

    def __str__(self):
        slist = [f'{t}' for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)


if __name__ == '__main__':
    main()
