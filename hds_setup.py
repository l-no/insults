from hds import hds


root = hds()

nouns = hds(root)
exclamations = hds(root)


animals = hds(nouns)
animals.data_from_file("wordlists/animals.txt")

adhominem = hds(exclamations)
adhominem.data_from_file("wordlists/curses/adhominem.txt")
