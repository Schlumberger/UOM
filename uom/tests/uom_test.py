"""Test functions."""
from unittest import TestCase, main

from ..command_line import main as main2
from ..unit_alias import unit_alias_dict
from ..uom import (base_conversion_factors, base_unit, conversion_factors,
                   convert, unit_alias)
from pandas import DataFrame


class UOMTestCase(TestCase):
    """Test class."""

    def test_conversion_of_value(self):
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

        # verbose tests
        for k in sorted(tests):
            i = tests[k]
            o = convert(i[0], i[1], i[2], True)

            self.assertEqual(o, i[3])

        # target unit missing test
        k = "ft => m"
        i = tests[k]
        o = convert(i[0], i[1], None)

        self.assertEqual(o, i[3])

        # source unit missing test
        k = "m => ft"
        i = tests[k]
        o = convert(i[0], None, i[2])

        self.assertEqual(o, i[3])

        for k in sorted(tests):
            i = tests[k]
            o = main2(i[0], i[1], i[2])

            self.assertEqual(o, i[3])

    def test_conversion_of_list(self):
        """Test conversion of list function."""
        tests = {
            "m => ft": [[10, 100], "m", "ft",
                        [32.80839895013123, 328.0839895013123]],
        }

        for k in sorted(tests):
            i = tests[k]
            o = main2(i[0], i[1], i[2])

            self.assertTrue(o == i[3])

    def test_conversion_of_dataframe(self):
        """Test conversion of list function."""
        df = DataFrame({"m": [10, 100], "ft":
                       [32.80839895013123, 328.0839895013123]})

        o = convert(df['m'], 'm', 'ft')

        self.assertTrue(df['ft'].equals(o))

    def test_bad_base_unit(self):
        """Test base_unit function with bad parameter."""
        base = base_unit("jhdfkjshdfkjs")
        self.assertIsNone(base)

        base = base_unit("jhdfkjshdfkjs", True)
        self.assertIsNone(base)

    def test_bad_convert(self):
        """Test convert function with bad parameter."""
        result = convert(10, "jhdfkjshdfkjs", '', True)
        self.assertIsNone(result)

        result = convert(10, "", 'jhdfkjshdfkjs')
        self.assertIsNone(result)

        result = convert("A", "", 'jhdfkjshdfkjs')
        self.assertIsNone(result)

        result = convert(10, None, 'jhdfkjshdfkjs')
        self.assertIsNone(result)

        result = convert(10, "jhdfkjshdfkjs", None)
        self.assertIsNone(result)

        result = convert("m", 10, '')
        self.assertIsNone(result)

        result = convert("m", '', 10)
        self.assertIsNone(result)

        result = convert(10, '', '')
        self.assertEqual(result, 10)

        result = convert(10, 'm', 'degC')
        self.assertIsNone(result)

        result = convert(10, 'm', 'degC', True)
        self.assertIsNone(result)

    def test_bad_conversion_factors(self):
        """Test conversion_factors function with bad parameter."""
        scale, offset = conversion_factors("jhdfkjshdfkjs", '', True)
        self.assertIsNone(scale)
        self.assertIsNone(offset)

        scale, offset = conversion_factors("", 'jhdfkjshdfkjs')
        self.assertIsNone(scale)
        self.assertIsNone(offset)

    def test_bad_base_conversion_factors(self):
        """Test base_conversion_factors function with bad parameter."""
        a, b, c = base_conversion_factors("jhdfkjshdfkjs", True)
        self.assertIsNone(a)
        self.assertIsNone(b)
        self.assertIsNone(c)

    def test_unit_alias(self):
        """Test unit_alias function."""
        for k in sorted(unit_alias_dict):
            unit = unit_alias(k)
            base = base_unit(unit)
            self.assertIsNotNone(base)

        unit = unit_alias('jhdfkjshdfkjs')
        self.assertEqual(unit, 'jhdfkjshdfkjs')


if __name__ == '__main__':
    main()
