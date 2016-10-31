import sys, math
from Num import Num
from Sym import Sym
from Csv import Csv
import sys
sys.dont_write_bytecode = True

class Table(object):

    def __init__(self, csvFileName):
        self.csv = Csv(csvFileName) 
        self.headers = self.csv.next
        self.rows = []
        self.cols = []
        self.addRows()

    def typeOfItem(self, val):
        try: return float(val), Num
        except ValueError: return val, Sym

    def addRows(self):
        for index, row in enumerate(self.csv.parse()):
            if index != 0:
                self.rows.append(row)
                for colNum, item in enumerate(row):
                    val, classType = self.typeOfItem(item)
                    if classType is Num and index == 1:
                        self.cols.append(Num(self.headers[colNum]))
                    elif classType is Sym and index == 1:
                        self.cols.append(Sym(self.headers[colNum]))
                    self.cols[colNum].add(item)

    # Forumla exactly taken from Aha's paper.
    def aha_distance(self, r1, r2):
        distance = 0
        for col, row1, row2 in zip(self.cols, r1, r2):
            distance += col.dist(row1, row2)
        if distance < 0:
            distance = 0
            for col, row1, row2 in zip(self.cols, r2, r1):
                distance += col.dist(row1, row2)
        return math.sqrt(distance)

    def minDistance(self, current_row, other_rows):
        min_distance = 10**32
        for i,row in enumerate(other_rows):
            current_distance = self.aha_distance(current_row, row)
            if current_distance < min_distance:
                min_distance = current_distance
                min_row = row
                index=i
        return min_row, index

    def maxDistance(self, index, row):
        max_distance = 10**-32
        current_row = self.rows[index]
        other_rows = self.rows[:index]
        if index < len(self.rows):
            other_rows += self.rows[index+1:]
        for i,row in enumerate(other_rows):
            current_distance = self.aha_distance(current_row, row)
            if current_distance > max_distance:
                    max_distance = current_distance
                    max_row = row
        return max_row


if __name__ == "__main__":
    csvFileName = './wine.csv'
    table = Table(csvFileName)
    # for row in table.rows:
    #     print row
    #print table.headers
    #for col in table.cols:
    #    col.show()
    #for i,r in enumerate(table.rows):
    #    print("Closest Row for Row %s : %s"%(str(r),str(table.minDistance(i,r))))
    #    print("Farthest Row for Row %s : %s"%(str(r),str(table.maxDistance(i,r))))