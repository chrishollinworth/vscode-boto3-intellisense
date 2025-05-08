"""
Type annotations for accessanalyzer service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewStatusReasonTypeDef

    data: AccessPreviewStatusReasonTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AccessCheckPolicyTypeType,
    AccessCheckResourceTypeType,
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    CheckAccessNotGrantedResultType,
    CheckNoNewAccessResultType,
    CheckNoPublicAccessResultType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    FindingTypeType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    RecommendedRemediationActionType,
    ResourceControlPolicyRestrictionType,
    ResourceTypeType,
    StatusType,
    TypeType,
    ValidatePolicyFindingTypeType,
    ValidatePolicyResourceTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AccessTypeDef",
    "AclGranteeTypeDef",
    "AnalysisRuleCriteriaOutputTypeDef",
    "AnalysisRuleCriteriaTypeDef",
    "AnalysisRuleOutputTypeDef",
    "AnalysisRuleTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerConfigurationOutputTypeDef",
    "AnalyzerConfigurationTypeDef",
    "AnalyzerConfigurationUnionTypeDef",
    "AnalyzerSummaryTypeDef",
    "ApplyArchiveRuleRequestTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CancelPolicyGenerationRequestTypeDef",
    "CheckAccessNotGrantedRequestTypeDef",
    "CheckAccessNotGrantedResponseTypeDef",
    "CheckNoNewAccessRequestTypeDef",
    "CheckNoNewAccessResponseTypeDef",
    "CheckNoPublicAccessRequestTypeDef",
    "CheckNoPublicAccessResponseTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationUnionTypeDef",
    "CreateAccessPreviewRequestTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerRequestTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CreateArchiveRuleRequestTypeDef",
    "CriterionOutputTypeDef",
    "CriterionTypeDef",
    "CriterionUnionTypeDef",
    "DeleteAnalyzerRequestTypeDef",
    "DeleteArchiveRuleRequestTypeDef",
    "DynamodbStreamConfigurationTypeDef",
    "DynamodbTableConfigurationTypeDef",
    "EbsSnapshotConfigurationOutputTypeDef",
    "EbsSnapshotConfigurationTypeDef",
    "EbsSnapshotConfigurationUnionTypeDef",
    "EcrRepositoryConfigurationTypeDef",
    "EfsFileSystemConfigurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExternalAccessDetailsTypeDef",
    "ExternalAccessFindingsStatisticsTypeDef",
    "FindingAggregationAccountDetailsTypeDef",
    "FindingDetailsTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingSummaryV2TypeDef",
    "FindingTypeDef",
    "FindingsStatisticsTypeDef",
    "GenerateFindingRecommendationRequestTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceRequestTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerRequestTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleRequestTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingRecommendationRequestPaginateTypeDef",
    "GetFindingRecommendationRequestTypeDef",
    "GetFindingRecommendationResponseTypeDef",
    "GetFindingRequestTypeDef",
    "GetFindingResponseTypeDef",
    "GetFindingV2RequestPaginateTypeDef",
    "GetFindingV2RequestTypeDef",
    "GetFindingV2ResponseTypeDef",
    "GetFindingsStatisticsRequestTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetGeneratedPolicyRequestTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationOutputTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConfigurationUnionTypeDef",
    "KmsGrantConstraintsOutputTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsGrantConstraintsUnionTypeDef",
    "KmsKeyConfigurationOutputTypeDef",
    "KmsKeyConfigurationTypeDef",
    "KmsKeyConfigurationUnionTypeDef",
    "ListAccessPreviewFindingsRequestPaginateTypeDef",
    "ListAccessPreviewFindingsRequestTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsRequestPaginateTypeDef",
    "ListAccessPreviewsRequestTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesRequestPaginateTypeDef",
    "ListAnalyzedResourcesRequestTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersRequestPaginateTypeDef",
    "ListAnalyzersRequestTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesRequestPaginateTypeDef",
    "ListArchiveRulesRequestTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsRequestPaginateTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListFindingsV2RequestPaginateTypeDef",
    "ListFindingsV2RequestTypeDef",
    "ListFindingsV2ResponseTypeDef",
    "ListPolicyGenerationsRequestPaginateTypeDef",
    "ListPolicyGenerationsRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationOutputTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "NetworkOriginConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "RdsDbClusterSnapshotAttributeValueOutputTypeDef",
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    "RdsDbClusterSnapshotAttributeValueUnionTypeDef",
    "RdsDbClusterSnapshotConfigurationOutputTypeDef",
    "RdsDbClusterSnapshotConfigurationTypeDef",
    "RdsDbClusterSnapshotConfigurationUnionTypeDef",
    "RdsDbSnapshotAttributeValueOutputTypeDef",
    "RdsDbSnapshotAttributeValueTypeDef",
    "RdsDbSnapshotAttributeValueUnionTypeDef",
    "RdsDbSnapshotConfigurationOutputTypeDef",
    "RdsDbSnapshotConfigurationTypeDef",
    "RdsDbSnapshotConfigurationUnionTypeDef",
    "ReasonSummaryTypeDef",
    "RecommendationErrorTypeDef",
    "RecommendedStepTypeDef",
    "ResourceTypeDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessPointConfigurationOutputTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3AccessPointConfigurationUnionTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationOutputTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3BucketConfigurationUnionTypeDef",
    "S3ExpressDirectoryAccessPointConfigurationOutputTypeDef",
    "S3ExpressDirectoryAccessPointConfigurationTypeDef",
    "S3ExpressDirectoryAccessPointConfigurationUnionTypeDef",
    "S3ExpressDirectoryBucketConfigurationOutputTypeDef",
    "S3ExpressDirectoryBucketConfigurationTypeDef",
    "S3ExpressDirectoryBucketConfigurationUnionTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SnsTopicConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationRequestTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StartResourceScanRequestTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "UntagResourceRequestTypeDef",
    "UnusedAccessConfigurationOutputTypeDef",
    "UnusedAccessConfigurationTypeDef",
    "UnusedAccessFindingsStatisticsTypeDef",
    "UnusedAccessTypeStatisticsTypeDef",
    "UnusedActionTypeDef",
    "UnusedIamRoleDetailsTypeDef",
    "UnusedIamUserAccessKeyDetailsTypeDef",
    "UnusedIamUserPasswordDetailsTypeDef",
    "UnusedPermissionDetailsTypeDef",
    "UnusedPermissionsRecommendedStepTypeDef",
    "UpdateAnalyzerRequestTypeDef",
    "UpdateAnalyzerResponseTypeDef",
    "UpdateArchiveRuleRequestTypeDef",
    "UpdateFindingsRequestTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyRequestPaginateTypeDef",
    "ValidatePolicyRequestTypeDef",
    "ValidatePolicyResponseTypeDef",
    "VpcConfigurationTypeDef",
)

class AccessPreviewStatusReasonTypeDef(TypedDict):
    code: AccessPreviewStatusReasonCodeType

class AccessTypeDef(TypedDict):
    actions: NotRequired[Sequence[str]]
    resources: NotRequired[Sequence[str]]

AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": NotRequired[str],
        "uri": NotRequired[str],
    },
)

class AnalysisRuleCriteriaOutputTypeDef(TypedDict):
    accountIds: NotRequired[List[str]]
    resourceTags: NotRequired[List[Dict[str, str]]]

class AnalysisRuleCriteriaTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    resourceTags: NotRequired[Sequence[Mapping[str, str]]]

class AnalyzedResourceSummaryTypeDef(TypedDict):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceTypeType

class AnalyzedResourceTypeDef(TypedDict):
    resourceArn: str
    resourceType: ResourceTypeType
    createdAt: datetime
    analyzedAt: datetime
    updatedAt: datetime
    isPublic: bool
    resourceOwnerAccount: str
    actions: NotRequired[List[str]]
    sharedVia: NotRequired[List[str]]
    status: NotRequired[FindingStatusType]
    error: NotRequired[str]

class StatusReasonTypeDef(TypedDict):
    code: ReasonCodeType

class ApplyArchiveRuleRequestTypeDef(TypedDict):
    analyzerArn: str
    ruleName: str
    clientToken: NotRequired[str]

class CriterionOutputTypeDef(TypedDict):
    eq: NotRequired[List[str]]
    neq: NotRequired[List[str]]
    contains: NotRequired[List[str]]
    exists: NotRequired[bool]

class CancelPolicyGenerationRequestTypeDef(TypedDict):
    jobId: str

class ReasonSummaryTypeDef(TypedDict):
    description: NotRequired[str]
    statementIndex: NotRequired[int]
    statementId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CheckNoNewAccessRequestTypeDef(TypedDict):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType

class CheckNoPublicAccessRequestTypeDef(TypedDict):
    policyDocument: str
    resourceType: AccessCheckResourceTypeType

TimestampTypeDef = Union[datetime, str]

class TrailTypeDef(TypedDict):
    cloudTrailArn: str
    regions: NotRequired[Sequence[str]]
    allRegions: NotRequired[bool]

class TrailPropertiesTypeDef(TypedDict):
    cloudTrailArn: str
    regions: NotRequired[List[str]]
    allRegions: NotRequired[bool]

class DynamodbStreamConfigurationTypeDef(TypedDict):
    streamPolicy: NotRequired[str]

class DynamodbTableConfigurationTypeDef(TypedDict):
    tablePolicy: NotRequired[str]

class EbsSnapshotConfigurationOutputTypeDef(TypedDict):
    userIds: NotRequired[List[str]]
    groups: NotRequired[List[str]]
    kmsKeyId: NotRequired[str]

class EcrRepositoryConfigurationTypeDef(TypedDict):
    repositoryPolicy: NotRequired[str]

class EfsFileSystemConfigurationTypeDef(TypedDict):
    fileSystemPolicy: NotRequired[str]

class IamRoleConfigurationTypeDef(TypedDict):
    trustPolicy: NotRequired[str]

class SecretsManagerSecretConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]
    secretPolicy: NotRequired[str]

class SnsTopicConfigurationTypeDef(TypedDict):
    topicPolicy: NotRequired[str]

class SqsQueueConfigurationTypeDef(TypedDict):
    queuePolicy: NotRequired[str]

class CriterionTypeDef(TypedDict):
    eq: NotRequired[Sequence[str]]
    neq: NotRequired[Sequence[str]]
    contains: NotRequired[Sequence[str]]
    exists: NotRequired[bool]

class DeleteAnalyzerRequestTypeDef(TypedDict):
    analyzerName: str
    clientToken: NotRequired[str]

class DeleteArchiveRuleRequestTypeDef(TypedDict):
    analyzerName: str
    ruleName: str
    clientToken: NotRequired[str]

class EbsSnapshotConfigurationTypeDef(TypedDict):
    userIds: NotRequired[Sequence[str]]
    groups: NotRequired[Sequence[str]]
    kmsKeyId: NotRequired[str]

class ResourceTypeDetailsTypeDef(TypedDict):
    totalActivePublic: NotRequired[int]
    totalActiveCrossAccount: NotRequired[int]

class FindingAggregationAccountDetailsTypeDef(TypedDict):
    account: NotRequired[str]
    numberOfActiveFindings: NotRequired[int]
    details: NotRequired[Dict[str, int]]

class UnusedIamRoleDetailsTypeDef(TypedDict):
    lastAccessed: NotRequired[datetime]

class UnusedIamUserAccessKeyDetailsTypeDef(TypedDict):
    accessKeyId: str
    lastAccessed: NotRequired[datetime]

class UnusedIamUserPasswordDetailsTypeDef(TypedDict):
    lastAccessed: NotRequired[datetime]

class FindingSourceDetailTypeDef(TypedDict):
    accessPointArn: NotRequired[str]
    accessPointAccount: NotRequired[str]

FindingSummaryV2TypeDef = TypedDict(
    "FindingSummaryV2TypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "id": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "error": NotRequired[str],
        "resource": NotRequired[str],
        "findingType": NotRequired[FindingTypeType],
    },
)
GenerateFindingRecommendationRequestTypeDef = TypedDict(
    "GenerateFindingRecommendationRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

class GeneratedPolicyTypeDef(TypedDict):
    policy: str

class GetAccessPreviewRequestTypeDef(TypedDict):
    accessPreviewId: str
    analyzerArn: str

class GetAnalyzedResourceRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceArn: str

class GetAnalyzerRequestTypeDef(TypedDict):
    analyzerName: str

class GetArchiveRuleRequestTypeDef(TypedDict):
    analyzerName: str
    ruleName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

GetFindingRecommendationRequestTypeDef = TypedDict(
    "GetFindingRecommendationRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class RecommendationErrorTypeDef(TypedDict):
    code: str
    message: str

GetFindingRequestTypeDef = TypedDict(
    "GetFindingRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)
GetFindingV2RequestTypeDef = TypedDict(
    "GetFindingV2RequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class GetFindingsStatisticsRequestTypeDef(TypedDict):
    analyzerArn: str

class GetGeneratedPolicyRequestTypeDef(TypedDict):
    jobId: str
    includeResourcePlaceholders: NotRequired[bool]
    includeServiceLevelTemplate: NotRequired[bool]

class JobErrorTypeDef(TypedDict):
    code: JobErrorCodeType
    message: str

class KmsGrantConstraintsOutputTypeDef(TypedDict):
    encryptionContextEquals: NotRequired[Dict[str, str]]
    encryptionContextSubset: NotRequired[Dict[str, str]]

class KmsGrantConstraintsTypeDef(TypedDict):
    encryptionContextEquals: NotRequired[Mapping[str, str]]
    encryptionContextSubset: NotRequired[Mapping[str, str]]

class ListAccessPreviewsRequestTypeDef(TypedDict):
    analyzerArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAnalyzedResourcesRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceType: NotRequired[ResourceTypeType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ListAnalyzersRequestTypeDef = TypedDict(
    "ListAnalyzersRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "type": NotRequired[TypeType],
    },
)

class ListArchiveRulesRequestTypeDef(TypedDict):
    analyzerName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SortCriteriaTypeDef(TypedDict):
    attributeName: NotRequired[str]
    orderBy: NotRequired[OrderByType]

class ListPolicyGenerationsRequestTypeDef(TypedDict):
    principalArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PolicyGenerationTypeDef(TypedDict):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class VpcConfigurationTypeDef(TypedDict):
    vpcId: str

class SubstringTypeDef(TypedDict):
    start: int
    length: int

class PolicyGenerationDetailsTypeDef(TypedDict):
    principalArn: str

class PositionTypeDef(TypedDict):
    line: int
    column: int
    offset: int

class RdsDbClusterSnapshotAttributeValueOutputTypeDef(TypedDict):
    accountIds: NotRequired[List[str]]

class RdsDbClusterSnapshotAttributeValueTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class RdsDbSnapshotAttributeValueOutputTypeDef(TypedDict):
    accountIds: NotRequired[List[str]]

class RdsDbSnapshotAttributeValueTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class UnusedPermissionsRecommendedStepTypeDef(TypedDict):
    recommendedAction: RecommendedRemediationActionType
    policyUpdatedAt: NotRequired[datetime]
    recommendedPolicy: NotRequired[str]
    existingPolicyId: NotRequired[str]

class S3PublicAccessBlockConfigurationTypeDef(TypedDict):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool

class StartResourceScanRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UnusedAccessTypeStatisticsTypeDef(TypedDict):
    unusedAccessType: NotRequired[str]
    total: NotRequired[int]

class UnusedActionTypeDef(TypedDict):
    action: str
    lastAccessed: NotRequired[datetime]

class UpdateFindingsRequestTypeDef(TypedDict):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: NotRequired[Sequence[str]]
    resourceArn: NotRequired[str]
    clientToken: NotRequired[str]

class ValidatePolicyRequestTypeDef(TypedDict):
    policyDocument: str
    policyType: PolicyTypeType
    locale: NotRequired[LocaleType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    validatePolicyResourceType: NotRequired[ValidatePolicyResourceTypeType]

AccessPreviewSummaryTypeDef = TypedDict(
    "AccessPreviewSummaryTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)

class CheckAccessNotGrantedRequestTypeDef(TypedDict):
    policyDocument: str
    access: Sequence[AccessTypeDef]
    policyType: AccessCheckPolicyTypeType

class S3BucketAclGrantConfigurationTypeDef(TypedDict):
    permission: AclPermissionType
    grantee: AclGranteeTypeDef

class AnalysisRuleOutputTypeDef(TypedDict):
    exclusions: NotRequired[List[AnalysisRuleCriteriaOutputTypeDef]]

class AnalysisRuleTypeDef(TypedDict):
    exclusions: NotRequired[Sequence[AnalysisRuleCriteriaTypeDef]]

ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "ruleName": str,
        "filter": Dict[str, CriterionOutputTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)

class CheckAccessNotGrantedResponseTypeDef(TypedDict):
    result: CheckAccessNotGrantedResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoNewAccessResponseTypeDef(TypedDict):
    result: CheckNoNewAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoPublicAccessResponseTypeDef(TypedDict):
    result: CheckNoPublicAccessResultType
    message: str
    reasons: List[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateAnalyzerResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalyzedResourceResponseTypeDef(TypedDict):
    resource: AnalyzedResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzedResourcesResponseTypeDef(TypedDict):
    analyzedResources: List[AnalyzedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudTrailDetailsTypeDef(TypedDict):
    trails: Sequence[TrailTypeDef]
    accessRole: str
    startTime: TimestampTypeDef
    endTime: NotRequired[TimestampTypeDef]

class CloudTrailPropertiesTypeDef(TypedDict):
    trailProperties: List[TrailPropertiesTypeDef]
    startTime: datetime
    endTime: datetime

CriterionUnionTypeDef = Union[CriterionTypeDef, CriterionOutputTypeDef]
EbsSnapshotConfigurationUnionTypeDef = Union[
    EbsSnapshotConfigurationTypeDef, EbsSnapshotConfigurationOutputTypeDef
]

class ExternalAccessFindingsStatisticsTypeDef(TypedDict):
    resourceTypeStatistics: NotRequired[Dict[ResourceTypeType, ResourceTypeDetailsTypeDef]]
    totalActiveFindings: NotRequired[int]
    totalArchivedFindings: NotRequired[int]
    totalResolvedFindings: NotRequired[int]

FindingSourceTypeDef = TypedDict(
    "FindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
        "detail": NotRequired[FindingSourceDetailTypeDef],
    },
)

class ListFindingsV2ResponseTypeDef(TypedDict):
    findings: List[FindingSummaryV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetFindingRecommendationRequestPaginateTypeDef = TypedDict(
    "GetFindingRecommendationRequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingV2RequestPaginateTypeDef = TypedDict(
    "GetFindingV2RequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListAccessPreviewsRequestPaginateTypeDef(TypedDict):
    analyzerArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAnalyzedResourcesRequestPaginateTypeDef(TypedDict):
    analyzerArn: str
    resourceType: NotRequired[ResourceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListAnalyzersRequestPaginateTypeDef = TypedDict(
    "ListAnalyzersRequestPaginateTypeDef",
    {
        "type": NotRequired[TypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListArchiveRulesRequestPaginateTypeDef(TypedDict):
    analyzerName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyGenerationsRequestPaginateTypeDef(TypedDict):
    principalArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ValidatePolicyRequestPaginateTypeDef(TypedDict):
    policyDocument: str
    policyType: PolicyTypeType
    locale: NotRequired[LocaleType]
    validatePolicyResourceType: NotRequired[ValidatePolicyResourceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class JobDetailsTypeDef(TypedDict):
    jobId: str
    status: JobStatusType
    startedOn: datetime
    completedOn: NotRequired[datetime]
    jobError: NotRequired[JobErrorTypeDef]

class KmsGrantConfigurationOutputTypeDef(TypedDict):
    operations: List[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: NotRequired[str]
    constraints: NotRequired[KmsGrantConstraintsOutputTypeDef]

KmsGrantConstraintsUnionTypeDef = Union[
    KmsGrantConstraintsTypeDef, KmsGrantConstraintsOutputTypeDef
]

class ListPolicyGenerationsResponseTypeDef(TypedDict):
    policyGenerations: List[PolicyGenerationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NetworkOriginConfigurationOutputTypeDef(TypedDict):
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    internetConfiguration: NotRequired[Dict[str, Any]]

class NetworkOriginConfigurationTypeDef(TypedDict):
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    internetConfiguration: NotRequired[Mapping[str, Any]]

class PathElementTypeDef(TypedDict):
    index: NotRequired[int]
    key: NotRequired[str]
    substring: NotRequired[SubstringTypeDef]
    value: NotRequired[str]

class SpanTypeDef(TypedDict):
    start: PositionTypeDef
    end: PositionTypeDef

class RdsDbClusterSnapshotConfigurationOutputTypeDef(TypedDict):
    attributes: NotRequired[Dict[str, RdsDbClusterSnapshotAttributeValueOutputTypeDef]]
    kmsKeyId: NotRequired[str]

RdsDbClusterSnapshotAttributeValueUnionTypeDef = Union[
    RdsDbClusterSnapshotAttributeValueTypeDef, RdsDbClusterSnapshotAttributeValueOutputTypeDef
]

class RdsDbSnapshotConfigurationOutputTypeDef(TypedDict):
    attributes: NotRequired[Dict[str, RdsDbSnapshotAttributeValueOutputTypeDef]]
    kmsKeyId: NotRequired[str]

RdsDbSnapshotAttributeValueUnionTypeDef = Union[
    RdsDbSnapshotAttributeValueTypeDef, RdsDbSnapshotAttributeValueOutputTypeDef
]

class RecommendedStepTypeDef(TypedDict):
    unusedPermissionsRecommendedStep: NotRequired[UnusedPermissionsRecommendedStepTypeDef]

class UnusedAccessFindingsStatisticsTypeDef(TypedDict):
    unusedAccessTypeStatistics: NotRequired[List[UnusedAccessTypeStatisticsTypeDef]]
    topAccounts: NotRequired[List[FindingAggregationAccountDetailsTypeDef]]
    totalActiveFindings: NotRequired[int]
    totalArchivedFindings: NotRequired[int]
    totalResolvedFindings: NotRequired[int]

class UnusedPermissionDetailsTypeDef(TypedDict):
    serviceNamespace: str
    actions: NotRequired[List[UnusedActionTypeDef]]
    lastAccessed: NotRequired[datetime]

class ListAccessPreviewsResponseTypeDef(TypedDict):
    accessPreviews: List[AccessPreviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UnusedAccessConfigurationOutputTypeDef(TypedDict):
    unusedAccessAge: NotRequired[int]
    analysisRule: NotRequired[AnalysisRuleOutputTypeDef]

class UnusedAccessConfigurationTypeDef(TypedDict):
    unusedAccessAge: NotRequired[int]
    analysisRule: NotRequired[AnalysisRuleTypeDef]

class GetArchiveRuleResponseTypeDef(TypedDict):
    archiveRule: ArchiveRuleSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArchiveRulesResponseTypeDef(TypedDict):
    archiveRules: List[ArchiveRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartPolicyGenerationRequestTypeDef(TypedDict):
    policyGenerationDetails: PolicyGenerationDetailsTypeDef
    cloudTrailDetails: NotRequired[CloudTrailDetailsTypeDef]
    clientToken: NotRequired[str]

class GeneratedPolicyPropertiesTypeDef(TypedDict):
    principalArn: str
    isComplete: NotRequired[bool]
    cloudTrailProperties: NotRequired[CloudTrailPropertiesTypeDef]

CreateArchiveRuleRequestTypeDef = TypedDict(
    "CreateArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionUnionTypeDef],
        "clientToken": NotRequired[str],
    },
)
InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "ruleName": str,
        "filter": Mapping[str, CriterionUnionTypeDef],
    },
)
ListAccessPreviewFindingsRequestPaginateTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestPaginateTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPreviewFindingsRequestTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsRequestPaginateTypeDef = TypedDict(
    "ListFindingsRequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestTypeDef = TypedDict(
    "ListFindingsRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsV2RequestPaginateTypeDef = TypedDict(
    "ListFindingsV2RequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsV2RequestTypeDef = TypedDict(
    "ListFindingsV2RequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionUnionTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortCriteriaTypeDef],
    },
)
UpdateArchiveRuleRequestTypeDef = TypedDict(
    "UpdateArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionUnionTypeDef],
        "clientToken": NotRequired[str],
    },
)
AccessPreviewFindingTypeDef = TypedDict(
    "AccessPreviewFindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "changeType": FindingChangeTypeType,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "existingFindingId": NotRequired[str],
        "existingFindingStatus": NotRequired[FindingStatusType],
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "condition": NotRequired[Dict[str, str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)

class ExternalAccessDetailsTypeDef(TypedDict):
    condition: Dict[str, str]
    action: NotRequired[List[str]]
    isPublic: NotRequired[bool]
    principal: NotRequired[Dict[str, str]]
    sources: NotRequired[List[FindingSourceTypeDef]]
    resourceControlPolicyRestriction: NotRequired[ResourceControlPolicyRestrictionType]

FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)

class KmsKeyConfigurationOutputTypeDef(TypedDict):
    keyPolicies: NotRequired[Dict[str, str]]
    grants: NotRequired[List[KmsGrantConfigurationOutputTypeDef]]

class KmsGrantConfigurationTypeDef(TypedDict):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: NotRequired[str]
    constraints: NotRequired[KmsGrantConstraintsUnionTypeDef]

class S3AccessPointConfigurationOutputTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    publicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    networkOrigin: NotRequired[NetworkOriginConfigurationOutputTypeDef]

class S3ExpressDirectoryAccessPointConfigurationOutputTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    networkOrigin: NotRequired[NetworkOriginConfigurationOutputTypeDef]

NetworkOriginConfigurationUnionTypeDef = Union[
    NetworkOriginConfigurationTypeDef, NetworkOriginConfigurationOutputTypeDef
]

class LocationTypeDef(TypedDict):
    path: List[PathElementTypeDef]
    span: SpanTypeDef

class RdsDbClusterSnapshotConfigurationTypeDef(TypedDict):
    attributes: NotRequired[Mapping[str, RdsDbClusterSnapshotAttributeValueUnionTypeDef]]
    kmsKeyId: NotRequired[str]

class RdsDbSnapshotConfigurationTypeDef(TypedDict):
    attributes: NotRequired[Mapping[str, RdsDbSnapshotAttributeValueUnionTypeDef]]
    kmsKeyId: NotRequired[str]

class GetFindingRecommendationResponseTypeDef(TypedDict):
    startedAt: datetime
    completedAt: datetime
    error: RecommendationErrorTypeDef
    resourceArn: str
    recommendedSteps: List[RecommendedStepTypeDef]
    recommendationType: Literal["UnusedPermissionRecommendation"]
    status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FindingsStatisticsTypeDef(TypedDict):
    externalAccessFindingsStatistics: NotRequired[ExternalAccessFindingsStatisticsTypeDef]
    unusedAccessFindingsStatistics: NotRequired[UnusedAccessFindingsStatisticsTypeDef]

class AnalyzerConfigurationOutputTypeDef(TypedDict):
    unusedAccess: NotRequired[UnusedAccessConfigurationOutputTypeDef]

class AnalyzerConfigurationTypeDef(TypedDict):
    unusedAccess: NotRequired[UnusedAccessConfigurationTypeDef]

class GeneratedPolicyResultTypeDef(TypedDict):
    properties: GeneratedPolicyPropertiesTypeDef
    generatedPolicies: NotRequired[List[GeneratedPolicyTypeDef]]

class ListAccessPreviewFindingsResponseTypeDef(TypedDict):
    findings: List[AccessPreviewFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FindingDetailsTypeDef(TypedDict):
    externalAccessDetails: NotRequired[ExternalAccessDetailsTypeDef]
    unusedPermissionDetails: NotRequired[UnusedPermissionDetailsTypeDef]
    unusedIamUserAccessKeyDetails: NotRequired[UnusedIamUserAccessKeyDetailsTypeDef]
    unusedIamRoleDetails: NotRequired[UnusedIamRoleDetailsTypeDef]
    unusedIamUserPasswordDetails: NotRequired[UnusedIamUserPasswordDetailsTypeDef]

class ListFindingsResponseTypeDef(TypedDict):
    findings: List[FindingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetFindingResponseTypeDef(TypedDict):
    finding: FindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

KmsGrantConfigurationUnionTypeDef = Union[
    KmsGrantConfigurationTypeDef, KmsGrantConfigurationOutputTypeDef
]

class S3BucketConfigurationOutputTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    bucketAclGrants: NotRequired[List[S3BucketAclGrantConfigurationTypeDef]]
    bucketPublicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    accessPoints: NotRequired[Dict[str, S3AccessPointConfigurationOutputTypeDef]]

class S3ExpressDirectoryBucketConfigurationOutputTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    accessPoints: NotRequired[Dict[str, S3ExpressDirectoryAccessPointConfigurationOutputTypeDef]]

class S3AccessPointConfigurationTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    publicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    networkOrigin: NotRequired[NetworkOriginConfigurationUnionTypeDef]

class S3ExpressDirectoryAccessPointConfigurationTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    networkOrigin: NotRequired[NetworkOriginConfigurationUnionTypeDef]

class ValidatePolicyFindingTypeDef(TypedDict):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: List[LocationTypeDef]

RdsDbClusterSnapshotConfigurationUnionTypeDef = Union[
    RdsDbClusterSnapshotConfigurationTypeDef, RdsDbClusterSnapshotConfigurationOutputTypeDef
]
RdsDbSnapshotConfigurationUnionTypeDef = Union[
    RdsDbSnapshotConfigurationTypeDef, RdsDbSnapshotConfigurationOutputTypeDef
]

class GetFindingsStatisticsResponseTypeDef(TypedDict):
    findingsStatistics: List[FindingsStatisticsTypeDef]
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

AnalyzerSummaryTypeDef = TypedDict(
    "AnalyzerSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TypeType,
        "createdAt": datetime,
        "status": AnalyzerStatusType,
        "lastResourceAnalyzed": NotRequired[str],
        "lastResourceAnalyzedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "statusReason": NotRequired[StatusReasonTypeDef],
        "configuration": NotRequired[AnalyzerConfigurationOutputTypeDef],
    },
)

class UpdateAnalyzerResponseTypeDef(TypedDict):
    configuration: AnalyzerConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

AnalyzerConfigurationUnionTypeDef = Union[
    AnalyzerConfigurationTypeDef, AnalyzerConfigurationOutputTypeDef
]

class GetGeneratedPolicyResponseTypeDef(TypedDict):
    jobDetails: JobDetailsTypeDef
    generatedPolicyResult: GeneratedPolicyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

GetFindingV2ResponseTypeDef = TypedDict(
    "GetFindingV2ResponseTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "error": str,
        "id": str,
        "resource": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "findingDetails": List[FindingDetailsTypeDef],
        "findingType": FindingTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)

class KmsKeyConfigurationTypeDef(TypedDict):
    keyPolicies: NotRequired[Mapping[str, str]]
    grants: NotRequired[Sequence[KmsGrantConfigurationUnionTypeDef]]

class ConfigurationOutputTypeDef(TypedDict):
    ebsSnapshot: NotRequired[EbsSnapshotConfigurationOutputTypeDef]
    ecrRepository: NotRequired[EcrRepositoryConfigurationTypeDef]
    iamRole: NotRequired[IamRoleConfigurationTypeDef]
    efsFileSystem: NotRequired[EfsFileSystemConfigurationTypeDef]
    kmsKey: NotRequired[KmsKeyConfigurationOutputTypeDef]
    rdsDbClusterSnapshot: NotRequired[RdsDbClusterSnapshotConfigurationOutputTypeDef]
    rdsDbSnapshot: NotRequired[RdsDbSnapshotConfigurationOutputTypeDef]
    secretsManagerSecret: NotRequired[SecretsManagerSecretConfigurationTypeDef]
    s3Bucket: NotRequired[S3BucketConfigurationOutputTypeDef]
    snsTopic: NotRequired[SnsTopicConfigurationTypeDef]
    sqsQueue: NotRequired[SqsQueueConfigurationTypeDef]
    s3ExpressDirectoryBucket: NotRequired[S3ExpressDirectoryBucketConfigurationOutputTypeDef]
    dynamodbStream: NotRequired[DynamodbStreamConfigurationTypeDef]
    dynamodbTable: NotRequired[DynamodbTableConfigurationTypeDef]

S3AccessPointConfigurationUnionTypeDef = Union[
    S3AccessPointConfigurationTypeDef, S3AccessPointConfigurationOutputTypeDef
]
S3ExpressDirectoryAccessPointConfigurationUnionTypeDef = Union[
    S3ExpressDirectoryAccessPointConfigurationTypeDef,
    S3ExpressDirectoryAccessPointConfigurationOutputTypeDef,
]

class ValidatePolicyResponseTypeDef(TypedDict):
    findings: List[ValidatePolicyFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetAnalyzerResponseTypeDef(TypedDict):
    analyzer: AnalyzerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzersResponseTypeDef(TypedDict):
    analyzers: List[AnalyzerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateAnalyzerRequestTypeDef = TypedDict(
    "CreateAnalyzerRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
        "archiveRules": NotRequired[Sequence[InlineArchiveRuleTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[AnalyzerConfigurationUnionTypeDef],
    },
)

class UpdateAnalyzerRequestTypeDef(TypedDict):
    analyzerName: str
    configuration: NotRequired[AnalyzerConfigurationUnionTypeDef]

KmsKeyConfigurationUnionTypeDef = Union[
    KmsKeyConfigurationTypeDef, KmsKeyConfigurationOutputTypeDef
]
AccessPreviewTypeDef = TypedDict(
    "AccessPreviewTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "configurations": Dict[str, ConfigurationOutputTypeDef],
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)

class S3BucketConfigurationTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    bucketAclGrants: NotRequired[Sequence[S3BucketAclGrantConfigurationTypeDef]]
    bucketPublicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    accessPoints: NotRequired[Mapping[str, S3AccessPointConfigurationUnionTypeDef]]

class S3ExpressDirectoryBucketConfigurationTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    accessPoints: NotRequired[Mapping[str, S3ExpressDirectoryAccessPointConfigurationUnionTypeDef]]

class GetAccessPreviewResponseTypeDef(TypedDict):
    accessPreview: AccessPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

S3BucketConfigurationUnionTypeDef = Union[
    S3BucketConfigurationTypeDef, S3BucketConfigurationOutputTypeDef
]
S3ExpressDirectoryBucketConfigurationUnionTypeDef = Union[
    S3ExpressDirectoryBucketConfigurationTypeDef, S3ExpressDirectoryBucketConfigurationOutputTypeDef
]

class ConfigurationTypeDef(TypedDict):
    ebsSnapshot: NotRequired[EbsSnapshotConfigurationUnionTypeDef]
    ecrRepository: NotRequired[EcrRepositoryConfigurationTypeDef]
    iamRole: NotRequired[IamRoleConfigurationTypeDef]
    efsFileSystem: NotRequired[EfsFileSystemConfigurationTypeDef]
    kmsKey: NotRequired[KmsKeyConfigurationUnionTypeDef]
    rdsDbClusterSnapshot: NotRequired[RdsDbClusterSnapshotConfigurationUnionTypeDef]
    rdsDbSnapshot: NotRequired[RdsDbSnapshotConfigurationUnionTypeDef]
    secretsManagerSecret: NotRequired[SecretsManagerSecretConfigurationTypeDef]
    s3Bucket: NotRequired[S3BucketConfigurationUnionTypeDef]
    snsTopic: NotRequired[SnsTopicConfigurationTypeDef]
    sqsQueue: NotRequired[SqsQueueConfigurationTypeDef]
    s3ExpressDirectoryBucket: NotRequired[S3ExpressDirectoryBucketConfigurationUnionTypeDef]
    dynamodbStream: NotRequired[DynamodbStreamConfigurationTypeDef]
    dynamodbTable: NotRequired[DynamodbTableConfigurationTypeDef]

ConfigurationUnionTypeDef = Union[ConfigurationTypeDef, ConfigurationOutputTypeDef]

class CreateAccessPreviewRequestTypeDef(TypedDict):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnionTypeDef]
    clientToken: NotRequired[str]
