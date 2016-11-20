import sys
sys.dont_write_bytecode = True


class Result(object):
    """docstring for Result"""
    def __init__(self):
        super(Result, self).__init__()
        self.content = []

    def set_content(self, content):
        self.content.append(content)

    def get_content(self):
        return self.table
