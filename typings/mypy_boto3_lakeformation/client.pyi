"""
Type annotations for lakeformation service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lakeformation import LakeFormationClient

    client: LakeFormationClient = boto3.client("lakeformation")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import DataLakeResourceTypeType, PermissionType, ResourceShareTypeType
from .type_defs import (
    AddLFTagsToResourceResponseTypeDef,
    BatchGrantPermissionsResponseTypeDef,
    BatchPermissionsRequestEntryTypeDef,
    BatchRevokePermissionsResponseTypeDef,
    DataLakePrincipalTypeDef,
    DataLakeSettingsTypeDef,
    DescribeResourceResponseTypeDef,
    FilterConditionTypeDef,
    GetDataLakeSettingsResponseTypeDef,
    GetEffectivePermissionsForPathResponseTypeDef,
    GetLFTagResponseTypeDef,
    GetResourceLFTagsResponseTypeDef,
    LFTagPairTypeDef,
    LFTagTypeDef,
    ListLFTagsResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListResourcesResponseTypeDef,
    RemoveLFTagsFromResourceResponseTypeDef,
    ResourceTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
)

__all__ = ("LakeFormationClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    GlueEncryptionException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    ResourceNumberLimitExceededException: Type[BotocoreClientError]

class LakeFormationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        LakeFormationClient exceptions.
        """
    def add_lf_tags_to_resource(
        self,
        *,
        Resource: "ResourceTypeDef",
        LFTags: List["LFTagPairTypeDef"],
        CatalogId: str = None
    ) -> AddLFTagsToResourceResponseTypeDef:
        """
        Attaches one or more tags to an existing resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.add_lf_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#add_lf_tags_to_resource)
        """
    def batch_grant_permissions(
        self, *, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchGrantPermissionsResponseTypeDef:
        """
        Batch operation to grant permissions to the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch_grant_permissions)
        """
    def batch_revoke_permissions(
        self, *, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchRevokePermissionsResponseTypeDef:
        """
        Batch operation to revoke permissions from the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch_revoke_permissions)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#can_paginate)
        """
    def create_lf_tag(
        self, *, TagKey: str, TagValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Creates a tag with the specified name and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.create_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#create_lf_tag)
        """
    def delete_lf_tag(self, *, TagKey: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        Deletes the specified tag key name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.delete_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#delete_lf_tag)
        """
    def deregister_resource(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deregisters the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#deregister_resource)
        """
    def describe_resource(self, *, ResourceArn: str) -> DescribeResourceResponseTypeDef:
        """
        Retrieves the current data access role for the given resource registered in AWS
        Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#describe_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#generate_presigned_url)
        """
    def get_data_lake_settings(
        self, *, CatalogId: str = None
    ) -> GetDataLakeSettingsResponseTypeDef:
        """
        Retrieves the list of the data lake administrators of a Lake Formation-managed
        data lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_data_lake_settings)
        """
    def get_effective_permissions_for_path(
        self,
        *,
        ResourceArn: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetEffectivePermissionsForPathResponseTypeDef:
        """
        Returns the Lake Formation permissions for a specified table or database
        resource located at a path in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_effective_permissions_for_path)
        """
    def get_lf_tag(self, *, TagKey: str, CatalogId: str = None) -> GetLFTagResponseTypeDef:
        """
        Returns a tag definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.get_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_lf_tag)
        """
    def get_resource_lf_tags(
        self, *, Resource: "ResourceTypeDef", CatalogId: str = None, ShowAssignedLFTags: bool = None
    ) -> GetResourceLFTagsResponseTypeDef:
        """
        Returns the tags applied to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.get_resource_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_resource_lf_tags)
        """
    def grant_permissions(
        self,
        *,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[PermissionType],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[PermissionType] = None
    ) -> Dict[str, Any]:
        """
        Grants permissions to the principal to access metadata in the Data Catalog and
        data organized in underlying data storage such as Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#grant_permissions)
        """
    def list_lf_tags(
        self,
        *,
        CatalogId: str = None,
        ResourceShareType: ResourceShareTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListLFTagsResponseTypeDef:
        """
        Lists tags that the requester has permission to view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.list_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_lf_tags)
        """
    def list_permissions(
        self,
        *,
        CatalogId: str = None,
        Principal: "DataLakePrincipalTypeDef" = None,
        ResourceType: DataLakeResourceTypeType = None,
        Resource: "ResourceTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPermissionsResponseTypeDef:
        """
        Returns a list of the principal permissions on the resource, filtered by the
        permissions of the caller.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_permissions)
        """
    def list_resources(
        self,
        *,
        FilterConditionList: List["FilterConditionTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListResourcesResponseTypeDef:
        """
        Lists the resources registered to be managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_resources)
        """
    def put_data_lake_settings(
        self, *, DataLakeSettings: "DataLakeSettingsTypeDef", CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Sets the list of data lake administrators who have admin privileges on all
        resources managed by Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#put_data_lake_settings)
        """
    def register_resource(
        self, *, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        Registers the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.register_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#register_resource)
        """
    def remove_lf_tags_from_resource(
        self,
        *,
        Resource: "ResourceTypeDef",
        LFTags: List["LFTagPairTypeDef"],
        CatalogId: str = None
    ) -> RemoveLFTagsFromResourceResponseTypeDef:
        """
        Removes a tag from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.remove_lf_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#remove_lf_tags_from_resource)
        """
    def revoke_permissions(
        self,
        *,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[PermissionType],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[PermissionType] = None
    ) -> Dict[str, Any]:
        """
        Revokes permissions to the principal to access metadata in the Data Catalog and
        data organized in underlying data storage such as Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#revoke_permissions)
        """
    def search_databases_by_lf_tags(
        self,
        *,
        Expression: List["LFTagTypeDef"],
        NextToken: str = None,
        MaxResults: int = None,
        CatalogId: str = None
    ) -> SearchDatabasesByLFTagsResponseTypeDef:
        """
        This operation allows a search on `DATABASE` resources by `TagCondition`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.search_databases_by_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#search_databases_by_lf_tags)
        """
    def search_tables_by_lf_tags(
        self,
        *,
        Expression: List["LFTagTypeDef"],
        NextToken: str = None,
        MaxResults: int = None,
        CatalogId: str = None
    ) -> SearchTablesByLFTagsResponseTypeDef:
        """
        This operation allows a search on `TABLE` resources by `LFTag` s.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.search_tables_by_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#search_tables_by_lf_tags)
        """
    def update_lf_tag(
        self,
        *,
        TagKey: str,
        CatalogId: str = None,
        TagValuesToDelete: List[str] = None,
        TagValuesToAdd: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates the list of possible values for the specified tag key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.update_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_lf_tag)
        """
    def update_resource(self, *, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Updates the data access role used for vending access to the given (registered)
        resource in AWS Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/lakeformation.html#LakeFormation.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_resource)
        """
