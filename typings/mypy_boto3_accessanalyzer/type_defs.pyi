"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewFindingTypeDef

    data: AccessPreviewFindingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    ResourceTypeType,
    TypeType,
    ValidatePolicyFindingTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerSummaryTypeDef",
    "ApplyArchiveRuleRequestRequestTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CancelPolicyGenerationRequestRequestTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationTypeDef",
    "CreateAccessPreviewRequestRequestTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerRequestRequestTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CreateArchiveRuleRequestRequestTypeDef",
    "CriterionTypeDef",
    "DeleteAnalyzerRequestRequestTypeDef",
    "DeleteArchiveRuleRequestRequestTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceRequestRequestTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerRequestRequestTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleRequestRequestTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingRequestRequestTypeDef",
    "GetFindingResponseTypeDef",
    "GetGeneratedPolicyRequestRequestTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsKeyConfigurationTypeDef",
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsRequestRequestTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesRequestRequestTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersRequestRequestTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesRequestRequestTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListPolicyGenerationsRequestRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationRequestRequestTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StartResourceScanRequestRequestTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateArchiveRuleRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyRequestRequestTypeDef",
    "ValidatePolicyResponseTypeDef",
    "VpcConfigurationTypeDef",
)

_RequiredAccessPreviewFindingTypeDef = TypedDict(
    "_RequiredAccessPreviewFindingTypeDef",
    {
        "changeType": FindingChangeTypeType,
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
    },
)
_OptionalAccessPreviewFindingTypeDef = TypedDict(
    "_OptionalAccessPreviewFindingTypeDef",
    {
        "action": List[str],
        "condition": Dict[str, str],
        "error": str,
        "existingFindingId": str,
        "existingFindingStatus": FindingStatusType,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)

class AccessPreviewFindingTypeDef(
    _RequiredAccessPreviewFindingTypeDef, _OptionalAccessPreviewFindingTypeDef
):
    pass

AccessPreviewStatusReasonTypeDef = TypedDict(
    "AccessPreviewStatusReasonTypeDef",
    {
        "code": AccessPreviewStatusReasonCodeType,
    },
)

_RequiredAccessPreviewSummaryTypeDef = TypedDict(
    "_RequiredAccessPreviewSummaryTypeDef",
    {
        "analyzerArn": str,
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewSummaryTypeDef = TypedDict(
    "_OptionalAccessPreviewSummaryTypeDef",
    {
        "statusReason": "AccessPreviewStatusReasonTypeDef",
    },
    total=False,
)

class AccessPreviewSummaryTypeDef(
    _RequiredAccessPreviewSummaryTypeDef, _OptionalAccessPreviewSummaryTypeDef
):
    pass

_RequiredAccessPreviewTypeDef = TypedDict(
    "_RequiredAccessPreviewTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewTypeDef = TypedDict(
    "_OptionalAccessPreviewTypeDef",
    {
        "statusReason": "AccessPreviewStatusReasonTypeDef",
    },
    total=False,
)

class AccessPreviewTypeDef(_RequiredAccessPreviewTypeDef, _OptionalAccessPreviewTypeDef):
    pass

AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": str,
        "uri": str,
    },
    total=False,
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
    },
)

_RequiredAnalyzedResourceTypeDef = TypedDict(
    "_RequiredAnalyzedResourceTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "isPublic": bool,
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "updatedAt": datetime,
    },
)
_OptionalAnalyzedResourceTypeDef = TypedDict(
    "_OptionalAnalyzedResourceTypeDef",
    {
        "actions": List[str],
        "error": str,
        "sharedVia": List[str],
        "status": FindingStatusType,
    },
    total=False,
)

class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, _OptionalAnalyzedResourceTypeDef):
    pass

_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "status": AnalyzerStatusType,
        "type": TypeType,
    },
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "statusReason": "StatusReasonTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass

_RequiredApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredApplyArchiveRuleRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "ruleName": str,
    },
)
_OptionalApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalApplyArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ApplyArchiveRuleRequestRequestTypeDef(
    _RequiredApplyArchiveRuleRequestRequestTypeDef, _OptionalApplyArchiveRuleRequestRequestTypeDef
):
    pass

ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

CancelPolicyGenerationRequestRequestTypeDef = TypedDict(
    "CancelPolicyGenerationRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredCloudTrailDetailsTypeDef = TypedDict(
    "_RequiredCloudTrailDetailsTypeDef",
    {
        "accessRole": str,
        "startTime": Union[datetime, str],
        "trails": List["TrailTypeDef"],
    },
)
_OptionalCloudTrailDetailsTypeDef = TypedDict(
    "_OptionalCloudTrailDetailsTypeDef",
    {
        "endTime": Union[datetime, str],
    },
    total=False,
)

class CloudTrailDetailsTypeDef(
    _RequiredCloudTrailDetailsTypeDef, _OptionalCloudTrailDetailsTypeDef
):
    pass

CloudTrailPropertiesTypeDef = TypedDict(
    "CloudTrailPropertiesTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
        "trailProperties": List["TrailPropertiesTypeDef"],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "iamRole": "IamRoleConfigurationTypeDef",
        "kmsKey": "KmsKeyConfigurationTypeDef",
        "s3Bucket": "S3BucketConfigurationTypeDef",
        "secretsManagerSecret": "SecretsManagerSecretConfigurationTypeDef",
        "sqsQueue": "SqsQueueConfigurationTypeDef",
    },
    total=False,
)

_RequiredCreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPreviewRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
    },
)
_OptionalCreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPreviewRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateAccessPreviewRequestRequestTypeDef(
    _RequiredCreateAccessPreviewRequestRequestTypeDef,
    _OptionalCreateAccessPreviewRequestRequestTypeDef,
):
    pass

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnalyzerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
    },
)
_OptionalCreateAnalyzerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnalyzerRequestRequestTypeDef",
    {
        "archiveRules": List["InlineArchiveRuleTypeDef"],
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAnalyzerRequestRequestTypeDef(
    _RequiredCreateAnalyzerRequestRequestTypeDef, _OptionalCreateAnalyzerRequestRequestTypeDef
):
    pass

CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)
_OptionalCreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateArchiveRuleRequestRequestTypeDef(
    _RequiredCreateArchiveRuleRequestRequestTypeDef, _OptionalCreateArchiveRuleRequestRequestTypeDef
):
    pass

CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {
        "contains": List[str],
        "eq": List[str],
        "exists": bool,
        "neq": List[str],
    },
    total=False,
)

_RequiredDeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalDeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalyzerRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAnalyzerRequestRequestTypeDef(
    _RequiredDeleteAnalyzerRequestRequestTypeDef, _OptionalDeleteAnalyzerRequestRequestTypeDef
):
    pass

_RequiredDeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)
_OptionalDeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteArchiveRuleRequestRequestTypeDef(
    _RequiredDeleteArchiveRuleRequestRequestTypeDef, _OptionalDeleteArchiveRuleRequestRequestTypeDef
):
    pass

FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef",
    {
        "accessPointArn": str,
    },
    total=False,
)

_RequiredFindingSourceTypeDef = TypedDict(
    "_RequiredFindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
    },
)
_OptionalFindingSourceTypeDef = TypedDict(
    "_OptionalFindingSourceTypeDef",
    {
        "detail": "FindingSourceDetailTypeDef",
    },
    total=False,
)

class FindingSourceTypeDef(_RequiredFindingSourceTypeDef, _OptionalFindingSourceTypeDef):
    pass

_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)

class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

_RequiredGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_RequiredGeneratedPolicyPropertiesTypeDef",
    {
        "principalArn": str,
    },
)
_OptionalGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_OptionalGeneratedPolicyPropertiesTypeDef",
    {
        "cloudTrailProperties": "CloudTrailPropertiesTypeDef",
        "isComplete": bool,
    },
    total=False,
)

class GeneratedPolicyPropertiesTypeDef(
    _RequiredGeneratedPolicyPropertiesTypeDef, _OptionalGeneratedPolicyPropertiesTypeDef
):
    pass

_RequiredGeneratedPolicyResultTypeDef = TypedDict(
    "_RequiredGeneratedPolicyResultTypeDef",
    {
        "properties": "GeneratedPolicyPropertiesTypeDef",
    },
)
_OptionalGeneratedPolicyResultTypeDef = TypedDict(
    "_OptionalGeneratedPolicyResultTypeDef",
    {
        "generatedPolicies": List["GeneratedPolicyTypeDef"],
    },
    total=False,
)

class GeneratedPolicyResultTypeDef(
    _RequiredGeneratedPolicyResultTypeDef, _OptionalGeneratedPolicyResultTypeDef
):
    pass

GeneratedPolicyTypeDef = TypedDict(
    "GeneratedPolicyTypeDef",
    {
        "policy": str,
    },
)

GetAccessPreviewRequestRequestTypeDef = TypedDict(
    "GetAccessPreviewRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)

GetAccessPreviewResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseTypeDef",
    {
        "accessPreview": "AccessPreviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzedResourceRequestRequestTypeDef = TypedDict(
    "GetAnalyzedResourceRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef",
    {
        "resource": "AnalyzedResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzerRequestRequestTypeDef = TypedDict(
    "GetAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)

GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef",
    {
        "analyzer": "AnalyzerSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveRuleRequestRequestTypeDef = TypedDict(
    "GetArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef",
    {
        "archiveRule": "ArchiveRuleSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingRequestRequestTypeDef = TypedDict(
    "GetFindingRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef",
    {
        "finding": "FindingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetGeneratedPolicyRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalGetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetGeneratedPolicyRequestRequestTypeDef",
    {
        "includeResourcePlaceholders": bool,
        "includeServiceLevelTemplate": bool,
    },
    total=False,
)

class GetGeneratedPolicyRequestRequestTypeDef(
    _RequiredGetGeneratedPolicyRequestRequestTypeDef,
    _OptionalGetGeneratedPolicyRequestRequestTypeDef,
):
    pass

GetGeneratedPolicyResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseTypeDef",
    {
        "generatedPolicyResult": "GeneratedPolicyResultTypeDef",
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamRoleConfigurationTypeDef = TypedDict(
    "IamRoleConfigurationTypeDef",
    {
        "trustPolicy": str,
    },
    total=False,
)

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)

_RequiredJobDetailsTypeDef = TypedDict(
    "_RequiredJobDetailsTypeDef",
    {
        "jobId": str,
        "startedOn": datetime,
        "status": JobStatusType,
    },
)
_OptionalJobDetailsTypeDef = TypedDict(
    "_OptionalJobDetailsTypeDef",
    {
        "completedOn": datetime,
        "jobError": "JobErrorTypeDef",
    },
    total=False,
)

class JobDetailsTypeDef(_RequiredJobDetailsTypeDef, _OptionalJobDetailsTypeDef):
    pass

JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "code": JobErrorCodeType,
        "message": str,
    },
)

_RequiredKmsGrantConfigurationTypeDef = TypedDict(
    "_RequiredKmsGrantConfigurationTypeDef",
    {
        "granteePrincipal": str,
        "issuingAccount": str,
        "operations": List[KmsGrantOperationType],
    },
)
_OptionalKmsGrantConfigurationTypeDef = TypedDict(
    "_OptionalKmsGrantConfigurationTypeDef",
    {
        "constraints": "KmsGrantConstraintsTypeDef",
        "retiringPrincipal": str,
    },
    total=False,
)

class KmsGrantConfigurationTypeDef(
    _RequiredKmsGrantConfigurationTypeDef, _OptionalKmsGrantConfigurationTypeDef
):
    pass

KmsGrantConstraintsTypeDef = TypedDict(
    "KmsGrantConstraintsTypeDef",
    {
        "encryptionContextEquals": Dict[str, str],
        "encryptionContextSubset": Dict[str, str],
    },
    total=False,
)

KmsKeyConfigurationTypeDef = TypedDict(
    "KmsKeyConfigurationTypeDef",
    {
        "grants": List["KmsGrantConfigurationTypeDef"],
        "keyPolicies": Dict[str, str],
    },
    total=False,
)

_RequiredListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAccessPreviewFindingsRequestRequestTypeDef(
    _RequiredListAccessPreviewFindingsRequestRequestTypeDef,
    _OptionalListAccessPreviewFindingsRequestRequestTypeDef,
):
    pass

ListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "ListAccessPreviewFindingsResponseTypeDef",
    {
        "findings": List["AccessPreviewFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewsRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAccessPreviewsRequestRequestTypeDef(
    _RequiredListAccessPreviewsRequestRequestTypeDef,
    _OptionalListAccessPreviewsRequestRequestTypeDef,
):
    pass

ListAccessPreviewsResponseTypeDef = TypedDict(
    "ListAccessPreviewsResponseTypeDef",
    {
        "accessPreviews": List["AccessPreviewSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resourceType": ResourceTypeType,
    },
    total=False,
)

class ListAnalyzedResourcesRequestRequestTypeDef(
    _RequiredListAnalyzedResourcesRequestRequestTypeDef,
    _OptionalListAnalyzedResourcesRequestRequestTypeDef,
):
    pass

ListAnalyzedResourcesResponseTypeDef = TypedDict(
    "ListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List["AnalyzedResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnalyzersRequestRequestTypeDef = TypedDict(
    "ListAnalyzersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "type": TypeType,
    },
    total=False,
)

ListAnalyzersResponseTypeDef = TypedDict(
    "ListAnalyzersResponseTypeDef",
    {
        "analyzers": List["AnalyzerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListArchiveRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListArchiveRulesRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalListArchiveRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListArchiveRulesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListArchiveRulesRequestRequestTypeDef(
    _RequiredListArchiveRulesRequestRequestTypeDef, _OptionalListArchiveRulesRequestRequestTypeDef
):
    pass

ListArchiveRulesResponseTypeDef = TypedDict(
    "ListArchiveRulesResponseTypeDef",
    {
        "archiveRules": List["ArchiveRuleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingsRequestRequestTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sort": "SortCriteriaTypeDef",
    },
    total=False,
)

class ListFindingsRequestRequestTypeDef(
    _RequiredListFindingsRequestRequestTypeDef, _OptionalListFindingsRequestRequestTypeDef
):
    pass

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List["FindingSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyGenerationsRequestRequestTypeDef = TypedDict(
    "ListPolicyGenerationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalArn": str,
    },
    total=False,
)

ListPolicyGenerationsResponseTypeDef = TypedDict(
    "ListPolicyGenerationsResponseTypeDef",
    {
        "nextToken": str,
        "policyGenerations": List["PolicyGenerationTypeDef"],
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

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "path": List["PathElementTypeDef"],
        "span": "SpanTypeDef",
    },
)

NetworkOriginConfigurationTypeDef = TypedDict(
    "NetworkOriginConfigurationTypeDef",
    {
        "internetConfiguration": Dict[str, Any],
        "vpcConfiguration": "VpcConfigurationTypeDef",
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

PathElementTypeDef = TypedDict(
    "PathElementTypeDef",
    {
        "index": int,
        "key": str,
        "substring": "SubstringTypeDef",
        "value": str,
    },
    total=False,
)

PolicyGenerationDetailsTypeDef = TypedDict(
    "PolicyGenerationDetailsTypeDef",
    {
        "principalArn": str,
    },
)

_RequiredPolicyGenerationTypeDef = TypedDict(
    "_RequiredPolicyGenerationTypeDef",
    {
        "jobId": str,
        "principalArn": str,
        "startedOn": datetime,
        "status": JobStatusType,
    },
)
_OptionalPolicyGenerationTypeDef = TypedDict(
    "_OptionalPolicyGenerationTypeDef",
    {
        "completedOn": datetime,
    },
    total=False,
)

class PolicyGenerationTypeDef(_RequiredPolicyGenerationTypeDef, _OptionalPolicyGenerationTypeDef):
    pass

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "column": int,
        "line": int,
        "offset": int,
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

S3AccessPointConfigurationTypeDef = TypedDict(
    "S3AccessPointConfigurationTypeDef",
    {
        "accessPointPolicy": str,
        "networkOrigin": "NetworkOriginConfigurationTypeDef",
        "publicAccessBlock": "S3PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

S3BucketAclGrantConfigurationTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationTypeDef",
    {
        "grantee": "AclGranteeTypeDef",
        "permission": AclPermissionType,
    },
)

S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "accessPoints": Dict[str, "S3AccessPointConfigurationTypeDef"],
        "bucketAclGrants": List["S3BucketAclGrantConfigurationTypeDef"],
        "bucketPolicy": str,
        "bucketPublicAccessBlock": "S3PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

S3PublicAccessBlockConfigurationTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)

SecretsManagerSecretConfigurationTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "secretPolicy": str,
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "end": "PositionTypeDef",
        "start": "PositionTypeDef",
    },
)

SqsQueueConfigurationTypeDef = TypedDict(
    "SqsQueueConfigurationTypeDef",
    {
        "queuePolicy": str,
    },
    total=False,
)

_RequiredStartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "_RequiredStartPolicyGenerationRequestRequestTypeDef",
    {
        "policyGenerationDetails": "PolicyGenerationDetailsTypeDef",
    },
)
_OptionalStartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "_OptionalStartPolicyGenerationRequestRequestTypeDef",
    {
        "clientToken": str,
        "cloudTrailDetails": "CloudTrailDetailsTypeDef",
    },
    total=False,
)

class StartPolicyGenerationRequestRequestTypeDef(
    _RequiredStartPolicyGenerationRequestRequestTypeDef,
    _OptionalStartPolicyGenerationRequestRequestTypeDef,
):
    pass

StartPolicyGenerationResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartResourceScanRequestRequestTypeDef = TypedDict(
    "StartResourceScanRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": ReasonCodeType,
    },
)

SubstringTypeDef = TypedDict(
    "SubstringTypeDef",
    {
        "length": int,
        "start": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTrailPropertiesTypeDef = TypedDict(
    "_RequiredTrailPropertiesTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailPropertiesTypeDef = TypedDict(
    "_OptionalTrailPropertiesTypeDef",
    {
        "allRegions": bool,
        "regions": List[str],
    },
    total=False,
)

class TrailPropertiesTypeDef(_RequiredTrailPropertiesTypeDef, _OptionalTrailPropertiesTypeDef):
    pass

_RequiredTrailTypeDef = TypedDict(
    "_RequiredTrailTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailTypeDef = TypedDict(
    "_OptionalTrailTypeDef",
    {
        "allRegions": bool,
        "regions": List[str],
    },
    total=False,
)

class TrailTypeDef(_RequiredTrailTypeDef, _OptionalTrailTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)
_OptionalUpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateArchiveRuleRequestRequestTypeDef(
    _RequiredUpdateArchiveRuleRequestRequestTypeDef, _OptionalUpdateArchiveRuleRequestRequestTypeDef
):
    pass

_RequiredUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "status": FindingStatusUpdateType,
    },
)
_OptionalUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "ids": List[str],
        "resourceArn": str,
    },
    total=False,
)

class UpdateFindingsRequestRequestTypeDef(
    _RequiredUpdateFindingsRequestRequestTypeDef, _OptionalUpdateFindingsRequestRequestTypeDef
):
    pass

ValidatePolicyFindingTypeDef = TypedDict(
    "ValidatePolicyFindingTypeDef",
    {
        "findingDetails": str,
        "findingType": ValidatePolicyFindingTypeType,
        "issueCode": str,
        "learnMoreLink": str,
        "locations": List["LocationTypeDef"],
    },
)

_RequiredValidatePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredValidatePolicyRequestRequestTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
    },
)
_OptionalValidatePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalValidatePolicyRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ValidatePolicyRequestRequestTypeDef(
    _RequiredValidatePolicyRequestRequestTypeDef, _OptionalValidatePolicyRequestRequestTypeDef
):
    pass

ValidatePolicyResponseTypeDef = TypedDict(
    "ValidatePolicyResponseTypeDef",
    {
        "findings": List["ValidatePolicyFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)
