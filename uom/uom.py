"""UOM conversion tool."""
from __future__ import absolute_import, division

from .unit_alias import unit_alias
from .uomdata import DF_UOM


def base_conversion_factors(unit_or_alias, verbose=False):
    """Return conversion facors to the base unit."""
    unit = unit_alias(unit_or_alias)

    if unit not in DF_UOM.index:
        if verbose:
            print(f"Unit {unit_or_alias} unknown.")

        return None, None, None

    if verbose:
        print(unit, DF_UOM["A"][unit], DF_UOM["B"][unit], DF_UOM["C"][unit])

    if DF_UOM["baseUnit"][unit] == "IS-BASE":
        if verbose:
            print(f"The unit {unit} it is a base unit.")

        return 0, 1, 1

    return DF_UOM["A"][unit], DF_UOM["B"][unit], DF_UOM["C"][unit]


def base_unit(unit_or_alias, verbose=False):
    """Return base unit."""
    unit = unit_alias(unit_or_alias)

    if unit not in DF_UOM.index:
        if verbose:
            print(f"Unit {unit_or_alias} unknown.")

        return None

    b_unit = DF_UOM["baseUnit"][unit]
    underlying_def = DF_UOM["underlyingDef"][unit]

    if verbose:
        print(
            f"Input: {unit_or_alias}, unit: {unit}, base_unit: {b_unit}, underlying_unit: "
            f"{underlying_def}"
        )

    if b_unit == "IS-BASE":
        if underlying_def:
            if underlying_def not in DF_UOM.index:
                if verbose:
                    print(
                        f"{unit_or_alias} => {unit} [Case1: IsBase, UD = {underlying_def}, "
                        "but not available]>"
                    )

                return unit

            if verbose:
                print(
                    f"{unit_or_alias} => {unit} [Case2: IsBase, UD = {underlying_def} and "
                    "available]"
                )

            unit2 = DF_UOM["baseUnit"][underlying_def]

            if unit2 not in DF_UOM.index:
                if verbose:
                    print(f"Base unit {unit2} not in the index")

                return underlying_def

            if verbose:
                print(f"Base unit {b_unit} in the index")
        else:
            if verbose:
                print(f"{unit_or_alias} => {unit} [Case3: IsBase, UD is missing]")

            return unit

    if verbose:
        print(f"{unit_or_alias} => {b_unit} [Case4: IsNotBase available]")

    return base_unit(b_unit, verbose)


def conversion_factors(source, target, verbose=False):
    """Return conversion scale and offset."""
    source_base_unit = base_unit(source, verbose)
    target_base_unit = base_unit(target, verbose)

    if source_base_unit is None or target_base_unit is None:
        return None, None

    if source_base_unit != target_base_unit:
        if verbose:
            print(f"The units {source} and {target} are not compatible.")

        source_dim = DF_UOM["dimension"][unit_alias(source)]

        if (
            source_dim == DF_UOM["dimension"][unit_alias(target)]
            and source_dim != "none"
        ):
            raise Exception("ERROR: Houston, we have a problem")

        return None, None

    source_a, source_b, source_c = base_conversion_factors(source, verbose)
    target_a, target_b, target_c = base_conversion_factors(target, verbose)

    scale = source_b * target_c / source_c / target_b
    offset = source_a * target_c / source_c / target_b - target_a / target_b

    if verbose:
        print(f"Scale: {scale:.15g}, offset: {offset:.15g}")

    return scale, offset


def convert(value, source=None, target=None, verbose=False):
    """Convert value(s) from source to target."""
    if source == target or ("unitless" in [source, target] and "" in [source, target]):
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
