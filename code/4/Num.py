from __future__ import division
import math
import sys
sys.dont_write_bytecode = True

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
