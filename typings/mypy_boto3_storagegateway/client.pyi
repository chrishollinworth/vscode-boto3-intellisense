"""
Type annotations for storagegateway service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_storagegateway import StorageGatewayClient

    client: StorageGatewayClient = boto3.client("storagegateway")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CaseSensitivityType,
    GatewayCapacityType,
    ObjectACLType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
)
from .paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListFileSharesPaginator,
    ListFileSystemAssociationsPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapePoolsPaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)
from .type_defs import (
    ActivateGatewayOutputTypeDef,
    AddCacheOutputTypeDef,
    AddTagsToResourceOutputTypeDef,
    AddUploadBufferOutputTypeDef,
    AddWorkingStorageOutputTypeDef,
    AssignTapePoolOutputTypeDef,
    AssociateFileSystemOutputTypeDef,
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
    DescribeFileSystemAssociationsOutputTypeDef,
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
    DisassociateFileSystemOutputTypeDef,
    EndpointNetworkConfigurationTypeDef,
    JoinDomainOutputTypeDef,
    ListAutomaticTapeCreationPoliciesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListFileSystemAssociationsOutputTypeDef,
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
    SMBLocalGroupsTypeDef,
    StartAvailabilityMonitorTestOutputTypeDef,
    StartGatewayOutputTypeDef,
    TagTypeDef,
    UpdateAutomaticTapeCreationPolicyOutputTypeDef,
    UpdateBandwidthRateLimitOutputTypeDef,
    UpdateBandwidthRateLimitScheduleOutputTypeDef,
    UpdateChapCredentialsOutputTypeDef,
    UpdateFileSystemAssociationOutputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateMaintenanceStartTimeOutputTypeDef,
    UpdateNFSFileShareOutputTypeDef,
    UpdateSMBFileShareOutputTypeDef,
    UpdateSMBFileShareVisibilityOutputTypeDef,
    UpdateSMBLocalGroupsOutputTypeDef,
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

class StorageGatewayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        StorageGatewayClient exceptions.
        """
    def activate_gateway(
        self,
        *,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ActivateGatewayOutputTypeDef:
        """
        Activates the gateway you previously deployed on your host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#activate_gateway)
        """
    def add_cache(self, *, GatewayARN: str, DiskIds: List[str]) -> AddCacheOutputTypeDef:
        """
        Configures one or more gateway local disks as cache for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.add_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add_cache)
        """
    def add_tags_to_resource(
        self, *, ResourceARN: str, Tags: List["TagTypeDef"]
    ) -> AddTagsToResourceOutputTypeDef:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add_tags_to_resource)
        """
    def add_upload_buffer(
        self, *, GatewayARN: str, DiskIds: List[str]
    ) -> AddUploadBufferOutputTypeDef:
        """
        Configures one or more gateway local disks as upload buffer for a specified
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add_upload_buffer)
        """
    def add_working_storage(
        self, *, GatewayARN: str, DiskIds: List[str]
    ) -> AddWorkingStorageOutputTypeDef:
        """
        Configures one or more gateway local disks as working storage for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add_working_storage)
        """
    def assign_tape_pool(
        self, *, TapeARN: str, PoolId: str, BypassGovernanceRetention: bool = None
    ) -> AssignTapePoolOutputTypeDef:
        """
        Assigns a tape to a tape pool for archiving.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#assign_tape_pool)
        """
    def associate_file_system(
        self,
        *,
        UserName: str,
        Password: str,
        ClientToken: str,
        GatewayARN: str,
        LocationARN: str,
        Tags: List["TagTypeDef"] = None,
        AuditDestinationARN: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        EndpointNetworkConfiguration: "EndpointNetworkConfigurationTypeDef" = None
    ) -> AssociateFileSystemOutputTypeDef:
        """
        Associate an Amazon FSx file system with the FSx File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.associate_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#associate_file_system)
        """
    def attach_volume(
        self,
        *,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None
    ) -> AttachVolumeOutputTypeDef:
        """
        Connects a volume to an iSCSI connection and then attaches the volume to the
        specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#attach_volume)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#can_paginate)
        """
    def cancel_archival(self, *, GatewayARN: str, TapeARN: str) -> CancelArchivalOutputTypeDef:
        """
        Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the
        archiving process is initiated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#cancel_archival)
        """
    def cancel_retrieval(self, *, GatewayARN: str, TapeARN: str) -> CancelRetrievalOutputTypeDef:
        """
        Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a
        gateway after the retrieval process is initiated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#cancel_retrieval)
        """
    def create_cached_iscsi_volume(
        self,
        *,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCachediSCSIVolumeOutputTypeDef:
        """
        Creates a cached volume on a specified cached volume gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_cached_iscsi_volume)
        """
    def create_nfs_file_share(
        self,
        *,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACLType = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
        VPCEndpointDNSName: str = None,
        BucketRegion: str = None,
        AuditDestinationARN: str = None
    ) -> CreateNFSFileShareOutputTypeDef:
        """
        Creates a Network File System (NFS) file share on an existing S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_nfs_file_share)
        """
    def create_smb_file_share(
        self,
        *,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACLType = None,
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
        CaseSensitivity: CaseSensitivityType = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
        VPCEndpointDNSName: str = None,
        BucketRegion: str = None,
        OplocksEnabled: bool = None
    ) -> CreateSMBFileShareOutputTypeDef:
        """
        Creates a Server Message Block (SMB) file share on an existing S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_smb_file_share)
        """
    def create_snapshot(
        self, *, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotOutputTypeDef:
        """
        Initiates a snapshot of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_snapshot)
        """
    def create_snapshot_from_volume_recovery_point(
        self, *, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
        """
        Initiates a snapshot of a gateway from a volume recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_snapshot_from_volume_recovery_point)
        """
    def create_stored_iscsi_volume(
        self,
        *,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateStorediSCSIVolumeOutputTypeDef:
        """
        Creates a volume on a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_stored_iscsi_volume)
        """
    def create_tape_pool(
        self,
        *,
        PoolName: str,
        StorageClass: TapeStorageClassType,
        RetentionLockType: RetentionLockTypeType = None,
        RetentionLockTimeInDays: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTapePoolOutputTypeDef:
        """
        Creates a new custom tape pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_tape_pool)
        """
    def create_tape_with_barcode(
        self,
        *,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTapeWithBarcodeOutputTypeDef:
        """
        Creates a virtual tape by using your own barcode.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_tape_with_barcode)
        """
    def create_tapes(
        self,
        *,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTapesOutputTypeDef:
        """
        Creates one or more virtual tapes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create_tapes)
        """
    def delete_automatic_tape_creation_policy(
        self, *, GatewayARN: str
    ) -> DeleteAutomaticTapeCreationPolicyOutputTypeDef:
        """
        Deletes the automatic tape creation policy of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_automatic_tape_creation_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_automatic_tape_creation_policy)
        """
    def delete_bandwidth_rate_limit(
        self, *, GatewayARN: str, BandwidthType: str
    ) -> DeleteBandwidthRateLimitOutputTypeDef:
        """
        Deletes the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_bandwidth_rate_limit)
        """
    def delete_chap_credentials(
        self, *, TargetARN: str, InitiatorName: str
    ) -> DeleteChapCredentialsOutputTypeDef:
        """
        Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a
        specified iSCSI target and initiator pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_chap_credentials)
        """
    def delete_file_share(
        self, *, FileShareARN: str, ForceDelete: bool = None
    ) -> DeleteFileShareOutputTypeDef:
        """
        Deletes a file share from an S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_file_share)
        """
    def delete_gateway(self, *, GatewayARN: str) -> DeleteGatewayOutputTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_gateway)
        """
    def delete_snapshot_schedule(self, *, VolumeARN: str) -> DeleteSnapshotScheduleOutputTypeDef:
        """
        Deletes a snapshot of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_snapshot_schedule)
        """
    def delete_tape(
        self, *, GatewayARN: str, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeOutputTypeDef:
        """
        Deletes the specified virtual tape.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_tape)
        """
    def delete_tape_archive(
        self, *, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeArchiveOutputTypeDef:
        """
        Deletes the specified virtual tape from the virtual tape shelf (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_tape_archive)
        """
    def delete_tape_pool(self, *, PoolARN: str) -> DeleteTapePoolOutputTypeDef:
        """
        Delete a custom tape pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_tape_pool)
        """
    def delete_volume(self, *, VolumeARN: str) -> DeleteVolumeOutputTypeDef:
        """
        Deletes the specified storage volume that you previously created using the
        CreateCachediSCSIVolume or  CreateStorediSCSIVolume API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete_volume)
        """
    def describe_availability_monitor_test(
        self, *, GatewayARN: str
    ) -> DescribeAvailabilityMonitorTestOutputTypeDef:
        """
        Returns information about the most recent high availability monitoring test that
        was performed on the host in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_availability_monitor_test)
        """
    def describe_bandwidth_rate_limit(
        self, *, GatewayARN: str
    ) -> DescribeBandwidthRateLimitOutputTypeDef:
        """
        Returns the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_bandwidth_rate_limit)
        """
    def describe_bandwidth_rate_limit_schedule(
        self, *, GatewayARN: str
    ) -> DescribeBandwidthRateLimitScheduleOutputTypeDef:
        """
        Returns information about the bandwidth rate limit schedule of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_bandwidth_rate_limit_schedule)
        """
    def describe_cache(self, *, GatewayARN: str) -> DescribeCacheOutputTypeDef:
        """
        Returns information about the cache of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_cache)
        """
    def describe_cached_iscsi_volumes(
        self, *, VolumeARNs: List[str]
    ) -> DescribeCachediSCSIVolumesOutputTypeDef:
        """
        Returns a description of the gateway volumes specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_cached_iscsi_volumes)
        """
    def describe_chap_credentials(self, *, TargetARN: str) -> DescribeChapCredentialsOutputTypeDef:
        """
        Returns an array of Challenge-Handshake Authentication Protocol (CHAP)
        credentials information for a specified iSCSI target, one for each target-
        initiator pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_chap_credentials)
        """
    def describe_file_system_associations(
        self, *, FileSystemAssociationARNList: List[str]
    ) -> DescribeFileSystemAssociationsOutputTypeDef:
        """
        Gets the file system association information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_file_system_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_file_system_associations)
        """
    def describe_gateway_information(
        self, *, GatewayARN: str
    ) -> DescribeGatewayInformationOutputTypeDef:
        """
        Returns metadata about a gateway such as its name, network interfaces,
        configured time zone, and the state (whether the gateway is running or not).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_gateway_information)
        """
    def describe_maintenance_start_time(
        self, *, GatewayARN: str
    ) -> DescribeMaintenanceStartTimeOutputTypeDef:
        """
        Returns your gateway's weekly maintenance start time including the day and time
        of the week.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_maintenance_start_time)
        """
    def describe_nfs_file_shares(
        self, *, FileShareARNList: List[str]
    ) -> DescribeNFSFileSharesOutputTypeDef:
        """
        Gets a description for one or more Network File System (NFS) file shares from an
        S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_nfs_file_shares)
        """
    def describe_smb_file_shares(
        self, *, FileShareARNList: List[str]
    ) -> DescribeSMBFileSharesOutputTypeDef:
        """
        Gets a description for one or more Server Message Block (SMB) file shares from a
        S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_smb_file_shares)
        """
    def describe_smb_settings(self, *, GatewayARN: str) -> DescribeSMBSettingsOutputTypeDef:
        """
        Gets a description of a Server Message Block (SMB) file share settings from a
        file gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_smb_settings)
        """
    def describe_snapshot_schedule(
        self, *, VolumeARN: str
    ) -> DescribeSnapshotScheduleOutputTypeDef:
        """
        Describes the snapshot schedule for the specified gateway volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_snapshot_schedule)
        """
    def describe_stored_iscsi_volumes(
        self, *, VolumeARNs: List[str]
    ) -> DescribeStorediSCSIVolumesOutputTypeDef:
        """
        Returns the description of the gateway volumes specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_stored_iscsi_volumes)
        """
    def describe_tape_archives(
        self, *, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        Returns a description of specified virtual tapes in the virtual tape shelf
        (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_tape_archives)
        """
    def describe_tape_recovery_points(
        self, *, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        Returns a list of virtual tape recovery points that are available for the
        specified tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_tape_recovery_points)
        """
    def describe_tapes(
        self, *, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapesOutputTypeDef:
        """
        Returns a description of the specified Amazon Resource Name (ARN) of virtual
        tapes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_tapes)
        """
    def describe_upload_buffer(self, *, GatewayARN: str) -> DescribeUploadBufferOutputTypeDef:
        """
        Returns information about the upload buffer of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_upload_buffer)
        """
    def describe_vtl_devices(
        self,
        *,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        Returns a description of virtual tape library (VTL) devices for the specified
        tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_vtl_devices)
        """
    def describe_working_storage(self, *, GatewayARN: str) -> DescribeWorkingStorageOutputTypeDef:
        """
        Returns information about the working storage of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe_working_storage)
        """
    def detach_volume(
        self, *, VolumeARN: str, ForceDetach: bool = None
    ) -> DetachVolumeOutputTypeDef:
        """
        Disconnects a volume from an iSCSI connection and then detaches the volume from
        the specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#detach_volume)
        """
    def disable_gateway(self, *, GatewayARN: str) -> DisableGatewayOutputTypeDef:
        """
        Disables a tape gateway when the gateway is no longer functioning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#disable_gateway)
        """
    def disassociate_file_system(
        self, *, FileSystemAssociationARN: str, ForceDelete: bool = None
    ) -> DisassociateFileSystemOutputTypeDef:
        """
        Disassociates an Amazon FSx file system from the specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.disassociate_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#disassociate_file_system)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#generate_presigned_url)
        """
    def join_domain(
        self,
        *,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None
    ) -> JoinDomainOutputTypeDef:
        """
        Adds a file gateway to an Active Directory domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.join_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#join_domain)
        """
    def list_automatic_tape_creation_policies(
        self, *, GatewayARN: str = None
    ) -> ListAutomaticTapeCreationPoliciesOutputTypeDef:
        """
        Lists the automatic tape creation policies for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_automatic_tape_creation_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_automatic_tape_creation_policies)
        """
    def list_file_shares(
        self, *, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSharesOutputTypeDef:
        """
        Gets a list of the file shares for a specific S3 File Gateway, or the list of
        file shares that belong to the calling user account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_file_shares)
        """
    def list_file_system_associations(
        self, *, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSystemAssociationsOutputTypeDef:
        """
        Gets a list of `FileSystemAssociationSummary` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_file_system_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_file_system_associations)
        """
    def list_gateways(self, *, Marker: str = None, Limit: int = None) -> ListGatewaysOutputTypeDef:
        """
        Lists gateways owned by an Amazon Web Services account in an Amazon Web Services
        Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_gateways)
        """
    def list_local_disks(self, *, GatewayARN: str) -> ListLocalDisksOutputTypeDef:
        """
        Returns a list of the gateway's local disks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_local_disks)
        """
    def list_tags_for_resource(
        self, *, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags that have been added to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_tags_for_resource)
        """
    def list_tape_pools(
        self, *, PoolARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapePoolsOutputTypeDef:
        """
        Lists custom tape pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_tape_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_tape_pools)
        """
    def list_tapes(
        self, *, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapesOutputTypeDef:
        """
        Lists virtual tapes in your virtual tape library (VTL) and your virtual tape
        shelf (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_tapes)
        """
    def list_volume_initiators(self, *, VolumeARN: str) -> ListVolumeInitiatorsOutputTypeDef:
        """
        Lists iSCSI initiators that are connected to a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_volume_initiators)
        """
    def list_volume_recovery_points(
        self, *, GatewayARN: str
    ) -> ListVolumeRecoveryPointsOutputTypeDef:
        """
        Lists the recovery points for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_volume_recovery_points)
        """
    def list_volumes(
        self, *, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ListVolumesOutputTypeDef:
        """
        Lists the iSCSI stored volumes of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list_volumes)
        """
    def notify_when_uploaded(self, *, FileShareARN: str) -> NotifyWhenUploadedOutputTypeDef:
        """
        Sends you notification through CloudWatch Events when all files written to your
        file share have been uploaded to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#notify_when_uploaded)
        """
    def refresh_cache(
        self, *, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> RefreshCacheOutputTypeDef:
        """
        Refreshes the cached inventory of objects for the specified file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#refresh_cache)
        """
    def remove_tags_from_resource(
        self, *, ResourceARN: str, TagKeys: List[str]
    ) -> RemoveTagsFromResourceOutputTypeDef:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#remove_tags_from_resource)
        """
    def reset_cache(self, *, GatewayARN: str) -> ResetCacheOutputTypeDef:
        """
        Resets all cache disks that have encountered an error and makes the disks
        available for reconfiguration as cache storage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#reset_cache)
        """
    def retrieve_tape_archive(
        self, *, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeArchiveOutputTypeDef:
        """
        Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#retrieve_tape_archive)
        """
    def retrieve_tape_recovery_point(
        self, *, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeRecoveryPointOutputTypeDef:
        """
        Retrieves the recovery point for the specified virtual tape.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#retrieve_tape_recovery_point)
        """
    def set_local_console_password(
        self, *, GatewayARN: str, LocalConsolePassword: str
    ) -> SetLocalConsolePasswordOutputTypeDef:
        """
        Sets the password for your VM local console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#set_local_console_password)
        """
    def set_smb_guest_password(
        self, *, GatewayARN: str, Password: str
    ) -> SetSMBGuestPasswordOutputTypeDef:
        """
        Sets the password for the guest user `smbguest`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#set_smb_guest_password)
        """
    def shutdown_gateway(self, *, GatewayARN: str) -> ShutdownGatewayOutputTypeDef:
        """
        Shuts down a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#shutdown_gateway)
        """
    def start_availability_monitor_test(
        self, *, GatewayARN: str
    ) -> StartAvailabilityMonitorTestOutputTypeDef:
        """
        Start a test that verifies that the specified gateway is configured for High
        Availability monitoring in your host environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#start_availability_monitor_test)
        """
    def start_gateway(self, *, GatewayARN: str) -> StartGatewayOutputTypeDef:
        """
        Starts a gateway that you previously shut down (see  ShutdownGateway ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#start_gateway)
        """
    def update_automatic_tape_creation_policy(
        self,
        *,
        AutomaticTapeCreationRules: List["AutomaticTapeCreationRuleTypeDef"],
        GatewayARN: str
    ) -> UpdateAutomaticTapeCreationPolicyOutputTypeDef:
        """
        Updates the automatic tape creation policy of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_automatic_tape_creation_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_automatic_tape_creation_policy)
        """
    def update_bandwidth_rate_limit(
        self,
        *,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None
    ) -> UpdateBandwidthRateLimitOutputTypeDef:
        """
        Updates the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_bandwidth_rate_limit)
        """
    def update_bandwidth_rate_limit_schedule(
        self,
        *,
        GatewayARN: str,
        BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"]
    ) -> UpdateBandwidthRateLimitScheduleOutputTypeDef:
        """
        Updates the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_bandwidth_rate_limit_schedule)
        """
    def update_chap_credentials(
        self,
        *,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None
    ) -> UpdateChapCredentialsOutputTypeDef:
        """
        Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a
        specified iSCSI target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_chap_credentials)
        """
    def update_file_system_association(
        self,
        *,
        FileSystemAssociationARN: str,
        UserName: str = None,
        Password: str = None,
        AuditDestinationARN: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None
    ) -> UpdateFileSystemAssociationOutputTypeDef:
        """
        Updates a file system association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_file_system_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_file_system_association)
        """
    def update_gateway_information(
        self,
        *,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
        GatewayCapacity: GatewayCapacityType = None
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        Updates a gateway's metadata, which includes the gateway's name and time zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_gateway_information)
        """
    def update_gateway_software_now(
        self, *, GatewayARN: str
    ) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        Updates the gateway virtual machine (VM) software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_gateway_software_now)
        """
    def update_maintenance_start_time(
        self,
        *,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None
    ) -> UpdateMaintenanceStartTimeOutputTypeDef:
        """
        Updates a gateway's weekly maintenance start time information, including day and
        time of the week.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_maintenance_start_time)
        """
    def update_nfs_file_share(
        self,
        *,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACLType = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
        AuditDestinationARN: str = None
    ) -> UpdateNFSFileShareOutputTypeDef:
        """
        Updates a Network File System (NFS) file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_nfs_file_share)
        """
    def update_smb_file_share(
        self,
        *,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACLType = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AccessBasedEnumeration: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        AuditDestinationARN: str = None,
        CaseSensitivity: CaseSensitivityType = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
        OplocksEnabled: bool = None
    ) -> UpdateSMBFileShareOutputTypeDef:
        """
        Updates a Server Message Block (SMB) file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_smb_file_share)
        """
    def update_smb_file_share_visibility(
        self, *, GatewayARN: str, FileSharesVisible: bool
    ) -> UpdateSMBFileShareVisibilityOutputTypeDef:
        """
        Controls whether the shares on an S3 File Gateway are visible in a net view or
        browse list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_smb_file_share_visibility)
        """
    def update_smb_local_groups(
        self, *, GatewayARN: str, SMBLocalGroups: "SMBLocalGroupsTypeDef"
    ) -> UpdateSMBLocalGroupsOutputTypeDef:
        """
        Updates the list of Active Directory users and groups that have special
        permissions for SMB file shares on the gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_smb_local_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_smb_local_groups)
        """
    def update_smb_security_strategy(
        self, *, GatewayARN: str, SMBSecurityStrategy: SMBSecurityStrategyType
    ) -> UpdateSMBSecurityStrategyOutputTypeDef:
        """
        Updates the SMB security strategy on a file gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_smb_security_strategy)
        """
    def update_snapshot_schedule(
        self,
        *,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> UpdateSnapshotScheduleOutputTypeDef:
        """
        Updates a snapshot schedule configured for a gateway volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_snapshot_schedule)
        """
    def update_vtl_device_type(
        self, *, VTLDeviceARN: str, DeviceType: str
    ) -> UpdateVTLDeviceTypeOutputTypeDef:
        """
        Updates the type of medium changer in a tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update_vtl_device_type)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> DescribeTapeArchivesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetapearchivespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> DescribeTapeRecoveryPointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetaperecoverypointspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_tapes"]) -> DescribeTapesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetapespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> DescribeVTLDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describevtldevicespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_file_shares"]) -> ListFileSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listfilesharespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_file_system_associations"]
    ) -> ListFileSystemAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileSystemAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listfilesystemassociationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listgatewayspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tape_pools"]) -> ListTapePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtapepoolspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tapes"]) -> ListTapesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtapespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_volumes"]) -> ListVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listvolumespaginator)
        """
