"""Command line option."""
from .uom import convert


def main(value, source, target):
    """Convert value."""
    return convert(value, source, target)
