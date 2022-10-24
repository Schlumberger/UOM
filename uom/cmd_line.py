"""Command line option."""
from __future__ import absolute_import

from argparse import ArgumentParser

from .uom import base_unit, convert


def cmd_convert(arg=None):
    """Convert value."""
    parser = ArgumentParser(prog="uom_convert_value")

    parser.add_argument("value", type=float, nargs="+", help="value to be converted")

    parser.add_argument("-s", dest="source", help="unit source")

    parser.add_argument("-t", dest="target", help="unit target")

    parser.add_argument("-v", dest="verbose", action="store_true", help="verbose")

    if arg is not None:
        args = parser.parse_args(arg.split())
    else:
        args = parser.parse_args()

    print(args)

    if len(args.value) == 1:
        out = convert(args.value[0], args.source, args.target, args.verbose)
    else:
        out = convert(args.value, args.source, args.target, args.verbose)

    if args.verbose:
        print(f"Output: {out}")

    return out


def cmd_base_unit(arg=None):
    """Base unit."""
    parser = ArgumentParser(prog="uom_base_unit")

    parser.add_argument("unit", help="input unit")

    parser.add_argument("-v", dest="verbose", action="store_true", help="verbose")

    if arg is not None:
        args = parser.parse_args(arg.split())
    else:
        args = parser.parse_args()

    print(args)

    out = base_unit(args.unit, args.verbose)

    if args.verbose:
        print(f"Output: {out}")

    return out
