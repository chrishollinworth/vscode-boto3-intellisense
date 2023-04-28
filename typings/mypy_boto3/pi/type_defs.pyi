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

from .literals import DetailStatusType, FeatureStatusType, PeriodAlignmentType, ServiceTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DataPointTypeDef",
    "DescribeDimensionKeysRequestRequestTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionDetailTypeDef",
    "DimensionGroupDetailTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "DimensionKeyDetailTypeDef",
    "FeatureMetadataTypeDef",
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    "GetDimensionKeyDetailsResponseTypeDef",
    "GetResourceMetadataRequestRequestTypeDef",
    "GetResourceMetadataResponseTypeDef",
    "GetResourceMetricsRequestRequestTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    "ListAvailableResourceDimensionsResponseTypeDef",
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    "ListAvailableResourceMetricsResponseTypeDef",
    "MetricDimensionGroupsTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "ResponseResourceMetricTypeDef",
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
        "ServiceType": ServiceTypeType,
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
        "AdditionalMetrics": List[str],
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

DimensionDetailTypeDef = TypedDict(
    "DimensionDetailTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)

DimensionGroupDetailTypeDef = TypedDict(
    "DimensionGroupDetailTypeDef",
    {
        "Group": str,
        "Dimensions": List["DimensionDetailTypeDef"],
    },
    total=False,
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
        "AdditionalMetrics": Dict[str, float],
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

FeatureMetadataTypeDef = TypedDict(
    "FeatureMetadataTypeDef",
    {
        "Status": FeatureStatusType,
    },
    total=False,
)

_RequiredGetDimensionKeyDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDimensionKeyDetailsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
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

GetResourceMetadataRequestRequestTypeDef = TypedDict(
    "GetResourceMetadataRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
    },
)

GetResourceMetadataResponseTypeDef = TypedDict(
    "GetResourceMetadataResponseTypeDef",
    {
        "Identifier": str,
        "Features": Dict[str, "FeatureMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
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
        "PeriodAlignment": PeriodAlignmentType,
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

_RequiredListAvailableResourceDimensionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableResourceDimensionsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "Metrics": List[str],
    },
)
_OptionalListAvailableResourceDimensionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableResourceDimensionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAvailableResourceDimensionsRequestRequestTypeDef(
    _RequiredListAvailableResourceDimensionsRequestRequestTypeDef,
    _OptionalListAvailableResourceDimensionsRequestRequestTypeDef,
):
    pass

ListAvailableResourceDimensionsResponseTypeDef = TypedDict(
    "ListAvailableResourceDimensionsResponseTypeDef",
    {
        "MetricDimensions": List["MetricDimensionGroupsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAvailableResourceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "MetricTypes": List[str],
    },
)
_OptionalListAvailableResourceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableResourceMetricsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAvailableResourceMetricsRequestRequestTypeDef(
    _RequiredListAvailableResourceMetricsRequestRequestTypeDef,
    _OptionalListAvailableResourceMetricsRequestRequestTypeDef,
):
    pass

ListAvailableResourceMetricsResponseTypeDef = TypedDict(
    "ListAvailableResourceMetricsResponseTypeDef",
    {
        "Metrics": List["ResponseResourceMetricTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionGroupsTypeDef = TypedDict(
    "MetricDimensionGroupsTypeDef",
    {
        "Metric": str,
        "Groups": List["DimensionGroupDetailTypeDef"],
    },
    total=False,
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

ResponseResourceMetricTypeDef = TypedDict(
    "ResponseResourceMetricTypeDef",
    {
        "Metric": str,
        "Description": str,
        "Unit": str,
    },
    total=False,
)
