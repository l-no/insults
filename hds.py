from random import random

# Hierarchical data structure
class hds:

    recursion_depth = 0

    def add_child(self, child):
        self.children.append(child)
    def add_parent(self, parent):
        self.parents.append(parent)
    # takes elements or lists
    def add_data(self, arg):
        if type(arg) == list:
            self.data.extend(arg)
        else:
            self.data.append(arg)

    # when flag is true, currently grabs a random element from each descendant
    # and then randomly returns one of those. This means that each node has
    # equivalent probability of being chosen rather than each individual
    # element having equal probability FIXME
    def random(self, include_descendants_in_search = False):
        if include_descendants_in_search == False or len(self.children) == 0:
            if len(self.data) == 0:
                return None
            return self.data[int(random() * len(self.data))].lower()
        else:
            hds.recursion_depth += 1
            possibilities = []
            s = self.random()
            if (s != None):
                possibilities.append(s)
            for child in self.children:
                recursed_possibilities = child.random(True)
                if recursed_possibilities != None:
                    possibilities.extend(recursed_possibilities)

            if hds.recursion_depth == 1:
                hds.recursion_depth = 0
                if possibilities == None or len(possibilities) == 0:
                    return None
                ret = possibilities[int(random() * len(possibilities))]
                if ret == None:
                    return None
                else:
                    return ret.lower()

            hds.recursion_depth -= 1
            return possibilities

    def __init__(self, parent = None):
        self.data = []
        self.parents = []
        self.children = []
        if parent != None:
            self.add_parent(parent)
            parent.add_child(self)
