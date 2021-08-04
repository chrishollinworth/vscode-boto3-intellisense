"""
Type annotations for databrew service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs.html)

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import BatchDeleteRecipeVersionRequestRequestTypeDef

    data: BatchDeleteRecipeVersionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
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
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "ColumnSelectorTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobRequestRequestTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobRequestRequestTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeRequestRequestTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateScheduleRequestRequestTypeDef",
    "CreateScheduleResponseTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DataCatalogOutputTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseOutputTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionRequestRequestTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListRecipeVersionsRequestRequestTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSchedulesRequestRequestTypeDef",
    "ListSchedulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathOptionsTypeDef",
    "ProfileConfigurationTypeDef",
    "ProjectTypeDef",
    "PublishRecipeRequestRequestTypeDef",
    "PublishRecipeResponseTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "S3TableOutputOptionsTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "SendProjectSessionActionRequestRequestTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionRequestRequestTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StatisticOverrideTypeDef",
    "StatisticsConfigurationTypeDef",
    "StopJobRunRequestRequestTypeDef",
    "StopJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobRequestRequestTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobRequestRequestTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeRequestRequestTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateScheduleRequestRequestTypeDef",
    "UpdateScheduleResponseTypeDef",
    "ViewFrameTypeDef",
)

BatchDeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": List[str],
    },
)

BatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "Errors": List["RecipeVersionErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnSelectorTypeDef = TypedDict(
    "ColumnSelectorTypeDef",
    {
        "Regex": str,
        "Name": str,
    },
    total=False,
)

_RequiredColumnStatisticsConfigurationTypeDef = TypedDict(
    "_RequiredColumnStatisticsConfigurationTypeDef",
    {
        "Statistics": "StatisticsConfigurationTypeDef",
    },
)
_OptionalColumnStatisticsConfigurationTypeDef = TypedDict(
    "_OptionalColumnStatisticsConfigurationTypeDef",
    {
        "Selectors": List["ColumnSelectorTypeDef"],
    },
    total=False,
)

class ColumnStatisticsConfigurationTypeDef(
    _RequiredColumnStatisticsConfigurationTypeDef, _OptionalColumnStatisticsConfigurationTypeDef
):
    pass

_RequiredConditionExpressionTypeDef = TypedDict(
    "_RequiredConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
    },
)
_OptionalConditionExpressionTypeDef = TypedDict(
    "_OptionalConditionExpressionTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class ConditionExpressionTypeDef(
    _RequiredConditionExpressionTypeDef, _OptionalConditionExpressionTypeDef
):
    pass

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateProfileJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileJobRequestRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Configuration": "ProfileConfigurationTypeDef",
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

class CreateProfileJobRequestRequestTypeDef(
    _RequiredCreateProfileJobRequestRequestTypeDef, _OptionalCreateProfileJobRequestRequestTypeDef
):
    pass

CreateProfileJobResponseTypeDef = TypedDict(
    "CreateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "Sample": "SampleTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecipeJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalCreateRecipeJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "Tags": Dict[str, str],
        "Timeout": int,
    },
    total=False,
)

class CreateRecipeJobRequestRequestTypeDef(
    _RequiredCreateRecipeJobRequestRequestTypeDef, _OptionalCreateRecipeJobRequestRequestTypeDef
):
    pass

CreateRecipeJobResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Steps": List["RecipeStepTypeDef"],
    },
)
_OptionalCreateRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRecipeRequestRequestTypeDef(
    _RequiredCreateRecipeRequestRequestTypeDef, _OptionalCreateRecipeRequestRequestTypeDef
):
    pass

CreateRecipeResponseTypeDef = TypedDict(
    "CreateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalCreateScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleRequestRequestTypeDef",
    {
        "JobNames": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateScheduleRequestRequestTypeDef(
    _RequiredCreateScheduleRequestRequestTypeDef, _OptionalCreateScheduleRequestRequestTypeDef
):
    pass

CreateScheduleResponseTypeDef = TypedDict(
    "CreateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": str,
        "HeaderRow": bool,
    },
    total=False,
)

CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": str,
    },
    total=False,
)

_RequiredDataCatalogInputDefinitionTypeDef = TypedDict(
    "_RequiredDataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogInputDefinitionTypeDef = TypedDict(
    "_OptionalDataCatalogInputDefinitionTypeDef",
    {
        "CatalogId": str,
        "TempDirectory": "S3LocationTypeDef",
    },
    total=False,
)

class DataCatalogInputDefinitionTypeDef(
    _RequiredDataCatalogInputDefinitionTypeDef, _OptionalDataCatalogInputDefinitionTypeDef
):
    pass

_RequiredDataCatalogOutputTypeDef = TypedDict(
    "_RequiredDataCatalogOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogOutputTypeDef = TypedDict(
    "_OptionalDataCatalogOutputTypeDef",
    {
        "CatalogId": str,
        "S3Options": "S3TableOutputOptionsTypeDef",
        "DatabaseOptions": "DatabaseTableOutputOptionsTypeDef",
        "Overwrite": bool,
    },
    total=False,
)

class DataCatalogOutputTypeDef(
    _RequiredDataCatalogOutputTypeDef, _OptionalDataCatalogOutputTypeDef
):
    pass

_RequiredDatabaseInputDefinitionTypeDef = TypedDict(
    "_RequiredDatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseTableName": str,
    },
)
_OptionalDatabaseInputDefinitionTypeDef = TypedDict(
    "_OptionalDatabaseInputDefinitionTypeDef",
    {
        "TempDirectory": "S3LocationTypeDef",
    },
    total=False,
)

class DatabaseInputDefinitionTypeDef(
    _RequiredDatabaseInputDefinitionTypeDef, _OptionalDatabaseInputDefinitionTypeDef
):
    pass

_RequiredDatabaseOutputTypeDef = TypedDict(
    "_RequiredDatabaseOutputTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseOptions": "DatabaseTableOutputOptionsTypeDef",
    },
)
_OptionalDatabaseOutputTypeDef = TypedDict(
    "_OptionalDatabaseOutputTypeDef",
    {
        "DatabaseOutputMode": Literal["NEW_TABLE"],
    },
    total=False,
)

class DatabaseOutputTypeDef(_RequiredDatabaseOutputTypeDef, _OptionalDatabaseOutputTypeDef):
    pass

_RequiredDatabaseTableOutputOptionsTypeDef = TypedDict(
    "_RequiredDatabaseTableOutputOptionsTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDatabaseTableOutputOptionsTypeDef = TypedDict(
    "_OptionalDatabaseTableOutputOptionsTypeDef",
    {
        "TempDirectory": "S3LocationTypeDef",
    },
    total=False,
)

class DatabaseTableOutputOptionsTypeDef(
    _RequiredDatabaseTableOutputOptionsTypeDef, _OptionalDatabaseTableOutputOptionsTypeDef
):
    pass

_RequiredDatasetParameterTypeDef = TypedDict(
    "_RequiredDatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalDatasetParameterTypeDef = TypedDict(
    "_OptionalDatasetParameterTypeDef",
    {
        "DatetimeOptions": "DatetimeOptionsTypeDef",
        "CreateColumn": bool,
        "Filter": "FilterExpressionTypeDef",
    },
    total=False,
)

class DatasetParameterTypeDef(_RequiredDatasetParameterTypeDef, _OptionalDatasetParameterTypeDef):
    pass

_RequiredDatasetTypeDef = TypedDict(
    "_RequiredDatasetTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalDatasetTypeDef = TypedDict(
    "_OptionalDatasetTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
    },
    total=False,
)

class DatasetTypeDef(_RequiredDatasetTypeDef, _OptionalDatasetTypeDef):
    pass

_RequiredDatetimeOptionsTypeDef = TypedDict(
    "_RequiredDatetimeOptionsTypeDef",
    {
        "Format": str,
    },
)
_OptionalDatetimeOptionsTypeDef = TypedDict(
    "_OptionalDatetimeOptionsTypeDef",
    {
        "TimezoneOffset": str,
        "LocaleCode": str,
    },
    total=False,
)

class DatetimeOptionsTypeDef(_RequiredDatetimeOptionsTypeDef, _OptionalDatetimeOptionsTypeDef):
    pass

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)

DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScheduleResponseTypeDef = TypedDict(
    "DeleteScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "Input": "InputTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

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
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "ProjectName": str,
        "ProfileConfiguration": "ProfileConfigurationTypeDef",
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "ProfileConfiguration": "ProfileConfigurationTypeDef",
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRecipeRequestRequestTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)

class DescribeRecipeRequestRequestTypeDef(
    _RequiredDescribeRecipeRequestRequestTypeDef, _OptionalDescribeRecipeRequestRequestTypeDef
):
    pass

DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": List[str],
        "SheetIndexes": List[int],
        "HeaderRow": bool,
    },
    total=False,
)

_RequiredFilesLimitTypeDef = TypedDict(
    "_RequiredFilesLimitTypeDef",
    {
        "MaxFiles": int,
    },
)
_OptionalFilesLimitTypeDef = TypedDict(
    "_OptionalFilesLimitTypeDef",
    {
        "OrderedBy": Literal["LAST_MODIFIED_DATE"],
        "Order": OrderType,
    },
    total=False,
)

class FilesLimitTypeDef(_RequiredFilesLimitTypeDef, _OptionalFilesLimitTypeDef):
    pass

FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Dict[str, str],
    },
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": "JsonOptionsTypeDef",
        "Excel": "ExcelOptionsTypeDef",
        "Csv": "CsvOptionsTypeDef",
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": "S3LocationTypeDef",
        "DataCatalogInputDefinition": "DataCatalogInputDefinitionTypeDef",
        "DatabaseInputDefinition": "DatabaseInputDefinitionTypeDef",
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": SampleModeType,
        "Size": int,
    },
    total=False,
)

_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef",
    {
        "Name": str,
    },
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Timeout": int,
        "Tags": Dict[str, str],
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass

JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": bool,
    },
    total=False,
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DatasetName": str,
        "MaxResults": int,
        "NextToken": str,
        "ProjectName": str,
    },
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List["ProjectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecipeVersionsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecipeVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRecipeVersionsRequestRequestTypeDef(
    _RequiredListRecipeVersionsRequestRequestTypeDef,
    _OptionalListRecipeVersionsRequestRequestTypeDef,
):
    pass

ListRecipeVersionsResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Recipes": List["RecipeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "RecipeVersion": str,
    },
    total=False,
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "Recipes": List["RecipeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulesRequestRequestTypeDef = TypedDict(
    "ListSchedulesRequestRequestTypeDef",
    {
        "JobName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSchedulesResponseTypeDef = TypedDict(
    "ListSchedulesResponseTypeDef",
    {
        "Schedules": List["ScheduleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": "CsvOutputOptionsTypeDef",
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Location": "S3LocationTypeDef",
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "CompressionFormat": CompressionFormatType,
        "Format": OutputFormatType,
        "PartitionColumns": List[str],
        "Overwrite": bool,
        "FormatOptions": "OutputFormatOptionsTypeDef",
    },
    total=False,
)

class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": "FilterExpressionTypeDef",
        "FilesLimit": "FilesLimitTypeDef",
        "Parameters": Dict[str, "DatasetParameterTypeDef"],
    },
    total=False,
)

ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "DatasetStatisticsConfiguration": "StatisticsConfigurationTypeDef",
        "ProfileColumns": List["ColumnSelectorTypeDef"],
        "ColumnStatisticsConfigurations": List["ColumnStatisticsConfigurationTypeDef"],
    },
    total=False,
)

_RequiredProjectTypeDef = TypedDict(
    "_RequiredProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
    },
)
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "AccountId": str,
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "Tags": Dict[str, str],
        "RoleArn": str,
        "OpenedBy": str,
        "OpenDate": datetime,
    },
    total=False,
)

class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass

_RequiredPublishRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredPublishRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPublishRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalPublishRecipeRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class PublishRecipeRequestRequestTypeDef(
    _RequiredPublishRecipeRequestRequestTypeDef, _OptionalPublishRecipeRequestRequestTypeDef
):
    pass

PublishRecipeResponseTypeDef = TypedDict(
    "PublishRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeActionTypeDef = TypedDict(
    "_RequiredRecipeActionTypeDef",
    {
        "Operation": str,
    },
)
_OptionalRecipeActionTypeDef = TypedDict(
    "_OptionalRecipeActionTypeDef",
    {
        "Parameters": Dict[str, str],
    },
    total=False,
)

class RecipeActionTypeDef(_RequiredRecipeActionTypeDef, _OptionalRecipeActionTypeDef):
    pass

_RequiredRecipeReferenceTypeDef = TypedDict(
    "_RequiredRecipeReferenceTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeReferenceTypeDef = TypedDict(
    "_OptionalRecipeReferenceTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)

class RecipeReferenceTypeDef(_RequiredRecipeReferenceTypeDef, _OptionalRecipeReferenceTypeDef):
    pass

_RequiredRecipeStepTypeDef = TypedDict(
    "_RequiredRecipeStepTypeDef",
    {
        "Action": "RecipeActionTypeDef",
    },
)
_OptionalRecipeStepTypeDef = TypedDict(
    "_OptionalRecipeStepTypeDef",
    {
        "ConditionExpressions": List["ConditionExpressionTypeDef"],
    },
    total=False,
)

class RecipeStepTypeDef(_RequiredRecipeStepTypeDef, _OptionalRecipeStepTypeDef):
    pass

_RequiredRecipeTypeDef = TypedDict(
    "_RequiredRecipeTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeTypeDef = TypedDict(
    "_OptionalRecipeTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "ResourceArn": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "RecipeVersion": str,
    },
    total=False,
)

class RecipeTypeDef(_RequiredRecipeTypeDef, _OptionalRecipeTypeDef):
    pass

RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "RecipeVersion": str,
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

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

S3TableOutputOptionsTypeDef = TypedDict(
    "S3TableOutputOptionsTypeDef",
    {
        "Location": "S3LocationTypeDef",
    },
)

_RequiredSampleTypeDef = TypedDict(
    "_RequiredSampleTypeDef",
    {
        "Type": SampleTypeType,
    },
)
_OptionalSampleTypeDef = TypedDict(
    "_OptionalSampleTypeDef",
    {
        "Size": int,
    },
    total=False,
)

class SampleTypeDef(_RequiredSampleTypeDef, _OptionalSampleTypeDef):
    pass

_RequiredScheduleTypeDef = TypedDict(
    "_RequiredScheduleTypeDef",
    {
        "Name": str,
    },
)
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass

_RequiredSendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "_RequiredSendProjectSessionActionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalSendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "_OptionalSendProjectSessionActionRequestRequestTypeDef",
    {
        "Preview": bool,
        "RecipeStep": "RecipeStepTypeDef",
        "StepIndex": int,
        "ClientSessionId": str,
        "ViewFrame": "ViewFrameTypeDef",
    },
    total=False,
)

class SendProjectSessionActionRequestRequestTypeDef(
    _RequiredSendProjectSessionActionRequestRequestTypeDef,
    _OptionalSendProjectSessionActionRequestRequestTypeDef,
):
    pass

SendProjectSessionActionResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartProjectSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStartProjectSessionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartProjectSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStartProjectSessionRequestRequestTypeDef",
    {
        "AssumeControl": bool,
    },
    total=False,
)

class StartProjectSessionRequestRequestTypeDef(
    _RequiredStartProjectSessionRequestRequestTypeDef,
    _OptionalStartProjectSessionRequestRequestTypeDef,
):
    pass

StartProjectSessionResponseTypeDef = TypedDict(
    "StartProjectSessionResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticOverrideTypeDef = TypedDict(
    "StatisticOverrideTypeDef",
    {
        "Statistic": str,
        "Parameters": Dict[str, str],
    },
)

StatisticsConfigurationTypeDef = TypedDict(
    "StatisticsConfigurationTypeDef",
    {
        "IncludedStatistics": List[str],
        "Overrides": List["StatisticOverrideTypeDef"],
    },
    total=False,
)

StopJobRunRequestRequestTypeDef = TypedDict(
    "StopJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StopJobRunResponseTypeDef = TypedDict(
    "StopJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "PathOptions": "PathOptionsTypeDef",
    },
    total=False,
)

class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileJobRequestRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
    },
)
_OptionalUpdateProfileJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileJobRequestRequestTypeDef",
    {
        "Configuration": "ProfileConfigurationTypeDef",
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

class UpdateProfileJobRequestRequestTypeDef(
    _RequiredUpdateProfileJobRequestRequestTypeDef, _OptionalUpdateProfileJobRequestRequestTypeDef
):
    pass

UpdateProfileJobResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "Sample": "SampleTypeDef",
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalUpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeJobRequestRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "Timeout": int,
    },
    total=False,
)

class UpdateRecipeJobRequestRequestTypeDef(
    _RequiredUpdateRecipeJobRequestRequestTypeDef, _OptionalUpdateRecipeJobRequestRequestTypeDef
):
    pass

UpdateRecipeJobResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeRequestRequestTypeDef",
    {
        "Description": str,
        "Steps": List["RecipeStepTypeDef"],
    },
    total=False,
)

class UpdateRecipeRequestRequestTypeDef(
    _RequiredUpdateRecipeRequestRequestTypeDef, _OptionalUpdateRecipeRequestRequestTypeDef
):
    pass

UpdateRecipeResponseTypeDef = TypedDict(
    "UpdateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduleRequestRequestTypeDef",
    {
        "JobNames": List[str],
    },
    total=False,
)

class UpdateScheduleRequestRequestTypeDef(
    _RequiredUpdateScheduleRequestRequestTypeDef, _OptionalUpdateScheduleRequestRequestTypeDef
):
    pass

UpdateScheduleResponseTypeDef = TypedDict(
    "UpdateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredViewFrameTypeDef = TypedDict(
    "_RequiredViewFrameTypeDef",
    {
        "StartColumnIndex": int,
    },
)
_OptionalViewFrameTypeDef = TypedDict(
    "_OptionalViewFrameTypeDef",
    {
        "ColumnRange": int,
        "HiddenColumns": List[str],
    },
    total=False,
)

class ViewFrameTypeDef(_RequiredViewFrameTypeDef, _OptionalViewFrameTypeDef):
    pass
