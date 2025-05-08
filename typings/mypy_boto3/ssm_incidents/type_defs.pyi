"""
Type annotations for ssm-incidents service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ssm_incidents.type_defs import AddRegionActionTypeDef

    data: AddRegionActionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
    VariableTypeType,
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
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ActionUnionTypeDef",
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "BatchGetIncidentFindingsErrorTypeDef",
    "BatchGetIncidentFindingsInputTypeDef",
    "BatchGetIncidentFindingsOutputTypeDef",
    "ChatChannelOutputTypeDef",
    "ChatChannelTypeDef",
    "ChatChannelUnionTypeDef",
    "CloudFormationStackUpdateTypeDef",
    "CodeDeployDeploymentTypeDef",
    "ConditionTypeDef",
    "CreateReplicationSetInputTypeDef",
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanInputTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventInputTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "DeleteIncidentRecordInputTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputTypeDef",
    "DeleteResourcePolicyInputTypeDef",
    "DeleteResponsePlanInputTypeDef",
    "DeleteTimelineEventInputTypeDef",
    "DynamicSsmParameterValueTypeDef",
    "EventReferenceTypeDef",
    "EventSummaryTypeDef",
    "FilterTypeDef",
    "FindingDetailsTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GetIncidentRecordInputTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "GetReplicationSetInputTypeDef",
    "GetReplicationSetInputWaitExtraTypeDef",
    "GetReplicationSetInputWaitTypeDef",
    "GetReplicationSetOutputTypeDef",
    "GetResourcePoliciesInputPaginateTypeDef",
    "GetResourcePoliciesInputTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "GetResponsePlanInputTypeDef",
    "GetResponsePlanOutputTypeDef",
    "GetTimelineEventInputTypeDef",
    "GetTimelineEventOutputTypeDef",
    "IncidentRecordSourceTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateOutputTypeDef",
    "IncidentTemplateTypeDef",
    "IncidentTemplateUnionTypeDef",
    "IntegrationTypeDef",
    "ItemIdentifierTypeDef",
    "ItemValueTypeDef",
    "ListIncidentFindingsInputPaginateTypeDef",
    "ListIncidentFindingsInputTypeDef",
    "ListIncidentFindingsOutputTypeDef",
    "ListIncidentRecordsInputPaginateTypeDef",
    "ListIncidentRecordsInputTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "ListRelatedItemsInputPaginateTypeDef",
    "ListRelatedItemsInputTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "ListReplicationSetsInputPaginateTypeDef",
    "ListReplicationSetsInputTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListResponsePlansInputPaginateTypeDef",
    "ListResponsePlansInputTypeDef",
    "ListResponsePlansOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimelineEventsInputPaginateTypeDef",
    "ListTimelineEventsInputTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "NotificationTargetItemTypeDef",
    "PagerDutyConfigurationTypeDef",
    "PagerDutyIncidentConfigurationTypeDef",
    "PagerDutyIncidentDetailTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyInputTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegionInfoTypeDef",
    "RegionMapInputValueTypeDef",
    "RelatedItemTypeDef",
    "RelatedItemsUpdateTypeDef",
    "ReplicationSetTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePlanSummaryTypeDef",
    "SsmAutomationOutputTypeDef",
    "SsmAutomationTypeDef",
    "SsmAutomationUnionTypeDef",
    "StartIncidentInputTypeDef",
    "StartIncidentOutputTypeDef",
    "TagResourceRequestTypeDef",
    "TimelineEventTypeDef",
    "TimestampTypeDef",
    "TriggerDetailsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeletionProtectionInputTypeDef",
    "UpdateIncidentRecordInputTypeDef",
    "UpdateRelatedItemsInputTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "UpdateReplicationSetInputTypeDef",
    "UpdateResponsePlanInputTypeDef",
    "UpdateTimelineEventInputTypeDef",
    "WaiterConfigTypeDef",
)

class AddRegionActionTypeDef(TypedDict):
    regionName: str
    sseKmsKeyId: NotRequired[str]

class AttributeValueListTypeDef(TypedDict):
    integerValues: NotRequired[Sequence[int]]
    stringValues: NotRequired[Sequence[str]]

class AutomationExecutionTypeDef(TypedDict):
    ssmExecutionArn: NotRequired[str]

class BatchGetIncidentFindingsErrorTypeDef(TypedDict):
    code: str
    findingId: str
    message: str

class BatchGetIncidentFindingsInputTypeDef(TypedDict):
    findingIds: Sequence[str]
    incidentRecordArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ChatChannelOutputTypeDef(TypedDict):
    chatbotSns: NotRequired[List[str]]
    empty: NotRequired[Dict[str, Any]]

class ChatChannelTypeDef(TypedDict):
    chatbotSns: NotRequired[Sequence[str]]
    empty: NotRequired[Mapping[str, Any]]

class CloudFormationStackUpdateTypeDef(TypedDict):
    stackArn: str
    startTime: datetime
    endTime: NotRequired[datetime]

class CodeDeployDeploymentTypeDef(TypedDict):
    deploymentGroupArn: str
    deploymentId: str
    startTime: datetime
    endTime: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class RegionMapInputValueTypeDef(TypedDict):
    sseKmsKeyId: NotRequired[str]

class EventReferenceTypeDef(TypedDict):
    relatedItemId: NotRequired[str]
    resource: NotRequired[str]

class DeleteIncidentRecordInputTypeDef(TypedDict):
    arn: str

class DeleteRegionActionTypeDef(TypedDict):
    regionName: str

class DeleteReplicationSetInputTypeDef(TypedDict):
    arn: str

class DeleteResourcePolicyInputTypeDef(TypedDict):
    policyId: str
    resourceArn: str

class DeleteResponsePlanInputTypeDef(TypedDict):
    arn: str

class DeleteTimelineEventInputTypeDef(TypedDict):
    eventId: str
    incidentRecordArn: str

class DynamicSsmParameterValueTypeDef(TypedDict):
    variable: NotRequired[VariableTypeType]

FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "id": str,
        "lastModifiedTime": datetime,
    },
)

class GetIncidentRecordInputTypeDef(TypedDict):
    arn: str

class GetReplicationSetInputTypeDef(TypedDict):
    arn: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetResourcePoliciesInputTypeDef(TypedDict):
    resourceArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ResourcePolicyTypeDef(TypedDict):
    policyDocument: str
    policyId: str
    ramResourceShareRegion: str

class GetResponsePlanInputTypeDef(TypedDict):
    arn: str

class GetTimelineEventInputTypeDef(TypedDict):
    eventId: str
    incidentRecordArn: str

class IncidentRecordSourceTypeDef(TypedDict):
    createdBy: str
    source: str
    invokedBy: NotRequired[str]
    resourceArn: NotRequired[str]

class NotificationTargetItemTypeDef(TypedDict):
    snsTopicArn: NotRequired[str]

PagerDutyIncidentDetailTypeDef = TypedDict(
    "PagerDutyIncidentDetailTypeDef",
    {
        "id": str,
        "autoResolve": NotRequired[bool],
        "secretId": NotRequired[str],
    },
)

class ListIncidentFindingsInputTypeDef(TypedDict):
    incidentRecordArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRelatedItemsInputTypeDef(TypedDict):
    incidentRecordArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListReplicationSetsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListResponsePlansInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ResponsePlanSummaryTypeDef(TypedDict):
    arn: str
    name: str
    displayName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PagerDutyIncidentConfigurationTypeDef(TypedDict):
    serviceId: str

class PutResourcePolicyInputTypeDef(TypedDict):
    policy: str
    resourceArn: str

class RegionInfoTypeDef(TypedDict):
    status: RegionStatusType
    statusUpdateDateTime: datetime
    sseKmsKeyId: NotRequired[str]
    statusMessage: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDeletionProtectionInputTypeDef(TypedDict):
    arn: str
    deletionProtected: bool
    clientToken: NotRequired[str]

class CreateReplicationSetOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResponsePlanOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTimelineEventOutputTypeDef(TypedDict):
    eventId: str
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReplicationSetsOutputTypeDef(TypedDict):
    replicationSetArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyOutputTypeDef(TypedDict):
    policyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartIncidentOutputTypeDef(TypedDict):
    incidentRecordArn: str
    ResponseMetadata: ResponseMetadataTypeDef

ChatChannelUnionTypeDef = Union[ChatChannelTypeDef, ChatChannelOutputTypeDef]

class FindingDetailsTypeDef(TypedDict):
    cloudFormationStackUpdate: NotRequired[CloudFormationStackUpdateTypeDef]
    codeDeployDeployment: NotRequired[CodeDeployDeploymentTypeDef]

class ConditionTypeDef(TypedDict):
    after: NotRequired[TimestampTypeDef]
    before: NotRequired[TimestampTypeDef]
    equals: NotRequired[AttributeValueListTypeDef]

class TriggerDetailsTypeDef(TypedDict):
    source: str
    timestamp: TimestampTypeDef
    rawData: NotRequired[str]
    triggerArn: NotRequired[str]

class CreateReplicationSetInputTypeDef(TypedDict):
    regions: Mapping[str, RegionMapInputValueTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateTimelineEventInputTypeDef(TypedDict):
    eventData: str
    eventTime: TimestampTypeDef
    eventType: str
    incidentRecordArn: str
    clientToken: NotRequired[str]
    eventReferences: NotRequired[Sequence[EventReferenceTypeDef]]

class EventSummaryTypeDef(TypedDict):
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: NotRequired[List[EventReferenceTypeDef]]

class TimelineEventTypeDef(TypedDict):
    eventData: str
    eventId: str
    eventTime: datetime
    eventType: str
    eventUpdatedTime: datetime
    incidentRecordArn: str
    eventReferences: NotRequired[List[EventReferenceTypeDef]]

class UpdateTimelineEventInputTypeDef(TypedDict):
    eventId: str
    incidentRecordArn: str
    clientToken: NotRequired[str]
    eventData: NotRequired[str]
    eventReferences: NotRequired[Sequence[EventReferenceTypeDef]]
    eventTime: NotRequired[TimestampTypeDef]
    eventType: NotRequired[str]

class UpdateReplicationSetActionTypeDef(TypedDict):
    addRegionAction: NotRequired[AddRegionActionTypeDef]
    deleteRegionAction: NotRequired[DeleteRegionActionTypeDef]

class SsmAutomationOutputTypeDef(TypedDict):
    documentName: str
    roleArn: str
    documentVersion: NotRequired[str]
    dynamicParameters: NotRequired[Dict[str, DynamicSsmParameterValueTypeDef]]
    parameters: NotRequired[Dict[str, List[str]]]
    targetAccount: NotRequired[SsmTargetAccountType]

class SsmAutomationTypeDef(TypedDict):
    documentName: str
    roleArn: str
    documentVersion: NotRequired[str]
    dynamicParameters: NotRequired[Mapping[str, DynamicSsmParameterValueTypeDef]]
    parameters: NotRequired[Mapping[str, Sequence[str]]]
    targetAccount: NotRequired[SsmTargetAccountType]

class ListIncidentFindingsOutputTypeDef(TypedDict):
    findings: List[FindingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetReplicationSetInputWaitExtraTypeDef(TypedDict):
    arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetReplicationSetInputWaitTypeDef(TypedDict):
    arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetResourcePoliciesInputPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIncidentFindingsInputPaginateTypeDef(TypedDict):
    incidentRecordArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRelatedItemsInputPaginateTypeDef(TypedDict):
    incidentRecordArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReplicationSetsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResponsePlansInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourcePoliciesOutputTypeDef(TypedDict):
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IncidentRecordSummaryTypeDef(TypedDict):
    arn: str
    creationTime: datetime
    impact: int
    incidentRecordSource: IncidentRecordSourceTypeDef
    status: IncidentRecordStatusType
    title: str
    resolvedTime: NotRequired[datetime]

class IncidentRecordTypeDef(TypedDict):
    arn: str
    creationTime: datetime
    dedupeString: str
    impact: int
    incidentRecordSource: IncidentRecordSourceTypeDef
    lastModifiedBy: str
    lastModifiedTime: datetime
    status: IncidentRecordStatusType
    title: str
    automationExecutions: NotRequired[List[AutomationExecutionTypeDef]]
    chatChannel: NotRequired[ChatChannelOutputTypeDef]
    notificationTargets: NotRequired[List[NotificationTargetItemTypeDef]]
    resolvedTime: NotRequired[datetime]
    summary: NotRequired[str]

class IncidentTemplateOutputTypeDef(TypedDict):
    impact: int
    title: str
    dedupeString: NotRequired[str]
    incidentTags: NotRequired[Dict[str, str]]
    notificationTargets: NotRequired[List[NotificationTargetItemTypeDef]]
    summary: NotRequired[str]

class IncidentTemplateTypeDef(TypedDict):
    impact: int
    title: str
    dedupeString: NotRequired[str]
    incidentTags: NotRequired[Mapping[str, str]]
    notificationTargets: NotRequired[Sequence[NotificationTargetItemTypeDef]]
    summary: NotRequired[str]

class ItemValueTypeDef(TypedDict):
    arn: NotRequired[str]
    metricDefinition: NotRequired[str]
    pagerDutyIncidentDetail: NotRequired[PagerDutyIncidentDetailTypeDef]
    url: NotRequired[str]

class ListResponsePlansOutputTypeDef(TypedDict):
    responsePlanSummaries: List[ResponsePlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PagerDutyConfigurationTypeDef(TypedDict):
    name: str
    pagerDutyIncidentConfiguration: PagerDutyIncidentConfigurationTypeDef
    secretId: str

class ReplicationSetTypeDef(TypedDict):
    createdBy: str
    createdTime: datetime
    deletionProtected: bool
    lastModifiedBy: str
    lastModifiedTime: datetime
    regionMap: Dict[str, RegionInfoTypeDef]
    status: ReplicationSetStatusType
    arn: NotRequired[str]

class UpdateIncidentRecordInputTypeDef(TypedDict):
    arn: str
    chatChannel: NotRequired[ChatChannelUnionTypeDef]
    clientToken: NotRequired[str]
    impact: NotRequired[int]
    notificationTargets: NotRequired[Sequence[NotificationTargetItemTypeDef]]
    status: NotRequired[IncidentRecordStatusType]
    summary: NotRequired[str]
    title: NotRequired[str]

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "creationTime": datetime,
        "id": str,
        "lastModifiedTime": datetime,
        "details": NotRequired[FindingDetailsTypeDef],
    },
)

class FilterTypeDef(TypedDict):
    condition: ConditionTypeDef
    key: str

class ListTimelineEventsOutputTypeDef(TypedDict):
    eventSummaries: List[EventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetTimelineEventOutputTypeDef(TypedDict):
    event: TimelineEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationSetInputTypeDef(TypedDict):
    actions: Sequence[UpdateReplicationSetActionTypeDef]
    arn: str
    clientToken: NotRequired[str]

class ActionOutputTypeDef(TypedDict):
    ssmAutomation: NotRequired[SsmAutomationOutputTypeDef]

SsmAutomationUnionTypeDef = Union[SsmAutomationTypeDef, SsmAutomationOutputTypeDef]

class ListIncidentRecordsOutputTypeDef(TypedDict):
    incidentRecordSummaries: List[IncidentRecordSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetIncidentRecordOutputTypeDef(TypedDict):
    incidentRecord: IncidentRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

IncidentTemplateUnionTypeDef = Union[IncidentTemplateTypeDef, IncidentTemplateOutputTypeDef]
ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": ItemValueTypeDef,
    },
)

class IntegrationTypeDef(TypedDict):
    pagerDutyConfiguration: NotRequired[PagerDutyConfigurationTypeDef]

class GetReplicationSetOutputTypeDef(TypedDict):
    replicationSet: ReplicationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetIncidentFindingsOutputTypeDef(TypedDict):
    errors: List[BatchGetIncidentFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListIncidentRecordsInputPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIncidentRecordsInputTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTimelineEventsInputPaginateTypeDef(TypedDict):
    incidentRecordArn: str
    filters: NotRequired[Sequence[FilterTypeDef]]
    sortBy: NotRequired[Literal["EVENT_TIME"]]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTimelineEventsInputTypeDef(TypedDict):
    incidentRecordArn: str
    filters: NotRequired[Sequence[FilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[Literal["EVENT_TIME"]]
    sortOrder: NotRequired[SortOrderType]

class ActionTypeDef(TypedDict):
    ssmAutomation: NotRequired[SsmAutomationUnionTypeDef]

class RelatedItemTypeDef(TypedDict):
    identifier: ItemIdentifierTypeDef
    generatedId: NotRequired[str]
    title: NotRequired[str]

class GetResponsePlanOutputTypeDef(TypedDict):
    actions: List[ActionOutputTypeDef]
    arn: str
    chatChannel: ChatChannelOutputTypeDef
    displayName: str
    engagements: List[str]
    incidentTemplate: IncidentTemplateOutputTypeDef
    integrations: List[IntegrationTypeDef]
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]

class ListRelatedItemsOutputTypeDef(TypedDict):
    relatedItems: List[RelatedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RelatedItemsUpdateTypeDef(TypedDict):
    itemToAdd: NotRequired[RelatedItemTypeDef]
    itemToRemove: NotRequired[ItemIdentifierTypeDef]

class StartIncidentInputTypeDef(TypedDict):
    responsePlanArn: str
    clientToken: NotRequired[str]
    impact: NotRequired[int]
    relatedItems: NotRequired[Sequence[RelatedItemTypeDef]]
    title: NotRequired[str]
    triggerDetails: NotRequired[TriggerDetailsTypeDef]

class CreateResponsePlanInputTypeDef(TypedDict):
    incidentTemplate: IncidentTemplateUnionTypeDef
    name: str
    actions: NotRequired[Sequence[ActionUnionTypeDef]]
    chatChannel: NotRequired[ChatChannelUnionTypeDef]
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    engagements: NotRequired[Sequence[str]]
    integrations: NotRequired[Sequence[IntegrationTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class UpdateResponsePlanInputTypeDef(TypedDict):
    arn: str
    actions: NotRequired[Sequence[ActionUnionTypeDef]]
    chatChannel: NotRequired[ChatChannelUnionTypeDef]
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    engagements: NotRequired[Sequence[str]]
    incidentTemplateDedupeString: NotRequired[str]
    incidentTemplateImpact: NotRequired[int]
    incidentTemplateNotificationTargets: NotRequired[Sequence[NotificationTargetItemTypeDef]]
    incidentTemplateSummary: NotRequired[str]
    incidentTemplateTags: NotRequired[Mapping[str, str]]
    incidentTemplateTitle: NotRequired[str]
    integrations: NotRequired[Sequence[IntegrationTypeDef]]

class UpdateRelatedItemsInputTypeDef(TypedDict):
    incidentRecordArn: str
    relatedItemsUpdate: RelatedItemsUpdateTypeDef
    clientToken: NotRequired[str]
