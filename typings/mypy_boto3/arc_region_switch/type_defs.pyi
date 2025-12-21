"""
Type annotations for arc-region-switch service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_arc_region_switch.type_defs import AbbreviatedExecutionTypeDef

    data: AbbreviatedExecutionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AlarmConditionType,
    AlarmTypeType,
    ApprovalType,
    DocumentDbDefaultBehaviorType,
    Ec2AsgCapacityMonitoringApproachType,
    EcsCapacityMonitoringApproachType,
    EvaluationStatusType,
    ExecutionActionType,
    ExecutionBlockTypeType,
    ExecutionEventTypeType,
    ExecutionModeType,
    ExecutionStateType,
    FailedReportErrorCodeType,
    GlobalAuroraDefaultBehaviorType,
    RecoveryApproachType,
    RegionToRunInType,
    ResourceWarningStatusType,
    Route53HealthCheckStatusType,
    RoutingControlStateChangeType,
    StepStatusType,
    UpdatePlanExecutionActionType,
    UpdatePlanExecutionStepActionType,
    WorkflowTargetActionType,
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
    "AbbreviatedExecutionTypeDef",
    "AbbreviatedPlanTypeDef",
    "ApprovePlanExecutionStepRequestTypeDef",
    "ArcRoutingControlConfigurationOutputTypeDef",
    "ArcRoutingControlConfigurationTypeDef",
    "ArcRoutingControlConfigurationUnionTypeDef",
    "ArcRoutingControlStateTypeDef",
    "AsgTypeDef",
    "AssociatedAlarmTypeDef",
    "CancelPlanExecutionRequestTypeDef",
    "CreatePlanRequestTypeDef",
    "CreatePlanResponseTypeDef",
    "CustomActionLambdaConfigurationOutputTypeDef",
    "CustomActionLambdaConfigurationTypeDef",
    "CustomActionLambdaConfigurationUnionTypeDef",
    "DeletePlanRequestTypeDef",
    "DocumentDbConfigurationOutputTypeDef",
    "DocumentDbConfigurationTypeDef",
    "DocumentDbConfigurationUnionTypeDef",
    "DocumentDbUngracefulTypeDef",
    "Ec2AsgCapacityIncreaseConfigurationOutputTypeDef",
    "Ec2AsgCapacityIncreaseConfigurationTypeDef",
    "Ec2AsgCapacityIncreaseConfigurationUnionTypeDef",
    "Ec2UngracefulTypeDef",
    "EcsCapacityIncreaseConfigurationOutputTypeDef",
    "EcsCapacityIncreaseConfigurationTypeDef",
    "EcsCapacityIncreaseConfigurationUnionTypeDef",
    "EcsUngracefulTypeDef",
    "EksClusterTypeDef",
    "EksResourceScalingConfigurationOutputTypeDef",
    "EksResourceScalingConfigurationTypeDef",
    "EksResourceScalingConfigurationUnionTypeDef",
    "EksResourceScalingUngracefulTypeDef",
    "ExecutionApprovalConfigurationTypeDef",
    "ExecutionBlockConfigurationOutputTypeDef",
    "ExecutionBlockConfigurationPaginatorTypeDef",
    "ExecutionBlockConfigurationTypeDef",
    "ExecutionBlockConfigurationUnionTypeDef",
    "ExecutionEventTypeDef",
    "FailedReportOutputTypeDef",
    "GeneratedReportTypeDef",
    "GetPlanEvaluationStatusRequestPaginateTypeDef",
    "GetPlanEvaluationStatusRequestTypeDef",
    "GetPlanEvaluationStatusRequestWaitTypeDef",
    "GetPlanEvaluationStatusResponseTypeDef",
    "GetPlanExecutionRequestPaginateTypeDef",
    "GetPlanExecutionRequestTypeDef",
    "GetPlanExecutionRequestWaitTypeDef",
    "GetPlanExecutionResponsePaginatorTypeDef",
    "GetPlanExecutionResponseTypeDef",
    "GetPlanInRegionRequestTypeDef",
    "GetPlanInRegionResponseTypeDef",
    "GetPlanRequestTypeDef",
    "GetPlanResponseTypeDef",
    "GlobalAuroraConfigurationOutputTypeDef",
    "GlobalAuroraConfigurationTypeDef",
    "GlobalAuroraConfigurationUnionTypeDef",
    "GlobalAuroraUngracefulTypeDef",
    "KubernetesResourceTypeTypeDef",
    "KubernetesScalingResourceTypeDef",
    "LambdaUngracefulTypeDef",
    "LambdasTypeDef",
    "ListPlanExecutionEventsRequestPaginateTypeDef",
    "ListPlanExecutionEventsRequestTypeDef",
    "ListPlanExecutionEventsResponseTypeDef",
    "ListPlanExecutionsRequestPaginateTypeDef",
    "ListPlanExecutionsRequestTypeDef",
    "ListPlanExecutionsResponseTypeDef",
    "ListPlansInRegionRequestPaginateTypeDef",
    "ListPlansInRegionRequestTypeDef",
    "ListPlansInRegionResponseTypeDef",
    "ListPlansRequestPaginateTypeDef",
    "ListPlansRequestTypeDef",
    "ListPlansResponseTypeDef",
    "ListRoute53HealthChecksInRegionRequestPaginateTypeDef",
    "ListRoute53HealthChecksInRegionRequestTypeDef",
    "ListRoute53HealthChecksInRegionResponseTypeDef",
    "ListRoute53HealthChecksRequestPaginateTypeDef",
    "ListRoute53HealthChecksRequestTypeDef",
    "ListRoute53HealthChecksResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MinimalWorkflowTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelExecutionBlockConfigurationOutputTypeDef",
    "ParallelExecutionBlockConfigurationPaginatorTypeDef",
    "ParallelExecutionBlockConfigurationTypeDef",
    "ParallelExecutionBlockConfigurationUnionTypeDef",
    "PlanPaginatorTypeDef",
    "PlanTypeDef",
    "RegionSwitchPlanConfigurationTypeDef",
    "ReportConfigurationOutputTypeDef",
    "ReportConfigurationTypeDef",
    "ReportConfigurationUnionTypeDef",
    "ReportOutputConfigurationTypeDef",
    "ReportOutputTypeDef",
    "ResourceWarningTypeDef",
    "ResponseMetadataTypeDef",
    "Route53HealthCheckConfigurationOutputTypeDef",
    "Route53HealthCheckConfigurationTypeDef",
    "Route53HealthCheckConfigurationUnionTypeDef",
    "Route53HealthCheckTypeDef",
    "Route53ResourceRecordSetTypeDef",
    "S3ReportOutputConfigurationTypeDef",
    "S3ReportOutputTypeDef",
    "ServiceTypeDef",
    "StartPlanExecutionRequestTypeDef",
    "StartPlanExecutionResponseTypeDef",
    "StepOutputTypeDef",
    "StepPaginatorTypeDef",
    "StepStateTypeDef",
    "StepTypeDef",
    "StepUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TriggerConditionTypeDef",
    "TriggerOutputTypeDef",
    "TriggerTypeDef",
    "TriggerUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePlanExecutionRequestTypeDef",
    "UpdatePlanExecutionStepRequestTypeDef",
    "UpdatePlanRequestTypeDef",
    "UpdatePlanResponseTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowOutputTypeDef",
    "WorkflowPaginatorTypeDef",
    "WorkflowTypeDef",
    "WorkflowUnionTypeDef",
)

class AbbreviatedExecutionTypeDef(TypedDict):
    planArn: str
    executionId: str
    startTime: datetime
    mode: ExecutionModeType
    executionState: ExecutionStateType
    executionAction: ExecutionActionType
    executionRegion: str
    version: NotRequired[str]
    updatedAt: NotRequired[datetime]
    comment: NotRequired[str]
    endTime: NotRequired[datetime]
    actualRecoveryTime: NotRequired[str]

class AbbreviatedPlanTypeDef(TypedDict):
    arn: str
    owner: str
    name: str
    regions: List[str]
    recoveryApproach: RecoveryApproachType
    primaryRegion: NotRequired[str]
    version: NotRequired[str]
    updatedAt: NotRequired[datetime]
    description: NotRequired[str]
    executionRole: NotRequired[str]
    activePlanExecution: NotRequired[str]
    recoveryTimeObjectiveMinutes: NotRequired[int]

class ApprovePlanExecutionStepRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    stepName: str
    approval: ApprovalType
    comment: NotRequired[str]

class ArcRoutingControlStateTypeDef(TypedDict):
    routingControlArn: str
    state: RoutingControlStateChangeType

class AsgTypeDef(TypedDict):
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    arn: NotRequired[str]

class AssociatedAlarmTypeDef(TypedDict):
    resourceIdentifier: str
    alarmType: AlarmTypeType
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]

class CancelPlanExecutionRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    comment: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LambdaUngracefulTypeDef(TypedDict):
    behavior: NotRequired[Literal["skip"]]

class LambdasTypeDef(TypedDict):
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    arn: NotRequired[str]

class DeletePlanRequestTypeDef(TypedDict):
    arn: str

class DocumentDbUngracefulTypeDef(TypedDict):
    ungraceful: NotRequired[Literal["failover"]]

class Ec2UngracefulTypeDef(TypedDict):
    minimumSuccessPercentage: int

class EcsUngracefulTypeDef(TypedDict):
    minimumSuccessPercentage: int

class ServiceTypeDef(TypedDict):
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    clusterArn: NotRequired[str]
    serviceArn: NotRequired[str]

class EksClusterTypeDef(TypedDict):
    clusterArn: str
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]

class EksResourceScalingUngracefulTypeDef(TypedDict):
    minimumSuccessPercentage: int

class KubernetesResourceTypeTypeDef(TypedDict):
    apiVersion: str
    kind: str

class KubernetesScalingResourceTypeDef(TypedDict):
    namespace: str
    name: str
    hpaName: NotRequired[str]

class ExecutionApprovalConfigurationTypeDef(TypedDict):
    approvalRole: str
    timeoutMinutes: NotRequired[int]

class ParallelExecutionBlockConfigurationOutputTypeDef(TypedDict):
    steps: List[Dict[str, Any]]

class RegionSwitchPlanConfigurationTypeDef(TypedDict):
    arn: str
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]

class ParallelExecutionBlockConfigurationPaginatorTypeDef(TypedDict):
    steps: List[Dict[str, Any]]

ExecutionEventTypeDef = TypedDict(
    "ExecutionEventTypeDef",
    {
        "eventId": str,
        "timestamp": NotRequired[datetime],
        "type": NotRequired[ExecutionEventTypeType],
        "stepName": NotRequired[str],
        "executionBlockType": NotRequired[ExecutionBlockTypeType],
        "resources": NotRequired[List[str]],
        "error": NotRequired[str],
        "description": NotRequired[str],
        "previousEventId": NotRequired[str],
    },
)

class FailedReportOutputTypeDef(TypedDict):
    errorCode: NotRequired[FailedReportErrorCodeType]
    errorMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetPlanEvaluationStatusRequestTypeDef(TypedDict):
    planArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetPlanExecutionRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class StepStateTypeDef(TypedDict):
    name: NotRequired[str]
    status: NotRequired[StepStatusType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    stepMode: NotRequired[ExecutionModeType]

class GetPlanInRegionRequestTypeDef(TypedDict):
    arn: str

class GetPlanRequestTypeDef(TypedDict):
    arn: str

class GlobalAuroraUngracefulTypeDef(TypedDict):
    ungraceful: NotRequired[Literal["failover"]]

class ListPlanExecutionEventsRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    name: NotRequired[str]

class ListPlanExecutionsRequestTypeDef(TypedDict):
    planArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    state: NotRequired[ExecutionStateType]

class ListPlansInRegionRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPlansRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRoute53HealthChecksInRegionRequestTypeDef(TypedDict):
    arn: str
    hostedZoneId: NotRequired[str]
    recordName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class Route53HealthCheckTypeDef(TypedDict):
    hostedZoneId: str
    recordName: str
    region: str
    healthCheckId: NotRequired[str]
    status: NotRequired[Route53HealthCheckStatusType]

class ListRoute53HealthChecksRequestTypeDef(TypedDict):
    arn: str
    hostedZoneId: NotRequired[str]
    recordName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    arn: str

class MinimalWorkflowTypeDef(TypedDict):
    action: NotRequired[ExecutionActionType]
    name: NotRequired[str]

class ParallelExecutionBlockConfigurationTypeDef(TypedDict):
    steps: Sequence[Mapping[str, Any]]

class S3ReportOutputConfigurationTypeDef(TypedDict):
    bucketPath: NotRequired[str]
    bucketOwner: NotRequired[str]

class S3ReportOutputTypeDef(TypedDict):
    s3ObjectKey: NotRequired[str]

class Route53ResourceRecordSetTypeDef(TypedDict):
    recordSetIdentifier: NotRequired[str]
    region: NotRequired[str]

class StartPlanExecutionRequestTypeDef(TypedDict):
    planArn: str
    targetRegion: str
    action: ExecutionActionType
    mode: NotRequired[ExecutionModeType]
    comment: NotRequired[str]
    latestVersion: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]

class TriggerConditionTypeDef(TypedDict):
    associatedAlarmName: str
    condition: AlarmConditionType

class UntagResourceRequestTypeDef(TypedDict):
    arn: str
    resourceTagKeys: Sequence[str]

class UpdatePlanExecutionRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    action: UpdatePlanExecutionActionType
    comment: NotRequired[str]

class UpdatePlanExecutionStepRequestTypeDef(TypedDict):
    planArn: str
    executionId: str
    comment: str
    stepName: str
    actionToTake: UpdatePlanExecutionStepActionType

class ArcRoutingControlConfigurationOutputTypeDef(TypedDict):
    regionAndRoutingControls: Dict[str, List[ArcRoutingControlStateTypeDef]]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]

class ArcRoutingControlConfigurationTypeDef(TypedDict):
    regionAndRoutingControls: Mapping[str, Sequence[ArcRoutingControlStateTypeDef]]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]

class ListPlanExecutionsResponseTypeDef(TypedDict):
    items: List[AbbreviatedExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPlansInRegionResponseTypeDef(TypedDict):
    plans: List[AbbreviatedPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPlansResponseTypeDef(TypedDict):
    plans: List[AbbreviatedPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    resourceTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPlanExecutionResponseTypeDef(TypedDict):
    executionId: str
    plan: str
    planVersion: str
    activateRegion: str
    deactivateRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomActionLambdaConfigurationOutputTypeDef(TypedDict):
    lambdas: List[LambdasTypeDef]
    retryIntervalMinutes: float
    regionToRun: RegionToRunInType
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[LambdaUngracefulTypeDef]

class CustomActionLambdaConfigurationTypeDef(TypedDict):
    lambdas: Sequence[LambdasTypeDef]
    retryIntervalMinutes: float
    regionToRun: RegionToRunInType
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[LambdaUngracefulTypeDef]

class DocumentDbConfigurationOutputTypeDef(TypedDict):
    behavior: DocumentDbDefaultBehaviorType
    globalClusterIdentifier: str
    databaseClusterArns: List[str]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    ungraceful: NotRequired[DocumentDbUngracefulTypeDef]

class DocumentDbConfigurationTypeDef(TypedDict):
    behavior: DocumentDbDefaultBehaviorType
    globalClusterIdentifier: str
    databaseClusterArns: Sequence[str]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    ungraceful: NotRequired[DocumentDbUngracefulTypeDef]

class Ec2AsgCapacityIncreaseConfigurationOutputTypeDef(TypedDict):
    asgs: List[AsgTypeDef]
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[Ec2UngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[Ec2AsgCapacityMonitoringApproachType]

class Ec2AsgCapacityIncreaseConfigurationTypeDef(TypedDict):
    asgs: Sequence[AsgTypeDef]
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[Ec2UngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[Ec2AsgCapacityMonitoringApproachType]

class EcsCapacityIncreaseConfigurationOutputTypeDef(TypedDict):
    services: List[ServiceTypeDef]
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[EcsUngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[EcsCapacityMonitoringApproachType]

class EcsCapacityIncreaseConfigurationTypeDef(TypedDict):
    services: Sequence[ServiceTypeDef]
    timeoutMinutes: NotRequired[int]
    ungraceful: NotRequired[EcsUngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[EcsCapacityMonitoringApproachType]

class EksResourceScalingConfigurationOutputTypeDef(TypedDict):
    kubernetesResourceType: KubernetesResourceTypeTypeDef
    timeoutMinutes: NotRequired[int]
    scalingResources: NotRequired[List[Dict[str, Dict[str, KubernetesScalingResourceTypeDef]]]]
    eksClusters: NotRequired[List[EksClusterTypeDef]]
    ungraceful: NotRequired[EksResourceScalingUngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[Literal["sampledMaxInLast24Hours"]]

class EksResourceScalingConfigurationTypeDef(TypedDict):
    kubernetesResourceType: KubernetesResourceTypeTypeDef
    timeoutMinutes: NotRequired[int]
    scalingResources: NotRequired[
        Sequence[Mapping[str, Mapping[str, KubernetesScalingResourceTypeDef]]]
    ]
    eksClusters: NotRequired[Sequence[EksClusterTypeDef]]
    ungraceful: NotRequired[EksResourceScalingUngracefulTypeDef]
    targetPercent: NotRequired[int]
    capacityMonitoringApproach: NotRequired[Literal["sampledMaxInLast24Hours"]]

class ListPlanExecutionEventsResponseTypeDef(TypedDict):
    items: List[ExecutionEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetPlanEvaluationStatusRequestPaginateTypeDef(TypedDict):
    planArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetPlanExecutionRequestPaginateTypeDef(TypedDict):
    planArn: str
    executionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlanExecutionEventsRequestPaginateTypeDef(TypedDict):
    planArn: str
    executionId: str
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlanExecutionsRequestPaginateTypeDef(TypedDict):
    planArn: str
    state: NotRequired[ExecutionStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlansInRegionRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlansRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoute53HealthChecksInRegionRequestPaginateTypeDef(TypedDict):
    arn: str
    hostedZoneId: NotRequired[str]
    recordName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoute53HealthChecksRequestPaginateTypeDef(TypedDict):
    arn: str
    hostedZoneId: NotRequired[str]
    recordName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetPlanEvaluationStatusRequestWaitTypeDef(TypedDict):
    planArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPlanExecutionRequestWaitTypeDef(TypedDict):
    planArn: str
    executionId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GlobalAuroraConfigurationOutputTypeDef(TypedDict):
    behavior: GlobalAuroraDefaultBehaviorType
    globalClusterIdentifier: str
    databaseClusterArns: List[str]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    ungraceful: NotRequired[GlobalAuroraUngracefulTypeDef]

class GlobalAuroraConfigurationTypeDef(TypedDict):
    behavior: GlobalAuroraDefaultBehaviorType
    globalClusterIdentifier: str
    databaseClusterArns: Sequence[str]
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    ungraceful: NotRequired[GlobalAuroraUngracefulTypeDef]

class ListRoute53HealthChecksInRegionResponseTypeDef(TypedDict):
    healthChecks: List[Route53HealthCheckTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRoute53HealthChecksResponseTypeDef(TypedDict):
    healthChecks: List[Route53HealthCheckTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ResourceWarningTypeDef(TypedDict):
    version: str
    warningStatus: ResourceWarningStatusType
    warningUpdatedTime: datetime
    warningMessage: str
    workflow: NotRequired[MinimalWorkflowTypeDef]
    stepName: NotRequired[str]
    resourceArn: NotRequired[str]

ParallelExecutionBlockConfigurationUnionTypeDef = Union[
    ParallelExecutionBlockConfigurationTypeDef, ParallelExecutionBlockConfigurationOutputTypeDef
]

class ReportOutputConfigurationTypeDef(TypedDict):
    s3Configuration: NotRequired[S3ReportOutputConfigurationTypeDef]

class ReportOutputTypeDef(TypedDict):
    s3ReportOutput: NotRequired[S3ReportOutputTypeDef]
    failedReportOutput: NotRequired[FailedReportOutputTypeDef]

class Route53HealthCheckConfigurationOutputTypeDef(TypedDict):
    hostedZoneId: str
    recordName: str
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    recordSets: NotRequired[List[Route53ResourceRecordSetTypeDef]]

class Route53HealthCheckConfigurationTypeDef(TypedDict):
    hostedZoneId: str
    recordName: str
    timeoutMinutes: NotRequired[int]
    crossAccountRole: NotRequired[str]
    externalId: NotRequired[str]
    recordSets: NotRequired[Sequence[Route53ResourceRecordSetTypeDef]]

class TriggerOutputTypeDef(TypedDict):
    targetRegion: str
    action: WorkflowTargetActionType
    conditions: List[TriggerConditionTypeDef]
    minDelayMinutesBetweenExecutions: int
    description: NotRequired[str]

class TriggerTypeDef(TypedDict):
    targetRegion: str
    action: WorkflowTargetActionType
    conditions: Sequence[TriggerConditionTypeDef]
    minDelayMinutesBetweenExecutions: int
    description: NotRequired[str]

ArcRoutingControlConfigurationUnionTypeDef = Union[
    ArcRoutingControlConfigurationTypeDef, ArcRoutingControlConfigurationOutputTypeDef
]
CustomActionLambdaConfigurationUnionTypeDef = Union[
    CustomActionLambdaConfigurationTypeDef, CustomActionLambdaConfigurationOutputTypeDef
]
DocumentDbConfigurationUnionTypeDef = Union[
    DocumentDbConfigurationTypeDef, DocumentDbConfigurationOutputTypeDef
]
Ec2AsgCapacityIncreaseConfigurationUnionTypeDef = Union[
    Ec2AsgCapacityIncreaseConfigurationTypeDef, Ec2AsgCapacityIncreaseConfigurationOutputTypeDef
]
EcsCapacityIncreaseConfigurationUnionTypeDef = Union[
    EcsCapacityIncreaseConfigurationTypeDef, EcsCapacityIncreaseConfigurationOutputTypeDef
]
EksResourceScalingConfigurationUnionTypeDef = Union[
    EksResourceScalingConfigurationTypeDef, EksResourceScalingConfigurationOutputTypeDef
]
GlobalAuroraConfigurationUnionTypeDef = Union[
    GlobalAuroraConfigurationTypeDef, GlobalAuroraConfigurationOutputTypeDef
]

class GetPlanEvaluationStatusResponseTypeDef(TypedDict):
    planArn: str
    lastEvaluationTime: datetime
    lastEvaluatedVersion: str
    region: str
    evaluationState: EvaluationStatusType
    warnings: List[ResourceWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReportConfigurationOutputTypeDef(TypedDict):
    reportOutput: NotRequired[List[ReportOutputConfigurationTypeDef]]

class ReportConfigurationTypeDef(TypedDict):
    reportOutput: NotRequired[Sequence[ReportOutputConfigurationTypeDef]]

class GeneratedReportTypeDef(TypedDict):
    reportGenerationTime: NotRequired[datetime]
    reportOutput: NotRequired[ReportOutputTypeDef]

class ExecutionBlockConfigurationOutputTypeDef(TypedDict):
    customActionLambdaConfig: NotRequired[CustomActionLambdaConfigurationOutputTypeDef]
    ec2AsgCapacityIncreaseConfig: NotRequired[Ec2AsgCapacityIncreaseConfigurationOutputTypeDef]
    executionApprovalConfig: NotRequired[ExecutionApprovalConfigurationTypeDef]
    arcRoutingControlConfig: NotRequired[ArcRoutingControlConfigurationOutputTypeDef]
    globalAuroraConfig: NotRequired[GlobalAuroraConfigurationOutputTypeDef]
    parallelConfig: NotRequired[ParallelExecutionBlockConfigurationOutputTypeDef]
    regionSwitchPlanConfig: NotRequired[RegionSwitchPlanConfigurationTypeDef]
    ecsCapacityIncreaseConfig: NotRequired[EcsCapacityIncreaseConfigurationOutputTypeDef]
    eksResourceScalingConfig: NotRequired[EksResourceScalingConfigurationOutputTypeDef]
    route53HealthCheckConfig: NotRequired[Route53HealthCheckConfigurationOutputTypeDef]
    documentDbConfig: NotRequired[DocumentDbConfigurationOutputTypeDef]

class ExecutionBlockConfigurationPaginatorTypeDef(TypedDict):
    customActionLambdaConfig: NotRequired[CustomActionLambdaConfigurationOutputTypeDef]
    ec2AsgCapacityIncreaseConfig: NotRequired[Ec2AsgCapacityIncreaseConfigurationOutputTypeDef]
    executionApprovalConfig: NotRequired[ExecutionApprovalConfigurationTypeDef]
    arcRoutingControlConfig: NotRequired[ArcRoutingControlConfigurationOutputTypeDef]
    globalAuroraConfig: NotRequired[GlobalAuroraConfigurationOutputTypeDef]
    parallelConfig: NotRequired[ParallelExecutionBlockConfigurationPaginatorTypeDef]
    regionSwitchPlanConfig: NotRequired[RegionSwitchPlanConfigurationTypeDef]
    ecsCapacityIncreaseConfig: NotRequired[EcsCapacityIncreaseConfigurationOutputTypeDef]
    eksResourceScalingConfig: NotRequired[EksResourceScalingConfigurationOutputTypeDef]
    route53HealthCheckConfig: NotRequired[Route53HealthCheckConfigurationOutputTypeDef]
    documentDbConfig: NotRequired[DocumentDbConfigurationOutputTypeDef]

Route53HealthCheckConfigurationUnionTypeDef = Union[
    Route53HealthCheckConfigurationTypeDef, Route53HealthCheckConfigurationOutputTypeDef
]
TriggerUnionTypeDef = Union[TriggerTypeDef, TriggerOutputTypeDef]
ReportConfigurationUnionTypeDef = Union[
    ReportConfigurationTypeDef, ReportConfigurationOutputTypeDef
]

class StepOutputTypeDef(TypedDict):
    name: str
    executionBlockConfiguration: ExecutionBlockConfigurationOutputTypeDef
    executionBlockType: ExecutionBlockTypeType
    description: NotRequired[str]

class StepPaginatorTypeDef(TypedDict):
    name: str
    executionBlockConfiguration: ExecutionBlockConfigurationPaginatorTypeDef
    executionBlockType: ExecutionBlockTypeType
    description: NotRequired[str]

class ExecutionBlockConfigurationTypeDef(TypedDict):
    customActionLambdaConfig: NotRequired[CustomActionLambdaConfigurationUnionTypeDef]
    ec2AsgCapacityIncreaseConfig: NotRequired[Ec2AsgCapacityIncreaseConfigurationUnionTypeDef]
    executionApprovalConfig: NotRequired[ExecutionApprovalConfigurationTypeDef]
    arcRoutingControlConfig: NotRequired[ArcRoutingControlConfigurationUnionTypeDef]
    globalAuroraConfig: NotRequired[GlobalAuroraConfigurationUnionTypeDef]
    parallelConfig: NotRequired[ParallelExecutionBlockConfigurationUnionTypeDef]
    regionSwitchPlanConfig: NotRequired[RegionSwitchPlanConfigurationTypeDef]
    ecsCapacityIncreaseConfig: NotRequired[EcsCapacityIncreaseConfigurationUnionTypeDef]
    eksResourceScalingConfig: NotRequired[EksResourceScalingConfigurationUnionTypeDef]
    route53HealthCheckConfig: NotRequired[Route53HealthCheckConfigurationUnionTypeDef]
    documentDbConfig: NotRequired[DocumentDbConfigurationUnionTypeDef]

class WorkflowOutputTypeDef(TypedDict):
    workflowTargetAction: WorkflowTargetActionType
    steps: NotRequired[List[StepOutputTypeDef]]
    workflowTargetRegion: NotRequired[str]
    workflowDescription: NotRequired[str]

class WorkflowPaginatorTypeDef(TypedDict):
    workflowTargetAction: WorkflowTargetActionType
    steps: NotRequired[List[StepPaginatorTypeDef]]
    workflowTargetRegion: NotRequired[str]
    workflowDescription: NotRequired[str]

ExecutionBlockConfigurationUnionTypeDef = Union[
    ExecutionBlockConfigurationTypeDef, ExecutionBlockConfigurationOutputTypeDef
]

class PlanTypeDef(TypedDict):
    arn: str
    workflows: List[WorkflowOutputTypeDef]
    executionRole: str
    name: str
    regions: List[str]
    recoveryApproach: RecoveryApproachType
    owner: str
    description: NotRequired[str]
    recoveryTimeObjectiveMinutes: NotRequired[int]
    associatedAlarms: NotRequired[Dict[str, AssociatedAlarmTypeDef]]
    triggers: NotRequired[List[TriggerOutputTypeDef]]
    reportConfiguration: NotRequired[ReportConfigurationOutputTypeDef]
    primaryRegion: NotRequired[str]
    version: NotRequired[str]
    updatedAt: NotRequired[datetime]

class PlanPaginatorTypeDef(TypedDict):
    arn: str
    workflows: List[WorkflowPaginatorTypeDef]
    executionRole: str
    name: str
    regions: List[str]
    recoveryApproach: RecoveryApproachType
    owner: str
    description: NotRequired[str]
    recoveryTimeObjectiveMinutes: NotRequired[int]
    associatedAlarms: NotRequired[Dict[str, AssociatedAlarmTypeDef]]
    triggers: NotRequired[List[TriggerOutputTypeDef]]
    reportConfiguration: NotRequired[ReportConfigurationOutputTypeDef]
    primaryRegion: NotRequired[str]
    version: NotRequired[str]
    updatedAt: NotRequired[datetime]

class StepTypeDef(TypedDict):
    name: str
    executionBlockConfiguration: ExecutionBlockConfigurationUnionTypeDef
    executionBlockType: ExecutionBlockTypeType
    description: NotRequired[str]

class CreatePlanResponseTypeDef(TypedDict):
    plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlanExecutionResponseTypeDef(TypedDict):
    planArn: str
    executionId: str
    version: str
    updatedAt: datetime
    comment: str
    startTime: datetime
    endTime: datetime
    mode: ExecutionModeType
    executionState: ExecutionStateType
    executionAction: ExecutionActionType
    executionRegion: str
    stepStates: List[StepStateTypeDef]
    plan: PlanTypeDef
    actualRecoveryTime: str
    generatedReportDetails: List[GeneratedReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetPlanInRegionResponseTypeDef(TypedDict):
    plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlanResponseTypeDef(TypedDict):
    plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePlanResponseTypeDef(TypedDict):
    plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlanExecutionResponsePaginatorTypeDef(TypedDict):
    planArn: str
    executionId: str
    version: str
    updatedAt: datetime
    comment: str
    startTime: datetime
    endTime: datetime
    mode: ExecutionModeType
    executionState: ExecutionStateType
    executionAction: ExecutionActionType
    executionRegion: str
    stepStates: List[StepStateTypeDef]
    plan: PlanPaginatorTypeDef
    actualRecoveryTime: str
    generatedReportDetails: List[GeneratedReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

StepUnionTypeDef = Union[StepTypeDef, StepOutputTypeDef]

class WorkflowTypeDef(TypedDict):
    workflowTargetAction: WorkflowTargetActionType
    steps: NotRequired[Sequence[StepUnionTypeDef]]
    workflowTargetRegion: NotRequired[str]
    workflowDescription: NotRequired[str]

WorkflowUnionTypeDef = Union[WorkflowTypeDef, WorkflowOutputTypeDef]

class CreatePlanRequestTypeDef(TypedDict):
    workflows: Sequence[WorkflowUnionTypeDef]
    executionRole: str
    name: str
    regions: Sequence[str]
    recoveryApproach: RecoveryApproachType
    description: NotRequired[str]
    recoveryTimeObjectiveMinutes: NotRequired[int]
    associatedAlarms: NotRequired[Mapping[str, AssociatedAlarmTypeDef]]
    triggers: NotRequired[Sequence[TriggerUnionTypeDef]]
    reportConfiguration: NotRequired[ReportConfigurationUnionTypeDef]
    primaryRegion: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdatePlanRequestTypeDef(TypedDict):
    arn: str
    workflows: Sequence[WorkflowUnionTypeDef]
    executionRole: str
    description: NotRequired[str]
    recoveryTimeObjectiveMinutes: NotRequired[int]
    associatedAlarms: NotRequired[Mapping[str, AssociatedAlarmTypeDef]]
    triggers: NotRequired[Sequence[TriggerUnionTypeDef]]
    reportConfiguration: NotRequired[ReportConfigurationUnionTypeDef]
