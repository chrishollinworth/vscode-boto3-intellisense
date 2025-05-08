"""
Type annotations for inspector service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AttributeTypeDef

    data: AttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AgentHealthCodeType,
    AgentHealthType,
    AssessmentRunNotificationSnsStatusCodeType,
    AssessmentRunStateType,
    FailedItemErrorCodeType,
    InspectorEventType,
    PreviewStatusType,
    ReportFileFormatType,
    ReportStatusType,
    ReportTypeType,
    ScopeTypeType,
    SeverityType,
    StopActionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddAttributesToFindingsRequestTypeDef",
    "AddAttributesToFindingsResponseTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "CreateAssessmentTargetRequestTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateRequestTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewRequestTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupRequestTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DeleteAssessmentRunRequestTypeDef",
    "DeleteAssessmentTargetRequestTypeDef",
    "DeleteAssessmentTemplateRequestTypeDef",
    "DescribeAssessmentRunsRequestTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeAssessmentTargetsRequestTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "DescribeAssessmentTemplatesRequestTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "DescribeExclusionsRequestTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "DescribeFindingsRequestTypeDef",
    "DescribeFindingsResponseTypeDef",
    "DescribeResourceGroupsRequestTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "DescribeRulesPackagesRequestTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "DurationRangeTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "GetAssessmentReportRequestTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "GetExclusionsPreviewRequestTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "GetTelemetryMetadataRequestTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "InspectorServiceAttributesTypeDef",
    "ListAssessmentRunAgentsRequestPaginateTypeDef",
    "ListAssessmentRunAgentsRequestTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentRunsRequestPaginateTypeDef",
    "ListAssessmentRunsRequestTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsRequestPaginateTypeDef",
    "ListAssessmentTargetsRequestTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesRequestPaginateTypeDef",
    "ListAssessmentTemplatesRequestTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListEventSubscriptionsRequestPaginateTypeDef",
    "ListEventSubscriptionsRequestTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "ListExclusionsRequestPaginateTypeDef",
    "ListExclusionsRequestTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsRequestPaginateTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesRequestPaginateTypeDef",
    "ListRulesPackagesRequestTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsRequestPaginateTypeDef",
    "PreviewAgentsRequestTypeDef",
    "PreviewAgentsResponseTypeDef",
    "PrivateIpTypeDef",
    "RegisterCrossAccountAccessRoleRequestTypeDef",
    "RemoveAttributesFromFindingsRequestTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "ResponseMetadataTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "SetTagsForResourceRequestTypeDef",
    "StartAssessmentRunRequestTypeDef",
    "StartAssessmentRunResponseTypeDef",
    "StopAssessmentRunRequestTypeDef",
    "SubscribeToEventRequestTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
    "TimestampTypeDef",
    "UnsubscribeFromEventRequestTypeDef",
    "UpdateAssessmentTargetRequestTypeDef",
)

class AttributeTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class FailedItemDetailsTypeDef(TypedDict):
    failureCode: FailedItemErrorCodeType
    retryable: bool

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AgentFilterTypeDef(TypedDict):
    agentHealths: Sequence[AgentHealthType]
    agentHealthCodes: Sequence[AgentHealthCodeType]

class AgentPreviewTypeDef(TypedDict):
    agentId: str
    hostname: NotRequired[str]
    autoScalingGroup: NotRequired[str]
    agentHealth: NotRequired[AgentHealthType]
    agentVersion: NotRequired[str]
    operatingSystem: NotRequired[str]
    kernelVersion: NotRequired[str]
    ipv4Address: NotRequired[str]

class TelemetryMetadataTypeDef(TypedDict):
    messageType: str
    count: int
    dataSize: NotRequired[int]

class DurationRangeTypeDef(TypedDict):
    minSeconds: NotRequired[int]
    maxSeconds: NotRequired[int]

class AssessmentRunNotificationTypeDef(TypedDict):
    date: datetime
    event: InspectorEventType
    error: bool
    message: NotRequired[str]
    snsTopicArn: NotRequired[str]
    snsPublishStatusCode: NotRequired[AssessmentRunNotificationSnsStatusCodeType]

class AssessmentRunStateChangeTypeDef(TypedDict):
    stateChangedAt: datetime
    state: AssessmentRunStateType

class AssessmentTargetFilterTypeDef(TypedDict):
    assessmentTargetNamePattern: NotRequired[str]

class AssessmentTargetTypeDef(TypedDict):
    arn: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    resourceGroupArn: NotRequired[str]

class TagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class CreateAssessmentTargetRequestTypeDef(TypedDict):
    assessmentTargetName: str
    resourceGroupArn: NotRequired[str]

class CreateExclusionsPreviewRequestTypeDef(TypedDict):
    assessmentTemplateArn: str

class ResourceGroupTagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class DeleteAssessmentRunRequestTypeDef(TypedDict):
    assessmentRunArn: str

class DeleteAssessmentTargetRequestTypeDef(TypedDict):
    assessmentTargetArn: str

class DeleteAssessmentTemplateRequestTypeDef(TypedDict):
    assessmentTemplateArn: str

class DescribeAssessmentRunsRequestTypeDef(TypedDict):
    assessmentRunArns: Sequence[str]

class DescribeAssessmentTargetsRequestTypeDef(TypedDict):
    assessmentTargetArns: Sequence[str]

class DescribeAssessmentTemplatesRequestTypeDef(TypedDict):
    assessmentTemplateArns: Sequence[str]

class DescribeExclusionsRequestTypeDef(TypedDict):
    exclusionArns: Sequence[str]
    locale: NotRequired[Literal["EN_US"]]

class DescribeFindingsRequestTypeDef(TypedDict):
    findingArns: Sequence[str]
    locale: NotRequired[Literal["EN_US"]]

class DescribeResourceGroupsRequestTypeDef(TypedDict):
    resourceGroupArns: Sequence[str]

class DescribeRulesPackagesRequestTypeDef(TypedDict):
    rulesPackageArns: Sequence[str]
    locale: NotRequired[Literal["EN_US"]]

class RulesPackageTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    provider: str
    description: NotRequired[str]

class EventSubscriptionTypeDef(TypedDict):
    event: InspectorEventType
    subscribedAt: datetime

class ScopeTypeDef(TypedDict):
    key: NotRequired[ScopeTypeType]
    value: NotRequired[str]

class InspectorServiceAttributesTypeDef(TypedDict):
    schemaVersion: int
    assessmentRunArn: NotRequired[str]
    rulesPackageArn: NotRequired[str]

class GetAssessmentReportRequestTypeDef(TypedDict):
    assessmentRunArn: str
    reportFileFormat: ReportFileFormatType
    reportType: ReportTypeType

class GetExclusionsPreviewRequestTypeDef(TypedDict):
    assessmentTemplateArn: str
    previewToken: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    locale: NotRequired[Literal["EN_US"]]

class GetTelemetryMetadataRequestTypeDef(TypedDict):
    assessmentRunArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEventSubscriptionsRequestTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListExclusionsRequestTypeDef(TypedDict):
    assessmentRunArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListRulesPackagesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PrivateIpTypeDef(TypedDict):
    privateDnsName: NotRequired[str]
    privateIpAddress: NotRequired[str]

class SecurityGroupTypeDef(TypedDict):
    groupName: NotRequired[str]
    groupId: NotRequired[str]

class PreviewAgentsRequestTypeDef(TypedDict):
    previewAgentsArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class RegisterCrossAccountAccessRoleRequestTypeDef(TypedDict):
    roleArn: str

class RemoveAttributesFromFindingsRequestTypeDef(TypedDict):
    findingArns: Sequence[str]
    attributeKeys: Sequence[str]

class StartAssessmentRunRequestTypeDef(TypedDict):
    assessmentTemplateArn: str
    assessmentRunName: NotRequired[str]

class StopAssessmentRunRequestTypeDef(TypedDict):
    assessmentRunArn: str
    stopAction: NotRequired[StopActionType]

class SubscribeToEventRequestTypeDef(TypedDict):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

TimestampTypeDef = Union[datetime, str]

class UnsubscribeFromEventRequestTypeDef(TypedDict):
    resourceArn: str
    event: InspectorEventType
    topicArn: str

class UpdateAssessmentTargetRequestTypeDef(TypedDict):
    assessmentTargetArn: str
    assessmentTargetName: str
    resourceGroupArn: NotRequired[str]

class AddAttributesToFindingsRequestTypeDef(TypedDict):
    findingArns: Sequence[str]
    attributes: Sequence[AttributeTypeDef]

class AssessmentTemplateTypeDef(TypedDict):
    arn: str
    name: str
    assessmentTargetArn: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[AttributeTypeDef]
    assessmentRunCount: int
    createdAt: datetime
    lastAssessmentRunArn: NotRequired[str]

class CreateAssessmentTemplateRequestTypeDef(TypedDict):
    assessmentTargetArn: str
    assessmentTemplateName: str
    durationInSeconds: int
    rulesPackageArns: Sequence[str]
    userAttributesForFindings: NotRequired[Sequence[AttributeTypeDef]]

class AddAttributesToFindingsResponseTypeDef(TypedDict):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTargetResponseTypeDef(TypedDict):
    assessmentTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentTemplateResponseTypeDef(TypedDict):
    assessmentTemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExclusionsPreviewResponseTypeDef(TypedDict):
    previewToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceGroupResponseTypeDef(TypedDict):
    resourceGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCrossAccountAccessRoleResponseTypeDef(TypedDict):
    roleArn: str
    valid: bool
    registeredAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentReportResponseTypeDef(TypedDict):
    status: ReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunsResponseTypeDef(TypedDict):
    assessmentRunArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssessmentTargetsResponseTypeDef(TypedDict):
    assessmentTargetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssessmentTemplatesResponseTypeDef(TypedDict):
    assessmentTemplateArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListExclusionsResponseTypeDef(TypedDict):
    exclusionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFindingsResponseTypeDef(TypedDict):
    findingArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRulesPackagesResponseTypeDef(TypedDict):
    rulesPackageArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RemoveAttributesFromFindingsResponseTypeDef(TypedDict):
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentRunResponseTypeDef(TypedDict):
    assessmentRunArn: str
    ResponseMetadata: ResponseMetadataTypeDef

ListAssessmentRunAgentsRequestTypeDef = TypedDict(
    "ListAssessmentRunAgentsRequestTypeDef",
    {
        "assessmentRunArn": str,
        "filter": NotRequired[AgentFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class PreviewAgentsResponseTypeDef(TypedDict):
    agentPreviews: List[AgentPreviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssessmentRunAgentTypeDef(TypedDict):
    agentId: str
    assessmentRunArn: str
    agentHealth: AgentHealthType
    agentHealthCode: AgentHealthCodeType
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    agentHealthDetails: NotRequired[str]
    autoScalingGroup: NotRequired[str]

class GetTelemetryMetadataResponseTypeDef(TypedDict):
    telemetryMetadata: List[TelemetryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTemplateFilterTypeDef(TypedDict):
    namePattern: NotRequired[str]
    durationRange: NotRequired[DurationRangeTypeDef]
    rulesPackageArns: NotRequired[Sequence[str]]

class AssessmentRunTypeDef(TypedDict):
    arn: str
    name: str
    assessmentTemplateArn: str
    state: AssessmentRunStateType
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List[AttributeTypeDef]
    createdAt: datetime
    stateChangedAt: datetime
    dataCollected: bool
    stateChanges: List[AssessmentRunStateChangeTypeDef]
    notifications: List[AssessmentRunNotificationTypeDef]
    findingCounts: Dict[SeverityType, int]
    startedAt: NotRequired[datetime]
    completedAt: NotRequired[datetime]

ListAssessmentTargetsRequestTypeDef = TypedDict(
    "ListAssessmentTargetsRequestTypeDef",
    {
        "filter": NotRequired[AssessmentTargetFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class DescribeAssessmentTargetsResponseTypeDef(TypedDict):
    assessmentTargets: List[AssessmentTargetTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateResourceGroupRequestTypeDef(TypedDict):
    resourceGroupTags: Sequence[ResourceGroupTagTypeDef]

class ResourceGroupTypeDef(TypedDict):
    arn: str
    tags: List[ResourceGroupTagTypeDef]
    createdAt: datetime

class DescribeRulesPackagesResponseTypeDef(TypedDict):
    rulesPackages: List[RulesPackageTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTypeDef(TypedDict):
    resourceArn: str
    topicArn: str
    eventSubscriptions: List[EventSubscriptionTypeDef]

class ExclusionPreviewTypeDef(TypedDict):
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: NotRequired[List[AttributeTypeDef]]

class ExclusionTypeDef(TypedDict):
    arn: str
    title: str
    description: str
    recommendation: str
    scopes: List[ScopeTypeDef]
    attributes: NotRequired[List[AttributeTypeDef]]

ListAssessmentRunAgentsRequestPaginateTypeDef = TypedDict(
    "ListAssessmentRunAgentsRequestPaginateTypeDef",
    {
        "assessmentRunArn": str,
        "filter": NotRequired[AgentFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentTargetsRequestPaginateTypeDef = TypedDict(
    "ListAssessmentTargetsRequestPaginateTypeDef",
    {
        "filter": NotRequired[AssessmentTargetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListEventSubscriptionsRequestPaginateTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExclusionsRequestPaginateTypeDef(TypedDict):
    assessmentRunArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesPackagesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class PreviewAgentsRequestPaginateTypeDef(TypedDict):
    previewAgentsArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class NetworkInterfaceTypeDef(TypedDict):
    networkInterfaceId: NotRequired[str]
    subnetId: NotRequired[str]
    vpcId: NotRequired[str]
    privateDnsName: NotRequired[str]
    privateIpAddress: NotRequired[str]
    privateIpAddresses: NotRequired[List[PrivateIpTypeDef]]
    publicDnsName: NotRequired[str]
    publicIp: NotRequired[str]
    ipv6Addresses: NotRequired[List[str]]
    securityGroups: NotRequired[List[SecurityGroupTypeDef]]

class TimestampRangeTypeDef(TypedDict):
    beginDate: NotRequired[TimestampTypeDef]
    endDate: NotRequired[TimestampTypeDef]

class DescribeAssessmentTemplatesResponseTypeDef(TypedDict):
    assessmentTemplates: List[AssessmentTemplateTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentRunAgentsResponseTypeDef(TypedDict):
    assessmentRunAgents: List[AssessmentRunAgentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListAssessmentTemplatesRequestPaginateTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestPaginateTypeDef",
    {
        "assessmentTargetArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentTemplateFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentTemplatesRequestTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestTypeDef",
    {
        "assessmentTargetArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentTemplateFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class DescribeAssessmentRunsResponseTypeDef(TypedDict):
    assessmentRuns: List[AssessmentRunTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceGroupsResponseTypeDef(TypedDict):
    resourceGroups: List[ResourceGroupTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSubscriptionsResponseTypeDef(TypedDict):
    subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetExclusionsPreviewResponseTypeDef(TypedDict):
    previewStatus: PreviewStatusType
    exclusionPreviews: List[ExclusionPreviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeExclusionsResponseTypeDef(TypedDict):
    exclusions: Dict[str, ExclusionTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssetAttributesTypeDef(TypedDict):
    schemaVersion: int
    agentId: NotRequired[str]
    autoScalingGroup: NotRequired[str]
    amiId: NotRequired[str]
    hostname: NotRequired[str]
    ipv4Addresses: NotRequired[List[str]]
    tags: NotRequired[List[TagTypeDef]]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]

class AssessmentRunFilterTypeDef(TypedDict):
    namePattern: NotRequired[str]
    states: NotRequired[Sequence[AssessmentRunStateType]]
    durationRange: NotRequired[DurationRangeTypeDef]
    rulesPackageArns: NotRequired[Sequence[str]]
    startTimeRange: NotRequired[TimestampRangeTypeDef]
    completionTimeRange: NotRequired[TimestampRangeTypeDef]
    stateChangeTimeRange: NotRequired[TimestampRangeTypeDef]

class FindingFilterTypeDef(TypedDict):
    agentIds: NotRequired[Sequence[str]]
    autoScalingGroups: NotRequired[Sequence[str]]
    ruleNames: NotRequired[Sequence[str]]
    severities: NotRequired[Sequence[SeverityType]]
    rulesPackageArns: NotRequired[Sequence[str]]
    attributes: NotRequired[Sequence[AttributeTypeDef]]
    userAttributes: NotRequired[Sequence[AttributeTypeDef]]
    creationTimeRange: NotRequired[TimestampRangeTypeDef]

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "arn": str,
        "attributes": List[AttributeTypeDef],
        "userAttributes": List[AttributeTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
        "schemaVersion": NotRequired[int],
        "service": NotRequired[str],
        "serviceAttributes": NotRequired[InspectorServiceAttributesTypeDef],
        "assetType": NotRequired[Literal["ec2-instance"]],
        "assetAttributes": NotRequired[AssetAttributesTypeDef],
        "id": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "recommendation": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "numericSeverity": NotRequired[float],
        "confidence": NotRequired[int],
        "indicatorOfCompromise": NotRequired[bool],
    },
)
ListAssessmentRunsRequestPaginateTypeDef = TypedDict(
    "ListAssessmentRunsRequestPaginateTypeDef",
    {
        "assessmentTemplateArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentRunFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentRunsRequestTypeDef = TypedDict(
    "ListAssessmentRunsRequestTypeDef",
    {
        "assessmentTemplateArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentRunFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsRequestPaginateTypeDef = TypedDict(
    "ListFindingsRequestPaginateTypeDef",
    {
        "assessmentRunArns": NotRequired[Sequence[str]],
        "filter": NotRequired[FindingFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestTypeDef = TypedDict(
    "ListFindingsRequestTypeDef",
    {
        "assessmentRunArns": NotRequired[Sequence[str]],
        "filter": NotRequired[FindingFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class DescribeFindingsResponseTypeDef(TypedDict):
    findings: List[FindingTypeDef]
    failedItems: Dict[str, FailedItemDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
