"""Unit alias dictionary."""

# Alias: UOM
UNIT_ALIAS_DICT = {
    'W/A': 'V',
    'deg': 'dega',
    'degr': 'dega',
    'lbm/gal': 'lbm/gal[US]',
    'gal/min': 'gal[US]/min',
    'c/s': 'rev/s',
    'cps': 'rev/s',
    'c/min': 'rpm',
    'kft.lbf': '1000 lbf.ft',
    'deg/100ft': '0.01 dega/ft',
    '0.01 deg/ft': '0.01 dega/ft',
    'feet': 'ft',
    'FT': 'ft',
    'foot': 'ft',
    'FT/S': 'ft/s',
    'ft/ht': 'ft/h',
    'ft/hr': 'ft/h',
    '1/30 deg/m': '1/30 dega/m',
    'deg/30m': '1/30 dega/m',
    'deg/m': 'dega/m',
    '1000 ft.lbf': '1000 lbf.ft',
    '1000 lbf': 'klbf',
    'kkgf': 'Mgf',
    'ppg': 'lbm/gal[US]',
    '1000 kgf': 'Mgf',
    'KKGF': 'Mgf',
    'deg C': 'degC',
    'RPM': 'rpm',
    'KLBF': 'klbf',
    'KFLB': 'klbf',
    'G': 'gn',
    "G's": 'gn',
    'hr': 'h',
    'hour': 'h',
    'hrs': 'h',
    'PSI': 'psi',
    'KPSI': 'kpsi',
    'ft.lbf': 'lbf.ft',
    'in.lbf': 'lbf.in'
}


def unit_alias(alias):
    """For a given unit alias return the approprieated unit."""
    if alias in UNIT_ALIAS_DICT:
        return UNIT_ALIAS_DICT[alias]
    else:
        return alias
