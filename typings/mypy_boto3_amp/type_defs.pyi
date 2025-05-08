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
    LoggingConfigurationStatusCodeType,
    RuleGroupsNamespaceStatusCodeType,
    ScraperStatusCodeType,
    WorkspaceConfigurationStatusCodeType,
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
    "BlobTypeDef",
    "CreateAlertManagerDefinitionRequestTypeDef",
    "CreateAlertManagerDefinitionResponseTypeDef",
    "CreateLoggingConfigurationRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "CreateRuleGroupsNamespaceRequestTypeDef",
    "CreateRuleGroupsNamespaceResponseTypeDef",
    "CreateScraperRequestTypeDef",
    "CreateScraperResponseTypeDef",
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteAlertManagerDefinitionRequestTypeDef",
    "DeleteLoggingConfigurationRequestTypeDef",
    "DeleteRuleGroupsNamespaceRequestTypeDef",
    "DeleteScraperRequestTypeDef",
    "DeleteScraperResponseTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DescribeAlertManagerDefinitionRequestTypeDef",
    "DescribeAlertManagerDefinitionResponseTypeDef",
    "DescribeLoggingConfigurationRequestTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeRuleGroupsNamespaceRequestTypeDef",
    "DescribeRuleGroupsNamespaceResponseTypeDef",
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
    "LimitsPerLabelSetEntryTypeDef",
    "LimitsPerLabelSetOutputTypeDef",
    "LimitsPerLabelSetTypeDef",
    "LimitsPerLabelSetUnionTypeDef",
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
    "PaginatorConfigTypeDef",
    "PutAlertManagerDefinitionRequestTypeDef",
    "PutAlertManagerDefinitionResponseTypeDef",
    "PutRuleGroupsNamespaceRequestTypeDef",
    "PutRuleGroupsNamespaceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RoleConfigurationTypeDef",
    "RuleGroupsNamespaceDescriptionTypeDef",
    "RuleGroupsNamespaceStatusTypeDef",
    "RuleGroupsNamespaceSummaryTypeDef",
    "ScrapeConfigurationOutputTypeDef",
    "ScrapeConfigurationTypeDef",
    "ScrapeConfigurationUnionTypeDef",
    "ScraperDescriptionTypeDef",
    "ScraperStatusTypeDef",
    "ScraperSummaryTypeDef",
    "SourceOutputTypeDef",
    "SourceTypeDef",
    "SourceUnionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLoggingConfigurationRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateScraperRequestTypeDef",
    "UpdateScraperResponseTypeDef",
    "UpdateWorkspaceAliasRequestTypeDef",
    "UpdateWorkspaceConfigurationRequestTypeDef",
    "UpdateWorkspaceConfigurationResponseTypeDef",
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

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateLoggingConfigurationRequestTypeDef(TypedDict):
    logGroupArn: str
    workspaceId: str
    clientToken: NotRequired[str]

class LoggingConfigurationStatusTypeDef(TypedDict):
    statusCode: LoggingConfigurationStatusCodeType
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
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class WorkspaceStatusTypeDef(TypedDict):
    statusCode: WorkspaceStatusCodeType

class DeleteAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteRuleGroupsNamespaceRequestTypeDef(TypedDict):
    name: str
    workspaceId: str
    clientToken: NotRequired[str]

class DeleteScraperRequestTypeDef(TypedDict):
    scraperId: str
    clientToken: NotRequired[str]

class DeleteWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]

class DescribeAlertManagerDefinitionRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeLoggingConfigurationRequestTypeDef(TypedDict):
    workspaceId: str

class DescribeRuleGroupsNamespaceRequestTypeDef(TypedDict):
    name: str
    workspaceId: str

class DescribeScraperRequestTypeDef(TypedDict):
    scraperId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

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

class LimitsPerLabelSetEntryTypeDef(TypedDict):
    maxSeries: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListRuleGroupsNamespacesRequestTypeDef(TypedDict):
    workspaceId: str
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]

class ListScrapersRequestTypeDef(TypedDict):
    filters: NotRequired[Mapping[str, Sequence[str]]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListWorkspacesRequestTypeDef(TypedDict):
    alias: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ScrapeConfigurationOutputTypeDef(TypedDict):
    configurationBlob: NotRequired[bytes]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLoggingConfigurationRequestTypeDef(TypedDict):
    logGroupArn: str
    workspaceId: str
    clientToken: NotRequired[str]

class UpdateWorkspaceAliasRequestTypeDef(TypedDict):
    workspaceId: str
    alias: NotRequired[str]
    clientToken: NotRequired[str]

class WorkspaceConfigurationStatusTypeDef(TypedDict):
    statusCode: WorkspaceConfigurationStatusCodeType
    statusReason: NotRequired[str]

class AlertManagerDefinitionDescriptionTypeDef(TypedDict):
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    status: AlertManagerDefinitionStatusTypeDef

class DestinationTypeDef(TypedDict):
    ampConfiguration: NotRequired[AmpConfigurationTypeDef]

class CreateAlertManagerDefinitionRequestTypeDef(TypedDict):
    data: BlobTypeDef
    workspaceId: str
    clientToken: NotRequired[str]

class CreateRuleGroupsNamespaceRequestTypeDef(TypedDict):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class PutAlertManagerDefinitionRequestTypeDef(TypedDict):
    data: BlobTypeDef
    workspaceId: str
    clientToken: NotRequired[str]

class PutRuleGroupsNamespaceRequestTypeDef(TypedDict):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: NotRequired[str]

class ScrapeConfigurationTypeDef(TypedDict):
    configurationBlob: NotRequired[BlobTypeDef]

class CreateAlertManagerDefinitionResponseTypeDef(TypedDict):
    status: AlertManagerDefinitionStatusTypeDef
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

class CreateLoggingConfigurationResponseTypeDef(TypedDict):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationMetadataTypeDef(TypedDict):
    createdAt: datetime
    logGroupArn: str
    modifiedAt: datetime
    status: LoggingConfigurationStatusTypeDef
    workspace: str

class UpdateLoggingConfigurationResponseTypeDef(TypedDict):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupsNamespaceResponseTypeDef(TypedDict):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuleGroupsNamespaceResponseTypeDef(TypedDict):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupsNamespaceDescriptionTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: NotRequired[Dict[str, str]]

class RuleGroupsNamespaceSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: NotRequired[Dict[str, str]]

class CreateScraperResponseTypeDef(TypedDict):
    arn: str
    scraperId: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScraperResponseTypeDef(TypedDict):
    scraperId: str
    status: ScraperStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScraperResponseTypeDef(TypedDict):
    arn: str
    scraperId: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(TypedDict):
    arn: str
    kmsKeyArn: str
    status: WorkspaceStatusTypeDef
    tags: Dict[str, str]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspaceDescriptionTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    prometheusEndpoint: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class WorkspaceSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

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

class SourceOutputTypeDef(TypedDict):
    eksConfiguration: NotRequired[EksConfigurationOutputTypeDef]

class SourceTypeDef(TypedDict):
    eksConfiguration: NotRequired[EksConfigurationTypeDef]

class LimitsPerLabelSetOutputTypeDef(TypedDict):
    labelSet: Dict[str, str]
    limits: LimitsPerLabelSetEntryTypeDef

class LimitsPerLabelSetTypeDef(TypedDict):
    labelSet: Mapping[str, str]
    limits: LimitsPerLabelSetEntryTypeDef

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

class UpdateWorkspaceConfigurationResponseTypeDef(TypedDict):
    status: WorkspaceConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlertManagerDefinitionResponseTypeDef(TypedDict):
    alertManagerDefinition: AlertManagerDefinitionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ScrapeConfigurationUnionTypeDef = Union[
    ScrapeConfigurationTypeDef, ScrapeConfigurationOutputTypeDef
]

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

class ScraperDescriptionTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scrapeConfiguration: ScrapeConfigurationOutputTypeDef
    scraperId: str
    source: SourceOutputTypeDef
    status: ScraperStatusTypeDef
    alias: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    statusReason: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ScraperSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scraperId: str
    source: SourceOutputTypeDef
    status: ScraperStatusTypeDef
    alias: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    statusReason: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

SourceUnionTypeDef = Union[SourceTypeDef, SourceOutputTypeDef]

class WorkspaceConfigurationDescriptionTypeDef(TypedDict):
    status: WorkspaceConfigurationStatusTypeDef
    limitsPerLabelSet: NotRequired[List[LimitsPerLabelSetOutputTypeDef]]
    retentionPeriodInDays: NotRequired[int]

LimitsPerLabelSetUnionTypeDef = Union[LimitsPerLabelSetTypeDef, LimitsPerLabelSetOutputTypeDef]

class UpdateScraperRequestTypeDef(TypedDict):
    scraperId: str
    alias: NotRequired[str]
    clientToken: NotRequired[str]
    destination: NotRequired[DestinationTypeDef]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    scrapeConfiguration: NotRequired[ScrapeConfigurationUnionTypeDef]

class DescribeScraperResponseTypeDef(TypedDict):
    scraper: ScraperDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScrapersResponseTypeDef(TypedDict):
    scrapers: List[ScraperSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateScraperRequestTypeDef(TypedDict):
    destination: DestinationTypeDef
    scrapeConfiguration: ScrapeConfigurationUnionTypeDef
    source: SourceUnionTypeDef
    alias: NotRequired[str]
    clientToken: NotRequired[str]
    roleConfiguration: NotRequired[RoleConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class DescribeWorkspaceConfigurationResponseTypeDef(TypedDict):
    workspaceConfiguration: WorkspaceConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceConfigurationRequestTypeDef(TypedDict):
    workspaceId: str
    clientToken: NotRequired[str]
    limitsPerLabelSet: NotRequired[Sequence[LimitsPerLabelSetUnionTypeDef]]
    retentionPeriodInDays: NotRequired[int]
