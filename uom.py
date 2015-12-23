"""UOM conversion tool."""
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from pandas import read_csv

from uomdata import tsv
from math import pi

df = None


def load(verbose=False):
    """Load unit dictionary."""
    global df

    tsv2 = tsv.replace("4*PI", str(4 * pi)).replace("2*PI", str(2 * pi))
    tsv2 = tsv2.replace("PI", str(pi))

    df = read_csv(StringIO(tsv2), sep='\t', index_col=0)

    if verbose:
        print(df)


def base_conversion_factors(unit, verbose=True):
    """"Return conversion facors to the base unit."""
    global df

    if df is None:
        load()

    if verbose:
        print(unit, df["A"][unit], df["B"][unit], df["C"][unit])

    if df["baseUnit"][unit] == "IS-BASE":
        if verbose:
            print("The unit {} it is a base unit.".format(unit))

        return 0, 1, 1

    return df["A"][unit], df["B"][unit], df["C"][unit]


def base_unit(unit):
    """Return base unit."""
    global df

    if df is None:
        load()

    base_unit = df["baseUnit"][unit]

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
        print("Test {}".format(k))
        print('=' * 80)
        i = tests[k]
        o = convert_value(i[0], i[1], i[2])

        if o == i[3]:
            print("OK {}({} == {})".format(k, o, i[3]))
        else:
            print("Error {} ({} <> {}, diff {} %)".format(k, o, i[3], abs(100 -
                                                          o / i[3] * 100)))

        print('=' * 80)

# test()
