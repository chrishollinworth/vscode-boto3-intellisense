"""
Type annotations for codeguru-security service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguru_security.type_defs import AccountFindingsMetricTypeDef

    data: AccountFindingsMetricTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnalysisTypeType,
    ErrorCodeType,
    ScanStateType,
    ScanTypeType,
    SeverityType,
    StatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountFindingsMetricTypeDef",
    "BatchGetFindingsErrorTypeDef",
    "BatchGetFindingsRequestRequestTypeDef",
    "BatchGetFindingsResponseTypeDef",
    "CategoryWithFindingNumTypeDef",
    "CodeLineTypeDef",
    "CreateScanRequestRequestTypeDef",
    "CreateScanResponseTypeDef",
    "CreateUploadUrlRequestRequestTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "EncryptionConfigTypeDef",
    "FilePathTypeDef",
    "FindingIdentifierTypeDef",
    "FindingMetricsValuePerSeverityTypeDef",
    "FindingTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetMetricsSummaryRequestRequestTypeDef",
    "GetMetricsSummaryResponseTypeDef",
    "GetScanRequestRequestTypeDef",
    "GetScanResponseTypeDef",
    "ListFindingsMetricsRequestRequestTypeDef",
    "ListFindingsMetricsResponseTypeDef",
    "ListScansRequestRequestTypeDef",
    "ListScansResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountConfigurationRequestRequestTypeDef",
    "UpdateAccountConfigurationResponseTypeDef",
    "VulnerabilityTypeDef",
)

AccountFindingsMetricTypeDef = TypedDict(
    "AccountFindingsMetricTypeDef",
    {
        "closedFindings": "FindingMetricsValuePerSeverityTypeDef",
        "date": datetime,
        "meanTimeToClose": "FindingMetricsValuePerSeverityTypeDef",
        "newFindings": "FindingMetricsValuePerSeverityTypeDef",
        "openFindings": "FindingMetricsValuePerSeverityTypeDef",
    },
    total=False,
)

BatchGetFindingsErrorTypeDef = TypedDict(
    "BatchGetFindingsErrorTypeDef",
    {
        "errorCode": ErrorCodeType,
        "findingId": str,
        "message": str,
        "scanName": str,
    },
)

BatchGetFindingsRequestRequestTypeDef = TypedDict(
    "BatchGetFindingsRequestRequestTypeDef",
    {
        "findingIdentifiers": List["FindingIdentifierTypeDef"],
    },
)

BatchGetFindingsResponseTypeDef = TypedDict(
    "BatchGetFindingsResponseTypeDef",
    {
        "failedFindings": List["BatchGetFindingsErrorTypeDef"],
        "findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CategoryWithFindingNumTypeDef = TypedDict(
    "CategoryWithFindingNumTypeDef",
    {
        "categoryName": str,
        "findingNumber": int,
    },
    total=False,
)

CodeLineTypeDef = TypedDict(
    "CodeLineTypeDef",
    {
        "content": str,
        "number": int,
    },
    total=False,
)

_RequiredCreateScanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScanRequestRequestTypeDef",
    {
        "resourceId": "ResourceIdTypeDef",
        "scanName": str,
    },
)
_OptionalCreateScanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScanRequestRequestTypeDef",
    {
        "analysisType": AnalysisTypeType,
        "clientToken": str,
        "scanType": ScanTypeType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateScanRequestRequestTypeDef(
    _RequiredCreateScanRequestRequestTypeDef, _OptionalCreateScanRequestRequestTypeDef
):
    pass

CreateScanResponseTypeDef = TypedDict(
    "CreateScanResponseTypeDef",
    {
        "resourceId": "ResourceIdTypeDef",
        "runId": str,
        "scanName": str,
        "scanNameArn": str,
        "scanState": ScanStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUploadUrlRequestRequestTypeDef = TypedDict(
    "CreateUploadUrlRequestRequestTypeDef",
    {
        "scanName": str,
    },
)

CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "codeArtifactId": str,
        "requestHeaders": Dict[str, str],
        "s3Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

FilePathTypeDef = TypedDict(
    "FilePathTypeDef",
    {
        "codeSnippet": List["CodeLineTypeDef"],
        "endLine": int,
        "name": str,
        "path": str,
        "startLine": int,
    },
    total=False,
)

FindingIdentifierTypeDef = TypedDict(
    "FindingIdentifierTypeDef",
    {
        "findingId": str,
        "scanName": str,
    },
)

FindingMetricsValuePerSeverityTypeDef = TypedDict(
    "FindingMetricsValuePerSeverityTypeDef",
    {
        "critical": float,
        "high": float,
        "info": float,
        "low": float,
        "medium": float,
    },
    total=False,
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "detectorId": str,
        "detectorName": str,
        "detectorTags": List[str],
        "generatorId": str,
        "id": str,
        "remediation": "RemediationTypeDef",
        "resource": "ResourceTypeDef",
        "ruleId": str,
        "severity": SeverityType,
        "status": StatusType,
        "title": str,
        "type": str,
        "updatedAt": datetime,
        "vulnerability": "VulnerabilityTypeDef",
    },
    total=False,
)

GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {
        "encryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestRequestTypeDef",
    {
        "scanName": str,
    },
)
_OptionalGetFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": StatusType,
    },
    total=False,
)

class GetFindingsRequestRequestTypeDef(
    _RequiredGetFindingsRequestRequestTypeDef, _OptionalGetFindingsRequestRequestTypeDef
):
    pass

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricsSummaryRequestRequestTypeDef = TypedDict(
    "GetMetricsSummaryRequestRequestTypeDef",
    {
        "date": Union[datetime, str],
    },
)

GetMetricsSummaryResponseTypeDef = TypedDict(
    "GetMetricsSummaryResponseTypeDef",
    {
        "metricsSummary": "MetricsSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetScanRequestRequestTypeDef = TypedDict(
    "_RequiredGetScanRequestRequestTypeDef",
    {
        "scanName": str,
    },
)
_OptionalGetScanRequestRequestTypeDef = TypedDict(
    "_OptionalGetScanRequestRequestTypeDef",
    {
        "runId": str,
    },
    total=False,
)

class GetScanRequestRequestTypeDef(
    _RequiredGetScanRequestRequestTypeDef, _OptionalGetScanRequestRequestTypeDef
):
    pass

GetScanResponseTypeDef = TypedDict(
    "GetScanResponseTypeDef",
    {
        "analysisType": AnalysisTypeType,
        "createdAt": datetime,
        "numberOfRevisions": int,
        "runId": str,
        "scanName": str,
        "scanNameArn": str,
        "scanState": ScanStateType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingsMetricsRequestRequestTypeDef",
    {
        "endDate": Union[datetime, str],
        "startDate": Union[datetime, str],
    },
)
_OptionalListFindingsMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingsMetricsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFindingsMetricsRequestRequestTypeDef(
    _RequiredListFindingsMetricsRequestRequestTypeDef,
    _OptionalListFindingsMetricsRequestRequestTypeDef,
):
    pass

ListFindingsMetricsResponseTypeDef = TypedDict(
    "ListFindingsMetricsResponseTypeDef",
    {
        "findingsMetrics": List["AccountFindingsMetricTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScansRequestRequestTypeDef = TypedDict(
    "ListScansRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListScansResponseTypeDef = TypedDict(
    "ListScansResponseTypeDef",
    {
        "nextToken": str,
        "summaries": List["ScanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "categoriesWithMostFindings": List["CategoryWithFindingNumTypeDef"],
        "date": datetime,
        "openFindings": "FindingMetricsValuePerSeverityTypeDef",
        "scansWithMostOpenCriticalFindings": List["ScanNameWithFindingNumTypeDef"],
        "scansWithMostOpenFindings": List["ScanNameWithFindingNumTypeDef"],
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

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "text": str,
        "url": str,
    },
    total=False,
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": "RecommendationTypeDef",
        "suggestedFixes": List["SuggestedFixTypeDef"],
    },
    total=False,
)

ResourceIdTypeDef = TypedDict(
    "ResourceIdTypeDef",
    {
        "codeArtifactId": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "subResourceId": str,
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

ScanNameWithFindingNumTypeDef = TypedDict(
    "ScanNameWithFindingNumTypeDef",
    {
        "findingNumber": int,
        "scanName": str,
    },
    total=False,
)

_RequiredScanSummaryTypeDef = TypedDict(
    "_RequiredScanSummaryTypeDef",
    {
        "createdAt": datetime,
        "runId": str,
        "scanName": str,
        "scanState": ScanStateType,
    },
)
_OptionalScanSummaryTypeDef = TypedDict(
    "_OptionalScanSummaryTypeDef",
    {
        "scanNameArn": str,
        "updatedAt": datetime,
    },
    total=False,
)

class ScanSummaryTypeDef(_RequiredScanSummaryTypeDef, _OptionalScanSummaryTypeDef):
    pass

SuggestedFixTypeDef = TypedDict(
    "SuggestedFixTypeDef",
    {
        "code": str,
        "description": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccountConfigurationRequestRequestTypeDef",
    {
        "encryptionConfig": "EncryptionConfigTypeDef",
    },
)

UpdateAccountConfigurationResponseTypeDef = TypedDict(
    "UpdateAccountConfigurationResponseTypeDef",
    {
        "encryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "filePath": "FilePathTypeDef",
        "id": str,
        "itemCount": int,
        "referenceUrls": List[str],
        "relatedVulnerabilities": List[str],
    },
    total=False,
)
