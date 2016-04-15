"""UOM conversion tool."""
from .unit_alias import unit_alias
from .uomdata import DF_UOM


def base_conversion_factors(unit_or_alias, verbose=False):
    """"Return conversion facors to the base unit."""
    unit = unit_alias(unit_or_alias)

    if unit not in DF_UOM.index:
        if verbose:
            print("Unit {} unknown.".format(unit_or_alias))

        return None, None, None

    if verbose:
        print(unit, DF_UOM["A"][unit], DF_UOM["B"][unit], DF_UOM["C"][unit])

    if DF_UOM["baseUnit"][unit] == "IS-BASE":
        if verbose:
            print("The unit {0} it is a base unit.".format(unit))

        return 0, 1, 1

    return DF_UOM["A"][unit], DF_UOM["B"][unit], DF_UOM["C"][unit]


def base_unit(unit_or_alias, verbose=False):
    """Return base unit."""
    unit = unit_alias(unit_or_alias)

    if unit not in DF_UOM.index:
        if verbose:
            print("Unit {} unknown.".format(unit_or_alias))

        return None

    b_unit = DF_UOM["baseUnit"][unit]

    if verbose:
        print(b_unit, type(b_unit))

    if b_unit == "IS-BASE":
        return unit

    return b_unit


def conversion_factors(source, target, verbose=False):
    """Return conversion scale and offset."""
    source_base_unit = base_unit(source, verbose)

    if source_base_unit is None:
        return None, None

    if base_unit(source, verbose) != base_unit(target, verbose):
        if verbose:
            print("The units {0} and {1} are not compatible.".format(source,
                                                                     target))

        return None, None

    source_a, source_b, source_c = base_conversion_factors(source, verbose)
    target_a, target_b, target_c = base_conversion_factors(target, verbose)

    scale = source_b * target_c / source_c / target_b
    offset = source_a * target_c / source_c / target_b - target_a / target_b

    if verbose:
        print("Scale: {0}, offset: {1}".format(scale, offset))

    return scale, offset


def convert(value, source=None, target=None, verbose=False):
    """Convert value(s) from source to target."""
    if source == target or \
            ('unitless' in [source, target] and '' in [source, target]):
        return value

    if target is None and source is not None:
        target = base_unit(source, verbose)

        if target is None:
            return None

    if source is None and target is not None:
        source = base_unit(target, verbose)

        if source is None:
            return None

    scale, offset = conversion_factors(source, target, verbose)

    if scale is None or offset is None:
        return None

    if verbose:
        print(value, type(value))

    if isinstance(value, list):
        target_value = [scale * i + offset for i in value]
    else:
        target_value = scale * value + offset

    if verbose:
        print(target_value, type(target_value))

    return target_value
