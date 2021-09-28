import pandas as pd
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
 
 class percent_missing:
    try:
       def __init__(self,df,pct_missing):
           self.df = df 
           self.pct_missing = pct_missing
       def missing_columns(self):
           miss_cols = self.df.columns[self.df.isna().sum()> self.df.shape[0]*pct_missing].tolist()
           rem_cols =   [col for col in self.df.columns if col not in miss_cols]
           return miss_cols
    except ValueError:
        print("pct_missing :should be between 0 and 1")