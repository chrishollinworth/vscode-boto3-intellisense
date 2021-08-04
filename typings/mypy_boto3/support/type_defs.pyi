"""
Type annotations for support service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs.html)

Usage::

    ```python
    from mypy_boto3_support.type_defs import AddAttachmentsToSetRequestRequestTypeDef

    data: AddAttachmentsToSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddAttachmentsToSetRequestRequestTypeDef",
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseRequestRequestTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "CreateCaseResponseTypeDef",
    "DescribeAttachmentRequestRequestTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "DescribeCasesRequestRequestTypeDef",
    "DescribeCasesResponseTypeDef",
    "DescribeCommunicationsRequestRequestTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeSeverityLevelsRequestRequestTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "ResolveCaseRequestRequestTypeDef",
    "ResolveCaseResponseTypeDef",
    "ResponseMetadataTypeDef",
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
)

_RequiredAddAttachmentsToSetRequestRequestTypeDef = TypedDict(
    "_RequiredAddAttachmentsToSetRequestRequestTypeDef",
    {
        "attachments": List["AttachmentTypeDef"],
    },
)
_OptionalAddAttachmentsToSetRequestRequestTypeDef = TypedDict(
    "_OptionalAddAttachmentsToSetRequestRequestTypeDef",
    {
        "attachmentSetId": str,
    },
    total=False,
)

class AddAttachmentsToSetRequestRequestTypeDef(
    _RequiredAddAttachmentsToSetRequestRequestTypeDef,
    _OptionalAddAttachmentsToSetRequestRequestTypeDef,
):
    pass

AddAttachmentsToSetResponseTypeDef = TypedDict(
    "AddAttachmentsToSetResponseTypeDef",
    {
        "attachmentSetId": str,
        "expiryTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddCommunicationToCaseRequestRequestTypeDef = TypedDict(
    "_RequiredAddCommunicationToCaseRequestRequestTypeDef",
    {
        "communicationBody": str,
    },
)
_OptionalAddCommunicationToCaseRequestRequestTypeDef = TypedDict(
    "_OptionalAddCommunicationToCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "ccEmailAddresses": List[str],
        "attachmentSetId": str,
    },
    total=False,
)

class AddCommunicationToCaseRequestRequestTypeDef(
    _RequiredAddCommunicationToCaseRequestRequestTypeDef,
    _OptionalAddCommunicationToCaseRequestRequestTypeDef,
):
    pass

AddCommunicationToCaseResponseTypeDef = TypedDict(
    "AddCommunicationToCaseResponseTypeDef",
    {
        "result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentDetailsTypeDef = TypedDict(
    "AttachmentDetailsTypeDef",
    {
        "attachmentId": str,
        "fileName": str,
    },
    total=False,
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "fileName": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
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

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

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

_RequiredCreateCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCaseRequestRequestTypeDef",
    {
        "subject": str,
        "communicationBody": str,
    },
)
_OptionalCreateCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCaseRequestRequestTypeDef",
    {
        "serviceCode": str,
        "severityCode": str,
        "categoryCode": str,
        "ccEmailAddresses": List[str],
        "language": str,
        "issueType": str,
        "attachmentSetId": str,
    },
    total=False,
)

class CreateCaseRequestRequestTypeDef(
    _RequiredCreateCaseRequestRequestTypeDef, _OptionalCreateCaseRequestRequestTypeDef
):
    pass

CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttachmentRequestRequestTypeDef = TypedDict(
    "DescribeAttachmentRequestRequestTypeDef",
    {
        "attachmentId": str,
    },
)

DescribeAttachmentResponseTypeDef = TypedDict(
    "DescribeAttachmentResponseTypeDef",
    {
        "attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCasesRequestRequestTypeDef = TypedDict(
    "DescribeCasesRequestRequestTypeDef",
    {
        "caseIdList": List[str],
        "displayId": str,
        "afterTime": str,
        "beforeTime": str,
        "includeResolvedCases": bool,
        "nextToken": str,
        "maxResults": int,
        "language": str,
        "includeCommunications": bool,
    },
    total=False,
)

DescribeCasesResponseTypeDef = TypedDict(
    "DescribeCasesResponseTypeDef",
    {
        "cases": List["CaseDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCommunicationsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCommunicationsRequestRequestTypeDef",
    {
        "caseId": str,
    },
)
_OptionalDescribeCommunicationsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCommunicationsRequestRequestTypeDef",
    {
        "beforeTime": str,
        "afterTime": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeCommunicationsRequestRequestTypeDef(
    _RequiredDescribeCommunicationsRequestRequestTypeDef,
    _OptionalDescribeCommunicationsRequestRequestTypeDef,
):
    pass

DescribeCommunicationsResponseTypeDef = TypedDict(
    "DescribeCommunicationsResponseTypeDef",
    {
        "communications": List["CommunicationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "serviceCodeList": List[str],
        "language": str,
    },
    total=False,
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSeverityLevelsRequestRequestTypeDef = TypedDict(
    "DescribeSeverityLevelsRequestRequestTypeDef",
    {
        "language": str,
    },
    total=False,
)

DescribeSeverityLevelsResponseTypeDef = TypedDict(
    "DescribeSeverityLevelsResponseTypeDef",
    {
        "severityLevels": List["SeverityLevelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    {
        "checkIds": List[str],
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {
        "statuses": List["TrustedAdvisorCheckRefreshStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTrustedAdvisorCheckResultRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    {
        "checkId": str,
    },
)
_OptionalDescribeTrustedAdvisorCheckResultRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    {
        "language": str,
    },
    total=False,
)

class DescribeTrustedAdvisorCheckResultRequestRequestTypeDef(
    _RequiredDescribeTrustedAdvisorCheckResultRequestRequestTypeDef,
    _OptionalDescribeTrustedAdvisorCheckResultRequestRequestTypeDef,
):
    pass

DescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    {
        "result": "TrustedAdvisorCheckResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    {
        "checkIds": List[str],
    },
)

DescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {
        "summaries": List["TrustedAdvisorCheckSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorChecksRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    {
        "language": str,
    },
)

DescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    {
        "checks": List["TrustedAdvisorCheckDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RecentCaseCommunicationsTypeDef = TypedDict(
    "RecentCaseCommunicationsTypeDef",
    {
        "communications": List["CommunicationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

RefreshTrustedAdvisorCheckRequestRequestTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    {
        "checkId": str,
    },
)

RefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    {
        "status": "TrustedAdvisorCheckRefreshStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCaseRequestRequestTypeDef = TypedDict(
    "ResolveCaseRequestRequestTypeDef",
    {
        "caseId": str,
    },
    total=False,
)

ResolveCaseResponseTypeDef = TypedDict(
    "ResolveCaseResponseTypeDef",
    {
        "initialCaseStatus": str,
        "finalCaseStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "code": str,
        "name": str,
        "categories": List["CategoryTypeDef"],
    },
    total=False,
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

TrustedAdvisorCategorySpecificSummaryTypeDef = TypedDict(
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    {
        "costOptimizing": "TrustedAdvisorCostOptimizingSummaryTypeDef",
    },
    total=False,
)

TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "category": str,
        "metadata": List[str],
    },
)

TrustedAdvisorCheckRefreshStatusTypeDef = TypedDict(
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    {
        "checkId": str,
        "status": str,
        "millisUntilNextRefreshable": int,
    },
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
    "_OptionalTrustedAdvisorCheckSummaryTypeDef",
    {
        "hasFlaggedResources": bool,
    },
    total=False,
)

class TrustedAdvisorCheckSummaryTypeDef(
    _RequiredTrustedAdvisorCheckSummaryTypeDef, _OptionalTrustedAdvisorCheckSummaryTypeDef
):
    pass

TrustedAdvisorCostOptimizingSummaryTypeDef = TypedDict(
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)

_RequiredTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_RequiredTrustedAdvisorResourceDetailTypeDef",
    {
        "status": str,
        "resourceId": str,
        "metadata": List[str],
    },
)
_OptionalTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_OptionalTrustedAdvisorResourceDetailTypeDef",
    {
        "region": str,
        "isSuppressed": bool,
    },
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
