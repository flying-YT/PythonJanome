import pandas as pd
import os
from janome.tokenizer import Tokenizer

path = "./csv"
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

t = Tokenizer()

col_names = [ 'c{0:02d}'.format(i) for i in range(8) ]

for file in files_file:
    file = 'csv/' + file 
    print(file)

    df = pd.read_csv(file, names=col_names)
    for row in df.itertuples():
        tokens = t.tokenize(row[2])
        pos = [token.base_form for token in tokens
            if token.part_of_speech.split(',')[0] in ["名詞", "動詞"]]
        print(pos)