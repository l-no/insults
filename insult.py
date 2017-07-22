from hds import hds

class insult:
    def fill(self):
        args = [x.random() for x in self.categories]
        return self.phrase.format(*args)
    def __init__(self, phrase, categories = None):
        self.phrase = phrase
        self.categories = categories


animals = hds()
with open("animals.txt", "r") as f:
    for animal in f:
        animals.add_data(animal)


x = insult("My favorite animal is the majestic {}",[animals])

print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())
print(x.fill())


