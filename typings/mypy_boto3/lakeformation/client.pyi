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
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DataLakeResourceTypeType,
    OptimizerTypeType,
    PermissionType,
    PermissionTypeType,
    ResourceShareTypeType,
    TransactionStatusFilterType,
    TransactionTypeType,
)
from .paginator import (
    GetWorkUnitsPaginator,
    ListDataCellsFilterPaginator,
    ListLFTagsPaginator,
    SearchDatabasesByLFTagsPaginator,
    SearchTablesByLFTagsPaginator,
)
from .type_defs import (
    AddLFTagsToResourceResponseTypeDef,
    AssumeDecoratedRoleWithSAMLResponseTypeDef,
    AuditContextTypeDef,
    BatchGrantPermissionsResponseTypeDef,
    BatchPermissionsRequestEntryTypeDef,
    BatchRevokePermissionsResponseTypeDef,
    CommitTransactionResponseTypeDef,
    DataCellsFilterTypeDef,
    DataLakePrincipalTypeDef,
    DataLakeSettingsTypeDef,
    DescribeResourceResponseTypeDef,
    DescribeTransactionResponseTypeDef,
    FilterConditionTypeDef,
    GetDataLakeSettingsResponseTypeDef,
    GetEffectivePermissionsForPathResponseTypeDef,
    GetLFTagResponseTypeDef,
    GetQueryStateResponseTypeDef,
    GetQueryStatisticsResponseTypeDef,
    GetResourceLFTagsResponseTypeDef,
    GetTableObjectsResponseTypeDef,
    GetTemporaryGluePartitionCredentialsResponseTypeDef,
    GetTemporaryGlueTableCredentialsResponseTypeDef,
    GetWorkUnitResultsResponseTypeDef,
    GetWorkUnitsResponseTypeDef,
    LFTagPairTypeDef,
    LFTagTypeDef,
    ListDataCellsFilterResponseTypeDef,
    ListLFTagsResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListTableStorageOptimizersResponseTypeDef,
    ListTransactionsResponseTypeDef,
    PartitionValueListTypeDef,
    QueryPlanningContextTypeDef,
    RemoveLFTagsFromResourceResponseTypeDef,
    ResourceTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
    StartQueryPlanningResponseTypeDef,
    StartTransactionResponseTypeDef,
    TableResourceTypeDef,
    UpdateTableStorageOptimizerResponseTypeDef,
    VirtualObjectTypeDef,
    WriteOperationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

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
    ExpiredException: Type[BotocoreClientError]
    GlueEncryptionException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    PermissionTypeMismatchException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ResourceNumberLimitExceededException: Type[BotocoreClientError]
    StatisticsNotReadyYetException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TransactionCanceledException: Type[BotocoreClientError]
    TransactionCommitInProgressException: Type[BotocoreClientError]
    TransactionCommittedException: Type[BotocoreClientError]
    WorkUnitsNotReadyYetException: Type[BotocoreClientError]

class LakeFormationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client)
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
        Attaches one or more LF-tags to an existing resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.add_lf_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#add_lf_tags_to_resource)
        """
    def assume_decorated_role_with_saml(
        self, *, SAMLAssertion: str, RoleArn: str, PrincipalArn: str, DurationSeconds: int = None
    ) -> AssumeDecoratedRoleWithSAMLResponseTypeDef:
        """
        Allows a caller to assume an IAM role decorated as the SAML user specified in
        the SAML assertion included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.assume_decorated_role_with_saml)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#assume_decorated_role_with_saml)
        """
    def batch_grant_permissions(
        self, *, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchGrantPermissionsResponseTypeDef:
        """
        Batch operation to grant permissions to the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch_grant_permissions)
        """
    def batch_revoke_permissions(
        self, *, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchRevokePermissionsResponseTypeDef:
        """
        Batch operation to revoke permissions from the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch_revoke_permissions)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#can_paginate)
        """
    def cancel_transaction(self, *, TransactionId: str) -> Dict[str, Any]:
        """
        Attempts to cancel the specified transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.cancel_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#cancel_transaction)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#close)
        """
    def commit_transaction(self, *, TransactionId: str) -> CommitTransactionResponseTypeDef:
        """
        Attempts to commit the specified transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.commit_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#commit_transaction)
        """
    def create_data_cells_filter(self, *, TableData: "DataCellsFilterTypeDef") -> Dict[str, Any]:
        """
        Creates a data cell filter to allow one to grant access to certain columns on
        certain rows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.create_data_cells_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#create_data_cells_filter)
        """
    def create_lf_tag(
        self, *, TagKey: str, TagValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Creates an LF-tag with the specified name and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.create_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#create_lf_tag)
        """
    def delete_data_cells_filter(
        self,
        *,
        TableCatalogId: str = None,
        DatabaseName: str = None,
        TableName: str = None,
        Name: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a data cell filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.delete_data_cells_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#delete_data_cells_filter)
        """
    def delete_lf_tag(self, *, TagKey: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        Deletes the specified LF-tag given a key name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.delete_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#delete_lf_tag)
        """
    def delete_objects_on_cancel(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        TransactionId: str,
        Objects: List["VirtualObjectTypeDef"],
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        For a specific governed table, provides a list of Amazon S3 objects that will be
        written during the current transaction and that can be automatically deleted if
        the transaction is canceled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.delete_objects_on_cancel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#delete_objects_on_cancel)
        """
    def deregister_resource(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deregisters the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#deregister_resource)
        """
    def describe_resource(self, *, ResourceArn: str) -> DescribeResourceResponseTypeDef:
        """
        Retrieves the current data access role for the given resource registered in Lake
        Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#describe_resource)
        """
    def describe_transaction(self, *, TransactionId: str) -> DescribeTransactionResponseTypeDef:
        """
        Returns the details of a single transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.describe_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#describe_transaction)
        """
    def extend_transaction(self, *, TransactionId: str = None) -> Dict[str, Any]:
        """
        Indicates to the service that the specified transaction is still active and
        should not be treated as idle and aborted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.extend_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#extend_transaction)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#generate_presigned_url)
        """
    def get_data_lake_settings(
        self, *, CatalogId: str = None
    ) -> GetDataLakeSettingsResponseTypeDef:
        """
        Retrieves the list of the data lake administrators of a Lake Formation-managed
        data lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_effective_permissions_for_path)
        """
    def get_lf_tag(self, *, TagKey: str, CatalogId: str = None) -> GetLFTagResponseTypeDef:
        """
        Returns an LF-tag definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_lf_tag)
        """
    def get_query_state(self, *, QueryId: str) -> GetQueryStateResponseTypeDef:
        """
        Returns the state of a query previously submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_query_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_query_state)
        """
    def get_query_statistics(self, *, QueryId: str) -> GetQueryStatisticsResponseTypeDef:
        """
        Retrieves statistics on the planning and execution of a query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_query_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_query_statistics)
        """
    def get_resource_lf_tags(
        self, *, Resource: "ResourceTypeDef", CatalogId: str = None, ShowAssignedLFTags: bool = None
    ) -> GetResourceLFTagsResponseTypeDef:
        """
        Returns the LF-tags applied to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_resource_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_resource_lf_tags)
        """
    def get_table_objects(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        TransactionId: str = None,
        QueryAsOfTime: Union[datetime, str] = None,
        PartitionPredicate: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetTableObjectsResponseTypeDef:
        """
        Returns the set of Amazon S3 objects that make up the specified governed table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_table_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_table_objects)
        """
    def get_temporary_glue_partition_credentials(
        self,
        *,
        TableArn: str,
        Partition: "PartitionValueListTypeDef",
        SupportedPermissionTypes: List[PermissionTypeType],
        Permissions: List[PermissionType] = None,
        DurationSeconds: int = None,
        AuditContext: "AuditContextTypeDef" = None
    ) -> GetTemporaryGluePartitionCredentialsResponseTypeDef:
        """
        This API is identical to `GetTemporaryTableCredentials` except that this is used
        when the target Data Catalog resource is of type Partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_temporary_glue_partition_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_temporary_glue_partition_credentials)
        """
    def get_temporary_glue_table_credentials(
        self,
        *,
        TableArn: str,
        SupportedPermissionTypes: List[PermissionTypeType],
        Permissions: List[PermissionType] = None,
        DurationSeconds: int = None,
        AuditContext: "AuditContextTypeDef" = None
    ) -> GetTemporaryGlueTableCredentialsResponseTypeDef:
        """
        Allows a caller in a secure environment to assume a role with permission to
        access Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_temporary_glue_table_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_temporary_glue_table_credentials)
        """
    def get_work_unit_results(
        self, *, QueryId: str, WorkUnitId: int, WorkUnitToken: str
    ) -> GetWorkUnitResultsResponseTypeDef:
        """
        Returns the work units resulting from the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_work_unit_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_work_unit_results)
        """
    def get_work_units(
        self, *, QueryId: str, NextToken: str = None, PageSize: int = None
    ) -> GetWorkUnitsResponseTypeDef:
        """
        Retrieves the work units generated by the `StartQueryPlanning` operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.get_work_units)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get_work_units)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#grant_permissions)
        """
    def list_data_cells_filter(
        self, *, Table: "TableResourceTypeDef" = None, NextToken: str = None, MaxResults: int = None
    ) -> ListDataCellsFilterResponseTypeDef:
        """
        Lists all the data cell filters on a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_data_cells_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_data_cells_filter)
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
        Lists LF-tags that the requester has permission to view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_lf_tags)
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
        MaxResults: int = None,
        IncludeRelated: str = None
    ) -> ListPermissionsResponseTypeDef:
        """
        Returns a list of the principal permissions on the resource, filtered by the
        permissions of the caller.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_resources)
        """
    def list_table_storage_optimizers(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        StorageOptimizerType: OptimizerTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTableStorageOptimizersResponseTypeDef:
        """
        Returns the configuration of all storage optimizers associated with a specified
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_table_storage_optimizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_table_storage_optimizers)
        """
    def list_transactions(
        self,
        *,
        CatalogId: str = None,
        StatusFilter: TransactionStatusFilterType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTransactionsResponseTypeDef:
        """
        Returns metadata about transactions and their status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.list_transactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list_transactions)
        """
    def put_data_lake_settings(
        self, *, DataLakeSettings: "DataLakeSettingsTypeDef", CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        Sets the list of data lake administrators who have admin privileges on all
        resources managed by Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#put_data_lake_settings)
        """
    def register_resource(
        self, *, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        Registers the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.register_resource)
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
        Removes an LF-tag from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.remove_lf_tags_from_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.search_databases_by_lf_tags)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.search_tables_by_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#search_tables_by_lf_tags)
        """
    def start_query_planning(
        self, *, QueryPlanningContext: "QueryPlanningContextTypeDef", QueryString: str
    ) -> StartQueryPlanningResponseTypeDef:
        """
        Submits a request to process a query statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.start_query_planning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#start_query_planning)
        """
    def start_transaction(
        self, *, TransactionType: TransactionTypeType = None
    ) -> StartTransactionResponseTypeDef:
        """
        Starts a new transaction and returns its transaction ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.start_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#start_transaction)
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
        Updates the list of possible values for the specified LF-tag key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.update_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_lf_tag)
        """
    def update_resource(self, *, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Updates the data access role used for vending access to the given (registered)
        resource in Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_resource)
        """
    def update_table_objects(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        WriteOperations: List["WriteOperationTypeDef"],
        CatalogId: str = None,
        TransactionId: str = None
    ) -> Dict[str, Any]:
        """
        Updates the manifest of Amazon S3 objects that make up the specified governed
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.update_table_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_table_objects)
        """
    def update_table_storage_optimizer(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        StorageOptimizerConfig: Dict[OptimizerTypeType, Dict[str, str]],
        CatalogId: str = None
    ) -> UpdateTableStorageOptimizerResponseTypeDef:
        """
        Updates the configuration of the storage optimizers for a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Client.update_table_storage_optimizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update_table_storage_optimizer)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_work_units"]) -> GetWorkUnitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Paginator.GetWorkUnits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#getworkunitspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_cells_filter"]
    ) -> ListDataCellsFilterPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Paginator.ListDataCellsFilter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listdatacellsfilterpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_lf_tags"]) -> ListLFTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Paginator.ListLFTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listlftagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_databases_by_lf_tags"]
    ) -> SearchDatabasesByLFTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Paginator.SearchDatabasesByLFTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchdatabasesbylftagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_tables_by_lf_tags"]
    ) -> SearchTablesByLFTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/lakeformation.html#LakeFormation.Paginator.SearchTablesByLFTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchtablesbylftagspaginator)
        """
