"""
Main interface for honeycode service client

Usage::

    ```python
    import boto3
    from mypy_boto3_honeycode import HoneycodeClient

    client: HoneycodeClient = boto3.client("honeycode")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_honeycode.paginator import (
    ListTableColumnsPaginator,
    ListTableRowsPaginator,
    ListTablesPaginator,
    QueryTableRowsPaginator,
)
from mypy_boto3_honeycode.type_defs import (
    BatchCreateTableRowsResultTypeDef,
    BatchDeleteTableRowsResultTypeDef,
    BatchUpdateTableRowsResultTypeDef,
    BatchUpsertTableRowsResultTypeDef,
    CreateRowDataTypeDef,
    DescribeTableDataImportJobResultTypeDef,
    FilterTypeDef,
    GetScreenDataResultTypeDef,
    ImportDataSourceTypeDef,
    ImportOptionsTypeDef,
    InvokeScreenAutomationResultTypeDef,
    ListTableColumnsResultTypeDef,
    ListTableRowsResultTypeDef,
    ListTablesResultTypeDef,
    QueryTableRowsResultTypeDef,
    StartTableDataImportJobResultTypeDef,
    UpdateRowDataTypeDef,
    UpsertRowDataTypeDef,
    VariableValueTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("HoneycodeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AutomationExecutionException: Type[BotocoreClientError]
    AutomationExecutionTimeoutException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class HoneycodeClient:
    """
    [Honeycode.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_create_table_rows(
        self,
        workbookId: str,
        tableId: str,
        rowsToCreate: List[CreateRowDataTypeDef],
        clientRequestToken: str = None,
    ) -> BatchCreateTableRowsResultTypeDef:
        """
        [Client.batch_create_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.batch_create_table_rows)
        """

    def batch_delete_table_rows(
        self, workbookId: str, tableId: str, rowIds: List[str], clientRequestToken: str = None
    ) -> BatchDeleteTableRowsResultTypeDef:
        """
        [Client.batch_delete_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.batch_delete_table_rows)
        """

    def batch_update_table_rows(
        self,
        workbookId: str,
        tableId: str,
        rowsToUpdate: List[UpdateRowDataTypeDef],
        clientRequestToken: str = None,
    ) -> BatchUpdateTableRowsResultTypeDef:
        """
        [Client.batch_update_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.batch_update_table_rows)
        """

    def batch_upsert_table_rows(
        self,
        workbookId: str,
        tableId: str,
        rowsToUpsert: List[UpsertRowDataTypeDef],
        clientRequestToken: str = None,
    ) -> BatchUpsertTableRowsResultTypeDef:
        """
        [Client.batch_upsert_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.batch_upsert_table_rows)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.can_paginate)
        """

    def describe_table_data_import_job(
        self, workbookId: str, tableId: str, jobId: str
    ) -> DescribeTableDataImportJobResultTypeDef:
        """
        [Client.describe_table_data_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.describe_table_data_import_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.generate_presigned_url)
        """

    def get_screen_data(
        self,
        workbookId: str,
        appId: str,
        screenId: str,
        variables: Dict[str, VariableValueTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> GetScreenDataResultTypeDef:
        """
        [Client.get_screen_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.get_screen_data)
        """

    def invoke_screen_automation(
        self,
        workbookId: str,
        appId: str,
        screenId: str,
        screenAutomationId: str,
        variables: Dict[str, VariableValueTypeDef] = None,
        rowId: str = None,
        clientRequestToken: str = None,
    ) -> InvokeScreenAutomationResultTypeDef:
        """
        [Client.invoke_screen_automation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.invoke_screen_automation)
        """

    def list_table_columns(
        self, workbookId: str, tableId: str, nextToken: str = None
    ) -> ListTableColumnsResultTypeDef:
        """
        [Client.list_table_columns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.list_table_columns)
        """

    def list_table_rows(
        self,
        workbookId: str,
        tableId: str,
        rowIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListTableRowsResultTypeDef:
        """
        [Client.list_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.list_table_rows)
        """

    def list_tables(
        self, workbookId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTablesResultTypeDef:
        """
        [Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.list_tables)
        """

    def query_table_rows(
        self,
        workbookId: str,
        tableId: str,
        filterFormula: "FilterTypeDef",
        maxResults: int = None,
        nextToken: str = None,
    ) -> QueryTableRowsResultTypeDef:
        """
        [Client.query_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.query_table_rows)
        """

    def start_table_data_import_job(
        self,
        workbookId: str,
        dataSource: "ImportDataSourceTypeDef",
        dataFormat: Literal["DELIMITED_TEXT"],
        destinationTableId: str,
        importOptions: "ImportOptionsTypeDef",
        clientRequestToken: str,
    ) -> StartTableDataImportJobResultTypeDef:
        """
        [Client.start_table_data_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Client.start_table_data_import_job)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_table_columns"]
    ) -> ListTableColumnsPaginator:
        """
        [Paginator.ListTableColumns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_table_rows"]) -> ListTableRowsPaginator:
        """
        [Paginator.ListTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTables)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query_table_rows"]) -> QueryTableRowsPaginator:
        """
        [Paginator.QueryTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)
        """
