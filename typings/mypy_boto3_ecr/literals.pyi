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
    "ScanStatusType",
    "TagStatusType",
)

DescribeImageScanFindingsPaginatorName = Literal["describe_image_scan_findings"]
DescribeImagesPaginatorName = Literal["describe_images"]
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
]
ImageScanCompleteWaiterName = Literal["image_scan_complete"]
ImageTagMutabilityType = Literal["IMMUTABLE", "MUTABLE"]
LayerAvailabilityType = Literal["AVAILABLE", "UNAVAILABLE"]
LayerFailureCodeType = Literal["InvalidLayerDigest", "MissingLayerDigest"]
LifecyclePolicyPreviewCompleteWaiterName = Literal["lifecycle_policy_preview_complete"]
LifecyclePolicyPreviewStatusType = Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"]
ListImagesPaginatorName = Literal["list_images"]
ScanStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
TagStatusType = Literal["ANY", "TAGGED", "UNTAGGED"]
