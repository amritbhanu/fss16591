class Data(object):
    """docstring for Data"""
    def __init__(self):
        super(Data, self).__init__()
        # self.table = \
        # self.results = \
        # self.train_data = \
        # self.train_label = \
        # self.test_data = \
        # self.test_label = None

    def set_content(self, content):
        self.table = content

    def get_content(self):
        return self.table

    def set_results(self, results):
        self.results = results

    def get_results(self):
        return self.results

    def set_train_data(self, content):
        self.train_data = content

    def get_train_data(self):
        return self.train_data

    def set_test_data(self, content):
        self.test_data = content

    def get_test_data(self):
        return self.test_data

    def set_train_label(self):
        self.train_label = [row[-1] for row in self.train_data]

    def get_train_label(self):
        return self.train_label

    def set_test_label(self):
        self.test_label = [row[-1] for row in self.test_data]

    def get_test_label(self):
        return self.test_label
        