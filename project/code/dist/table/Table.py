import sys, math
from dist.table.Num import Num
from dist.table.Sym import Sym


class Table(object):

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.headers = self.raw_data.next()
        self.rows = []
        self.cols = []
        self.add_rows()

    def typeOfItem(self, val):
        try: return float(val), Num
        except ValueError: return val, Sym

    def add_rows(self):
        for index, row in enumerate(self.raw_data):
            if index != 0:
                for colNum, item in enumerate(row):
                    if index == 1:
                        val, classType = self.typeOfItem(item)
                        if classType is Num: 
                            self.cols.append(Num(self.headers[colNum]))
                        elif classType is Sym:
                            self.cols.append(Sym(self.headers[colNum]))
                    self.cols[colNum].add(item)
                row = self.clean_row(row)
                self.rows.append(row)

    def clean_row(self, row):
        for i in xrange(len(row)):
            try:
                row[i] = float(row[i])
            except:
                row[i] = 0.0
        return row

    # Forumla exactly taken from Aha's paper.
    # def distance(self, r1, r2):
    #     distance = 0
    #     for col, row1, row2 in zip(self.cols, r1, r2):
    #         distance += col.dist(row1, row2)
    #     if distance < 0:
    #         distance = 0
    #         for col, row1, row2 in zip(self.cols, r2, r1):
    #             distance += col.dist(row1, row2)
    #     return math.sqrt(distance)

    # def minDistance(self, current_row, other_rows):
    #     min_distance = 10**32
    #     for i,row in enumerate(other_rows):
    #         current_distance = self.distance(current_row, row)
    #         if current_distance < min_distance:
    #             min_distance = current_distance
    #             min_row = row
    #             index=i
    #     return min_row, index

    # def maxDistance(self, index, row):
    #     max_distance = 10**-32
    #     current_row = self.rows[index]
    #     other_rows = self.rows[:index]
    #     if index < len(self.rows):
    #         other_rows += self.rows[index+1:]
    #     for i,row in enumerate(other_rows):
    #         current_distance = self.distance(current_row, row)
    #         if current_distance > max_distance:
    #                 max_distance = current_distance
    #                 max_row = row
    #     return max_row
