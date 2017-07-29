from random import random

# Hierarchical data structure
class hds:

    recursive_index = 0

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
    def data_from_file(self, fname):
        with open(fname, "r") as f:
            for line in f:
                self.add_data(line)

    # stack the data of this node and all its children end to end, grab the ith
    # the stack is depth first
    def get_ith_recursive(self, i):
        if i < len(self.data):
            return self.data[i]
        else:
            hds.recursive_index = i - len(self.data)
            for child in self.children:
                r = child.get_ith_recursive(hds.recursive_index)
                if type(r) == str:
                    return r

    def random(self, include_descendants_in_search = False):
        if include_descendants_in_search == False or len(self.children) == 0:
            if len(self.data) == 0:
                return None
            return self.data[int(random() * len(self.data))].lower().strip()
        else: # recursive case
            # Go down the tree, appending the lens of each array
            self.recursion_array.append(len(self.data))
            for child in self.children:
                child.random(True)



    def __init__(self, parent = None):
        self.data = []
        self.parents = []
        self.children = []
        if parent != None:
            self.add_parent(parent)
            parent.add_child(self)
