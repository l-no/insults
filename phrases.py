from hds_setup import *
from insult import *
from random import random


insults = []

insults.append(
    insult("You smell like {} {}s; Why haven't you taken a shower yet you {}!?",
            [adjectives, animals, rude_nouns])
)

insults.append(
    insult("Yeah you {} {}, I {} your {} while riding a {}.",
            [adjectives, rude_nouns, past_transitive, family, animals])
)

insults.append(
    insult("I would rather {} a {} than spend another minute with you, you {} {}.",
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

insults.append(
    insult("How can I put into words what you mean to me? ... Oh wait, I got it: {} {}.",
            [adjectives, rude_nouns])
)

insults.append(
    insult("Every time I see your {}, I weep in {} for what a {} place you've made the world.",
            [body_parts, abstract_nouns, adjectives])
)









def random_phrase():
    r = int(random() * len(insults))
    print(insults[r].fill())

if __name__ == "__main__":
   random_phrase()
