"""
This test script just proves that there is a converging value, and no matter how much
they change, they will have equal / the required proportion of each type, everytime.
"""
from ant import Ant
from random import randint
from matplotlib import pyplot as plt
from utility_functions import get_counts
from random import choice
from tqdm import tqdm

ants = []
for i in range(1000):
    ants.append(Ant(randint(0, 4)))

ant_types = []
for i in ants:
    ant_types.append(i.get_type())

print(ant_types)
counts = get_counts(ant_types)
print(counts)
fig = plt.bar(counts.keys(), counts.values())
plt.show()


# lets try to get the ants to just interact with each other

for i in tqdm(range(10000)):
    ant_one = choice(ants)
    ant_two = choice(ants)
    if ant_one != ant_two:
        ant_one.interact_with_ant(ant_two)
        ant_two.interact_with_ant(ant_one)


ant_types = []
for i in ants:
    ant_types.append(i.get_type())

print(ant_types)
counts = get_counts(ant_types)
print(counts)

fig = plt.bar(counts.keys(), counts.values())
plt.show()