"""
Type annotations for athena service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_athena.type_defs import AclConfigurationTypeDef

    data: AclConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    CalculationExecutionStateType,
    CapacityAllocationStatusType,
    CapacityReservationStatusType,
    ColumnNullableType,
    ConnectionTypeType,
    DataCatalogStatusType,
    DataCatalogTypeType,
    EncryptionOptionType,
    ExecutorStateType,
    ExecutorTypeType,
    QueryExecutionStateType,
    SessionStateType,
    StatementTypeType,
    WorkGroupStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AclConfigurationTypeDef",
    "ApplicationDPUSizesTypeDef",
    "AthenaErrorTypeDef",
    "BatchGetNamedQueryInputTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetPreparedStatementInputTypeDef",
    "BatchGetPreparedStatementOutputTypeDef",
    "BatchGetQueryExecutionInputTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "CalculationConfigurationTypeDef",
    "CalculationResultTypeDef",
    "CalculationStatisticsTypeDef",
    "CalculationStatusTypeDef",
    "CalculationSummaryTypeDef",
    "CancelCapacityReservationInputTypeDef",
    "CapacityAllocationTypeDef",
    "CapacityAssignmentConfigurationTypeDef",
    "CapacityAssignmentOutputTypeDef",
    "CapacityAssignmentTypeDef",
    "CapacityAssignmentUnionTypeDef",
    "CapacityReservationTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateCapacityReservationInputTypeDef",
    "CreateDataCatalogInputTypeDef",
    "CreateDataCatalogOutputTypeDef",
    "CreateNamedQueryInputTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "CreateNotebookInputTypeDef",
    "CreateNotebookOutputTypeDef",
    "CreatePreparedStatementInputTypeDef",
    "CreatePresignedNotebookUrlRequestTypeDef",
    "CreatePresignedNotebookUrlResponseTypeDef",
    "CreateWorkGroupInputTypeDef",
    "CustomerContentEncryptionConfigurationTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteCapacityReservationInputTypeDef",
    "DeleteDataCatalogInputTypeDef",
    "DeleteDataCatalogOutputTypeDef",
    "DeleteNamedQueryInputTypeDef",
    "DeleteNotebookInputTypeDef",
    "DeletePreparedStatementInputTypeDef",
    "DeleteWorkGroupInputTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineConfigurationOutputTypeDef",
    "EngineConfigurationTypeDef",
    "EngineConfigurationUnionTypeDef",
    "EngineVersionTypeDef",
    "ExecutorsSummaryTypeDef",
    "ExportNotebookInputTypeDef",
    "ExportNotebookOutputTypeDef",
    "FilterDefinitionTypeDef",
    "GetCalculationExecutionCodeRequestTypeDef",
    "GetCalculationExecutionCodeResponseTypeDef",
    "GetCalculationExecutionRequestTypeDef",
    "GetCalculationExecutionResponseTypeDef",
    "GetCalculationExecutionStatusRequestTypeDef",
    "GetCalculationExecutionStatusResponseTypeDef",
    "GetCapacityAssignmentConfigurationInputTypeDef",
    "GetCapacityAssignmentConfigurationOutputTypeDef",
    "GetCapacityReservationInputTypeDef",
    "GetCapacityReservationOutputTypeDef",
    "GetDataCatalogInputTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseInputTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryInputTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetNotebookMetadataInputTypeDef",
    "GetNotebookMetadataOutputTypeDef",
    "GetPreparedStatementInputTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionInputTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsInputPaginateTypeDef",
    "GetQueryResultsInputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetQueryRuntimeStatisticsInputTypeDef",
    "GetQueryRuntimeStatisticsOutputTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetSessionStatusRequestTypeDef",
    "GetSessionStatusResponseTypeDef",
    "GetTableMetadataInputTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupInputTypeDef",
    "GetWorkGroupOutputTypeDef",
    "IdentityCenterConfigurationTypeDef",
    "ImportNotebookInputTypeDef",
    "ImportNotebookOutputTypeDef",
    "ListApplicationDPUSizesInputTypeDef",
    "ListApplicationDPUSizesOutputTypeDef",
    "ListCalculationExecutionsRequestTypeDef",
    "ListCalculationExecutionsResponseTypeDef",
    "ListCapacityReservationsInputTypeDef",
    "ListCapacityReservationsOutputTypeDef",
    "ListDataCatalogsInputPaginateTypeDef",
    "ListDataCatalogsInputTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesInputPaginateTypeDef",
    "ListDatabasesInputTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsInputTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListExecutorsRequestTypeDef",
    "ListExecutorsResponseTypeDef",
    "ListNamedQueriesInputPaginateTypeDef",
    "ListNamedQueriesInputTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListNotebookMetadataInputTypeDef",
    "ListNotebookMetadataOutputTypeDef",
    "ListNotebookSessionsRequestTypeDef",
    "ListNotebookSessionsResponseTypeDef",
    "ListPreparedStatementsInputTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsInputPaginateTypeDef",
    "ListQueryExecutionsInputTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListTableMetadataInputPaginateTypeDef",
    "ListTableMetadataInputTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsInputTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "NotebookMetadataTypeDef",
    "NotebookSessionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "PutCapacityAssignmentConfigurationInputTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "QueryResultsS3AccessGrantsConfigurationTypeDef",
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
    "StartCalculationExecutionRequestTypeDef",
    "StartCalculationExecutionResponseTypeDef",
    "StartQueryExecutionInputTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "StartSessionRequestTypeDef",
    "StartSessionResponseTypeDef",
    "StopCalculationExecutionRequestTypeDef",
    "StopCalculationExecutionResponseTypeDef",
    "StopQueryExecutionInputTypeDef",
    "TableMetadataTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TerminateSessionRequestTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedPreparedStatementNameTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateCapacityReservationInputTypeDef",
    "UpdateDataCatalogInputTypeDef",
    "UpdateNamedQueryInputTypeDef",
    "UpdateNotebookInputTypeDef",
    "UpdateNotebookMetadataInputTypeDef",
    "UpdatePreparedStatementInputTypeDef",
    "UpdateWorkGroupInputTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

class AclConfigurationTypeDef(TypedDict):
    S3AclOption: Literal["BUCKET_OWNER_FULL_CONTROL"]

class ApplicationDPUSizesTypeDef(TypedDict):
    ApplicationRuntimeId: NotRequired[str]
    SupportedDPUSizes: NotRequired[List[int]]

class AthenaErrorTypeDef(TypedDict):
    ErrorCategory: NotRequired[int]
    ErrorType: NotRequired[int]
    Retryable: NotRequired[bool]
    ErrorMessage: NotRequired[str]

class BatchGetNamedQueryInputTypeDef(TypedDict):
    NamedQueryIds: Sequence[str]

class NamedQueryTypeDef(TypedDict):
    Name: str
    Database: str
    QueryString: str
    Description: NotRequired[str]
    NamedQueryId: NotRequired[str]
    WorkGroup: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UnprocessedNamedQueryIdTypeDef(TypedDict):
    NamedQueryId: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class BatchGetPreparedStatementInputTypeDef(TypedDict):
    PreparedStatementNames: Sequence[str]
    WorkGroup: str

class PreparedStatementTypeDef(TypedDict):
    StatementName: NotRequired[str]
    QueryStatement: NotRequired[str]
    WorkGroupName: NotRequired[str]
    Description: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]

class UnprocessedPreparedStatementNameTypeDef(TypedDict):
    StatementName: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class BatchGetQueryExecutionInputTypeDef(TypedDict):
    QueryExecutionIds: Sequence[str]

class UnprocessedQueryExecutionIdTypeDef(TypedDict):
    QueryExecutionId: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class CalculationConfigurationTypeDef(TypedDict):
    CodeBlock: NotRequired[str]

class CalculationResultTypeDef(TypedDict):
    StdOutS3Uri: NotRequired[str]
    StdErrorS3Uri: NotRequired[str]
    ResultS3Uri: NotRequired[str]
    ResultType: NotRequired[str]

class CalculationStatisticsTypeDef(TypedDict):
    DpuExecutionInMillis: NotRequired[int]
    Progress: NotRequired[str]

class CalculationStatusTypeDef(TypedDict):
    SubmissionDateTime: NotRequired[datetime]
    CompletionDateTime: NotRequired[datetime]
    State: NotRequired[CalculationExecutionStateType]
    StateChangeReason: NotRequired[str]

class CancelCapacityReservationInputTypeDef(TypedDict):
    Name: str

class CapacityAllocationTypeDef(TypedDict):
    Status: CapacityAllocationStatusType
    RequestTime: datetime
    StatusMessage: NotRequired[str]
    RequestCompletionTime: NotRequired[datetime]

class CapacityAssignmentOutputTypeDef(TypedDict):
    WorkGroupNames: NotRequired[List[str]]

class CapacityAssignmentTypeDef(TypedDict):
    WorkGroupNames: NotRequired[Sequence[str]]

ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
        "CatalogName": NotRequired[str],
        "SchemaName": NotRequired[str],
        "TableName": NotRequired[str],
        "Label": NotRequired[str],
        "Precision": NotRequired[int],
        "Scale": NotRequired[int],
        "Nullable": NotRequired[ColumnNullableType],
        "CaseSensitive": NotRequired[bool],
    },
)
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
    },
)

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

DataCatalogTypeDef = TypedDict(
    "DataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "Status": NotRequired[DataCatalogStatusType],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "Error": NotRequired[str],
    },
)

class CreateNamedQueryInputTypeDef(TypedDict):
    Name: str
    Database: str
    QueryString: str
    Description: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    WorkGroup: NotRequired[str]

class CreateNotebookInputTypeDef(TypedDict):
    WorkGroup: str
    Name: str
    ClientRequestToken: NotRequired[str]

class CreatePreparedStatementInputTypeDef(TypedDict):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: NotRequired[str]

class CreatePresignedNotebookUrlRequestTypeDef(TypedDict):
    SessionId: str

class CustomerContentEncryptionConfigurationTypeDef(TypedDict):
    KmsKey: str

DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": NotRequired[str],
        "Type": NotRequired[DataCatalogTypeType],
        "Status": NotRequired[DataCatalogStatusType],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "Error": NotRequired[str],
    },
)

class DatabaseTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]

class DatumTypeDef(TypedDict):
    VarCharValue: NotRequired[str]

class DeleteCapacityReservationInputTypeDef(TypedDict):
    Name: str

class DeleteDataCatalogInputTypeDef(TypedDict):
    Name: str
    DeleteCatalogOnly: NotRequired[bool]

class DeleteNamedQueryInputTypeDef(TypedDict):
    NamedQueryId: str

class DeleteNotebookInputTypeDef(TypedDict):
    NotebookId: str

class DeletePreparedStatementInputTypeDef(TypedDict):
    StatementName: str
    WorkGroup: str

class DeleteWorkGroupInputTypeDef(TypedDict):
    WorkGroup: str
    RecursiveDeleteOption: NotRequired[bool]

class EncryptionConfigurationTypeDef(TypedDict):
    EncryptionOption: EncryptionOptionType
    KmsKey: NotRequired[str]

class EngineConfigurationOutputTypeDef(TypedDict):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: NotRequired[int]
    DefaultExecutorDpuSize: NotRequired[int]
    AdditionalConfigs: NotRequired[Dict[str, str]]
    SparkProperties: NotRequired[Dict[str, str]]

class EngineConfigurationTypeDef(TypedDict):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: NotRequired[int]
    DefaultExecutorDpuSize: NotRequired[int]
    AdditionalConfigs: NotRequired[Mapping[str, str]]
    SparkProperties: NotRequired[Mapping[str, str]]

class EngineVersionTypeDef(TypedDict):
    SelectedEngineVersion: NotRequired[str]
    EffectiveEngineVersion: NotRequired[str]

class ExecutorsSummaryTypeDef(TypedDict):
    ExecutorId: str
    ExecutorType: NotRequired[ExecutorTypeType]
    StartDateTime: NotRequired[int]
    TerminationDateTime: NotRequired[int]
    ExecutorState: NotRequired[ExecutorStateType]
    ExecutorSize: NotRequired[int]

class ExportNotebookInputTypeDef(TypedDict):
    NotebookId: str

NotebookMetadataTypeDef = TypedDict(
    "NotebookMetadataTypeDef",
    {
        "NotebookId": NotRequired[str],
        "Name": NotRequired[str],
        "WorkGroup": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Type": NotRequired[Literal["IPYNB"]],
        "LastModifiedTime": NotRequired[datetime],
    },
)

class FilterDefinitionTypeDef(TypedDict):
    Name: NotRequired[str]

class GetCalculationExecutionCodeRequestTypeDef(TypedDict):
    CalculationExecutionId: str

class GetCalculationExecutionRequestTypeDef(TypedDict):
    CalculationExecutionId: str

class GetCalculationExecutionStatusRequestTypeDef(TypedDict):
    CalculationExecutionId: str

class GetCapacityAssignmentConfigurationInputTypeDef(TypedDict):
    CapacityReservationName: str

class GetCapacityReservationInputTypeDef(TypedDict):
    Name: str

class GetDataCatalogInputTypeDef(TypedDict):
    Name: str
    WorkGroup: NotRequired[str]

class GetDatabaseInputTypeDef(TypedDict):
    CatalogName: str
    DatabaseName: str
    WorkGroup: NotRequired[str]

class GetNamedQueryInputTypeDef(TypedDict):
    NamedQueryId: str

class GetNotebookMetadataInputTypeDef(TypedDict):
    NotebookId: str

class GetPreparedStatementInputTypeDef(TypedDict):
    StatementName: str
    WorkGroup: str

class GetQueryExecutionInputTypeDef(TypedDict):
    QueryExecutionId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetQueryResultsInputTypeDef(TypedDict):
    QueryExecutionId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetQueryRuntimeStatisticsInputTypeDef(TypedDict):
    QueryExecutionId: str

class GetSessionRequestTypeDef(TypedDict):
    SessionId: str

class SessionStatisticsTypeDef(TypedDict):
    DpuExecutionInMillis: NotRequired[int]

class SessionStatusTypeDef(TypedDict):
    StartDateTime: NotRequired[datetime]
    LastModifiedDateTime: NotRequired[datetime]
    EndDateTime: NotRequired[datetime]
    IdleSinceDateTime: NotRequired[datetime]
    State: NotRequired[SessionStateType]
    StateChangeReason: NotRequired[str]

class GetSessionStatusRequestTypeDef(TypedDict):
    SessionId: str

class GetTableMetadataInputTypeDef(TypedDict):
    CatalogName: str
    DatabaseName: str
    TableName: str
    WorkGroup: NotRequired[str]

class GetWorkGroupInputTypeDef(TypedDict):
    WorkGroup: str

class IdentityCenterConfigurationTypeDef(TypedDict):
    EnableIdentityCenter: NotRequired[bool]
    IdentityCenterInstanceArn: NotRequired[str]

ImportNotebookInputTypeDef = TypedDict(
    "ImportNotebookInputTypeDef",
    {
        "WorkGroup": str,
        "Name": str,
        "Type": Literal["IPYNB"],
        "Payload": NotRequired[str],
        "NotebookS3LocationUri": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

class ListApplicationDPUSizesInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCalculationExecutionsRequestTypeDef(TypedDict):
    SessionId: str
    StateFilter: NotRequired[CalculationExecutionStateType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCapacityReservationsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataCatalogsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WorkGroup: NotRequired[str]

class ListDatabasesInputTypeDef(TypedDict):
    CatalogName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WorkGroup: NotRequired[str]

class ListEngineVersionsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListExecutorsRequestTypeDef(TypedDict):
    SessionId: str
    ExecutorStateFilter: NotRequired[ExecutorStateType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListNamedQueriesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WorkGroup: NotRequired[str]

class ListNotebookSessionsRequestTypeDef(TypedDict):
    NotebookId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NotebookSessionSummaryTypeDef(TypedDict):
    SessionId: NotRequired[str]
    CreationTime: NotRequired[datetime]

class ListPreparedStatementsInputTypeDef(TypedDict):
    WorkGroup: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PreparedStatementSummaryTypeDef(TypedDict):
    StatementName: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]

class ListQueryExecutionsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WorkGroup: NotRequired[str]

class ListSessionsRequestTypeDef(TypedDict):
    WorkGroup: str
    StateFilter: NotRequired[SessionStateType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTableMetadataInputTypeDef(TypedDict):
    CatalogName: str
    DatabaseName: str
    Expression: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WorkGroup: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceARN: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListWorkGroupsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class QueryExecutionContextTypeDef(TypedDict):
    Database: NotRequired[str]
    Catalog: NotRequired[str]

class ResultReuseInformationTypeDef(TypedDict):
    ReusedPreviousResult: bool

class QueryResultsS3AccessGrantsConfigurationTypeDef(TypedDict):
    EnableS3AccessGrants: bool
    AuthenticationType: Literal["DIRECTORY_IDENTITY"]
    CreateUserLevelPrefix: NotRequired[bool]

class QueryRuntimeStatisticsRowsTypeDef(TypedDict):
    InputRows: NotRequired[int]
    InputBytes: NotRequired[int]
    OutputBytes: NotRequired[int]
    OutputRows: NotRequired[int]

class QueryRuntimeStatisticsTimelineTypeDef(TypedDict):
    QueryQueueTimeInMillis: NotRequired[int]
    ServicePreProcessingTimeInMillis: NotRequired[int]
    QueryPlanningTimeInMillis: NotRequired[int]
    EngineExecutionTimeInMillis: NotRequired[int]
    ServiceProcessingTimeInMillis: NotRequired[int]
    TotalExecutionTimeInMillis: NotRequired[int]

class QueryStagePlanNodeTypeDef(TypedDict):
    Name: NotRequired[str]
    Identifier: NotRequired[str]
    Children: NotRequired[List[Dict[str, Any]]]
    RemoteSources: NotRequired[List[str]]

class ResultReuseByAgeConfigurationTypeDef(TypedDict):
    Enabled: bool
    MaxAgeInMinutes: NotRequired[int]

class StopCalculationExecutionRequestTypeDef(TypedDict):
    CalculationExecutionId: str

class StopQueryExecutionInputTypeDef(TypedDict):
    QueryExecutionId: str

class TerminateSessionRequestTypeDef(TypedDict):
    SessionId: str

class UntagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCapacityReservationInputTypeDef(TypedDict):
    TargetDpus: int
    Name: str

UpdateDataCatalogInputTypeDef = TypedDict(
    "UpdateDataCatalogInputTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

class UpdateNamedQueryInputTypeDef(TypedDict):
    NamedQueryId: str
    Name: str
    QueryString: str
    Description: NotRequired[str]

UpdateNotebookInputTypeDef = TypedDict(
    "UpdateNotebookInputTypeDef",
    {
        "NotebookId": str,
        "Payload": str,
        "Type": Literal["IPYNB"],
        "SessionId": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

class UpdateNotebookMetadataInputTypeDef(TypedDict):
    NotebookId: str
    Name: str
    ClientRequestToken: NotRequired[str]

class UpdatePreparedStatementInputTypeDef(TypedDict):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: NotRequired[str]

class QueryExecutionStatusTypeDef(TypedDict):
    State: NotRequired[QueryExecutionStateType]
    StateChangeReason: NotRequired[str]
    SubmissionDateTime: NotRequired[datetime]
    CompletionDateTime: NotRequired[datetime]
    AthenaError: NotRequired[AthenaErrorTypeDef]

class CreateNamedQueryOutputTypeDef(TypedDict):
    NamedQueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookOutputTypeDef(TypedDict):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedNotebookUrlResponseTypeDef(TypedDict):
    NotebookUrl: str
    AuthToken: str
    AuthTokenExpirationTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionCodeResponseTypeDef(TypedDict):
    CodeBlock: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamedQueryOutputTypeDef(TypedDict):
    NamedQuery: NamedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportNotebookOutputTypeDef(TypedDict):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationDPUSizesOutputTypeDef(TypedDict):
    ApplicationDPUSizes: List[ApplicationDPUSizesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListNamedQueriesOutputTypeDef(TypedDict):
    NamedQueryIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQueryExecutionsOutputTypeDef(TypedDict):
    QueryExecutionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartCalculationExecutionResponseTypeDef(TypedDict):
    CalculationExecutionId: str
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryExecutionOutputTypeDef(TypedDict):
    QueryExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionResponseTypeDef(TypedDict):
    SessionId: str
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopCalculationExecutionResponseTypeDef(TypedDict):
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSessionResponseTypeDef(TypedDict):
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetNamedQueryOutputTypeDef(TypedDict):
    NamedQueries: List[NamedQueryTypeDef]
    UnprocessedNamedQueryIds: List[UnprocessedNamedQueryIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPreparedStatementOutputTypeDef(TypedDict):
    PreparedStatement: PreparedStatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetPreparedStatementOutputTypeDef(TypedDict):
    PreparedStatements: List[PreparedStatementTypeDef]
    UnprocessedPreparedStatementNames: List[UnprocessedPreparedStatementNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartCalculationExecutionRequestTypeDef(TypedDict):
    SessionId: str
    Description: NotRequired[str]
    CalculationConfiguration: NotRequired[CalculationConfigurationTypeDef]
    CodeBlock: NotRequired[str]
    ClientRequestToken: NotRequired[str]

class CalculationSummaryTypeDef(TypedDict):
    CalculationExecutionId: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[CalculationStatusTypeDef]

class GetCalculationExecutionResponseTypeDef(TypedDict):
    CalculationExecutionId: str
    SessionId: str
    Description: str
    WorkingDirectory: str
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    Result: CalculationResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionStatusResponseTypeDef(TypedDict):
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CapacityReservationTypeDef(TypedDict):
    Name: str
    Status: CapacityReservationStatusType
    TargetDpus: int
    AllocatedDpus: int
    CreationTime: datetime
    LastAllocation: NotRequired[CapacityAllocationTypeDef]
    LastSuccessfulAllocationTime: NotRequired[datetime]

class CapacityAssignmentConfigurationTypeDef(TypedDict):
    CapacityReservationName: NotRequired[str]
    CapacityAssignments: NotRequired[List[CapacityAssignmentOutputTypeDef]]

CapacityAssignmentUnionTypeDef = Union[CapacityAssignmentTypeDef, CapacityAssignmentOutputTypeDef]

class ResultSetMetadataTypeDef(TypedDict):
    ColumnInfo: NotRequired[List[ColumnInfoTypeDef]]

class TableMetadataTypeDef(TypedDict):
    Name: str
    CreateTime: NotRequired[datetime]
    LastAccessTime: NotRequired[datetime]
    TableType: NotRequired[str]
    Columns: NotRequired[List[ColumnTypeDef]]
    PartitionKeys: NotRequired[List[ColumnTypeDef]]
    Parameters: NotRequired[Dict[str, str]]

class CreateCapacityReservationInputTypeDef(TypedDict):
    TargetDpus: int
    Name: str
    Tags: NotRequired[Sequence[TagTypeDef]]

CreateDataCatalogInputTypeDef = TypedDict(
    "CreateDataCatalogInputTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateDataCatalogOutputTypeDef(TypedDict):
    DataCatalog: DataCatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataCatalogOutputTypeDef(TypedDict):
    DataCatalog: DataCatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataCatalogOutputTypeDef(TypedDict):
    DataCatalog: DataCatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataCatalogsOutputTypeDef(TypedDict):
    DataCatalogsSummary: List[DataCatalogSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDatabaseOutputTypeDef(TypedDict):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesOutputTypeDef(TypedDict):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RowTypeDef(TypedDict):
    Data: NotRequired[List[DatumTypeDef]]

class ResultConfigurationTypeDef(TypedDict):
    OutputLocation: NotRequired[str]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    ExpectedBucketOwner: NotRequired[str]
    AclConfiguration: NotRequired[AclConfigurationTypeDef]

class ResultConfigurationUpdatesTypeDef(TypedDict):
    OutputLocation: NotRequired[str]
    RemoveOutputLocation: NotRequired[bool]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    RemoveEncryptionConfiguration: NotRequired[bool]
    ExpectedBucketOwner: NotRequired[str]
    RemoveExpectedBucketOwner: NotRequired[bool]
    AclConfiguration: NotRequired[AclConfigurationTypeDef]
    RemoveAclConfiguration: NotRequired[bool]

class SessionConfigurationTypeDef(TypedDict):
    ExecutionRole: NotRequired[str]
    WorkingDirectory: NotRequired[str]
    IdleTimeoutSeconds: NotRequired[int]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

EngineConfigurationUnionTypeDef = Union[
    EngineConfigurationTypeDef, EngineConfigurationOutputTypeDef
]

class ListEngineVersionsOutputTypeDef(TypedDict):
    EngineVersions: List[EngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class WorkGroupSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    State: NotRequired[WorkGroupStateType]
    Description: NotRequired[str]
    CreationTime: NotRequired[datetime]
    EngineVersion: NotRequired[EngineVersionTypeDef]
    IdentityCenterApplicationArn: NotRequired[str]

class ListExecutorsResponseTypeDef(TypedDict):
    SessionId: str
    ExecutorsSummary: List[ExecutorsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExportNotebookOutputTypeDef(TypedDict):
    NotebookMetadata: NotebookMetadataTypeDef
    Payload: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotebookMetadataOutputTypeDef(TypedDict):
    NotebookMetadata: NotebookMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotebookMetadataOutputTypeDef(TypedDict):
    NotebookMetadataList: List[NotebookMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListNotebookMetadataInputTypeDef(TypedDict):
    WorkGroup: str
    Filters: NotRequired[FilterDefinitionTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetQueryResultsInputPaginateTypeDef(TypedDict):
    QueryExecutionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataCatalogsInputPaginateTypeDef(TypedDict):
    WorkGroup: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatabasesInputPaginateTypeDef(TypedDict):
    CatalogName: str
    WorkGroup: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNamedQueriesInputPaginateTypeDef(TypedDict):
    WorkGroup: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueryExecutionsInputPaginateTypeDef(TypedDict):
    WorkGroup: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTableMetadataInputPaginateTypeDef(TypedDict):
    CatalogName: str
    DatabaseName: str
    Expression: NotRequired[str]
    WorkGroup: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    ResourceARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSessionStatusResponseTypeDef(TypedDict):
    SessionId: str
    Status: SessionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SessionSummaryTypeDef(TypedDict):
    SessionId: NotRequired[str]
    Description: NotRequired[str]
    EngineVersion: NotRequired[EngineVersionTypeDef]
    NotebookVersion: NotRequired[str]
    Status: NotRequired[SessionStatusTypeDef]

class ListNotebookSessionsResponseTypeDef(TypedDict):
    NotebookSessionsList: List[NotebookSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPreparedStatementsOutputTypeDef(TypedDict):
    PreparedStatements: List[PreparedStatementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class QueryExecutionStatisticsTypeDef(TypedDict):
    EngineExecutionTimeInMillis: NotRequired[int]
    DataScannedInBytes: NotRequired[int]
    DataManifestLocation: NotRequired[str]
    TotalExecutionTimeInMillis: NotRequired[int]
    QueryQueueTimeInMillis: NotRequired[int]
    ServicePreProcessingTimeInMillis: NotRequired[int]
    QueryPlanningTimeInMillis: NotRequired[int]
    ServiceProcessingTimeInMillis: NotRequired[int]
    ResultReuseInformation: NotRequired[ResultReuseInformationTypeDef]

class QueryStageTypeDef(TypedDict):
    StageId: NotRequired[int]
    State: NotRequired[str]
    OutputBytes: NotRequired[int]
    OutputRows: NotRequired[int]
    InputBytes: NotRequired[int]
    InputRows: NotRequired[int]
    ExecutionTime: NotRequired[int]
    QueryStagePlan: NotRequired[QueryStagePlanNodeTypeDef]
    SubStages: NotRequired[List[Dict[str, Any]]]

class ResultReuseConfigurationTypeDef(TypedDict):
    ResultReuseByAgeConfiguration: NotRequired[ResultReuseByAgeConfigurationTypeDef]

class ListCalculationExecutionsResponseTypeDef(TypedDict):
    Calculations: List[CalculationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCapacityReservationOutputTypeDef(TypedDict):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapacityReservationsOutputTypeDef(TypedDict):
    CapacityReservations: List[CapacityReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCapacityAssignmentConfigurationOutputTypeDef(TypedDict):
    CapacityAssignmentConfiguration: CapacityAssignmentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCapacityAssignmentConfigurationInputTypeDef(TypedDict):
    CapacityReservationName: str
    CapacityAssignments: Sequence[CapacityAssignmentUnionTypeDef]

class GetTableMetadataOutputTypeDef(TypedDict):
    TableMetadata: TableMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableMetadataOutputTypeDef(TypedDict):
    TableMetadataList: List[TableMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResultSetTypeDef(TypedDict):
    Rows: NotRequired[List[RowTypeDef]]
    ResultSetMetadata: NotRequired[ResultSetMetadataTypeDef]

class WorkGroupConfigurationTypeDef(TypedDict):
    ResultConfiguration: NotRequired[ResultConfigurationTypeDef]
    EnforceWorkGroupConfiguration: NotRequired[bool]
    PublishCloudWatchMetricsEnabled: NotRequired[bool]
    BytesScannedCutoffPerQuery: NotRequired[int]
    RequesterPaysEnabled: NotRequired[bool]
    EngineVersion: NotRequired[EngineVersionTypeDef]
    AdditionalConfiguration: NotRequired[str]
    ExecutionRole: NotRequired[str]
    CustomerContentEncryptionConfiguration: NotRequired[
        CustomerContentEncryptionConfigurationTypeDef
    ]
    EnableMinimumEncryptionConfiguration: NotRequired[bool]
    IdentityCenterConfiguration: NotRequired[IdentityCenterConfigurationTypeDef]
    QueryResultsS3AccessGrantsConfiguration: NotRequired[
        QueryResultsS3AccessGrantsConfigurationTypeDef
    ]

class WorkGroupConfigurationUpdatesTypeDef(TypedDict):
    EnforceWorkGroupConfiguration: NotRequired[bool]
    ResultConfigurationUpdates: NotRequired[ResultConfigurationUpdatesTypeDef]
    PublishCloudWatchMetricsEnabled: NotRequired[bool]
    BytesScannedCutoffPerQuery: NotRequired[int]
    RemoveBytesScannedCutoffPerQuery: NotRequired[bool]
    RequesterPaysEnabled: NotRequired[bool]
    EngineVersion: NotRequired[EngineVersionTypeDef]
    RemoveCustomerContentEncryptionConfiguration: NotRequired[bool]
    AdditionalConfiguration: NotRequired[str]
    ExecutionRole: NotRequired[str]
    CustomerContentEncryptionConfiguration: NotRequired[
        CustomerContentEncryptionConfigurationTypeDef
    ]
    EnableMinimumEncryptionConfiguration: NotRequired[bool]
    QueryResultsS3AccessGrantsConfiguration: NotRequired[
        QueryResultsS3AccessGrantsConfigurationTypeDef
    ]

class GetSessionResponseTypeDef(TypedDict):
    SessionId: str
    Description: str
    WorkGroup: str
    EngineVersion: str
    EngineConfiguration: EngineConfigurationOutputTypeDef
    NotebookVersion: str
    SessionConfiguration: SessionConfigurationTypeDef
    Status: SessionStatusTypeDef
    Statistics: SessionStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionRequestTypeDef(TypedDict):
    WorkGroup: str
    EngineConfiguration: EngineConfigurationUnionTypeDef
    Description: NotRequired[str]
    NotebookVersion: NotRequired[str]
    SessionIdleTimeoutInMinutes: NotRequired[int]
    ClientRequestToken: NotRequired[str]

class ListWorkGroupsOutputTypeDef(TypedDict):
    WorkGroups: List[WorkGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSessionsResponseTypeDef(TypedDict):
    Sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class QueryRuntimeStatisticsTypeDef(TypedDict):
    Timeline: NotRequired[QueryRuntimeStatisticsTimelineTypeDef]
    Rows: NotRequired[QueryRuntimeStatisticsRowsTypeDef]
    OutputStage: NotRequired[QueryStageTypeDef]

class QueryExecutionTypeDef(TypedDict):
    QueryExecutionId: NotRequired[str]
    Query: NotRequired[str]
    StatementType: NotRequired[StatementTypeType]
    ResultConfiguration: NotRequired[ResultConfigurationTypeDef]
    ResultReuseConfiguration: NotRequired[ResultReuseConfigurationTypeDef]
    QueryExecutionContext: NotRequired[QueryExecutionContextTypeDef]
    Status: NotRequired[QueryExecutionStatusTypeDef]
    Statistics: NotRequired[QueryExecutionStatisticsTypeDef]
    WorkGroup: NotRequired[str]
    EngineVersion: NotRequired[EngineVersionTypeDef]
    ExecutionParameters: NotRequired[List[str]]
    SubstatementType: NotRequired[str]
    QueryResultsS3AccessGrantsConfiguration: NotRequired[
        QueryResultsS3AccessGrantsConfigurationTypeDef
    ]

class StartQueryExecutionInputTypeDef(TypedDict):
    QueryString: str
    ClientRequestToken: NotRequired[str]
    QueryExecutionContext: NotRequired[QueryExecutionContextTypeDef]
    ResultConfiguration: NotRequired[ResultConfigurationTypeDef]
    WorkGroup: NotRequired[str]
    ExecutionParameters: NotRequired[Sequence[str]]
    ResultReuseConfiguration: NotRequired[ResultReuseConfigurationTypeDef]

class GetQueryResultsOutputTypeDef(TypedDict):
    UpdateCount: int
    ResultSet: ResultSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateWorkGroupInputTypeDef(TypedDict):
    Name: str
    Configuration: NotRequired[WorkGroupConfigurationTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class WorkGroupTypeDef(TypedDict):
    Name: str
    State: NotRequired[WorkGroupStateType]
    Configuration: NotRequired[WorkGroupConfigurationTypeDef]
    Description: NotRequired[str]
    CreationTime: NotRequired[datetime]
    IdentityCenterApplicationArn: NotRequired[str]

class UpdateWorkGroupInputTypeDef(TypedDict):
    WorkGroup: str
    Description: NotRequired[str]
    ConfigurationUpdates: NotRequired[WorkGroupConfigurationUpdatesTypeDef]
    State: NotRequired[WorkGroupStateType]

class GetQueryRuntimeStatisticsOutputTypeDef(TypedDict):
    QueryRuntimeStatistics: QueryRuntimeStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetQueryExecutionOutputTypeDef(TypedDict):
    QueryExecutions: List[QueryExecutionTypeDef]
    UnprocessedQueryExecutionIds: List[UnprocessedQueryExecutionIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryExecutionOutputTypeDef(TypedDict):
    QueryExecution: QueryExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkGroupOutputTypeDef(TypedDict):
    WorkGroup: WorkGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
