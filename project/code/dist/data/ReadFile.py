import os
from Csv import Csv
from Table import Table


class ReadFile(object):
    """docstring for ReadFile"""
    def __init__(self, filename):
        super(ReadFile, self).__init__()
        self.filename = filename
        if os.path.isfile(self.filename):
            if 'arff' == (self.filename).split(".")[-1]:
                self.arff_reader()
            elif 'csv' == (self.filename).split(".")[-1]:
                self.csv_reader()
            else:
                Exception("Unsupported File!")
        else:
            Exception("File not found!")
        # self.clean_rows()
        self.build_table()

    def arff_reader(self):
        pass

    def csv_reader(self):
        csv = Csv(self.filename)
        # you can remove this.
        self.headers = csv.next
        self.rows = csv.parse()
        # for data in self.rows:
        #     print data

    def build_table(self):
        print "Buidling Table: "
        return Table(self.headers, self.rows)
