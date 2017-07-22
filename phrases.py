from hds_setup import *
from insult import *
from random import random


insults = []

p1 = insult("{}! Why haven't you taken a shower yet you {} {}!?",
            [adhominem, adjectives, animals])
insults.append(p1)

p2 = insult("Yeah, you {} {}, I {} your mother while riding a {}.",
            [adjectives, rude_nouns, past_transitive, animals])
insults.append(p1)

p3 = insult("I would rather {} a {} than spend another minute with you, you {} {}",
            [infinitive_transitive, animals, adjectives, rude_nouns])
insults.append(p3)


p4 = insult("Holy {}! You are the sinlge most {} piece of {} that I have ever seen",
            [rude_nouns, adjectives, rude_nouns])
insults.append(p4)




















def random_phrase():
    print(insults[int(random() * len(insults))].fill())

if __name__ == "__main__":
   random_phrase()
