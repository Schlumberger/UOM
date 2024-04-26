"""Command line option."""

from __future__ import absolute_import

from argparse import ArgumentParser

from colorlog import DEBUG, INFO, ColoredFormatter, StreamHandler, debug, getLogger

from uom import base_unit, convert


def cmd_convert(arg=None):
    """Convert value."""
    logger = getLogger()

    handler = StreamHandler()
    handler.setFormatter(
        ColoredFormatter(
            "%(log_color)s%(asctime)s [%(levelname)s]: %(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "green",
                "INFO": "cyan",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={},
            style="%",
        )
    )

    logger.propagate = False
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(INFO)

    # debug("Debug 1")
    # info("Info 1")

    parser = ArgumentParser(prog="uom_convert_value")

    parser.add_argument("value", type=float, nargs="+", help="value to be converted")

    parser.add_argument("-s", dest="source", help="unit source")

    parser.add_argument("-t", dest="target", help="unit target")

    parser.add_argument("-v", dest="verbose", action="store_true", help="verbose")

    if arg is not None:
        args = parser.parse_args(arg.split())
    else:
        args = parser.parse_args()

    if args.verbose:
        logger.setLevel(DEBUG)

        # debug("Debug 2")
        # info("Info 2")

        debug(args)

    if len(args.value) == 1:
        out = convert(args.value[0], args.source, args.target)
    else:
        out = convert(args.value, args.source, args.target)

    debug(f"Output: {out}")

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

    debug(args)

    out = base_unit(args.unit)

    debug(f"Output: {out}")

    return out
