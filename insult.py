from hds import hds
from hds_setup import *

class insult:
    def fill(self):
        args = [x.random() for x in self.categories]
        return self.phrase.format(*args)
    def __init__(self, phrase, categories = None):
        self.phrase = phrase
        self.categories = categories

