class PrintUtils(object):
    """ This contains all utility functions for I/O """

    def __init__(self):
        super(PrintUtils, self).__init__()

    def print_with_border(self, string):
        print "#"*(len(string)+4)
        print "# " + string + " #"
        print "#"*(len(string)+4)
