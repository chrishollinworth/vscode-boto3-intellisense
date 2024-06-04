"""
Type annotations for trustedadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_trustedadvisor.type_defs import AccountRecommendationLifecycleSummaryTypeDef

    data: AccountRecommendationLifecycleSummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountRecommendationLifecycleSummaryTypeDef",
    "BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef",
    "BatchUpdateRecommendationResourceExclusionResponseTypeDef",
    "CheckSummaryTypeDef",
    "GetOrganizationRecommendationRequestRequestTypeDef",
    "GetOrganizationRecommendationResponseTypeDef",
    "GetRecommendationRequestRequestTypeDef",
    "GetRecommendationResponseTypeDef",
    "ListChecksRequestRequestTypeDef",
    "ListChecksResponseTypeDef",
    "ListOrganizationRecommendationAccountsRequestRequestTypeDef",
    "ListOrganizationRecommendationAccountsResponseTypeDef",
    "ListOrganizationRecommendationResourcesRequestRequestTypeDef",
    "ListOrganizationRecommendationResourcesResponseTypeDef",
    "ListOrganizationRecommendationsRequestRequestTypeDef",
    "ListOrganizationRecommendationsResponseTypeDef",
    "ListRecommendationResourcesRequestRequestTypeDef",
    "ListRecommendationResourcesResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
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
    "UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef",
    "UpdateRecommendationLifecycleRequestRequestTypeDef",
    "UpdateRecommendationResourceExclusionErrorTypeDef",
)

AccountRecommendationLifecycleSummaryTypeDef = TypedDict(
    "AccountRecommendationLifecycleSummaryTypeDef",
    {
        "accountId": str,
        "accountRecommendationArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleStage": RecommendationLifecycleStageType,
        "updateReason": str,
        "updateReasonCode": UpdateRecommendationLifecycleStageReasonCodeType,
        "updatedOnBehalfOf": str,
        "updatedOnBehalfOfJobTitle": str,
    },
    total=False,
)

BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef = TypedDict(
    "BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef",
    {
        "recommendationResourceExclusions": List["RecommendationResourceExclusionTypeDef"],
    },
)

BatchUpdateRecommendationResourceExclusionResponseTypeDef = TypedDict(
    "BatchUpdateRecommendationResourceExclusionResponseTypeDef",
    {
        "batchUpdateRecommendationResourceExclusionErrors": List[
            "UpdateRecommendationResourceExclusionErrorTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

GetOrganizationRecommendationRequestRequestTypeDef = TypedDict(
    "GetOrganizationRecommendationRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
    },
)

GetOrganizationRecommendationResponseTypeDef = TypedDict(
    "GetOrganizationRecommendationResponseTypeDef",
    {
        "organizationRecommendation": "OrganizationRecommendationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationRequestRequestTypeDef = TypedDict(
    "GetRecommendationRequestRequestTypeDef",
    {
        "recommendationIdentifier": str,
    },
)

GetRecommendationResponseTypeDef = TypedDict(
    "GetRecommendationResponseTypeDef",
    {
        "recommendation": "RecommendationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChecksRequestRequestTypeDef = TypedDict(
    "ListChecksRequestRequestTypeDef",
    {
        "awsService": str,
        "language": RecommendationLanguageType,
        "maxResults": int,
        "nextToken": str,
        "pillar": RecommendationPillarType,
        "source": RecommendationSourceType,
    },
    total=False,
)

ListChecksResponseTypeDef = TypedDict(
    "ListChecksResponseTypeDef",
    {
        "checkSummaries": List["CheckSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrganizationRecommendationAccountsRequestRequestTypeDef = TypedDict(
    "_RequiredListOrganizationRecommendationAccountsRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
    },
)
_OptionalListOrganizationRecommendationAccountsRequestRequestTypeDef = TypedDict(
    "_OptionalListOrganizationRecommendationAccountsRequestRequestTypeDef",
    {
        "affectedAccountId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListOrganizationRecommendationAccountsRequestRequestTypeDef(
    _RequiredListOrganizationRecommendationAccountsRequestRequestTypeDef,
    _OptionalListOrganizationRecommendationAccountsRequestRequestTypeDef,
):
    pass

ListOrganizationRecommendationAccountsResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationAccountsResponseTypeDef",
    {
        "accountRecommendationLifecycleSummaries": List[
            "AccountRecommendationLifecycleSummaryTypeDef"
        ],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrganizationRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListOrganizationRecommendationResourcesRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
    },
)
_OptionalListOrganizationRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListOrganizationRecommendationResourcesRequestRequestTypeDef",
    {
        "affectedAccountId": str,
        "exclusionStatus": ExclusionStatusType,
        "maxResults": int,
        "nextToken": str,
        "regionCode": str,
        "status": ResourceStatusType,
    },
    total=False,
)

class ListOrganizationRecommendationResourcesRequestRequestTypeDef(
    _RequiredListOrganizationRecommendationResourcesRequestRequestTypeDef,
    _OptionalListOrganizationRecommendationResourcesRequestRequestTypeDef,
):
    pass

ListOrganizationRecommendationResourcesResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationResourcesResponseTypeDef",
    {
        "nextToken": str,
        "organizationRecommendationResourceSummaries": List[
            "OrganizationRecommendationResourceSummaryTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationRecommendationsRequestRequestTypeDef = TypedDict(
    "ListOrganizationRecommendationsRequestRequestTypeDef",
    {
        "afterLastUpdatedAt": Union[datetime, str],
        "awsService": str,
        "beforeLastUpdatedAt": Union[datetime, str],
        "checkIdentifier": str,
        "maxResults": int,
        "nextToken": str,
        "pillar": RecommendationPillarType,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
    total=False,
)

ListOrganizationRecommendationsResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "organizationRecommendationSummaries": List["OrganizationRecommendationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendationResourcesRequestRequestTypeDef",
    {
        "recommendationIdentifier": str,
    },
)
_OptionalListRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendationResourcesRequestRequestTypeDef",
    {
        "exclusionStatus": ExclusionStatusType,
        "maxResults": int,
        "nextToken": str,
        "regionCode": str,
        "status": ResourceStatusType,
    },
    total=False,
)

class ListRecommendationResourcesRequestRequestTypeDef(
    _RequiredListRecommendationResourcesRequestRequestTypeDef,
    _OptionalListRecommendationResourcesRequestRequestTypeDef,
):
    pass

ListRecommendationResourcesResponseTypeDef = TypedDict(
    "ListRecommendationResourcesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationResourceSummaries": List["RecommendationResourceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "afterLastUpdatedAt": Union[datetime, str],
        "awsService": str,
        "beforeLastUpdatedAt": Union[datetime, str],
        "checkIdentifier": str,
        "maxResults": int,
        "nextToken": str,
        "pillar": RecommendationPillarType,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List["RecommendationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOrganizationRecommendationResourceSummaryTypeDef = TypedDict(
    "_RequiredOrganizationRecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
    },
)
_OptionalOrganizationRecommendationResourceSummaryTypeDef = TypedDict(
    "_OptionalOrganizationRecommendationResourceSummaryTypeDef",
    {
        "accountId": str,
        "exclusionStatus": ExclusionStatusType,
    },
    total=False,
)

class OrganizationRecommendationResourceSummaryTypeDef(
    _RequiredOrganizationRecommendationResourceSummaryTypeDef,
    _OptionalOrganizationRecommendationResourceSummaryTypeDef,
):
    pass

_RequiredOrganizationRecommendationSummaryTypeDef = TypedDict(
    "_RequiredOrganizationRecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": "RecommendationResourcesAggregatesTypeDef",
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
)
_OptionalOrganizationRecommendationSummaryTypeDef = TypedDict(
    "_OptionalOrganizationRecommendationSummaryTypeDef",
    {
        "awsServices": List[str],
        "checkArn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "lifecycleStage": RecommendationLifecycleStageType,
        "pillarSpecificAggregates": "RecommendationPillarSpecificAggregatesTypeDef",
    },
    total=False,
)

class OrganizationRecommendationSummaryTypeDef(
    _RequiredOrganizationRecommendationSummaryTypeDef,
    _OptionalOrganizationRecommendationSummaryTypeDef,
):
    pass

_RequiredOrganizationRecommendationTypeDef = TypedDict(
    "_RequiredOrganizationRecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": "RecommendationResourcesAggregatesTypeDef",
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
)
_OptionalOrganizationRecommendationTypeDef = TypedDict(
    "_OptionalOrganizationRecommendationTypeDef",
    {
        "awsServices": List[str],
        "checkArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "lastUpdatedAt": datetime,
        "lifecycleStage": RecommendationLifecycleStageType,
        "pillarSpecificAggregates": "RecommendationPillarSpecificAggregatesTypeDef",
        "resolvedAt": datetime,
        "updateReason": str,
        "updateReasonCode": UpdateRecommendationLifecycleStageReasonCodeType,
        "updatedOnBehalfOf": str,
        "updatedOnBehalfOfJobTitle": str,
    },
    total=False,
)

class OrganizationRecommendationTypeDef(
    _RequiredOrganizationRecommendationTypeDef, _OptionalOrganizationRecommendationTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RecommendationCostOptimizingAggregatesTypeDef = TypedDict(
    "RecommendationCostOptimizingAggregatesTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)

RecommendationPillarSpecificAggregatesTypeDef = TypedDict(
    "RecommendationPillarSpecificAggregatesTypeDef",
    {
        "costOptimizing": "RecommendationCostOptimizingAggregatesTypeDef",
    },
    total=False,
)

RecommendationResourceExclusionTypeDef = TypedDict(
    "RecommendationResourceExclusionTypeDef",
    {
        "arn": str,
        "isExcluded": bool,
    },
)

_RequiredRecommendationResourceSummaryTypeDef = TypedDict(
    "_RequiredRecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
    },
)
_OptionalRecommendationResourceSummaryTypeDef = TypedDict(
    "_OptionalRecommendationResourceSummaryTypeDef",
    {
        "exclusionStatus": ExclusionStatusType,
    },
    total=False,
)

class RecommendationResourceSummaryTypeDef(
    _RequiredRecommendationResourceSummaryTypeDef, _OptionalRecommendationResourceSummaryTypeDef
):
    pass

RecommendationResourcesAggregatesTypeDef = TypedDict(
    "RecommendationResourcesAggregatesTypeDef",
    {
        "errorCount": int,
        "okCount": int,
        "warningCount": int,
    },
)

_RequiredRecommendationSummaryTypeDef = TypedDict(
    "_RequiredRecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": "RecommendationResourcesAggregatesTypeDef",
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
)
_OptionalRecommendationSummaryTypeDef = TypedDict(
    "_OptionalRecommendationSummaryTypeDef",
    {
        "awsServices": List[str],
        "checkArn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "lifecycleStage": RecommendationLifecycleStageType,
        "pillarSpecificAggregates": "RecommendationPillarSpecificAggregatesTypeDef",
    },
    total=False,
)

class RecommendationSummaryTypeDef(
    _RequiredRecommendationSummaryTypeDef, _OptionalRecommendationSummaryTypeDef
):
    pass

_RequiredRecommendationTypeDef = TypedDict(
    "_RequiredRecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": "RecommendationResourcesAggregatesTypeDef",
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
    },
)
_OptionalRecommendationTypeDef = TypedDict(
    "_OptionalRecommendationTypeDef",
    {
        "awsServices": List[str],
        "checkArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "lastUpdatedAt": datetime,
        "lifecycleStage": RecommendationLifecycleStageType,
        "pillarSpecificAggregates": "RecommendationPillarSpecificAggregatesTypeDef",
        "resolvedAt": datetime,
        "updateReason": str,
        "updateReasonCode": UpdateRecommendationLifecycleStageReasonCodeType,
        "updatedOnBehalfOf": str,
        "updatedOnBehalfOfJobTitle": str,
    },
    total=False,
)

class RecommendationTypeDef(_RequiredRecommendationTypeDef, _OptionalRecommendationTypeDef):
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

_RequiredUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef",
    {
        "lifecycleStage": UpdateRecommendationLifecycleStageType,
        "organizationRecommendationIdentifier": str,
    },
)
_OptionalUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef",
    {
        "updateReason": str,
        "updateReasonCode": UpdateRecommendationLifecycleStageReasonCodeType,
    },
    total=False,
)

class UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef(
    _RequiredUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef,
    _OptionalUpdateOrganizationRecommendationLifecycleRequestRequestTypeDef,
):
    pass

_RequiredUpdateRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecommendationLifecycleRequestRequestTypeDef",
    {
        "lifecycleStage": UpdateRecommendationLifecycleStageType,
        "recommendationIdentifier": str,
    },
)
_OptionalUpdateRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecommendationLifecycleRequestRequestTypeDef",
    {
        "updateReason": str,
        "updateReasonCode": UpdateRecommendationLifecycleStageReasonCodeType,
    },
    total=False,
)

class UpdateRecommendationLifecycleRequestRequestTypeDef(
    _RequiredUpdateRecommendationLifecycleRequestRequestTypeDef,
    _OptionalUpdateRecommendationLifecycleRequestRequestTypeDef,
):
    pass

UpdateRecommendationResourceExclusionErrorTypeDef = TypedDict(
    "UpdateRecommendationResourceExclusionErrorTypeDef",
    {
        "arn": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)
