import sys
sys.dont_write_bytecode = True


class Table(object):

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.headers = self.raw_data.next()
        self.rows = []
        self.cols = []
        self.add_rows()

    '''def typeOfItem(self, val):
        try: return float(val), Num
        except ValueError: return val, Sym'''

    def add_rows(self):
        for index, row in enumerate(self.raw_data):
            if index != 0:
                '''for colNum, item in enumerate(row):
                    if index == 1:
                        val, classType = self.typeOfItem(item)
                        if classType is Num: 
                            self.cols.append(Num(self.headers[colNum]))
                        elif classType is Sym:
                            self.cols.append(Sym(self.headers[colNum]))
                    self.cols[colNum].add(item)'''
                row = self.clean_row(row)
                self.rows.append(row)

    def clean_row(self, row):
        for i in xrange(len(row)):
            try:
                row[i] = float(row[i])
            except:
                row.pop(i)
        return row
