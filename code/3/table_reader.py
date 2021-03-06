# from __future__ import print_function, division

__author__ = 'amrit'

import sys, string, re, math

sys.dont_write_bytecode = True


## Code for Num, Sym class have been taken from https://github.com/txt/fss16/blob/master/doc/hw2.md
def max(x, y): return x if x > y else y


def min(x, y): return x if x < y else y


class Num:
    def __init__(i, name):
        i.mu, i.n, i.m2, i.up, i.lo, i.name = 0, 0, 0, -10e32, 10e32, name

    def add(i, x):
        i.n += 1
        x = float(x)
        if x > i.up: i.up = x
        if x < i.lo: i.lo = x
        delta = x - i.mu
        i.mu += delta / i.n
        i.m2 += delta * (x - i.mu)
        return x

    def sub(i, x):
        i.n = max(0, i.n - 1)
        delta = x - i.mu
        i.mu = max(0, i.mu - delta / i.n)
        i.m2 = max(0, i.m2 - delta * (x - i.mu))

    def sd(i):
        return 0 if i.n <= 2 else (i.m2 / (i.n - 1)) ** 0.5

    def show(i):
        print(str(i.name).ljust(15) + "mean: %0.3f, std dev: %0.3f" %
              (i.mu, i.sd()))

    # Norm code by Dr.Menzies
    def norm(i, x):
        tmp = (x - i.lo) / (i.up - i.lo + 10**-32)
        if tmp > 1: return 1
        elif tmp < 0: return 0
        else: return tmp

    def dist(i, x, y):
        return i.norm(x) - i.norm(y)

    def furthest(i, x):
        return i.up if x < (i.up - i.lo)/2 else i.lo


class Sym:
    def __init__(i, name):
        i.counts, i.most, i.mode, i.n, i.name = {}, 0, None, 0, name

    def add(i, x):
        i.n += 1
        new = i.counts[x] = i.counts.get(x, 0) + 1
        if new > i.most:
            i.most, i.mode = new, x
        return x

    def sub(i, x):
        i.n -= 1
        i.counts[x] -= 1
        if x == i.mode:
            i.most, i.mode = None, None

    def ent(i):
        tmp = 0
        for val in i.counts.values():
            p = val / i.n
            if p:
                tmp -= p * math.log(p, 2)
        return tmp

    def show(i):
        print(str(i.name).ljust(15) + "mode: %s, entropy: %0.3f" % (i.mode, i.ent()))

    # Norm code by Dr.Menzies
    def norm(i, x):
        return x

    def dist(i, x, y):
        return 0 if x == y else 1

    def furthest(i, x):
        return x


## Code for rows, csv functions have been taken from https://github.com/txt/fss16/blob/master/src/rows.py

def rows(file, prep=None,
         whitespace='[\n\r\t]',
         comments='#.*',
         sep=","
         ):
    """
    Walk down comma seperated values,
    skipping bad white space and blank lines
    """
    doomed = re.compile('(' + whitespace + '|' + comments + ')')
    with open(file) as fs:
        for line in fs:
            line = re.sub(doomed, "", line)
            if line:
                row = map(lambda z: z.strip(), line.split(sep))
                if len(row) > 0:
                    yield prep(row) if prep else row


def csv(file):
    """
    Convert rows of strings to ints,floats, or strings
    as appropriate
    """

    def atoms(lst):
        return map(atom, lst)

    def atom(x):
        try:
            return int(x)
        except:
            try:
                return float(x)
            except ValueError:
                return x

    for row in rows(file, prep=atoms):
        yield row


class Table:
    def __init__(self, csv_file):
        self.csv = csv_file
        self.rows = []
        headings = csv(csv_file).next()
        self.cols = [Sym(headings[0]), Num(headings[1].split('-')[0]),
                     Num(headings[2].split('<')[1]), Sym(headings[3]),
                     Num(headings[4].split('>')[1])]

    def add_rows(self, csv_file):
        headings = csv(csv_file).next()
        for num, row in enumerate(csv(csv_file)):
            if num is not 0:
                self.rows.append(row)
                for count, item in enumerate(row):
                    self.cols[count].add(item)

    # Forumla exactly taken from Aha's paper.
    # Minus sign is removed, because distance can't be negative.
    def aha_distance(i, r1, r2):
        distance = 0
        for col, row1, row2 in zip(i.cols, r1, r2):
            distance += col.dist(row1, row2)
        if distance<0:
            distance = 0
            for col, row1, row2 in zip(i.cols, r2, r1):
                distance += col.dist(row1, row2)
        return math.sqrt(distance)

    def min_max_distances(i):
        for a in xrange(len(i.rows)):
            min_distance = 10**32
            max_distance = 10**-32
            current_row = i.rows[a]
            other_rows = i.rows[:a]
            if a < len(i.rows):
                other_rows += i.rows[a+1:]
            # print current_row
            for row in other_rows:
                current_distance = i.aha_distance(current_row, row)
                # print current_distance,row, min_distance, max_distance, min_row, max_row
                if current_distance < min_distance:
                    min_distance = current_distance
                    min_row = row
                if current_distance > max_distance:
                    max_distance = current_distance
                    max_row = row
            print("Closest Row for Row " + str(i.rows[a]) + ": " + str(min_row))
            print("Farthest Row for Row " + str(i.rows[a]) + ": " + str(max_row))


if __name__ == '__main__':
    data = '../1/ninja/data/weather.csv'
    table = Table(data)
    table.add_rows(data)
    for col in table.cols:
        col.show()
    table.min_max_distances()
