"""UOM conversion tool."""
from .unit_alias import unit_alias
from .uomdata import df_uom


def base_conversion_factors(unit_or_alias, verbose=False):
    """"Return conversion facors to the base unit."""
    unit = unit_alias(unit_or_alias)

    if verbose:
        print(unit, df_uom["A"][unit], df_uom["B"][unit], df_uom["C"][unit])

    if df_uom["baseUnit"][unit] == "IS-BASE":
        if verbose:
            print("The unit {0} it is a base unit.".format(unit))

        return 0, 1, 1

    return df_uom["A"][unit], df_uom["B"][unit], df_uom["C"][unit]


def base_unit(unit_or_alias, verbose=False):
    """Return base unit."""
    unit = unit_alias(unit_or_alias)

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
            print("The units {0} and {1} are not compatible.".format(source,
                                                                     target))

        return None, None

    source_A, source_B, source_C = base_conversion_factors(source)
    target_A, target_B, target_C = base_conversion_factors(target)

    scale = source_B * target_C / source_C / target_B
    offset = source_A * target_C / source_C / target_B - target_A / target_B

    if verbose:
        print("Scale: {0}, offset: {1}".format(scale, offset))

    return scale, offset


def convert(value, source=None, target=None, verbose=False):
    """Convert value(s) from source to target."""
    if target is None and source is not None:
        target = base_unit(source)

    if source is None and target is not None:
        source = base_unit(target)

    scale, offset = conversion_factors(source, target)

    if verbose:
        print(value, type(value))

    target_value = scale * value + offset

    if verbose:
        print(target_value, type(target_value))

    return target_value
