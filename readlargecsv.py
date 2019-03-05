import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 10)

x = pd.read_csv(r'c:\temp\out4.tsv',sep="\t",error_bad_lines=0,index_col=False)
y = x.head(100) 
