"""
Type annotations for efs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_efs import EFSClient

    client: EFSClient = boto3.client("efs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import PerformanceModeType, ResourceIdTypeType, ThroughputModeType
from .paginator import (
    DescribeFileSystemsPaginator,
    DescribeMountTargetsPaginator,
    DescribeTagsPaginator,
)
from .type_defs import (
    AccessPointDescriptionResponseMetadataTypeDef,
    BackupPolicyDescriptionTypeDef,
    BackupPolicyTypeDef,
    DescribeAccessPointsResponseTypeDef,
    DescribeAccountPreferencesResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetSecurityGroupsResponseTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeTagsResponseTypeDef,
    FileSystemDescriptionResponseMetadataTypeDef,
    FileSystemPolicyDescriptionTypeDef,
    LifecycleConfigurationDescriptionTypeDef,
    LifecyclePolicyTypeDef,
    ListTagsForResourceResponseTypeDef,
    MountTargetDescriptionResponseMetadataTypeDef,
    PosixUserTypeDef,
    PutAccountPreferencesResponseTypeDef,
    RootDirectoryTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EFSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessPointAlreadyExists: Type[BotocoreClientError]
    AccessPointLimitExceeded: Type[BotocoreClientError]
    AccessPointNotFound: Type[BotocoreClientError]
    AvailabilityZonesMismatch: Type[BotocoreClientError]
    BadRequest: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyTimeout: Type[BotocoreClientError]
    FileSystemAlreadyExists: Type[BotocoreClientError]
    FileSystemInUse: Type[BotocoreClientError]
    FileSystemLimitExceeded: Type[BotocoreClientError]
    FileSystemNotFound: Type[BotocoreClientError]
    IncorrectFileSystemLifeCycleState: Type[BotocoreClientError]
    IncorrectMountTargetState: Type[BotocoreClientError]
    InsufficientThroughputCapacity: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidPolicyException: Type[BotocoreClientError]
    IpAddressInUse: Type[BotocoreClientError]
    MountTargetConflict: Type[BotocoreClientError]
    MountTargetNotFound: Type[BotocoreClientError]
    NetworkInterfaceLimitExceeded: Type[BotocoreClientError]
    NoFreeAddressesInSubnet: Type[BotocoreClientError]
    PolicyNotFound: Type[BotocoreClientError]
    SecurityGroupLimitExceeded: Type[BotocoreClientError]
    SecurityGroupNotFound: Type[BotocoreClientError]
    SubnetNotFound: Type[BotocoreClientError]
    ThroughputLimitExceeded: Type[BotocoreClientError]
    TooManyRequests: Type[BotocoreClientError]
    UnsupportedAvailabilityZone: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EFSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        EFSClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#can_paginate)
        """
    def create_access_point(
        self,
        *,
        ClientToken: str,
        FileSystemId: str,
        Tags: List["TagTypeDef"] = None,
        PosixUser: "PosixUserTypeDef" = None,
        RootDirectory: "RootDirectoryTypeDef" = None
    ) -> AccessPointDescriptionResponseMetadataTypeDef:
        """
        Creates an EFS access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.create_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#create_access_point)
        """
    def create_file_system(
        self,
        *,
        CreationToken: str,
        PerformanceMode: PerformanceModeType = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        ThroughputMode: ThroughputModeType = None,
        ProvisionedThroughputInMibps: float = None,
        AvailabilityZoneName: str = None,
        Backup: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> FileSystemDescriptionResponseMetadataTypeDef:
        """
        Creates a new, empty file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.create_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#create_file_system)
        """
    def create_mount_target(
        self,
        *,
        FileSystemId: str,
        SubnetId: str,
        IpAddress: str = None,
        SecurityGroups: List[str] = None
    ) -> MountTargetDescriptionResponseMetadataTypeDef:
        """
        Creates a mount target for a file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.create_mount_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#create_mount_target)
        """
    def create_tags(self, *, FileSystemId: str, Tags: List["TagTypeDef"]) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#create_tags)
        """
    def delete_access_point(self, *, AccessPointId: str) -> None:
        """
        Deletes the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.delete_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#delete_access_point)
        """
    def delete_file_system(self, *, FileSystemId: str) -> None:
        """
        Deletes a file system, permanently severing access to its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.delete_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#delete_file_system)
        """
    def delete_file_system_policy(self, *, FileSystemId: str) -> None:
        """
        Deletes the `FileSystemPolicy` for the specified file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.delete_file_system_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#delete_file_system_policy)
        """
    def delete_mount_target(self, *, MountTargetId: str) -> None:
        """
        Deletes the specified mount target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.delete_mount_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#delete_mount_target)
        """
    def delete_tags(self, *, FileSystemId: str, TagKeys: List[str]) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#delete_tags)
        """
    def describe_access_points(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        AccessPointId: str = None,
        FileSystemId: str = None
    ) -> DescribeAccessPointsResponseTypeDef:
        """
        Returns the description of a specific Amazon EFS access point if the
        `AccessPointId` is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_access_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_access_points)
        """
    def describe_account_preferences(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAccountPreferencesResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasti
        cfilesystem-2015-02-01/DescribeAccountPreferences>`_ **Request Syntax** response
        = client.describe_account_preferences( NextToken='string', MaxResults=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_account_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_account_preferences)
        """
    def describe_backup_policy(self, *, FileSystemId: str) -> BackupPolicyDescriptionTypeDef:
        """
        Returns the backup policy for the specified EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_backup_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_backup_policy)
        """
    def describe_file_system_policy(
        self, *, FileSystemId: str
    ) -> FileSystemPolicyDescriptionTypeDef:
        """
        Returns the `FileSystemPolicy` for the specified EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_file_system_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_file_system_policy)
        """
    def describe_file_systems(
        self,
        *,
        MaxItems: int = None,
        Marker: str = None,
        CreationToken: str = None,
        FileSystemId: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        Returns the description of a specific Amazon EFS file system if either the file
        system `CreationToken` or the `FileSystemId` is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_file_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_file_systems)
        """
    def describe_lifecycle_configuration(
        self, *, FileSystemId: str
    ) -> LifecycleConfigurationDescriptionTypeDef:
        """
        Returns the current `LifecycleConfiguration` object for the specified Amazon EFS
        file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_lifecycle_configuration)
        """
    def describe_mount_target_security_groups(
        self, *, MountTargetId: str
    ) -> DescribeMountTargetSecurityGroupsResponseTypeDef:
        """
        Returns the security groups currently in effect for a mount target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_mount_target_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_mount_target_security_groups)
        """
    def describe_mount_targets(
        self,
        *,
        MaxItems: int = None,
        Marker: str = None,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None
    ) -> DescribeMountTargetsResponseTypeDef:
        """
        Returns the descriptions of all the current mount targets, or a specific mount
        target, for a file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_mount_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_mount_targets)
        """
    def describe_tags(
        self, *, FileSystemId: str, MaxItems: int = None, Marker: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#describe_tags)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#generate_presigned_url)
        """
    def list_tags_for_resource(
        self, *, ResourceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags for a top-level EFS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#list_tags_for_resource)
        """
    def modify_mount_target_security_groups(
        self, *, MountTargetId: str, SecurityGroups: List[str] = None
    ) -> None:
        """
        Modifies the set of security groups in effect for a mount target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.modify_mount_target_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#modify_mount_target_security_groups)
        """
    def put_account_preferences(
        self, *, ResourceIdType: ResourceIdTypeType
    ) -> PutAccountPreferencesResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasti
        cfilesystem-2015-02-01/PutAccountPreferences>`_ **Request Syntax** response =
        client.put_account_preferences( ResourceIdType='LONG_ID'|'SHORT_ID' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.put_account_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#put_account_preferences)
        """
    def put_backup_policy(
        self, *, FileSystemId: str, BackupPolicy: "BackupPolicyTypeDef"
    ) -> BackupPolicyDescriptionTypeDef:
        """
        Updates the file system's backup policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.put_backup_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#put_backup_policy)
        """
    def put_file_system_policy(
        self, *, FileSystemId: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> FileSystemPolicyDescriptionTypeDef:
        """
        Applies an Amazon EFS `FileSystemPolicy` to an Amazon EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.put_file_system_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#put_file_system_policy)
        """
    def put_lifecycle_configuration(
        self, *, FileSystemId: str, LifecyclePolicies: List["LifecyclePolicyTypeDef"]
    ) -> LifecycleConfigurationDescriptionTypeDef:
        """
        Enables lifecycle management by creating a new `LifecycleConfiguration` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.put_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#put_lifecycle_configuration)
        """
    def tag_resource(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Creates a tag for an EFS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceId: str, TagKeys: List[str]) -> None:
        """
        Removes tags from an EFS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#untag_resource)
        """
    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ThroughputMode: ThroughputModeType = None,
        ProvisionedThroughputInMibps: float = None
    ) -> FileSystemDescriptionResponseMetadataTypeDef:
        """
        Updates the throughput mode or the amount of provisioned throughput of an
        existing file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Client.update_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/client.html#update_file_system)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describefilesystemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mount_targets"]
    ) -> DescribeMountTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describemounttargetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/efs.html#EFS.Paginator.DescribeTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/paginators.html#describetagspaginator)
        """
