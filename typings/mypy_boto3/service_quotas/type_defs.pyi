"""
Type annotations for service-quotas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef

    data: DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ErrorCodeType,
    PeriodUnitType,
    RequestStatusType,
    ServiceQuotaTemplateAssociationStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "GetServiceQuotaRequestRequestTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasRequestRequestTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasRequestRequestTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

GetAWSDefaultServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetAWSDefaultServiceQuotaResponseTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    {
        "ServiceQuotaTemplateAssociationStatus": ServiceQuotaTemplateAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRequestedServiceQuotaChangeRequestRequestTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    {
        "RequestId": str,
    },
)

GetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetServiceQuotaResponseTypeDef = TypedDict(
    "GetServiceQuotaResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAWSDefaultServiceQuotasRequestRequestTypeDef = TypedDict(
    "_RequiredListAWSDefaultServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
    },
)
_OptionalListAWSDefaultServiceQuotasRequestRequestTypeDef = TypedDict(
    "_OptionalListAWSDefaultServiceQuotasRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAWSDefaultServiceQuotasRequestRequestTypeDef(
    _RequiredListAWSDefaultServiceQuotasRequestRequestTypeDef,
    _OptionalListAWSDefaultServiceQuotasRequestRequestTypeDef,
):
    pass

ListAWSDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef = TypedDict(
    "_RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)
_OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef = TypedDict(
    "_OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    {
        "Status": RequestStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef(
    _RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef,
    _OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef,
):
    pass

ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "Status": RequestStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "AwsRegion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            "ServiceQuotaIncreaseRequestInTemplateTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceQuotasRequestRequestTypeDef = TypedDict(
    "_RequiredListServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
    },
)
_OptionalListServiceQuotasRequestRequestTypeDef = TypedDict(
    "_OptionalListServiceQuotasRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListServiceQuotasRequestRequestTypeDef(
    _RequiredListServiceQuotasRequestRequestTypeDef, _OptionalListServiceQuotasRequestRequestTypeDef
):
    pass

ListServiceQuotasResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "NextToken": str,
        "Services": List["ServiceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
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

MetricInfoTypeDef = TypedDict(
    "MetricInfoTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    {
        "QuotaCode": str,
        "ServiceCode": str,
        "AwsRegion": str,
        "DesiredValue": float,
    },
)

PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": PeriodUnitType,
    },
    total=False,
)

RequestServiceQuotaIncreaseRequestRequestTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "DesiredValue": float,
    },
)

RequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": RequestStatusType,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
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

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
    },
    total=False,
)

ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": "MetricInfoTypeDef",
        "Period": "QuotaPeriodTypeDef",
        "ErrorReason": "ErrorReasonTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
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
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)
