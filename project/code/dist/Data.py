import sys
sys.dont_write_bytecode = True


class Data(object):
    """docstring for Data"""
    def __init__(self):
        super(Data, self).__init__()

    def set_content(self, content):
        self.table = content

    def get_content(self):
        return self.table

    def set_train_data(self, content):
        self.train_data = [row[:-1] for row in content]

    def get_train_data(self):
        return self.train_data

    def set_test_data(self, content):
        self.test_data = [row[:-1] for row in content]

    def get_test_data(self):
        return self.test_data

    def set_train_label(self, labels):
        self.train_label = labels

    def get_train_label(self):
        return self.train_label

    def set_test_label(self,labels):
        self.test_label = labels

    def get_test_label(self):
        return self.test_label
        