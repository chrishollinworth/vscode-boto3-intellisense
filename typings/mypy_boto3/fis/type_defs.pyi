"""
Type annotations for fis service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AccountTargetingType,
    ActionsModeType,
    EmptyTargetResolutionModeType,
    ExperimentActionStatusType,
    ExperimentReportStatusType,
    ExperimentStatusType,
    SafetyLeverStatusInputType,
    SafetyLeverStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionParameterTypeDef",
    "ActionSummaryTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateExperimentOptionsInputTypeDef",
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    "CreateExperimentTemplateReportConfigurationInputTypeDef",
    "CreateExperimentTemplateRequestTypeDef",
    "CreateExperimentTemplateResponseTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "CreateTargetAccountConfigurationRequestTypeDef",
    "CreateTargetAccountConfigurationResponseTypeDef",
    "DeleteExperimentTemplateRequestTypeDef",
    "DeleteExperimentTemplateResponseTypeDef",
    "DeleteTargetAccountConfigurationRequestTypeDef",
    "DeleteTargetAccountConfigurationResponseTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentErrorTypeDef",
    "ExperimentLogConfigurationTypeDef",
    "ExperimentOptionsTypeDef",
    "ExperimentReportConfigurationCloudWatchDashboardTypeDef",
    "ExperimentReportConfigurationDataSourcesTypeDef",
    "ExperimentReportConfigurationOutputsS3ConfigurationTypeDef",
    "ExperimentReportConfigurationOutputsTypeDef",
    "ExperimentReportConfigurationTypeDef",
    "ExperimentReportErrorTypeDef",
    "ExperimentReportS3ReportTypeDef",
    "ExperimentReportStateTypeDef",
    "ExperimentReportTypeDef",
    "ExperimentS3LogConfigurationTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTargetAccountConfigurationSummaryTypeDef",
    "ExperimentTargetAccountConfigurationTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentTemplateExperimentOptionsTypeDef",
    "ExperimentTemplateLogConfigurationTypeDef",
    "ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef",
    "ExperimentTemplateReportConfigurationDataSourcesInputTypeDef",
    "ExperimentTemplateReportConfigurationDataSourcesTypeDef",
    "ExperimentTemplateReportConfigurationOutputsInputTypeDef",
    "ExperimentTemplateReportConfigurationOutputsTypeDef",
    "ExperimentTemplateReportConfigurationTypeDef",
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    "ExperimentTemplateS3LogConfigurationTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ExperimentTemplateTypeDef",
    "ExperimentTypeDef",
    "GetActionRequestTypeDef",
    "GetActionResponseTypeDef",
    "GetExperimentRequestTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentTargetAccountConfigurationRequestTypeDef",
    "GetExperimentTargetAccountConfigurationResponseTypeDef",
    "GetExperimentTemplateRequestTypeDef",
    "GetExperimentTemplateResponseTypeDef",
    "GetSafetyLeverRequestTypeDef",
    "GetSafetyLeverResponseTypeDef",
    "GetTargetAccountConfigurationRequestTypeDef",
    "GetTargetAccountConfigurationResponseTypeDef",
    "GetTargetResourceTypeRequestTypeDef",
    "GetTargetResourceTypeResponseTypeDef",
    "ListActionsRequestPaginateTypeDef",
    "ListActionsRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListExperimentResolvedTargetsRequestPaginateTypeDef",
    "ListExperimentResolvedTargetsRequestTypeDef",
    "ListExperimentResolvedTargetsResponseTypeDef",
    "ListExperimentTargetAccountConfigurationsRequestTypeDef",
    "ListExperimentTargetAccountConfigurationsResponseTypeDef",
    "ListExperimentTemplatesRequestPaginateTypeDef",
    "ListExperimentTemplatesRequestTypeDef",
    "ListExperimentTemplatesResponseTypeDef",
    "ListExperimentsRequestPaginateTypeDef",
    "ListExperimentsRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetAccountConfigurationsRequestPaginateTypeDef",
    "ListTargetAccountConfigurationsRequestTypeDef",
    "ListTargetAccountConfigurationsResponseTypeDef",
    "ListTargetResourceTypesRequestPaginateTypeDef",
    "ListTargetResourceTypesRequestTypeDef",
    "ListTargetResourceTypesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReportConfigurationCloudWatchDashboardInputTypeDef",
    "ReportConfigurationS3OutputInputTypeDef",
    "ReportConfigurationS3OutputTypeDef",
    "ResolvedTargetTypeDef",
    "ResponseMetadataTypeDef",
    "SafetyLeverStateTypeDef",
    "SafetyLeverTypeDef",
    "StartExperimentExperimentOptionsInputTypeDef",
    "StartExperimentRequestTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentRequestTypeDef",
    "StopExperimentResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TargetAccountConfigurationSummaryTypeDef",
    "TargetAccountConfigurationTypeDef",
    "TargetResourceTypeParameterTypeDef",
    "TargetResourceTypeSummaryTypeDef",
    "TargetResourceTypeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateExperimentOptionsInputTypeDef",
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    "UpdateExperimentTemplateReportConfigurationInputTypeDef",
    "UpdateExperimentTemplateRequestTypeDef",
    "UpdateExperimentTemplateResponseTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
    "UpdateSafetyLeverStateInputTypeDef",
    "UpdateSafetyLeverStateRequestTypeDef",
    "UpdateSafetyLeverStateResponseTypeDef",
    "UpdateTargetAccountConfigurationRequestTypeDef",
    "UpdateTargetAccountConfigurationResponseTypeDef",
)

class ActionParameterTypeDef(TypedDict):
    description: NotRequired[str]
    required: NotRequired[bool]

class ActionTargetTypeDef(TypedDict):
    resourceType: NotRequired[str]

class CreateExperimentTemplateActionInputTypeDef(TypedDict):
    actionId: str
    description: NotRequired[str]
    parameters: NotRequired[Mapping[str, str]]
    targets: NotRequired[Mapping[str, str]]
    startAfter: NotRequired[Sequence[str]]

class CreateExperimentTemplateExperimentOptionsInputTypeDef(TypedDict):
    accountTargeting: NotRequired[AccountTargetingType]
    emptyTargetResolutionMode: NotRequired[EmptyTargetResolutionModeType]

class ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef(TypedDict):
    logGroupArn: str

class ExperimentTemplateS3LogConfigurationInputTypeDef(TypedDict):
    bucketName: str
    prefix: NotRequired[str]

class CreateExperimentTemplateStopConditionInputTypeDef(TypedDict):
    source: str
    value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ExperimentTemplateTargetInputFilterTypeDef(TypedDict):
    path: str
    values: Sequence[str]

class CreateTargetAccountConfigurationRequestTypeDef(TypedDict):
    experimentTemplateId: str
    accountId: str
    roleArn: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class TargetAccountConfigurationTypeDef(TypedDict):
    roleArn: NotRequired[str]
    accountId: NotRequired[str]
    description: NotRequired[str]

DeleteExperimentTemplateRequestTypeDef = TypedDict(
    "DeleteExperimentTemplateRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteTargetAccountConfigurationRequestTypeDef(TypedDict):
    experimentTemplateId: str
    accountId: str

class ExperimentActionStateTypeDef(TypedDict):
    status: NotRequired[ExperimentActionStatusType]
    reason: NotRequired[str]

class ExperimentCloudWatchLogsLogConfigurationTypeDef(TypedDict):
    logGroupArn: NotRequired[str]

class ExperimentErrorTypeDef(TypedDict):
    accountId: NotRequired[str]
    code: NotRequired[str]
    location: NotRequired[str]

class ExperimentS3LogConfigurationTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class ExperimentOptionsTypeDef(TypedDict):
    accountTargeting: NotRequired[AccountTargetingType]
    emptyTargetResolutionMode: NotRequired[EmptyTargetResolutionModeType]
    actionsMode: NotRequired[ActionsModeType]

class ExperimentReportConfigurationCloudWatchDashboardTypeDef(TypedDict):
    dashboardIdentifier: NotRequired[str]

class ExperimentReportConfigurationOutputsS3ConfigurationTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class ExperimentReportErrorTypeDef(TypedDict):
    code: NotRequired[str]

class ExperimentReportS3ReportTypeDef(TypedDict):
    arn: NotRequired[str]
    reportType: NotRequired[str]

class ExperimentStopConditionTypeDef(TypedDict):
    source: NotRequired[str]
    value: NotRequired[str]

class ExperimentTargetAccountConfigurationSummaryTypeDef(TypedDict):
    roleArn: NotRequired[str]
    accountId: NotRequired[str]
    description: NotRequired[str]

class ExperimentTargetAccountConfigurationTypeDef(TypedDict):
    roleArn: NotRequired[str]
    accountId: NotRequired[str]
    description: NotRequired[str]

class ExperimentTargetFilterTypeDef(TypedDict):
    path: NotRequired[str]
    values: NotRequired[List[str]]

class ExperimentTemplateActionTypeDef(TypedDict):
    actionId: NotRequired[str]
    description: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]
    targets: NotRequired[Dict[str, str]]
    startAfter: NotRequired[List[str]]

class ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef(TypedDict):
    logGroupArn: NotRequired[str]

class ExperimentTemplateExperimentOptionsTypeDef(TypedDict):
    accountTargeting: NotRequired[AccountTargetingType]
    emptyTargetResolutionMode: NotRequired[EmptyTargetResolutionModeType]

class ExperimentTemplateS3LogConfigurationTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef(TypedDict):
    dashboardIdentifier: NotRequired[str]

class ReportConfigurationCloudWatchDashboardInputTypeDef(TypedDict):
    dashboardIdentifier: NotRequired[str]

class ReportConfigurationS3OutputInputTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class ReportConfigurationS3OutputTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class ExperimentTemplateStopConditionTypeDef(TypedDict):
    source: NotRequired[str]
    value: NotRequired[str]

ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

class ExperimentTemplateTargetFilterTypeDef(TypedDict):
    path: NotRequired[str]
    values: NotRequired[List[str]]

GetActionRequestTypeDef = TypedDict(
    "GetActionRequestTypeDef",
    {
        "id": str,
    },
)
GetExperimentRequestTypeDef = TypedDict(
    "GetExperimentRequestTypeDef",
    {
        "id": str,
    },
)

class GetExperimentTargetAccountConfigurationRequestTypeDef(TypedDict):
    experimentId: str
    accountId: str

GetExperimentTemplateRequestTypeDef = TypedDict(
    "GetExperimentTemplateRequestTypeDef",
    {
        "id": str,
    },
)
GetSafetyLeverRequestTypeDef = TypedDict(
    "GetSafetyLeverRequestTypeDef",
    {
        "id": str,
    },
)

class GetTargetAccountConfigurationRequestTypeDef(TypedDict):
    experimentTemplateId: str
    accountId: str

class GetTargetResourceTypeRequestTypeDef(TypedDict):
    resourceType: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListActionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListExperimentResolvedTargetsRequestTypeDef(TypedDict):
    experimentId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    targetName: NotRequired[str]

class ResolvedTargetTypeDef(TypedDict):
    resourceType: NotRequired[str]
    targetName: NotRequired[str]
    targetInformation: NotRequired[Dict[str, str]]

class ListExperimentTargetAccountConfigurationsRequestTypeDef(TypedDict):
    experimentId: str
    nextToken: NotRequired[str]

class ListExperimentTemplatesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListExperimentsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    experimentTemplateId: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTargetAccountConfigurationsRequestTypeDef(TypedDict):
    experimentTemplateId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TargetAccountConfigurationSummaryTypeDef(TypedDict):
    roleArn: NotRequired[str]
    accountId: NotRequired[str]
    description: NotRequired[str]

class ListTargetResourceTypesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TargetResourceTypeSummaryTypeDef(TypedDict):
    resourceType: NotRequired[str]
    description: NotRequired[str]

class SafetyLeverStateTypeDef(TypedDict):
    status: NotRequired[SafetyLeverStatusType]
    reason: NotRequired[str]

class StartExperimentExperimentOptionsInputTypeDef(TypedDict):
    actionsMode: NotRequired[ActionsModeType]

StopExperimentRequestTypeDef = TypedDict(
    "StopExperimentRequestTypeDef",
    {
        "id": str,
    },
)

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TargetResourceTypeParameterTypeDef(TypedDict):
    description: NotRequired[str]
    required: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: NotRequired[Sequence[str]]

class UpdateExperimentTemplateActionInputItemTypeDef(TypedDict):
    actionId: NotRequired[str]
    description: NotRequired[str]
    parameters: NotRequired[Mapping[str, str]]
    targets: NotRequired[Mapping[str, str]]
    startAfter: NotRequired[Sequence[str]]

class UpdateExperimentTemplateExperimentOptionsInputTypeDef(TypedDict):
    emptyTargetResolutionMode: NotRequired[EmptyTargetResolutionModeType]

class UpdateExperimentTemplateStopConditionInputTypeDef(TypedDict):
    source: str
    value: NotRequired[str]

class UpdateSafetyLeverStateInputTypeDef(TypedDict):
    status: SafetyLeverStatusInputType
    reason: str

class UpdateTargetAccountConfigurationRequestTypeDef(TypedDict):
    experimentTemplateId: str
    accountId: str
    roleArn: NotRequired[str]
    description: NotRequired[str]

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, ActionTargetTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, ActionParameterTypeDef]],
        "targets": NotRequired[Dict[str, ActionTargetTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateExperimentTemplateLogConfigurationInputTypeDef(TypedDict):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: NotRequired[
        ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef
    ]
    s3Configuration: NotRequired[ExperimentTemplateS3LogConfigurationInputTypeDef]

class UpdateExperimentTemplateLogConfigurationInputTypeDef(TypedDict):
    cloudWatchLogsConfiguration: NotRequired[
        ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef
    ]
    s3Configuration: NotRequired[ExperimentTemplateS3LogConfigurationInputTypeDef]
    logSchemaVersion: NotRequired[int]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateTargetInputTypeDef(TypedDict):
    resourceType: str
    selectionMode: str
    resourceArns: NotRequired[Sequence[str]]
    resourceTags: NotRequired[Mapping[str, str]]
    filters: NotRequired[Sequence[ExperimentTemplateTargetInputFilterTypeDef]]
    parameters: NotRequired[Mapping[str, str]]

class UpdateExperimentTemplateTargetInputTypeDef(TypedDict):
    resourceType: str
    selectionMode: str
    resourceArns: NotRequired[Sequence[str]]
    resourceTags: NotRequired[Mapping[str, str]]
    filters: NotRequired[Sequence[ExperimentTemplateTargetInputFilterTypeDef]]
    parameters: NotRequired[Mapping[str, str]]

class CreateTargetAccountConfigurationResponseTypeDef(TypedDict):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTargetAccountConfigurationResponseTypeDef(TypedDict):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetAccountConfigurationResponseTypeDef(TypedDict):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTargetAccountConfigurationResponseTypeDef(TypedDict):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentActionTypeDef(TypedDict):
    actionId: NotRequired[str]
    description: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]
    targets: NotRequired[Dict[str, str]]
    startAfter: NotRequired[List[str]]
    state: NotRequired[ExperimentActionStateTypeDef]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class ExperimentStateTypeDef(TypedDict):
    status: NotRequired[ExperimentStatusType]
    reason: NotRequired[str]
    error: NotRequired[ExperimentErrorTypeDef]

class ExperimentLogConfigurationTypeDef(TypedDict):
    cloudWatchLogsConfiguration: NotRequired[ExperimentCloudWatchLogsLogConfigurationTypeDef]
    s3Configuration: NotRequired[ExperimentS3LogConfigurationTypeDef]
    logSchemaVersion: NotRequired[int]

class ExperimentReportConfigurationDataSourcesTypeDef(TypedDict):
    cloudWatchDashboards: NotRequired[List[ExperimentReportConfigurationCloudWatchDashboardTypeDef]]

class ExperimentReportConfigurationOutputsTypeDef(TypedDict):
    s3Configuration: NotRequired[ExperimentReportConfigurationOutputsS3ConfigurationTypeDef]

class ExperimentReportStateTypeDef(TypedDict):
    status: NotRequired[ExperimentReportStatusType]
    reason: NotRequired[str]
    error: NotRequired[ExperimentReportErrorTypeDef]

class ListExperimentTargetAccountConfigurationsResponseTypeDef(TypedDict):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetExperimentTargetAccountConfigurationResponseTypeDef(TypedDict):
    targetAccountConfiguration: ExperimentTargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTargetTypeDef(TypedDict):
    resourceType: NotRequired[str]
    resourceArns: NotRequired[List[str]]
    resourceTags: NotRequired[Dict[str, str]]
    filters: NotRequired[List[ExperimentTargetFilterTypeDef]]
    selectionMode: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]

class ExperimentTemplateLogConfigurationTypeDef(TypedDict):
    cloudWatchLogsConfiguration: NotRequired[
        ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef
    ]
    s3Configuration: NotRequired[ExperimentTemplateS3LogConfigurationTypeDef]
    logSchemaVersion: NotRequired[int]

class ExperimentTemplateReportConfigurationDataSourcesTypeDef(TypedDict):
    cloudWatchDashboards: NotRequired[
        List[ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef]
    ]

class ExperimentTemplateReportConfigurationDataSourcesInputTypeDef(TypedDict):
    cloudWatchDashboards: NotRequired[Sequence[ReportConfigurationCloudWatchDashboardInputTypeDef]]

class ExperimentTemplateReportConfigurationOutputsInputTypeDef(TypedDict):
    s3Configuration: NotRequired[ReportConfigurationS3OutputInputTypeDef]

class ExperimentTemplateReportConfigurationOutputsTypeDef(TypedDict):
    s3Configuration: NotRequired[ReportConfigurationS3OutputTypeDef]

class ListExperimentTemplatesResponseTypeDef(TypedDict):
    experimentTemplates: List[ExperimentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ExperimentTemplateTargetTypeDef(TypedDict):
    resourceType: NotRequired[str]
    resourceArns: NotRequired[List[str]]
    resourceTags: NotRequired[Dict[str, str]]
    filters: NotRequired[List[ExperimentTemplateTargetFilterTypeDef]]
    selectionMode: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]

class ListActionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExperimentResolvedTargetsRequestPaginateTypeDef(TypedDict):
    experimentId: str
    targetName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExperimentTemplatesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExperimentsRequestPaginateTypeDef(TypedDict):
    experimentTemplateId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetAccountConfigurationsRequestPaginateTypeDef(TypedDict):
    experimentTemplateId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetResourceTypesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExperimentResolvedTargetsResponseTypeDef(TypedDict):
    resolvedTargets: List[ResolvedTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTargetAccountConfigurationsResponseTypeDef(TypedDict):
    targetAccountConfigurations: List[TargetAccountConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTargetResourceTypesResponseTypeDef(TypedDict):
    targetResourceTypes: List[TargetResourceTypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

SafetyLeverTypeDef = TypedDict(
    "SafetyLeverTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[SafetyLeverStateTypeDef],
    },
)

class StartExperimentRequestTypeDef(TypedDict):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: NotRequired[StartExperimentExperimentOptionsInputTypeDef]
    tags: NotRequired[Mapping[str, str]]

class TargetResourceTypeTypeDef(TypedDict):
    resourceType: NotRequired[str]
    description: NotRequired[str]
    parameters: NotRequired[Dict[str, TargetResourceTypeParameterTypeDef]]

UpdateSafetyLeverStateRequestTypeDef = TypedDict(
    "UpdateSafetyLeverStateRequestTypeDef",
    {
        "id": str,
        "state": UpdateSafetyLeverStateInputTypeDef,
    },
)

class ListActionsResponseTypeDef(TypedDict):
    actions: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetActionResponseTypeDef(TypedDict):
    action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "state": NotRequired[ExperimentStateTypeDef],
        "creationTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "experimentOptions": NotRequired[ExperimentOptionsTypeDef],
    },
)

class ExperimentReportConfigurationTypeDef(TypedDict):
    outputs: NotRequired[ExperimentReportConfigurationOutputsTypeDef]
    dataSources: NotRequired[ExperimentReportConfigurationDataSourcesTypeDef]
    preExperimentDuration: NotRequired[str]
    postExperimentDuration: NotRequired[str]

class ExperimentReportTypeDef(TypedDict):
    state: NotRequired[ExperimentReportStateTypeDef]
    s3Reports: NotRequired[List[ExperimentReportS3ReportTypeDef]]

class CreateExperimentTemplateReportConfigurationInputTypeDef(TypedDict):
    outputs: NotRequired[ExperimentTemplateReportConfigurationOutputsInputTypeDef]
    dataSources: NotRequired[ExperimentTemplateReportConfigurationDataSourcesInputTypeDef]
    preExperimentDuration: NotRequired[str]
    postExperimentDuration: NotRequired[str]

class UpdateExperimentTemplateReportConfigurationInputTypeDef(TypedDict):
    outputs: NotRequired[ExperimentTemplateReportConfigurationOutputsInputTypeDef]
    dataSources: NotRequired[ExperimentTemplateReportConfigurationDataSourcesInputTypeDef]
    preExperimentDuration: NotRequired[str]
    postExperimentDuration: NotRequired[str]

class ExperimentTemplateReportConfigurationTypeDef(TypedDict):
    outputs: NotRequired[ExperimentTemplateReportConfigurationOutputsTypeDef]
    dataSources: NotRequired[ExperimentTemplateReportConfigurationDataSourcesTypeDef]
    preExperimentDuration: NotRequired[str]
    postExperimentDuration: NotRequired[str]

class GetSafetyLeverResponseTypeDef(TypedDict):
    safetyLever: SafetyLeverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSafetyLeverStateResponseTypeDef(TypedDict):
    safetyLever: SafetyLeverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetResourceTypeResponseTypeDef(TypedDict):
    targetResourceType: TargetResourceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperimentsResponseTypeDef(TypedDict):
    experiments: List[ExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "roleArn": NotRequired[str],
        "state": NotRequired[ExperimentStateTypeDef],
        "targets": NotRequired[Dict[str, ExperimentTargetTypeDef]],
        "actions": NotRequired[Dict[str, ExperimentActionTypeDef]],
        "stopConditions": NotRequired[List[ExperimentStopConditionTypeDef]],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired[ExperimentLogConfigurationTypeDef],
        "experimentOptions": NotRequired[ExperimentOptionsTypeDef],
        "targetAccountConfigurationsCount": NotRequired[int],
        "experimentReportConfiguration": NotRequired[ExperimentReportConfigurationTypeDef],
        "experimentReport": NotRequired[ExperimentReportTypeDef],
    },
)

class CreateExperimentTemplateRequestTypeDef(TypedDict):
    clientToken: str
    description: str
    stopConditions: Sequence[CreateExperimentTemplateStopConditionInputTypeDef]
    actions: Mapping[str, CreateExperimentTemplateActionInputTypeDef]
    roleArn: str
    targets: NotRequired[Mapping[str, CreateExperimentTemplateTargetInputTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    logConfiguration: NotRequired[CreateExperimentTemplateLogConfigurationInputTypeDef]
    experimentOptions: NotRequired[CreateExperimentTemplateExperimentOptionsInputTypeDef]
    experimentReportConfiguration: NotRequired[
        CreateExperimentTemplateReportConfigurationInputTypeDef
    ]

UpdateExperimentTemplateRequestTypeDef = TypedDict(
    "UpdateExperimentTemplateRequestTypeDef",
    {
        "id": str,
        "description": NotRequired[str],
        "stopConditions": NotRequired[Sequence[UpdateExperimentTemplateStopConditionInputTypeDef]],
        "targets": NotRequired[Mapping[str, UpdateExperimentTemplateTargetInputTypeDef]],
        "actions": NotRequired[Mapping[str, UpdateExperimentTemplateActionInputItemTypeDef]],
        "roleArn": NotRequired[str],
        "logConfiguration": NotRequired[UpdateExperimentTemplateLogConfigurationInputTypeDef],
        "experimentOptions": NotRequired[UpdateExperimentTemplateExperimentOptionsInputTypeDef],
        "experimentReportConfiguration": NotRequired[
            UpdateExperimentTemplateReportConfigurationInputTypeDef
        ],
    },
)
ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, ExperimentTemplateTargetTypeDef]],
        "actions": NotRequired[Dict[str, ExperimentTemplateActionTypeDef]],
        "stopConditions": NotRequired[List[ExperimentTemplateStopConditionTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired[ExperimentTemplateLogConfigurationTypeDef],
        "experimentOptions": NotRequired[ExperimentTemplateExperimentOptionsTypeDef],
        "targetAccountConfigurationsCount": NotRequired[int],
        "experimentReportConfiguration": NotRequired[ExperimentTemplateReportConfigurationTypeDef],
    },
)

class GetExperimentResponseTypeDef(TypedDict):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentResponseTypeDef(TypedDict):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopExperimentResponseTypeDef(TypedDict):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateResponseTypeDef(TypedDict):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExperimentTemplateResponseTypeDef(TypedDict):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentTemplateResponseTypeDef(TypedDict):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentTemplateResponseTypeDef(TypedDict):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
