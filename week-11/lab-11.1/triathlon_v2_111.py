#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.triathlon = {}

    def add(self, triathlete):
        self.triathlon[triathlete.tid] = triathlete

    def remove(self, tid):
        self.triathlon.pop(tid)

    def lookup(self, tid):
        if tid in self.triathlon.keys():
            return self.triathlon[tid]

    def __str__(self):
        



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
