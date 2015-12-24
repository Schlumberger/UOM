# UOM
Unit of Measurements conversation factors tool

The tool conversion factors and unit spelling is based on the Energistics UOM 1.0:
http://www.energistics.org/news/energistics-publishes-unit-of-measure-standard-v1-0
extended with few extra unit aliases and "unitless" special unit that cannot be converted.

The units are cases sensitives.

Please find few example of utilization:

 - Find conversion factors to be applied to convert from one unit to another

```
from uom import conversion_factors

scale, offset = conversion_factors(source="m", target="ft")
```
 - Convert a value from one unit to another

```
from uom import convert_value

print(convert_value(value=10, source="m", target="ft"))
```
 - Return the base (SI) unit

```
from uom import base_unit

print(base_value("ft/h"))
```
