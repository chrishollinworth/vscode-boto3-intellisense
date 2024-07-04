"""
Type annotations for apptest service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apptest.type_defs import BatchStepInputTypeDef

    data: BatchStepInputTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CaptureToolType,
    CloudFormationActionTypeType,
    ComparisonStatusEnumType,
    FormatType,
    M2ManagedActionTypeType,
    M2NonManagedActionTypeType,
    StepRunStatusType,
    TestCaseLifecycleType,
    TestCaseRunStatusType,
    TestConfigurationLifecycleType,
    TestRunStatusType,
    TestSuiteLifecycleType,
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
    "BatchStepInputTypeDef",
    "BatchStepOutputTypeDef",
    "BatchSummaryTypeDef",
    "BatchTypeDef",
    "CloudFormationActionTypeDef",
    "CloudFormationStepSummaryTypeDef",
    "CloudFormationTypeDef",
    "CompareActionSummaryTypeDef",
    "CompareActionTypeDef",
    "CompareDataSetsStepInputTypeDef",
    "CompareDataSetsStepOutputTypeDef",
    "CompareDataSetsSummaryTypeDef",
    "CompareDatabaseCDCStepInputTypeDef",
    "CompareDatabaseCDCStepOutputTypeDef",
    "CompareDatabaseCDCSummaryTypeDef",
    "CompareFileTypeTypeDef",
    "CreateCloudFormationStepInputTypeDef",
    "CreateCloudFormationStepOutputTypeDef",
    "CreateCloudFormationSummaryTypeDef",
    "CreateTestCaseRequestRequestTypeDef",
    "CreateTestCaseResponseTypeDef",
    "CreateTestConfigurationRequestRequestTypeDef",
    "CreateTestConfigurationResponseTypeDef",
    "CreateTestSuiteRequestRequestTypeDef",
    "CreateTestSuiteResponseTypeDef",
    "DataSetTypeDef",
    "DatabaseCDCTypeDef",
    "DeleteCloudFormationStepInputTypeDef",
    "DeleteCloudFormationSummaryTypeDef",
    "DeleteTestCaseRequestRequestTypeDef",
    "DeleteTestConfigurationRequestRequestTypeDef",
    "DeleteTestRunRequestRequestTypeDef",
    "DeleteTestSuiteRequestRequestTypeDef",
    "FileMetadataTypeDef",
    "FileTypeDef",
    "GetTestCaseRequestRequestTypeDef",
    "GetTestCaseResponseTypeDef",
    "GetTestConfigurationRequestRequestTypeDef",
    "GetTestConfigurationResponseTypeDef",
    "GetTestRunStepRequestRequestTypeDef",
    "GetTestRunStepResponseTypeDef",
    "GetTestSuiteRequestRequestTypeDef",
    "GetTestSuiteResponseTypeDef",
    "InputFileTypeDef",
    "InputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestCasesRequestRequestTypeDef",
    "ListTestCasesResponseTypeDef",
    "ListTestConfigurationsRequestRequestTypeDef",
    "ListTestConfigurationsResponseTypeDef",
    "ListTestRunStepsRequestRequestTypeDef",
    "ListTestRunStepsResponseTypeDef",
    "ListTestRunTestCasesRequestRequestTypeDef",
    "ListTestRunTestCasesResponseTypeDef",
    "ListTestRunsRequestRequestTypeDef",
    "ListTestRunsResponseTypeDef",
    "ListTestSuitesRequestRequestTypeDef",
    "ListTestSuitesResponseTypeDef",
    "M2ManagedActionPropertiesTypeDef",
    "M2ManagedApplicationActionTypeDef",
    "M2ManagedApplicationStepInputTypeDef",
    "M2ManagedApplicationStepOutputTypeDef",
    "M2ManagedApplicationStepSummaryTypeDef",
    "M2ManagedApplicationSummaryTypeDef",
    "M2ManagedApplicationTypeDef",
    "M2NonManagedApplicationActionTypeDef",
    "M2NonManagedApplicationStepInputTypeDef",
    "M2NonManagedApplicationStepSummaryTypeDef",
    "M2NonManagedApplicationSummaryTypeDef",
    "M2NonManagedApplicationTypeDef",
    "MainframeActionPropertiesTypeDef",
    "MainframeActionSummaryTypeDef",
    "MainframeActionTypeDef",
    "MainframeActionTypeTypeDef",
    "MainframeResourceSummaryTypeDef",
    "OutputFileTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceActionSummaryTypeDef",
    "ResourceActionTypeDef",
    "ResourceTypeDef",
    "ResourceTypeTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptSummaryTypeDef",
    "ScriptTypeDef",
    "ServiceSettingsTypeDef",
    "SourceDatabaseMetadataTypeDef",
    "StartTestRunRequestRequestTypeDef",
    "StartTestRunResponseTypeDef",
    "StepActionTypeDef",
    "StepRunSummaryTypeDef",
    "StepTypeDef",
    "TN3270StepInputTypeDef",
    "TN3270StepOutputTypeDef",
    "TN3270SummaryTypeDef",
    "TN3270TypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetDatabaseMetadataTypeDef",
    "TestCaseLatestVersionTypeDef",
    "TestCaseRunSummaryTypeDef",
    "TestCaseSummaryTypeDef",
    "TestCasesTypeDef",
    "TestConfigurationLatestVersionTypeDef",
    "TestConfigurationSummaryTypeDef",
    "TestRunStepSummaryTypeDef",
    "TestRunSummaryTypeDef",
    "TestSuiteLatestVersionTypeDef",
    "TestSuiteSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateTestCaseRequestRequestTypeDef",
    "UpdateTestCaseResponseTypeDef",
    "UpdateTestConfigurationRequestRequestTypeDef",
    "UpdateTestConfigurationResponseTypeDef",
    "UpdateTestSuiteRequestRequestTypeDef",
    "UpdateTestSuiteResponseTypeDef",
)

_RequiredBatchStepInputTypeDef = TypedDict(
    "_RequiredBatchStepInputTypeDef",
    {
        "resource": "MainframeResourceSummaryTypeDef",
        "batchJobName": str,
    },
)
_OptionalBatchStepInputTypeDef = TypedDict(
    "_OptionalBatchStepInputTypeDef",
    {
        "batchJobParameters": Dict[str, str],
        "exportDataSetNames": List[str],
        "properties": "MainframeActionPropertiesTypeDef",
    },
    total=False,
)

class BatchStepInputTypeDef(_RequiredBatchStepInputTypeDef, _OptionalBatchStepInputTypeDef):
    pass

BatchStepOutputTypeDef = TypedDict(
    "BatchStepOutputTypeDef",
    {
        "dataSetExportLocation": str,
        "dmsOutputLocation": str,
        "dataSetDetails": List["DataSetTypeDef"],
    },
    total=False,
)

_RequiredBatchSummaryTypeDef = TypedDict(
    "_RequiredBatchSummaryTypeDef",
    {
        "stepInput": "BatchStepInputTypeDef",
    },
)
_OptionalBatchSummaryTypeDef = TypedDict(
    "_OptionalBatchSummaryTypeDef",
    {
        "stepOutput": "BatchStepOutputTypeDef",
    },
    total=False,
)

class BatchSummaryTypeDef(_RequiredBatchSummaryTypeDef, _OptionalBatchSummaryTypeDef):
    pass

_RequiredBatchTypeDef = TypedDict(
    "_RequiredBatchTypeDef",
    {
        "batchJobName": str,
    },
)
_OptionalBatchTypeDef = TypedDict(
    "_OptionalBatchTypeDef",
    {
        "batchJobParameters": Dict[str, str],
        "exportDataSetNames": List[str],
    },
    total=False,
)

class BatchTypeDef(_RequiredBatchTypeDef, _OptionalBatchTypeDef):
    pass

_RequiredCloudFormationActionTypeDef = TypedDict(
    "_RequiredCloudFormationActionTypeDef",
    {
        "resource": str,
    },
)
_OptionalCloudFormationActionTypeDef = TypedDict(
    "_OptionalCloudFormationActionTypeDef",
    {
        "actionType": CloudFormationActionTypeType,
    },
    total=False,
)

class CloudFormationActionTypeDef(
    _RequiredCloudFormationActionTypeDef, _OptionalCloudFormationActionTypeDef
):
    pass

CloudFormationStepSummaryTypeDef = TypedDict(
    "CloudFormationStepSummaryTypeDef",
    {
        "createCloudformation": "CreateCloudFormationSummaryTypeDef",
        "deleteCloudformation": "DeleteCloudFormationSummaryTypeDef",
    },
    total=False,
)

_RequiredCloudFormationTypeDef = TypedDict(
    "_RequiredCloudFormationTypeDef",
    {
        "templateLocation": str,
    },
)
_OptionalCloudFormationTypeDef = TypedDict(
    "_OptionalCloudFormationTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)

class CloudFormationTypeDef(_RequiredCloudFormationTypeDef, _OptionalCloudFormationTypeDef):
    pass

CompareActionSummaryTypeDef = TypedDict(
    "CompareActionSummaryTypeDef",
    {
        "type": "FileTypeDef",
    },
)

_RequiredCompareActionTypeDef = TypedDict(
    "_RequiredCompareActionTypeDef",
    {
        "input": "InputTypeDef",
    },
)
_OptionalCompareActionTypeDef = TypedDict(
    "_OptionalCompareActionTypeDef",
    {
        "output": "OutputTypeDef",
    },
    total=False,
)

class CompareActionTypeDef(_RequiredCompareActionTypeDef, _OptionalCompareActionTypeDef):
    pass

CompareDataSetsStepInputTypeDef = TypedDict(
    "CompareDataSetsStepInputTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "sourceDataSets": List["DataSetTypeDef"],
        "targetDataSets": List["DataSetTypeDef"],
    },
)

CompareDataSetsStepOutputTypeDef = TypedDict(
    "CompareDataSetsStepOutputTypeDef",
    {
        "comparisonOutputLocation": str,
        "comparisonStatus": ComparisonStatusEnumType,
    },
)

_RequiredCompareDataSetsSummaryTypeDef = TypedDict(
    "_RequiredCompareDataSetsSummaryTypeDef",
    {
        "stepInput": "CompareDataSetsStepInputTypeDef",
    },
)
_OptionalCompareDataSetsSummaryTypeDef = TypedDict(
    "_OptionalCompareDataSetsSummaryTypeDef",
    {
        "stepOutput": "CompareDataSetsStepOutputTypeDef",
    },
    total=False,
)

class CompareDataSetsSummaryTypeDef(
    _RequiredCompareDataSetsSummaryTypeDef, _OptionalCompareDataSetsSummaryTypeDef
):
    pass

_RequiredCompareDatabaseCDCStepInputTypeDef = TypedDict(
    "_RequiredCompareDatabaseCDCStepInputTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "sourceMetadata": "SourceDatabaseMetadataTypeDef",
        "targetMetadata": "TargetDatabaseMetadataTypeDef",
    },
)
_OptionalCompareDatabaseCDCStepInputTypeDef = TypedDict(
    "_OptionalCompareDatabaseCDCStepInputTypeDef",
    {
        "outputLocation": str,
    },
    total=False,
)

class CompareDatabaseCDCStepInputTypeDef(
    _RequiredCompareDatabaseCDCStepInputTypeDef, _OptionalCompareDatabaseCDCStepInputTypeDef
):
    pass

CompareDatabaseCDCStepOutputTypeDef = TypedDict(
    "CompareDatabaseCDCStepOutputTypeDef",
    {
        "comparisonOutputLocation": str,
        "comparisonStatus": ComparisonStatusEnumType,
    },
)

_RequiredCompareDatabaseCDCSummaryTypeDef = TypedDict(
    "_RequiredCompareDatabaseCDCSummaryTypeDef",
    {
        "stepInput": "CompareDatabaseCDCStepInputTypeDef",
    },
)
_OptionalCompareDatabaseCDCSummaryTypeDef = TypedDict(
    "_OptionalCompareDatabaseCDCSummaryTypeDef",
    {
        "stepOutput": "CompareDatabaseCDCStepOutputTypeDef",
    },
    total=False,
)

class CompareDatabaseCDCSummaryTypeDef(
    _RequiredCompareDatabaseCDCSummaryTypeDef, _OptionalCompareDatabaseCDCSummaryTypeDef
):
    pass

CompareFileTypeTypeDef = TypedDict(
    "CompareFileTypeTypeDef",
    {
        "datasets": "CompareDataSetsSummaryTypeDef",
        "databaseCDC": "CompareDatabaseCDCSummaryTypeDef",
    },
    total=False,
)

_RequiredCreateCloudFormationStepInputTypeDef = TypedDict(
    "_RequiredCreateCloudFormationStepInputTypeDef",
    {
        "templateLocation": str,
    },
)
_OptionalCreateCloudFormationStepInputTypeDef = TypedDict(
    "_OptionalCreateCloudFormationStepInputTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)

class CreateCloudFormationStepInputTypeDef(
    _RequiredCreateCloudFormationStepInputTypeDef, _OptionalCreateCloudFormationStepInputTypeDef
):
    pass

_RequiredCreateCloudFormationStepOutputTypeDef = TypedDict(
    "_RequiredCreateCloudFormationStepOutputTypeDef",
    {
        "stackId": str,
    },
)
_OptionalCreateCloudFormationStepOutputTypeDef = TypedDict(
    "_OptionalCreateCloudFormationStepOutputTypeDef",
    {
        "exports": Dict[str, str],
    },
    total=False,
)

class CreateCloudFormationStepOutputTypeDef(
    _RequiredCreateCloudFormationStepOutputTypeDef, _OptionalCreateCloudFormationStepOutputTypeDef
):
    pass

_RequiredCreateCloudFormationSummaryTypeDef = TypedDict(
    "_RequiredCreateCloudFormationSummaryTypeDef",
    {
        "stepInput": "CreateCloudFormationStepInputTypeDef",
    },
)
_OptionalCreateCloudFormationSummaryTypeDef = TypedDict(
    "_OptionalCreateCloudFormationSummaryTypeDef",
    {
        "stepOutput": "CreateCloudFormationStepOutputTypeDef",
    },
    total=False,
)

class CreateCloudFormationSummaryTypeDef(
    _RequiredCreateCloudFormationSummaryTypeDef, _OptionalCreateCloudFormationSummaryTypeDef
):
    pass

_RequiredCreateTestCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTestCaseRequestRequestTypeDef",
    {
        "name": str,
        "steps": List["StepTypeDef"],
    },
)
_OptionalCreateTestCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTestCaseRequestRequestTypeDef",
    {
        "description": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateTestCaseRequestRequestTypeDef(
    _RequiredCreateTestCaseRequestRequestTypeDef, _OptionalCreateTestCaseRequestRequestTypeDef
):
    pass

CreateTestCaseResponseTypeDef = TypedDict(
    "CreateTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTestConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTestConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "resources": List["ResourceTypeDef"],
    },
)
_OptionalCreateTestConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTestConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "properties": Dict[str, str],
        "clientToken": str,
        "tags": Dict[str, str],
        "serviceSettings": "ServiceSettingsTypeDef",
    },
    total=False,
)

class CreateTestConfigurationRequestRequestTypeDef(
    _RequiredCreateTestConfigurationRequestRequestTypeDef,
    _OptionalCreateTestConfigurationRequestRequestTypeDef,
):
    pass

CreateTestConfigurationResponseTypeDef = TypedDict(
    "CreateTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTestSuiteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTestSuiteRequestRequestTypeDef",
    {
        "name": str,
        "testCases": "TestCasesTypeDef",
    },
)
_OptionalCreateTestSuiteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTestSuiteRequestRequestTypeDef",
    {
        "description": str,
        "beforeSteps": List["StepTypeDef"],
        "afterSteps": List["StepTypeDef"],
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateTestSuiteRequestRequestTypeDef(
    _RequiredCreateTestSuiteRequestRequestTypeDef, _OptionalCreateTestSuiteRequestRequestTypeDef
):
    pass

CreateTestSuiteResponseTypeDef = TypedDict(
    "CreateTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "testSuiteVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "type": Literal["PS"],
        "name": str,
        "ccsid": str,
        "format": FormatType,
        "length": int,
    },
)

DatabaseCDCTypeDef = TypedDict(
    "DatabaseCDCTypeDef",
    {
        "sourceMetadata": "SourceDatabaseMetadataTypeDef",
        "targetMetadata": "TargetDatabaseMetadataTypeDef",
    },
)

DeleteCloudFormationStepInputTypeDef = TypedDict(
    "DeleteCloudFormationStepInputTypeDef",
    {
        "stackId": str,
    },
)

_RequiredDeleteCloudFormationSummaryTypeDef = TypedDict(
    "_RequiredDeleteCloudFormationSummaryTypeDef",
    {
        "stepInput": "DeleteCloudFormationStepInputTypeDef",
    },
)
_OptionalDeleteCloudFormationSummaryTypeDef = TypedDict(
    "_OptionalDeleteCloudFormationSummaryTypeDef",
    {
        "stepOutput": Dict[str, Any],
    },
    total=False,
)

class DeleteCloudFormationSummaryTypeDef(
    _RequiredDeleteCloudFormationSummaryTypeDef, _OptionalDeleteCloudFormationSummaryTypeDef
):
    pass

DeleteTestCaseRequestRequestTypeDef = TypedDict(
    "DeleteTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
    },
)

DeleteTestConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
    },
)

DeleteTestRunRequestRequestTypeDef = TypedDict(
    "DeleteTestRunRequestRequestTypeDef",
    {
        "testRunId": str,
    },
)

DeleteTestSuiteRequestRequestTypeDef = TypedDict(
    "DeleteTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
    },
)

FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {
        "dataSets": List["DataSetTypeDef"],
        "databaseCDC": "DatabaseCDCTypeDef",
    },
    total=False,
)

FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "fileType": "CompareFileTypeTypeDef",
    },
    total=False,
)

_RequiredGetTestCaseRequestRequestTypeDef = TypedDict(
    "_RequiredGetTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
    },
)
_OptionalGetTestCaseRequestRequestTypeDef = TypedDict(
    "_OptionalGetTestCaseRequestRequestTypeDef",
    {
        "testCaseVersion": int,
    },
    total=False,
)

class GetTestCaseRequestRequestTypeDef(
    _RequiredGetTestCaseRequestRequestTypeDef, _OptionalGetTestCaseRequestRequestTypeDef
):
    pass

GetTestCaseResponseTypeDef = TypedDict(
    "GetTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseArn": str,
        "name": str,
        "description": str,
        "latestVersion": "TestCaseLatestVersionTypeDef",
        "testCaseVersion": int,
        "status": TestCaseLifecycleType,
        "statusReason": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "steps": List["StepTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTestConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
    },
)
_OptionalGetTestConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationVersion": int,
    },
    total=False,
)

class GetTestConfigurationRequestRequestTypeDef(
    _RequiredGetTestConfigurationRequestRequestTypeDef,
    _OptionalGetTestConfigurationRequestRequestTypeDef,
):
    pass

GetTestConfigurationResponseTypeDef = TypedDict(
    "GetTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "name": str,
        "testConfigurationArn": str,
        "latestVersion": "TestConfigurationLatestVersionTypeDef",
        "testConfigurationVersion": int,
        "status": TestConfigurationLifecycleType,
        "statusReason": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "description": str,
        "resources": List["ResourceTypeDef"],
        "properties": Dict[str, str],
        "tags": Dict[str, str],
        "serviceSettings": "ServiceSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTestRunStepRequestRequestTypeDef = TypedDict(
    "_RequiredGetTestRunStepRequestRequestTypeDef",
    {
        "testRunId": str,
        "stepName": str,
    },
)
_OptionalGetTestRunStepRequestRequestTypeDef = TypedDict(
    "_OptionalGetTestRunStepRequestRequestTypeDef",
    {
        "testCaseId": str,
        "testSuiteId": str,
    },
    total=False,
)

class GetTestRunStepRequestRequestTypeDef(
    _RequiredGetTestRunStepRequestRequestTypeDef, _OptionalGetTestRunStepRequestRequestTypeDef
):
    pass

GetTestRunStepResponseTypeDef = TypedDict(
    "GetTestRunStepResponseTypeDef",
    {
        "stepName": str,
        "testRunId": str,
        "testCaseId": str,
        "testCaseVersion": int,
        "testSuiteId": str,
        "testSuiteVersion": int,
        "beforeStep": bool,
        "afterStep": bool,
        "status": StepRunStatusType,
        "statusReason": str,
        "runStartTime": datetime,
        "runEndTime": datetime,
        "stepRunSummary": "StepRunSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTestSuiteRequestRequestTypeDef = TypedDict(
    "_RequiredGetTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
    },
)
_OptionalGetTestSuiteRequestRequestTypeDef = TypedDict(
    "_OptionalGetTestSuiteRequestRequestTypeDef",
    {
        "testSuiteVersion": int,
    },
    total=False,
)

class GetTestSuiteRequestRequestTypeDef(
    _RequiredGetTestSuiteRequestRequestTypeDef, _OptionalGetTestSuiteRequestRequestTypeDef
):
    pass

GetTestSuiteResponseTypeDef = TypedDict(
    "GetTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "name": str,
        "latestVersion": "TestSuiteLatestVersionTypeDef",
        "testSuiteVersion": int,
        "status": TestSuiteLifecycleType,
        "statusReason": str,
        "testSuiteArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "description": str,
        "beforeSteps": List["StepTypeDef"],
        "afterSteps": List["StepTypeDef"],
        "testCases": "TestCasesTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputFileTypeDef = TypedDict(
    "InputFileTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "fileMetadata": "FileMetadataTypeDef",
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "file": "InputFileTypeDef",
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestCasesRequestRequestTypeDef = TypedDict(
    "ListTestCasesRequestRequestTypeDef",
    {
        "testCaseIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTestCasesResponseTypeDef = TypedDict(
    "ListTestCasesResponseTypeDef",
    {
        "testCases": List["TestCaseSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTestConfigurationsRequestRequestTypeDef",
    {
        "testConfigurationIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTestConfigurationsResponseTypeDef = TypedDict(
    "ListTestConfigurationsResponseTypeDef",
    {
        "testConfigurations": List["TestConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestRunStepsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestRunStepsRequestRequestTypeDef",
    {
        "testRunId": str,
    },
)
_OptionalListTestRunStepsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestRunStepsRequestRequestTypeDef",
    {
        "testCaseId": str,
        "testSuiteId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTestRunStepsRequestRequestTypeDef(
    _RequiredListTestRunStepsRequestRequestTypeDef, _OptionalListTestRunStepsRequestRequestTypeDef
):
    pass

ListTestRunStepsResponseTypeDef = TypedDict(
    "ListTestRunStepsResponseTypeDef",
    {
        "testRunSteps": List["TestRunStepSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestRunTestCasesRequestRequestTypeDef = TypedDict(
    "_RequiredListTestRunTestCasesRequestRequestTypeDef",
    {
        "testRunId": str,
    },
)
_OptionalListTestRunTestCasesRequestRequestTypeDef = TypedDict(
    "_OptionalListTestRunTestCasesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTestRunTestCasesRequestRequestTypeDef(
    _RequiredListTestRunTestCasesRequestRequestTypeDef,
    _OptionalListTestRunTestCasesRequestRequestTypeDef,
):
    pass

ListTestRunTestCasesResponseTypeDef = TypedDict(
    "ListTestRunTestCasesResponseTypeDef",
    {
        "testRunTestCases": List["TestCaseRunSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestRunsRequestRequestTypeDef = TypedDict(
    "ListTestRunsRequestRequestTypeDef",
    {
        "testSuiteId": str,
        "testRunIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTestRunsResponseTypeDef = TypedDict(
    "ListTestRunsResponseTypeDef",
    {
        "testRuns": List["TestRunSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestSuitesRequestRequestTypeDef = TypedDict(
    "ListTestSuitesRequestRequestTypeDef",
    {
        "testSuiteIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTestSuitesResponseTypeDef = TypedDict(
    "ListTestSuitesResponseTypeDef",
    {
        "testSuites": List["TestSuiteSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

M2ManagedActionPropertiesTypeDef = TypedDict(
    "M2ManagedActionPropertiesTypeDef",
    {
        "forceStop": bool,
        "importDataSetLocation": str,
    },
    total=False,
)

_RequiredM2ManagedApplicationActionTypeDef = TypedDict(
    "_RequiredM2ManagedApplicationActionTypeDef",
    {
        "resource": str,
        "actionType": M2ManagedActionTypeType,
    },
)
_OptionalM2ManagedApplicationActionTypeDef = TypedDict(
    "_OptionalM2ManagedApplicationActionTypeDef",
    {
        "properties": "M2ManagedActionPropertiesTypeDef",
    },
    total=False,
)

class M2ManagedApplicationActionTypeDef(
    _RequiredM2ManagedApplicationActionTypeDef, _OptionalM2ManagedApplicationActionTypeDef
):
    pass

_RequiredM2ManagedApplicationStepInputTypeDef = TypedDict(
    "_RequiredM2ManagedApplicationStepInputTypeDef",
    {
        "applicationId": str,
        "runtime": str,
        "actionType": M2ManagedActionTypeType,
    },
)
_OptionalM2ManagedApplicationStepInputTypeDef = TypedDict(
    "_OptionalM2ManagedApplicationStepInputTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": int,
        "properties": "M2ManagedActionPropertiesTypeDef",
    },
    total=False,
)

class M2ManagedApplicationStepInputTypeDef(
    _RequiredM2ManagedApplicationStepInputTypeDef, _OptionalM2ManagedApplicationStepInputTypeDef
):
    pass

M2ManagedApplicationStepOutputTypeDef = TypedDict(
    "M2ManagedApplicationStepOutputTypeDef",
    {
        "importDataSetSummary": Dict[str, str],
    },
    total=False,
)

_RequiredM2ManagedApplicationStepSummaryTypeDef = TypedDict(
    "_RequiredM2ManagedApplicationStepSummaryTypeDef",
    {
        "stepInput": "M2ManagedApplicationStepInputTypeDef",
    },
)
_OptionalM2ManagedApplicationStepSummaryTypeDef = TypedDict(
    "_OptionalM2ManagedApplicationStepSummaryTypeDef",
    {
        "stepOutput": "M2ManagedApplicationStepOutputTypeDef",
    },
    total=False,
)

class M2ManagedApplicationStepSummaryTypeDef(
    _RequiredM2ManagedApplicationStepSummaryTypeDef, _OptionalM2ManagedApplicationStepSummaryTypeDef
):
    pass

_RequiredM2ManagedApplicationSummaryTypeDef = TypedDict(
    "_RequiredM2ManagedApplicationSummaryTypeDef",
    {
        "applicationId": str,
        "runtime": Literal["MicroFocus"],
    },
)
_OptionalM2ManagedApplicationSummaryTypeDef = TypedDict(
    "_OptionalM2ManagedApplicationSummaryTypeDef",
    {
        "listenerPort": int,
    },
    total=False,
)

class M2ManagedApplicationSummaryTypeDef(
    _RequiredM2ManagedApplicationSummaryTypeDef, _OptionalM2ManagedApplicationSummaryTypeDef
):
    pass

_RequiredM2ManagedApplicationTypeDef = TypedDict(
    "_RequiredM2ManagedApplicationTypeDef",
    {
        "applicationId": str,
        "runtime": Literal["MicroFocus"],
    },
)
_OptionalM2ManagedApplicationTypeDef = TypedDict(
    "_OptionalM2ManagedApplicationTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": str,
    },
    total=False,
)

class M2ManagedApplicationTypeDef(
    _RequiredM2ManagedApplicationTypeDef, _OptionalM2ManagedApplicationTypeDef
):
    pass

M2NonManagedApplicationActionTypeDef = TypedDict(
    "M2NonManagedApplicationActionTypeDef",
    {
        "resource": str,
        "actionType": M2NonManagedActionTypeType,
    },
)

_RequiredM2NonManagedApplicationStepInputTypeDef = TypedDict(
    "_RequiredM2NonManagedApplicationStepInputTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": int,
        "runtime": Literal["BluAge"],
        "actionType": M2NonManagedActionTypeType,
    },
)
_OptionalM2NonManagedApplicationStepInputTypeDef = TypedDict(
    "_OptionalM2NonManagedApplicationStepInputTypeDef",
    {
        "webAppName": str,
    },
    total=False,
)

class M2NonManagedApplicationStepInputTypeDef(
    _RequiredM2NonManagedApplicationStepInputTypeDef,
    _OptionalM2NonManagedApplicationStepInputTypeDef,
):
    pass

_RequiredM2NonManagedApplicationStepSummaryTypeDef = TypedDict(
    "_RequiredM2NonManagedApplicationStepSummaryTypeDef",
    {
        "stepInput": "M2NonManagedApplicationStepInputTypeDef",
    },
)
_OptionalM2NonManagedApplicationStepSummaryTypeDef = TypedDict(
    "_OptionalM2NonManagedApplicationStepSummaryTypeDef",
    {
        "stepOutput": Dict[str, Any],
    },
    total=False,
)

class M2NonManagedApplicationStepSummaryTypeDef(
    _RequiredM2NonManagedApplicationStepSummaryTypeDef,
    _OptionalM2NonManagedApplicationStepSummaryTypeDef,
):
    pass

_RequiredM2NonManagedApplicationSummaryTypeDef = TypedDict(
    "_RequiredM2NonManagedApplicationSummaryTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": int,
        "runtime": Literal["BluAge"],
    },
)
_OptionalM2NonManagedApplicationSummaryTypeDef = TypedDict(
    "_OptionalM2NonManagedApplicationSummaryTypeDef",
    {
        "webAppName": str,
    },
    total=False,
)

class M2NonManagedApplicationSummaryTypeDef(
    _RequiredM2NonManagedApplicationSummaryTypeDef, _OptionalM2NonManagedApplicationSummaryTypeDef
):
    pass

_RequiredM2NonManagedApplicationTypeDef = TypedDict(
    "_RequiredM2NonManagedApplicationTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": str,
        "runtime": Literal["BluAge"],
    },
)
_OptionalM2NonManagedApplicationTypeDef = TypedDict(
    "_OptionalM2NonManagedApplicationTypeDef",
    {
        "webAppName": str,
    },
    total=False,
)

class M2NonManagedApplicationTypeDef(
    _RequiredM2NonManagedApplicationTypeDef, _OptionalM2NonManagedApplicationTypeDef
):
    pass

MainframeActionPropertiesTypeDef = TypedDict(
    "MainframeActionPropertiesTypeDef",
    {
        "dmsTaskArn": str,
    },
    total=False,
)

MainframeActionSummaryTypeDef = TypedDict(
    "MainframeActionSummaryTypeDef",
    {
        "batch": "BatchSummaryTypeDef",
        "tn3270": "TN3270SummaryTypeDef",
    },
    total=False,
)

_RequiredMainframeActionTypeDef = TypedDict(
    "_RequiredMainframeActionTypeDef",
    {
        "resource": str,
        "actionType": "MainframeActionTypeTypeDef",
    },
)
_OptionalMainframeActionTypeDef = TypedDict(
    "_OptionalMainframeActionTypeDef",
    {
        "properties": "MainframeActionPropertiesTypeDef",
    },
    total=False,
)

class MainframeActionTypeDef(_RequiredMainframeActionTypeDef, _OptionalMainframeActionTypeDef):
    pass

MainframeActionTypeTypeDef = TypedDict(
    "MainframeActionTypeTypeDef",
    {
        "batch": "BatchTypeDef",
        "tn3270": "TN3270TypeDef",
    },
    total=False,
)

MainframeResourceSummaryTypeDef = TypedDict(
    "MainframeResourceSummaryTypeDef",
    {
        "m2ManagedApplication": "M2ManagedApplicationSummaryTypeDef",
        "m2NonManagedApplication": "M2NonManagedApplicationSummaryTypeDef",
    },
    total=False,
)

OutputFileTypeDef = TypedDict(
    "OutputFileTypeDef",
    {
        "fileLocation": str,
    },
    total=False,
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "file": "OutputFileTypeDef",
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

ResourceActionSummaryTypeDef = TypedDict(
    "ResourceActionSummaryTypeDef",
    {
        "cloudFormation": "CloudFormationStepSummaryTypeDef",
        "m2ManagedApplication": "M2ManagedApplicationStepSummaryTypeDef",
        "m2NonManagedApplication": "M2NonManagedApplicationStepSummaryTypeDef",
    },
    total=False,
)

ResourceActionTypeDef = TypedDict(
    "ResourceActionTypeDef",
    {
        "m2ManagedApplicationAction": "M2ManagedApplicationActionTypeDef",
        "m2NonManagedApplicationAction": "M2NonManagedApplicationActionTypeDef",
        "cloudFormationAction": "CloudFormationActionTypeDef",
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": "ResourceTypeTypeDef",
    },
)

ResourceTypeTypeDef = TypedDict(
    "ResourceTypeTypeDef",
    {
        "cloudFormation": "CloudFormationTypeDef",
        "m2ManagedApplication": "M2ManagedApplicationTypeDef",
        "m2NonManagedApplication": "M2NonManagedApplicationTypeDef",
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

ScriptSummaryTypeDef = TypedDict(
    "ScriptSummaryTypeDef",
    {
        "scriptLocation": str,
        "type": Literal["Selenium"],
    },
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "scriptLocation": str,
        "type": Literal["Selenium"],
    },
)

ServiceSettingsTypeDef = TypedDict(
    "ServiceSettingsTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

SourceDatabaseMetadataTypeDef = TypedDict(
    "SourceDatabaseMetadataTypeDef",
    {
        "type": Literal["z/OS-DB2"],
        "captureTool": CaptureToolType,
    },
)

_RequiredStartTestRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestRunRequestRequestTypeDef",
    {
        "testSuiteId": str,
    },
)
_OptionalStartTestRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestRunRequestRequestTypeDef",
    {
        "testConfigurationId": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartTestRunRequestRequestTypeDef(
    _RequiredStartTestRunRequestRequestTypeDef, _OptionalStartTestRunRequestRequestTypeDef
):
    pass

StartTestRunResponseTypeDef = TypedDict(
    "StartTestRunResponseTypeDef",
    {
        "testRunId": str,
        "testRunStatus": TestRunStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepActionTypeDef = TypedDict(
    "StepActionTypeDef",
    {
        "resourceAction": "ResourceActionTypeDef",
        "mainframeAction": "MainframeActionTypeDef",
        "compareAction": "CompareActionTypeDef",
    },
    total=False,
)

StepRunSummaryTypeDef = TypedDict(
    "StepRunSummaryTypeDef",
    {
        "mainframeAction": "MainframeActionSummaryTypeDef",
        "compareAction": "CompareActionSummaryTypeDef",
        "resourceAction": "ResourceActionSummaryTypeDef",
    },
    total=False,
)

_RequiredStepTypeDef = TypedDict(
    "_RequiredStepTypeDef",
    {
        "name": str,
        "action": "StepActionTypeDef",
    },
)
_OptionalStepTypeDef = TypedDict(
    "_OptionalStepTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StepTypeDef(_RequiredStepTypeDef, _OptionalStepTypeDef):
    pass

_RequiredTN3270StepInputTypeDef = TypedDict(
    "_RequiredTN3270StepInputTypeDef",
    {
        "resource": "MainframeResourceSummaryTypeDef",
        "script": "ScriptSummaryTypeDef",
    },
)
_OptionalTN3270StepInputTypeDef = TypedDict(
    "_OptionalTN3270StepInputTypeDef",
    {
        "exportDataSetNames": List[str],
        "properties": "MainframeActionPropertiesTypeDef",
    },
    total=False,
)

class TN3270StepInputTypeDef(_RequiredTN3270StepInputTypeDef, _OptionalTN3270StepInputTypeDef):
    pass

_RequiredTN3270StepOutputTypeDef = TypedDict(
    "_RequiredTN3270StepOutputTypeDef",
    {
        "scriptOutputLocation": str,
    },
)
_OptionalTN3270StepOutputTypeDef = TypedDict(
    "_OptionalTN3270StepOutputTypeDef",
    {
        "dataSetExportLocation": str,
        "dmsOutputLocation": str,
        "dataSetDetails": List["DataSetTypeDef"],
    },
    total=False,
)

class TN3270StepOutputTypeDef(_RequiredTN3270StepOutputTypeDef, _OptionalTN3270StepOutputTypeDef):
    pass

_RequiredTN3270SummaryTypeDef = TypedDict(
    "_RequiredTN3270SummaryTypeDef",
    {
        "stepInput": "TN3270StepInputTypeDef",
    },
)
_OptionalTN3270SummaryTypeDef = TypedDict(
    "_OptionalTN3270SummaryTypeDef",
    {
        "stepOutput": "TN3270StepOutputTypeDef",
    },
    total=False,
)

class TN3270SummaryTypeDef(_RequiredTN3270SummaryTypeDef, _OptionalTN3270SummaryTypeDef):
    pass

_RequiredTN3270TypeDef = TypedDict(
    "_RequiredTN3270TypeDef",
    {
        "script": "ScriptTypeDef",
    },
)
_OptionalTN3270TypeDef = TypedDict(
    "_OptionalTN3270TypeDef",
    {
        "exportDataSetNames": List[str],
    },
    total=False,
)

class TN3270TypeDef(_RequiredTN3270TypeDef, _OptionalTN3270TypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetDatabaseMetadataTypeDef = TypedDict(
    "TargetDatabaseMetadataTypeDef",
    {
        "type": Literal["PostgreSQL"],
        "captureTool": CaptureToolType,
    },
)

_RequiredTestCaseLatestVersionTypeDef = TypedDict(
    "_RequiredTestCaseLatestVersionTypeDef",
    {
        "version": int,
        "status": TestCaseLifecycleType,
    },
)
_OptionalTestCaseLatestVersionTypeDef = TypedDict(
    "_OptionalTestCaseLatestVersionTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestCaseLatestVersionTypeDef(
    _RequiredTestCaseLatestVersionTypeDef, _OptionalTestCaseLatestVersionTypeDef
):
    pass

_RequiredTestCaseRunSummaryTypeDef = TypedDict(
    "_RequiredTestCaseRunSummaryTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "testRunId": str,
        "status": TestCaseRunStatusType,
        "runStartTime": datetime,
    },
)
_OptionalTestCaseRunSummaryTypeDef = TypedDict(
    "_OptionalTestCaseRunSummaryTypeDef",
    {
        "statusReason": str,
        "runEndTime": datetime,
    },
    total=False,
)

class TestCaseRunSummaryTypeDef(
    _RequiredTestCaseRunSummaryTypeDef, _OptionalTestCaseRunSummaryTypeDef
):
    pass

_RequiredTestCaseSummaryTypeDef = TypedDict(
    "_RequiredTestCaseSummaryTypeDef",
    {
        "testCaseId": str,
        "testCaseArn": str,
        "name": str,
        "latestVersion": int,
        "status": TestCaseLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
)
_OptionalTestCaseSummaryTypeDef = TypedDict(
    "_OptionalTestCaseSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestCaseSummaryTypeDef(_RequiredTestCaseSummaryTypeDef, _OptionalTestCaseSummaryTypeDef):
    pass

TestCasesTypeDef = TypedDict(
    "TestCasesTypeDef",
    {
        "sequential": List[str],
    },
    total=False,
)

_RequiredTestConfigurationLatestVersionTypeDef = TypedDict(
    "_RequiredTestConfigurationLatestVersionTypeDef",
    {
        "version": int,
        "status": TestConfigurationLifecycleType,
    },
)
_OptionalTestConfigurationLatestVersionTypeDef = TypedDict(
    "_OptionalTestConfigurationLatestVersionTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestConfigurationLatestVersionTypeDef(
    _RequiredTestConfigurationLatestVersionTypeDef, _OptionalTestConfigurationLatestVersionTypeDef
):
    pass

_RequiredTestConfigurationSummaryTypeDef = TypedDict(
    "_RequiredTestConfigurationSummaryTypeDef",
    {
        "testConfigurationId": str,
        "name": str,
        "latestVersion": int,
        "testConfigurationArn": str,
        "status": TestConfigurationLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
)
_OptionalTestConfigurationSummaryTypeDef = TypedDict(
    "_OptionalTestConfigurationSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestConfigurationSummaryTypeDef(
    _RequiredTestConfigurationSummaryTypeDef, _OptionalTestConfigurationSummaryTypeDef
):
    pass

_RequiredTestRunStepSummaryTypeDef = TypedDict(
    "_RequiredTestRunStepSummaryTypeDef",
    {
        "stepName": str,
        "testRunId": str,
        "status": StepRunStatusType,
        "runStartTime": datetime,
    },
)
_OptionalTestRunStepSummaryTypeDef = TypedDict(
    "_OptionalTestRunStepSummaryTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "testSuiteId": str,
        "testSuiteVersion": int,
        "beforeStep": bool,
        "afterStep": bool,
        "statusReason": str,
        "runEndTime": datetime,
    },
    total=False,
)

class TestRunStepSummaryTypeDef(
    _RequiredTestRunStepSummaryTypeDef, _OptionalTestRunStepSummaryTypeDef
):
    pass

_RequiredTestRunSummaryTypeDef = TypedDict(
    "_RequiredTestRunSummaryTypeDef",
    {
        "testRunId": str,
        "testRunArn": str,
        "testSuiteId": str,
        "testSuiteVersion": int,
        "status": TestRunStatusType,
        "runStartTime": datetime,
    },
)
_OptionalTestRunSummaryTypeDef = TypedDict(
    "_OptionalTestRunSummaryTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": int,
        "statusReason": str,
        "runEndTime": datetime,
    },
    total=False,
)

class TestRunSummaryTypeDef(_RequiredTestRunSummaryTypeDef, _OptionalTestRunSummaryTypeDef):
    pass

_RequiredTestSuiteLatestVersionTypeDef = TypedDict(
    "_RequiredTestSuiteLatestVersionTypeDef",
    {
        "version": int,
        "status": TestSuiteLifecycleType,
    },
)
_OptionalTestSuiteLatestVersionTypeDef = TypedDict(
    "_OptionalTestSuiteLatestVersionTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestSuiteLatestVersionTypeDef(
    _RequiredTestSuiteLatestVersionTypeDef, _OptionalTestSuiteLatestVersionTypeDef
):
    pass

_RequiredTestSuiteSummaryTypeDef = TypedDict(
    "_RequiredTestSuiteSummaryTypeDef",
    {
        "testSuiteId": str,
        "name": str,
        "latestVersion": int,
        "testSuiteArn": str,
        "status": TestSuiteLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
)
_OptionalTestSuiteSummaryTypeDef = TypedDict(
    "_OptionalTestSuiteSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class TestSuiteSummaryTypeDef(_RequiredTestSuiteSummaryTypeDef, _OptionalTestSuiteSummaryTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateTestCaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
    },
)
_OptionalUpdateTestCaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestCaseRequestRequestTypeDef",
    {
        "description": str,
        "steps": List["StepTypeDef"],
    },
    total=False,
)

class UpdateTestCaseRequestRequestTypeDef(
    _RequiredUpdateTestCaseRequestRequestTypeDef, _OptionalUpdateTestCaseRequestRequestTypeDef
):
    pass

UpdateTestCaseResponseTypeDef = TypedDict(
    "UpdateTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
    },
)
_OptionalUpdateTestConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "resources": List["ResourceTypeDef"],
        "properties": Dict[str, str],
        "serviceSettings": "ServiceSettingsTypeDef",
    },
    total=False,
)

class UpdateTestConfigurationRequestRequestTypeDef(
    _RequiredUpdateTestConfigurationRequestRequestTypeDef,
    _OptionalUpdateTestConfigurationRequestRequestTypeDef,
):
    pass

UpdateTestConfigurationResponseTypeDef = TypedDict(
    "UpdateTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestSuiteRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
    },
)
_OptionalUpdateTestSuiteRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestSuiteRequestRequestTypeDef",
    {
        "description": str,
        "beforeSteps": List["StepTypeDef"],
        "afterSteps": List["StepTypeDef"],
        "testCases": "TestCasesTypeDef",
    },
    total=False,
)

class UpdateTestSuiteRequestRequestTypeDef(
    _RequiredUpdateTestSuiteRequestRequestTypeDef, _OptionalUpdateTestSuiteRequestRequestTypeDef
):
    pass

UpdateTestSuiteResponseTypeDef = TypedDict(
    "UpdateTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "testSuiteVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
