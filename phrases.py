from hds_setup import *
from insult import *
from random import random


insults = []

insults.append(
    insult("{}! Why haven't you taken a shower yet you {} {}!?",
            [adhominem, adjectives, animals])
)

insults.append(
    insult("Yeah, you {} {}, I {} your mother while riding a {}.",
            [adjectives, rude_nouns, past_transitive, animals])
)

insults.append(
    insult("I would rather {} a {} than spend another minute with you, you {} {}",
            [infinitive_transitive, animals, adjectives, rude_nouns])
)

insults.append(
    insult("Holy {}! You are the single most {} piece of {} that I have ever seen.",
            [rude_nouns, adjectives, rude_nouns])
)

insults.append(
    insult("Honestly, just fuck off.",
            [])
)

insults.append(
    insult("How many times do I need to tell you to stop {} {}s, you {} {}.",
           [progressive_transitive, animals, adjectives, rude_nouns])
)



















def random_phrase():
    print(insults[int(random() * len(insults))].fill())

if __name__ == "__main__":
   random_phrase()
