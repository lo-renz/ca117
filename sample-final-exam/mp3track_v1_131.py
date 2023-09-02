#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        slist = []
        slist.append('Title: {}'.format(self.title))
        slist.append('Duration: {}'.format(self.duration))
        return '\n'.join(slist)


def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    assert(t1.title == 'Fools Gold')
    assert(t1.duration == 604)

    print(t1)
    print(t2)
    print(t3)


if __name__ == '__main__':
    main()
