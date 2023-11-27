"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs.html)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import AclConfigurationTypeDef

    data: AclConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CalculationExecutionStateType,
    CapacityAllocationStatusType,
    CapacityReservationStatusType,
    ColumnNullableType,
    DataCatalogTypeType,
    EncryptionOptionType,
    ExecutorStateType,
    ExecutorTypeType,
    QueryExecutionStateType,
    SessionStateType,
    StatementTypeType,
    WorkGroupStateType,
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
    "AclConfigurationTypeDef",
    "ApplicationDPUSizesTypeDef",
    "AthenaErrorTypeDef",
    "BatchGetNamedQueryInputRequestTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetPreparedStatementInputRequestTypeDef",
    "BatchGetPreparedStatementOutputTypeDef",
    "BatchGetQueryExecutionInputRequestTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "CalculationConfigurationTypeDef",
    "CalculationResultTypeDef",
    "CalculationStatisticsTypeDef",
    "CalculationStatusTypeDef",
    "CalculationSummaryTypeDef",
    "CancelCapacityReservationInputRequestTypeDef",
    "CapacityAllocationTypeDef",
    "CapacityAssignmentConfigurationTypeDef",
    "CapacityAssignmentTypeDef",
    "CapacityReservationTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateCapacityReservationInputRequestTypeDef",
    "CreateDataCatalogInputRequestTypeDef",
    "CreateNamedQueryInputRequestTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "CreateNotebookInputRequestTypeDef",
    "CreateNotebookOutputTypeDef",
    "CreatePreparedStatementInputRequestTypeDef",
    "CreatePresignedNotebookUrlRequestRequestTypeDef",
    "CreatePresignedNotebookUrlResponseTypeDef",
    "CreateWorkGroupInputRequestTypeDef",
    "CustomerContentEncryptionConfigurationTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteCapacityReservationInputRequestTypeDef",
    "DeleteDataCatalogInputRequestTypeDef",
    "DeleteNamedQueryInputRequestTypeDef",
    "DeleteNotebookInputRequestTypeDef",
    "DeletePreparedStatementInputRequestTypeDef",
    "DeleteWorkGroupInputRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineConfigurationTypeDef",
    "EngineVersionTypeDef",
    "ExecutorsSummaryTypeDef",
    "ExportNotebookInputRequestTypeDef",
    "ExportNotebookOutputTypeDef",
    "FilterDefinitionTypeDef",
    "GetCalculationExecutionCodeRequestRequestTypeDef",
    "GetCalculationExecutionCodeResponseTypeDef",
    "GetCalculationExecutionRequestRequestTypeDef",
    "GetCalculationExecutionResponseTypeDef",
    "GetCalculationExecutionStatusRequestRequestTypeDef",
    "GetCalculationExecutionStatusResponseTypeDef",
    "GetCapacityAssignmentConfigurationInputRequestTypeDef",
    "GetCapacityAssignmentConfigurationOutputTypeDef",
    "GetCapacityReservationInputRequestTypeDef",
    "GetCapacityReservationOutputTypeDef",
    "GetDataCatalogInputRequestTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryInputRequestTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetNotebookMetadataInputRequestTypeDef",
    "GetNotebookMetadataOutputTypeDef",
    "GetPreparedStatementInputRequestTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionInputRequestTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetQueryRuntimeStatisticsInputRequestTypeDef",
    "GetQueryRuntimeStatisticsOutputTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetSessionStatusRequestRequestTypeDef",
    "GetSessionStatusResponseTypeDef",
    "GetTableMetadataInputRequestTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupInputRequestTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ImportNotebookInputRequestTypeDef",
    "ImportNotebookOutputTypeDef",
    "ListApplicationDPUSizesInputRequestTypeDef",
    "ListApplicationDPUSizesOutputTypeDef",
    "ListCalculationExecutionsRequestRequestTypeDef",
    "ListCalculationExecutionsResponseTypeDef",
    "ListCapacityReservationsInputRequestTypeDef",
    "ListCapacityReservationsOutputTypeDef",
    "ListDataCatalogsInputRequestTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsInputRequestTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListExecutorsRequestRequestTypeDef",
    "ListExecutorsResponseTypeDef",
    "ListNamedQueriesInputRequestTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListNotebookMetadataInputRequestTypeDef",
    "ListNotebookMetadataOutputTypeDef",
    "ListNotebookSessionsRequestRequestTypeDef",
    "ListNotebookSessionsResponseTypeDef",
    "ListPreparedStatementsInputRequestTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsInputRequestTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListTableMetadataInputRequestTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsInputRequestTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "NotebookMetadataTypeDef",
    "NotebookSessionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "PutCapacityAssignmentConfigurationInputRequestTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "QueryRuntimeStatisticsRowsTypeDef",
    "QueryRuntimeStatisticsTimelineTypeDef",
    "QueryRuntimeStatisticsTypeDef",
    "QueryStagePlanNodeTypeDef",
    "QueryStageTypeDef",
    "ResponseMetadataTypeDef",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultReuseByAgeConfigurationTypeDef",
    "ResultReuseConfigurationTypeDef",
    "ResultReuseInformationTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "SessionConfigurationTypeDef",
    "SessionStatisticsTypeDef",
    "SessionStatusTypeDef",
    "SessionSummaryTypeDef",
    "StartCalculationExecutionRequestRequestTypeDef",
    "StartCalculationExecutionResponseTypeDef",
    "StartQueryExecutionInputRequestTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "StartSessionRequestRequestTypeDef",
    "StartSessionResponseTypeDef",
    "StopCalculationExecutionRequestRequestTypeDef",
    "StopCalculationExecutionResponseTypeDef",
    "StopQueryExecutionInputRequestTypeDef",
    "TableMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TerminateSessionRequestRequestTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedPreparedStatementNameTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateCapacityReservationInputRequestTypeDef",
    "UpdateDataCatalogInputRequestTypeDef",
    "UpdateNamedQueryInputRequestTypeDef",
    "UpdateNotebookInputRequestTypeDef",
    "UpdateNotebookMetadataInputRequestTypeDef",
    "UpdatePreparedStatementInputRequestTypeDef",
    "UpdateWorkGroupInputRequestTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "S3AclOption": Literal["BUCKET_OWNER_FULL_CONTROL"],
    },
)

ApplicationDPUSizesTypeDef = TypedDict(
    "ApplicationDPUSizesTypeDef",
    {
        "ApplicationRuntimeId": str,
        "SupportedDPUSizes": List[int],
    },
    total=False,
)

AthenaErrorTypeDef = TypedDict(
    "AthenaErrorTypeDef",
    {
        "ErrorCategory": int,
        "ErrorType": int,
        "Retryable": bool,
        "ErrorMessage": str,
    },
    total=False,
)

BatchGetNamedQueryInputRequestTypeDef = TypedDict(
    "BatchGetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryIds": List[str],
    },
)

BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetPreparedStatementInputRequestTypeDef = TypedDict(
    "BatchGetPreparedStatementInputRequestTypeDef",
    {
        "PreparedStatementNames": List[str],
        "WorkGroup": str,
    },
)

BatchGetPreparedStatementOutputTypeDef = TypedDict(
    "BatchGetPreparedStatementOutputTypeDef",
    {
        "PreparedStatements": List["PreparedStatementTypeDef"],
        "UnprocessedPreparedStatementNames": List["UnprocessedPreparedStatementNameTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetQueryExecutionInputRequestTypeDef = TypedDict(
    "BatchGetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionIds": List[str],
    },
)

BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List["QueryExecutionTypeDef"],
        "UnprocessedQueryExecutionIds": List["UnprocessedQueryExecutionIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculationConfigurationTypeDef = TypedDict(
    "CalculationConfigurationTypeDef",
    {
        "CodeBlock": str,
    },
    total=False,
)

CalculationResultTypeDef = TypedDict(
    "CalculationResultTypeDef",
    {
        "StdOutS3Uri": str,
        "StdErrorS3Uri": str,
        "ResultS3Uri": str,
        "ResultType": str,
    },
    total=False,
)

CalculationStatisticsTypeDef = TypedDict(
    "CalculationStatisticsTypeDef",
    {
        "DpuExecutionInMillis": int,
        "Progress": str,
    },
    total=False,
)

CalculationStatusTypeDef = TypedDict(
    "CalculationStatusTypeDef",
    {
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
        "State": CalculationExecutionStateType,
        "StateChangeReason": str,
    },
    total=False,
)

CalculationSummaryTypeDef = TypedDict(
    "CalculationSummaryTypeDef",
    {
        "CalculationExecutionId": str,
        "Description": str,
        "Status": "CalculationStatusTypeDef",
    },
    total=False,
)

CancelCapacityReservationInputRequestTypeDef = TypedDict(
    "CancelCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredCapacityAllocationTypeDef = TypedDict(
    "_RequiredCapacityAllocationTypeDef",
    {
        "Status": CapacityAllocationStatusType,
        "RequestTime": datetime,
    },
)
_OptionalCapacityAllocationTypeDef = TypedDict(
    "_OptionalCapacityAllocationTypeDef",
    {
        "StatusMessage": str,
        "RequestCompletionTime": datetime,
    },
    total=False,
)

class CapacityAllocationTypeDef(
    _RequiredCapacityAllocationTypeDef, _OptionalCapacityAllocationTypeDef
):
    pass

CapacityAssignmentConfigurationTypeDef = TypedDict(
    "CapacityAssignmentConfigurationTypeDef",
    {
        "CapacityReservationName": str,
        "CapacityAssignments": List["CapacityAssignmentTypeDef"],
    },
    total=False,
)

CapacityAssignmentTypeDef = TypedDict(
    "CapacityAssignmentTypeDef",
    {
        "WorkGroupNames": List[str],
    },
    total=False,
)

_RequiredCapacityReservationTypeDef = TypedDict(
    "_RequiredCapacityReservationTypeDef",
    {
        "Name": str,
        "Status": CapacityReservationStatusType,
        "TargetDpus": int,
        "AllocatedDpus": int,
        "CreationTime": datetime,
    },
)
_OptionalCapacityReservationTypeDef = TypedDict(
    "_OptionalCapacityReservationTypeDef",
    {
        "LastAllocation": "CapacityAllocationTypeDef",
        "LastSuccessfulAllocationTime": datetime,
    },
    total=False,
)

class CapacityReservationTypeDef(
    _RequiredCapacityReservationTypeDef, _OptionalCapacityReservationTypeDef
):
    pass

_RequiredColumnInfoTypeDef = TypedDict(
    "_RequiredColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Label": str,
        "Precision": int,
        "Scale": int,
        "Nullable": ColumnNullableType,
        "CaseSensitive": bool,
    },
    total=False,
)

class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass

_RequiredColumnTypeDef = TypedDict(
    "_RequiredColumnTypeDef",
    {
        "Name": str,
    },
)
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {
        "Type": str,
        "Comment": str,
    },
    total=False,
)

class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass

_RequiredCreateCapacityReservationInputRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityReservationInputRequestTypeDef",
    {
        "TargetDpus": int,
        "Name": str,
    },
)
_OptionalCreateCapacityReservationInputRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityReservationInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCapacityReservationInputRequestTypeDef(
    _RequiredCreateCapacityReservationInputRequestTypeDef,
    _OptionalCreateCapacityReservationInputRequestTypeDef,
):
    pass

_RequiredCreateDataCatalogInputRequestTypeDef = TypedDict(
    "_RequiredCreateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalCreateDataCatalogInputRequestTypeDef = TypedDict(
    "_OptionalCreateDataCatalogInputRequestTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataCatalogInputRequestTypeDef(
    _RequiredCreateDataCatalogInputRequestTypeDef, _OptionalCreateDataCatalogInputRequestTypeDef
):
    pass

_RequiredCreateNamedQueryInputRequestTypeDef = TypedDict(
    "_RequiredCreateNamedQueryInputRequestTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalCreateNamedQueryInputRequestTypeDef = TypedDict(
    "_OptionalCreateNamedQueryInputRequestTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "WorkGroup": str,
    },
    total=False,
)

class CreateNamedQueryInputRequestTypeDef(
    _RequiredCreateNamedQueryInputRequestTypeDef, _OptionalCreateNamedQueryInputRequestTypeDef
):
    pass

CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNotebookInputRequestTypeDef = TypedDict(
    "_RequiredCreateNotebookInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Name": str,
    },
)
_OptionalCreateNotebookInputRequestTypeDef = TypedDict(
    "_OptionalCreateNotebookInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateNotebookInputRequestTypeDef(
    _RequiredCreateNotebookInputRequestTypeDef, _OptionalCreateNotebookInputRequestTypeDef
):
    pass

CreateNotebookOutputTypeDef = TypedDict(
    "CreateNotebookOutputTypeDef",
    {
        "NotebookId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePreparedStatementInputRequestTypeDef = TypedDict(
    "_RequiredCreatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalCreatePreparedStatementInputRequestTypeDef = TypedDict(
    "_OptionalCreatePreparedStatementInputRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreatePreparedStatementInputRequestTypeDef(
    _RequiredCreatePreparedStatementInputRequestTypeDef,
    _OptionalCreatePreparedStatementInputRequestTypeDef,
):
    pass

CreatePresignedNotebookUrlRequestRequestTypeDef = TypedDict(
    "CreatePresignedNotebookUrlRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

CreatePresignedNotebookUrlResponseTypeDef = TypedDict(
    "CreatePresignedNotebookUrlResponseTypeDef",
    {
        "NotebookUrl": str,
        "AuthToken": str,
        "AuthTokenExpirationTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateWorkGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateWorkGroupInputRequestTypeDef",
    {
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkGroupInputRequestTypeDef(
    _RequiredCreateWorkGroupInputRequestTypeDef, _OptionalCreateWorkGroupInputRequestTypeDef
):
    pass

CustomerContentEncryptionConfigurationTypeDef = TypedDict(
    "CustomerContentEncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)

DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": str,
        "Type": DataCatalogTypeType,
    },
    total=False,
)

_RequiredDataCatalogTypeDef = TypedDict(
    "_RequiredDataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalDataCatalogTypeDef = TypedDict(
    "_OptionalDataCatalogTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class DataCatalogTypeDef(_RequiredDataCatalogTypeDef, _OptionalDataCatalogTypeDef):
    pass

_RequiredDatabaseTypeDef = TypedDict(
    "_RequiredDatabaseTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseTypeDef = TypedDict(
    "_OptionalDatabaseTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "VarCharValue": str,
    },
    total=False,
)

DeleteCapacityReservationInputRequestTypeDef = TypedDict(
    "DeleteCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDataCatalogInputRequestTypeDef = TypedDict(
    "DeleteDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteNamedQueryInputRequestTypeDef = TypedDict(
    "DeleteNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

DeleteNotebookInputRequestTypeDef = TypedDict(
    "DeleteNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)

DeletePreparedStatementInputRequestTypeDef = TypedDict(
    "DeletePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

_RequiredDeleteWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalDeleteWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkGroupInputRequestTypeDef",
    {
        "RecursiveDeleteOption": bool,
    },
    total=False,
)

class DeleteWorkGroupInputRequestTypeDef(
    _RequiredDeleteWorkGroupInputRequestTypeDef, _OptionalDeleteWorkGroupInputRequestTypeDef
):
    pass

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "EncryptionOption": EncryptionOptionType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
    total=False,
)

class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass

_RequiredEngineConfigurationTypeDef = TypedDict(
    "_RequiredEngineConfigurationTypeDef",
    {
        "MaxConcurrentDpus": int,
    },
)
_OptionalEngineConfigurationTypeDef = TypedDict(
    "_OptionalEngineConfigurationTypeDef",
    {
        "CoordinatorDpuSize": int,
        "DefaultExecutorDpuSize": int,
        "AdditionalConfigs": Dict[str, str],
        "SparkProperties": Dict[str, str],
    },
    total=False,
)

class EngineConfigurationTypeDef(
    _RequiredEngineConfigurationTypeDef, _OptionalEngineConfigurationTypeDef
):
    pass

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "SelectedEngineVersion": str,
        "EffectiveEngineVersion": str,
    },
    total=False,
)

_RequiredExecutorsSummaryTypeDef = TypedDict(
    "_RequiredExecutorsSummaryTypeDef",
    {
        "ExecutorId": str,
    },
)
_OptionalExecutorsSummaryTypeDef = TypedDict(
    "_OptionalExecutorsSummaryTypeDef",
    {
        "ExecutorType": ExecutorTypeType,
        "StartDateTime": int,
        "TerminationDateTime": int,
        "ExecutorState": ExecutorStateType,
        "ExecutorSize": int,
    },
    total=False,
)

class ExecutorsSummaryTypeDef(_RequiredExecutorsSummaryTypeDef, _OptionalExecutorsSummaryTypeDef):
    pass

ExportNotebookInputRequestTypeDef = TypedDict(
    "ExportNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)

ExportNotebookOutputTypeDef = TypedDict(
    "ExportNotebookOutputTypeDef",
    {
        "NotebookMetadata": "NotebookMetadataTypeDef",
        "Payload": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterDefinitionTypeDef = TypedDict(
    "FilterDefinitionTypeDef",
    {
        "Name": str,
    },
    total=False,
)

GetCalculationExecutionCodeRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionCodeRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)

GetCalculationExecutionCodeResponseTypeDef = TypedDict(
    "GetCalculationExecutionCodeResponseTypeDef",
    {
        "CodeBlock": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCalculationExecutionRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)

GetCalculationExecutionResponseTypeDef = TypedDict(
    "GetCalculationExecutionResponseTypeDef",
    {
        "CalculationExecutionId": str,
        "SessionId": str,
        "Description": str,
        "WorkingDirectory": str,
        "Status": "CalculationStatusTypeDef",
        "Statistics": "CalculationStatisticsTypeDef",
        "Result": "CalculationResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCalculationExecutionStatusRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionStatusRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)

GetCalculationExecutionStatusResponseTypeDef = TypedDict(
    "GetCalculationExecutionStatusResponseTypeDef",
    {
        "Status": "CalculationStatusTypeDef",
        "Statistics": "CalculationStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCapacityAssignmentConfigurationInputRequestTypeDef = TypedDict(
    "GetCapacityAssignmentConfigurationInputRequestTypeDef",
    {
        "CapacityReservationName": str,
    },
)

GetCapacityAssignmentConfigurationOutputTypeDef = TypedDict(
    "GetCapacityAssignmentConfigurationOutputTypeDef",
    {
        "CapacityAssignmentConfiguration": "CapacityAssignmentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCapacityReservationInputRequestTypeDef = TypedDict(
    "GetCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetCapacityReservationOutputTypeDef = TypedDict(
    "GetCapacityReservationOutputTypeDef",
    {
        "CapacityReservation": "CapacityReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataCatalogInputRequestTypeDef = TypedDict(
    "GetDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {
        "DataCatalog": "DataCatalogTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamedQueryInputRequestTypeDef = TypedDict(
    "GetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {
        "NamedQuery": "NamedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotebookMetadataInputRequestTypeDef = TypedDict(
    "GetNotebookMetadataInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)

GetNotebookMetadataOutputTypeDef = TypedDict(
    "GetNotebookMetadataOutputTypeDef",
    {
        "NotebookMetadata": "NotebookMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPreparedStatementInputRequestTypeDef = TypedDict(
    "GetPreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

GetPreparedStatementOutputTypeDef = TypedDict(
    "GetPreparedStatementOutputTypeDef",
    {
        "PreparedStatement": "PreparedStatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryExecutionInputRequestTypeDef = TypedDict(
    "GetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {
        "QueryExecution": "QueryExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsInputRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)
_OptionalGetQueryResultsInputRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetQueryResultsInputRequestTypeDef(
    _RequiredGetQueryResultsInputRequestTypeDef, _OptionalGetQueryResultsInputRequestTypeDef
):
    pass

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryRuntimeStatisticsInputRequestTypeDef = TypedDict(
    "GetQueryRuntimeStatisticsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

GetQueryRuntimeStatisticsOutputTypeDef = TypedDict(
    "GetQueryRuntimeStatisticsOutputTypeDef",
    {
        "QueryRuntimeStatistics": "QueryRuntimeStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "SessionId": str,
        "Description": str,
        "WorkGroup": str,
        "EngineVersion": str,
        "EngineConfiguration": "EngineConfigurationTypeDef",
        "NotebookVersion": str,
        "SessionConfiguration": "SessionConfigurationTypeDef",
        "Status": "SessionStatusTypeDef",
        "Statistics": "SessionStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionStatusRequestRequestTypeDef = TypedDict(
    "GetSessionStatusRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

GetSessionStatusResponseTypeDef = TypedDict(
    "GetSessionStatusResponseTypeDef",
    {
        "SessionId": str,
        "Status": "SessionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableMetadataInputRequestTypeDef = TypedDict(
    "GetTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "TableName": str,
    },
)

GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {
        "TableMetadata": "TableMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkGroupInputRequestTypeDef = TypedDict(
    "GetWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)

GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {
        "WorkGroup": "WorkGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportNotebookInputRequestTypeDef = TypedDict(
    "_RequiredImportNotebookInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Name": str,
        "Payload": str,
        "Type": Literal["IPYNB"],
    },
)
_OptionalImportNotebookInputRequestTypeDef = TypedDict(
    "_OptionalImportNotebookInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class ImportNotebookInputRequestTypeDef(
    _RequiredImportNotebookInputRequestTypeDef, _OptionalImportNotebookInputRequestTypeDef
):
    pass

ImportNotebookOutputTypeDef = TypedDict(
    "ImportNotebookOutputTypeDef",
    {
        "NotebookId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationDPUSizesInputRequestTypeDef = TypedDict(
    "ListApplicationDPUSizesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationDPUSizesOutputTypeDef = TypedDict(
    "ListApplicationDPUSizesOutputTypeDef",
    {
        "ApplicationDPUSizes": List["ApplicationDPUSizesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCalculationExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListCalculationExecutionsRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
_OptionalListCalculationExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListCalculationExecutionsRequestRequestTypeDef",
    {
        "StateFilter": CalculationExecutionStateType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCalculationExecutionsRequestRequestTypeDef(
    _RequiredListCalculationExecutionsRequestRequestTypeDef,
    _OptionalListCalculationExecutionsRequestRequestTypeDef,
):
    pass

ListCalculationExecutionsResponseTypeDef = TypedDict(
    "ListCalculationExecutionsResponseTypeDef",
    {
        "NextToken": str,
        "Calculations": List["CalculationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCapacityReservationsInputRequestTypeDef = TypedDict(
    "ListCapacityReservationsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCapacityReservationsOutputTypeDef = TypedDict(
    "ListCapacityReservationsOutputTypeDef",
    {
        "NextToken": str,
        "CapacityReservations": List["CapacityReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataCatalogsInputRequestTypeDef = TypedDict(
    "ListDataCatalogsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatabasesInputRequestTypeDef = TypedDict(
    "_RequiredListDatabasesInputRequestTypeDef",
    {
        "CatalogName": str,
    },
)
_OptionalListDatabasesInputRequestTypeDef = TypedDict(
    "_OptionalListDatabasesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatabasesInputRequestTypeDef(
    _RequiredListDatabasesInputRequestTypeDef, _OptionalListDatabasesInputRequestTypeDef
):
    pass

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsInputRequestTypeDef = TypedDict(
    "ListEngineVersionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEngineVersionsOutputTypeDef = TypedDict(
    "ListEngineVersionsOutputTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutorsRequestRequestTypeDef = TypedDict(
    "_RequiredListExecutorsRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
_OptionalListExecutorsRequestRequestTypeDef = TypedDict(
    "_OptionalListExecutorsRequestRequestTypeDef",
    {
        "ExecutorStateFilter": ExecutorStateType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListExecutorsRequestRequestTypeDef(
    _RequiredListExecutorsRequestRequestTypeDef, _OptionalListExecutorsRequestRequestTypeDef
):
    pass

ListExecutorsResponseTypeDef = TypedDict(
    "ListExecutorsResponseTypeDef",
    {
        "SessionId": str,
        "NextToken": str,
        "ExecutorsSummary": List["ExecutorsSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedQueriesInputRequestTypeDef = TypedDict(
    "ListNamedQueriesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {
        "NamedQueryIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNotebookMetadataInputRequestTypeDef = TypedDict(
    "_RequiredListNotebookMetadataInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalListNotebookMetadataInputRequestTypeDef = TypedDict(
    "_OptionalListNotebookMetadataInputRequestTypeDef",
    {
        "Filters": "FilterDefinitionTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListNotebookMetadataInputRequestTypeDef(
    _RequiredListNotebookMetadataInputRequestTypeDef,
    _OptionalListNotebookMetadataInputRequestTypeDef,
):
    pass

ListNotebookMetadataOutputTypeDef = TypedDict(
    "ListNotebookMetadataOutputTypeDef",
    {
        "NextToken": str,
        "NotebookMetadataList": List["NotebookMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNotebookSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListNotebookSessionsRequestRequestTypeDef",
    {
        "NotebookId": str,
    },
)
_OptionalListNotebookSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListNotebookSessionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListNotebookSessionsRequestRequestTypeDef(
    _RequiredListNotebookSessionsRequestRequestTypeDef,
    _OptionalListNotebookSessionsRequestRequestTypeDef,
):
    pass

ListNotebookSessionsResponseTypeDef = TypedDict(
    "ListNotebookSessionsResponseTypeDef",
    {
        "NotebookSessionsList": List["NotebookSessionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPreparedStatementsInputRequestTypeDef = TypedDict(
    "_RequiredListPreparedStatementsInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalListPreparedStatementsInputRequestTypeDef = TypedDict(
    "_OptionalListPreparedStatementsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPreparedStatementsInputRequestTypeDef(
    _RequiredListPreparedStatementsInputRequestTypeDef,
    _OptionalListPreparedStatementsInputRequestTypeDef,
):
    pass

ListPreparedStatementsOutputTypeDef = TypedDict(
    "ListPreparedStatementsOutputTypeDef",
    {
        "PreparedStatements": List["PreparedStatementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryExecutionsInputRequestTypeDef = TypedDict(
    "ListQueryExecutionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {
        "QueryExecutionIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionsRequestRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalListSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionsRequestRequestTypeDef",
    {
        "StateFilter": SessionStateType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSessionsRequestRequestTypeDef(
    _RequiredListSessionsRequestRequestTypeDef, _OptionalListSessionsRequestRequestTypeDef
):
    pass

ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "NextToken": str,
        "Sessions": List["SessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableMetadataInputRequestTypeDef = TypedDict(
    "_RequiredListTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)
_OptionalListTableMetadataInputRequestTypeDef = TypedDict(
    "_OptionalListTableMetadataInputRequestTypeDef",
    {
        "Expression": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTableMetadataInputRequestTypeDef(
    _RequiredListTableMetadataInputRequestTypeDef, _OptionalListTableMetadataInputRequestTypeDef
):
    pass

ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkGroupsInputRequestTypeDef = TypedDict(
    "ListWorkGroupsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List["WorkGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNamedQueryTypeDef = TypedDict(
    "_RequiredNamedQueryTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalNamedQueryTypeDef = TypedDict(
    "_OptionalNamedQueryTypeDef",
    {
        "Description": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)

class NamedQueryTypeDef(_RequiredNamedQueryTypeDef, _OptionalNamedQueryTypeDef):
    pass

NotebookMetadataTypeDef = TypedDict(
    "NotebookMetadataTypeDef",
    {
        "NotebookId": str,
        "Name": str,
        "WorkGroup": str,
        "CreationTime": datetime,
        "Type": Literal["IPYNB"],
        "LastModifiedTime": datetime,
    },
    total=False,
)

NotebookSessionSummaryTypeDef = TypedDict(
    "NotebookSessionSummaryTypeDef",
    {
        "SessionId": str,
        "CreationTime": datetime,
    },
    total=False,
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

PreparedStatementSummaryTypeDef = TypedDict(
    "PreparedStatementSummaryTypeDef",
    {
        "StatementName": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

PreparedStatementTypeDef = TypedDict(
    "PreparedStatementTypeDef",
    {
        "StatementName": str,
        "QueryStatement": str,
        "WorkGroupName": str,
        "Description": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

PutCapacityAssignmentConfigurationInputRequestTypeDef = TypedDict(
    "PutCapacityAssignmentConfigurationInputRequestTypeDef",
    {
        "CapacityReservationName": str,
        "CapacityAssignments": List["CapacityAssignmentTypeDef"],
    },
)

QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef",
    {
        "Database": str,
        "Catalog": str,
    },
    total=False,
)

QueryExecutionStatisticsTypeDef = TypedDict(
    "QueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
        "TotalExecutionTimeInMillis": int,
        "QueryQueueTimeInMillis": int,
        "ServicePreProcessingTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
        "ResultReuseInformation": "ResultReuseInformationTypeDef",
    },
    total=False,
)

QueryExecutionStatusTypeDef = TypedDict(
    "QueryExecutionStatusTypeDef",
    {
        "State": QueryExecutionStateType,
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
        "AthenaError": "AthenaErrorTypeDef",
    },
    total=False,
)

QueryExecutionTypeDef = TypedDict(
    "QueryExecutionTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": StatementTypeType,
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "ResultReuseConfiguration": "ResultReuseConfigurationTypeDef",
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "Status": "QueryExecutionStatusTypeDef",
        "Statistics": "QueryExecutionStatisticsTypeDef",
        "WorkGroup": str,
        "EngineVersion": "EngineVersionTypeDef",
        "ExecutionParameters": List[str],
        "SubstatementType": str,
    },
    total=False,
)

QueryRuntimeStatisticsRowsTypeDef = TypedDict(
    "QueryRuntimeStatisticsRowsTypeDef",
    {
        "InputRows": int,
        "InputBytes": int,
        "OutputBytes": int,
        "OutputRows": int,
    },
    total=False,
)

QueryRuntimeStatisticsTimelineTypeDef = TypedDict(
    "QueryRuntimeStatisticsTimelineTypeDef",
    {
        "QueryQueueTimeInMillis": int,
        "ServicePreProcessingTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "EngineExecutionTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
        "TotalExecutionTimeInMillis": int,
    },
    total=False,
)

QueryRuntimeStatisticsTypeDef = TypedDict(
    "QueryRuntimeStatisticsTypeDef",
    {
        "Timeline": "QueryRuntimeStatisticsTimelineTypeDef",
        "Rows": "QueryRuntimeStatisticsRowsTypeDef",
        "OutputStage": "QueryStageTypeDef",
    },
    total=False,
)

QueryStagePlanNodeTypeDef = TypedDict(
    "QueryStagePlanNodeTypeDef",
    {
        "Name": str,
        "Identifier": str,
        "Children": List[Dict[str, Any]],
        "RemoteSources": List[str],
    },
    total=False,
)

QueryStageTypeDef = TypedDict(
    "QueryStageTypeDef",
    {
        "StageId": int,
        "State": str,
        "OutputBytes": int,
        "OutputRows": int,
        "InputBytes": int,
        "InputRows": int,
        "ExecutionTime": int,
        "QueryStagePlan": "QueryStagePlanNodeTypeDef",
        "SubStages": List[Dict[str, Any]],
    },
    total=False,
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

ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "ExpectedBucketOwner": str,
        "AclConfiguration": "AclConfigurationTypeDef",
    },
    total=False,
)

ResultConfigurationUpdatesTypeDef = TypedDict(
    "ResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "RemoveEncryptionConfiguration": bool,
        "ExpectedBucketOwner": str,
        "RemoveExpectedBucketOwner": bool,
        "AclConfiguration": "AclConfigurationTypeDef",
        "RemoveAclConfiguration": bool,
    },
    total=False,
)

_RequiredResultReuseByAgeConfigurationTypeDef = TypedDict(
    "_RequiredResultReuseByAgeConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalResultReuseByAgeConfigurationTypeDef = TypedDict(
    "_OptionalResultReuseByAgeConfigurationTypeDef",
    {
        "MaxAgeInMinutes": int,
    },
    total=False,
)

class ResultReuseByAgeConfigurationTypeDef(
    _RequiredResultReuseByAgeConfigurationTypeDef, _OptionalResultReuseByAgeConfigurationTypeDef
):
    pass

ResultReuseConfigurationTypeDef = TypedDict(
    "ResultReuseConfigurationTypeDef",
    {
        "ResultReuseByAgeConfiguration": "ResultReuseByAgeConfigurationTypeDef",
    },
    total=False,
)

ResultReuseInformationTypeDef = TypedDict(
    "ResultReuseInformationTypeDef",
    {
        "ReusedPreviousResult": bool,
    },
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "ColumnInfo": List["ColumnInfoTypeDef"],
    },
    total=False,
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "Rows": List["RowTypeDef"],
        "ResultSetMetadata": "ResultSetMetadataTypeDef",
    },
    total=False,
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List["DatumTypeDef"],
    },
    total=False,
)

SessionConfigurationTypeDef = TypedDict(
    "SessionConfigurationTypeDef",
    {
        "ExecutionRole": str,
        "WorkingDirectory": str,
        "IdleTimeoutSeconds": int,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

SessionStatisticsTypeDef = TypedDict(
    "SessionStatisticsTypeDef",
    {
        "DpuExecutionInMillis": int,
    },
    total=False,
)

SessionStatusTypeDef = TypedDict(
    "SessionStatusTypeDef",
    {
        "StartDateTime": datetime,
        "LastModifiedDateTime": datetime,
        "EndDateTime": datetime,
        "IdleSinceDateTime": datetime,
        "State": SessionStateType,
        "StateChangeReason": str,
    },
    total=False,
)

SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "SessionId": str,
        "Description": str,
        "EngineVersion": "EngineVersionTypeDef",
        "NotebookVersion": str,
        "Status": "SessionStatusTypeDef",
    },
    total=False,
)

_RequiredStartCalculationExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartCalculationExecutionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
_OptionalStartCalculationExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartCalculationExecutionRequestRequestTypeDef",
    {
        "Description": str,
        "CalculationConfiguration": "CalculationConfigurationTypeDef",
        "CodeBlock": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class StartCalculationExecutionRequestRequestTypeDef(
    _RequiredStartCalculationExecutionRequestRequestTypeDef,
    _OptionalStartCalculationExecutionRequestRequestTypeDef,
):
    pass

StartCalculationExecutionResponseTypeDef = TypedDict(
    "StartCalculationExecutionResponseTypeDef",
    {
        "CalculationExecutionId": str,
        "State": CalculationExecutionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartQueryExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartQueryExecutionInputRequestTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalStartQueryExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartQueryExecutionInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "WorkGroup": str,
        "ExecutionParameters": List[str],
        "ResultReuseConfiguration": "ResultReuseConfigurationTypeDef",
    },
    total=False,
)

class StartQueryExecutionInputRequestTypeDef(
    _RequiredStartQueryExecutionInputRequestTypeDef, _OptionalStartQueryExecutionInputRequestTypeDef
):
    pass

StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStartSessionRequestRequestTypeDef",
    {
        "WorkGroup": str,
        "EngineConfiguration": "EngineConfigurationTypeDef",
    },
)
_OptionalStartSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStartSessionRequestRequestTypeDef",
    {
        "Description": str,
        "NotebookVersion": str,
        "SessionIdleTimeoutInMinutes": int,
        "ClientRequestToken": str,
    },
    total=False,
)

class StartSessionRequestRequestTypeDef(
    _RequiredStartSessionRequestRequestTypeDef, _OptionalStartSessionRequestRequestTypeDef
):
    pass

StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {
        "SessionId": str,
        "State": SessionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopCalculationExecutionRequestRequestTypeDef = TypedDict(
    "StopCalculationExecutionRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)

StopCalculationExecutionResponseTypeDef = TypedDict(
    "StopCalculationExecutionResponseTypeDef",
    {
        "State": CalculationExecutionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryExecutionInputRequestTypeDef = TypedDict(
    "StopQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

_RequiredTableMetadataTypeDef = TypedDict(
    "_RequiredTableMetadataTypeDef",
    {
        "Name": str,
    },
)
_OptionalTableMetadataTypeDef = TypedDict(
    "_OptionalTableMetadataTypeDef",
    {
        "CreateTime": datetime,
        "LastAccessTime": datetime,
        "TableType": str,
        "Columns": List["ColumnTypeDef"],
        "PartitionKeys": List["ColumnTypeDef"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

class TableMetadataTypeDef(_RequiredTableMetadataTypeDef, _OptionalTableMetadataTypeDef):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TerminateSessionRequestRequestTypeDef = TypedDict(
    "TerminateSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef",
    {
        "State": SessionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {
        "NamedQueryId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UnprocessedPreparedStatementNameTypeDef = TypedDict(
    "UnprocessedPreparedStatementNameTypeDef",
    {
        "StatementName": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {
        "QueryExecutionId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateCapacityReservationInputRequestTypeDef = TypedDict(
    "UpdateCapacityReservationInputRequestTypeDef",
    {
        "TargetDpus": int,
        "Name": str,
    },
)

_RequiredUpdateDataCatalogInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalUpdateDataCatalogInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataCatalogInputRequestTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class UpdateDataCatalogInputRequestTypeDef(
    _RequiredUpdateDataCatalogInputRequestTypeDef, _OptionalUpdateDataCatalogInputRequestTypeDef
):
    pass

_RequiredUpdateNamedQueryInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
        "Name": str,
        "QueryString": str,
    },
)
_OptionalUpdateNamedQueryInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNamedQueryInputRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateNamedQueryInputRequestTypeDef(
    _RequiredUpdateNamedQueryInputRequestTypeDef, _OptionalUpdateNamedQueryInputRequestTypeDef
):
    pass

_RequiredUpdateNotebookInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
        "Payload": str,
        "Type": Literal["IPYNB"],
    },
)
_OptionalUpdateNotebookInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookInputRequestTypeDef",
    {
        "SessionId": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class UpdateNotebookInputRequestTypeDef(
    _RequiredUpdateNotebookInputRequestTypeDef, _OptionalUpdateNotebookInputRequestTypeDef
):
    pass

_RequiredUpdateNotebookMetadataInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookMetadataInputRequestTypeDef",
    {
        "NotebookId": str,
        "Name": str,
    },
)
_OptionalUpdateNotebookMetadataInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookMetadataInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class UpdateNotebookMetadataInputRequestTypeDef(
    _RequiredUpdateNotebookMetadataInputRequestTypeDef,
    _OptionalUpdateNotebookMetadataInputRequestTypeDef,
):
    pass

_RequiredUpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalUpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePreparedStatementInputRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdatePreparedStatementInputRequestTypeDef(
    _RequiredUpdatePreparedStatementInputRequestTypeDef,
    _OptionalUpdatePreparedStatementInputRequestTypeDef,
):
    pass

_RequiredUpdateWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalUpdateWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkGroupInputRequestTypeDef",
    {
        "Description": str,
        "ConfigurationUpdates": "WorkGroupConfigurationUpdatesTypeDef",
        "State": WorkGroupStateType,
    },
    total=False,
)

class UpdateWorkGroupInputRequestTypeDef(
    _RequiredUpdateWorkGroupInputRequestTypeDef, _OptionalUpdateWorkGroupInputRequestTypeDef
):
    pass

WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
        "EngineVersion": "EngineVersionTypeDef",
        "AdditionalConfiguration": str,
        "ExecutionRole": str,
        "CustomerContentEncryptionConfiguration": "CustomerContentEncryptionConfigurationTypeDef",
        "EnableMinimumEncryptionConfiguration": bool,
    },
    total=False,
)

WorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "WorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": bool,
        "ResultConfigurationUpdates": "ResultConfigurationUpdatesTypeDef",
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RemoveBytesScannedCutoffPerQuery": bool,
        "RequesterPaysEnabled": bool,
        "EngineVersion": "EngineVersionTypeDef",
        "RemoveCustomerContentEncryptionConfiguration": bool,
        "AdditionalConfiguration": str,
        "ExecutionRole": str,
        "CustomerContentEncryptionConfiguration": "CustomerContentEncryptionConfigurationTypeDef",
        "EnableMinimumEncryptionConfiguration": bool,
    },
    total=False,
)

WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": str,
        "State": WorkGroupStateType,
        "Description": str,
        "CreationTime": datetime,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

_RequiredWorkGroupTypeDef = TypedDict(
    "_RequiredWorkGroupTypeDef",
    {
        "Name": str,
    },
)
_OptionalWorkGroupTypeDef = TypedDict(
    "_OptionalWorkGroupTypeDef",
    {
        "State": WorkGroupStateType,
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)

class WorkGroupTypeDef(_RequiredWorkGroupTypeDef, _OptionalWorkGroupTypeDef):
    pass
