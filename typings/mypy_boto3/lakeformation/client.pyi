"""
Type annotations for lakeformation service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lakeformation.client import LakeFormationClient

    session = Session()
    client: LakeFormationClient = session.client("lakeformation")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetWorkUnitsPaginator,
    ListDataCellsFilterPaginator,
    ListLFTagExpressionsPaginator,
    ListLFTagsPaginator,
    SearchDatabasesByLFTagsPaginator,
    SearchTablesByLFTagsPaginator,
)
from .type_defs import (
    AddLFTagsToResourceRequestTypeDef,
    AddLFTagsToResourceResponseTypeDef,
    AssumeDecoratedRoleWithSAMLRequestTypeDef,
    AssumeDecoratedRoleWithSAMLResponseTypeDef,
    BatchGrantPermissionsRequestTypeDef,
    BatchGrantPermissionsResponseTypeDef,
    BatchRevokePermissionsRequestTypeDef,
    BatchRevokePermissionsResponseTypeDef,
    CancelTransactionRequestTypeDef,
    CommitTransactionRequestTypeDef,
    CommitTransactionResponseTypeDef,
    CreateDataCellsFilterRequestTypeDef,
    CreateLakeFormationIdentityCenterConfigurationRequestTypeDef,
    CreateLakeFormationIdentityCenterConfigurationResponseTypeDef,
    CreateLakeFormationOptInRequestTypeDef,
    CreateLFTagExpressionRequestTypeDef,
    CreateLFTagRequestTypeDef,
    DeleteDataCellsFilterRequestTypeDef,
    DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef,
    DeleteLakeFormationOptInRequestTypeDef,
    DeleteLFTagExpressionRequestTypeDef,
    DeleteLFTagRequestTypeDef,
    DeleteObjectsOnCancelRequestTypeDef,
    DeregisterResourceRequestTypeDef,
    DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef,
    DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef,
    DescribeResourceRequestTypeDef,
    DescribeResourceResponseTypeDef,
    DescribeTransactionRequestTypeDef,
    DescribeTransactionResponseTypeDef,
    ExtendTransactionRequestTypeDef,
    GetDataCellsFilterRequestTypeDef,
    GetDataCellsFilterResponseTypeDef,
    GetDataLakePrincipalResponseTypeDef,
    GetDataLakeSettingsRequestTypeDef,
    GetDataLakeSettingsResponseTypeDef,
    GetEffectivePermissionsForPathRequestTypeDef,
    GetEffectivePermissionsForPathResponseTypeDef,
    GetLFTagExpressionRequestTypeDef,
    GetLFTagExpressionResponseTypeDef,
    GetLFTagRequestTypeDef,
    GetLFTagResponseTypeDef,
    GetQueryStateRequestTypeDef,
    GetQueryStateResponseTypeDef,
    GetQueryStatisticsRequestTypeDef,
    GetQueryStatisticsResponseTypeDef,
    GetResourceLFTagsRequestTypeDef,
    GetResourceLFTagsResponseTypeDef,
    GetTableObjectsRequestTypeDef,
    GetTableObjectsResponseTypeDef,
    GetTemporaryGluePartitionCredentialsRequestTypeDef,
    GetTemporaryGluePartitionCredentialsResponseTypeDef,
    GetTemporaryGlueTableCredentialsRequestTypeDef,
    GetTemporaryGlueTableCredentialsResponseTypeDef,
    GetWorkUnitResultsRequestTypeDef,
    GetWorkUnitResultsResponseTypeDef,
    GetWorkUnitsRequestTypeDef,
    GetWorkUnitsResponseTypeDef,
    GrantPermissionsRequestTypeDef,
    ListDataCellsFilterRequestTypeDef,
    ListDataCellsFilterResponseTypeDef,
    ListLakeFormationOptInsRequestTypeDef,
    ListLakeFormationOptInsResponseTypeDef,
    ListLFTagExpressionsRequestTypeDef,
    ListLFTagExpressionsResponseTypeDef,
    ListLFTagsRequestTypeDef,
    ListLFTagsResponseTypeDef,
    ListPermissionsRequestTypeDef,
    ListPermissionsResponseTypeDef,
    ListResourcesRequestTypeDef,
    ListResourcesResponseTypeDef,
    ListTableStorageOptimizersRequestTypeDef,
    ListTableStorageOptimizersResponseTypeDef,
    ListTransactionsRequestTypeDef,
    ListTransactionsResponseTypeDef,
    PutDataLakeSettingsRequestTypeDef,
    RegisterResourceRequestTypeDef,
    RemoveLFTagsFromResourceRequestTypeDef,
    RemoveLFTagsFromResourceResponseTypeDef,
    RevokePermissionsRequestTypeDef,
    SearchDatabasesByLFTagsRequestTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsRequestTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
    StartQueryPlanningRequestTypeDef,
    StartQueryPlanningResponseTypeDef,
    StartTransactionRequestTypeDef,
    StartTransactionResponseTypeDef,
    UpdateDataCellsFilterRequestTypeDef,
    UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef,
    UpdateLFTagExpressionRequestTypeDef,
    UpdateLFTagRequestTypeDef,
    UpdateResourceRequestTypeDef,
    UpdateTableObjectsRequestTypeDef,
    UpdateTableStorageOptimizerRequestTypeDef,
    UpdateTableStorageOptimizerResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("LakeFormationClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LakeFormationClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#generate_presigned_url)
        """

    def add_lf_tags_to_resource(
        self, **kwargs: Unpack[AddLFTagsToResourceRequestTypeDef]
    ) -> AddLFTagsToResourceResponseTypeDef:
        """
        Attaches one or more LF-tags to an existing resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/add_lf_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#add_lf_tags_to_resource)
        """

    def assume_decorated_role_with_saml(
        self, **kwargs: Unpack[AssumeDecoratedRoleWithSAMLRequestTypeDef]
    ) -> AssumeDecoratedRoleWithSAMLResponseTypeDef:
        """
        Allows a caller to assume an IAM role decorated as the SAML user specified in
        the SAML assertion included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/assume_decorated_role_with_saml.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#assume_decorated_role_with_saml)
        """

    def batch_grant_permissions(
        self, **kwargs: Unpack[BatchGrantPermissionsRequestTypeDef]
    ) -> BatchGrantPermissionsResponseTypeDef:
        """
        Batch operation to grant permissions to the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/batch_grant_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#batch_grant_permissions)
        """

    def batch_revoke_permissions(
        self, **kwargs: Unpack[BatchRevokePermissionsRequestTypeDef]
    ) -> BatchRevokePermissionsResponseTypeDef:
        """
        Batch operation to revoke permissions from the principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/batch_revoke_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#batch_revoke_permissions)
        """

    def cancel_transaction(
        self, **kwargs: Unpack[CancelTransactionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attempts to cancel the specified transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/cancel_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#cancel_transaction)
        """

    def commit_transaction(
        self, **kwargs: Unpack[CommitTransactionRequestTypeDef]
    ) -> CommitTransactionResponseTypeDef:
        """
        Attempts to commit the specified transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/commit_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#commit_transaction)
        """

    def create_data_cells_filter(
        self, **kwargs: Unpack[CreateDataCellsFilterRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a data cell filter to allow one to grant access to certain columns on
        certain rows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/create_data_cells_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#create_data_cells_filter)
        """

    def create_lf_tag(self, **kwargs: Unpack[CreateLFTagRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates an LF-tag with the specified name and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/create_lf_tag.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#create_lf_tag)
        """

    def create_lf_tag_expression(
        self, **kwargs: Unpack[CreateLFTagExpressionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a new LF-Tag expression with the provided name, description, catalog
        ID, and expression body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/create_lf_tag_expression.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#create_lf_tag_expression)
        """

    def create_lake_formation_identity_center_configuration(
        self, **kwargs: Unpack[CreateLakeFormationIdentityCenterConfigurationRequestTypeDef]
    ) -> CreateLakeFormationIdentityCenterConfigurationResponseTypeDef:
        """
        Creates an IAM Identity Center connection with Lake Formation to allow IAM
        Identity Center users and groups to access Data Catalog resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/create_lake_formation_identity_center_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#create_lake_formation_identity_center_configuration)
        """

    def create_lake_formation_opt_in(
        self, **kwargs: Unpack[CreateLakeFormationOptInRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enforce Lake Formation permissions for the given databases, tables, and
        principals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/create_lake_formation_opt_in.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#create_lake_formation_opt_in)
        """

    def delete_data_cells_filter(
        self, **kwargs: Unpack[DeleteDataCellsFilterRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a data cell filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_data_cells_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_data_cells_filter)
        """

    def delete_lf_tag(self, **kwargs: Unpack[DeleteLFTagRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified LF-tag given a key name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_lf_tag.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_lf_tag)
        """

    def delete_lf_tag_expression(
        self, **kwargs: Unpack[DeleteLFTagExpressionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the LF-Tag expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_lf_tag_expression.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_lf_tag_expression)
        """

    def delete_lake_formation_identity_center_configuration(
        self, **kwargs: Unpack[DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an IAM Identity Center connection with Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_lake_formation_identity_center_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_lake_formation_identity_center_configuration)
        """

    def delete_lake_formation_opt_in(
        self, **kwargs: Unpack[DeleteLakeFormationOptInRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove the Lake Formation permissions enforcement of the given databases,
        tables, and principals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_lake_formation_opt_in.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_lake_formation_opt_in)
        """

    def delete_objects_on_cancel(
        self, **kwargs: Unpack[DeleteObjectsOnCancelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        For a specific governed table, provides a list of Amazon S3 objects that will
        be written during the current transaction and that can be automatically deleted
        if the transaction is canceled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/delete_objects_on_cancel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#delete_objects_on_cancel)
        """

    def deregister_resource(
        self, **kwargs: Unpack[DeregisterResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/deregister_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#deregister_resource)
        """

    def describe_lake_formation_identity_center_configuration(
        self, **kwargs: Unpack[DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef]
    ) -> DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef:
        """
        Retrieves the instance ARN and application ARN for the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/describe_lake_formation_identity_center_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#describe_lake_formation_identity_center_configuration)
        """

    def describe_resource(
        self, **kwargs: Unpack[DescribeResourceRequestTypeDef]
    ) -> DescribeResourceResponseTypeDef:
        """
        Retrieves the current data access role for the given resource registered in
        Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/describe_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#describe_resource)
        """

    def describe_transaction(
        self, **kwargs: Unpack[DescribeTransactionRequestTypeDef]
    ) -> DescribeTransactionResponseTypeDef:
        """
        Returns the details of a single transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/describe_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#describe_transaction)
        """

    def extend_transaction(
        self, **kwargs: Unpack[ExtendTransactionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Indicates to the service that the specified transaction is still active and
        should not be treated as idle and aborted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/extend_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#extend_transaction)
        """

    def get_data_cells_filter(
        self, **kwargs: Unpack[GetDataCellsFilterRequestTypeDef]
    ) -> GetDataCellsFilterResponseTypeDef:
        """
        Returns a data cells filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_data_cells_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_data_cells_filter)
        """

    def get_data_lake_principal(self) -> GetDataLakePrincipalResponseTypeDef:
        """
        Returns the identity of the invoking principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_data_lake_principal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_data_lake_principal)
        """

    def get_data_lake_settings(
        self, **kwargs: Unpack[GetDataLakeSettingsRequestTypeDef]
    ) -> GetDataLakeSettingsResponseTypeDef:
        """
        Retrieves the list of the data lake administrators of a Lake Formation-managed
        data lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_data_lake_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_data_lake_settings)
        """

    def get_effective_permissions_for_path(
        self, **kwargs: Unpack[GetEffectivePermissionsForPathRequestTypeDef]
    ) -> GetEffectivePermissionsForPathResponseTypeDef:
        """
        Returns the Lake Formation permissions for a specified table or database
        resource located at a path in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_effective_permissions_for_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_effective_permissions_for_path)
        """

    def get_lf_tag(self, **kwargs: Unpack[GetLFTagRequestTypeDef]) -> GetLFTagResponseTypeDef:
        """
        Returns an LF-tag definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_lf_tag.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_lf_tag)
        """

    def get_lf_tag_expression(
        self, **kwargs: Unpack[GetLFTagExpressionRequestTypeDef]
    ) -> GetLFTagExpressionResponseTypeDef:
        """
        Returns the details about the LF-Tag expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_lf_tag_expression.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_lf_tag_expression)
        """

    def get_query_state(
        self, **kwargs: Unpack[GetQueryStateRequestTypeDef]
    ) -> GetQueryStateResponseTypeDef:
        """
        Returns the state of a query previously submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_query_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_query_state)
        """

    def get_query_statistics(
        self, **kwargs: Unpack[GetQueryStatisticsRequestTypeDef]
    ) -> GetQueryStatisticsResponseTypeDef:
        """
        Retrieves statistics on the planning and execution of a query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_query_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_query_statistics)
        """

    def get_resource_lf_tags(
        self, **kwargs: Unpack[GetResourceLFTagsRequestTypeDef]
    ) -> GetResourceLFTagsResponseTypeDef:
        """
        Returns the LF-tags applied to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_resource_lf_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_resource_lf_tags)
        """

    def get_table_objects(
        self, **kwargs: Unpack[GetTableObjectsRequestTypeDef]
    ) -> GetTableObjectsResponseTypeDef:
        """
        Returns the set of Amazon S3 objects that make up the specified governed table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_table_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_table_objects)
        """

    def get_temporary_glue_partition_credentials(
        self, **kwargs: Unpack[GetTemporaryGluePartitionCredentialsRequestTypeDef]
    ) -> GetTemporaryGluePartitionCredentialsResponseTypeDef:
        """
        This API is identical to <code>GetTemporaryTableCredentials</code> except that
        this is used when the target Data Catalog resource is of type Partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_temporary_glue_partition_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_temporary_glue_partition_credentials)
        """

    def get_temporary_glue_table_credentials(
        self, **kwargs: Unpack[GetTemporaryGlueTableCredentialsRequestTypeDef]
    ) -> GetTemporaryGlueTableCredentialsResponseTypeDef:
        """
        Allows a caller in a secure environment to assume a role with permission to
        access Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_temporary_glue_table_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_temporary_glue_table_credentials)
        """

    def get_work_unit_results(
        self, **kwargs: Unpack[GetWorkUnitResultsRequestTypeDef]
    ) -> GetWorkUnitResultsResponseTypeDef:
        """
        Returns the work units resulting from the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_work_unit_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_work_unit_results)
        """

    def get_work_units(
        self, **kwargs: Unpack[GetWorkUnitsRequestTypeDef]
    ) -> GetWorkUnitsResponseTypeDef:
        """
        Retrieves the work units generated by the <code>StartQueryPlanning</code>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_work_units.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_work_units)
        """

    def grant_permissions(self, **kwargs: Unpack[GrantPermissionsRequestTypeDef]) -> Dict[str, Any]:
        """
        Grants permissions to the principal to access metadata in the Data Catalog and
        data organized in underlying data storage such as Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/grant_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#grant_permissions)
        """

    def list_data_cells_filter(
        self, **kwargs: Unpack[ListDataCellsFilterRequestTypeDef]
    ) -> ListDataCellsFilterResponseTypeDef:
        """
        Lists all the data cell filters on a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_data_cells_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_data_cells_filter)
        """

    def list_lf_tag_expressions(
        self, **kwargs: Unpack[ListLFTagExpressionsRequestTypeDef]
    ) -> ListLFTagExpressionsResponseTypeDef:
        """
        Returns the LF-Tag expressions in caller's account filtered based on caller's
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_lf_tag_expressions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_lf_tag_expressions)
        """

    def list_lf_tags(self, **kwargs: Unpack[ListLFTagsRequestTypeDef]) -> ListLFTagsResponseTypeDef:
        """
        Lists LF-tags that the requester has permission to view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_lf_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_lf_tags)
        """

    def list_lake_formation_opt_ins(
        self, **kwargs: Unpack[ListLakeFormationOptInsRequestTypeDef]
    ) -> ListLakeFormationOptInsResponseTypeDef:
        """
        Retrieve the current list of resources and principals that are opt in to
        enforce Lake Formation permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_lake_formation_opt_ins.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_lake_formation_opt_ins)
        """

    def list_permissions(
        self, **kwargs: Unpack[ListPermissionsRequestTypeDef]
    ) -> ListPermissionsResponseTypeDef:
        """
        Returns a list of the principal permissions on the resource, filtered by the
        permissions of the caller.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_permissions)
        """

    def list_resources(
        self, **kwargs: Unpack[ListResourcesRequestTypeDef]
    ) -> ListResourcesResponseTypeDef:
        """
        Lists the resources registered to be managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_resources)
        """

    def list_table_storage_optimizers(
        self, **kwargs: Unpack[ListTableStorageOptimizersRequestTypeDef]
    ) -> ListTableStorageOptimizersResponseTypeDef:
        """
        Returns the configuration of all storage optimizers associated with a specified
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_table_storage_optimizers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_table_storage_optimizers)
        """

    def list_transactions(
        self, **kwargs: Unpack[ListTransactionsRequestTypeDef]
    ) -> ListTransactionsResponseTypeDef:
        """
        Returns metadata about transactions and their status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/list_transactions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#list_transactions)
        """

    def put_data_lake_settings(
        self, **kwargs: Unpack[PutDataLakeSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the list of data lake administrators who have admin privileges on all
        resources managed by Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/put_data_lake_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#put_data_lake_settings)
        """

    def register_resource(self, **kwargs: Unpack[RegisterResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Registers the resource as managed by the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/register_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#register_resource)
        """

    def remove_lf_tags_from_resource(
        self, **kwargs: Unpack[RemoveLFTagsFromResourceRequestTypeDef]
    ) -> RemoveLFTagsFromResourceResponseTypeDef:
        """
        Removes an LF-tag from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/remove_lf_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#remove_lf_tags_from_resource)
        """

    def revoke_permissions(
        self, **kwargs: Unpack[RevokePermissionsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Revokes permissions to the principal to access metadata in the Data Catalog and
        data organized in underlying data storage such as Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/revoke_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#revoke_permissions)
        """

    def search_databases_by_lf_tags(
        self, **kwargs: Unpack[SearchDatabasesByLFTagsRequestTypeDef]
    ) -> SearchDatabasesByLFTagsResponseTypeDef:
        """
        This operation allows a search on <code>DATABASE</code> resources by
        <code>TagCondition</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/search_databases_by_lf_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#search_databases_by_lf_tags)
        """

    def search_tables_by_lf_tags(
        self, **kwargs: Unpack[SearchTablesByLFTagsRequestTypeDef]
    ) -> SearchTablesByLFTagsResponseTypeDef:
        """
        This operation allows a search on <code>TABLE</code> resources by
        <code>LFTag</code>s.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/search_tables_by_lf_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#search_tables_by_lf_tags)
        """

    def start_query_planning(
        self, **kwargs: Unpack[StartQueryPlanningRequestTypeDef]
    ) -> StartQueryPlanningResponseTypeDef:
        """
        Submits a request to process a query statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/start_query_planning.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#start_query_planning)
        """

    def start_transaction(
        self, **kwargs: Unpack[StartTransactionRequestTypeDef]
    ) -> StartTransactionResponseTypeDef:
        """
        Starts a new transaction and returns its transaction ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/start_transaction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#start_transaction)
        """

    def update_data_cells_filter(
        self, **kwargs: Unpack[UpdateDataCellsFilterRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a data cell filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_data_cells_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_data_cells_filter)
        """

    def update_lf_tag(self, **kwargs: Unpack[UpdateLFTagRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the list of possible values for the specified LF-tag key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_lf_tag.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_lf_tag)
        """

    def update_lf_tag_expression(
        self, **kwargs: Unpack[UpdateLFTagExpressionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the name of the LF-Tag expression to the new description and expression
        body provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_lf_tag_expression.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_lf_tag_expression)
        """

    def update_lake_formation_identity_center_configuration(
        self, **kwargs: Unpack[UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the IAM Identity Center connection parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_lake_formation_identity_center_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_lake_formation_identity_center_configuration)
        """

    def update_resource(self, **kwargs: Unpack[UpdateResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the data access role used for vending access to the given (registered)
        resource in Lake Formation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_resource)
        """

    def update_table_objects(
        self, **kwargs: Unpack[UpdateTableObjectsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the manifest of Amazon S3 objects that make up the specified governed
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_table_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_table_objects)
        """

    def update_table_storage_optimizer(
        self, **kwargs: Unpack[UpdateTableStorageOptimizerRequestTypeDef]
    ) -> UpdateTableStorageOptimizerResponseTypeDef:
        """
        Updates the configuration of the storage optimizers for a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/update_table_storage_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#update_table_storage_optimizer)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_work_units"]
    ) -> GetWorkUnitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_cells_filter"]
    ) -> ListDataCellsFilterPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lf_tag_expressions"]
    ) -> ListLFTagExpressionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lf_tags"]
    ) -> ListLFTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_databases_by_lf_tags"]
    ) -> SearchDatabasesByLFTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_tables_by_lf_tags"]
    ) -> SearchTablesByLFTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client/#get_paginator)
        """
