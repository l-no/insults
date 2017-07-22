from hds import hds
from hds_setup import *

class insult:
    def fill(self):
        if len(self.categories) > 0:
            args = [x.random() for x in self.categories]
            return self.phrase.format(*args)
        else:
            return self.phrase
    def __init__(self, phrase, categories = None):
        self.phrase = phrase
        self.categories = categories
