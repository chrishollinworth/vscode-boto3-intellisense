"""
Type annotations for service-quotas service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef

    data: DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AppliedLevelEnumType,
    ErrorCodeType,
    PeriodUnitType,
    QuotaContextScopeType,
    RequestStatusType,
    ServiceQuotaTemplateAssociationStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaRequestTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetRequestedServiceQuotaChangeRequestTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "GetServiceQuotaRequestTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasRequestPaginateTypeDef",
    "ListAWSDefaultServiceQuotasRequestTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasRequestPaginateTypeDef",
    "ListServiceQuotasRequestTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ListServicesRequestPaginateTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "QuotaContextInfoTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseRequestTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

class DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

class ErrorReasonTypeDef(TypedDict):
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class GetAWSDefaultServiceQuotaRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetRequestedServiceQuotaChangeRequestTypeDef(TypedDict):
    RequestId: str

class GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "AwsRegion": NotRequired[str],
        "Unit": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
    },
)

class GetServiceQuotaRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    ContextId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAWSDefaultServiceQuotasRequestTypeDef(TypedDict):
    ServiceCode: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    Status: NotRequired[RequestStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuotaRequestedAtLevel: NotRequired[AppliedLevelEnumType]

class ListRequestedServiceQuotaChangeHistoryRequestTypeDef(TypedDict):
    ServiceCode: NotRequired[str]
    Status: NotRequired[RequestStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuotaRequestedAtLevel: NotRequired[AppliedLevelEnumType]

class ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef(TypedDict):
    ServiceCode: NotRequired[str]
    AwsRegion: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListServiceQuotasRequestTypeDef(TypedDict):
    ServiceCode: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuotaCode: NotRequired[str]
    QuotaAppliedAtLevel: NotRequired[AppliedLevelEnumType]

class ListServicesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class MetricInfoTypeDef(TypedDict):
    MetricNamespace: NotRequired[str]
    MetricName: NotRequired[str]
    MetricDimensions: NotRequired[Dict[str, str]]
    MetricStatisticRecommendation: NotRequired[str]

class PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef(TypedDict):
    QuotaCode: str
    ServiceCode: str
    AwsRegion: str
    DesiredValue: float

class QuotaContextInfoTypeDef(TypedDict):
    ContextScope: NotRequired[QuotaContextScopeType]
    ContextScopeType: NotRequired[str]
    ContextId: NotRequired[str]

class QuotaPeriodTypeDef(TypedDict):
    PeriodValue: NotRequired[int]
    PeriodUnit: NotRequired[PeriodUnitType]

class RequestServiceQuotaIncreaseRequestTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    DesiredValue: float
    ContextId: NotRequired[str]
    SupportCaseAllowed: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class GetAssociationForServiceQuotaTemplateResponseTypeDef(TypedDict):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(TypedDict):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(TypedDict):
    ServiceQuotaIncreaseRequestInTemplateList: List[ServiceQuotaIncreaseRequestInTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(TypedDict):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasRequestPaginateTypeDef(TypedDict):
    ServiceCode: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: str
    Status: NotRequired[RequestStatusType]
    QuotaRequestedAtLevel: NotRequired[AppliedLevelEnumType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef(TypedDict):
    ServiceCode: NotRequired[str]
    Status: NotRequired[RequestStatusType]
    QuotaRequestedAtLevel: NotRequired[AppliedLevelEnumType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef(TypedDict):
    ServiceCode: NotRequired[str]
    AwsRegion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceQuotasRequestPaginateTypeDef(TypedDict):
    ServiceCode: str
    QuotaCode: NotRequired[str]
    QuotaAppliedAtLevel: NotRequired[AppliedLevelEnumType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesResponseTypeDef(TypedDict):
    Services: List[ServiceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": NotRequired[str],
        "CaseId": NotRequired[str],
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "Status": NotRequired[RequestStatusType],
        "Created": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Requester": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
        "Unit": NotRequired[str],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
        "QuotaContext": NotRequired[QuotaContextInfoTypeDef],
    },
)
ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "Value": NotRequired[float],
        "Unit": NotRequired[str],
        "Adjustable": NotRequired[bool],
        "GlobalQuota": NotRequired[bool],
        "UsageMetric": NotRequired[MetricInfoTypeDef],
        "Period": NotRequired[QuotaPeriodTypeDef],
        "ErrorReason": NotRequired[ErrorReasonTypeDef],
        "QuotaAppliedAtLevel": NotRequired[AppliedLevelEnumType],
        "QuotaContext": NotRequired[QuotaContextInfoTypeDef],
        "Description": NotRequired[str],
    },
)

class GetRequestedServiceQuotaChangeResponseTypeDef(TypedDict):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(TypedDict):
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRequestedServiceQuotaChangeHistoryResponseTypeDef(TypedDict):
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RequestServiceQuotaIncreaseResponseTypeDef(TypedDict):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAWSDefaultServiceQuotaResponseTypeDef(TypedDict):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaResponseTypeDef(TypedDict):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasResponseTypeDef(TypedDict):
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceQuotasResponseTypeDef(TypedDict):
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
