"""Unit alias dictionary."""

unit_alias_dict = {
    "deg": "dega",
    "lbm/gal": "lbf/gal[US]",
    "gal/min": "gal[US]/min",
    "c/min": "rpm",
    "kft.lbf": "1000 lbf.ft",
    "deg/100ft": "0.01 dega/ft",
    "feet": "ft",
    "FT": "ft",
    "foot": "ft"
}


def unit_alias(alias):
    """For a given unit alias return the approprieated unit."""
    if alias in unit_alias_dict:
        return unit_alias_dict[alias]
    else:
        return alias
