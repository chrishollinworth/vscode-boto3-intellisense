"""
Type annotations for support service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_support.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

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
    "AddAttachmentsToSetRequestTypeDef",
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseRequestTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentOutputTypeDef",
    "AttachmentTypeDef",
    "AttachmentUnionTypeDef",
    "BlobTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "CommunicationTypeOptionsTypeDef",
    "CreateCaseRequestTypeDef",
    "CreateCaseResponseTypeDef",
    "DateIntervalTypeDef",
    "DescribeAttachmentRequestTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "DescribeCasesRequestPaginateTypeDef",
    "DescribeCasesRequestTypeDef",
    "DescribeCasesResponseTypeDef",
    "DescribeCommunicationsRequestPaginateTypeDef",
    "DescribeCommunicationsRequestTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "DescribeCreateCaseOptionsRequestTypeDef",
    "DescribeCreateCaseOptionsResponseTypeDef",
    "DescribeServicesRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeSeverityLevelsRequestTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeSupportedLanguagesRequestTypeDef",
    "DescribeSupportedLanguagesResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultRequestTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesRequestTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeTrustedAdvisorChecksRequestTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "RefreshTrustedAdvisorCheckRequestTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "ResolveCaseRequestTypeDef",
    "ResolveCaseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceTypeDef",
    "SeverityLevelTypeDef",
    "SupportedHourTypeDef",
    "SupportedLanguageTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AddCommunicationToCaseRequestTypeDef(TypedDict):
    communicationBody: str
    caseId: NotRequired[str]
    ccEmailAddresses: NotRequired[Sequence[str]]
    attachmentSetId: NotRequired[str]

class AttachmentDetailsTypeDef(TypedDict):
    attachmentId: NotRequired[str]
    fileName: NotRequired[str]

class AttachmentOutputTypeDef(TypedDict):
    fileName: NotRequired[str]
    data: NotRequired[bytes]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CategoryTypeDef(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]

class DateIntervalTypeDef(TypedDict):
    startDateTime: NotRequired[str]
    endDateTime: NotRequired[str]

class SupportedHourTypeDef(TypedDict):
    startTime: NotRequired[str]
    endTime: NotRequired[str]

class CreateCaseRequestTypeDef(TypedDict):
    subject: str
    communicationBody: str
    serviceCode: NotRequired[str]
    severityCode: NotRequired[str]
    categoryCode: NotRequired[str]
    ccEmailAddresses: NotRequired[Sequence[str]]
    language: NotRequired[str]
    issueType: NotRequired[str]
    attachmentSetId: NotRequired[str]

class DescribeAttachmentRequestTypeDef(TypedDict):
    attachmentId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeCasesRequestTypeDef(TypedDict):
    caseIdList: NotRequired[Sequence[str]]
    displayId: NotRequired[str]
    afterTime: NotRequired[str]
    beforeTime: NotRequired[str]
    includeResolvedCases: NotRequired[bool]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    language: NotRequired[str]
    includeCommunications: NotRequired[bool]

class DescribeCommunicationsRequestTypeDef(TypedDict):
    caseId: str
    beforeTime: NotRequired[str]
    afterTime: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeCreateCaseOptionsRequestTypeDef(TypedDict):
    issueType: str
    serviceCode: str
    language: str
    categoryCode: str

class DescribeServicesRequestTypeDef(TypedDict):
    serviceCodeList: NotRequired[Sequence[str]]
    language: NotRequired[str]

class DescribeSeverityLevelsRequestTypeDef(TypedDict):
    language: NotRequired[str]

class SeverityLevelTypeDef(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]

class DescribeSupportedLanguagesRequestTypeDef(TypedDict):
    issueType: str
    serviceCode: str
    categoryCode: str

class SupportedLanguageTypeDef(TypedDict):
    code: NotRequired[str]
    language: NotRequired[str]
    display: NotRequired[str]

class DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef(TypedDict):
    checkIds: Sequence[str]

class TrustedAdvisorCheckRefreshStatusTypeDef(TypedDict):
    checkId: str
    status: str
    millisUntilNextRefreshable: int

class DescribeTrustedAdvisorCheckResultRequestTypeDef(TypedDict):
    checkId: str
    language: NotRequired[str]

class DescribeTrustedAdvisorCheckSummariesRequestTypeDef(TypedDict):
    checkIds: Sequence[str]

class DescribeTrustedAdvisorChecksRequestTypeDef(TypedDict):
    language: str

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

class RefreshTrustedAdvisorCheckRequestTypeDef(TypedDict):
    checkId: str

class ResolveCaseRequestTypeDef(TypedDict):
    caseId: NotRequired[str]

class TrustedAdvisorCostOptimizingSummaryTypeDef(TypedDict):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float

class TrustedAdvisorResourceDetailTypeDef(TypedDict):
    status: str
    resourceId: str
    metadata: List[str]
    region: NotRequired[str]
    isSuppressed: NotRequired[bool]

class TrustedAdvisorResourcesSummaryTypeDef(TypedDict):
    resourcesProcessed: int
    resourcesFlagged: int
    resourcesIgnored: int
    resourcesSuppressed: int

class AddAttachmentsToSetResponseTypeDef(TypedDict):
    attachmentSetId: str
    expiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddCommunicationToCaseResponseTypeDef(TypedDict):
    result: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseResponseTypeDef(TypedDict):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveCaseResponseTypeDef(TypedDict):
    initialCaseStatus: str
    finalCaseStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class CommunicationTypeDef(TypedDict):
    caseId: NotRequired[str]
    body: NotRequired[str]
    submittedBy: NotRequired[str]
    timeCreated: NotRequired[str]
    attachmentSet: NotRequired[List[AttachmentDetailsTypeDef]]

class DescribeAttachmentResponseTypeDef(TypedDict):
    attachment: AttachmentOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentTypeDef(TypedDict):
    fileName: NotRequired[str]
    data: NotRequired[BlobTypeDef]

class ServiceTypeDef(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]
    categories: NotRequired[List[CategoryTypeDef]]

CommunicationTypeOptionsTypeDef = TypedDict(
    "CommunicationTypeOptionsTypeDef",
    {
        "type": NotRequired[str],
        "supportedHours": NotRequired[List[SupportedHourTypeDef]],
        "datesWithoutSupport": NotRequired[List[DateIntervalTypeDef]],
    },
)

class DescribeCasesRequestPaginateTypeDef(TypedDict):
    caseIdList: NotRequired[Sequence[str]]
    displayId: NotRequired[str]
    afterTime: NotRequired[str]
    beforeTime: NotRequired[str]
    includeResolvedCases: NotRequired[bool]
    language: NotRequired[str]
    includeCommunications: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCommunicationsRequestPaginateTypeDef(TypedDict):
    caseId: str
    beforeTime: NotRequired[str]
    afterTime: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSeverityLevelsResponseTypeDef(TypedDict):
    severityLevels: List[SeverityLevelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSupportedLanguagesResponseTypeDef(TypedDict):
    supportedLanguages: List[SupportedLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(TypedDict):
    statuses: List[TrustedAdvisorCheckRefreshStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshTrustedAdvisorCheckResponseTypeDef(TypedDict):
    status: TrustedAdvisorCheckRefreshStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorChecksResponseTypeDef(TypedDict):
    checks: List[TrustedAdvisorCheckDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrustedAdvisorCategorySpecificSummaryTypeDef(TypedDict):
    costOptimizing: NotRequired[TrustedAdvisorCostOptimizingSummaryTypeDef]

class DescribeCommunicationsResponseTypeDef(TypedDict):
    communications: List[CommunicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RecentCaseCommunicationsTypeDef(TypedDict):
    communications: NotRequired[List[CommunicationTypeDef]]
    nextToken: NotRequired[str]

AttachmentUnionTypeDef = Union[AttachmentTypeDef, AttachmentOutputTypeDef]

class DescribeServicesResponseTypeDef(TypedDict):
    services: List[ServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCreateCaseOptionsResponseTypeDef(TypedDict):
    languageAvailability: str
    communicationTypes: List[CommunicationTypeOptionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrustedAdvisorCheckResultTypeDef(TypedDict):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    flaggedResources: List[TrustedAdvisorResourceDetailTypeDef]

class TrustedAdvisorCheckSummaryTypeDef(TypedDict):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    hasFlaggedResources: NotRequired[bool]

class CaseDetailsTypeDef(TypedDict):
    caseId: NotRequired[str]
    displayId: NotRequired[str]
    subject: NotRequired[str]
    status: NotRequired[str]
    serviceCode: NotRequired[str]
    categoryCode: NotRequired[str]
    severityCode: NotRequired[str]
    submittedBy: NotRequired[str]
    timeCreated: NotRequired[str]
    recentCommunications: NotRequired[RecentCaseCommunicationsTypeDef]
    ccEmailAddresses: NotRequired[List[str]]
    language: NotRequired[str]

class AddAttachmentsToSetRequestTypeDef(TypedDict):
    attachments: Sequence[AttachmentUnionTypeDef]
    attachmentSetId: NotRequired[str]

class DescribeTrustedAdvisorCheckResultResponseTypeDef(TypedDict):
    result: TrustedAdvisorCheckResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorCheckSummariesResponseTypeDef(TypedDict):
    summaries: List[TrustedAdvisorCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCasesResponseTypeDef(TypedDict):
    cases: List[CaseDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
