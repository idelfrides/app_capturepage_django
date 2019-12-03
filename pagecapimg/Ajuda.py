

class Ajuda(object):
    email = list()

    def __init__(self):
        self.email = 'não vale'

    def my_set(self, dado):
        self.email = dado

    def my_get(self):
        return self.email
