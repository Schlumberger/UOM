"""UOM DataFrame."""
from pandas import read_csv

df_uom = read_csv("uom/uom.tsv", sep='\t', index_col=0)
