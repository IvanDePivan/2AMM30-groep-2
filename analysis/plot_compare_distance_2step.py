import srsly
from itertools import chain
import seaborn as sns
import matplotlib.pyplot as plt
comp1 = srsly.read_json('comp1_closest_matches_removed_empty.json')
comp2 = srsly.read_json('comp2_closest_matches.json')

distances_comp1 = []
for item in chain.from_iterable(comp1):
    distances_comp1.append(item[2])

distances_comp2 = []
for item in chain.from_iterable(comp2):
    distances_comp2.append(item[2])

p = sns.displot({"Component 1": distances_comp1, "Component 2": distances_comp2}, binwidth=5)
p.set_xlabels('Levenshtein distance')
p.set_ylabels('number of relations')
# plt.show()
plt.savefig('levenshtein_comparison')
