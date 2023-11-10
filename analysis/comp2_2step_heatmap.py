import re
import srsly
import pandas as pd
from matplotlib.colors import LogNorm, Normalize
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_set = srsly.read_json('comp2_test_set.json')
output = srsly.read_json('comp2_output_relations.json')

labels = ['org:caused_by', 'org:happened_at', 'no relation']
display_labels = ['Caused by', 'Happenend at', 'No Match']

cm = np.zeros((3,3))

def get_text_from_id(labels, id):
    for label in labels:
        if label["id"] == id:
            return label["value"]["text"]


ground_truth_labels = []
output = list(output.items())
count = 0 
total_count = 0
matched_predictions = []
for i, item in enumerate(test_set):
    # print(item["data"]["text"])
    output_doc = output[i]
    matched_predictions.append([])
    ground_truth_relations = [a for a in item['annotations'][0]["result"] if a["type"] == 'relation']
    ground_truth_labels = [a for a in item['annotations'][0]["result"] if a["type"] == 'labels']
    for j, relation in enumerate(ground_truth_relations):
        total_count += 1
        from_text = get_text_from_id(ground_truth_labels, relation['from_id'])
        to_text = get_text_from_id(ground_truth_labels, relation['to_id'])

        relation_label = relation["labels"][0]
        if from_text == '' or to_text == "" or relation_label == 'same_as':
            continue
        truth_index = labels.index(relation_label)
        found = False
        for k, output_relation in enumerate(output_doc[1]):
            if from_text == output_relation[0] and to_text == output_relation[1] and k not in matched_predictions[i]:
                pred_index = labels.index(output_relation[2])
                cm[truth_index, pred_index] += 1
                found = True
                matched_predictions[i].append(k)
                count += 1
                break
        if not found:
            # ground truth didn't match
            cm[truth_index, -1] += 1
    # predicted didnt match

for i, doc in enumerate(output):
    for j, rel in enumerate(doc[1]):
        if j not in matched_predictions[i]:
            cm[-1, labels.index(rel[2])] += 1
        
print(matched_predictions)
print(count, total_count)
cm_color = np.where(cm==0,0.5,cm)
sns.heatmap(cm_color, annot=cm, norm=LogNorm(vmin=0.5), xticklabels=display_labels, yticklabels=display_labels, fmt='.0f')
plt.show()