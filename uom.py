"""UOM conversion tool."""
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from pandas import read_csv

from uomdata import tsv

df_uom = None

unit_alias_dict = {
    "deg": "dega",
    "lbm/gal": "lbf/gal[US]",
    "gal/min": "gal[US]/min",
    "c/min": "rpm",
    "kft.lbf": "1000 lbf.ft",
    "deg/100ft": "0.01 dega/ft"
}


def load(verbose=False):
    """Load unit dictionary."""
    global df_uom

    df_uom = read_csv(StringIO(tsv), sep='\t', index_col=0)

    if verbose:
        print(df_uom)


def unit_alias(alias):
    """For a given unit alias return the approprieated unit."""
    if alias in unit_alias_dict:
        return unit_alias_dict[alias]
    else:
        return alias


def base_conversion_factors(unit_or_alias, verbose=True):
    """"Return conversion facors to the base unit."""
    global df_uom

    if df_uom is None:
        load()

    unit = unit_alias(unit_or_alias)

    if verbose:
        print(unit, df_uom["A"][unit], df_uom["B"][unit], df_uom["C"][unit])

    if df_uom["baseUnit"][unit] == "IS-BASE":
        if verbose:
            print("The unit {} it is a base unit.".format(unit))

        return 0, 1, 1

    return df_uom["A"][unit], df_uom["B"][unit], df_uom["C"][unit]


def base_unit(unit_or_alias, verbose=False):
    """Return base unit."""
    global df_uom

    unit = unit_alias(unit_or_alias)

    if df_uom is None:
        load()

    if unit not in df_uom.index:
        return None

    base_unit = df_uom["baseUnit"][unit]

    if verbose:
        print(base_unit, type(base_unit))

    if base_unit == "IS-BASE":
        return unit

    return base_unit


def conversion_factors(source, target, verbose=False):
    """Return conversion scale and offset."""
    if base_unit(source) != base_unit(target):
        if verbose:
            print("The units {} and {} are not compatible.".format(source,
                                                                   target))

        return None, None

    source_A, source_B, source_C = base_conversion_factors(source)
    target_A, target_B, target_C = base_conversion_factors(target)

    scale = source_B * target_C / source_C / target_B
    offset = source_A * target_C / source_C / target_B - target_A / target_B

    if verbose:
        print("Scale: {}, offset: {}".format(scale, offset))

    return scale, offset


def convert_value(value, source, target):
    """Convert value from source to target."""
    scale, offset = conversion_factors(source, target)
    target_value = scale * value + offset

    return target_value


def test():
    """Test function."""
    tests = {
        "ft/h => ft/s": [1, "ft/h", "ft/s", 0.0002777777777777778],
        "m => ft": [10, "m", "ft", 32.80839895013123],
        "ft => m": [30, "ft", "m", 9.144],
        "degC => degF": [22.4, "degC", "degF", 72.32]
    }

    for k in sorted(tests):
        print("Test conversion {}".format(k))
        print('=' * 80)
        i = tests[k]
        o = convert_value(i[0], i[1], i[2])

        if o == i[3]:
            print("OK {}({} == {})".format(k, o, i[3]))
        else:
            assert(False)
            print("Error {} ({} <> {}, diff {} %)".format(k, o, i[3], abs(100 -
                                                          o / i[3] * 100)))

        print('=' * 80)

    for k in sorted(unit_alias_dict):
        print("Test unit alias {}".format(k))
        print('=' * 80)

        unit = unit_alias(k)
        base = base_unit(unit)
        print("Alias: {}, Unit: {}, Base unit: {}".format(k, unit, base))

        assert(base is not None)

        print('=' * 80)

# test()
