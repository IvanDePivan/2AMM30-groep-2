import pandas as pd
from pathlib import Path
import spacy
import ftfy
import codecs 
nlp = spacy.load("en_core_web_sm")

pathlist = [p for p in Path("enwiki20230820-stripped-json").glob("**/*") if p.is_file()]
check = 0
instance = 'Martti Ahtisaari'

for path in pathlist:
    df = pd.read_json(path, lines = True)
    for ind in df.index:
        if df['title'][ind] == instance:
            text = df['text'][ind]
            text = text.replace('\n', ' ')
            with codecs.open('instance.txt', 'w', 'utf-8-sig') as f:
                f.write(ftfy.fix_text(text))
            check=1
            break 
    if check == 1:
        break
    
    
