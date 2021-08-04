"""
Type annotations for pi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pi.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import DetailStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DataPointTypeDef",
    "DescribeDimensionKeysRequestRequestTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "DimensionKeyDetailTypeDef",
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    "GetDimensionKeyDetailsResponseTypeDef",
    "GetResourceMetricsRequestRequestTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
)

_RequiredDescribeDimensionKeysRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDimensionKeysRequestRequestTypeDef",
    {
        "ServiceType": Literal["RDS"],
        "Identifier": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Metric": str,
        "GroupBy": "DimensionGroupTypeDef",
    },
)
_OptionalDescribeDimensionKeysRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDimensionKeysRequestRequestTypeDef",
    {
        "PeriodInSeconds": int,
        "PartitionBy": "DimensionGroupTypeDef",
        "Filter": Dict[str, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeDimensionKeysRequestRequestTypeDef(
    _RequiredDescribeDimensionKeysRequestRequestTypeDef,
    _OptionalDescribeDimensionKeysRequestRequestTypeDef,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDimensionGroupTypeDef = TypedDict(
    "_RequiredDimensionGroupTypeDef",
    {
        "Group": str,
    },
)
_OptionalDimensionGroupTypeDef = TypedDict(
    "_OptionalDimensionGroupTypeDef",
    {
        "Dimensions": List[str],
        "Limit": int,
    },
    total=False,
)

class DimensionGroupTypeDef(_RequiredDimensionGroupTypeDef, _OptionalDimensionGroupTypeDef):
    pass

DimensionKeyDescriptionTypeDef = TypedDict(
    "DimensionKeyDescriptionTypeDef",
    {
        "Dimensions": Dict[str, str],
        "Total": float,
        "Partitions": List[float],
    },
    total=False,
)

DimensionKeyDetailTypeDef = TypedDict(
    "DimensionKeyDetailTypeDef",
    {
        "Value": str,
        "Dimension": str,
        "Status": DetailStatusType,
    },
    total=False,
)

_RequiredGetDimensionKeyDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDimensionKeyDetailsRequestRequestTypeDef",
    {
        "ServiceType": Literal["RDS"],
        "Identifier": str,
        "Group": str,
        "GroupIdentifier": str,
    },
)
_OptionalGetDimensionKeyDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDimensionKeyDetailsRequestRequestTypeDef",
    {
        "RequestedDimensions": List[str],
    },
    total=False,
)

class GetDimensionKeyDetailsRequestRequestTypeDef(
    _RequiredGetDimensionKeyDetailsRequestRequestTypeDef,
    _OptionalGetDimensionKeyDetailsRequestRequestTypeDef,
):
    pass

GetDimensionKeyDetailsResponseTypeDef = TypedDict(
    "GetDimensionKeyDetailsResponseTypeDef",
    {
        "Dimensions": List["DimensionKeyDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": Literal["RDS"],
        "Identifier": str,
        "MetricQueries": List["MetricQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetResourceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceMetricsRequestRequestTypeDef",
    {
        "PeriodInSeconds": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetResourceMetricsRequestRequestTypeDef(
    _RequiredGetResourceMetricsRequestRequestTypeDef,
    _OptionalGetResourceMetricsRequestRequestTypeDef,
):
    pass

GetResourceMetricsResponseTypeDef = TypedDict(
    "GetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List["MetricKeyDataPointsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricKeyDataPointsTypeDef = TypedDict(
    "MetricKeyDataPointsTypeDef",
    {
        "Key": "ResponseResourceMetricKeyTypeDef",
        "DataPoints": List["DataPointTypeDef"],
    },
    total=False,
)

_RequiredMetricQueryTypeDef = TypedDict(
    "_RequiredMetricQueryTypeDef",
    {
        "Metric": str,
    },
)
_OptionalMetricQueryTypeDef = TypedDict(
    "_OptionalMetricQueryTypeDef",
    {
        "GroupBy": "DimensionGroupTypeDef",
        "Filter": Dict[str, str],
    },
    total=False,
)

class MetricQueryTypeDef(_RequiredMetricQueryTypeDef, _OptionalMetricQueryTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResponsePartitionKeyTypeDef = TypedDict(
    "ResponsePartitionKeyTypeDef",
    {
        "Dimensions": Dict[str, str],
    },
)

_RequiredResponseResourceMetricKeyTypeDef = TypedDict(
    "_RequiredResponseResourceMetricKeyTypeDef",
    {
        "Metric": str,
    },
)
_OptionalResponseResourceMetricKeyTypeDef = TypedDict(
    "_OptionalResponseResourceMetricKeyTypeDef",
    {
        "Dimensions": Dict[str, str],
    },
    total=False,
)

class ResponseResourceMetricKeyTypeDef(
    _RequiredResponseResourceMetricKeyTypeDef, _OptionalResponseResourceMetricKeyTypeDef
):
    pass
