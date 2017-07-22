from hds import hds


words = hds()

nouns = hds(words)

animals = hds(nouns)
with open("wordlists/animals.txt", "r") as f:
    for animal in f:
        animals.add_data(animal)


