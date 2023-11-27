"""
Type annotations for finspace-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace_data import FinSpaceDataClient

    client: FinSpaceDataClient = boto3.client("finspace-data")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApiAccessType,
    ApplicationPermissionType,
    ChangeTypeType,
    DatasetKindType,
    UserTypeType,
    locationTypeType,
)
from .paginator import (
    ListChangesetsPaginator,
    ListDatasetsPaginator,
    ListDataViewsPaginator,
    ListPermissionGroupsPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AssociateUserToPermissionGroupResponseTypeDef,
    CreateChangesetResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDataViewResponseTypeDef,
    CreatePermissionGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    DatasetOwnerInfoTypeDef,
    DataViewDestinationTypeParamsTypeDef,
    DeleteDatasetResponseTypeDef,
    DeletePermissionGroupResponseTypeDef,
    DisableUserResponseTypeDef,
    DisassociateUserFromPermissionGroupResponseTypeDef,
    EnableUserResponseTypeDef,
    GetChangesetResponseTypeDef,
    GetDatasetResponseTypeDef,
    GetDataViewResponseTypeDef,
    GetExternalDataViewAccessDetailsResponseTypeDef,
    GetPermissionGroupResponseTypeDef,
    GetProgrammaticAccessCredentialsResponseTypeDef,
    GetUserResponseTypeDef,
    GetWorkingLocationResponseTypeDef,
    ListChangesetsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListDataViewsResponseTypeDef,
    ListPermissionGroupsByUserResponseTypeDef,
    ListPermissionGroupsResponseTypeDef,
    ListUsersByPermissionGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    PermissionGroupParamsTypeDef,
    ResetUserPasswordResponseTypeDef,
    SchemaUnionTypeDef,
    UpdateChangesetResponseTypeDef,
    UpdateDatasetResponseTypeDef,
    UpdatePermissionGroupResponseTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FinSpaceDataClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FinSpaceDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FinSpaceDataClient exceptions.
        """
    def associate_user_to_permission_group(
        self, *, permissionGroupId: str, userId: str, clientToken: str = None
    ) -> AssociateUserToPermissionGroupResponseTypeDef:
        """
        Adds a user to a permission group to grant permissions for actions a user can
        perform in FinSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.associate_user_to_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#associate_user_to_permission_group)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#close)
        """
    def create_changeset(
        self,
        *,
        datasetId: str,
        changeType: ChangeTypeType,
        sourceParams: Dict[str, str],
        formatParams: Dict[str, str],
        clientToken: str = None
    ) -> CreateChangesetResponseTypeDef:
        """
        Creates a new Changeset in a FinSpace Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.create_changeset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_changeset)
        """
    def create_data_view(
        self,
        *,
        datasetId: str,
        destinationTypeParams: "DataViewDestinationTypeParamsTypeDef",
        clientToken: str = None,
        autoUpdate: bool = None,
        sortColumns: List[str] = None,
        partitionColumns: List[str] = None,
        asOfTimestamp: int = None
    ) -> CreateDataViewResponseTypeDef:
        """
        Creates a Dataview for a Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.create_data_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_data_view)
        """
    def create_dataset(
        self,
        *,
        datasetTitle: str,
        kind: DatasetKindType,
        permissionGroupParams: "PermissionGroupParamsTypeDef",
        clientToken: str = None,
        datasetDescription: str = None,
        ownerInfo: "DatasetOwnerInfoTypeDef" = None,
        alias: str = None,
        schemaDefinition: "SchemaUnionTypeDef" = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a new FinSpace Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_dataset)
        """
    def create_permission_group(
        self,
        *,
        name: str,
        applicationPermissions: List[ApplicationPermissionType],
        description: str = None,
        clientToken: str = None
    ) -> CreatePermissionGroupResponseTypeDef:
        """
        Creates a group of permissions for various actions that a user can perform in
        FinSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.create_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_permission_group)
        """
    def create_user(
        self,
        *,
        emailAddress: str,
        type: UserTypeType,
        firstName: str = None,
        lastName: str = None,
        apiAccess: ApiAccessType = None,
        apiAccessPrincipalArn: str = None,
        clientToken: str = None
    ) -> CreateUserResponseTypeDef:
        """
        Creates a new user in FinSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_user)
        """
    def delete_dataset(
        self, *, datasetId: str, clientToken: str = None
    ) -> DeleteDatasetResponseTypeDef:
        """
        Deletes a FinSpace Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#delete_dataset)
        """
    def delete_permission_group(
        self, *, permissionGroupId: str, clientToken: str = None
    ) -> DeletePermissionGroupResponseTypeDef:
        """
        Deletes a permission group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.delete_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#delete_permission_group)
        """
    def disable_user(self, *, userId: str, clientToken: str = None) -> DisableUserResponseTypeDef:
        """
        Denies access to the FinSpace web application and API for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.disable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#disable_user)
        """
    def disassociate_user_from_permission_group(
        self, *, permissionGroupId: str, userId: str, clientToken: str = None
    ) -> DisassociateUserFromPermissionGroupResponseTypeDef:
        """
        Removes a user from a permission group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.disassociate_user_from_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#disassociate_user_from_permission_group)
        """
    def enable_user(self, *, userId: str, clientToken: str = None) -> EnableUserResponseTypeDef:
        """
        Allows the specified user to access the FinSpace web application and API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.enable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#enable_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#generate_presigned_url)
        """
    def get_changeset(self, *, datasetId: str, changesetId: str) -> GetChangesetResponseTypeDef:
        """
        Get information about a Changeset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_changeset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_changeset)
        """
    def get_data_view(self, *, dataViewId: str, datasetId: str) -> GetDataViewResponseTypeDef:
        """
        Gets information about a Dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_data_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_data_view)
        """
    def get_dataset(self, *, datasetId: str) -> GetDatasetResponseTypeDef:
        """
        Returns information about a Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_dataset)
        """
    def get_external_data_view_access_details(
        self, *, dataViewId: str, datasetId: str
    ) -> GetExternalDataViewAccessDetailsResponseTypeDef:
        """
        Returns the credentials to access the external Dataview from an S3 location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_external_data_view_access_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_external_data_view_access_details)
        """
    def get_permission_group(self, *, permissionGroupId: str) -> GetPermissionGroupResponseTypeDef:
        """
        Retrieves the details of a specific permission group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_permission_group)
        """
    def get_programmatic_access_credentials(
        self, *, environmentId: str, durationInMinutes: int = None
    ) -> GetProgrammaticAccessCredentialsResponseTypeDef:
        """
        Request programmatic credentials to use with FinSpace SDK.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_programmatic_access_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_programmatic_access_credentials)
        """
    def get_user(self, *, userId: str) -> GetUserResponseTypeDef:
        """
        Retrieves details for a specific user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_user)
        """
    def get_working_location(
        self, *, locationType: locationTypeType = None
    ) -> GetWorkingLocationResponseTypeDef:
        """
        A temporary Amazon S3 location, where you can copy your files from a source
        location to stage or use as a scratch space in FinSpace notebook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.get_working_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_working_location)
        """
    def list_changesets(
        self, *, datasetId: str, maxResults: int = None, nextToken: str = None
    ) -> ListChangesetsResponseTypeDef:
        """
        Lists the FinSpace Changesets for a Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_changesets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_changesets)
        """
    def list_data_views(
        self, *, datasetId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataViewsResponseTypeDef:
        """
        Lists all available Dataviews for a Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_data_views)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_data_views)
        """
    def list_datasets(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists all of the active Datasets that a user has access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_datasets)
        """
    def list_permission_groups(
        self, *, maxResults: int, nextToken: str = None
    ) -> ListPermissionGroupsResponseTypeDef:
        """
        Lists all available permission groups in FinSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_permission_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_permission_groups)
        """
    def list_permission_groups_by_user(
        self, *, userId: str, maxResults: int, nextToken: str = None
    ) -> ListPermissionGroupsByUserResponseTypeDef:
        """
        Lists all the permission groups that are associated with a specific user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_permission_groups_by_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_permission_groups_by_user)
        """
    def list_users(self, *, maxResults: int, nextToken: str = None) -> ListUsersResponseTypeDef:
        """
        Lists all available users in FinSpace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_users)
        """
    def list_users_by_permission_group(
        self, *, permissionGroupId: str, maxResults: int, nextToken: str = None
    ) -> ListUsersByPermissionGroupResponseTypeDef:
        """
        Lists details of all the users in a specific permission group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.list_users_by_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#list_users_by_permission_group)
        """
    def reset_user_password(
        self, *, userId: str, clientToken: str = None
    ) -> ResetUserPasswordResponseTypeDef:
        """
        Resets the password for a specified user ID and generates a temporary one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.reset_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#reset_user_password)
        """
    def update_changeset(
        self,
        *,
        datasetId: str,
        changesetId: str,
        sourceParams: Dict[str, str],
        formatParams: Dict[str, str],
        clientToken: str = None
    ) -> UpdateChangesetResponseTypeDef:
        """
        Updates a FinSpace Changeset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.update_changeset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#update_changeset)
        """
    def update_dataset(
        self,
        *,
        datasetId: str,
        datasetTitle: str,
        kind: DatasetKindType,
        clientToken: str = None,
        datasetDescription: str = None,
        alias: str = None,
        schemaDefinition: "SchemaUnionTypeDef" = None
    ) -> UpdateDatasetResponseTypeDef:
        """
        Updates a FinSpace Dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.update_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#update_dataset)
        """
    def update_permission_group(
        self,
        *,
        permissionGroupId: str,
        name: str = None,
        description: str = None,
        applicationPermissions: List[ApplicationPermissionType] = None,
        clientToken: str = None
    ) -> UpdatePermissionGroupResponseTypeDef:
        """
        Modifies the details of a permission group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.update_permission_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#update_permission_group)
        """
    def update_user(
        self,
        *,
        userId: str,
        type: UserTypeType = None,
        firstName: str = None,
        lastName: str = None,
        apiAccess: ApiAccessType = None,
        apiAccessPrincipalArn: str = None,
        clientToken: str = None
    ) -> UpdateUserResponseTypeDef:
        """
        Modifies the details of the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#update_user)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_changesets"]) -> ListChangesetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Paginator.ListChangesets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listchangesetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_data_views"]) -> ListDataViewsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDataViews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdataviewspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_groups"]
    ) -> ListPermissionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Paginator.ListPermissionGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listpermissiongroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/finspace-data.html#FinSpaceData.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listuserspaginator)
        """
