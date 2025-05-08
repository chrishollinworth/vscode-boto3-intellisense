"""
Type annotations for trustedadvisor service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_trustedadvisor.type_defs import AccountRecommendationLifecycleSummaryTypeDef

    data: AccountRecommendationLifecycleSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ExclusionStatusType,
    RecommendationLanguageType,
    RecommendationLifecycleStageType,
    RecommendationPillarType,
    RecommendationSourceType,
    RecommendationStatusType,
    RecommendationTypeType,
    ResourceStatusType,
    UpdateRecommendationLifecycleStageReasonCodeType,
    UpdateRecommendationLifecycleStageType,
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
    "AccountRecommendationLifecycleSummaryTypeDef",
    "BatchUpdateRecommendationResourceExclusionRequestTypeDef",
    "BatchUpdateRecommendationResourceExclusionResponseTypeDef",
    "CheckSummaryTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetOrganizationRecommendationRequestTypeDef",
    "GetOrganizationRecommendationResponseTypeDef",
    "GetRecommendationRequestTypeDef",
    "GetRecommendationResponseTypeDef",
    "ListChecksRequestPaginateTypeDef",
    "ListChecksRequestTypeDef",
    "ListChecksResponseTypeDef",
    "ListOrganizationRecommendationAccountsRequestPaginateTypeDef",
    "ListOrganizationRecommendationAccountsRequestTypeDef",
    "ListOrganizationRecommendationAccountsResponseTypeDef",
    "ListOrganizationRecommendationResourcesRequestPaginateTypeDef",
    "ListOrganizationRecommendationResourcesRequestTypeDef",
    "ListOrganizationRecommendationResourcesResponseTypeDef",
    "ListOrganizationRecommendationsRequestPaginateTypeDef",
    "ListOrganizationRecommendationsRequestTypeDef",
    "ListOrganizationRecommendationsResponseTypeDef",
    "ListRecommendationResourcesRequestPaginateTypeDef",
    "ListRecommendationResourcesRequestTypeDef",
    "ListRecommendationResourcesResponseTypeDef",
    "ListRecommendationsRequestPaginateTypeDef",
    "ListRecommendationsRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "OrganizationRecommendationResourceSummaryTypeDef",
    "OrganizationRecommendationSummaryTypeDef",
    "OrganizationRecommendationTypeDef",
    "PaginatorConfigTypeDef",
    "RecommendationCostOptimizingAggregatesTypeDef",
    "RecommendationPillarSpecificAggregatesTypeDef",
    "RecommendationResourceExclusionTypeDef",
    "RecommendationResourceSummaryTypeDef",
    "RecommendationResourcesAggregatesTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendationTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "UpdateOrganizationRecommendationLifecycleRequestTypeDef",
    "UpdateRecommendationLifecycleRequestTypeDef",
    "UpdateRecommendationResourceExclusionErrorTypeDef",
)

class AccountRecommendationLifecycleSummaryTypeDef(TypedDict):
    accountId: NotRequired[str]
    accountRecommendationArn: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]
    lifecycleStage: NotRequired[RecommendationLifecycleStageType]
    updateReason: NotRequired[str]
    updateReasonCode: NotRequired[UpdateRecommendationLifecycleStageReasonCodeType]
    updatedOnBehalfOf: NotRequired[str]
    updatedOnBehalfOfJobTitle: NotRequired[str]

class RecommendationResourceExclusionTypeDef(TypedDict):
    arn: str
    isExcluded: bool

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UpdateRecommendationResourceExclusionErrorTypeDef(TypedDict):
    arn: NotRequired[str]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

CheckSummaryTypeDef = TypedDict(
    "CheckSummaryTypeDef",
    {
        "arn": str,
        "awsServices": List[str],
        "description": str,
        "id": str,
        "metadata": Dict[str, str],
        "name": str,
        "pillars": List[RecommendationPillarType],
        "source": RecommendationSourceType,
    },
)

class GetOrganizationRecommendationRequestTypeDef(TypedDict):
    organizationRecommendationIdentifier: str

class GetRecommendationRequestTypeDef(TypedDict):
    recommendationIdentifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChecksRequestTypeDef(TypedDict):
    awsService: NotRequired[str]
    language: NotRequired[RecommendationLanguageType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    pillar: NotRequired[RecommendationPillarType]
    source: NotRequired[RecommendationSourceType]

class ListOrganizationRecommendationAccountsRequestTypeDef(TypedDict):
    organizationRecommendationIdentifier: str
    affectedAccountId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListOrganizationRecommendationResourcesRequestTypeDef(TypedDict):
    organizationRecommendationIdentifier: str
    affectedAccountId: NotRequired[str]
    exclusionStatus: NotRequired[ExclusionStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    regionCode: NotRequired[str]
    status: NotRequired[ResourceStatusType]

OrganizationRecommendationResourceSummaryTypeDef = TypedDict(
    "OrganizationRecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
        "accountId": NotRequired[str],
        "exclusionStatus": NotRequired[ExclusionStatusType],
    },
)
TimestampTypeDef = Union[datetime, str]

class ListRecommendationResourcesRequestTypeDef(TypedDict):
    recommendationIdentifier: str
    exclusionStatus: NotRequired[ExclusionStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    regionCode: NotRequired[str]
    status: NotRequired[ResourceStatusType]

RecommendationResourceSummaryTypeDef = TypedDict(
    "RecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
        "exclusionStatus": NotRequired[ExclusionStatusType],
    },
)

class RecommendationResourcesAggregatesTypeDef(TypedDict):
    errorCount: int
    okCount: int
    warningCount: int

class RecommendationCostOptimizingAggregatesTypeDef(TypedDict):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float

class UpdateOrganizationRecommendationLifecycleRequestTypeDef(TypedDict):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    organizationRecommendationIdentifier: str
    updateReason: NotRequired[str]
    updateReasonCode: NotRequired[UpdateRecommendationLifecycleStageReasonCodeType]

class UpdateRecommendationLifecycleRequestTypeDef(TypedDict):
    lifecycleStage: UpdateRecommendationLifecycleStageType
    recommendationIdentifier: str
    updateReason: NotRequired[str]
    updateReasonCode: NotRequired[UpdateRecommendationLifecycleStageReasonCodeType]

class BatchUpdateRecommendationResourceExclusionRequestTypeDef(TypedDict):
    recommendationResourceExclusions: Sequence[RecommendationResourceExclusionTypeDef]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationRecommendationAccountsResponseTypeDef(TypedDict):
    accountRecommendationLifecycleSummaries: List[AccountRecommendationLifecycleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchUpdateRecommendationResourceExclusionResponseTypeDef(TypedDict):
    batchUpdateRecommendationResourceExclusionErrors: List[
        UpdateRecommendationResourceExclusionErrorTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChecksResponseTypeDef(TypedDict):
    checkSummaries: List[CheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListChecksRequestPaginateTypeDef(TypedDict):
    awsService: NotRequired[str]
    language: NotRequired[RecommendationLanguageType]
    pillar: NotRequired[RecommendationPillarType]
    source: NotRequired[RecommendationSourceType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationRecommendationAccountsRequestPaginateTypeDef(TypedDict):
    organizationRecommendationIdentifier: str
    affectedAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationRecommendationResourcesRequestPaginateTypeDef(TypedDict):
    organizationRecommendationIdentifier: str
    affectedAccountId: NotRequired[str]
    exclusionStatus: NotRequired[ExclusionStatusType]
    regionCode: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendationResourcesRequestPaginateTypeDef(TypedDict):
    recommendationIdentifier: str
    exclusionStatus: NotRequired[ExclusionStatusType]
    regionCode: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationRecommendationResourcesResponseTypeDef(TypedDict):
    organizationRecommendationResourceSummaries: List[
        OrganizationRecommendationResourceSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListOrganizationRecommendationsRequestPaginateTypeDef = TypedDict(
    "ListOrganizationRecommendationsRequestPaginateTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationRecommendationsRequestTypeDef = TypedDict(
    "ListOrganizationRecommendationsRequestTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
    },
)
ListRecommendationsRequestPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestPaginateTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestTypeDef = TypedDict(
    "ListRecommendationsRequestTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
    },
)

class ListRecommendationResourcesResponseTypeDef(TypedDict):
    recommendationResourceSummaries: List[RecommendationResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RecommendationPillarSpecificAggregatesTypeDef(TypedDict):
    costOptimizing: NotRequired[RecommendationCostOptimizingAggregatesTypeDef]

OrganizationRecommendationSummaryTypeDef = TypedDict(
    "OrganizationRecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
    },
)
OrganizationRecommendationTypeDef = TypedDict(
    "OrganizationRecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
        "resolvedAt": NotRequired[datetime],
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
        "updatedOnBehalfOf": NotRequired[str],
        "updatedOnBehalfOfJobTitle": NotRequired[str],
    },
)
RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
        "resolvedAt": NotRequired[datetime],
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
        "updatedOnBehalfOf": NotRequired[str],
        "updatedOnBehalfOfJobTitle": NotRequired[str],
    },
)

class ListOrganizationRecommendationsResponseTypeDef(TypedDict):
    organizationRecommendationSummaries: List[OrganizationRecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetOrganizationRecommendationResponseTypeDef(TypedDict):
    organizationRecommendation: OrganizationRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationsResponseTypeDef(TypedDict):
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetRecommendationResponseTypeDef(TypedDict):
    recommendation: RecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
