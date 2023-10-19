import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')

df.display()