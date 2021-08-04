"""
Type annotations for honeycode service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs.html)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsRequestRequestTypeDef

    data: BatchCreateTableRowsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    FormatType,
    ImportDataCharacterEncodingType,
    TableDataImportJobStatusType,
    UpsertActionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchCreateTableRowsRequestRequestTypeDef",
    "BatchCreateTableRowsResultTypeDef",
    "BatchDeleteTableRowsRequestRequestTypeDef",
    "BatchDeleteTableRowsResultTypeDef",
    "BatchUpdateTableRowsRequestRequestTypeDef",
    "BatchUpdateTableRowsResultTypeDef",
    "BatchUpsertTableRowsRequestRequestTypeDef",
    "BatchUpsertTableRowsResultTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "CreateRowDataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobRequestRequestTypeDef",
    "DescribeTableDataImportJobResultTypeDef",
    "DestinationOptionsTypeDef",
    "FailedBatchItemTypeDef",
    "FilterTypeDef",
    "GetScreenDataRequestRequestTypeDef",
    "GetScreenDataResultTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportDataSourceTypeDef",
    "ImportJobSubmitterTypeDef",
    "ImportOptionsTypeDef",
    "InvokeScreenAutomationRequestRequestTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "ListTableColumnsRequestRequestTypeDef",
    "ListTableColumnsResultTypeDef",
    "ListTableRowsRequestRequestTypeDef",
    "ListTableRowsResultTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResultTypeDef",
    "PaginatorConfigTypeDef",
    "QueryTableRowsRequestRequestTypeDef",
    "QueryTableRowsResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "StartTableDataImportJobRequestRequestTypeDef",
    "StartTableDataImportJobResultTypeDef",
    "TableColumnTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "TableRowTypeDef",
    "TableTypeDef",
    "UpdateRowDataTypeDef",
    "UpsertRowDataTypeDef",
    "UpsertRowsResultTypeDef",
    "VariableValueTypeDef",
)

_RequiredBatchCreateTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToCreate": List["CreateRowDataTypeDef"],
    },
)
_OptionalBatchCreateTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class BatchCreateTableRowsRequestRequestTypeDef(
    _RequiredBatchCreateTableRowsRequestRequestTypeDef,
    _OptionalBatchCreateTableRowsRequestRequestTypeDef,
):
    pass

BatchCreateTableRowsResultTypeDef = TypedDict(
    "BatchCreateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "createdRows": Dict[str, str],
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowIds": List[str],
    },
)
_OptionalBatchDeleteTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class BatchDeleteTableRowsRequestRequestTypeDef(
    _RequiredBatchDeleteTableRowsRequestRequestTypeDef,
    _OptionalBatchDeleteTableRowsRequestRequestTypeDef,
):
    pass

BatchDeleteTableRowsResultTypeDef = TypedDict(
    "BatchDeleteTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpdateTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpdate": List["UpdateRowDataTypeDef"],
    },
)
_OptionalBatchUpdateTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class BatchUpdateTableRowsRequestRequestTypeDef(
    _RequiredBatchUpdateTableRowsRequestRequestTypeDef,
    _OptionalBatchUpdateTableRowsRequestRequestTypeDef,
):
    pass

BatchUpdateTableRowsResultTypeDef = TypedDict(
    "BatchUpdateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpsertTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpsertTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpsert": List["UpsertRowDataTypeDef"],
    },
)
_OptionalBatchUpsertTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpsertTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class BatchUpsertTableRowsRequestRequestTypeDef(
    _RequiredBatchUpsertTableRowsRequestRequestTypeDef,
    _OptionalBatchUpsertTableRowsRequestRequestTypeDef,
):
    pass

BatchUpsertTableRowsResultTypeDef = TypedDict(
    "BatchUpsertTableRowsResultTypeDef",
    {
        "rows": Dict[str, "UpsertRowsResultTypeDef"],
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CellInputTypeDef = TypedDict(
    "CellInputTypeDef",
    {
        "fact": str,
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "formula": str,
        "format": FormatType,
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "format": FormatType,
    },
)

CreateRowDataTypeDef = TypedDict(
    "CreateRowDataTypeDef",
    {
        "batchItemId": str,
        "cellsToCreate": Dict[str, "CellInputTypeDef"],
    },
)

DataItemTypeDef = TypedDict(
    "DataItemTypeDef",
    {
        "overrideFormat": FormatType,
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

_RequiredDelimitedTextImportOptionsTypeDef = TypedDict(
    "_RequiredDelimitedTextImportOptionsTypeDef",
    {
        "delimiter": str,
    },
)
_OptionalDelimitedTextImportOptionsTypeDef = TypedDict(
    "_OptionalDelimitedTextImportOptionsTypeDef",
    {
        "hasHeaderRow": bool,
        "ignoreEmptyRows": bool,
        "dataCharacterEncoding": ImportDataCharacterEncodingType,
    },
    total=False,
)

class DelimitedTextImportOptionsTypeDef(
    _RequiredDelimitedTextImportOptionsTypeDef, _OptionalDelimitedTextImportOptionsTypeDef
):
    pass

DescribeTableDataImportJobRequestRequestTypeDef = TypedDict(
    "DescribeTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "jobId": str,
    },
)

DescribeTableDataImportJobResultTypeDef = TypedDict(
    "DescribeTableDataImportJobResultTypeDef",
    {
        "jobStatus": TableDataImportJobStatusType,
        "message": str,
        "jobMetadata": "TableDataImportJobMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationOptionsTypeDef = TypedDict(
    "DestinationOptionsTypeDef",
    {
        "columnMap": Dict[str, "SourceDataColumnPropertiesTypeDef"],
    },
    total=False,
)

FailedBatchItemTypeDef = TypedDict(
    "FailedBatchItemTypeDef",
    {
        "id": str,
        "errorMessage": str,
    },
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "formula": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "contextRowId": str,
    },
    total=False,
)

class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass

_RequiredGetScreenDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetScreenDataRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
    },
)
_OptionalGetScreenDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetScreenDataRequestRequestTypeDef",
    {
        "variables": Dict[str, "VariableValueTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetScreenDataRequestRequestTypeDef(
    _RequiredGetScreenDataRequestRequestTypeDef, _OptionalGetScreenDataRequestRequestTypeDef
):
    pass

GetScreenDataResultTypeDef = TypedDict(
    "GetScreenDataResultTypeDef",
    {
        "results": Dict[str, "ResultSetTypeDef"],
        "workbookCursor": int,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportDataSourceConfigTypeDef = TypedDict(
    "ImportDataSourceConfigTypeDef",
    {
        "dataSourceUrl": str,
    },
    total=False,
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "dataSourceConfig": "ImportDataSourceConfigTypeDef",
    },
)

ImportJobSubmitterTypeDef = TypedDict(
    "ImportJobSubmitterTypeDef",
    {
        "email": str,
        "userArn": str,
    },
    total=False,
)

ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "destinationOptions": "DestinationOptionsTypeDef",
        "delimitedTextOptions": "DelimitedTextImportOptionsTypeDef",
    },
    total=False,
)

_RequiredInvokeScreenAutomationRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeScreenAutomationRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
        "screenAutomationId": str,
    },
)
_OptionalInvokeScreenAutomationRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeScreenAutomationRequestRequestTypeDef",
    {
        "variables": Dict[str, "VariableValueTypeDef"],
        "rowId": str,
        "clientRequestToken": str,
    },
    total=False,
)

class InvokeScreenAutomationRequestRequestTypeDef(
    _RequiredInvokeScreenAutomationRequestRequestTypeDef,
    _OptionalInvokeScreenAutomationRequestRequestTypeDef,
):
    pass

InvokeScreenAutomationResultTypeDef = TypedDict(
    "InvokeScreenAutomationResultTypeDef",
    {
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableColumnsRequestRequestTypeDef = TypedDict(
    "_RequiredListTableColumnsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableColumnsRequestRequestTypeDef = TypedDict(
    "_OptionalListTableColumnsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListTableColumnsRequestRequestTypeDef(
    _RequiredListTableColumnsRequestRequestTypeDef, _OptionalListTableColumnsRequestRequestTypeDef
):
    pass

ListTableColumnsResultTypeDef = TypedDict(
    "ListTableColumnsResultTypeDef",
    {
        "tableColumns": List["TableColumnTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredListTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalListTableRowsRequestRequestTypeDef",
    {
        "rowIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTableRowsRequestRequestTypeDef(
    _RequiredListTableRowsRequestRequestTypeDef, _OptionalListTableRowsRequestRequestTypeDef
):
    pass

ListTableRowsResultTypeDef = TypedDict(
    "ListTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "rowIdsNotFound": List[str],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTablesRequestRequestTypeDef = TypedDict(
    "_RequiredListTablesRequestRequestTypeDef",
    {
        "workbookId": str,
    },
)
_OptionalListTablesRequestRequestTypeDef = TypedDict(
    "_OptionalListTablesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTablesRequestRequestTypeDef(
    _RequiredListTablesRequestRequestTypeDef, _OptionalListTablesRequestRequestTypeDef
):
    pass

ListTablesResultTypeDef = TypedDict(
    "ListTablesResultTypeDef",
    {
        "tables": List["TableTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredQueryTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredQueryTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "filterFormula": "FilterTypeDef",
    },
)
_OptionalQueryTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalQueryTableRowsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class QueryTableRowsRequestRequestTypeDef(
    _RequiredQueryTableRowsRequestRequestTypeDef, _OptionalQueryTableRowsRequestRequestTypeDef
):
    pass

QueryTableRowsResultTypeDef = TypedDict(
    "QueryTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredResultRowTypeDef = TypedDict(
    "_RequiredResultRowTypeDef",
    {
        "dataItems": List["DataItemTypeDef"],
    },
)
_OptionalResultRowTypeDef = TypedDict(
    "_OptionalResultRowTypeDef",
    {
        "rowId": str,
    },
    total=False,
)

class ResultRowTypeDef(_RequiredResultRowTypeDef, _OptionalResultRowTypeDef):
    pass

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "headers": List["ColumnMetadataTypeDef"],
        "rows": List["ResultRowTypeDef"],
    },
)

SourceDataColumnPropertiesTypeDef = TypedDict(
    "SourceDataColumnPropertiesTypeDef",
    {
        "columnIndex": int,
    },
    total=False,
)

StartTableDataImportJobRequestRequestTypeDef = TypedDict(
    "StartTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "dataSource": "ImportDataSourceTypeDef",
        "dataFormat": Literal["DELIMITED_TEXT"],
        "destinationTableId": str,
        "importOptions": "ImportOptionsTypeDef",
        "clientRequestToken": str,
    },
)

StartTableDataImportJobResultTypeDef = TypedDict(
    "StartTableDataImportJobResultTypeDef",
    {
        "jobId": str,
        "jobStatus": TableDataImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableColumnTypeDef = TypedDict(
    "TableColumnTypeDef",
    {
        "tableColumnId": str,
        "tableColumnName": str,
        "format": FormatType,
    },
    total=False,
)

TableDataImportJobMetadataTypeDef = TypedDict(
    "TableDataImportJobMetadataTypeDef",
    {
        "submitter": "ImportJobSubmitterTypeDef",
        "submitTime": datetime,
        "importOptions": "ImportOptionsTypeDef",
        "dataSource": "ImportDataSourceTypeDef",
    },
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "rowId": str,
        "cells": List["CellTypeDef"],
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "tableId": str,
        "tableName": str,
    },
    total=False,
)

UpdateRowDataTypeDef = TypedDict(
    "UpdateRowDataTypeDef",
    {
        "rowId": str,
        "cellsToUpdate": Dict[str, "CellInputTypeDef"],
    },
)

UpsertRowDataTypeDef = TypedDict(
    "UpsertRowDataTypeDef",
    {
        "batchItemId": str,
        "filter": "FilterTypeDef",
        "cellsToUpdate": Dict[str, "CellInputTypeDef"],
    },
)

UpsertRowsResultTypeDef = TypedDict(
    "UpsertRowsResultTypeDef",
    {
        "rowIds": List[str],
        "upsertAction": UpsertActionType,
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "rawValue": str,
    },
)
