"""
Type annotations for apptest service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_apptest.type_defs import BatchOutputTypeDef

    data: BatchOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

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
    "BatchOutputTypeDef",
    "BatchStepInputTypeDef",
    "BatchStepOutputTypeDef",
    "BatchSummaryTypeDef",
    "BatchTypeDef",
    "BatchUnionTypeDef",
    "CloudFormationActionTypeDef",
    "CloudFormationOutputTypeDef",
    "CloudFormationStepSummaryTypeDef",
    "CloudFormationTypeDef",
    "CloudFormationUnionTypeDef",
    "CompareActionOutputTypeDef",
    "CompareActionSummaryTypeDef",
    "CompareActionTypeDef",
    "CompareActionUnionTypeDef",
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
    "CreateTestCaseRequestTypeDef",
    "CreateTestCaseResponseTypeDef",
    "CreateTestConfigurationRequestTypeDef",
    "CreateTestConfigurationResponseTypeDef",
    "CreateTestSuiteRequestTypeDef",
    "CreateTestSuiteResponseTypeDef",
    "DataSetTypeDef",
    "DatabaseCDCTypeDef",
    "DeleteCloudFormationStepInputTypeDef",
    "DeleteCloudFormationSummaryTypeDef",
    "DeleteTestCaseRequestTypeDef",
    "DeleteTestConfigurationRequestTypeDef",
    "DeleteTestRunRequestTypeDef",
    "DeleteTestSuiteRequestTypeDef",
    "FileMetadataOutputTypeDef",
    "FileMetadataTypeDef",
    "FileMetadataUnionTypeDef",
    "FileTypeDef",
    "GetTestCaseRequestTypeDef",
    "GetTestCaseResponseTypeDef",
    "GetTestConfigurationRequestTypeDef",
    "GetTestConfigurationResponseTypeDef",
    "GetTestRunStepRequestTypeDef",
    "GetTestRunStepResponseTypeDef",
    "GetTestSuiteRequestTypeDef",
    "GetTestSuiteResponseTypeDef",
    "InputFileOutputTypeDef",
    "InputFileTypeDef",
    "InputFileUnionTypeDef",
    "InputOutputTypeDef",
    "InputTypeDef",
    "InputUnionTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestCasesRequestPaginateTypeDef",
    "ListTestCasesRequestTypeDef",
    "ListTestCasesResponseTypeDef",
    "ListTestConfigurationsRequestPaginateTypeDef",
    "ListTestConfigurationsRequestTypeDef",
    "ListTestConfigurationsResponseTypeDef",
    "ListTestRunStepsRequestPaginateTypeDef",
    "ListTestRunStepsRequestTypeDef",
    "ListTestRunStepsResponseTypeDef",
    "ListTestRunTestCasesRequestPaginateTypeDef",
    "ListTestRunTestCasesRequestTypeDef",
    "ListTestRunTestCasesResponseTypeDef",
    "ListTestRunsRequestPaginateTypeDef",
    "ListTestRunsRequestTypeDef",
    "ListTestRunsResponseTypeDef",
    "ListTestSuitesRequestPaginateTypeDef",
    "ListTestSuitesRequestTypeDef",
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
    "MainframeActionOutputTypeDef",
    "MainframeActionPropertiesTypeDef",
    "MainframeActionSummaryTypeDef",
    "MainframeActionTypeDef",
    "MainframeActionTypeOutputTypeDef",
    "MainframeActionTypeTypeDef",
    "MainframeActionTypeUnionTypeDef",
    "MainframeActionUnionTypeDef",
    "MainframeResourceSummaryTypeDef",
    "OutputFileTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceActionSummaryTypeDef",
    "ResourceActionTypeDef",
    "ResourceOutputTypeDef",
    "ResourceTypeDef",
    "ResourceTypeOutputTypeDef",
    "ResourceTypeTypeDef",
    "ResourceTypeUnionTypeDef",
    "ResourceUnionTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptSummaryTypeDef",
    "ScriptTypeDef",
    "ServiceSettingsTypeDef",
    "SourceDatabaseMetadataTypeDef",
    "StartTestRunRequestTypeDef",
    "StartTestRunResponseTypeDef",
    "StepActionOutputTypeDef",
    "StepActionTypeDef",
    "StepActionUnionTypeDef",
    "StepOutputTypeDef",
    "StepRunSummaryTypeDef",
    "StepTypeDef",
    "StepUnionTypeDef",
    "TN3270OutputTypeDef",
    "TN3270StepInputTypeDef",
    "TN3270StepOutputTypeDef",
    "TN3270SummaryTypeDef",
    "TN3270TypeDef",
    "TN3270UnionTypeDef",
    "TagResourceRequestTypeDef",
    "TargetDatabaseMetadataTypeDef",
    "TestCaseLatestVersionTypeDef",
    "TestCaseRunSummaryTypeDef",
    "TestCaseSummaryTypeDef",
    "TestCasesOutputTypeDef",
    "TestCasesTypeDef",
    "TestCasesUnionTypeDef",
    "TestConfigurationLatestVersionTypeDef",
    "TestConfigurationSummaryTypeDef",
    "TestRunStepSummaryTypeDef",
    "TestRunSummaryTypeDef",
    "TestSuiteLatestVersionTypeDef",
    "TestSuiteSummaryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateTestCaseRequestTypeDef",
    "UpdateTestCaseResponseTypeDef",
    "UpdateTestConfigurationRequestTypeDef",
    "UpdateTestConfigurationResponseTypeDef",
    "UpdateTestSuiteRequestTypeDef",
    "UpdateTestSuiteResponseTypeDef",
)

class BatchOutputTypeDef(TypedDict):
    batchJobName: str
    batchJobParameters: NotRequired[Dict[str, str]]
    exportDataSetNames: NotRequired[List[str]]

class MainframeActionPropertiesTypeDef(TypedDict):
    dmsTaskArn: NotRequired[str]

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

class BatchTypeDef(TypedDict):
    batchJobName: str
    batchJobParameters: NotRequired[Mapping[str, str]]
    exportDataSetNames: NotRequired[Sequence[str]]

class CloudFormationActionTypeDef(TypedDict):
    resource: str
    actionType: NotRequired[CloudFormationActionTypeType]

class CloudFormationOutputTypeDef(TypedDict):
    templateLocation: str
    parameters: NotRequired[Dict[str, str]]

class CloudFormationTypeDef(TypedDict):
    templateLocation: str
    parameters: NotRequired[Mapping[str, str]]

class CompareDataSetsStepOutputTypeDef(TypedDict):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType

SourceDatabaseMetadataTypeDef = TypedDict(
    "SourceDatabaseMetadataTypeDef",
    {
        "type": Literal["z/OS-DB2"],
        "captureTool": CaptureToolType,
    },
)
TargetDatabaseMetadataTypeDef = TypedDict(
    "TargetDatabaseMetadataTypeDef",
    {
        "type": Literal["PostgreSQL"],
        "captureTool": CaptureToolType,
    },
)

class CompareDatabaseCDCStepOutputTypeDef(TypedDict):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType

class CreateCloudFormationStepInputTypeDef(TypedDict):
    templateLocation: str
    parameters: NotRequired[Dict[str, str]]

class CreateCloudFormationStepOutputTypeDef(TypedDict):
    stackId: str
    exports: NotRequired[Dict[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ServiceSettingsTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]

class DeleteCloudFormationStepInputTypeDef(TypedDict):
    stackId: str

class DeleteTestCaseRequestTypeDef(TypedDict):
    testCaseId: str

class DeleteTestConfigurationRequestTypeDef(TypedDict):
    testConfigurationId: str

class DeleteTestRunRequestTypeDef(TypedDict):
    testRunId: str

class DeleteTestSuiteRequestTypeDef(TypedDict):
    testSuiteId: str

class GetTestCaseRequestTypeDef(TypedDict):
    testCaseId: str
    testCaseVersion: NotRequired[int]

class TestCaseLatestVersionTypeDef(TypedDict):
    version: int
    status: TestCaseLifecycleType
    statusReason: NotRequired[str]

class GetTestConfigurationRequestTypeDef(TypedDict):
    testConfigurationId: str
    testConfigurationVersion: NotRequired[int]

class TestConfigurationLatestVersionTypeDef(TypedDict):
    version: int
    status: TestConfigurationLifecycleType
    statusReason: NotRequired[str]

class GetTestRunStepRequestTypeDef(TypedDict):
    testRunId: str
    stepName: str
    testCaseId: NotRequired[str]
    testSuiteId: NotRequired[str]

class GetTestSuiteRequestTypeDef(TypedDict):
    testSuiteId: str
    testSuiteVersion: NotRequired[int]

class TestCasesOutputTypeDef(TypedDict):
    sequential: NotRequired[List[str]]

class TestSuiteLatestVersionTypeDef(TypedDict):
    version: int
    status: TestSuiteLifecycleType
    statusReason: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTestCasesRequestTypeDef(TypedDict):
    testCaseIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestCaseSummaryTypeDef(TypedDict):
    testCaseId: str
    testCaseArn: str
    name: str
    latestVersion: int
    status: TestCaseLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: NotRequired[str]

class ListTestConfigurationsRequestTypeDef(TypedDict):
    testConfigurationIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestConfigurationSummaryTypeDef(TypedDict):
    testConfigurationId: str
    name: str
    latestVersion: int
    testConfigurationArn: str
    status: TestConfigurationLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: NotRequired[str]

class ListTestRunStepsRequestTypeDef(TypedDict):
    testRunId: str
    testCaseId: NotRequired[str]
    testSuiteId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestRunStepSummaryTypeDef(TypedDict):
    stepName: str
    testRunId: str
    status: StepRunStatusType
    runStartTime: datetime
    testCaseId: NotRequired[str]
    testCaseVersion: NotRequired[int]
    testSuiteId: NotRequired[str]
    testSuiteVersion: NotRequired[int]
    beforeStep: NotRequired[bool]
    afterStep: NotRequired[bool]
    statusReason: NotRequired[str]
    runEndTime: NotRequired[datetime]

class ListTestRunTestCasesRequestTypeDef(TypedDict):
    testRunId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestCaseRunSummaryTypeDef(TypedDict):
    testCaseId: str
    testCaseVersion: int
    testRunId: str
    status: TestCaseRunStatusType
    runStartTime: datetime
    statusReason: NotRequired[str]
    runEndTime: NotRequired[datetime]

class ListTestRunsRequestTypeDef(TypedDict):
    testSuiteId: NotRequired[str]
    testRunIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestRunSummaryTypeDef(TypedDict):
    testRunId: str
    testRunArn: str
    testSuiteId: str
    testSuiteVersion: int
    status: TestRunStatusType
    runStartTime: datetime
    testConfigurationId: NotRequired[str]
    testConfigurationVersion: NotRequired[int]
    statusReason: NotRequired[str]
    runEndTime: NotRequired[datetime]

class ListTestSuitesRequestTypeDef(TypedDict):
    testSuiteIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TestSuiteSummaryTypeDef(TypedDict):
    testSuiteId: str
    name: str
    latestVersion: int
    testSuiteArn: str
    status: TestSuiteLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: NotRequired[str]

class M2ManagedActionPropertiesTypeDef(TypedDict):
    forceStop: NotRequired[bool]
    importDataSetLocation: NotRequired[str]

class M2ManagedApplicationStepOutputTypeDef(TypedDict):
    importDataSetSummary: NotRequired[Dict[str, str]]

class M2ManagedApplicationSummaryTypeDef(TypedDict):
    applicationId: str
    runtime: Literal["MicroFocus"]
    listenerPort: NotRequired[int]

class M2ManagedApplicationTypeDef(TypedDict):
    applicationId: str
    runtime: Literal["MicroFocus"]
    vpcEndpointServiceName: NotRequired[str]
    listenerPort: NotRequired[str]

class M2NonManagedApplicationActionTypeDef(TypedDict):
    resource: str
    actionType: M2NonManagedActionTypeType

class M2NonManagedApplicationStepInputTypeDef(TypedDict):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    actionType: M2NonManagedActionTypeType
    webAppName: NotRequired[str]

class M2NonManagedApplicationSummaryTypeDef(TypedDict):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    webAppName: NotRequired[str]

class M2NonManagedApplicationTypeDef(TypedDict):
    vpcEndpointServiceName: str
    listenerPort: str
    runtime: Literal["BluAge"]
    webAppName: NotRequired[str]

class OutputFileTypeDef(TypedDict):
    fileLocation: NotRequired[str]

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

class StartTestRunRequestTypeDef(TypedDict):
    testSuiteId: str
    testConfigurationId: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TestCasesTypeDef(TypedDict):
    sequential: NotRequired[Sequence[str]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchStepOutputTypeDef(TypedDict):
    dataSetExportLocation: NotRequired[str]
    dmsOutputLocation: NotRequired[str]
    dataSetDetails: NotRequired[List[DataSetTypeDef]]

class CompareDataSetsStepInputTypeDef(TypedDict):
    sourceLocation: str
    targetLocation: str
    sourceDataSets: List[DataSetTypeDef]
    targetDataSets: List[DataSetTypeDef]

class TN3270StepOutputTypeDef(TypedDict):
    scriptOutputLocation: str
    dataSetExportLocation: NotRequired[str]
    dmsOutputLocation: NotRequired[str]
    dataSetDetails: NotRequired[List[DataSetTypeDef]]

BatchUnionTypeDef = Union[BatchTypeDef, BatchOutputTypeDef]
CloudFormationUnionTypeDef = Union[CloudFormationTypeDef, CloudFormationOutputTypeDef]

class CompareDatabaseCDCStepInputTypeDef(TypedDict):
    sourceLocation: str
    targetLocation: str
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef
    outputLocation: NotRequired[str]

class DatabaseCDCTypeDef(TypedDict):
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef

class CreateCloudFormationSummaryTypeDef(TypedDict):
    stepInput: CreateCloudFormationStepInputTypeDef
    stepOutput: NotRequired[CreateCloudFormationStepOutputTypeDef]

class CreateTestCaseResponseTypeDef(TypedDict):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestConfigurationResponseTypeDef(TypedDict):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestSuiteResponseTypeDef(TypedDict):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestRunResponseTypeDef(TypedDict):
    testRunId: str
    testRunStatus: TestRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestCaseResponseTypeDef(TypedDict):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestConfigurationResponseTypeDef(TypedDict):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestSuiteResponseTypeDef(TypedDict):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCloudFormationSummaryTypeDef(TypedDict):
    stepInput: DeleteCloudFormationStepInputTypeDef
    stepOutput: NotRequired[Dict[str, Any]]

class ListTestCasesRequestPaginateTypeDef(TypedDict):
    testCaseIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestConfigurationsRequestPaginateTypeDef(TypedDict):
    testConfigurationIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestRunStepsRequestPaginateTypeDef(TypedDict):
    testRunId: str
    testCaseId: NotRequired[str]
    testSuiteId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestRunTestCasesRequestPaginateTypeDef(TypedDict):
    testRunId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestRunsRequestPaginateTypeDef(TypedDict):
    testSuiteId: NotRequired[str]
    testRunIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestSuitesRequestPaginateTypeDef(TypedDict):
    testSuiteIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestCasesResponseTypeDef(TypedDict):
    testCases: List[TestCaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestConfigurationsResponseTypeDef(TypedDict):
    testConfigurations: List[TestConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestRunStepsResponseTypeDef(TypedDict):
    testRunSteps: List[TestRunStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestRunTestCasesResponseTypeDef(TypedDict):
    testRunTestCases: List[TestCaseRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestRunsResponseTypeDef(TypedDict):
    testRuns: List[TestRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestSuitesResponseTypeDef(TypedDict):
    testSuites: List[TestSuiteSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class M2ManagedApplicationActionTypeDef(TypedDict):
    resource: str
    actionType: M2ManagedActionTypeType
    properties: NotRequired[M2ManagedActionPropertiesTypeDef]

class M2ManagedApplicationStepInputTypeDef(TypedDict):
    applicationId: str
    runtime: str
    actionType: M2ManagedActionTypeType
    vpcEndpointServiceName: NotRequired[str]
    listenerPort: NotRequired[int]
    properties: NotRequired[M2ManagedActionPropertiesTypeDef]

class M2NonManagedApplicationStepSummaryTypeDef(TypedDict):
    stepInput: M2NonManagedApplicationStepInputTypeDef
    stepOutput: NotRequired[Dict[str, Any]]

class MainframeResourceSummaryTypeDef(TypedDict):
    m2ManagedApplication: NotRequired[M2ManagedApplicationSummaryTypeDef]
    m2NonManagedApplication: NotRequired[M2NonManagedApplicationSummaryTypeDef]

class ResourceTypeOutputTypeDef(TypedDict):
    cloudFormation: NotRequired[CloudFormationOutputTypeDef]
    m2ManagedApplication: NotRequired[M2ManagedApplicationTypeDef]
    m2NonManagedApplication: NotRequired[M2NonManagedApplicationTypeDef]

class OutputTypeDef(TypedDict):
    file: NotRequired[OutputFileTypeDef]

class TN3270OutputTypeDef(TypedDict):
    script: ScriptTypeDef
    exportDataSetNames: NotRequired[List[str]]

class TN3270TypeDef(TypedDict):
    script: ScriptTypeDef
    exportDataSetNames: NotRequired[Sequence[str]]

TestCasesUnionTypeDef = Union[TestCasesTypeDef, TestCasesOutputTypeDef]

class CompareDataSetsSummaryTypeDef(TypedDict):
    stepInput: CompareDataSetsStepInputTypeDef
    stepOutput: NotRequired[CompareDataSetsStepOutputTypeDef]

class ResourceTypeTypeDef(TypedDict):
    cloudFormation: NotRequired[CloudFormationUnionTypeDef]
    m2ManagedApplication: NotRequired[M2ManagedApplicationTypeDef]
    m2NonManagedApplication: NotRequired[M2NonManagedApplicationTypeDef]

class CompareDatabaseCDCSummaryTypeDef(TypedDict):
    stepInput: CompareDatabaseCDCStepInputTypeDef
    stepOutput: NotRequired[CompareDatabaseCDCStepOutputTypeDef]

class FileMetadataOutputTypeDef(TypedDict):
    dataSets: NotRequired[List[DataSetTypeDef]]
    databaseCDC: NotRequired[DatabaseCDCTypeDef]

class FileMetadataTypeDef(TypedDict):
    dataSets: NotRequired[Sequence[DataSetTypeDef]]
    databaseCDC: NotRequired[DatabaseCDCTypeDef]

class CloudFormationStepSummaryTypeDef(TypedDict):
    createCloudformation: NotRequired[CreateCloudFormationSummaryTypeDef]
    deleteCloudformation: NotRequired[DeleteCloudFormationSummaryTypeDef]

class ResourceActionTypeDef(TypedDict):
    m2ManagedApplicationAction: NotRequired[M2ManagedApplicationActionTypeDef]
    m2NonManagedApplicationAction: NotRequired[M2NonManagedApplicationActionTypeDef]
    cloudFormationAction: NotRequired[CloudFormationActionTypeDef]

class M2ManagedApplicationStepSummaryTypeDef(TypedDict):
    stepInput: M2ManagedApplicationStepInputTypeDef
    stepOutput: NotRequired[M2ManagedApplicationStepOutputTypeDef]

class BatchStepInputTypeDef(TypedDict):
    resource: MainframeResourceSummaryTypeDef
    batchJobName: str
    batchJobParameters: NotRequired[Dict[str, str]]
    exportDataSetNames: NotRequired[List[str]]
    properties: NotRequired[MainframeActionPropertiesTypeDef]

class TN3270StepInputTypeDef(TypedDict):
    resource: MainframeResourceSummaryTypeDef
    script: ScriptSummaryTypeDef
    exportDataSetNames: NotRequired[List[str]]
    properties: NotRequired[MainframeActionPropertiesTypeDef]

ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "name": str,
        "type": ResourceTypeOutputTypeDef,
    },
)

class MainframeActionTypeOutputTypeDef(TypedDict):
    batch: NotRequired[BatchOutputTypeDef]
    tn3270: NotRequired[TN3270OutputTypeDef]

TN3270UnionTypeDef = Union[TN3270TypeDef, TN3270OutputTypeDef]
ResourceTypeUnionTypeDef = Union[ResourceTypeTypeDef, ResourceTypeOutputTypeDef]

class CompareFileTypeTypeDef(TypedDict):
    datasets: NotRequired[CompareDataSetsSummaryTypeDef]
    databaseCDC: NotRequired[CompareDatabaseCDCSummaryTypeDef]

class InputFileOutputTypeDef(TypedDict):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataOutputTypeDef

FileMetadataUnionTypeDef = Union[FileMetadataTypeDef, FileMetadataOutputTypeDef]

class ResourceActionSummaryTypeDef(TypedDict):
    cloudFormation: NotRequired[CloudFormationStepSummaryTypeDef]
    m2ManagedApplication: NotRequired[M2ManagedApplicationStepSummaryTypeDef]
    m2NonManagedApplication: NotRequired[M2NonManagedApplicationStepSummaryTypeDef]

class BatchSummaryTypeDef(TypedDict):
    stepInput: BatchStepInputTypeDef
    stepOutput: NotRequired[BatchStepOutputTypeDef]

class TN3270SummaryTypeDef(TypedDict):
    stepInput: TN3270StepInputTypeDef
    stepOutput: NotRequired[TN3270StepOutputTypeDef]

class GetTestConfigurationResponseTypeDef(TypedDict):
    testConfigurationId: str
    name: str
    testConfigurationArn: str
    latestVersion: TestConfigurationLatestVersionTypeDef
    testConfigurationVersion: int
    status: TestConfigurationLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    resources: List[ResourceOutputTypeDef]
    properties: Dict[str, str]
    tags: Dict[str, str]
    serviceSettings: ServiceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MainframeActionOutputTypeDef(TypedDict):
    resource: str
    actionType: MainframeActionTypeOutputTypeDef
    properties: NotRequired[MainframeActionPropertiesTypeDef]

class MainframeActionTypeTypeDef(TypedDict):
    batch: NotRequired[BatchUnionTypeDef]
    tn3270: NotRequired[TN3270UnionTypeDef]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": ResourceTypeUnionTypeDef,
    },
)

class FileTypeDef(TypedDict):
    fileType: NotRequired[CompareFileTypeTypeDef]

class InputOutputTypeDef(TypedDict):
    file: NotRequired[InputFileOutputTypeDef]

class InputFileTypeDef(TypedDict):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataUnionTypeDef

class MainframeActionSummaryTypeDef(TypedDict):
    batch: NotRequired[BatchSummaryTypeDef]
    tn3270: NotRequired[TN3270SummaryTypeDef]

MainframeActionTypeUnionTypeDef = Union[
    MainframeActionTypeTypeDef, MainframeActionTypeOutputTypeDef
]
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]
CompareActionSummaryTypeDef = TypedDict(
    "CompareActionSummaryTypeDef",
    {
        "type": FileTypeDef,
    },
)
CompareActionOutputTypeDef = TypedDict(
    "CompareActionOutputTypeDef",
    {
        "input": InputOutputTypeDef,
        "output": NotRequired[OutputTypeDef],
    },
)
InputFileUnionTypeDef = Union[InputFileTypeDef, InputFileOutputTypeDef]

class MainframeActionTypeDef(TypedDict):
    resource: str
    actionType: MainframeActionTypeUnionTypeDef
    properties: NotRequired[MainframeActionPropertiesTypeDef]

class CreateTestConfigurationRequestTypeDef(TypedDict):
    name: str
    resources: Sequence[ResourceUnionTypeDef]
    description: NotRequired[str]
    properties: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    serviceSettings: NotRequired[ServiceSettingsTypeDef]

class UpdateTestConfigurationRequestTypeDef(TypedDict):
    testConfigurationId: str
    description: NotRequired[str]
    resources: NotRequired[Sequence[ResourceUnionTypeDef]]
    properties: NotRequired[Mapping[str, str]]
    serviceSettings: NotRequired[ServiceSettingsTypeDef]

class StepRunSummaryTypeDef(TypedDict):
    mainframeAction: NotRequired[MainframeActionSummaryTypeDef]
    compareAction: NotRequired[CompareActionSummaryTypeDef]
    resourceAction: NotRequired[ResourceActionSummaryTypeDef]

class StepActionOutputTypeDef(TypedDict):
    resourceAction: NotRequired[ResourceActionTypeDef]
    mainframeAction: NotRequired[MainframeActionOutputTypeDef]
    compareAction: NotRequired[CompareActionOutputTypeDef]

class InputTypeDef(TypedDict):
    file: NotRequired[InputFileUnionTypeDef]

MainframeActionUnionTypeDef = Union[MainframeActionTypeDef, MainframeActionOutputTypeDef]

class GetTestRunStepResponseTypeDef(TypedDict):
    stepName: str
    testRunId: str
    testCaseId: str
    testCaseVersion: int
    testSuiteId: str
    testSuiteVersion: int
    beforeStep: bool
    afterStep: bool
    status: StepRunStatusType
    statusReason: str
    runStartTime: datetime
    runEndTime: datetime
    stepRunSummary: StepRunSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StepOutputTypeDef(TypedDict):
    name: str
    action: StepActionOutputTypeDef
    description: NotRequired[str]

InputUnionTypeDef = Union[InputTypeDef, InputOutputTypeDef]

class GetTestCaseResponseTypeDef(TypedDict):
    testCaseId: str
    testCaseArn: str
    name: str
    description: str
    latestVersion: TestCaseLatestVersionTypeDef
    testCaseVersion: int
    status: TestCaseLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    steps: List[StepOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestSuiteResponseTypeDef(TypedDict):
    testSuiteId: str
    name: str
    latestVersion: TestSuiteLatestVersionTypeDef
    testSuiteVersion: int
    status: TestSuiteLifecycleType
    statusReason: str
    testSuiteArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    beforeSteps: List[StepOutputTypeDef]
    afterSteps: List[StepOutputTypeDef]
    testCases: TestCasesOutputTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

CompareActionTypeDef = TypedDict(
    "CompareActionTypeDef",
    {
        "input": InputUnionTypeDef,
        "output": NotRequired[OutputTypeDef],
    },
)
CompareActionUnionTypeDef = Union[CompareActionTypeDef, CompareActionOutputTypeDef]

class StepActionTypeDef(TypedDict):
    resourceAction: NotRequired[ResourceActionTypeDef]
    mainframeAction: NotRequired[MainframeActionUnionTypeDef]
    compareAction: NotRequired[CompareActionUnionTypeDef]

StepActionUnionTypeDef = Union[StepActionTypeDef, StepActionOutputTypeDef]

class StepTypeDef(TypedDict):
    name: str
    action: StepActionUnionTypeDef
    description: NotRequired[str]

StepUnionTypeDef = Union[StepTypeDef, StepOutputTypeDef]

class CreateTestCaseRequestTypeDef(TypedDict):
    name: str
    steps: Sequence[StepUnionTypeDef]
    description: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateTestSuiteRequestTypeDef(TypedDict):
    name: str
    testCases: TestCasesUnionTypeDef
    description: NotRequired[str]
    beforeSteps: NotRequired[Sequence[StepUnionTypeDef]]
    afterSteps: NotRequired[Sequence[StepUnionTypeDef]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateTestCaseRequestTypeDef(TypedDict):
    testCaseId: str
    description: NotRequired[str]
    steps: NotRequired[Sequence[StepUnionTypeDef]]

class UpdateTestSuiteRequestTypeDef(TypedDict):
    testSuiteId: str
    description: NotRequired[str]
    beforeSteps: NotRequired[Sequence[StepUnionTypeDef]]
    afterSteps: NotRequired[Sequence[StepUnionTypeDef]]
    testCases: NotRequired[TestCasesUnionTypeDef]
