"""Unit alias dictionary."""

# Alias: UOM
unit_alias_dict = {
    'deg': 'dega',
    'lbm/gal': 'lbf/gal[US]',
    'gal/min': 'gal[US]/min',
    'c/min': 'rpm',
    'kft.lbf': '1000 lbf.ft',
    'deg/100ft': '0.01 dega/ft',
    'feet': 'ft',
    'FT': 'ft',
    'foot': 'ft',
    'ft/ht': 'ft/h',
    '1/30 deg/m': '1/30 dega/m',
    'deg/30m': '1/30 dega/m',
    'deg/m': 'dega/m',
    '1000 ft.lbf': '1000 lbf.ft',
    '1000 lbf': 'klbf',
    'kkgf': 'Mgf',
    'ppg': 'lbm/gal[US]',
    'lbm/gal': 'lbm/gal[US]',
    '1000 kgf': 'Mgf',
    'KKGF': 'Mgf',
    'deg C': 'degC',
    'RPM': 'rpm',
    'KLBF': 'klbf',
    'KFLB': 'klbf',
    'G': 'gn',
    "G's": 'gn',
    'hr': 'h'
}


def unit_alias(alias):
    """For a given unit alias return the approprieated unit."""
    if alias in unit_alias_dict:
        return unit_alias_dict[alias]
    else:
        return alias
