from random import random

# Hierarchical data structure
class hds:

    recursion_depth = 0

    def add_child(self, child):
        self.children.append(child)
    def add_parent(self, parent):
        self.parents.append(parent)
    def add_data(self, element):
        self.data.append(element)

    # when flag is true, currently grabs a random element from each descendant
    # and then randomly returns one of those. This means that each node has
    # equivalent probability of being chosen rather than each individual
    # element having equal probability FIXME
    def random(self, include_descendants_in_search = False):
        if include_descendants_in_search == False or len(self.children) == 0:
            if len(self.data) == 0:
                return None
            return self.data[int(random() * len(self.data))]
        else:
            hds.recursion_depth += 1
            possibilities = [self.random()]
            for child in self.children:
                possibilities.append(child.random(True))

            if hds.recursion_depth == 1:
                hds.recursion_depth = 0
                return possibilities[int(random() * len(possibilities))]

            hds.recursion_depth -= 1
            return possibilities

    def __init__(self, parent = None):
        self.data = []
        self.parents = []
        self.children = []
        if parent != None:
            print("Parent ", parent)
            print("self ", self)
            self.add_parent(parent)
            parent.add_child(self)
