"""UOM DataFrame."""
from pkg_resources import resource_filename

from pandas import read_csv

DF_UOM = read_csv(resource_filename('uom', 'uom.csv'), index_col=0)
