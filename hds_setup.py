from hds import hds


root = hds()

nouns = hds(root)
exclamations = hds(root)

adjectives = hds(root)
adjectives.data_from_file("wordlists/curses/adjectives.txt")

animals = hds(nouns)
animals.data_from_file("wordlists/animals.txt")

adhominem = hds(exclamations)
adhominem.data_from_file("wordlists/curses/adhominem.txt")
