# UOM

[![Codacy Badge](https://api.codacy.com/project/badge/grade/139005588a93460293258a672797615a)](https://www.codacy.com)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/ab7fbdf0551643a3b73dcf5fcd881572/badge.svg)](https://www.quantifiedcode.com/app/project/ab7fbdf0551643a3b73dcf5fcd881572)
[![Build Status](https://travis-ci.com/Schlumberger/UOM.svg?token=qgnSxUFcykzzPyjostSM&branch=master)](https://travis-ci.com/Schlumberger/UOM)
[![Coverage Status](https://coveralls.io/repos/Schlumberger/UOM/badge.svg?branch=master&service=github&t=ETSOWO)](https://coveralls.io/github/Schlumberger/UOM?branch=master)

# Build package

pip3.7 install wheel
python3.7 setup.py bdist_wheel

# Unit of Measure conversion tool

The conversion factors and unit symbols are based on the Energistics UOM 1.0:
http://www.energistics.org/news/energistics-publishes-unit-of-measure-standard-v1-0
extended with few extra unit aliases and "unitless" special unit that cannot be converted.

The units are cases sensitives.


## Install
```
gsutil cp gs://slb_dl/whl/uom-0.3.4-py2.py3-none-any.whl .
pip install uom-0.3.4-py2.py3-none-any.whl
```

## Examples

Please find few example of possible utilization:

### Find conversion factors to be applied to convert from one unit to another

```
from uom import conversion_factors

scale, offset = conversion_factors(source='m', target='ft')
```
### Convert a value from one unit to another

```
from uom import convert_value

print(convert(value=10, source='m', target='ft'))
```
### Return the base (SI) unit and if you are using unit alias you can find the equivalent Energistics UOM symbol

```
from uom import base_unit, unit_alias

print(base_unit('kft.lbf'))
print(unit_alias('kft.lbf'))
```

If you have suggestions for improvement or you found bugs, please don't hesitate to put them in the issue list.
