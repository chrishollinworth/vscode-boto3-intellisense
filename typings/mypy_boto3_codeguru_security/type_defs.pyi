"""
Type annotations for codeguru-security service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codeguru_security.type_defs import FindingMetricsValuePerSeverityTypeDef

    data: FindingMetricsValuePerSeverityTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AnalysisTypeType,
    ErrorCodeType,
    ScanStateType,
    ScanTypeType,
    SeverityType,
    StatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountFindingsMetricTypeDef",
    "BatchGetFindingsErrorTypeDef",
    "BatchGetFindingsRequestTypeDef",
    "BatchGetFindingsResponseTypeDef",
    "CategoryWithFindingNumTypeDef",
    "CodeLineTypeDef",
    "CreateScanRequestTypeDef",
    "CreateScanResponseTypeDef",
    "CreateUploadUrlRequestTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "EncryptionConfigTypeDef",
    "FilePathTypeDef",
    "FindingIdentifierTypeDef",
    "FindingMetricsValuePerSeverityTypeDef",
    "FindingTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetFindingsRequestPaginateTypeDef",
    "GetFindingsRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetMetricsSummaryRequestTypeDef",
    "GetMetricsSummaryResponseTypeDef",
    "GetScanRequestTypeDef",
    "GetScanResponseTypeDef",
    "ListFindingsMetricsRequestPaginateTypeDef",
    "ListFindingsMetricsRequestTypeDef",
    "ListFindingsMetricsResponseTypeDef",
    "ListScansRequestPaginateTypeDef",
    "ListScansRequestTypeDef",
    "ListScansResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RecommendationTypeDef",
    "RemediationTypeDef",
    "ResourceIdTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanNameWithFindingNumTypeDef",
    "ScanSummaryTypeDef",
    "SuggestedFixTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountConfigurationRequestTypeDef",
    "UpdateAccountConfigurationResponseTypeDef",
    "VulnerabilityTypeDef",
)

class FindingMetricsValuePerSeverityTypeDef(TypedDict):
    critical: NotRequired[float]
    high: NotRequired[float]
    info: NotRequired[float]
    low: NotRequired[float]
    medium: NotRequired[float]

class BatchGetFindingsErrorTypeDef(TypedDict):
    errorCode: ErrorCodeType
    findingId: str
    message: str
    scanName: str

class FindingIdentifierTypeDef(TypedDict):
    findingId: str
    scanName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CategoryWithFindingNumTypeDef(TypedDict):
    categoryName: NotRequired[str]
    findingNumber: NotRequired[int]

class CodeLineTypeDef(TypedDict):
    content: NotRequired[str]
    number: NotRequired[int]

class ResourceIdTypeDef(TypedDict):
    codeArtifactId: NotRequired[str]

class CreateUploadUrlRequestTypeDef(TypedDict):
    scanName: str

class EncryptionConfigTypeDef(TypedDict):
    kmsKeyArn: NotRequired[str]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "subResourceId": NotRequired[str],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetFindingsRequestTypeDef(TypedDict):
    scanName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[StatusType]

TimestampTypeDef = Union[datetime, str]

class GetScanRequestTypeDef(TypedDict):
    scanName: str
    runId: NotRequired[str]

class ListScansRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ScanSummaryTypeDef(TypedDict):
    createdAt: datetime
    runId: str
    scanName: str
    scanState: ScanStateType
    scanNameArn: NotRequired[str]
    updatedAt: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ScanNameWithFindingNumTypeDef(TypedDict):
    findingNumber: NotRequired[int]
    scanName: NotRequired[str]

class RecommendationTypeDef(TypedDict):
    text: NotRequired[str]
    url: NotRequired[str]

class SuggestedFixTypeDef(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class AccountFindingsMetricTypeDef(TypedDict):
    closedFindings: NotRequired[FindingMetricsValuePerSeverityTypeDef]
    date: NotRequired[datetime]
    meanTimeToClose: NotRequired[FindingMetricsValuePerSeverityTypeDef]
    newFindings: NotRequired[FindingMetricsValuePerSeverityTypeDef]
    openFindings: NotRequired[FindingMetricsValuePerSeverityTypeDef]

class BatchGetFindingsRequestTypeDef(TypedDict):
    findingIdentifiers: Sequence[FindingIdentifierTypeDef]

class CreateUploadUrlResponseTypeDef(TypedDict):
    codeArtifactId: str
    requestHeaders: Dict[str, str]
    s3Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetScanResponseTypeDef(TypedDict):
    analysisType: AnalysisTypeType
    createdAt: datetime
    errorMessage: str
    numberOfRevisions: int
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class FilePathTypeDef(TypedDict):
    codeSnippet: NotRequired[List[CodeLineTypeDef]]
    endLine: NotRequired[int]
    name: NotRequired[str]
    path: NotRequired[str]
    startLine: NotRequired[int]

class CreateScanRequestTypeDef(TypedDict):
    resourceId: ResourceIdTypeDef
    scanName: str
    analysisType: NotRequired[AnalysisTypeType]
    clientToken: NotRequired[str]
    scanType: NotRequired[ScanTypeType]
    tags: NotRequired[Mapping[str, str]]

class CreateScanResponseTypeDef(TypedDict):
    resourceId: ResourceIdTypeDef
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountConfigurationResponseTypeDef(TypedDict):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountConfigurationRequestTypeDef(TypedDict):
    encryptionConfig: EncryptionConfigTypeDef

class UpdateAccountConfigurationResponseTypeDef(TypedDict):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsRequestPaginateTypeDef(TypedDict):
    scanName: str
    status: NotRequired[StatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListScansRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetMetricsSummaryRequestTypeDef(TypedDict):
    date: TimestampTypeDef

class ListFindingsMetricsRequestPaginateTypeDef(TypedDict):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingsMetricsRequestTypeDef(TypedDict):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListScansResponseTypeDef(TypedDict):
    summaries: List[ScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MetricsSummaryTypeDef(TypedDict):
    categoriesWithMostFindings: NotRequired[List[CategoryWithFindingNumTypeDef]]
    date: NotRequired[datetime]
    openFindings: NotRequired[FindingMetricsValuePerSeverityTypeDef]
    scansWithMostOpenCriticalFindings: NotRequired[List[ScanNameWithFindingNumTypeDef]]
    scansWithMostOpenFindings: NotRequired[List[ScanNameWithFindingNumTypeDef]]

class RemediationTypeDef(TypedDict):
    recommendation: NotRequired[RecommendationTypeDef]
    suggestedFixes: NotRequired[List[SuggestedFixTypeDef]]

class ListFindingsMetricsResponseTypeDef(TypedDict):
    findingsMetrics: List[AccountFindingsMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "filePath": NotRequired[FilePathTypeDef],
        "id": NotRequired[str],
        "itemCount": NotRequired[int],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
    },
)

class GetMetricsSummaryResponseTypeDef(TypedDict):
    metricsSummary: MetricsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "detectorId": NotRequired[str],
        "detectorName": NotRequired[str],
        "detectorTags": NotRequired[List[str]],
        "generatorId": NotRequired[str],
        "id": NotRequired[str],
        "remediation": NotRequired[RemediationTypeDef],
        "resource": NotRequired[ResourceTypeDef],
        "ruleId": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "status": NotRequired[StatusType],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "vulnerability": NotRequired[VulnerabilityTypeDef],
    },
)

class BatchGetFindingsResponseTypeDef(TypedDict):
    failedFindings: List[BatchGetFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsResponseTypeDef(TypedDict):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
