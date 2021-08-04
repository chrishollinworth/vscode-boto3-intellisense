"""
Type annotations for dataexchange service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/literals.html)

Usage::

    ```python
    from mypy_boto3_dataexchange.literals import AssetTypeType

    data: AssetTypeType = "S3_SNAPSHOT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssetTypeType",
    "CodeType",
    "JobErrorLimitNameType",
    "JobErrorResourceTypesType",
    "ListDataSetRevisionsPaginatorName",
    "ListDataSetsPaginatorName",
    "ListJobsPaginatorName",
    "ListRevisionAssetsPaginatorName",
    "OriginType",
    "ServerSideEncryptionTypesType",
    "StateType",
    "TypeType",
)

AssetTypeType = Literal["S3_SNAPSHOT"]
CodeType = Literal[
    "ACCESS_DENIED_EXCEPTION",
    "INTERNAL_SERVER_EXCEPTION",
    "MALWARE_DETECTED",
    "MALWARE_SCAN_ENCRYPTED_FILE",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
    "VALIDATION_EXCEPTION",
]
JobErrorLimitNameType = Literal["Asset size in GB", "Assets per revision"]
JobErrorResourceTypesType = Literal["ASSET", "REVISION"]
ListDataSetRevisionsPaginatorName = Literal["list_data_set_revisions"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListJobsPaginatorName = Literal["list_jobs"]
ListRevisionAssetsPaginatorName = Literal["list_revision_assets"]
OriginType = Literal["ENTITLED", "OWNED"]
ServerSideEncryptionTypesType = Literal["AES256", "aws:kms"]
StateType = Literal["CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "TIMED_OUT", "WAITING"]
TypeType = Literal[
    "EXPORT_ASSETS_TO_S3",
    "EXPORT_ASSET_TO_SIGNED_URL",
    "EXPORT_REVISIONS_TO_S3",
    "IMPORT_ASSETS_FROM_S3",
    "IMPORT_ASSET_FROM_SIGNED_URL",
]
