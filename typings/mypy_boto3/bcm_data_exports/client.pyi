"""
Type annotations for bcm-data-exports service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_bcm_data_exports import BillingandCostManagementDataExportsClient

    client: BillingandCostManagementDataExportsClient = boto3.client("bcm-data-exports")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListExecutionsPaginator, ListExportsPaginator, ListTablesPaginator
from .type_defs import (
    CreateExportResponseTypeDef,
    DeleteExportResponseTypeDef,
    ExportTypeDef,
    GetExecutionResponseTypeDef,
    GetExportResponseTypeDef,
    GetTableResponseTypeDef,
    ListExecutionsResponseTypeDef,
    ListExportsResponseTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResourceTagTypeDef,
    UpdateExportResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BillingandCostManagementDataExportsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BillingandCostManagementDataExportsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingandCostManagementDataExportsClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#close)
        """

    def create_export(
        self, *, Export: "ExportTypeDef", ResourceTags: List["ResourceTagTypeDef"] = None
    ) -> CreateExportResponseTypeDef:
        """
        Creates a data export and specifies the data query, the delivery preference, and
        any optional resource tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.create_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#create_export)
        """

    def delete_export(self, *, ExportArn: str) -> DeleteExportResponseTypeDef:
        """
        Deletes an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.delete_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#delete_export)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#generate_presigned_url)
        """

    def get_execution(self, *, ExecutionId: str, ExportArn: str) -> GetExecutionResponseTypeDef:
        """
        Exports data based on the source data update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.get_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#get_execution)
        """

    def get_export(self, *, ExportArn: str) -> GetExportResponseTypeDef:
        """
        Views the definition of an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.get_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#get_export)
        """

    def get_table(
        self, *, TableName: str, TableProperties: Dict[str, str] = None
    ) -> GetTableResponseTypeDef:
        """
        Returns the metadata for the specified table and table properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.get_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#get_table)
        """

    def list_executions(
        self, *, ExportArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListExecutionsResponseTypeDef:
        """
        Lists the historical executions for the export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.list_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#list_executions)
        """

    def list_exports(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListExportsResponseTypeDef:
        """
        Lists all data export definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#list_exports)
        """

    def list_tables(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListTablesResponseTypeDef:
        """
        Lists all available tables in data exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#list_tables)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags associated with an existing data export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#list_tags_for_resource)
        """

    def tag_resource(
        self, *, ResourceArn: str, ResourceTags: List["ResourceTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Adds tags for an existing data export definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, ResourceTagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes tags associated with an existing data export definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#untag_resource)
        """

    def update_export(
        self, *, Export: "ExportTypeDef", ExportArn: str
    ) -> UpdateExportResponseTypeDef:
        """
        Updates an existing data export by overwriting all export parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Client.update_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/client.html#update_export)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexecutionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_exports"]) -> ListExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexportspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listtablespaginator)
        """
