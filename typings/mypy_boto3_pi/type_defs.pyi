"""
Main interface for pi service type definitions.

Usage::

    ```python
    from mypy_boto3_pi.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DataPointTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "MetricKeyDataPointsTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "MetricQueryTypeDef",
)

DataPointTypeDef = TypedDict("DataPointTypeDef", {"Timestamp": datetime, "Value": float})

_RequiredDimensionGroupTypeDef = TypedDict("_RequiredDimensionGroupTypeDef", {"Group": str})
_OptionalDimensionGroupTypeDef = TypedDict(
    "_OptionalDimensionGroupTypeDef", {"Dimensions": List[str], "Limit": int}, total=False
)


class DimensionGroupTypeDef(_RequiredDimensionGroupTypeDef, _OptionalDimensionGroupTypeDef):
    pass


DimensionKeyDescriptionTypeDef = TypedDict(
    "DimensionKeyDescriptionTypeDef",
    {"Dimensions": Dict[str, str], "Total": float, "Partitions": List[float]},
    total=False,
)

MetricKeyDataPointsTypeDef = TypedDict(
    "MetricKeyDataPointsTypeDef",
    {"Key": "ResponseResourceMetricKeyTypeDef", "DataPoints": List["DataPointTypeDef"]},
    total=False,
)

ResponsePartitionKeyTypeDef = TypedDict(
    "ResponsePartitionKeyTypeDef", {"Dimensions": Dict[str, str]}
)

_RequiredResponseResourceMetricKeyTypeDef = TypedDict(
    "_RequiredResponseResourceMetricKeyTypeDef", {"Metric": str}
)
_OptionalResponseResourceMetricKeyTypeDef = TypedDict(
    "_OptionalResponseResourceMetricKeyTypeDef", {"Dimensions": Dict[str, str]}, total=False
)


class ResponseResourceMetricKeyTypeDef(
    _RequiredResponseResourceMetricKeyTypeDef, _OptionalResponseResourceMetricKeyTypeDef
):
    pass


DescribeDimensionKeysResponseTypeDef = TypedDict(
    "DescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List["ResponsePartitionKeyTypeDef"],
        "Keys": List["DimensionKeyDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetResourceMetricsResponseTypeDef = TypedDict(
    "GetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List["MetricKeyDataPointsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredMetricQueryTypeDef = TypedDict("_RequiredMetricQueryTypeDef", {"Metric": str})
_OptionalMetricQueryTypeDef = TypedDict(
    "_OptionalMetricQueryTypeDef",
    {"GroupBy": "DimensionGroupTypeDef", "Filter": Dict[str, str]},
    total=False,
)


class MetricQueryTypeDef(_RequiredMetricQueryTypeDef, _OptionalMetricQueryTypeDef):
    pass
