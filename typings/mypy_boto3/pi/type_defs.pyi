"""
Type annotations for pi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pi.type_defs import AnalysisReportSummaryTypeDef

    data: AnalysisReportSummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnalysisStatusType,
    ContextTypeType,
    DetailStatusType,
    FeatureStatusType,
    FineGrainedActionType,
    PeriodAlignmentType,
    ServiceTypeType,
    SeverityType,
    TextFormatType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AnalysisReportSummaryTypeDef",
    "AnalysisReportTypeDef",
    "CreatePerformanceAnalysisReportRequestRequestTypeDef",
    "CreatePerformanceAnalysisReportResponseTypeDef",
    "DataPointTypeDef",
    "DataTypeDef",
    "DeletePerformanceAnalysisReportRequestRequestTypeDef",
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
    "GetPerformanceAnalysisReportRequestRequestTypeDef",
    "GetPerformanceAnalysisReportResponseTypeDef",
    "GetResourceMetadataRequestRequestTypeDef",
    "GetResourceMetadataResponseTypeDef",
    "GetResourceMetricsRequestRequestTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "InsightTypeDef",
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    "ListAvailableResourceDimensionsResponseTypeDef",
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    "ListAvailableResourceMetricsResponseTypeDef",
    "ListPerformanceAnalysisReportsRequestRequestTypeDef",
    "ListPerformanceAnalysisReportsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDimensionGroupsTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "PerformanceInsightsMetricTypeDef",
    "RecommendationTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "ResponseResourceMetricTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AnalysisReportSummaryTypeDef = TypedDict(
    "AnalysisReportSummaryTypeDef",
    {
        "AnalysisReportId": str,
        "CreateTime": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": AnalysisStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredAnalysisReportTypeDef = TypedDict(
    "_RequiredAnalysisReportTypeDef",
    {
        "AnalysisReportId": str,
    },
)
_OptionalAnalysisReportTypeDef = TypedDict(
    "_OptionalAnalysisReportTypeDef",
    {
        "Identifier": str,
        "ServiceType": ServiceTypeType,
        "CreateTime": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": AnalysisStatusType,
        "Insights": List["InsightTypeDef"],
    },
    total=False,
)

class AnalysisReportTypeDef(_RequiredAnalysisReportTypeDef, _OptionalAnalysisReportTypeDef):
    pass

_RequiredCreatePerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalCreatePerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePerformanceAnalysisReportRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePerformanceAnalysisReportRequestRequestTypeDef(
    _RequiredCreatePerformanceAnalysisReportRequestRequestTypeDef,
    _OptionalCreatePerformanceAnalysisReportRequestRequestTypeDef,
):
    pass

CreatePerformanceAnalysisReportResponseTypeDef = TypedDict(
    "CreatePerformanceAnalysisReportResponseTypeDef",
    {
        "AnalysisReportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
)

DataTypeDef = TypedDict(
    "DataTypeDef",
    {
        "PerformanceInsightsMetric": "PerformanceInsightsMetricTypeDef",
    },
    total=False,
)

DeletePerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "DeletePerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "AnalysisReportId": str,
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

_RequiredGetPerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "_RequiredGetPerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "AnalysisReportId": str,
    },
)
_OptionalGetPerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "_OptionalGetPerformanceAnalysisReportRequestRequestTypeDef",
    {
        "TextFormat": TextFormatType,
        "AcceptLanguage": Literal["EN_US"],
    },
    total=False,
)

class GetPerformanceAnalysisReportRequestRequestTypeDef(
    _RequiredGetPerformanceAnalysisReportRequestRequestTypeDef,
    _OptionalGetPerformanceAnalysisReportRequestRequestTypeDef,
):
    pass

GetPerformanceAnalysisReportResponseTypeDef = TypedDict(
    "GetPerformanceAnalysisReportResponseTypeDef",
    {
        "AnalysisReport": "AnalysisReportTypeDef",
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

_RequiredInsightTypeDef = TypedDict(
    "_RequiredInsightTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalInsightTypeDef = TypedDict(
    "_OptionalInsightTypeDef",
    {
        "InsightType": str,
        "Context": ContextTypeType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Severity": SeverityType,
        "SupportingInsights": List[Dict[str, Any]],
        "Description": str,
        "Recommendations": List["RecommendationTypeDef"],
        "InsightData": List["DataTypeDef"],
        "BaselineData": List["DataTypeDef"],
    },
    total=False,
)

class InsightTypeDef(_RequiredInsightTypeDef, _OptionalInsightTypeDef):
    pass

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
        "AuthorizedActions": List[FineGrainedActionType],
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

_RequiredListPerformanceAnalysisReportsRequestRequestTypeDef = TypedDict(
    "_RequiredListPerformanceAnalysisReportsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
    },
)
_OptionalListPerformanceAnalysisReportsRequestRequestTypeDef = TypedDict(
    "_OptionalListPerformanceAnalysisReportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ListTags": bool,
    },
    total=False,
)

class ListPerformanceAnalysisReportsRequestRequestTypeDef(
    _RequiredListPerformanceAnalysisReportsRequestRequestTypeDef,
    _OptionalListPerformanceAnalysisReportsRequestRequestTypeDef,
):
    pass

ListPerformanceAnalysisReportsResponseTypeDef = TypedDict(
    "ListPerformanceAnalysisReportsResponseTypeDef",
    {
        "AnalysisReports": List["AnalysisReportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

PerformanceInsightsMetricTypeDef = TypedDict(
    "PerformanceInsightsMetricTypeDef",
    {
        "Metric": str,
        "DisplayName": str,
        "Dimensions": Dict[str, str],
        "Value": float,
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "RecommendationId": str,
        "RecommendationDescription": str,
    },
    total=False,
)

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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)
