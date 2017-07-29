from hds import hds
from root import root
from hds_setup import *
from insult import *
from random import random


nsfw = hds(root)

insults = nsfw.data

insults.append(
    insult("You smell like {} {}s; Why haven't you taken a shower yet you {}!?",
            [adjectives, animals, rude_nouns])
)

insults.append(
    insult("Yeah you {} {}, I {} your {} while riding a {} {}.",
            [adjectives, rude_nouns, past_transitive, family, adjectives, animals])
)

insults.append(
    insult("I would rather {} {} {}s than spend another minute with you, you {} {}.",
            [infinitive_transitive, numbers, animals, adjectives, rude_nouns])
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

insults.append(
    insult("How do you sleep at night you {} excuse for a {} {}'s {}",
            [adjectives, adjectives, animals, family])
)

insults.append(
    insult("When you walk into a room, I can feel the stupity oozing from your {}.",
            [body_parts])
)

insults.append(
    insult("Nothing would give me more joy than to see you succeed in society today; The problem is you're just such a {}.",
            [rude_nouns])
)

insults.append(
    insult("Doth my own eyes decieve me, wherefore art thou you {} {}?",
            [adjectives, rude_nouns])
)


if __name__ == "__main__":
   #random_phrase()
    print(nsfw.random().fill())
