"""
Main interface for service-quotas service type definitions.

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import ErrorReasonTypeDef

    data: ErrorReasonTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ErrorReasonTypeDef",
    "MetricInfoTypeDef",
    "QuotaPeriodTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ListServicesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
)

ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
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

QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
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
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef", {"ServiceCode": str, "ServiceName": str}, total=False
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

GetAWSDefaultServiceQuotaResponseTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaResponseTypeDef", {"Quota": "ServiceQuotaTypeDef"}, total=False
)

GetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    {"ServiceQuotaTemplateAssociationStatus": Literal["ASSOCIATED", "DISASSOCIATED"]},
    total=False,
)

GetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    {"RequestedQuota": "RequestedServiceQuotaChangeTypeDef"},
    total=False,
)

GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {"ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef"},
    total=False,
)

GetServiceQuotaResponseTypeDef = TypedDict(
    "GetServiceQuotaResponseTypeDef", {"Quota": "ServiceQuotaTypeDef"}, total=False
)

ListAWSDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List["ServiceQuotaTypeDef"]},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {"NextToken": str, "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"]},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {"NextToken": str, "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"]},
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            "ServiceQuotaIncreaseRequestInTemplateTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListServiceQuotasResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List["ServiceQuotaTypeDef"]},
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {"NextToken": str, "Services": List["ServiceInfoTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {"ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef"},
    total=False,
)

RequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseResponseTypeDef",
    {"RequestedQuota": "RequestedServiceQuotaChangeTypeDef"},
    total=False,
)
