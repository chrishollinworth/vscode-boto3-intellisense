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
from typing import Any, Dict, List

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
    "BandwidthRateLimitIntervalTypeDef",
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
    "ResponseMetadata",
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
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
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
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
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


_RequiredBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_RequiredBandwidthRateLimitIntervalTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": List[int],
    },
)
_OptionalBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_OptionalBandwidthRateLimitIntervalTypeDef",
    {"AverageUploadRateLimitInBitsPerSec": int, "AverageDownloadRateLimitInBitsPerSec": int},
    total=False,
)


class BandwidthRateLimitIntervalTypeDef(
    _RequiredBandwidthRateLimitIntervalTypeDef, _OptionalBandwidthRateLimitIntervalTypeDef
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
        "NotificationPolicy": str,
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

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
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
        "AccessBasedEnumeration": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "Authentication": str,
        "CaseSensitivity": Literal["ClientSpecified", "CaseSensitive"],
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
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
    "ActivateGatewayOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AddCacheOutputTypeDef = TypedDict(
    "AddCacheOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef",
    {"ResourceARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef",
    {"VolumeARN": str, "TargetARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef",
    {"VolumeARN": str, "TargetARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef",
    {"FileShareARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef",
    {"FileShareARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef",
    {"VolumeARN": str, "SnapshotId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef",
    {"PoolARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef",
    {"TapeARNs": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef",
    {"TargetARN": str, "InitiatorName": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef",
    {"FileShareARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef",
    {"VolumeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteTapeOutputTypeDef = TypedDict(
    "DeleteTapeOutputTypeDef", {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"}, total=False
)

DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef",
    {"PoolARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteVolumeOutputTypeDef = TypedDict(
    "DeleteVolumeOutputTypeDef",
    {"VolumeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "Status": Literal["COMPLETE", "FAILED", "PENDING"],
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
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
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {
        "CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {"ChapCredentials": List["ChapInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
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
        "ResponseMetadata": "ResponseMetadata",
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
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {
        "NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {
        "SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
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
        "FileSharesVisible": bool,
        "ResponseMetadata": "ResponseMetadata",
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
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {
        "StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {
        "TapeArchives": List["TapeArchiveTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef",
    {"Tapes": List["TapeTypeDef"], "Marker": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List["VTLDeviceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DetachVolumeOutputTypeDef = TypedDict(
    "DetachVolumeOutputTypeDef",
    {"VolumeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
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
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List["FileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {"Gateways": List["GatewayInfoTypeDef"], "Marker": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef",
    {"GatewayARN": str, "Disks": List["DiskTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef",
    {"PoolInfos": List["PoolInfoTypeDef"], "Marker": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef",
    {"TapeInfos": List["TapeInfoTypeDef"], "Marker": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef",
    {"Initiators": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List["VolumeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef",
    {"FileShareARN": str, "NotificationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef",
    {"FileShareARN": str, "NotificationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef",
    {"ResourceARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ResetCacheOutputTypeDef = TypedDict(
    "ResetCacheOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef",
    {"TapeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartGatewayOutputTypeDef = TypedDict(
    "StartGatewayOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef",
    {"TargetARN": str, "InitiatorName": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {"GatewayARN": str, "GatewayName": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef",
    {"FileShareARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef",
    {"FileShareARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateSMBFileShareVisibilityOutputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef",
    {"GatewayARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef",
    {"VolumeARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef",
    {"VTLDeviceARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
