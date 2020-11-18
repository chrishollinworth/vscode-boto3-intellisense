# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for workspaces service client

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces import WorkSpacesClient

    client: WorkSpacesClient = boto3.client("workspaces")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_workspaces.paginator import (
    DescribeAccountModificationsPaginator,
    DescribeIpGroupsPaginator,
    DescribeWorkspaceBundlesPaginator,
    DescribeWorkspaceDirectoriesPaginator,
    DescribeWorkspaceImagesPaginator,
    DescribeWorkspacesConnectionStatusPaginator,
    DescribeWorkspacesPaginator,
    ListAvailableManagementCidrRangesPaginator,
)
from mypy_boto3_workspaces.type_defs import (
    AssociateConnectionAliasResultTypeDef,
    ClientPropertiesTypeDef,
    ConnectionAliasPermissionTypeDef,
    CopyWorkspaceImageResultTypeDef,
    CreateConnectionAliasResultTypeDef,
    CreateIpGroupResultTypeDef,
    CreateWorkspacesResultTypeDef,
    DescribeAccountModificationsResultTypeDef,
    DescribeAccountResultTypeDef,
    DescribeClientPropertiesResultTypeDef,
    DescribeConnectionAliasesResultTypeDef,
    DescribeConnectionAliasPermissionsResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagePermissionsResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspaceSnapshotsResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ImportWorkspaceImageResultTypeDef,
    IpRuleItemTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    MigrateWorkspaceResultTypeDef,
    RebootRequestTypeDef,
    RebootWorkspacesResultTypeDef,
    RebuildRequestTypeDef,
    RebuildWorkspacesResultTypeDef,
    SelfservicePermissionsTypeDef,
    StartRequestTypeDef,
    StartWorkspacesResultTypeDef,
    StopRequestTypeDef,
    StopWorkspacesResultTypeDef,
    TagTypeDef,
    TerminateRequestTypeDef,
    TerminateWorkspacesResultTypeDef,
    WorkspaceAccessPropertiesTypeDef,
    WorkspaceCreationPropertiesTypeDef,
    WorkspacePropertiesTypeDef,
    WorkspaceRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkSpacesClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidParameterValuesException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    OperationInProgressException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceAssociatedException: Type[BotocoreClientError]
    ResourceCreationFailedException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    UnsupportedNetworkConfigurationException: Type[BotocoreClientError]
    UnsupportedWorkspaceConfigurationException: Type[BotocoreClientError]
    WorkspacesDefaultRoleNotFoundException: Type[BotocoreClientError]


class WorkSpacesClient:
    """
    [WorkSpaces.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_connection_alias(
        self, AliasId: str, ResourceId: str
    ) -> AssociateConnectionAliasResultTypeDef:
        """
        [Client.associate_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.associate_connection_alias)
        """

    def associate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.associate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)
        """

    def authorize_ip_rules(
        self, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.authorize_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)
        """

    def copy_workspace_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyWorkspaceImageResultTypeDef:
        """
        [Client.copy_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)
        """

    def create_connection_alias(
        self, ConnectionString: str, Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionAliasResultTypeDef:
        """
        [Client.create_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.create_connection_alias)
        """

    def create_ip_group(
        self,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List["IpRuleItemTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateIpGroupResultTypeDef:
        """
        [Client.create_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)
        """

    def create_tags(self, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.create_tags)
        """

    def create_workspaces(
        self, Workspaces: List["WorkspaceRequestTypeDef"]
    ) -> CreateWorkspacesResultTypeDef:
        """
        [Client.create_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)
        """

    def delete_connection_alias(self, AliasId: str) -> Dict[str, Any]:
        """
        [Client.delete_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.delete_connection_alias)
        """

    def delete_ip_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)
        """

    def delete_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)
        """

    def delete_workspace_image(self, ImageId: str) -> Dict[str, Any]:
        """
        [Client.delete_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)
        """

    def deregister_workspace_directory(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.deregister_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)
        """

    def describe_account(self) -> DescribeAccountResultTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_account)
        """

    def describe_account_modifications(
        self, NextToken: str = None
    ) -> DescribeAccountModificationsResultTypeDef:
        """
        [Client.describe_account_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)
        """

    def describe_client_properties(
        self, ResourceIds: List[str]
    ) -> DescribeClientPropertiesResultTypeDef:
        """
        [Client.describe_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)
        """

    def describe_connection_alias_permissions(
        self, AliasId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeConnectionAliasPermissionsResultTypeDef:
        """
        [Client.describe_connection_alias_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_alias_permissions)
        """

    def describe_connection_aliases(
        self,
        AliasIds: List[str] = None,
        ResourceId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeConnectionAliasesResultTypeDef:
        """
        [Client.describe_connection_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_aliases)
        """

    def describe_ip_groups(
        self, GroupIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeIpGroupsResultTypeDef:
        """
        [Client.describe_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)
        """

    def describe_tags(self, ResourceId: str) -> DescribeTagsResultTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)
        """

    def describe_workspace_bundles(
        self, BundleIds: List[str] = None, Owner: str = None, NextToken: str = None
    ) -> DescribeWorkspaceBundlesResultTypeDef:
        """
        [Client.describe_workspace_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)
        """

    def describe_workspace_directories(
        self, DirectoryIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeWorkspaceDirectoriesResultTypeDef:
        """
        [Client.describe_workspace_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)
        """

    def describe_workspace_image_permissions(
        self, ImageId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeWorkspaceImagePermissionsResultTypeDef:
        """
        [Client.describe_workspace_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_image_permissions)
        """

    def describe_workspace_images(
        self,
        ImageIds: List[str] = None,
        ImageType: Literal["OWNED", "SHARED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeWorkspaceImagesResultTypeDef:
        """
        [Client.describe_workspace_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)
        """

    def describe_workspace_snapshots(
        self, WorkspaceId: str
    ) -> DescribeWorkspaceSnapshotsResultTypeDef:
        """
        [Client.describe_workspace_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)
        """

    def describe_workspaces(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeWorkspacesResultTypeDef:
        """
        [Client.describe_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)
        """

    def describe_workspaces_connection_status(
        self, WorkspaceIds: List[str] = None, NextToken: str = None
    ) -> DescribeWorkspacesConnectionStatusResultTypeDef:
        """
        [Client.describe_workspaces_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)
        """

    def disassociate_connection_alias(self, AliasId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.disassociate_connection_alias)
        """

    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.disassociate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)
        """

    def import_workspace_image(
        self,
        Ec2ImageId: str,
        IngestionProcess: Literal["BYOL_REGULAR", "BYOL_GRAPHICS", "BYOL_GRAPHICSPRO"],
        ImageName: str,
        ImageDescription: str,
        Tags: List["TagTypeDef"] = None,
        Applications: List[Literal["Microsoft_Office_2016", "Microsoft_Office_2019"]] = None,
    ) -> ImportWorkspaceImageResultTypeDef:
        """
        [Client.import_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)
        """

    def list_available_management_cidr_ranges(
        self, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAvailableManagementCidrRangesResultTypeDef:
        """
        [Client.list_available_management_cidr_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)
        """

    def migrate_workspace(
        self, SourceWorkspaceId: str, BundleId: str
    ) -> MigrateWorkspaceResultTypeDef:
        """
        [Client.migrate_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.migrate_workspace)
        """

    def modify_account(
        self,
        DedicatedTenancySupport: Literal["ENABLED"] = None,
        DedicatedTenancyManagementCidrRange: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.modify_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_account)
        """

    def modify_client_properties(
        self, ResourceId: str, ClientProperties: "ClientPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.modify_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)
        """

    def modify_selfservice_permissions(
        self, ResourceId: str, SelfservicePermissions: "SelfservicePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.modify_selfservice_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)
        """

    def modify_workspace_access_properties(
        self, ResourceId: str, WorkspaceAccessProperties: "WorkspaceAccessPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_access_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)
        """

    def modify_workspace_creation_properties(
        self, ResourceId: str, WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_creation_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)
        """

    def modify_workspace_properties(
        self, WorkspaceId: str, WorkspaceProperties: "WorkspacePropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)
        """

    def modify_workspace_state(
        self, WorkspaceId: str, WorkspaceState: Literal["AVAILABLE", "ADMIN_MAINTENANCE"]
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)
        """

    def reboot_workspaces(
        self, RebootWorkspaceRequests: List[RebootRequestTypeDef]
    ) -> RebootWorkspacesResultTypeDef:
        """
        [Client.reboot_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)
        """

    def rebuild_workspaces(
        self, RebuildWorkspaceRequests: List[RebuildRequestTypeDef]
    ) -> RebuildWorkspacesResultTypeDef:
        """
        [Client.rebuild_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)
        """

    def register_workspace_directory(
        self,
        DirectoryId: str,
        EnableWorkDocs: bool,
        SubnetIds: List[str] = None,
        EnableSelfService: bool = None,
        Tenancy: Literal["DEDICATED", "SHARED"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.register_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)
        """

    def restore_workspace(self, WorkspaceId: str) -> Dict[str, Any]:
        """
        [Client.restore_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)
        """

    def revoke_ip_rules(self, GroupId: str, UserRules: List[str]) -> Dict[str, Any]:
        """
        [Client.revoke_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)
        """

    def start_workspaces(
        self, StartWorkspaceRequests: List[StartRequestTypeDef]
    ) -> StartWorkspacesResultTypeDef:
        """
        [Client.start_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)
        """

    def stop_workspaces(
        self, StopWorkspaceRequests: List[StopRequestTypeDef]
    ) -> StopWorkspacesResultTypeDef:
        """
        [Client.stop_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)
        """

    def terminate_workspaces(
        self, TerminateWorkspaceRequests: List[TerminateRequestTypeDef]
    ) -> TerminateWorkspacesResultTypeDef:
        """
        [Client.terminate_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)
        """

    def update_connection_alias_permission(
        self, AliasId: str, ConnectionAliasPermission: "ConnectionAliasPermissionTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.update_connection_alias_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.update_connection_alias_permission)
        """

    def update_rules_of_ip_group(
        self, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.update_rules_of_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)
        """

    def update_workspace_image_permission(
        self, ImageId: str, AllowCopyImage: bool, SharedAccountId: str
    ) -> Dict[str, Any]:
        """
        [Client.update_workspace_image_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_image_permission)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_modifications"]
    ) -> DescribeAccountModificationsPaginator:
        """
        [Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ip_groups"]
    ) -> DescribeIpGroupsPaginator:
        """
        [Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_bundles"]
    ) -> DescribeWorkspaceBundlesPaginator:
        """
        [Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_directories"]
    ) -> DescribeWorkspaceDirectoriesPaginator:
        """
        [Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_images"]
    ) -> DescribeWorkspaceImagesPaginator:
        """
        [Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces"]
    ) -> DescribeWorkspacesPaginator:
        """
        [Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces_connection_status"]
    ) -> DescribeWorkspacesConnectionStatusPaginator:
        """
        [Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_available_management_cidr_ranges"]
    ) -> ListAvailableManagementCidrRangesPaginator:
        """
        [Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
        """
