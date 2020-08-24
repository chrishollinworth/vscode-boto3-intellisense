"""
Main interface for storagegateway service type definitions.

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import AutomaticTapeCreationPolicyInfoTypeDef

    data: AutomaticTapeCreationPolicyInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "ChapInfoTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DiskTypeDef",
    "FileShareInfoTypeDef",
    "GatewayInfoTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "PoolInfoTypeDef",
    "SMBFileShareInfoTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
    "ActivateGatewayOutputTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AttachVolumeOutputTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalOutputTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeOutputTypeDef",
    "DisableGatewayOutputTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesOutputTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheOutputTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayOutputTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
)

AutomaticTapeCreationPolicyInfoTypeDef = TypedDict(
    "AutomaticTapeCreationPolicyInfoTypeDef",
    {"AutomaticTapeCreationRules": List["AutomaticTapeCreationRuleTypeDef"], "GatewayARN": str},
    total=False,
)

_RequiredAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_RequiredAutomaticTapeCreationRuleTypeDef",
    {"TapeBarcodePrefix": str, "PoolId": str, "TapeSizeInBytes": int, "MinimumNumTapes": int},
)
_OptionalAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_OptionalAutomaticTapeCreationRuleTypeDef", {"Worm": bool}, total=False
)


class AutomaticTapeCreationRuleTypeDef(
    _RequiredAutomaticTapeCreationRuleTypeDef, _OptionalAutomaticTapeCreationRuleTypeDef
):
    pass


CacheAttributesTypeDef = TypedDict(
    "CacheAttributesTypeDef", {"CacheStaleTimeoutInSeconds": int}, total=False
)

CachediSCSIVolumeTypeDef = TypedDict(
    "CachediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

ChapInfoTypeDef = TypedDict(
    "ChapInfoTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)

DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {"TargetARN": str, "NetworkInterfaceId": str, "NetworkInterfacePort": int, "ChapEnabled": bool},
    total=False,
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)

FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": Literal["NFS", "SMB"],
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)

NFSFileShareDefaultsTypeDef = TypedDict(
    "NFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)

NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {"Ipv4Address": str, "MacAddress": str, "Ipv6Address": str},
    total=False,
)

PoolInfoTypeDef = TypedDict(
    "PoolInfoTypeDef",
    {
        "PoolARN": str,
        "PoolName": str,
        "StorageClass": Literal["DEEP_ARCHIVE", "GLACIER"],
        "RetentionLockType": Literal["COMPLIANCE", "GOVERNANCE", "NONE"],
        "RetentionLockTimeInDays": int,
        "PoolStatus": Literal["ACTIVE", "DELETED"],
    },
    total=False,
)

SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "Authentication": str,
        "CaseSensitivity": Literal["ClientSpecified", "CaseSensitive"],
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)

StorediSCSIVolumeTypeDef = TypedDict(
    "StorediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {"TapeARN": str, "TapeRecoveryPointTime": datetime, "TapeSizeInBytes": int, "TapeStatus": str},
    total=False,
)

TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": "DeviceiSCSIAttributesTypeDef",
    },
    total=False,
)

VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)

VolumeRecoveryPointInfoTypeDef = TypedDict(
    "VolumeRecoveryPointInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)

VolumeiSCSIAttributesTypeDef = TypedDict(
    "VolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)

ActivateGatewayOutputTypeDef = TypedDict(
    "ActivateGatewayOutputTypeDef", {"GatewayARN": str}, total=False
)

AddCacheOutputTypeDef = TypedDict("AddCacheOutputTypeDef", {"GatewayARN": str}, total=False)

AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef", {"ResourceARN": str}, total=False
)

AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef", {"GatewayARN": str}, total=False
)

AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef", {"GatewayARN": str}, total=False
)

AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef", {"TapeARN": str}, total=False
)

AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef", {"VolumeARN": str, "TargetARN": str}, total=False
)

CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef", {"TapeARN": str}, total=False
)

CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef", {"TapeARN": str}, total=False
)

CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef", {"VolumeARN": str, "TargetARN": str}, total=False
)

CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef", {"FileShareARN": str}, total=False
)

CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef", {"FileShareARN": str}, total=False
)

CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {"SnapshotId": str, "VolumeARN": str, "VolumeRecoveryPointTime": str},
    total=False,
)

CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef", {"VolumeARN": str, "SnapshotId": str}, total=False
)

CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {"VolumeARN": str, "VolumeSizeInBytes": int, "TargetARN": str},
    total=False,
)

CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef", {"PoolARN": str}, total=False
)

CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef", {"TapeARN": str}, total=False
)

CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef", {"TapeARNs": List[str]}, total=False
)

DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef", {"GatewayARN": str}, total=False
)

DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef", {"GatewayARN": str}, total=False
)

DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef", {"TargetARN": str, "InitiatorName": str}, total=False
)

DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef", {"FileShareARN": str}, total=False
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef", {"GatewayARN": str}, total=False
)

DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef", {"VolumeARN": str}, total=False
)

DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef", {"TapeARN": str}, total=False
)

DeleteTapeOutputTypeDef = TypedDict("DeleteTapeOutputTypeDef", {"TapeARN": str}, total=False)

DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef", {"PoolARN": str}, total=False
)

DeleteVolumeOutputTypeDef = TypedDict("DeleteVolumeOutputTypeDef", {"VolumeARN": str}, total=False)

DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {"GatewayARN": str, "Status": Literal["COMPLETE", "FAILED", "PENDING"], "StartTime": datetime},
    total=False,
)

DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)

DescribeCacheOutputTypeDef = TypedDict(
    "DescribeCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
    },
    total=False,
)

DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {"CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"]},
    total=False,
)

DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {"ChapCredentials": List["ChapInfoTypeDef"]},
    total=False,
)

DescribeGatewayInformationOutputTypeDef = TypedDict(
    "DescribeGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List["TagTypeDef"],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": Literal["VMWARE", "HYPER-V", "EC2", "KVM", "OTHER"],
        "EndpointType": str,
        "SoftwareUpdatesEndDate": str,
        "DeprecationDate": str,
    },
    total=False,
)

DescribeMaintenanceStartTimeOutputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
    },
    total=False,
)

DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {"NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"]},
    total=False,
)

DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {"SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"]},
    total=False,
)

DescribeSMBSettingsOutputTypeDef = TypedDict(
    "DescribeSMBSettingsOutputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": Literal[
            "ClientSpecified", "MandatorySigning", "MandatoryEncryption"
        ],
    },
    total=False,
)

DescribeSnapshotScheduleOutputTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {"StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"]},
    total=False,
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {"TapeArchives": List["TapeArchiveTypeDef"], "Marker": str},
    total=False,
)

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef", {"Tapes": List["TapeTypeDef"], "Marker": str}, total=False
)

DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
    },
    total=False,
)

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {"GatewayARN": str, "VTLDevices": List["VTLDeviceTypeDef"], "Marker": str},
    total=False,
)

DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
    },
    total=False,
)

DetachVolumeOutputTypeDef = TypedDict("DetachVolumeOutputTypeDef", {"VolumeARN": str}, total=False)

DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef", {"GatewayARN": str}, total=False
)

JoinDomainOutputTypeDef = TypedDict(
    "JoinDomainOutputTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
    },
    total=False,
)

ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {"AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"]},
    total=False,
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {"Marker": str, "NextMarker": str, "FileShareInfoList": List["FileShareInfoTypeDef"]},
    total=False,
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {"Gateways": List["GatewayInfoTypeDef"], "Marker": str},
    total=False,
)

ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef", {"GatewayARN": str, "Disks": List["DiskTypeDef"]}, total=False
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"ResourceARN": str, "Marker": str, "Tags": List["TagTypeDef"]},
    total=False,
)

ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef", {"PoolInfos": List["PoolInfoTypeDef"], "Marker": str}, total=False
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef", {"TapeInfos": List["TapeInfoTypeDef"], "Marker": str}, total=False
)

ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef", {"Initiators": List[str]}, total=False
)

ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {"GatewayARN": str, "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"]},
    total=False,
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {"GatewayARN": str, "Marker": str, "VolumeInfos": List["VolumeInfoTypeDef"]},
    total=False,
)

NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef", {"FileShareARN": str, "NotificationId": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef", {"FileShareARN": str, "NotificationId": str}, total=False
)

RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef", {"ResourceARN": str}, total=False
)

ResetCacheOutputTypeDef = TypedDict("ResetCacheOutputTypeDef", {"GatewayARN": str}, total=False)

RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef", {"TapeARN": str}, total=False
)

RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef", {"TapeARN": str}, total=False
)

SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef", {"GatewayARN": str}, total=False
)

SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef", {"GatewayARN": str}, total=False
)

ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef", {"GatewayARN": str}, total=False
)

StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef", {"GatewayARN": str}, total=False
)

StartGatewayOutputTypeDef = TypedDict("StartGatewayOutputTypeDef", {"GatewayARN": str}, total=False)

UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef", {"GatewayARN": str}, total=False
)

UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef", {"GatewayARN": str}, total=False
)

UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef", {"TargetARN": str, "InitiatorName": str}, total=False
)

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef", {"GatewayARN": str, "GatewayName": str}, total=False
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef", {"GatewayARN": str}, total=False
)

UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef", {"GatewayARN": str}, total=False
)

UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef", {"FileShareARN": str}, total=False
)

UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef", {"FileShareARN": str}, total=False
)

UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef", {"GatewayARN": str}, total=False
)

UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef", {"VolumeARN": str}, total=False
)

UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef", {"VTLDeviceARN": str}, total=False
)
