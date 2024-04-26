# UOM

## Static code analysis

| Tools | Badges |
| --- | --------------------------- |
| Scrutinizer | [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Schlumberger/UOM/?branch=master) [![Code Coverage](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/Schlumberger/UOM/?branch=master) [![Build Status](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Schlumberger/UOM/build-status/master) [![Code Intelligence Status](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence) |
| Codacy | [![Codacy Badge](https://app.codacy.com/project/badge/Grade/f2c1140afacf439c8fec00194acdc7db)](https://www.codacy.com/gh/Schlumberger/UOM/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Schlumberger/UOM&amp;utm_campaign=Badge_Grade) |
| Codecov | [![codecov](https://codecov.io/gh/Schlumberger/UOM/branch/master/graph/badge.svg?token=mUH2Yzsxmd)](https://codecov.io/gh/Schlumberger/UOM) |
| Coveralls | [![Coverage Status](https://coveralls.io/repos/github/Schlumberger/UOM/badge.svg?branch=master)](https://coveralls.io/github/Schlumberger/UOM?branch=master) |
| CodeQL | [![CodeQL](https://github.com/Schlumberger/UOM/actions/workflows/codeql.yml/badge.svg)](https://github.com/Schlumberger/UOM/actions/workflows/codeql.yml) |
| CircleCI | [![CircleCI](https://circleci.com/gh/Schlumberger/UOM/tree/master.svg?style=svg)](https://circleci.com/gh/Schlumberger/UOM/tree/master) |
| TravisCI | [![Build Status](https://travis-ci.com/Schlumberger/UOM.svg?token=qgnSxUFcykzzPyjostSM&branch=master)](https://travis-ci.com/Schlumberger/UOM) |
| Fossa | [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSchlumberger%2FUOM.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FSchlumberger%2FUOM?ref=badge_shield) |
| PyPI | [![PyPI Latest Release](https://img.shields.io/pypi/v/uom.svg)](https://pypi.org/project/uom/) [![Package Status](https://img.shields.io/pypi/status/uom.svg)](https://pypi.org/project/uom/) [![Python](https://img.shields.io/pypi/pyversions/uom.svg?style=plastic)](https://badge.fury.io/py/uom) |
| PePy | [![Downloads](https://pepy.tech/badge/uom)](https://pepy.tech/project/uom) [![Downloads](https://pepy.tech/badge/uom/month)](https://pepy.tech/project/uom) [![Downloads](https://pepy.tech/badge/uom/week)](https://pepy.tech/project/uom) |
| Code formatting | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |

<!--
## Build package

```sh
pip3 install test-requirements.txt
python -m build
``` -->

## Description

Python unit of measure (UOM) conversion tool

Energistics UOM 1.0 (<https://www.energistics.org/energistics-unit-of-measure-standard/>)
is the primary source of conversion factors and unit symbols.
We extended it with additional unit aliases and a \"unitless\" unit that
doesn't have any conversion.

The units are case-sensitive.

## Where to get it

The source code is available on GitHub at: <https://github.com/Schlumberger/UOM>

Binary installers for the latest released version are available at the Python
Package Index (PyPI).

```sh
pip install uom
```

## Usage

Please find examples of possible utilization:

Find conversion factors to be applied to convert from one unit to another

```Python
from uom import conversion_factors

scale, offset = conversion_factors(source='m', target='ft')
```

Convert a value from one unit to another

```Python
from uom import convert

print(convert(value=10, source='m', target='ft'))
```

Return the base SI (
<https://en.wikipedia.org/wiki/International_System_of_Units>) unit.
If you are using unit alias you can find the compatible Energistics UOM symbol

```Python
from uom import base_unit, unit_alias

print(base_unit('kft.lbf'))
print(unit_alias('kft.lbf'))
```

If you have suggestions for improvement or you found bugs,
please don't hesitate to put them on the issue list.

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSchlumberger%2FUOM.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSchlumberger%2FUOM?ref=badge_large)
