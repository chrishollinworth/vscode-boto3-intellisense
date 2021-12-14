"""
Type annotations for ecr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionTypeType,
    FindingSeverityType,
    ImageFailureCodeType,
    ImageTagMutabilityType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    LifecyclePolicyPreviewStatusType,
    ReplicationStatusType,
    ScanFrequencyType,
    ScanStatusType,
    ScanTypeType,
    TagStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageRequestRequestTypeDef",
    "BatchGetImageResponseTypeDef",
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    "CreatePullThroughCacheRuleResponseTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResponseTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    "DeletePullThroughCacheRuleResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    "DescribeImageReplicationStatusResponseTypeDef",
    "DescribeImageScanFindingsRequestRequestTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    "DescribePullThroughCacheRulesResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "EnhancedImageScanFindingTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRegistryScanningConfigurationResponseTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageReplicationStatusTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PullThroughCacheRuleTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageResponseTypeDef",
    "PutImageScanningConfigurationRequestRequestTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "PutImageTagMutabilityRequestRequestTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyRequestRequestTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyRequestRequestTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    "PutRegistryScanningConfigurationResponseTypeDef",
    "PutReplicationConfigurationRequestRequestTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "RecommendationTypeDef",
    "RegistryScanningConfigurationTypeDef",
    "RegistryScanningRuleTypeDef",
    "RemediationTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryFilterTypeDef",
    "RepositoryScanningConfigurationFailureTypeDef",
    "RepositoryScanningConfigurationTypeDef",
    "RepositoryTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanningRepositoryFilterTypeDef",
    "ScoreDetailsTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartImageScanRequestRequestTypeDef",
    "StartImageScanResponseTypeDef",
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "UploadLayerPartResponseTypeDef",
    "VulnerablePackageTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "key": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
        "proxyEndpoint": str,
    },
    total=False,
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "architecture": str,
        "author": str,
        "imageHash": str,
        "imageTags": List[str],
        "platform": str,
        "pushedAt": datetime,
        "registry": str,
        "repositoryName": str,
    },
    total=False,
)

_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": List[str],
    },
)
_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchCheckLayerAvailabilityRequestRequestTypeDef(
    _RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef,
    _OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef,
):
    pass

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": List["ImageIdentifierTypeDef"],
    },
)
_OptionalBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteImageRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchDeleteImageRequestRequestTypeDef(
    _RequiredBatchDeleteImageRequestRequestTypeDef, _OptionalBatchDeleteImageRequestRequestTypeDef
):
    pass

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetImageRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": List["ImageIdentifierTypeDef"],
    },
)
_OptionalBatchGetImageRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetImageRequestRequestTypeDef",
    {
        "registryId": str,
        "acceptedMediaTypes": List[str],
    },
    total=False,
)

class BatchGetImageRequestRequestTypeDef(
    _RequiredBatchGetImageRequestRequestTypeDef, _OptionalBatchGetImageRequestRequestTypeDef
):
    pass

BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {
        "images": List["ImageTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryNames": List[str],
    },
)

BatchGetRepositoryScanningConfigurationResponseTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    {
        "scanningConfigurations": List["RepositoryScanningConfigurationTypeDef"],
        "failures": List["RepositoryScanningConfigurationFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": List[str],
    },
)
_OptionalCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCompleteLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class CompleteLayerUploadRequestRequestTypeDef(
    _RequiredCompleteLayerUploadRequestRequestTypeDef,
    _OptionalCompleteLayerUploadRequestRequestTypeDef,
):
    pass

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
    },
)
_OptionalCreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class CreatePullThroughCacheRuleRequestRequestTypeDef(
    _RequiredCreatePullThroughCacheRuleRequestRequestTypeDef,
    _OptionalCreatePullThroughCacheRuleRequestRequestTypeDef,
):
    pass

CreatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "CreatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestRequestTypeDef",
    {
        "registryId": str,
        "tags": List["TagTypeDef"],
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

class CreateRepositoryRequestRequestTypeDef(
    _RequiredCreateRepositoryRequestRequestTypeDef, _OptionalCreateRepositoryRequestRequestTypeDef
):
    pass

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
    total=False,
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "adjustments": List["CvssScoreAdjustmentTypeDef"],
        "score": float,
        "scoreSource": str,
        "scoringVector": str,
        "version": str,
    },
    total=False,
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "source": str,
        "version": str,
    },
    total=False,
)

_RequiredDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeleteLifecyclePolicyRequestRequestTypeDef(
    _RequiredDeleteLifecyclePolicyRequestRequestTypeDef,
    _OptionalDeleteLifecyclePolicyRequestRequestTypeDef,
):
    pass

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
    },
)
_OptionalDeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeletePullThroughCacheRuleRequestRequestTypeDef(
    _RequiredDeletePullThroughCacheRuleRequestRequestTypeDef,
    _OptionalDeletePullThroughCacheRuleRequestRequestTypeDef,
):
    pass

DeletePullThroughCacheRuleResponseTypeDef = TypedDict(
    "DeletePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeleteRepositoryPolicyRequestRequestTypeDef(
    _RequiredDeleteRepositoryPolicyRequestRequestTypeDef,
    _OptionalDeleteRepositoryPolicyRequestRequestTypeDef,
):
    pass

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class DeleteRepositoryRequestRequestTypeDef(
    _RequiredDeleteRepositoryRequestRequestTypeDef, _OptionalDeleteRepositoryRequestRequestTypeDef
):
    pass

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
    },
)
_OptionalDescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DescribeImageReplicationStatusRequestRequestTypeDef(
    _RequiredDescribeImageReplicationStatusRequestRequestTypeDef,
    _OptionalDescribeImageReplicationStatusRequestRequestTypeDef,
):
    pass

DescribeImageReplicationStatusResponseTypeDef = TypedDict(
    "DescribeImageReplicationStatusResponseTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "replicationStatuses": List["ImageReplicationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageScanFindingsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
    },
)
_OptionalDescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageScanFindingsRequestRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeImageScanFindingsRequestRequestTypeDef(
    _RequiredDescribeImageScanFindingsRequestRequestTypeDef,
    _OptionalDescribeImageScanFindingsRequestRequestTypeDef,
):
    pass

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindings": "ImageScanFindingsTypeDef",
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

_RequiredDescribeImagesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImagesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImagesRequestRequestTypeDef",
    {
        "registryId": str,
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "filter": "DescribeImagesFilterTypeDef",
    },
    total=False,
)

class DescribeImagesRequestRequestTypeDef(
    _RequiredDescribeImagesRequestRequestTypeDef, _OptionalDescribeImagesRequestRequestTypeDef
):
    pass

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePullThroughCacheRulesRequestRequestTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    {
        "registryId": str,
        "ecrRepositoryPrefixes": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribePullThroughCacheRulesResponseTypeDef = TypedDict(
    "DescribePullThroughCacheRulesResponseTypeDef",
    {
        "pullThroughCacheRules": List["PullThroughCacheRuleTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": str,
        "repositoryNames": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "kmsKey": str,
    },
    total=False,
)

class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass

EnhancedImageScanFindingTypeDef = TypedDict(
    "EnhancedImageScanFindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "packageVulnerabilityDetails": "PackageVulnerabilityDetailsTypeDef",
        "remediation": "RemediationTypeDef",
        "resources": List["ResourceTypeDef"],
        "score": float,
        "scoreDetails": "ScoreDetailsTypeDef",
        "severity": str,
        "status": str,
        "title": str,
        "type": str,
        "updatedAt": datetime,
    },
    total=False,
)

GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "registryIds": List[str],
    },
    total=False,
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List["AuthorizationDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "_RequiredGetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigest": str,
    },
)
_OptionalGetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "_OptionalGetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetDownloadUrlForLayerRequestRequestTypeDef(
    _RequiredGetDownloadUrlForLayerRequestRequestTypeDef,
    _OptionalGetDownloadUrlForLayerRequestRequestTypeDef,
):
    pass

GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "registryId": str,
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "filter": "LifecyclePolicyPreviewFilterTypeDef",
    },
    total=False,
)

class GetLifecyclePolicyPreviewRequestRequestTypeDef(
    _RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef,
    _OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef,
):
    pass

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List["LifecyclePolicyPreviewResultTypeDef"],
        "summary": "LifecyclePolicyPreviewSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetLifecyclePolicyRequestRequestTypeDef(
    _RequiredGetLifecyclePolicyRequestRequestTypeDef,
    _OptionalGetLifecyclePolicyRequestRequestTypeDef,
):
    pass

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "GetRegistryScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "scanningConfiguration": "RegistryScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetRepositoryPolicyRequestRequestTypeDef(
    _RequiredGetRepositoryPolicyRequestRequestTypeDef,
    _OptionalGetRepositoryPolicyRequestRequestTypeDef,
):
    pass

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindingsSummary": "ImageScanFindingsSummaryTypeDef",
        "imageManifestMediaType": str,
        "artifactMediaType": str,
    },
    total=False,
)

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": "ImageIdentifierTypeDef",
        "failureCode": ImageFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": str,
        "imageTag": str,
    },
    total=False,
)

ImageReplicationStatusTypeDef = TypedDict(
    "ImageReplicationStatusTypeDef",
    {
        "region": str,
        "registryId": str,
        "status": ReplicationStatusType,
        "failureCode": str,
    },
    total=False,
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": FindingSeverityType,
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[FindingSeverityType, int],
    },
    total=False,
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[FindingSeverityType, int],
        "findings": List["ImageScanFindingTypeDef"],
        "enhancedFindings": List["EnhancedImageScanFindingTypeDef"],
    },
    total=False,
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {
        "status": ScanStatusType,
        "description": str,
    },
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "scanOnPush": bool,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageManifest": str,
        "imageManifestMediaType": str,
    },
    total=False,
)

_RequiredInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredInitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalInitiateLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class InitiateLayerUploadRequestRequestTypeDef(
    _RequiredInitiateLayerUploadRequestRequestTypeDef,
    _OptionalInitiateLayerUploadRequestRequestTypeDef,
):
    pass

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": str,
        "failureCode": LayerFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": LayerAvailabilityType,
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": "LifecyclePolicyRuleActionTypeDef",
        "appliedRulePriority": int,
    },
    total=False,
)

LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef",
    {
        "expiringImageTotalCount": int,
    },
    total=False,
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef",
    {
        "type": Literal["EXPIRE"],
    },
    total=False,
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

_RequiredListImagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListImagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagesRequestRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
        "filter": "ListImagesFilterTypeDef",
    },
    total=False,
)

class ListImagesRequestRequestTypeDef(
    _RequiredListImagesRequestRequestTypeDef, _OptionalListImagesRequestRequestTypeDef
):
    pass

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "cvss": List["CvssScoreTypeDef"],
        "referenceUrls": List[str],
        "relatedVulnerabilities": List[str],
        "source": str,
        "sourceUrl": str,
        "vendorCreatedAt": datetime,
        "vendorSeverity": str,
        "vendorUpdatedAt": datetime,
        "vulnerabilityId": str,
        "vulnerablePackages": List["VulnerablePackageTypeDef"],
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

PullThroughCacheRuleTypeDef = TypedDict(
    "PullThroughCacheRuleTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
    },
    total=False,
)

_RequiredPutImageRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
    },
)
_OptionalPutImageRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageRequestRequestTypeDef",
    {
        "registryId": str,
        "imageManifestMediaType": str,
        "imageTag": str,
        "imageDigest": str,
    },
    total=False,
)

class PutImageRequestRequestTypeDef(
    _RequiredPutImageRequestRequestTypeDef, _OptionalPutImageRequestRequestTypeDef
):
    pass

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
    },
)
_OptionalPutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageScanningConfigurationRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutImageScanningConfigurationRequestRequestTypeDef(
    _RequiredPutImageScanningConfigurationRequestRequestTypeDef,
    _OptionalPutImageScanningConfigurationRequestRequestTypeDef,
):
    pass

PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageTagMutabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
    },
)
_OptionalPutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageTagMutabilityRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutImageTagMutabilityRequestRequestTypeDef(
    _RequiredPutImageTagMutabilityRequestRequestTypeDef,
    _OptionalPutImageTagMutabilityRequestRequestTypeDef,
):
    pass

PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "lifecyclePolicyText": str,
    },
)
_OptionalPutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutLifecyclePolicyRequestRequestTypeDef(
    _RequiredPutLifecyclePolicyRequestRequestTypeDef,
    _OptionalPutLifecyclePolicyRequestRequestTypeDef,
):
    pass

PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryPolicyRequestRequestTypeDef = TypedDict(
    "PutRegistryPolicyRequestRequestTypeDef",
    {
        "policyText": str,
    },
)

PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    {
        "scanType": ScanTypeType,
        "rules": List["RegistryScanningRuleTypeDef"],
    },
    total=False,
)

PutRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "PutRegistryScanningConfigurationResponseTypeDef",
    {
        "registryScanningConfiguration": "RegistryScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutReplicationConfigurationRequestRequestTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)

PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "url": str,
        "text": str,
    },
    total=False,
)

RegistryScanningConfigurationTypeDef = TypedDict(
    "RegistryScanningConfigurationTypeDef",
    {
        "scanType": ScanTypeType,
        "rules": List["RegistryScanningRuleTypeDef"],
    },
    total=False,
)

RegistryScanningRuleTypeDef = TypedDict(
    "RegistryScanningRuleTypeDef",
    {
        "scanFrequency": ScanFrequencyType,
        "repositoryFilters": List["ScanningRepositoryFilterTypeDef"],
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": "RecommendationTypeDef",
    },
    total=False,
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {
        "destinations": List["ReplicationDestinationTypeDef"],
    },
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "repositoryFilters": List["RepositoryFilterTypeDef"],
    },
    total=False,
)

class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass

RepositoryFilterTypeDef = TypedDict(
    "RepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["PREFIX_MATCH"],
    },
)

RepositoryScanningConfigurationFailureTypeDef = TypedDict(
    "RepositoryScanningConfigurationFailureTypeDef",
    {
        "repositoryName": str,
        "failureCode": Literal["REPOSITORY_NOT_FOUND"],
        "failureReason": str,
    },
    total=False,
)

RepositoryScanningConfigurationTypeDef = TypedDict(
    "RepositoryScanningConfigurationTypeDef",
    {
        "repositoryArn": str,
        "repositoryName": str,
        "scanOnPush": bool,
        "scanFrequency": ScanFrequencyType,
        "appliedScanFilters": List["ScanningRepositoryFilterTypeDef"],
    },
    total=False,
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEcrContainerImage": "AwsEcrContainerImageDetailsTypeDef",
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "details": "ResourceDetailsTypeDef",
        "id": str,
        "tags": Dict[str, str],
        "type": str,
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

ScanningRepositoryFilterTypeDef = TypedDict(
    "ScanningRepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["WILDCARD"],
    },
)

ScoreDetailsTypeDef = TypedDict(
    "ScoreDetailsTypeDef",
    {
        "cvss": "CvssScoreDetailsTypeDef",
    },
    total=False,
)

_RequiredSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredSetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
    },
)
_OptionalSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalSetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class SetRepositoryPolicyRequestRequestTypeDef(
    _RequiredSetRepositoryPolicyRequestRequestTypeDef,
    _OptionalSetRepositoryPolicyRequestRequestTypeDef,
):
    pass

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImageScanRequestRequestTypeDef = TypedDict(
    "_RequiredStartImageScanRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
    },
)
_OptionalStartImageScanRequestRequestTypeDef = TypedDict(
    "_OptionalStartImageScanRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class StartImageScanRequestRequestTypeDef(
    _RequiredStartImageScanRequestRequestTypeDef, _OptionalStartImageScanRequestRequestTypeDef
):
    pass

StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "registryId": str,
        "lifecyclePolicyText": str,
    },
    total=False,
)

class StartLifecyclePolicyPreviewRequestRequestTypeDef(
    _RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef,
    _OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef,
):
    pass

StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_RequiredUploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_OptionalUploadLayerPartRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class UploadLayerPartRequestRequestTypeDef(
    _RequiredUploadLayerPartRequestRequestTypeDef, _OptionalUploadLayerPartRequestRequestTypeDef
):
    pass

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "arch": str,
        "epoch": int,
        "filePath": str,
        "name": str,
        "packageManager": str,
        "release": str,
        "sourceLayerHash": str,
        "version": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
