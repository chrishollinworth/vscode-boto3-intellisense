"""
Type annotations for workspaces service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces import WorkSpacesClient

    client: WorkSpacesClient = boto3.client("workspaces")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApplicationType,
    ClientDeviceTypeType,
    DeletableSamlPropertyType,
    ImageTypeType,
    TargetWorkspaceStateType,
    TenancyType,
    WorkspaceImageIngestionProcessType,
)
from .paginator import (
    DescribeAccountModificationsPaginator,
    DescribeIpGroupsPaginator,
    DescribeWorkspaceBundlesPaginator,
    DescribeWorkspaceDirectoriesPaginator,
    DescribeWorkspaceImagesPaginator,
    DescribeWorkspacesConnectionStatusPaginator,
    DescribeWorkspacesPaginator,
    ListAvailableManagementCidrRangesPaginator,
)
from .type_defs import (
    AssociateConnectionAliasResultTypeDef,
    CertificateBasedAuthPropertiesTypeDef,
    ClientPropertiesTypeDef,
    ComputeTypeTypeDef,
    ConnectionAliasPermissionTypeDef,
    CopyWorkspaceImageResultTypeDef,
    CreateConnectClientAddInResultTypeDef,
    CreateConnectionAliasResultTypeDef,
    CreateIpGroupResultTypeDef,
    CreateStandbyWorkspacesResultTypeDef,
    CreateUpdatedWorkspaceImageResultTypeDef,
    CreateWorkspaceBundleResultTypeDef,
    CreateWorkspaceImageResultTypeDef,
    CreateWorkspacesResultTypeDef,
    DefaultImportClientBrandingAttributesTypeDef,
    DescribeAccountModificationsResultTypeDef,
    DescribeAccountResultTypeDef,
    DescribeClientBrandingResultTypeDef,
    DescribeClientPropertiesResultTypeDef,
    DescribeConnectClientAddInsResultTypeDef,
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
    ImportClientBrandingResultTypeDef,
    ImportWorkspaceImageResultTypeDef,
    IosImportClientBrandingAttributesTypeDef,
    IpRuleItemTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    MigrateWorkspaceResultTypeDef,
    RebootRequestTypeDef,
    RebootWorkspacesResultTypeDef,
    RebuildRequestTypeDef,
    RebuildWorkspacesResultTypeDef,
    RootStorageTypeDef,
    SamlPropertiesTypeDef,
    SelfservicePermissionsTypeDef,
    StandbyWorkspaceTypeDef,
    StartRequestTypeDef,
    StartWorkspacesResultTypeDef,
    StopRequestTypeDef,
    StopWorkspacesResultTypeDef,
    TagTypeDef,
    TerminateRequestTypeDef,
    TerminateWorkspacesResultTypeDef,
    UserStorageTypeDef,
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

class WorkSpacesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkSpacesClient exceptions.
        """
    def associate_connection_alias(
        self, *, AliasId: str, ResourceId: str
    ) -> AssociateConnectionAliasResultTypeDef:
        """
        Associates the specified connection alias with the specified directory to enable
        cross-Region redirection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.associate_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#associate_connection_alias)
        """
    def associate_ip_groups(self, *, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        Associates the specified IP access control group with the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#associate_ip_groups)
        """
    def authorize_ip_rules(
        self, *, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        Adds one or more rules to the specified IP access control group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#authorize_ip_rules)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#close)
        """
    def copy_workspace_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CopyWorkspaceImageResultTypeDef:
        """
        Copies the specified image from the specified Region to the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#copy_workspace_image)
        """
    def create_connect_client_add_in(
        self, *, ResourceId: str, Name: str, URL: str
    ) -> CreateConnectClientAddInResultTypeDef:
        """
        Creates a client-add-in for Amazon Connect within a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_connect_client_add_in)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_connect_client_add_in)
        """
    def create_connection_alias(
        self, *, ConnectionString: str, Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionAliasResultTypeDef:
        """
        Creates the specified connection alias for use with cross-Region redirection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_connection_alias)
        """
    def create_ip_group(
        self,
        *,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List["IpRuleItemTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateIpGroupResultTypeDef:
        """
        Creates an IP access control group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_ip_group)
        """
    def create_standby_workspaces(
        self, *, PrimaryRegion: str, StandbyWorkspaces: List["StandbyWorkspaceTypeDef"]
    ) -> CreateStandbyWorkspacesResultTypeDef:
        """
        Creates a Standby WorkSpace in a secondary region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_standby_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_standby_workspaces)
        """
    def create_tags(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Creates the specified tags for the specified WorkSpaces resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_tags)
        """
    def create_updated_workspace_image(
        self, *, Name: str, Description: str, SourceImageId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateUpdatedWorkspaceImageResultTypeDef:
        """
        Creates a new updated WorkSpace image based on the specified source image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_updated_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_updated_workspace_image)
        """
    def create_workspace_bundle(
        self,
        *,
        BundleName: str,
        BundleDescription: str,
        ImageId: str,
        ComputeType: "ComputeTypeTypeDef",
        UserStorage: "UserStorageTypeDef",
        RootStorage: "RootStorageTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWorkspaceBundleResultTypeDef:
        """
        Creates the specified WorkSpace bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_workspace_bundle)
        """
    def create_workspace_image(
        self, *, Name: str, Description: str, WorkspaceId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateWorkspaceImageResultTypeDef:
        """
        Creates a new WorkSpace image from an existing WorkSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_workspace_image)
        """
    def create_workspaces(
        self, *, Workspaces: List["WorkspaceRequestTypeDef"]
    ) -> CreateWorkspacesResultTypeDef:
        """
        Creates one or more WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_workspaces)
        """
    def delete_client_branding(
        self, *, ResourceId: str, Platforms: List[ClientDeviceTypeType]
    ) -> Dict[str, Any]:
        """
        Deletes customized client branding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_client_branding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_client_branding)
        """
    def delete_connect_client_add_in(self, *, AddInId: str, ResourceId: str) -> Dict[str, Any]:
        """
        Deletes a client-add-in for Amazon Connect that is configured within a
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_connect_client_add_in)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_connect_client_add_in)
        """
    def delete_connection_alias(self, *, AliasId: str) -> Dict[str, Any]:
        """
        Deletes the specified connection alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_connection_alias)
        """
    def delete_ip_group(self, *, GroupId: str) -> Dict[str, Any]:
        """
        Deletes the specified IP access control group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_ip_group)
        """
    def delete_tags(self, *, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from the specified WorkSpaces resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_tags)
        """
    def delete_workspace_bundle(self, *, BundleId: str = None) -> Dict[str, Any]:
        """
        Deletes the specified WorkSpace bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_workspace_bundle)
        """
    def delete_workspace_image(self, *, ImageId: str) -> Dict[str, Any]:
        """
        Deletes the specified image from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_workspace_image)
        """
    def deregister_workspace_directory(self, *, DirectoryId: str) -> Dict[str, Any]:
        """
        Deregisters the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#deregister_workspace_directory)
        """
    def describe_account(self) -> DescribeAccountResultTypeDef:
        """
        Retrieves a list that describes the configuration of Bring Your Own License
        (BYOL) for the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_account)
        """
    def describe_account_modifications(
        self, *, NextToken: str = None
    ) -> DescribeAccountModificationsResultTypeDef:
        """
        Retrieves a list that describes modifications to the configuration of Bring Your
        Own License (BYOL) for the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_account_modifications)
        """
    def describe_client_branding(self, *, ResourceId: str) -> DescribeClientBrandingResultTypeDef:
        """
        Describes the specified client branding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_client_branding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_client_branding)
        """
    def describe_client_properties(
        self, *, ResourceIds: List[str]
    ) -> DescribeClientPropertiesResultTypeDef:
        """
        Retrieves a list that describes one or more specified Amazon WorkSpaces clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_client_properties)
        """
    def describe_connect_client_add_ins(
        self, *, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeConnectClientAddInsResultTypeDef:
        """
        Retrieves a list of Amazon Connect client add-ins that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_connect_client_add_ins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_connect_client_add_ins)
        """
    def describe_connection_alias_permissions(
        self, *, AliasId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeConnectionAliasPermissionsResultTypeDef:
        """
        Describes the permissions that the owner of a connection alias has granted to
        another Amazon Web Services account for the specified connection alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_alias_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_connection_alias_permissions)
        """
    def describe_connection_aliases(
        self,
        *,
        AliasIds: List[str] = None,
        ResourceId: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeConnectionAliasesResultTypeDef:
        """
        Retrieves a list that describes the connection aliases used for cross-Region
        redirection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_connection_aliases)
        """
    def describe_ip_groups(
        self, *, GroupIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeIpGroupsResultTypeDef:
        """
        Describes one or more of your IP access control groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_ip_groups)
        """
    def describe_tags(self, *, ResourceId: str) -> DescribeTagsResultTypeDef:
        """
        Describes the specified tags for the specified WorkSpaces resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_tags)
        """
    def describe_workspace_bundles(
        self, *, BundleIds: List[str] = None, Owner: str = None, NextToken: str = None
    ) -> DescribeWorkspaceBundlesResultTypeDef:
        """
        Retrieves a list that describes the available WorkSpace bundles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_bundles)
        """
    def describe_workspace_directories(
        self, *, DirectoryIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeWorkspaceDirectoriesResultTypeDef:
        """
        Describes the available directories that are registered with Amazon WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_directories)
        """
    def describe_workspace_image_permissions(
        self, *, ImageId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeWorkspaceImagePermissionsResultTypeDef:
        """
        Describes the permissions that the owner of an image has granted to other Amazon
        Web Services accounts for an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_image_permissions)
        """
    def describe_workspace_images(
        self,
        *,
        ImageIds: List[str] = None,
        ImageType: ImageTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeWorkspaceImagesResultTypeDef:
        """
        Retrieves a list that describes one or more specified images, if the image
        identifiers are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_images)
        """
    def describe_workspace_snapshots(
        self, *, WorkspaceId: str
    ) -> DescribeWorkspaceSnapshotsResultTypeDef:
        """
        Describes the snapshots for the specified WorkSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_snapshots)
        """
    def describe_workspaces(
        self,
        *,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeWorkspacesResultTypeDef:
        """
        Describes the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspaces)
        """
    def describe_workspaces_connection_status(
        self, *, WorkspaceIds: List[str] = None, NextToken: str = None
    ) -> DescribeWorkspacesConnectionStatusResultTypeDef:
        """
        Describes the connection status of the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspaces_connection_status)
        """
    def disassociate_connection_alias(self, *, AliasId: str) -> Dict[str, Any]:
        """
        Disassociates a connection alias from a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.disassociate_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#disassociate_connection_alias)
        """
    def disassociate_ip_groups(self, *, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        Disassociates the specified IP access control group from the specified
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#disassociate_ip_groups)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#generate_presigned_url)
        """
    def import_client_branding(
        self,
        *,
        ResourceId: str,
        DeviceTypeWindows: "DefaultImportClientBrandingAttributesTypeDef" = None,
        DeviceTypeOsx: "DefaultImportClientBrandingAttributesTypeDef" = None,
        DeviceTypeAndroid: "DefaultImportClientBrandingAttributesTypeDef" = None,
        DeviceTypeIos: "IosImportClientBrandingAttributesTypeDef" = None,
        DeviceTypeLinux: "DefaultImportClientBrandingAttributesTypeDef" = None,
        DeviceTypeWeb: "DefaultImportClientBrandingAttributesTypeDef" = None
    ) -> ImportClientBrandingResultTypeDef:
        """
        Imports client branding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.import_client_branding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#import_client_branding)
        """
    def import_workspace_image(
        self,
        *,
        Ec2ImageId: str,
        IngestionProcess: WorkspaceImageIngestionProcessType,
        ImageName: str,
        ImageDescription: str,
        Tags: List["TagTypeDef"] = None,
        Applications: List[ApplicationType] = None
    ) -> ImportWorkspaceImageResultTypeDef:
        """
        Imports the specified Windows 10 Bring Your Own License (BYOL) or Windows Server
        2016 BYOL image into Amazon WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#import_workspace_image)
        """
    def list_available_management_cidr_ranges(
        self, *, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAvailableManagementCidrRangesResultTypeDef:
        """
        Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you
        can use for the network management interface when you enable Bring Your Own
        License (BYOL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#list_available_management_cidr_ranges)
        """
    def migrate_workspace(
        self, *, SourceWorkspaceId: str, BundleId: str
    ) -> MigrateWorkspaceResultTypeDef:
        """
        Migrates a WorkSpace from one operating system or bundle type to another, while
        retaining the data on the user volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.migrate_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#migrate_workspace)
        """
    def modify_account(
        self,
        *,
        DedicatedTenancySupport: Literal["ENABLED"] = None,
        DedicatedTenancyManagementCidrRange: str = None
    ) -> Dict[str, Any]:
        """
        Modifies the configuration of Bring Your Own License (BYOL) for the specified
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_account)
        """
    def modify_certificate_based_auth_properties(
        self,
        *,
        ResourceId: str,
        CertificateBasedAuthProperties: "CertificateBasedAuthPropertiesTypeDef" = None,
        PropertiesToDelete: List[
            Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]
        ] = None
    ) -> Dict[str, Any]:
        """
        Modifies the properties of the certificate-based authentication you want to use
        with your WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_certificate_based_auth_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_certificate_based_auth_properties)
        """
    def modify_client_properties(
        self, *, ResourceId: str, ClientProperties: "ClientPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        Modifies the properties of the specified Amazon WorkSpaces clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_client_properties)
        """
    def modify_saml_properties(
        self,
        *,
        ResourceId: str,
        SamlProperties: "SamlPropertiesTypeDef" = None,
        PropertiesToDelete: List[DeletableSamlPropertyType] = None
    ) -> Dict[str, Any]:
        """
        Modifies multiple properties related to SAML 2.0 authentication, including the
        enablement status, user access URL, and relay state parameter name that are used
        for configuring federation with an SAML 2.0 identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_saml_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_saml_properties)
        """
    def modify_selfservice_permissions(
        self, *, ResourceId: str, SelfservicePermissions: "SelfservicePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Modifies the self-service WorkSpace management capabilities for your users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_selfservice_permissions)
        """
    def modify_workspace_access_properties(
        self, *, ResourceId: str, WorkspaceAccessProperties: "WorkspaceAccessPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        Specifies which devices and operating systems users can use to access their
        WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_access_properties)
        """
    def modify_workspace_creation_properties(
        self, *, ResourceId: str, WorkspaceCreationProperties: "WorkspaceCreationPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        Modify the default properties used to create WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_creation_properties)
        """
    def modify_workspace_properties(
        self, *, WorkspaceId: str, WorkspaceProperties: "WorkspacePropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        Modifies the specified WorkSpace properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_properties)
        """
    def modify_workspace_state(
        self, *, WorkspaceId: str, WorkspaceState: TargetWorkspaceStateType
    ) -> Dict[str, Any]:
        """
        Sets the state of the specified WorkSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_state)
        """
    def reboot_workspaces(
        self, *, RebootWorkspaceRequests: List["RebootRequestTypeDef"]
    ) -> RebootWorkspacesResultTypeDef:
        """
        Reboots the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#reboot_workspaces)
        """
    def rebuild_workspaces(
        self, *, RebuildWorkspaceRequests: List["RebuildRequestTypeDef"]
    ) -> RebuildWorkspacesResultTypeDef:
        """
        Rebuilds the specified WorkSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#rebuild_workspaces)
        """
    def register_workspace_directory(
        self,
        *,
        DirectoryId: str,
        EnableWorkDocs: bool,
        SubnetIds: List[str] = None,
        EnableSelfService: bool = None,
        Tenancy: TenancyType = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Registers the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#register_workspace_directory)
        """
    def restore_workspace(self, *, WorkspaceId: str) -> Dict[str, Any]:
        """
        Restores the specified WorkSpace to its last known healthy state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#restore_workspace)
        """
    def revoke_ip_rules(self, *, GroupId: str, UserRules: List[str]) -> Dict[str, Any]:
        """
        Removes one or more rules from the specified IP access control group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#revoke_ip_rules)
        """
    def start_workspaces(
        self, *, StartWorkspaceRequests: List["StartRequestTypeDef"]
    ) -> StartWorkspacesResultTypeDef:
        """
        Starts the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#start_workspaces)
        """
    def stop_workspaces(
        self, *, StopWorkspaceRequests: List["StopRequestTypeDef"]
    ) -> StopWorkspacesResultTypeDef:
        """
        Stops the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#stop_workspaces)
        """
    def terminate_workspaces(
        self, *, TerminateWorkspaceRequests: List["TerminateRequestTypeDef"]
    ) -> TerminateWorkspacesResultTypeDef:
        """
        Terminates the specified WorkSpaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#terminate_workspaces)
        """
    def update_connect_client_add_in(
        self, *, AddInId: str, ResourceId: str, Name: str = None, URL: str = None
    ) -> Dict[str, Any]:
        """
        Updates a Amazon Connect client add-in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.update_connect_client_add_in)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_connect_client_add_in)
        """
    def update_connection_alias_permission(
        self, *, AliasId: str, ConnectionAliasPermission: "ConnectionAliasPermissionTypeDef"
    ) -> Dict[str, Any]:
        """
        Shares or unshares a connection alias with one account by specifying whether
        that account has permission to associate the connection alias with a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.update_connection_alias_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_connection_alias_permission)
        """
    def update_rules_of_ip_group(
        self, *, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        Replaces the current rules of the specified IP access control group with the
        specified rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_rules_of_ip_group)
        """
    def update_workspace_bundle(
        self, *, BundleId: str = None, ImageId: str = None
    ) -> Dict[str, Any]:
        """
        Updates a WorkSpace bundle with a new image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_workspace_bundle)
        """
    def update_workspace_image_permission(
        self, *, ImageId: str, AllowCopyImage: bool, SharedAccountId: str
    ) -> Dict[str, Any]:
        """
        Shares or unshares an image with one account in the same Amazon Web Services
        Region by specifying whether that account has permission to copy the image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_image_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_workspace_image_permission)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_modifications"]
    ) -> DescribeAccountModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeaccountmodificationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ip_groups"]
    ) -> DescribeIpGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeipgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_bundles"]
    ) -> DescribeWorkspaceBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacebundlespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_directories"]
    ) -> DescribeWorkspaceDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacedirectoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_images"]
    ) -> DescribeWorkspaceImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspaceimagespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces"]
    ) -> DescribeWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces_connection_status"]
    ) -> DescribeWorkspacesConnectionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_available_management_cidr_ranges"]
    ) -> ListAvailableManagementCidrRangesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
        """
