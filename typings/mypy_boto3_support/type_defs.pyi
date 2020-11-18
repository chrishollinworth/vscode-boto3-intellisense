"""
Main interface for support service type definitions.

Usage::

    ```python
    from mypy_boto3_support.type_defs import AttachmentDetailsTypeDef

    data: AttachmentDetailsTypeDef = {...}
    ```
"""
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentDetailsTypeDef",
    "AttachmentTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "ServiceTypeDef",
    "SeverityLevelTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "CreateCaseResponseTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "DescribeCasesResponseTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "ResolveCaseResponseTypeDef",
)

AttachmentDetailsTypeDef = TypedDict(
    "AttachmentDetailsTypeDef", {"attachmentId": str, "fileName": str}, total=False
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef", {"fileName": str, "data": Union[bytes, IO[bytes]]}, total=False
)

CaseDetailsTypeDef = TypedDict(
    "CaseDetailsTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": "RecentCaseCommunicationsTypeDef",
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)

CategoryTypeDef = TypedDict("CategoryTypeDef", {"code": str, "name": str}, total=False)

CommunicationTypeDef = TypedDict(
    "CommunicationTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List["AttachmentDetailsTypeDef"],
    },
    total=False,
)

RecentCaseCommunicationsTypeDef = TypedDict(
    "RecentCaseCommunicationsTypeDef",
    {"communications": List["CommunicationTypeDef"], "nextToken": str},
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef", {"code": str, "name": str, "categories": List["CategoryTypeDef"]}, total=False
)

SeverityLevelTypeDef = TypedDict("SeverityLevelTypeDef", {"code": str, "name": str}, total=False)

TrustedAdvisorCategorySpecificSummaryTypeDef = TypedDict(
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    {"costOptimizing": "TrustedAdvisorCostOptimizingSummaryTypeDef"},
    total=False,
)

TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {"id": str, "name": str, "description": str, "category": str, "metadata": List[str]},
)

TrustedAdvisorCheckRefreshStatusTypeDef = TypedDict(
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
)

TrustedAdvisorCheckResultTypeDef = TypedDict(
    "TrustedAdvisorCheckResultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
        "flaggedResources": List["TrustedAdvisorResourceDetailTypeDef"],
    },
)

_RequiredTrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "_RequiredTrustedAdvisorCheckSummaryTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
    },
)
_OptionalTrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "_OptionalTrustedAdvisorCheckSummaryTypeDef", {"hasFlaggedResources": bool}, total=False
)


class TrustedAdvisorCheckSummaryTypeDef(
    _RequiredTrustedAdvisorCheckSummaryTypeDef, _OptionalTrustedAdvisorCheckSummaryTypeDef
):
    pass


TrustedAdvisorCostOptimizingSummaryTypeDef = TypedDict(
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
)

_RequiredTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_RequiredTrustedAdvisorResourceDetailTypeDef",
    {"status": str, "resourceId": str, "metadata": List[str]},
)
_OptionalTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_OptionalTrustedAdvisorResourceDetailTypeDef",
    {"region": str, "isSuppressed": bool},
    total=False,
)


class TrustedAdvisorResourceDetailTypeDef(
    _RequiredTrustedAdvisorResourceDetailTypeDef, _OptionalTrustedAdvisorResourceDetailTypeDef
):
    pass


TrustedAdvisorResourcesSummaryTypeDef = TypedDict(
    "TrustedAdvisorResourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
)

AddAttachmentsToSetResponseTypeDef = TypedDict(
    "AddAttachmentsToSetResponseTypeDef", {"attachmentSetId": str, "expiryTime": str}, total=False
)

AddCommunicationToCaseResponseTypeDef = TypedDict(
    "AddCommunicationToCaseResponseTypeDef", {"result": bool}, total=False
)

CreateCaseResponseTypeDef = TypedDict("CreateCaseResponseTypeDef", {"caseId": str}, total=False)

DescribeAttachmentResponseTypeDef = TypedDict(
    "DescribeAttachmentResponseTypeDef", {"attachment": "AttachmentTypeDef"}, total=False
)

DescribeCasesResponseTypeDef = TypedDict(
    "DescribeCasesResponseTypeDef",
    {"cases": List["CaseDetailsTypeDef"], "nextToken": str},
    total=False,
)

DescribeCommunicationsResponseTypeDef = TypedDict(
    "DescribeCommunicationsResponseTypeDef",
    {"communications": List["CommunicationTypeDef"], "nextToken": str},
    total=False,
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef", {"services": List["ServiceTypeDef"]}, total=False
)

DescribeSeverityLevelsResponseTypeDef = TypedDict(
    "DescribeSeverityLevelsResponseTypeDef",
    {"severityLevels": List["SeverityLevelTypeDef"]},
    total=False,
)

DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {"statuses": List["TrustedAdvisorCheckRefreshStatusTypeDef"]},
)

DescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    {"result": "TrustedAdvisorCheckResultTypeDef"},
    total=False,
)

DescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {"summaries": List["TrustedAdvisorCheckSummaryTypeDef"]},
)

DescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    {"checks": List["TrustedAdvisorCheckDescriptionTypeDef"]},
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    {"status": "TrustedAdvisorCheckRefreshStatusTypeDef"},
)

ResolveCaseResponseTypeDef = TypedDict(
    "ResolveCaseResponseTypeDef", {"initialCaseStatus": str, "finalCaseStatus": str}, total=False
)
