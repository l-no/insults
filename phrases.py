from hds_setup import *
from insult import *


p1 = insult("{}! Why haven't you taken a shower yet you {} {}!?\n",
            [adhominem, adjectives, animals])

p2 = insult("Yeah, you {} {}, I {} your mother while riding a {}.\n",
            [adjectives, adhominem, past_transitive, animals])



print(p1.fill())
print(p2.fill())

print(p1.fill())
print(p2.fill())

print(p1.fill())
print(p2.fill())

print(p1.fill())
print(p2.fill())
