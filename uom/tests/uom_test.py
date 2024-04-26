"""Test functions."""

from __future__ import absolute_import

from unittest import TestCase, main

from pandas import DataFrame

from ..cmd_line import cmd_base_unit, cmd_convert
from ..unit_alias import UNIT_ALIAS_DICT
from ..uom import (
    base_conversion_factors,
    base_unit,
    conversion_factors,
    convert,
    unit_alias,
)


class UOMTestCase(TestCase):
    """Test class."""

    def test_conversion_of_value(self):
        """Test conversion function."""
        tests = {
            "ft/h => ft/s": [1, "ft/h", "ft/s", 0.0002777777777777778],
            "m => ft": [10, "m", "ft", 32.80839895013123],
            "psi => Pa": [1, "psi", "Pa", 6894.757293168361],
            "psi => J/m3": [1, "psi", "J/m3", 6894.757293168361],
            #                             6894.7572931683608
            #                             6894.757293168
            # http://www.metric4us.com/calculator.html
            #                             6894.757293168362
            # python                      6894.757293168361
            "Pa => psi": [1, "Pa", "psi", 0.0001450377377302092],
            "N => J.m/m2": [1, "N", "J.m/m2", 1],
            "J.m/m2 => N": [1, "J.m/m2", "N", 1],
            "Hz => 1/s": [1, "Hz", "1/s", 1],
            "1/s => Hz": [1, "1/s", "Hz", 1],
            "ft => m": [30, "ft", "m", 9.144],
            "N.m => J": [1, "N.m", "J", 1],
            "W => J/s": [1, "W", "J/s", 1],
            "kft.lbf => J": [1, "kft.lbf", "J", 1355.8179483314004],
            "degC => degF": [22.4, "degC", "degF", 72.32],
        }

        for k in sorted(tests):
            i = tests[k]
            out = convert(i[0], i[1], i[2])

            self.assertEqual(out, i[3])

        # target unit missing test
        k = "ft => m"
        i = tests[k]
        out = convert(i[0], i[1], None)

        self.assertEqual(out, i[3])

        # source unit missing test
        k = "m => ft"
        i = tests[k]
        out = convert(i[0], None, i[2])

        # convert uncompatible unit return None
        out = convert(1, "m", "kg")

        self.assertIsNone(out)

        # convert uncompatible unit_aliases return None
        out = convert(1, "gal/min", "kft.lbf")

        self.assertIsNone(out)

        # convert none dimension unit return None
        out = convert(1, "B", "gAPI")

        self.assertIsNone(out)

        for k in sorted(tests):
            i = tests[k]
            arg = f"{i[0]} -s={i[1]} -t={i[2]}"
            print("\n===== arg:", arg)
            out = cmd_convert(arg)

            self.assertEqual(out, i[3])

        for k in sorted(tests):
            i = tests[k]
            arg = f"{i[0]} -s={i[1]} -t={i[2]} -v"
            print("\n===== arg:", arg)
            out = cmd_convert(arg)

            self.assertEqual(out, i[3])

        # cmd_convert()
        # cmd_base_unit()

    def test_conversion_unitless(self):
        """Test conversion of unitless function."""
        tests = {"u1": [10, "", "unitless", 10], "u2": [10, "unitless", "", 10]}

        for k in sorted(tests):
            i = tests[k]
            arg = f"{i[0]} -s={i[1]} -t={i[2]}"
            print("\n===== arg:", arg)
            out = cmd_convert(arg)

            self.assertTrue(out == i[3])

    def test_conversion_of_list(self):
        """Test conversion of list function."""
        tests = {
            "m => ft": [[10, 100], "m", "ft", [32.80839895013123, 328.0839895013123]],
        }

        for k in sorted(tests):
            i = tests[k]
            arg = f"""{' '.join([str(x) for x in i[0]])} -s={i[1]} -t={i[2]}"""

            print("\n===== arg:", arg)
            out = cmd_convert(arg)

            self.assertTrue(out == i[3])

    def test_conversion_of_dataframe(self):
        """Test conversion of list function."""
        dtf = DataFrame({"m": [10, 100], "ft": [32.80839895013123, 328.0839895013123]})

        out = convert(dtf["m"], "m", "ft")

        self.assertTrue(dtf["ft"].equals(out))

    def test_bad_base_unit(self):
        """Test base_unit function with bad parameter."""
        base = base_unit("jhdfkjshdfkjs")
        self.assertIsNone(base)

    def test_cmd_base_unit(self):
        """Test base_unit function with bad parameter."""
        base = cmd_base_unit("jhdfkjshdfkjs")
        self.assertIsNone(base)

        base = cmd_base_unit("jhdfkjshdfkjs -v")
        self.assertIsNone(base)
        base = cmd_base_unit("psi")
        self.assertEqual(base, "J/m3")

    def test_bad_convert(self):
        """Test convert function with bad parameter."""
        result = convert(10, "jhdfkjshdfkjs", "")
        self.assertIsNone(result)

        result = convert(10, "", "jhdfkjshdfkjs")
        self.assertIsNone(result)

        result = convert("aaa", "", "jhdfkjshdfkjs")
        self.assertIsNone(result)

        result = convert(10, None, "jhdfkjshdfkjs")
        self.assertIsNone(result)

        result = convert(10, "jhdfkjshdfkjs", None)
        self.assertIsNone(result)

        result = convert("m", 10, "")
        self.assertIsNone(result)

        result = convert("m", "", 10)
        self.assertIsNone(result)

        result = convert(10, "", "")
        self.assertEqual(result, 10)

        result = convert(10, "m", "degC")
        self.assertIsNone(result)

    def test_bad_conversion_factors(self):
        """Test conversion_factors function with bad parameter."""
        scale, offset = conversion_factors("jhdfkjshdfkjs", "")
        self.assertIsNone(scale)
        self.assertIsNone(offset)

    def test_base_unit_recursive(self):
        """Test base_unit recursive."""
        base = base_unit("J.m/m2")
        self.assertEqual(base, "N")

        scale, offset = conversion_factors("Hz", "1/s")
        self.assertEqual(scale, 1)
        self.assertEqual(offset, 0)

        scale, offset = conversion_factors("m3/m3", "%")
        self.assertEqual(scale, 100)
        self.assertEqual(offset, 0)

    def test_bad_base_conv_factors(self):
        """Test base_conversion_factors function with bad parameter."""
        aaa, bbb, ccc = base_conversion_factors("jhdfkjshdfkjs")
        self.assertIsNone(aaa)
        self.assertIsNone(bbb)
        self.assertIsNone(ccc)

    def test_unit_alias(self):
        """Test unit_alias function."""
        for k in sorted(UNIT_ALIAS_DICT):
            unit = unit_alias(k)
            base = base_unit(unit)
            self.assertIsNotNone(base)

        unit = unit_alias("jhdfkjshdfkjs")
        self.assertEqual(unit, "jhdfkjshdfkjs")

    def test_conv_without_target(self):
        """Test conversion without target."""
        out = cmd_convert("-s psi 1 -v")
        self.assertEqual(out, 6894.757293168361)


if __name__ == "__main__":
    main()
