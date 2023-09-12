import pandas as pd
from pathlib import Path
import spacy
import re
nlp = spacy.load("en_core_web_sm")

pathlist = [p for p in Path(r"C:\Users\NinavanDiermen\OneDrive - Pipple BV\Documenten\Text Mining\enwiki20230820-stripped-json").glob("**/*") if p.is_file()]
occurences = 0

for path in pathlist:
    df = pd.read_json(path, lines = True)
    for ind in df.index:
        if re.search('^Eurovision Song Contest 20[0-2][0-9]$',df['title'][ind]):
            occurences +=1
            text = df['text'][ind]
            doc = nlp(text)
            print('\n')
            print(df['title'][ind])
            print('=== Entities ===')
            for ent in doc.ents:
                print(ent.text, ent.start_char, ent.end_char, ent.label_)
   
#%%



    
