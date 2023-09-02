#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    contacts = {}
    for line in f:
        name, number = line.strip().split()
        contacts[name] = number

for line in sys.stdin:
    name = line.strip()
    slist = []

    try:
        slist.append('Name: {}'.format(name))
        slist.append('Phone: {}'.format(contacts[name]))
        print('\n'.join(slist))
    except KeyError:
        slist.append('No such contact')
        print('\n'.join(slist))
