"""
Type annotations for ecr service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/literals.html)

Usage::

    ```python
    from mypy_boto3_ecr.literals import DescribeImageScanFindingsPaginatorName

    data: DescribeImageScanFindingsPaginatorName = "describe_image_scan_findings"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeImageScanFindingsPaginatorName",
    "DescribeImagesPaginatorName",
    "DescribePullThroughCacheRulesPaginatorName",
    "DescribeRepositoriesPaginatorName",
    "EncryptionTypeType",
    "FindingSeverityType",
    "GetLifecyclePolicyPreviewPaginatorName",
    "ImageActionTypeType",
    "ImageFailureCodeType",
    "ImageScanCompleteWaiterName",
    "ImageTagMutabilityType",
    "LayerAvailabilityType",
    "LayerFailureCodeType",
    "LifecyclePolicyPreviewCompleteWaiterName",
    "LifecyclePolicyPreviewStatusType",
    "ListImagesPaginatorName",
    "ReplicationStatusType",
    "RepositoryFilterTypeType",
    "ScanFrequencyType",
    "ScanStatusType",
    "ScanTypeType",
    "ScanningConfigurationFailureCodeType",
    "ScanningRepositoryFilterTypeType",
    "TagStatusType",
    "UpstreamRegistryType",
)

DescribeImageScanFindingsPaginatorName = Literal["describe_image_scan_findings"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribePullThroughCacheRulesPaginatorName = Literal["describe_pull_through_cache_rules"]
DescribeRepositoriesPaginatorName = Literal["describe_repositories"]
EncryptionTypeType = Literal["AES256", "KMS"]
FindingSeverityType = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNDEFINED"]
GetLifecyclePolicyPreviewPaginatorName = Literal["get_lifecycle_policy_preview"]
ImageActionTypeType = Literal["EXPIRE"]
ImageFailureCodeType = Literal[
    "ImageNotFound",
    "ImageReferencedByManifestList",
    "ImageTagDoesNotMatchDigest",
    "InvalidImageDigest",
    "InvalidImageTag",
    "KmsError",
    "MissingDigestAndTag",
    "UpstreamAccessDenied",
    "UpstreamTooManyRequests",
    "UpstreamUnavailable",
]
ImageScanCompleteWaiterName = Literal["image_scan_complete"]
ImageTagMutabilityType = Literal["IMMUTABLE", "MUTABLE"]
LayerAvailabilityType = Literal["AVAILABLE", "UNAVAILABLE"]
LayerFailureCodeType = Literal["InvalidLayerDigest", "MissingLayerDigest"]
LifecyclePolicyPreviewCompleteWaiterName = Literal["lifecycle_policy_preview_complete"]
LifecyclePolicyPreviewStatusType = Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"]
ListImagesPaginatorName = Literal["list_images"]
ReplicationStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
RepositoryFilterTypeType = Literal["PREFIX_MATCH"]
ScanFrequencyType = Literal["CONTINUOUS_SCAN", "MANUAL", "SCAN_ON_PUSH"]
ScanStatusType = Literal[
    "ACTIVE",
    "COMPLETE",
    "FAILED",
    "FINDINGS_UNAVAILABLE",
    "IN_PROGRESS",
    "PENDING",
    "SCAN_ELIGIBILITY_EXPIRED",
    "UNSUPPORTED_IMAGE",
]
ScanTypeType = Literal["BASIC", "ENHANCED"]
ScanningConfigurationFailureCodeType = Literal["REPOSITORY_NOT_FOUND"]
ScanningRepositoryFilterTypeType = Literal["WILDCARD"]
TagStatusType = Literal["ANY", "TAGGED", "UNTAGGED"]
UpstreamRegistryType = Literal[
    "azure-container-registry",
    "docker-hub",
    "ecr-public",
    "github-container-registry",
    "k8s",
    "quay",
]
