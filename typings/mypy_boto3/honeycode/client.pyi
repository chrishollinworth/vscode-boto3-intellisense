"""
Type annotations for honeycode service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_honeycode import HoneycodeClient

    client: HoneycodeClient = boto3.client("honeycode")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListTableColumnsPaginator,
    ListTableRowsPaginator,
    ListTablesPaginator,
    QueryTableRowsPaginator,
)
from .type_defs import (
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
    ListTagsForResourceResultTypeDef,
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

class HoneycodeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HoneycodeClient exceptions.
        """
    def batch_create_table_rows(
        self,
        *,
        workbookId: str,
        tableId: str,
        rowsToCreate: List["CreateRowDataTypeDef"],
        clientRequestToken: str = None
    ) -> BatchCreateTableRowsResultTypeDef:
        """
        The BatchCreateTableRows API allows you to create one or more rows at the end of
        a table in a workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.batch_create_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#batch_create_table_rows)
        """
    def batch_delete_table_rows(
        self, *, workbookId: str, tableId: str, rowIds: List[str], clientRequestToken: str = None
    ) -> BatchDeleteTableRowsResultTypeDef:
        """
        The BatchDeleteTableRows API allows you to delete one or more rows from a table
        in a workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.batch_delete_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#batch_delete_table_rows)
        """
    def batch_update_table_rows(
        self,
        *,
        workbookId: str,
        tableId: str,
        rowsToUpdate: List["UpdateRowDataTypeDef"],
        clientRequestToken: str = None
    ) -> BatchUpdateTableRowsResultTypeDef:
        """
        The BatchUpdateTableRows API allows you to update one or more rows in a table in
        a workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.batch_update_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#batch_update_table_rows)
        """
    def batch_upsert_table_rows(
        self,
        *,
        workbookId: str,
        tableId: str,
        rowsToUpsert: List["UpsertRowDataTypeDef"],
        clientRequestToken: str = None
    ) -> BatchUpsertTableRowsResultTypeDef:
        """
        The BatchUpsertTableRows API allows you to upsert one or more rows in a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.batch_upsert_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#batch_upsert_table_rows)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#close)
        """
    def describe_table_data_import_job(
        self, *, workbookId: str, tableId: str, jobId: str
    ) -> DescribeTableDataImportJobResultTypeDef:
        """
        The DescribeTableDataImportJob API allows you to retrieve the status and details
        of a table data import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.describe_table_data_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#describe_table_data_import_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#generate_presigned_url)
        """
    def get_screen_data(
        self,
        *,
        workbookId: str,
        appId: str,
        screenId: str,
        variables: Dict[str, "VariableValueTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> GetScreenDataResultTypeDef:
        """
        The GetScreenData API allows retrieval of data from a screen in a Honeycode app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.get_screen_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#get_screen_data)
        """
    def invoke_screen_automation(
        self,
        *,
        workbookId: str,
        appId: str,
        screenId: str,
        screenAutomationId: str,
        variables: Dict[str, "VariableValueTypeDef"] = None,
        rowId: str = None,
        clientRequestToken: str = None
    ) -> InvokeScreenAutomationResultTypeDef:
        """
        The InvokeScreenAutomation API allows invoking an action defined in a screen in
        a Honeycode app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.invoke_screen_automation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#invoke_screen_automation)
        """
    def list_table_columns(
        self, *, workbookId: str, tableId: str, nextToken: str = None
    ) -> ListTableColumnsResultTypeDef:
        """
        The ListTableColumns API allows you to retrieve a list of all the columns in a
        table in a workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.list_table_columns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#list_table_columns)
        """
    def list_table_rows(
        self,
        *,
        workbookId: str,
        tableId: str,
        rowIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTableRowsResultTypeDef:
        """
        The ListTableRows API allows you to retrieve a list of all the rows in a table
        in a workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.list_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#list_table_rows)
        """
    def list_tables(
        self, *, workbookId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTablesResultTypeDef:
        """
        The ListTables API allows you to retrieve a list of all the tables in a
        workbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#list_tables)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        The ListTagsForResource API allows you to return a resource's tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#list_tags_for_resource)
        """
    def query_table_rows(
        self,
        *,
        workbookId: str,
        tableId: str,
        filterFormula: "FilterTypeDef",
        maxResults: int = None,
        nextToken: str = None
    ) -> QueryTableRowsResultTypeDef:
        """
        The QueryTableRows API allows you to use a filter formula to query for specific
        rows in a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.query_table_rows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#query_table_rows)
        """
    def start_table_data_import_job(
        self,
        *,
        workbookId: str,
        dataSource: "ImportDataSourceTypeDef",
        dataFormat: Literal["DELIMITED_TEXT"],
        destinationTableId: str,
        importOptions: "ImportOptionsTypeDef",
        clientRequestToken: str
    ) -> StartTableDataImportJobResultTypeDef:
        """
        The StartTableDataImportJob API allows you to start an import job on a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.start_table_data_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#start_table_data_import_job)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        The TagResource API allows you to add tags to an ARN-able resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        The UntagResource API allows you to removes tags from an ARN-able resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/client.html#untag_resource)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_table_columns"]
    ) -> ListTableColumnsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablecolumnspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_table_rows"]) -> ListTableRowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablerowspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Paginator.ListTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["query_table_rows"]) -> QueryTableRowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#querytablerowspaginator)
        """
