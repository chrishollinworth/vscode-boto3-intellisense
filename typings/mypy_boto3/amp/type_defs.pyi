"""
Type annotations for amp service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_amp.type_defs import AlertManagerDefinitionStatusTypeDef

    data: AlertManagerDefinitionStatusTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AlertManagerDefinitionStatusCodeType,
    AnomalyDetectorStatusCodeType,
    LoggingConfigurationStatusCodeType,
    QueryLoggingConfigurationStatusCodeType,
    RuleGroupsNamespaceStatusCodeType,
    ScraperComponentTypeType,
    ScraperLoggingConfigurationStatusCodeType,
    ScraperStatusCodeType,
    WorkspaceConfigurationStatusCodeType,
    WorkspacePolicyStatusCodeType,
    WorkspaceStatusCodeType,
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
    "AlertManagerDefinitionDescriptionTypeDef",
    "AlertManagerDefinitionStatusTypeDef",
    "AmpConfigurationTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorDescriptionTypeDef",
    "AnomalyDetectorMissingDataActionTypeDef",
    "AnomalyDetectorStatusTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "BlobTypeDef",
    "CloudWatchLogDestinationTypeDef",
    "ComponentConfigOutputTypeDef",
    "ComponentConfigTypeDef",
    "ComponentConfigUnionTypeDef",
    "CreateAlertManagerDefinitionRequestTypeDef",
    "CreateAlertManagerDefinitionResponseTypeDef",
    "CreateAnomalyDetectorRequestTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateLoggingConfigurationRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "CreateQueryLoggingConfigurationRequestTypeDef",
    "CreateQueryLoggingConfigurationResponseTypeDef",
    "CreateRuleGroupsNamespaceRequestTypeDef",
    "CreateRuleGroupsNamespaceResponseTypeDef",
    "CreateScraperRequestTypeDef",
    "CreateScraperResponseTypeDef",
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteAlertManagerDefinitionRequestTypeDef",
    "DeleteAnomalyDetectorRequestTypeDef",
    "DeleteLoggingConfigurationRequestTypeDef",
    "DeleteQueryLoggingConfigurationRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteRuleGroupsNamespaceRequestTypeDef",
    "DeleteScraperLoggingConfigurationRequestTypeDef",
    "DeleteScraperRequestTypeDef",
    "DeleteScraperResponseTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DescribeAlertManagerDefinitionRequestTypeDef",
    "DescribeAlertManagerDefinitionResponseTypeDef",
    "DescribeAnomalyDetectorRequestTypeDef",
    "DescribeAnomalyDetectorRequestWaitExtraTypeDef",
    "DescribeAnomalyDetectorRequestWaitTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "DescribeLoggingConfigurationRequestTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeQueryLoggingConfigurationRequestTypeDef",
    "DescribeQueryLoggingConfigurationResponseTypeDef",
    "DescribeResourcePolicyRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupsNamespaceRequestTypeDef",
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    "DescribeScraperLoggingConfigurationRequestTypeDef",
    "DescribeScraperLoggingConfigurationResponseTypeDef",
    "DescribeScraperRequestTypeDef",
    "DescribeScraperRequestWaitExtraTypeDef",
    "DescribeScraperRequestWaitTypeDef",
    "DescribeScraperResponseTypeDef",
    "DescribeWorkspaceConfigurationRequestTypeDef",
    "DescribeWorkspaceConfigurationResponseTypeDef",
    "DescribeWorkspaceRequestTypeDef",
    "DescribeWorkspaceRequestWaitExtraTypeDef",
    "DescribeWorkspaceRequestWaitTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DestinationTypeDef",
    "EksConfigurationOutputTypeDef",
    "EksConfigurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDefaultScraperConfigurationResponseTypeDef",
    "IgnoreNearExpectedTypeDef",
    "LimitsPerLabelSetEntryTypeDef",
    "LimitsPerLabelSetOutputTypeDef",
    "LimitsPerLabelSetTypeDef",
    "LimitsPerLabelSetUnionTypeDef",
    "ListAnomalyDetectorsRequestPaginateTypeDef",
    "ListAnomalyDetectorsRequestTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListRuleGroupsNamespacesRequestPaginateTypeDef",
    "ListRuleGroupsNamespacesRequestTypeDef",
    "ListRuleGroupsNamespacesResponseTypeDef",
    "ListScrapersRequestPaginateTypeDef",
    "ListScrapersRequestTypeDef",
    "ListScrapersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestPaginateTypeDef",
    "ListWorkspacesRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "LoggingConfigurationMetadataTypeDef",
    "LoggingConfigurationStatusTypeDef",
    "LoggingDestinationTypeDef",
    "LoggingFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PutAlertManagerDefinitionRequestTypeDef",
    "PutAlertManagerDefinitionResponseTypeDef",
    "PutAnomalyDetectorRequestTypeDef",
    "PutAnomalyDetectorResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutRuleGroupsNamespaceRequestTypeDef",
    "PutRuleGroupsNamespaceResponseTypeDef",
    "QueryLoggingConfigurationMetadataTypeDef",
    "QueryLoggingConfigurationStatusTypeDef",
    "RandomCutForestConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RoleConfigurationTypeDef",
    "RuleGroupsNamespaceDescriptionTypeDef",
    "RuleGroupsNamespaceStatusTypeDef",
    "RuleGroupsNamespaceSummaryTypeDef",
    "ScrapeConfigurationOutputTypeDef",
    "ScrapeConfigurationTypeDef",
    "ScrapeConfigurationUnionTypeDef",
    "ScraperComponentOutputTypeDef",
    "ScraperComponentTypeDef",
    "ScraperComponentUnionTypeDef",
    "ScraperDescriptionTypeDef",
    "ScraperLoggingConfigurationStatusTypeDef",
    "ScraperLoggingDestinationTypeDef",
    "ScraperStatusTypeDef",
    "ScraperSummaryTypeDef",
    "SourceOutputTypeDef",
    "SourceTypeDef",
    "SourceUnionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLoggingConfigurationRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateQueryLoggingConfigurationRequestTypeDef",
    "UpdateQueryLoggingConfigurationResponseTypeDef",
    "UpdateScraperLoggingConfigurationRequestTypeDef",
    "UpdateScraperLoggingConfigurationResponseTypeDef",
    "UpdateScraperRequestTypeDef",
    "UpdateScraperResponseTypeDef",
    "UpdateWorkspaceAliasRequestTypeDef",
    "UpdateWorkspaceConfigurationRequestTypeDef",
    "UpdateWorkspaceConfigurationResponseTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WorkspaceConfigurationDescriptionTypeDef",
    "WorkspaceConfigurationStatusTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

class AlertManagerDefinitionStatusTypeDef(TypedDict):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: NotRequired[str]

class AmpConfigurationTypeDef(TypedDict):
    workspaceArn: str

class AnomalyDetectorMissingDataActionTypeDef(TypedDict):
    markAsAnomaly: NotRequired[bool]
    skip: NotRequired[bool]

class AnomalyDetectorStatusTypeDef(TypedDict):
    statusCode: AnomalyDetectorStatusCodeType
    statusReason: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CloudWatchLogDestinationTypeDef(TypedDict):
    logGroupArn: str

class ComponentConfigOutputTypeDef(TypedDict):
    options: NotRequired[Dict[str, str]]

class ComponentConfigTypeDef(TypedDict):
    options: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    logGroupArn: str
    clientToken: NotRequired[str]

class LoggingConfigurationStatusTypeDef(TypedDict):
    statusCode: LoggingConfigurationStatusCodeType
    statusReason: NotRequired[str]

class QueryLoggingConfigurationStatusTypeDef(TypedDict):
    statusCode: QueryLoggingConfigurationStatusCodeType
    statusReason: NotRequired[str]

class RuleGroupsNamespaceStatusTypeDef(TypedDict):
    statusCode: RuleGroupsNamespaceStatusCodeType
    statusReason: NotRequired[str]

class RoleConfigurationTypeDef(TypedDict):
    sourceRoleArn: NotRequired[str]
    targetRoleArn: NotRequired[str]

class ScraperStatusTypeDef(TypedDict):
    statusCode: ScraperStatusCodeType

class CreateWorkspaceRequestTypeDef(TypedDict):
    alias: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]

class WorkspaceStatusTypeDef(TypedDict):
    statusCode: WorkspaceStatusCodeType

class DeleteAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteAnomalyDetectorRequestTypeDef(TypedDict):
    workspaceId: str
    anomalyDetectorId: str
    clientToken: NotRequired[str]

class DeleteLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteQueryLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]
    revisionId: NotRequired[str]

class DeleteRuleGroupsNamespaceRequestTypeDef(TypedDict):
    workspaceId: str
    name: str
    clientToken: NotRequired[str]

class DeleteScraperLoggingConfigurationRequestTypeDef(TypedDict):
    scraperId: str
    clientToken: NotRequired[str]

class DeleteScraperRequestTypeDef(TypedDict):
    scraperId: str
    clientToken: NotRequired[str]

class DeleteWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DescribeAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeAnomalyDetectorRequestTypeDef(TypedDict):
    workspaceId: str
    anomalyDetectorId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeQueryLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeResourcePolicyRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeRuleGroupsNamespaceRequestTypeDef(TypedDict):
    workspaceId: str
    name: str

class DescribeScraperLoggingConfigurationRequestTypeDef(TypedDict):
    scraperId: str

class ScraperLoggingConfigurationStatusTypeDef(TypedDict):
    statusCode: ScraperLoggingConfigurationStatusCodeType
    statusReason: NotRequired[str]

class DescribeScraperRequestTypeDef(TypedDict):
    scraperId: str

class DescribeWorkspaceConfigurationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str

class EksConfigurationOutputTypeDef(TypedDict):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: NotRequired[List[str]]

class EksConfigurationTypeDef(TypedDict):
    clusterArn: str
    subnetIds: Sequence[str]
    securityGroupIds: NotRequired[Sequence[str]]

class IgnoreNearExpectedTypeDef(TypedDict):
    amount: NotRequired[float]
    ratio: NotRequired[float]

class LimitsPerLabelSetEntryTypeDef(TypedDict):
    maxSeries: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAnomalyDetectorsRequestTypeDef(TypedDict):
    workspaceId: str
    alias: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRuleGroupsNamespacesRequestTypeDef(TypedDict):
    workspaceId: str
    name: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListScrapersRequestTypeDef(TypedDict):
    filters: NotRequired[Mapping[str, Sequence[str]]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListWorkspacesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    alias: NotRequired[str]
    maxResults: NotRequired[int]

class LoggingFilterTypeDef(TypedDict):
    qspThreshold: int

class PutResourcePolicyRequestTypeDef(TypedDict):
    workspaceId: str
    policyDocument: str
    clientToken: NotRequired[str]
    revisionId: NotRequired[str]

class ScrapeConfigurationOutputTypeDef(TypedDict):
    configurationBlob: NotRequired[bytes]

class VpcConfigurationOutputTypeDef(TypedDict):
    securityGroupIds: List[str]
    subnetIds: List[str]

class VpcConfigurationTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    logGroupArn: str
    clientToken: NotRequired[str]

class UpdateWorkspaceAliasRequestTypeDef(TypedDict):
    workspaceId: str
    alias: NotRequired[str]
    clientToken: NotRequired[str]

class WorkspaceConfigurationStatusTypeDef(TypedDict):
    statusCode: WorkspaceConfigurationStatusCodeType
    statusReason: NotRequired[str]

class AlertManagerDefinitionDescriptionTypeDef(TypedDict):
    status: AlertManagerDefinitionStatusTypeDef
    data: bytes
    createdAt: datetime
    modifiedAt: datetime

class DestinationTypeDef(TypedDict):
    ampConfiguration: NotRequired[AmpConfigurationTypeDef]

class AnomalyDetectorSummaryTypeDef(TypedDict):
    arn: str
    anomalyDetectorId: str
    alias: str
    status: AnomalyDetectorStatusTypeDef
    createdAt: datetime
    modifiedAt: datetime
    tags: NotRequired[Dict[str, str]]

class CreateAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str
    data: BlobTypeDef
    clientToken: NotRequired[str]

class CreateRuleGroupsNamespaceRequestTypeDef(TypedDict):
    workspaceId: str
    name: str
    data: BlobTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class PutAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str
    data: BlobTypeDef
    clientToken: NotRequired[str]

class PutRuleGroupsNamespaceRequestTypeDef(TypedDict):
    workspaceId: str
    name: str
    data: BlobTypeDef
    clientToken: NotRequired[str]

class ScrapeConfigurationTypeDef(TypedDict):
    configurationBlob: NotRequired[BlobTypeDef]

class ScraperLoggingDestinationTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogDestinationTypeDef]

ScraperComponentOutputTypeDef = TypedDict(
    "ScraperComponentOutputTypeDef",
    {
        "type": ScraperComponentTypeType,
        "config": NotRequired[ComponentConfigOutputTypeDef],
    },
)
ComponentConfigUnionTypeDef = Union[ComponentConfigTypeDef, ComponentConfigOutputTypeDef]

class CreateAlertManagerDefinitionResponseTypeDef(TypedDict):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalyDetectorResponseTypeDef(TypedDict):
    anomalyDetectorId: str
    arn: str
    status: AnomalyDetectorStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(TypedDict):
    policyDocument: str
    policyStatus: WorkspacePolicyStatusCodeType
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultScraperConfigurationResponseTypeDef(TypedDict):
    configuration: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAlertManagerDefinitionResponseTypeDef(TypedDict):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAnomalyDetectorResponseTypeDef(TypedDict):
    anomalyDetectorId: str
    arn: str
    status: AnomalyDetectorStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    policyStatus: WorkspacePolicyStatusCodeType
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggingConfigurationResponseTypeDef(TypedDict):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationMetadataTypeDef(TypedDict):
    status: LoggingConfigurationStatusTypeDef
    workspace: str
    logGroupArn: str
    createdAt: datetime
    modifiedAt: datetime

class UpdateLoggingConfigurationResponseTypeDef(TypedDict):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueryLoggingConfigurationResponseTypeDef(TypedDict):
    status: QueryLoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQueryLoggingConfigurationResponseTypeDef(TypedDict):
    status: QueryLoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupsNamespaceResponseTypeDef(TypedDict):
    name: str
    arn: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuleGroupsNamespaceResponseTypeDef(TypedDict):
    name: str
    arn: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupsNamespaceDescriptionTypeDef(TypedDict):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    data: bytes
    createdAt: datetime
    modifiedAt: datetime
    tags: NotRequired[Dict[str, str]]

class RuleGroupsNamespaceSummaryTypeDef(TypedDict):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    createdAt: datetime
    modifiedAt: datetime
    tags: NotRequired[Dict[str, str]]

class CreateScraperResponseTypeDef(TypedDict):
    scraperId: str
    arn: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScraperResponseTypeDef(TypedDict):
    scraperId: str
    status: ScraperStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScraperResponseTypeDef(TypedDict):
    scraperId: str
    arn: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(TypedDict):
    workspaceId: str
    arn: str
    status: WorkspaceStatusTypeDef
    tags: Dict[str, str]
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspaceDescriptionTypeDef(TypedDict):
    workspaceId: str
    arn: str
    status: WorkspaceStatusTypeDef
    createdAt: datetime
    alias: NotRequired[str]
    prometheusEndpoint: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    kmsKeyArn: NotRequired[str]

class WorkspaceSummaryTypeDef(TypedDict):
    workspaceId: str
    arn: str
    status: WorkspaceStatusTypeDef
    createdAt: datetime
    alias: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    kmsKeyArn: NotRequired[str]

class DescribeAnomalyDetectorRequestWaitExtraTypeDef(TypedDict):
    workspaceId: str
    anomalyDetectorId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeAnomalyDetectorRequestWaitTypeDef(TypedDict):
    workspaceId: str
    anomalyDetectorId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeScraperRequestWaitExtraTypeDef(TypedDict):
    scraperId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeScraperRequestWaitTypeDef(TypedDict):
    scraperId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeWorkspaceRequestWaitExtraTypeDef(TypedDict):
    workspaceId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeWorkspaceRequestWaitTypeDef(TypedDict):
    workspaceId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class UpdateScraperLoggingConfigurationResponseTypeDef(TypedDict):
    status: ScraperLoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RandomCutForestConfigurationTypeDef(TypedDict):
    query: str
    shingleSize: NotRequired[int]
    sampleSize: NotRequired[int]
    ignoreNearExpectedFromAbove: NotRequired[IgnoreNearExpectedTypeDef]
    ignoreNearExpectedFromBelow: NotRequired[IgnoreNearExpectedTypeDef]

class LimitsPerLabelSetOutputTypeDef(TypedDict):
    limits: LimitsPerLabelSetEntryTypeDef
    labelSet: Dict[str, str]

class LimitsPerLabelSetTypeDef(TypedDict):
    limits: LimitsPerLabelSetEntryTypeDef
    labelSet: Mapping[str, str]

class ListAnomalyDetectorsRequestPaginateTypeDef(TypedDict):
    workspaceId: str
    alias: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRuleGroupsNamespacesRequestPaginateTypeDef(TypedDict):
    workspaceId: str
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListScrapersRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Mapping[str, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspacesRequestPaginateTypeDef(TypedDict):
    alias: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LoggingDestinationTypeDef(TypedDict):
    cloudWatchLogs: CloudWatchLogDestinationTypeDef
    filters: LoggingFilterTypeDef

class SourceOutputTypeDef(TypedDict):
    eksConfiguration: NotRequired[EksConfigurationOutputTypeDef]
    vpcConfiguration: NotRequired[VpcConfigurationOutputTypeDef]

class SourceTypeDef(TypedDict):
    eksConfiguration: NotRequired[EksConfigurationTypeDef]
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]

class UpdateWorkspaceConfigurationResponseTypeDef(TypedDict):
    status: WorkspaceConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlertManagerDefinitionResponseTypeDef(TypedDict):
    alertManagerDefinition: AlertManagerDefinitionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnomalyDetectorsResponseTypeDef(TypedDict):
    anomalyDetectors: List[AnomalyDetectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ScrapeConfigurationUnionTypeDef = Union[
    ScrapeConfigurationTypeDef, ScrapeConfigurationOutputTypeDef
]

class DescribeScraperLoggingConfigurationResponseTypeDef(TypedDict):
    status: ScraperLoggingConfigurationStatusTypeDef
    scraperId: str
    loggingDestination: ScraperLoggingDestinationTypeDef
    scraperComponents: List[ScraperComponentOutputTypeDef]
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

ScraperComponentTypeDef = TypedDict(
    "ScraperComponentTypeDef",
    {
        "type": ScraperComponentTypeType,
        "config": NotRequired[ComponentConfigUnionTypeDef],
    },
)

class DescribeLoggingConfigurationResponseTypeDef(TypedDict):
    loggingConfiguration: LoggingConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuleGroupsNamespaceResponseTypeDef(TypedDict):
    ruleGroupsNamespace: RuleGroupsNamespaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsNamespacesResponseTypeDef(TypedDict):
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeWorkspaceResponseTypeDef(TypedDict):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspacesResponseTypeDef(TypedDict):
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AnomalyDetectorConfigurationTypeDef(TypedDict):
    randomCutForest: NotRequired[RandomCutForestConfigurationTypeDef]

class WorkspaceConfigurationDescriptionTypeDef(TypedDict):
    status: WorkspaceConfigurationStatusTypeDef
    limitsPerLabelSet: NotRequired[List[LimitsPerLabelSetOutputTypeDef]]
    retentionPeriodInDays: NotRequired[int]

LimitsPerLabelSetUnionTypeDef = Union[LimitsPerLabelSetTypeDef, LimitsPerLabelSetOutputTypeDef]

class CreateQueryLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    destinations: Sequence[LoggingDestinationTypeDef]
    clientToken: NotRequired[str]

class QueryLoggingConfigurationMetadataTypeDef(TypedDict):
    status: QueryLoggingConfigurationStatusTypeDef
    workspace: str
    destinations: List[LoggingDestinationTypeDef]
    createdAt: datetime
    modifiedAt: datetime

class UpdateQueryLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    destinations: Sequence[LoggingDestinationTypeDef]
    clientToken: NotRequired[str]

class ScraperDescriptionTypeDef(TypedDict):
    scraperId: str
    arn: str
    roleArn: str
    status: ScraperStatusTypeDef
    createdAt: datetime
    lastModifiedAt: datetime
    scrapeConfiguration: ScrapeConfigurationOutputTypeDef
    source: SourceOutputTypeDef
    destination: DestinationTypeDef
    alias: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    statusReason: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]

class ScraperSummaryTypeDef(TypedDict):
    scraperId: str
    arn: str
    roleArn: str
    status: ScraperStatusTypeDef
    createdAt: datetime
    lastModifiedAt: datetime
    source: SourceOutputTypeDef
    destination: DestinationTypeDef
    alias: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    statusReason: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]

SourceUnionTypeDef = Union[SourceTypeDef, SourceOutputTypeDef]

class UpdateScraperRequestTypeDef(TypedDict):
    scraperId: str
    alias: NotRequired[str]
    scrapeConfiguration: NotRequired[ScrapeConfigurationUnionTypeDef]
    destination: NotRequired[DestinationTypeDef]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    clientToken: NotRequired[str]

ScraperComponentUnionTypeDef = Union[ScraperComponentTypeDef, ScraperComponentOutputTypeDef]

class AnomalyDetectorDescriptionTypeDef(TypedDict):
    arn: str
    anomalyDetectorId: str
    alias: str
    status: AnomalyDetectorStatusTypeDef
    createdAt: datetime
    modifiedAt: datetime
    evaluationIntervalInSeconds: NotRequired[int]
    missingDataAction: NotRequired[AnomalyDetectorMissingDataActionTypeDef]
    configuration: NotRequired[AnomalyDetectorConfigurationTypeDef]
    labels: NotRequired[Dict[str, str]]
    tags: NotRequired[Dict[str, str]]

class CreateAnomalyDetectorRequestTypeDef(TypedDict):
    workspaceId: str
    alias: str
    configuration: AnomalyDetectorConfigurationTypeDef
    evaluationIntervalInSeconds: NotRequired[int]
    missingDataAction: NotRequired[AnomalyDetectorMissingDataActionTypeDef]
    labels: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class PutAnomalyDetectorRequestTypeDef(TypedDict):
    workspaceId: str
    anomalyDetectorId: str
    configuration: AnomalyDetectorConfigurationTypeDef
    evaluationIntervalInSeconds: NotRequired[int]
    missingDataAction: NotRequired[AnomalyDetectorMissingDataActionTypeDef]
    labels: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class DescribeWorkspaceConfigurationResponseTypeDef(TypedDict):
    workspaceConfiguration: WorkspaceConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]
    limitsPerLabelSet: NotRequired[Sequence[LimitsPerLabelSetUnionTypeDef]]
    retentionPeriodInDays: NotRequired[int]

class DescribeQueryLoggingConfigurationResponseTypeDef(TypedDict):
    queryLoggingConfiguration: QueryLoggingConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScraperResponseTypeDef(TypedDict):
    scraper: ScraperDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScrapersResponseTypeDef(TypedDict):
    scrapers: List[ScraperSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateScraperRequestTypeDef(TypedDict):
    scrapeConfiguration: ScrapeConfigurationUnionTypeDef
    source: SourceUnionTypeDef
    destination: DestinationTypeDef
    alias: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateScraperLoggingConfigurationRequestTypeDef(TypedDict):
    scraperId: str
    loggingDestination: ScraperLoggingDestinationTypeDef
    scraperComponents: NotRequired[Sequence[ScraperComponentUnionTypeDef]]

class DescribeAnomalyDetectorResponseTypeDef(TypedDict):
    anomalyDetector: AnomalyDetectorDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
