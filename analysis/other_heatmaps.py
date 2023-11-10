from matplotlib.colors import LogNorm, Normalize
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def comp1_ner_heatmap():
    labels = ['B-Winner', 'I-Winner', 'B-Date', 'I-Date', 'B-Nationality','I-Nationality', 'B-Prizetype', 'I-Prizetype', 'B-Reason', 'I-Reason', 'O']
    
    results = pd.read_csv('component1\\ner\\test.tsv',sep=' ', names=['x', 'y_true', 'y_pred'])
    y_true = results['y_true']
    y_pred = results['y_pred']
    cm = confusion_matrix(y_true,y_pred, labels=labels)
    cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    cm_color = np.where(cm==0,0.5,cm)
    sns.heatmap(cm_color, annot=cmn,  xticklabels=labels, yticklabels=labels, fmt='')

    plt.show()


def comp1_re_heatmap():
    y_true = []
    y_pred = []
    pattern = r'(has_nationality|died_on|born_on|received_nobelprize_for|has_won|received_nobelprize_in)'
    with open('component1\\relations\\test.tsv', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'^ \- Gold:', line) is not None:
                match = re.search(pattern, line)
                if match is None:
                    y_true.append('')
                else:
                    y_true.append(match.group(1))
            if re.search(r'^ \- Pred:', line) is not None:
                match = re.search(pattern, line)
                if match is None:
                    y_pred.append('')
                else:
                    y_pred.append(match.group(1))
    
    labels = ['No relation', 'Born on', 'Died on','Has nationality','Has won', 'Received Nobel prize for', 'Received Nobel prize in']
    cm = confusion_matrix(y_true,y_pred)
    cm_color = np.where(cm==0,0.5,cm)
    sns.heatmap(cm_color, annot=cm, norm=LogNorm(vmin=0.5), xticklabels=labels, yticklabels=labels, fmt='')
    plt.show()

def comp2_ner_heatmap():
    labels = ['B-Component', 'I-Component', 'B-Date', 'I-Date', 'B-Person','I-Person', 'B-Time', 'I-Time', 'O']
    label_names = ['B-Component event', 'I-Component event', 'B-Date', 'I-Date', 'B-Person Intervention','I-Person Intervention', 'B-Time', 'I-Time', 'O']
    # labels.sort()
    results = pd.read_csv( 'component2\\ner\\test.tsv',sep=' ', names=['x', 'y_true', 'y_pred'])
    y_true = results['y_true']
    y_pred = results['y_pred']
    cm = confusion_matrix(y_true,y_pred, labels=labels, normalize='true')
    cm_color = np.where(cm==0,0.0,cm)
    sns.heatmap(cm_color, annot=cm, norm=Normalize(), xticklabels=label_names, yticklabels=label_names, fmt='')

    plt.show()

def comp2_re_heatmap():
        y_true = []
        y_pred = []
        pattern = r'(happened_at|caused_by)'
        with open('component2\\relations\\test.tsv', encoding='utf8') as f:
            lines = f.readlines()
            for line in lines:
                if re.search(r'^ \- Gold:', line) is not None:
                    match = re.search(pattern, line)
                    if match is None:
                        y_true.append('')
                    else:
                        y_true.append(match.group(1))
                if re.search(r'^ \- Pred:', line) is not None:
                    match = re.search(pattern, line)
                    if match is None:
                        y_pred.append('')
                    else:
                        y_pred.append(match.group(1))
        
        labels = ['No relation', 'Caused by', 'Happenend at']
        lab = ['', 'caused_by', 'happened_at']
        cm = confusion_matrix(y_true,y_pred, labels=lab)
        cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        # cm_color = np.where(cm==0,0.5,cm)
        sns.heatmap(cmn, xticklabels=labels, yticklabels=labels, fmt='.2f', annot=True)
        plt.show()



def comp1_ner_heatmap():
    labels = ['B-Winner', 'I-Winner', 'B-Date', 'I-Date', 'B-Nationality','I-Nationality', 'B-Prizetype', 'I-Prizetype', 'B-Reason', 'I-Reason', 'O']
    results = pd.read_csv( 'component1\\ner\\test.tsv',sep=' ', names=['x', 'y_true', 'y_pred'])

    cm = confusion_matrix(results['y_true'], results['y_pred'], labels=labels)
    cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    ax = sns.heatmap(cmn, vmin=0, vmax=1, fmt='.2f', annot=True, xticklabels=labels, yticklabels=labels)

    plt.show()

