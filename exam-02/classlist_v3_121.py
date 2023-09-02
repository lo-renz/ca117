#!/usr/bin/env python3

def tagger(item):
    return item[0]

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.d = {}

    def __str__(self):
        slist = []
        slist.append('Name: {:s}'.format(self.name))
        slist.append('CAO: {:d}'.format(self.cao))
        return '\n'.join(slist)

    def add_grade(self, subject, grade):
        self.d[subject] = grade

    def get_grade(self, subject):
        if subject in self.d.keys():
            return self.d[subject]
        return 'N/A'

class Classlist(object):

    def __init__(self):
        self.d = {}

    def add(self, student):
        self.d[student.cao] = student

    def remove(self, cao):
        if cao in self.d.keys():
            del(self.d[cao])

    def lookup(self, cao):
        if cao in self.d:
            return self.d[cao]
        return None

    def __str__(self):
        slist = [f'{s}' for s in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)

    def most_popular_subject(self):
        subjects = []
        for student in self.d.values():
            subjects.append(str(student.d.items()))

        p = {}
        for subject in subjects:
            if subject not in p:
                p[subject] = 1
            elif subject in p:
                p[subject] += 1

        most_popular = []
        for k, v in sorted(p.items(), key=tagger):
            most_popular.append(k)

        return most_popular[0][14:21]


def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H1')
    s1.add_grade('irish', 'O4')

    s2.add_grade('english', 'H2')
    s2.add_grade('french', 'O5')
    s2.add_grade('spanish', 'O1')

    s3.add_grade('english', 'O3')
    s3.add_grade('irish', 'O3')

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.most_popular_subject())


if __name__ == '__main__':
    main()

