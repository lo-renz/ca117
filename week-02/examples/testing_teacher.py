#!/usr/bin/env python3

def main1(filename):
    
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

def main02(filename):

    try:
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

    except FileNotFoundError:
        print(f'Could not open: {filename:s}')

# main1('input.txt')
main02('input.txt')
