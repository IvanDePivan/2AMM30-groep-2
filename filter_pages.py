import pandas as pd
from pathlib import Path
import spacy
import ftfy
import codecs 
import re
import json
nlp = spacy.load("en_core_web_sm")

pathlist = [p for p in Path("enwiki20230820-stripped-json").glob("**/*") if p.is_file()]
count = 0
subset = []

for path in pathlist:
    df = pd.read_json(path, lines = True)
    for ind in df.index:
        if re.search('won the Nobel Prize',df['text'][ind]):
            count +=1
            text = df['text'][ind]
            text = text.replace('\n', ' ')
            subset.append(text)
    #         if count == 2:
    #             break
    # if count == 2:
    #     break
            
with codecs.open('subset.json', 'w', 'utf-8-sig') as f:
    json.dump(subset, f)

    
    
