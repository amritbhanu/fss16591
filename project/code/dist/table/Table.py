import sys
sys.dont_write_bytecode = True


class Table(object):

    def __init__(self, raw_data):
        self.rows = []
        self.add_rows(raw_data)

    def add_rows(self, raw_data):
        ignore_cols = []
        for index, row in enumerate(raw_data):
            if index == 0: continue
            new_row = []
            for col, val in enumerate(row):
                if col in ignore_cols: continue
                try:
                    val = float(val)
                    new_row.append(val)
                except:
                    ignore_cols.append(col)
            self.rows.append(new_row)
