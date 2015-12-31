"""Test functions."""
from unit_alias import unit_alias, unit_alias_dict
from uom import base_unit, convert


def test():
    """Test function."""
    tests = {
        "ft/h => ft/s": [1, "ft/h", "ft/s", 0.0002777777777777778],
        "m => ft": [10, "m", "ft", 32.80839895013123],
        "ft => m": [30, "ft", "m", 9.144],
        "degC => degF": [22.4, "degC", "degF", 72.32]
    }

    for k in sorted(tests):
        print("Test conversion {0}".format(k))
        print('=' * 80)
        i = tests[k]
        o = convert(i[0], i[1], i[2])

        if o == i[3]:
            print("OK {0}({1} == {2})".format(k, o, i[3]))
        else:
            assert(False)
            print("Error {0} ({1} <> {2}, diff {3} %)".format(k, o, i[3],
                                                              abs(100 - o /
                                                                  i[3] * 100)))

        print('=' * 80)

    for k in sorted(unit_alias_dict):
        print("Test unit alias {0}".format(k))
        print('=' * 80)

        unit = unit_alias(k)
        base = base_unit(unit)
        print("Alias: {0}, Unit: {1}, Base unit: {2}".format(k, unit, base))

        assert(base is not None)

        print('=' * 80)

test()
