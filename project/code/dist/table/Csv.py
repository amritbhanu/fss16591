from __future__ import division
import csv, re
import sys
sys.dont_write_bytecode = True

class Csv(object):
    """docstring for Csv"""
    def __init__(self, csvFileName):
        self.csvFileName = csvFileName
        self.next = self.parse().next()

    def parse(self):
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

        for row in self.rows(prep=atoms):
            yield row

    def rows(self, prep=None,
             whitespace='[\n\r\t]',
             comments='#.*',
             sep=","
             ):
        """
        Walk down comma seperated values,
        skipping bad white space and blank lines
        """
        doomed = re.compile('(' + whitespace + '|' + comments + ')')
        with open(self.csvFileName) as fs:
            for line in fs:
                line = re.sub(doomed, "", line)
                if line:
                    row = map(lambda z: z.strip(), line.split(sep))
                    if len(row) > 0:
                        yield prep(row) if prep else row

        