# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for storagegateway service client

Usage::

    ```python
    import boto3
    from mypy_boto3_storagegateway import StorageGatewayClient

    client: StorageGatewayClient = boto3.client("storagegateway")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_storagegateway.paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListFileSharesPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapePoolsPaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)
from mypy_boto3_storagegateway.type_defs import (
    ActivateGatewayOutputTypeDef,
    AddCacheOutputTypeDef,
    AddTagsToResourceOutputTypeDef,
    AddUploadBufferOutputTypeDef,
    AddWorkingStorageOutputTypeDef,
    AssignTapePoolOutputTypeDef,
    AttachVolumeOutputTypeDef,
    AutomaticTapeCreationRuleTypeDef,
    BandwidthRateLimitIntervalTypeDef,
    CacheAttributesTypeDef,
    CancelArchivalOutputTypeDef,
    CancelRetrievalOutputTypeDef,
    CreateCachediSCSIVolumeOutputTypeDef,
    CreateNFSFileShareOutputTypeDef,
    CreateSMBFileShareOutputTypeDef,
    CreateSnapshotFromVolumeRecoveryPointOutputTypeDef,
    CreateSnapshotOutputTypeDef,
    CreateStorediSCSIVolumeOutputTypeDef,
    CreateTapePoolOutputTypeDef,
    CreateTapesOutputTypeDef,
    CreateTapeWithBarcodeOutputTypeDef,
    DeleteAutomaticTapeCreationPolicyOutputTypeDef,
    DeleteBandwidthRateLimitOutputTypeDef,
    DeleteChapCredentialsOutputTypeDef,
    DeleteFileShareOutputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteSnapshotScheduleOutputTypeDef,
    DeleteTapeArchiveOutputTypeDef,
    DeleteTapeOutputTypeDef,
    DeleteTapePoolOutputTypeDef,
    DeleteVolumeOutputTypeDef,
    DescribeAvailabilityMonitorTestOutputTypeDef,
    DescribeBandwidthRateLimitOutputTypeDef,
    DescribeBandwidthRateLimitScheduleOutputTypeDef,
    DescribeCachediSCSIVolumesOutputTypeDef,
    DescribeCacheOutputTypeDef,
    DescribeChapCredentialsOutputTypeDef,
    DescribeGatewayInformationOutputTypeDef,
    DescribeMaintenanceStartTimeOutputTypeDef,
    DescribeNFSFileSharesOutputTypeDef,
    DescribeSMBFileSharesOutputTypeDef,
    DescribeSMBSettingsOutputTypeDef,
    DescribeSnapshotScheduleOutputTypeDef,
    DescribeStorediSCSIVolumesOutputTypeDef,
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeUploadBufferOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    DescribeWorkingStorageOutputTypeDef,
    DetachVolumeOutputTypeDef,
    DisableGatewayOutputTypeDef,
    JoinDomainOutputTypeDef,
    ListAutomaticTapeCreationPoliciesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListLocalDisksOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapePoolsOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumeInitiatorsOutputTypeDef,
    ListVolumeRecoveryPointsOutputTypeDef,
    ListVolumesOutputTypeDef,
    NFSFileShareDefaultsTypeDef,
    NotifyWhenUploadedOutputTypeDef,
    RefreshCacheOutputTypeDef,
    RemoveTagsFromResourceOutputTypeDef,
    ResetCacheOutputTypeDef,
    RetrieveTapeArchiveOutputTypeDef,
    RetrieveTapeRecoveryPointOutputTypeDef,
    SetLocalConsolePasswordOutputTypeDef,
    SetSMBGuestPasswordOutputTypeDef,
    ShutdownGatewayOutputTypeDef,
    StartAvailabilityMonitorTestOutputTypeDef,
    StartGatewayOutputTypeDef,
    TagTypeDef,
    UpdateAutomaticTapeCreationPolicyOutputTypeDef,
    UpdateBandwidthRateLimitOutputTypeDef,
    UpdateBandwidthRateLimitScheduleOutputTypeDef,
    UpdateChapCredentialsOutputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateMaintenanceStartTimeOutputTypeDef,
    UpdateNFSFileShareOutputTypeDef,
    UpdateSMBFileShareOutputTypeDef,
    UpdateSMBFileShareVisibilityOutputTypeDef,
    UpdateSMBSecurityStrategyOutputTypeDef,
    UpdateSnapshotScheduleOutputTypeDef,
    UpdateVTLDeviceTypeOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("StorageGatewayClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidGatewayRequestException: Type[BotocoreClientError]
    ServiceUnavailableError: Type[BotocoreClientError]


class StorageGatewayClient:
    """
    [StorageGateway.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ActivateGatewayOutputTypeDef:
        """
        [Client.activate_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)
        """

    def add_cache(self, GatewayARN: str, DiskIds: List[str]) -> AddCacheOutputTypeDef:
        """
        [Client.add_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.add_cache)
        """

    def add_tags_to_resource(
        self, ResourceARN: str, Tags: List["TagTypeDef"]
    ) -> AddTagsToResourceOutputTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)
        """

    def add_upload_buffer(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddUploadBufferOutputTypeDef:
        """
        [Client.add_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)
        """

    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddWorkingStorageOutputTypeDef:
        """
        [Client.add_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)
        """

    def assign_tape_pool(
        self, TapeARN: str, PoolId: str, BypassGovernanceRetention: bool = None
    ) -> AssignTapePoolOutputTypeDef:
        """
        [Client.assign_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)
        """

    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> AttachVolumeOutputTypeDef:
        """
        [Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)
        """

    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> CancelArchivalOutputTypeDef:
        """
        [Client.cancel_archival documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)
        """

    def cancel_retrieval(self, GatewayARN: str, TapeARN: str) -> CancelRetrievalOutputTypeDef:
        """
        [Client.cancel_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)
        """

    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCachediSCSIVolumeOutputTypeDef:
        """
        [Client.create_cached_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)
        """

    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> CreateNFSFileShareOutputTypeDef:
        """
        [Client.create_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)
        """

    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AccessBasedEnumeration: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        AuditDestinationARN: str = None,
        Authentication: str = None,
        CaseSensitivity: Literal["ClientSpecified", "CaseSensitive"] = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> CreateSMBFileShareOutputTypeDef:
        """
        [Client.create_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)
        """

    def create_snapshot(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotOutputTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)
        """

    def create_snapshot_from_volume_recovery_point(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
        """
        [Client.create_snapshot_from_volume_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)
        """

    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateStorediSCSIVolumeOutputTypeDef:
        """
        [Client.create_stored_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)
        """

    def create_tape_pool(
        self,
        PoolName: str,
        StorageClass: Literal["DEEP_ARCHIVE", "GLACIER"],
        RetentionLockType: Literal["COMPLIANCE", "GOVERNANCE", "NONE"] = None,
        RetentionLockTimeInDays: int = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapePoolOutputTypeDef:
        """
        [Client.create_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_tape_pool)
        """

    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapeWithBarcodeOutputTypeDef:
        """
        [Client.create_tape_with_barcode documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)
        """

    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapesOutputTypeDef:
        """
        [Client.create_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)
        """

    def delete_automatic_tape_creation_policy(
        self, GatewayARN: str
    ) -> DeleteAutomaticTapeCreationPolicyOutputTypeDef:
        """
        [Client.delete_automatic_tape_creation_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_automatic_tape_creation_policy)
        """

    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> DeleteBandwidthRateLimitOutputTypeDef:
        """
        [Client.delete_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)
        """

    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> DeleteChapCredentialsOutputTypeDef:
        """
        [Client.delete_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)
        """

    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> DeleteFileShareOutputTypeDef:
        """
        [Client.delete_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)
        """

    def delete_gateway(self, GatewayARN: str) -> DeleteGatewayOutputTypeDef:
        """
        [Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)
        """

    def delete_snapshot_schedule(self, VolumeARN: str) -> DeleteSnapshotScheduleOutputTypeDef:
        """
        [Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)
        """

    def delete_tape(
        self, GatewayARN: str, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeOutputTypeDef:
        """
        [Client.delete_tape documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)
        """

    def delete_tape_archive(
        self, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeArchiveOutputTypeDef:
        """
        [Client.delete_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)
        """

    def delete_tape_pool(self, PoolARN: str) -> DeleteTapePoolOutputTypeDef:
        """
        [Client.delete_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_pool)
        """

    def delete_volume(self, VolumeARN: str) -> DeleteVolumeOutputTypeDef:
        """
        [Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)
        """

    def describe_availability_monitor_test(
        self, GatewayARN: str
    ) -> DescribeAvailabilityMonitorTestOutputTypeDef:
        """
        [Client.describe_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)
        """

    def describe_bandwidth_rate_limit(
        self, GatewayARN: str
    ) -> DescribeBandwidthRateLimitOutputTypeDef:
        """
        [Client.describe_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)
        """

    def describe_bandwidth_rate_limit_schedule(
        self, GatewayARN: str
    ) -> DescribeBandwidthRateLimitScheduleOutputTypeDef:
        """
        [Client.describe_bandwidth_rate_limit_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit_schedule)
        """

    def describe_cache(self, GatewayARN: str) -> DescribeCacheOutputTypeDef:
        """
        [Client.describe_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)
        """

    def describe_cached_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeCachediSCSIVolumesOutputTypeDef:
        """
        [Client.describe_cached_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)
        """

    def describe_chap_credentials(self, TargetARN: str) -> DescribeChapCredentialsOutputTypeDef:
        """
        [Client.describe_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)
        """

    def describe_gateway_information(
        self, GatewayARN: str
    ) -> DescribeGatewayInformationOutputTypeDef:
        """
        [Client.describe_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)
        """

    def describe_maintenance_start_time(
        self, GatewayARN: str
    ) -> DescribeMaintenanceStartTimeOutputTypeDef:
        """
        [Client.describe_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)
        """

    def describe_nfs_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeNFSFileSharesOutputTypeDef:
        """
        [Client.describe_nfs_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)
        """

    def describe_smb_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeSMBFileSharesOutputTypeDef:
        """
        [Client.describe_smb_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)
        """

    def describe_smb_settings(self, GatewayARN: str) -> DescribeSMBSettingsOutputTypeDef:
        """
        [Client.describe_smb_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)
        """

    def describe_snapshot_schedule(self, VolumeARN: str) -> DescribeSnapshotScheduleOutputTypeDef:
        """
        [Client.describe_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)
        """

    def describe_stored_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeStorediSCSIVolumesOutputTypeDef:
        """
        [Client.describe_stored_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)
        """

    def describe_tape_archives(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        [Client.describe_tape_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)
        """

    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        [Client.describe_tape_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)
        """

    def describe_tapes(
        self, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapesOutputTypeDef:
        """
        [Client.describe_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)
        """

    def describe_upload_buffer(self, GatewayARN: str) -> DescribeUploadBufferOutputTypeDef:
        """
        [Client.describe_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)
        """

    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        [Client.describe_vtl_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)
        """

    def describe_working_storage(self, GatewayARN: str) -> DescribeWorkingStorageOutputTypeDef:
        """
        [Client.describe_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)
        """

    def detach_volume(self, VolumeARN: str, ForceDetach: bool = None) -> DetachVolumeOutputTypeDef:
        """
        [Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)
        """

    def disable_gateway(self, GatewayARN: str) -> DisableGatewayOutputTypeDef:
        """
        [Client.disable_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)
        """

    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None,
    ) -> JoinDomainOutputTypeDef:
        """
        [Client.join_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.join_domain)
        """

    def list_automatic_tape_creation_policies(
        self, GatewayARN: str = None
    ) -> ListAutomaticTapeCreationPoliciesOutputTypeDef:
        """
        [Client.list_automatic_tape_creation_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_automatic_tape_creation_policies)
        """

    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSharesOutputTypeDef:
        """
        [Client.list_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)
        """

    def list_gateways(self, Marker: str = None, Limit: int = None) -> ListGatewaysOutputTypeDef:
        """
        [Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)
        """

    def list_local_disks(self, GatewayARN: str) -> ListLocalDisksOutputTypeDef:
        """
        [Client.list_local_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)
        """

    def list_tape_pools(
        self, PoolARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapePoolsOutputTypeDef:
        """
        [Client.list_tape_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_tape_pools)
        """

    def list_tapes(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapesOutputTypeDef:
        """
        [Client.list_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)
        """

    def list_volume_initiators(self, VolumeARN: str) -> ListVolumeInitiatorsOutputTypeDef:
        """
        [Client.list_volume_initiators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)
        """

    def list_volume_recovery_points(self, GatewayARN: str) -> ListVolumeRecoveryPointsOutputTypeDef:
        """
        [Client.list_volume_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)
        """

    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ListVolumesOutputTypeDef:
        """
        [Client.list_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)
        """

    def notify_when_uploaded(self, FileShareARN: str) -> NotifyWhenUploadedOutputTypeDef:
        """
        [Client.notify_when_uploaded documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)
        """

    def refresh_cache(
        self, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> RefreshCacheOutputTypeDef:
        """
        [Client.refresh_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)
        """

    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[str]
    ) -> RemoveTagsFromResourceOutputTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)
        """

    def reset_cache(self, GatewayARN: str) -> ResetCacheOutputTypeDef:
        """
        [Client.reset_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)
        """

    def retrieve_tape_archive(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeArchiveOutputTypeDef:
        """
        [Client.retrieve_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)
        """

    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeRecoveryPointOutputTypeDef:
        """
        [Client.retrieve_tape_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)
        """

    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> SetLocalConsolePasswordOutputTypeDef:
        """
        [Client.set_local_console_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)
        """

    def set_smb_guest_password(
        self, GatewayARN: str, Password: str
    ) -> SetSMBGuestPasswordOutputTypeDef:
        """
        [Client.set_smb_guest_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)
        """

    def shutdown_gateway(self, GatewayARN: str) -> ShutdownGatewayOutputTypeDef:
        """
        [Client.shutdown_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)
        """

    def start_availability_monitor_test(
        self, GatewayARN: str
    ) -> StartAvailabilityMonitorTestOutputTypeDef:
        """
        [Client.start_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)
        """

    def start_gateway(self, GatewayARN: str) -> StartGatewayOutputTypeDef:
        """
        [Client.start_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)
        """

    def update_automatic_tape_creation_policy(
        self, AutomaticTapeCreationRules: List["AutomaticTapeCreationRuleTypeDef"], GatewayARN: str
    ) -> UpdateAutomaticTapeCreationPolicyOutputTypeDef:
        """
        [Client.update_automatic_tape_creation_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_automatic_tape_creation_policy)
        """

    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> UpdateBandwidthRateLimitOutputTypeDef:
        """
        [Client.update_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)
        """

    def update_bandwidth_rate_limit_schedule(
        self,
        GatewayARN: str,
        BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"],
    ) -> UpdateBandwidthRateLimitScheduleOutputTypeDef:
        """
        [Client.update_bandwidth_rate_limit_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit_schedule)
        """

    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> UpdateChapCredentialsOutputTypeDef:
        """
        [Client.update_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)
        """

    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        [Client.update_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)
        """

    def update_gateway_software_now(self, GatewayARN: str) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        [Client.update_gateway_software_now documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)
        """

    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> UpdateMaintenanceStartTimeOutputTypeDef:
        """
        [Client.update_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)
        """

    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> UpdateNFSFileShareOutputTypeDef:
        """
        [Client.update_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)
        """

    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AccessBasedEnumeration: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        AuditDestinationARN: str = None,
        CaseSensitivity: Literal["ClientSpecified", "CaseSensitive"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> UpdateSMBFileShareOutputTypeDef:
        """
        [Client.update_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)
        """

    def update_smb_file_share_visibility(
        self, GatewayARN: str, FileSharesVisible: bool
    ) -> UpdateSMBFileShareVisibilityOutputTypeDef:
        """
        [Client.update_smb_file_share_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share_visibility)
        """

    def update_smb_security_strategy(
        self,
        GatewayARN: str,
        SMBSecurityStrategy: Literal["ClientSpecified", "MandatorySigning", "MandatoryEncryption"],
    ) -> UpdateSMBSecurityStrategyOutputTypeDef:
        """
        [Client.update_smb_security_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)
        """

    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> UpdateSnapshotScheduleOutputTypeDef:
        """
        [Client.update_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)
        """

    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> UpdateVTLDeviceTypeOutputTypeDef:
        """
        [Client.update_vtl_device_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> DescribeTapeArchivesPaginator:
        """
        [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> DescribeTapeRecoveryPointsPaginator:
        """
        [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tapes"]) -> DescribeTapesPaginator:
        """
        [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> DescribeVTLDevicesPaginator:
        """
        [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_file_shares"]) -> ListFileSharesPaginator:
        """
        [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tape_pools"]) -> ListTapePoolsPaginator:
        """
        [Paginator.ListTapePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tapes"]) -> ListTapesPaginator:
        """
        [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_volumes"]) -> ListVolumesPaginator:
        """
        [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
        """
