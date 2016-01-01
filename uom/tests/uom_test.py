"""Test functions."""
# from os.path import dirname
# from sys.path import insert; insert(0, dirname(dirname(__file__)))
from unittest import TestCase, main

from ..unit_alias import unit_alias, unit_alias_dict
from ..uom import base_unit, convert


class UOMTestCase(TestCase):
    """Test class."""

    def test_conversion(self):
        """Test conversion function."""
        tests = {
            "ft/h => ft/s": [1, "ft/h", "ft/s", 0.0002777777777777778],
            "m => ft": [10, "m", "ft", 32.80839895013123],
            "ft => m": [30, "ft", "m", 9.144],
            "degC => degF": [22.4, "degC", "degF", 72.32]
        }

        for k in sorted(tests):
            i = tests[k]
            o = convert(i[0], i[1], i[2])

            self.assertEqual(o, i[3])

    def test_unit_alis(self):
        """Test unit aliases function."""
        for k in sorted(unit_alias_dict):
            unit = unit_alias(k)
            base = base_unit(unit)
            self.assertIsNotNone(base)


if __name__ == '__main__':
    main()
