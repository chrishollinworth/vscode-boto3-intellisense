"""
Main interface for ecr service type definitions.

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

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
    "EncryptionConfigurationTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryTypeDef",
    "TagTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageResponseTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartImageScanResponseTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "UploadLayerPartResponseTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"key": str})
_OptionalAttributeTypeDef = TypedDict("_OptionalAttributeTypeDef", {"value": str}, total=False)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {"authorizationToken": str, "expiresAt": datetime, "proxyEndpoint": str},
    total=False,
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef", {"encryptionType": Literal["AES256", "KMS"]}
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef", {"kmsKey": str}, total=False
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


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
        "failureCode": Literal[
            "InvalidImageDigest",
            "InvalidImageTag",
            "ImageTagDoesNotMatchDigest",
            "ImageNotFound",
            "MissingDigestAndTag",
            "ImageReferencedByManifestList",
            "KmsError",
        ],
        "failureReason": str,
    },
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"],
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[
            Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"], int
        ],
    },
    total=False,
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List["ImageScanFindingTypeDef"],
        "findingSeverityCounts": Dict[
            Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"], int
        ],
    },
    total=False,
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef", {"scanOnPush": bool}, total=False
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

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": str,
        "failureCode": Literal["InvalidLayerDigest", "MissingLayerDigest"],
        "failureReason": str,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": Literal["AVAILABLE", "UNAVAILABLE"],
        "layerSize": int,
        "mediaType": str,
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
    "LifecyclePolicyPreviewSummaryTypeDef", {"expiringImageTotalCount": int}, total=False
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef", {"type": Literal["EXPIRE"]}, total=False
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef", {"rules": List["ReplicationRuleTypeDef"]}
)

ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef", {"region": str, "registryId": str}
)

ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef", {"destinations": List["ReplicationDestinationTypeDef"]}
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {"layers": List["LayerTypeDef"], "failures": List["LayerFailureTypeDef"]},
    total=False,
)

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {"imageIds": List["ImageIdentifierTypeDef"], "failures": List["ImageFailureTypeDef"]},
    total=False,
)

BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {"images": List["ImageTypeDef"], "failures": List["ImageFailureTypeDef"]},
    total=False,
)

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "layerDigest": str},
    total=False,
)

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef", {"repository": "RepositoryTypeDef"}, total=False
)

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef", {"registryId": str, "policyText": str}, total=False
)

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef", {"repository": "RepositoryTypeDef"}, total=False
)

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindings": "ImageScanFindingsTypeDef",
        "nextToken": str,
    },
    total=False,
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef", {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]}, total=False
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {"imageDetails": List["ImageDetailTypeDef"], "nextToken": str},
    total=False,
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {"registryId": str, "replicationConfiguration": "ReplicationConfigurationTypeDef"},
    total=False,
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {"repositories": List["RepositoryTypeDef"], "nextToken": str},
    total=False,
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {"authorizationData": List["AuthorizationDataTypeDef"]},
    total=False,
)

GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef", {"downloadUrl": str, "layerDigest": str}, total=False
)

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
        "nextToken": str,
        "previewResults": List["LifecyclePolicyPreviewResultTypeDef"],
        "summary": "LifecyclePolicyPreviewSummaryTypeDef",
    },
    total=False,
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef", {"registryId": str, "policyText": str}, total=False
)

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef", {"uploadId": str, "partSize": int}, total=False
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef", {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]}, total=False
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {"imageIds": List["ImageIdentifierTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef", {"image": "ImageTypeDef"}, total=False
)

PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
    },
    total=False,
)

PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
    },
    total=False,
)

PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "lifecyclePolicyText": str},
    total=False,
)

PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef", {"registryId": str, "policyText": str}, total=False
)

PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {"replicationConfiguration": "ReplicationConfigurationTypeDef"},
    total=False,
)

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
    },
    total=False,
)

StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
    },
    total=False,
)

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "lastByteReceived": int},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
