"""UOM DataFrame."""

from __future__ import absolute_import
from pandas import read_csv

try:
    from importlib import resources as importlib_resources
except ImportError:  # Python < 3.7 fallback to backport
    import importlib_resources as importlib_resources  # type: ignore

# Load the CSV from package resources without pkg_resources
with importlib_resources.open_binary("uom", "uom.csv") as _csv:
    DF_UOM = read_csv(_csv, index_col=0)
