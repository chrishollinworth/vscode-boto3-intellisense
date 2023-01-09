"""
Type annotations for dataexchange service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/literals.html)

Usage::

    ```python
    from mypy_boto3_dataexchange.literals import AssetTypeType

    data: AssetTypeType = "API_GATEWAY_API"
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
    "DatabaseLFTagPolicyPermissionType",
    "JobErrorLimitNameType",
    "JobErrorResourceTypesType",
    "LFPermissionType",
    "LFResourceTypeType",
    "LakeFormationDataPermissionTypeType",
    "ListDataSetRevisionsPaginatorName",
    "ListDataSetsPaginatorName",
    "ListEventActionsPaginatorName",
    "ListJobsPaginatorName",
    "ListRevisionAssetsPaginatorName",
    "OriginType",
    "ProtocolTypeType",
    "ServerSideEncryptionTypesType",
    "StateType",
    "TableTagPolicyLFPermissionType",
    "TypeType",
)

AssetTypeType = Literal[
    "API_GATEWAY_API",
    "LAKE_FORMATION_DATA_PERMISSION",
    "REDSHIFT_DATA_SHARE",
    "S3_DATA_ACCESS",
    "S3_SNAPSHOT",
]
CodeType = Literal[
    "ACCESS_DENIED_EXCEPTION",
    "INTERNAL_SERVER_EXCEPTION",
    "MALWARE_DETECTED",
    "MALWARE_SCAN_ENCRYPTED_FILE",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
    "VALIDATION_EXCEPTION",
]
DatabaseLFTagPolicyPermissionType = Literal["DESCRIBE"]
JobErrorLimitNameType = Literal[
    "AWS Lake Formation data permission assets per revision",
    "Amazon Redshift datashare assets per revision",
    "Amazon S3 data access assets per revision",
    "Asset size in GB",
    "Assets per revision",
]
JobErrorResourceTypesType = Literal["ASSET", "DATA_SET", "REVISION"]
LFPermissionType = Literal["DESCRIBE", "SELECT"]
LFResourceTypeType = Literal["DATABASE", "TABLE"]
LakeFormationDataPermissionTypeType = Literal["LFTagPolicy"]
ListDataSetRevisionsPaginatorName = Literal["list_data_set_revisions"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListEventActionsPaginatorName = Literal["list_event_actions"]
ListJobsPaginatorName = Literal["list_jobs"]
ListRevisionAssetsPaginatorName = Literal["list_revision_assets"]
OriginType = Literal["ENTITLED", "OWNED"]
ProtocolTypeType = Literal["REST"]
ServerSideEncryptionTypesType = Literal["AES256", "aws:kms"]
StateType = Literal["CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "TIMED_OUT", "WAITING"]
TableTagPolicyLFPermissionType = Literal["DESCRIBE", "SELECT"]
TypeType = Literal[
    "CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET",
    "EXPORT_ASSETS_TO_S3",
    "EXPORT_ASSET_TO_SIGNED_URL",
    "EXPORT_REVISIONS_TO_S3",
    "IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY",
    "IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES",
    "IMPORT_ASSETS_FROM_S3",
    "IMPORT_ASSET_FROM_API_GATEWAY_API",
    "IMPORT_ASSET_FROM_SIGNED_URL",
]
