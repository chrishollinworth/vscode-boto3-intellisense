"""
Type annotations for storagegateway service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/literals.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.literals import ActiveDirectoryStatusType

    data: ActiveDirectoryStatusType = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActiveDirectoryStatusType",
    "AvailabilityMonitorTestStatusType",
    "CaseSensitivityType",
    "DescribeTapeArchivesPaginatorName",
    "DescribeTapeRecoveryPointsPaginatorName",
    "DescribeTapesPaginatorName",
    "DescribeVTLDevicesPaginatorName",
    "FileShareTypeType",
    "GatewayCapacityType",
    "HostEnvironmentType",
    "ListFileSharesPaginatorName",
    "ListFileSystemAssociationsPaginatorName",
    "ListGatewaysPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTapePoolsPaginatorName",
    "ListTapesPaginatorName",
    "ListVolumesPaginatorName",
    "ObjectACLType",
    "PoolStatusType",
    "RetentionLockTypeType",
    "SMBSecurityStrategyType",
    "TapeStorageClassType",
)

ActiveDirectoryStatusType = Literal[
    "ACCESS_DENIED", "DETACHED", "JOINED", "JOINING", "NETWORK_ERROR", "TIMEOUT", "UNKNOWN_ERROR"
]
AvailabilityMonitorTestStatusType = Literal["COMPLETE", "FAILED", "PENDING"]
CaseSensitivityType = Literal["CaseSensitive", "ClientSpecified"]
DescribeTapeArchivesPaginatorName = Literal["describe_tape_archives"]
DescribeTapeRecoveryPointsPaginatorName = Literal["describe_tape_recovery_points"]
DescribeTapesPaginatorName = Literal["describe_tapes"]
DescribeVTLDevicesPaginatorName = Literal["describe_vtl_devices"]
FileShareTypeType = Literal["NFS", "SMB"]
GatewayCapacityType = Literal["Large", "Medium", "Small"]
HostEnvironmentType = Literal["EC2", "HYPER-V", "KVM", "OTHER", "VMWARE"]
ListFileSharesPaginatorName = Literal["list_file_shares"]
ListFileSystemAssociationsPaginatorName = Literal["list_file_system_associations"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTapePoolsPaginatorName = Literal["list_tape_pools"]
ListTapesPaginatorName = Literal["list_tapes"]
ListVolumesPaginatorName = Literal["list_volumes"]
ObjectACLType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
PoolStatusType = Literal["ACTIVE", "DELETED"]
RetentionLockTypeType = Literal["COMPLIANCE", "GOVERNANCE", "NONE"]
SMBSecurityStrategyType = Literal["ClientSpecified", "MandatoryEncryption", "MandatorySigning"]
TapeStorageClassType = Literal["DEEP_ARCHIVE", "GLACIER"]
