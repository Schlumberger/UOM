# UOM
Unit of Measurements conversation factors tool

The tool is using the Energistics UOM 1.0
http://www.energistics.org/news/energistics-publishes-unit-of-measure-standard-v1-0

Please find example of utilization:
```
from uom import conversion_factors

scale, offset = conversion_factors(source="m", target="ft")
```
or
```
from uom import convert_value

print(convert_value(value=10, source="m", target="ft"))
```
