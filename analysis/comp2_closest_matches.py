import re
import srsly
import pandas as pd
from matplotlib.colors import LogNorm, Normalize
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.metrics.distance import edit_distance
test_set = srsly.read_json('comp2_test_set.json')
output = srsly.read_json('comp2_output_relations.json')

labels = ['org:happened_at', 'org:caused_by', 'no relation']
cm = np.zeros((3,3))

def get_text_from_id(labels, id):
    for label in labels:
        if label["id"] == id:
            return label["value"]["text"]

ground_truth_labels = []
output = list(output.items())
count = 0 
total_count = 0
best_matches = []
fail = 0
for i, item in enumerate(test_set):
    # print(item["data"]["text"])
    output_doc = output[i]
    best_matches.append([])
    

    ground_truth_relations = [a for a in item['annotations'][0]["result"] if a["type"] == 'relation']
    ground_truth_labels = [a for a in item['annotations'][0]["result"] if a["type"] == 'labels']
    for j, relation in enumerate(ground_truth_relations):
        total_count += 1
        from_text = get_text_from_id(ground_truth_labels, relation['from_id'])
        to_text = get_text_from_id(ground_truth_labels, relation['to_id'])
        if from_text == '' or to_text == "":
            continue
        relation_label = relation["labels"][0]
        if relation_label == 'same_as':
            continue
        truth_index = labels.index(relation_label)
        distance = 9000000000000000000000
        best_match = -1
        
        best_match_rel = []
        for k, output_relation in enumerate(output_doc[1]):
            new_distance = edit_distance(from_text, output_relation[0]) + edit_distance(to_text, output_relation[1])
            if new_distance < distance:
                best_match = k
                distance = new_distance
                best_match_rel = output_relation
        if not best_match_rel == []:
            best_matches[i].append(([from_text, to_text, relation_label], best_match_rel, distance))
        else:
            best_matches[i].append(([from_text, to_text, relation_label], None, -1))
    # predicted didnt match

# print(fail)
srsly.write_json('comp2_best_matches.json', best_matches)

