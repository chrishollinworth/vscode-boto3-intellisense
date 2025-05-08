"""
Type annotations for databrew service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import AllowedStatisticsOutputTypeDef

    data: AllowedStatisticsOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AnalyticsModeType,
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
    ThresholdTypeType,
    ThresholdUnitType,
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
    "AllowedStatisticsOutputTypeDef",
    "AllowedStatisticsTypeDef",
    "BatchDeleteRecipeVersionRequestTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "ColumnSelectorTypeDef",
    "ColumnStatisticsConfigurationOutputTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobRequestTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobRequestTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeRequestTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateRulesetRequestTypeDef",
    "CreateRulesetResponseTypeDef",
    "CreateScheduleRequestTypeDef",
    "CreateScheduleResponseTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DataCatalogOutputTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseOutputTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "DatasetParameterOutputTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionRequestTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteRulesetRequestTypeDef",
    "DeleteRulesetResponseTypeDef",
    "DeleteScheduleRequestTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeRecipeRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeRulesetRequestTypeDef",
    "DescribeRulesetResponseTypeDef",
    "DescribeScheduleRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "EntityDetectorConfigurationOutputTypeDef",
    "EntityDetectorConfigurationTypeDef",
    "ExcelOptionsOutputTypeDef",
    "ExcelOptionsTypeDef",
    "ExtraTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionOutputTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsOutputTypeDef",
    "FormatOptionsTypeDef",
    "FormatOptionsUnionTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "ListDatasetsRequestPaginateTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListJobRunsRequestPaginateTypeDef",
    "ListJobRunsRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListProjectsRequestPaginateTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListRecipeVersionsRequestPaginateTypeDef",
    "ListRecipeVersionsRequestTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesRequestPaginateTypeDef",
    "ListRecipesRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListRulesetsRequestPaginateTypeDef",
    "ListRulesetsRequestTypeDef",
    "ListRulesetsResponseTypeDef",
    "ListSchedulesRequestPaginateTypeDef",
    "ListSchedulesRequestTypeDef",
    "ListSchedulesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetadataTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathOptionsOutputTypeDef",
    "PathOptionsTypeDef",
    "PathOptionsUnionTypeDef",
    "ProfileConfigurationOutputTypeDef",
    "ProfileConfigurationTypeDef",
    "ProfileConfigurationUnionTypeDef",
    "ProjectTypeDef",
    "PublishRecipeRequestTypeDef",
    "PublishRecipeResponseTypeDef",
    "RecipeActionOutputTypeDef",
    "RecipeActionTypeDef",
    "RecipeActionUnionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepOutputTypeDef",
    "RecipeStepTypeDef",
    "RecipeStepUnionTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "RulesetItemTypeDef",
    "S3LocationTypeDef",
    "S3TableOutputOptionsTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "SendProjectSessionActionRequestTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionRequestTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StatisticOverrideOutputTypeDef",
    "StatisticOverrideTypeDef",
    "StatisticsConfigurationOutputTypeDef",
    "StatisticsConfigurationTypeDef",
    "StopJobRunRequestTypeDef",
    "StopJobRunResponseTypeDef",
    "TagResourceRequestTypeDef",
    "ThresholdTypeDef",
    "UnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobRequestTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobRequestTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeRequestTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateRulesetRequestTypeDef",
    "UpdateRulesetResponseTypeDef",
    "UpdateScheduleRequestTypeDef",
    "UpdateScheduleResponseTypeDef",
    "ValidationConfigurationTypeDef",
    "ViewFrameTypeDef",
)

class AllowedStatisticsOutputTypeDef(TypedDict):
    Statistics: List[str]

class AllowedStatisticsTypeDef(TypedDict):
    Statistics: Sequence[str]

class BatchDeleteRecipeVersionRequestTypeDef(TypedDict):
    Name: str
    RecipeVersions: Sequence[str]

class RecipeVersionErrorDetailTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    RecipeVersion: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ColumnSelectorTypeDef(TypedDict):
    Regex: NotRequired[str]
    Name: NotRequired[str]

class ConditionExpressionTypeDef(TypedDict):
    Condition: str
    TargetColumn: str
    Value: NotRequired[str]

class JobSampleTypeDef(TypedDict):
    Mode: NotRequired[SampleModeType]
    Size: NotRequired[int]

class S3LocationTypeDef(TypedDict):
    Bucket: str
    Key: NotRequired[str]
    BucketOwner: NotRequired[str]

class ValidationConfigurationTypeDef(TypedDict):
    RulesetArn: str
    ValidationMode: NotRequired[Literal["CHECK_ALL"]]

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "Type": SampleTypeType,
        "Size": NotRequired[int],
    },
)

class RecipeReferenceTypeDef(TypedDict):
    Name: str
    RecipeVersion: NotRequired[str]

class CreateScheduleRequestTypeDef(TypedDict):
    CronExpression: str
    Name: str
    JobNames: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class CsvOptionsTypeDef(TypedDict):
    Delimiter: NotRequired[str]
    HeaderRow: NotRequired[bool]

class CsvOutputOptionsTypeDef(TypedDict):
    Delimiter: NotRequired[str]

class DatetimeOptionsTypeDef(TypedDict):
    Format: str
    TimezoneOffset: NotRequired[str]
    LocaleCode: NotRequired[str]

class FilterExpressionOutputTypeDef(TypedDict):
    Expression: str
    ValuesMap: Dict[str, str]

class FilterExpressionTypeDef(TypedDict):
    Expression: str
    ValuesMap: Mapping[str, str]

class DeleteDatasetRequestTypeDef(TypedDict):
    Name: str

class DeleteJobRequestTypeDef(TypedDict):
    Name: str

class DeleteProjectRequestTypeDef(TypedDict):
    Name: str

class DeleteRecipeVersionRequestTypeDef(TypedDict):
    Name: str
    RecipeVersion: str

class DeleteRulesetRequestTypeDef(TypedDict):
    Name: str

class DeleteScheduleRequestTypeDef(TypedDict):
    Name: str

class DescribeDatasetRequestTypeDef(TypedDict):
    Name: str

class DescribeJobRequestTypeDef(TypedDict):
    Name: str

class DescribeJobRunRequestTypeDef(TypedDict):
    Name: str
    RunId: str

class DescribeProjectRequestTypeDef(TypedDict):
    Name: str

class DescribeRecipeRequestTypeDef(TypedDict):
    Name: str
    RecipeVersion: NotRequired[str]

class DescribeRulesetRequestTypeDef(TypedDict):
    Name: str

class DescribeScheduleRequestTypeDef(TypedDict):
    Name: str

class ExcelOptionsOutputTypeDef(TypedDict):
    SheetNames: NotRequired[List[str]]
    SheetIndexes: NotRequired[List[int]]
    HeaderRow: NotRequired[bool]

class ExcelOptionsTypeDef(TypedDict):
    SheetNames: NotRequired[Sequence[str]]
    SheetIndexes: NotRequired[Sequence[int]]
    HeaderRow: NotRequired[bool]

class FilesLimitTypeDef(TypedDict):
    MaxFiles: int
    OrderedBy: NotRequired[Literal["LAST_MODIFIED_DATE"]]
    Order: NotRequired[OrderType]

class JsonOptionsTypeDef(TypedDict):
    MultiLine: NotRequired[bool]

class MetadataTypeDef(TypedDict):
    SourceArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDatasetsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListJobRunsRequestTypeDef(TypedDict):
    Name: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListJobsRequestTypeDef(TypedDict):
    DatasetName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ProjectName: NotRequired[str]

class ListProjectsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRecipeVersionsRequestTypeDef(TypedDict):
    Name: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRecipesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    RecipeVersion: NotRequired[str]

class ListRulesetsRequestTypeDef(TypedDict):
    TargetArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RulesetItemTypeDef(TypedDict):
    Name: str
    TargetArn: str
    AccountId: NotRequired[str]
    CreatedBy: NotRequired[str]
    CreateDate: NotRequired[datetime]
    Description: NotRequired[str]
    LastModifiedBy: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    ResourceArn: NotRequired[str]
    RuleCount: NotRequired[int]
    Tags: NotRequired[Dict[str, str]]

class ListSchedulesRequestTypeDef(TypedDict):
    JobName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ScheduleTypeDef(TypedDict):
    Name: str
    AccountId: NotRequired[str]
    CreatedBy: NotRequired[str]
    CreateDate: NotRequired[datetime]
    JobNames: NotRequired[List[str]]
    LastModifiedBy: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    ResourceArn: NotRequired[str]
    CronExpression: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PublishRecipeRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]

class RecipeActionOutputTypeDef(TypedDict):
    Operation: str
    Parameters: NotRequired[Dict[str, str]]

class RecipeActionTypeDef(TypedDict):
    Operation: str
    Parameters: NotRequired[Mapping[str, str]]

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": float,
        "Type": NotRequired[ThresholdTypeType],
        "Unit": NotRequired[ThresholdUnitType],
    },
)

class ViewFrameTypeDef(TypedDict):
    StartColumnIndex: int
    ColumnRange: NotRequired[int]
    HiddenColumns: NotRequired[Sequence[str]]
    StartRowIndex: NotRequired[int]
    RowRange: NotRequired[int]
    Analytics: NotRequired[AnalyticsModeType]

class StartJobRunRequestTypeDef(TypedDict):
    Name: str

class StartProjectSessionRequestTypeDef(TypedDict):
    Name: str
    AssumeControl: NotRequired[bool]

class StatisticOverrideOutputTypeDef(TypedDict):
    Statistic: str
    Parameters: Dict[str, str]

class StatisticOverrideTypeDef(TypedDict):
    Statistic: str
    Parameters: Mapping[str, str]

class StopJobRunRequestTypeDef(TypedDict):
    Name: str
    RunId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateScheduleRequestTypeDef(TypedDict):
    CronExpression: str
    Name: str
    JobNames: NotRequired[Sequence[str]]

class EntityDetectorConfigurationOutputTypeDef(TypedDict):
    EntityTypes: List[str]
    AllowedStatistics: NotRequired[List[AllowedStatisticsOutputTypeDef]]

class EntityDetectorConfigurationTypeDef(TypedDict):
    EntityTypes: Sequence[str]
    AllowedStatistics: NotRequired[Sequence[AllowedStatisticsTypeDef]]

class BatchDeleteRecipeVersionResponseTypeDef(TypedDict):
    Name: str
    Errors: List[RecipeVersionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecipeJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecipeResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRulesetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduleResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRecipeVersionResponseTypeDef(TypedDict):
    Name: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRulesetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScheduleResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduleResponseTypeDef(TypedDict):
    CreateDate: datetime
    CreatedBy: str
    JobNames: List[str]
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    CronExpression: str
    Tags: Dict[str, str]
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishRecipeResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendProjectSessionActionResponseTypeDef(TypedDict):
    Result: str
    Name: str
    ActionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartProjectSessionResponseTypeDef(TypedDict):
    Name: str
    ClientSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopJobRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResponseTypeDef(TypedDict):
    LastModifiedDate: datetime
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecipeJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecipeResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRulesetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduleResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataCatalogInputDefinitionTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    TempDirectory: NotRequired[S3LocationTypeDef]

class DatabaseInputDefinitionTypeDef(TypedDict):
    GlueConnectionName: str
    DatabaseTableName: NotRequired[str]
    TempDirectory: NotRequired[S3LocationTypeDef]
    QueryString: NotRequired[str]

class DatabaseTableOutputOptionsTypeDef(TypedDict):
    TableName: str
    TempDirectory: NotRequired[S3LocationTypeDef]

class S3TableOutputOptionsTypeDef(TypedDict):
    Location: S3LocationTypeDef

class CreateProjectRequestTypeDef(TypedDict):
    DatasetName: str
    Name: str
    RecipeName: str
    RoleArn: str
    Sample: NotRequired[SampleTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class DescribeProjectResponseTypeDef(TypedDict):
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    LastModifiedDate: datetime
    LastModifiedBy: str
    Name: str
    RecipeName: str
    ResourceArn: str
    Sample: SampleTypeDef
    RoleArn: str
    Tags: Dict[str, str]
    SessionStatus: SessionStatusType
    OpenedBy: str
    OpenDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectTypeDef(TypedDict):
    Name: str
    RecipeName: str
    AccountId: NotRequired[str]
    CreateDate: NotRequired[datetime]
    CreatedBy: NotRequired[str]
    DatasetName: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    LastModifiedBy: NotRequired[str]
    ResourceArn: NotRequired[str]
    Sample: NotRequired[SampleTypeDef]
    Tags: NotRequired[Dict[str, str]]
    RoleArn: NotRequired[str]
    OpenedBy: NotRequired[str]
    OpenDate: NotRequired[datetime]

class UpdateProjectRequestTypeDef(TypedDict):
    RoleArn: str
    Name: str
    Sample: NotRequired[SampleTypeDef]

class OutputFormatOptionsTypeDef(TypedDict):
    Csv: NotRequired[CsvOutputOptionsTypeDef]

DatasetParameterOutputTypeDef = TypedDict(
    "DatasetParameterOutputTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionOutputTypeDef],
    },
)
DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionTypeDef],
    },
)

class FormatOptionsOutputTypeDef(TypedDict):
    Json: NotRequired[JsonOptionsTypeDef]
    Excel: NotRequired[ExcelOptionsOutputTypeDef]
    Csv: NotRequired[CsvOptionsTypeDef]

class FormatOptionsTypeDef(TypedDict):
    Json: NotRequired[JsonOptionsTypeDef]
    Excel: NotRequired[ExcelOptionsTypeDef]
    Csv: NotRequired[CsvOptionsTypeDef]

class ListDatasetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunsRequestPaginateTypeDef(TypedDict):
    Name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestPaginateTypeDef(TypedDict):
    DatasetName: NotRequired[str]
    ProjectName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecipeVersionsRequestPaginateTypeDef(TypedDict):
    Name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecipesRequestPaginateTypeDef(TypedDict):
    RecipeVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesetsRequestPaginateTypeDef(TypedDict):
    TargetArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchedulesRequestPaginateTypeDef(TypedDict):
    JobName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesetsResponseTypeDef(TypedDict):
    Rulesets: List[RulesetItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchedulesResponseTypeDef(TypedDict):
    Schedules: List[ScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RecipeStepOutputTypeDef(TypedDict):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: NotRequired[List[ConditionExpressionTypeDef]]

RecipeActionUnionTypeDef = Union[RecipeActionTypeDef, RecipeActionOutputTypeDef]

class RuleOutputTypeDef(TypedDict):
    Name: str
    CheckExpression: str
    Disabled: NotRequired[bool]
    SubstitutionMap: NotRequired[Dict[str, str]]
    Threshold: NotRequired[ThresholdTypeDef]
    ColumnSelectors: NotRequired[List[ColumnSelectorTypeDef]]

class RuleTypeDef(TypedDict):
    Name: str
    CheckExpression: str
    Disabled: NotRequired[bool]
    SubstitutionMap: NotRequired[Mapping[str, str]]
    Threshold: NotRequired[ThresholdTypeDef]
    ColumnSelectors: NotRequired[Sequence[ColumnSelectorTypeDef]]

class StatisticsConfigurationOutputTypeDef(TypedDict):
    IncludedStatistics: NotRequired[List[str]]
    Overrides: NotRequired[List[StatisticOverrideOutputTypeDef]]

class StatisticsConfigurationTypeDef(TypedDict):
    IncludedStatistics: NotRequired[Sequence[str]]
    Overrides: NotRequired[Sequence[StatisticOverrideTypeDef]]

class InputTypeDef(TypedDict):
    S3InputDefinition: NotRequired[S3LocationTypeDef]
    DataCatalogInputDefinition: NotRequired[DataCatalogInputDefinitionTypeDef]
    DatabaseInputDefinition: NotRequired[DatabaseInputDefinitionTypeDef]
    Metadata: NotRequired[MetadataTypeDef]

class DatabaseOutputTypeDef(TypedDict):
    GlueConnectionName: str
    DatabaseOptions: DatabaseTableOutputOptionsTypeDef
    DatabaseOutputMode: NotRequired[Literal["NEW_TABLE"]]

class DataCatalogOutputTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    S3Options: NotRequired[S3TableOutputOptionsTypeDef]
    DatabaseOptions: NotRequired[DatabaseTableOutputOptionsTypeDef]
    Overwrite: NotRequired[bool]

class ListProjectsResponseTypeDef(TypedDict):
    Projects: List[ProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExtraTypeDef(TypedDict):
    Location: S3LocationTypeDef
    CompressionFormat: NotRequired[CompressionFormatType]
    Format: NotRequired[OutputFormatType]
    PartitionColumns: NotRequired[List[str]]
    Overwrite: NotRequired[bool]
    FormatOptions: NotRequired[OutputFormatOptionsTypeDef]
    MaxOutputFiles: NotRequired[int]

class OutputTypeDef(TypedDict):
    Location: S3LocationTypeDef
    CompressionFormat: NotRequired[CompressionFormatType]
    Format: NotRequired[OutputFormatType]
    PartitionColumns: NotRequired[Sequence[str]]
    Overwrite: NotRequired[bool]
    FormatOptions: NotRequired[OutputFormatOptionsTypeDef]
    MaxOutputFiles: NotRequired[int]

class PathOptionsOutputTypeDef(TypedDict):
    LastModifiedDateCondition: NotRequired[FilterExpressionOutputTypeDef]
    FilesLimit: NotRequired[FilesLimitTypeDef]
    Parameters: NotRequired[Dict[str, DatasetParameterOutputTypeDef]]

class PathOptionsTypeDef(TypedDict):
    LastModifiedDateCondition: NotRequired[FilterExpressionTypeDef]
    FilesLimit: NotRequired[FilesLimitTypeDef]
    Parameters: NotRequired[Mapping[str, DatasetParameterTypeDef]]

FormatOptionsUnionTypeDef = Union[FormatOptionsTypeDef, FormatOptionsOutputTypeDef]

class DescribeRecipeResponseTypeDef(TypedDict):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    Name: str
    Steps: List[RecipeStepOutputTypeDef]
    Tags: Dict[str, str]
    ResourceArn: str
    RecipeVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipeTypeDef(TypedDict):
    Name: str
    CreatedBy: NotRequired[str]
    CreateDate: NotRequired[datetime]
    LastModifiedBy: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    ProjectName: NotRequired[str]
    PublishedBy: NotRequired[str]
    PublishedDate: NotRequired[datetime]
    Description: NotRequired[str]
    ResourceArn: NotRequired[str]
    Steps: NotRequired[List[RecipeStepOutputTypeDef]]
    Tags: NotRequired[Dict[str, str]]
    RecipeVersion: NotRequired[str]

class RecipeStepTypeDef(TypedDict):
    Action: RecipeActionUnionTypeDef
    ConditionExpressions: NotRequired[Sequence[ConditionExpressionTypeDef]]

class DescribeRulesetResponseTypeDef(TypedDict):
    Name: str
    Description: str
    TargetArn: str
    Rules: List[RuleOutputTypeDef]
    CreateDate: datetime
    CreatedBy: str
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class ColumnStatisticsConfigurationOutputTypeDef(TypedDict):
    Statistics: StatisticsConfigurationOutputTypeDef
    Selectors: NotRequired[List[ColumnSelectorTypeDef]]

class ColumnStatisticsConfigurationTypeDef(TypedDict):
    Statistics: StatisticsConfigurationTypeDef
    Selectors: NotRequired[Sequence[ColumnSelectorTypeDef]]

class JobRunTypeDef(TypedDict):
    Attempt: NotRequired[int]
    CompletedOn: NotRequired[datetime]
    DatasetName: NotRequired[str]
    ErrorMessage: NotRequired[str]
    ExecutionTime: NotRequired[int]
    JobName: NotRequired[str]
    RunId: NotRequired[str]
    State: NotRequired[JobRunStateType]
    LogSubscription: NotRequired[LogSubscriptionType]
    LogGroupName: NotRequired[str]
    Outputs: NotRequired[List[ExtraTypeDef]]
    DataCatalogOutputs: NotRequired[List[DataCatalogOutputTypeDef]]
    DatabaseOutputs: NotRequired[List[DatabaseOutputTypeDef]]
    RecipeReference: NotRequired[RecipeReferenceTypeDef]
    StartedBy: NotRequired[str]
    StartedOn: NotRequired[datetime]
    JobSample: NotRequired[JobSampleTypeDef]
    ValidationConfigurations: NotRequired[List[ValidationConfigurationTypeDef]]

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "Type": NotRequired[JobTypeType],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[List[ExtraTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Timeout": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
UnionTypeDef = Union[OutputTypeDef, ExtraTypeDef]

class DatasetTypeDef(TypedDict):
    Name: str
    Input: InputTypeDef
    AccountId: NotRequired[str]
    CreatedBy: NotRequired[str]
    CreateDate: NotRequired[datetime]
    Format: NotRequired[InputFormatType]
    FormatOptions: NotRequired[FormatOptionsOutputTypeDef]
    LastModifiedDate: NotRequired[datetime]
    LastModifiedBy: NotRequired[str]
    Source: NotRequired[SourceType]
    PathOptions: NotRequired[PathOptionsOutputTypeDef]
    Tags: NotRequired[Dict[str, str]]
    ResourceArn: NotRequired[str]

class DescribeDatasetResponseTypeDef(TypedDict):
    CreatedBy: str
    CreateDate: datetime
    Name: str
    Format: InputFormatType
    FormatOptions: FormatOptionsOutputTypeDef
    Input: InputTypeDef
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: SourceType
    PathOptions: PathOptionsOutputTypeDef
    Tags: Dict[str, str]
    ResourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

PathOptionsUnionTypeDef = Union[PathOptionsTypeDef, PathOptionsOutputTypeDef]

class ListRecipeVersionsResponseTypeDef(TypedDict):
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRecipesResponseTypeDef(TypedDict):
    Recipes: List[RecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RecipeStepUnionTypeDef = Union[RecipeStepTypeDef, RecipeStepOutputTypeDef]

class CreateRulesetRequestTypeDef(TypedDict):
    Name: str
    TargetArn: str
    Rules: Sequence[RuleUnionTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateRulesetRequestTypeDef(TypedDict):
    Name: str
    Rules: Sequence[RuleUnionTypeDef]
    Description: NotRequired[str]

class ProfileConfigurationOutputTypeDef(TypedDict):
    DatasetStatisticsConfiguration: NotRequired[StatisticsConfigurationOutputTypeDef]
    ProfileColumns: NotRequired[List[ColumnSelectorTypeDef]]
    ColumnStatisticsConfigurations: NotRequired[List[ColumnStatisticsConfigurationOutputTypeDef]]
    EntityDetectorConfiguration: NotRequired[EntityDetectorConfigurationOutputTypeDef]

class ProfileConfigurationTypeDef(TypedDict):
    DatasetStatisticsConfiguration: NotRequired[StatisticsConfigurationTypeDef]
    ProfileColumns: NotRequired[Sequence[ColumnSelectorTypeDef]]
    ColumnStatisticsConfigurations: NotRequired[Sequence[ColumnStatisticsConfigurationTypeDef]]
    EntityDetectorConfiguration: NotRequired[EntityDetectorConfigurationTypeDef]

class ListJobRunsResponseTypeDef(TypedDict):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListJobsResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateRecipeJobRequestTypeDef(TypedDict):
    Name: str
    RoleArn: str
    DatasetName: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    EncryptionMode: NotRequired[EncryptionModeType]
    LogSubscription: NotRequired[LogSubscriptionType]
    MaxCapacity: NotRequired[int]
    MaxRetries: NotRequired[int]
    Outputs: NotRequired[Sequence[UnionTypeDef]]
    DataCatalogOutputs: NotRequired[Sequence[DataCatalogOutputTypeDef]]
    DatabaseOutputs: NotRequired[Sequence[DatabaseOutputTypeDef]]
    ProjectName: NotRequired[str]
    RecipeReference: NotRequired[RecipeReferenceTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    Timeout: NotRequired[int]

class UpdateRecipeJobRequestTypeDef(TypedDict):
    Name: str
    RoleArn: str
    EncryptionKeyArn: NotRequired[str]
    EncryptionMode: NotRequired[EncryptionModeType]
    LogSubscription: NotRequired[LogSubscriptionType]
    MaxCapacity: NotRequired[int]
    MaxRetries: NotRequired[int]
    Outputs: NotRequired[Sequence[UnionTypeDef]]
    DataCatalogOutputs: NotRequired[Sequence[DataCatalogOutputTypeDef]]
    DatabaseOutputs: NotRequired[Sequence[DatabaseOutputTypeDef]]
    Timeout: NotRequired[int]

class ListDatasetsResponseTypeDef(TypedDict):
    Datasets: List[DatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDatasetRequestTypeDef(TypedDict):
    Name: str
    Input: InputTypeDef
    Format: NotRequired[InputFormatType]
    FormatOptions: NotRequired[FormatOptionsUnionTypeDef]
    PathOptions: NotRequired[PathOptionsUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateDatasetRequestTypeDef(TypedDict):
    Name: str
    Input: InputTypeDef
    Format: NotRequired[InputFormatType]
    FormatOptions: NotRequired[FormatOptionsUnionTypeDef]
    PathOptions: NotRequired[PathOptionsUnionTypeDef]

class CreateRecipeRequestTypeDef(TypedDict):
    Name: str
    Steps: Sequence[RecipeStepUnionTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class SendProjectSessionActionRequestTypeDef(TypedDict):
    Name: str
    Preview: NotRequired[bool]
    RecipeStep: NotRequired[RecipeStepUnionTypeDef]
    StepIndex: NotRequired[int]
    ClientSessionId: NotRequired[str]
    ViewFrame: NotRequired[ViewFrameTypeDef]

class UpdateRecipeRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Steps: NotRequired[Sequence[RecipeStepUnionTypeDef]]

DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List[ExtraTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "ProjectName": str,
        "ProfileConfiguration": ProfileConfigurationOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationTypeDef],
        "RecipeReference": RecipeReferenceTypeDef,
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": JobSampleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DescribeJobRunResponseTypeDef(TypedDict):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    JobName: str
    ProfileConfiguration: ProfileConfigurationOutputTypeDef
    ValidationConfigurations: List[ValidationConfigurationTypeDef]
    RunId: str
    State: JobRunStateType
    LogSubscription: LogSubscriptionType
    LogGroupName: str
    Outputs: List[ExtraTypeDef]
    DataCatalogOutputs: List[DataCatalogOutputTypeDef]
    DatabaseOutputs: List[DatabaseOutputTypeDef]
    RecipeReference: RecipeReferenceTypeDef
    StartedBy: str
    StartedOn: datetime
    JobSample: JobSampleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ProfileConfigurationUnionTypeDef = Union[
    ProfileConfigurationTypeDef, ProfileConfigurationOutputTypeDef
]

class CreateProfileJobRequestTypeDef(TypedDict):
    DatasetName: str
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    EncryptionKeyArn: NotRequired[str]
    EncryptionMode: NotRequired[EncryptionModeType]
    LogSubscription: NotRequired[LogSubscriptionType]
    MaxCapacity: NotRequired[int]
    MaxRetries: NotRequired[int]
    Configuration: NotRequired[ProfileConfigurationUnionTypeDef]
    ValidationConfigurations: NotRequired[Sequence[ValidationConfigurationTypeDef]]
    Tags: NotRequired[Mapping[str, str]]
    Timeout: NotRequired[int]
    JobSample: NotRequired[JobSampleTypeDef]

class UpdateProfileJobRequestTypeDef(TypedDict):
    Name: str
    OutputLocation: S3LocationTypeDef
    RoleArn: str
    Configuration: NotRequired[ProfileConfigurationUnionTypeDef]
    EncryptionKeyArn: NotRequired[str]
    EncryptionMode: NotRequired[EncryptionModeType]
    LogSubscription: NotRequired[LogSubscriptionType]
    MaxCapacity: NotRequired[int]
    MaxRetries: NotRequired[int]
    ValidationConfigurations: NotRequired[Sequence[ValidationConfigurationTypeDef]]
    Timeout: NotRequired[int]
    JobSample: NotRequired[JobSampleTypeDef]
