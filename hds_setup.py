from hds import hds


root = hds()

nouns = hds(root)
exclamations = hds(root)
verbs = hds(root)

adjectives = hds(root)
adjectives.data_from_file("wordlists/curses/adjectives.txt")

animals = hds(nouns)
animals.data_from_file("wordlists/animals.txt")

rude_nouns = hds(nouns)
rude_nouns.data_from_file("wordlists/misc/bad-nouns.txt")

adhominem = hds(exclamations)
adhominem.data_from_file("wordlists/curses/adhominem.txt")

past_transitive = hds(verbs)
past_transitive.data_from_file("wordlists/verbs/past_transitive.txt")

infinitive_transitive = hds(verbs)
infinitive_transitive.data_from_file("wordlists/verbs/infinitive_transitive.txt")

progressive_transitive = hds(verbs)
progressive_transitive.data_from_file("wordlists/verbs/progressive_transitive.txt")
