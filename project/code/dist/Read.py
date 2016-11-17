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
        if 'arff' == (self.filename).split(".")[-1]:
            self.arff_reader()
        elif 'csv' == (self.filename).split(".")[-1]:
            self.csv_reader()
        else:
            Exception("Unsupported File!")
        self.build_table()

    def arff_reader(self):
        Exception("Not Yet Implemented!")

    def csv_reader(self):
        csv = Csv(self.filename)
        self.rows = csv.parse()

    def build_table(self):
        table = Table(self.rows)
        self.data.set_content(table.rows)
