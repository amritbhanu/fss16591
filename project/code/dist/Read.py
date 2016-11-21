from dist.table.Csv import Csv
from dist.table.Table import Table
import sys
sys.dont_write_bytecode = True


class Read(object):
    """docstring for Read"""
    def __init__(self, filename, data):
        super(Read, self).__init__()
        self.filename = filename
        # print self.filename
        self.data = data
        if 'csv' == (self.filename).split(".")[-1]:
            self.csv_reader()
            self.build_table()
        else:
            print "Unsupported File: " + filename

    def csv_reader(self):
        csv = Csv(self.filename)
        self.rows = csv.parse()

    def build_table(self):
        table = Table(self.rows)
        self.data.set_content(table.rows)
        return True
