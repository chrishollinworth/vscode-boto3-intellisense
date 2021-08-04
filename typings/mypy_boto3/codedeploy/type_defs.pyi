"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AddTagsToOnPremisesInstancesInputRequestTypeDef

    data: AddTagsToOnPremisesInstancesInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ApplicationRevisionSortByType,
    AutoRollbackEventType,
    BundleTypeType,
    ComputePlatformType,
    DeploymentCreatorType,
    DeploymentOptionType,
    DeploymentReadyActionType,
    DeploymentStatusType,
    DeploymentTargetTypeType,
    DeploymentTypeType,
    DeploymentWaitTypeType,
    EC2TagFilterTypeType,
    ErrorCodeType,
    FileExistsBehaviorType,
    GreenFleetProvisioningActionType,
    InstanceActionType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleErrorCodeType,
    LifecycleEventStatusType,
    ListStateFilterActionType,
    MinimumHealthyHostsTypeType,
    OutdatedInstancesStrategyType,
    RegistrationStatusType,
    RevisionLocationTypeType,
    SortOrderType,
    StopStatusType,
    TagFilterTypeType,
    TargetFilterNameType,
    TargetLabelType,
    TargetStatusType,
    TrafficRoutingTypeType,
    TriggerEventTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsInputRequestTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsInputRequestTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "ContinueDeploymentInputRequestTypeDef",
    "CreateApplicationInputRequestTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigInputRequestTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupInputRequestTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentInputRequestTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteApplicationInputRequestTypeDef",
    "DeleteDeploymentConfigInputRequestTypeDef",
    "DeleteDeploymentGroupInputRequestTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionInputRequestTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigInputRequestTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupInputRequestTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetDeploymentInstanceInputRequestTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetInputRequestTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceInputRequestTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "ListApplicationRevisionsInputRequestTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsInputRequestTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsInputRequestTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesInputRequestTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsInputRequestTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesInputRequestTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "RawStringTypeDef",
    "RegisterApplicationRevisionInputRequestTypeDef",
    "RegisterOnPremisesInstanceInputRequestTypeDef",
    "RelatedDeploymentsTypeDef",
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    "StopDeploymentInputRequestTypeDef",
    "StopDeploymentOutputTypeDef",
    "TagFilterTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TimeRangeTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApplicationInputRequestTypeDef",
    "UpdateDeploymentGroupInputRequestTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "instanceNames": List[str],
    },
)

AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List["AlarmTypeDef"],
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": str,
    },
    total=False,
)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef",
    {
        "content": str,
        "sha256": str,
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": ComputePlatformType,
    },
    total=False,
)

AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[AutoRollbackEventType],
    },
    total=False,
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": str,
        "hook": str,
    },
    total=False,
)

BatchGetApplicationRevisionsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
        "revisions": List["RevisionLocationTypeDef"],
    },
)

BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List["RevisionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetApplicationsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationsInputRequestTypeDef",
    {
        "applicationNames": List[str],
    },
)

BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {
        "applicationsInfo": List["ApplicationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentGroupsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupNames": List[str],
    },
)

BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {
        "deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentInstancesInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceIds": List[str],
    },
)

BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {
        "instancesSummary": List["InstanceSummaryTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentTargetsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": str,
        "targetIds": List[str],
    },
    total=False,
)

BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {
        "deploymentTargets": List["DeploymentTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentsInputRequestTypeDef",
    {
        "deploymentIds": List[str],
    },
)

BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {
        "deploymentsInfo": List["DeploymentInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    {
        "instanceNames": List[str],
    },
)

BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
    {
        "instanceInfos": List["InstanceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "BlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": "BlueInstanceTerminationOptionTypeDef",
        "deploymentReadyOption": "DeploymentReadyOptionTypeDef",
        "greenFleetProvisioningOption": "GreenFleetProvisioningOptionTypeDef",
    },
    total=False,
)

BlueInstanceTerminationOptionTypeDef = TypedDict(
    "BlueInstanceTerminationOptionTypeDef",
    {
        "action": InstanceActionType,
        "terminationWaitTimeInMinutes": int,
    },
    total=False,
)

CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatusType,
        "resourceType": str,
        "targetVersionWeight": float,
    },
    total=False,
)

ContinueDeploymentInputRequestTypeDef = TypedDict(
    "ContinueDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
        "deploymentWaitType": DeploymentWaitTypeType,
    },
    total=False,
)

_RequiredCreateApplicationInputRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalCreateApplicationInputRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationInputRequestTypeDef",
    {
        "computePlatform": ComputePlatformType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateApplicationInputRequestTypeDef(
    _RequiredCreateApplicationInputRequestTypeDef, _OptionalCreateApplicationInputRequestTypeDef
):
    pass

CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef",
    {
        "applicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)
_OptionalCreateDeploymentConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentConfigInputRequestTypeDef",
    {
        "minimumHealthyHosts": "MinimumHealthyHostsTypeDef",
        "trafficRoutingConfig": "TrafficRoutingConfigTypeDef",
        "computePlatform": ComputePlatformType,
    },
    total=False,
)

class CreateDeploymentConfigInputRequestTypeDef(
    _RequiredCreateDeploymentConfigInputRequestTypeDef,
    _OptionalCreateDeploymentConfigInputRequestTypeDef,
):
    pass

CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "serviceRoleArn": str,
    },
)
_OptionalCreateDeploymentGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentGroupInputRequestTypeDef",
    {
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "deploymentStyle": "DeploymentStyleTypeDef",
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "ecsServices": List["ECSServiceTypeDef"],
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDeploymentGroupInputRequestTypeDef(
    _RequiredCreateDeploymentGroupInputRequestTypeDef,
    _OptionalCreateDeploymentGroupInputRequestTypeDef,
):
    pass

CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalCreateDeploymentInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentInputRequestTypeDef",
    {
        "deploymentGroupName": str,
        "revision": "RevisionLocationTypeDef",
        "deploymentConfigName": str,
        "description": str,
        "ignoreApplicationStopFailures": bool,
        "targetInstances": "TargetInstancesTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "updateOutdatedInstancesOnly": bool,
        "fileExistsBehavior": FileExistsBehaviorType,
    },
    total=False,
)

class CreateDeploymentInputRequestTypeDef(
    _RequiredCreateDeploymentInputRequestTypeDef, _OptionalCreateDeploymentInputRequestTypeDef
):
    pass

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationInputRequestTypeDef = TypedDict(
    "DeleteApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)

DeleteDeploymentConfigInputRequestTypeDef = TypedDict(
    "DeleteDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)

DeleteDeploymentGroupInputRequestTypeDef = TypedDict(
    "DeleteDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGitHubAccountTokenInputRequestTypeDef = TypedDict(
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    {
        "tokenName": str,
    },
    total=False,
)

DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef",
    {
        "tokenName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcesByExternalIdInputRequestTypeDef = TypedDict(
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

DeploymentConfigInfoTypeDef = TypedDict(
    "DeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": "MinimumHealthyHostsTypeDef",
        "createTime": datetime,
        "computePlatform": ComputePlatformType,
        "trafficRoutingConfig": "TrafficRoutingConfigTypeDef",
    },
    total=False,
)

DeploymentGroupInfoTypeDef = TypedDict(
    "DeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List["AutoScalingGroupTypeDef"],
        "serviceRoleArn": str,
        "targetRevision": "RevisionLocationTypeDef",
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "lastSuccessfulDeployment": "LastDeploymentInfoTypeDef",
        "lastAttemptedDeployment": "LastDeploymentInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "computePlatform": ComputePlatformType,
        "ecsServices": List["ECSServiceTypeDef"],
    },
    total=False,
)

DeploymentInfoTypeDef = TypedDict(
    "DeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": "RevisionLocationTypeDef",
        "revision": "RevisionLocationTypeDef",
        "status": DeploymentStatusType,
        "errorInformation": "ErrorInformationTypeDef",
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": "DeploymentOverviewTypeDef",
        "description": str,
        "creator": DeploymentCreatorType,
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": "RollbackInfoTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "targetInstances": "TargetInstancesTypeDef",
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": FileExistsBehaviorType,
        "deploymentStatusMessages": List[str],
        "computePlatform": ComputePlatformType,
        "externalId": str,
        "relatedDeployments": "RelatedDeploymentsTypeDef",
    },
    total=False,
)

DeploymentOverviewTypeDef = TypedDict(
    "DeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)

DeploymentReadyOptionTypeDef = TypedDict(
    "DeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": DeploymentReadyActionType,
        "waitTimeInMinutes": int,
    },
    total=False,
)

DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {
        "deploymentType": DeploymentTypeType,
        "deploymentOption": DeploymentOptionType,
    },
    total=False,
)

DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": DeploymentTargetTypeType,
        "instanceTarget": "InstanceTargetTypeDef",
        "lambdaTarget": "LambdaTargetTypeDef",
        "ecsTarget": "ECSTargetTypeDef",
        "cloudFormationTarget": "CloudFormationTargetTypeDef",
    },
    total=False,
)

DeregisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)

DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {
        "errorCode": LifecycleErrorCodeType,
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Type": EC2TagFilterTypeType,
    },
    total=False,
)

EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef",
    {
        "ec2TagSetList": List[List["EC2TagFilterTypeDef"]],
    },
    total=False,
)

ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef",
    {
        "serviceName": str,
        "clusterName": str,
    },
    total=False,
)

ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatusType,
        "taskSetsInfo": List["ECSTaskSetTypeDef"],
    },
    total=False,
)

ECSTaskSetTypeDef = TypedDict(
    "ECSTaskSetTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": "TargetGroupInfoTypeDef",
        "taskSetLabel": TargetLabelType,
    },
    total=False,
)

ELBInfoTypeDef = TypedDict(
    "ELBInfoTypeDef",
    {
        "name": str,
    },
    total=False,
)

ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
    total=False,
)

GenericRevisionInfoTypeDef = TypedDict(
    "GenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)

GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "application": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRevisionInputRequestTypeDef = TypedDict(
    "GetApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
    },
)

GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentConfigInputRequestTypeDef = TypedDict(
    "GetDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)

GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigInfo": "DeploymentConfigInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentGroupInputRequestTypeDef = TypedDict(
    "GetDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupInfo": "DeploymentGroupInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentInstanceInputRequestTypeDef = TypedDict(
    "GetDeploymentInstanceInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
    },
)

GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef",
    {
        "instanceSummary": "InstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deploymentInfo": "DeploymentInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentTargetInputRequestTypeDef = TypedDict(
    "GetDeploymentTargetInputRequestTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
    },
    total=False,
)

GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef",
    {
        "deploymentTarget": "DeploymentTargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "GetOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef",
    {
        "instanceInfo": "InstanceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef",
    {
        "repository": str,
        "commitId": str,
    },
    total=False,
)

GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef",
    {
        "action": GreenFleetProvisioningActionType,
    },
    total=False,
)

InstanceInfoTypeDef = TypedDict(
    "InstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": InstanceStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceType": InstanceTypeType,
    },
    total=False,
)

InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceLabel": TargetLabelType,
    },
    total=False,
)

LambdaFunctionInfoTypeDef = TypedDict(
    "LambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)

LambdaTargetTypeDef = TypedDict(
    "LambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "lambdaFunctionInfo": "LambdaFunctionInfoTypeDef",
    },
    total=False,
)

LastDeploymentInfoTypeDef = TypedDict(
    "LastDeploymentInfoTypeDef",
    {
        "deploymentId": str,
        "status": DeploymentStatusType,
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

LifecycleEventTypeDef = TypedDict(
    "LifecycleEventTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": "DiagnosticsTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": LifecycleEventStatusType,
    },
    total=False,
)

_RequiredListApplicationRevisionsInputRequestTypeDef = TypedDict(
    "_RequiredListApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalListApplicationRevisionsInputRequestTypeDef = TypedDict(
    "_OptionalListApplicationRevisionsInputRequestTypeDef",
    {
        "sortBy": ApplicationRevisionSortByType,
        "sortOrder": SortOrderType,
        "s3Bucket": str,
        "s3KeyPrefix": str,
        "deployed": ListStateFilterActionType,
        "nextToken": str,
    },
    total=False,
)

class ListApplicationRevisionsInputRequestTypeDef(
    _RequiredListApplicationRevisionsInputRequestTypeDef,
    _OptionalListApplicationRevisionsInputRequestTypeDef,
):
    pass

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {
        "revisions": List["RevisionLocationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "applications": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentConfigsInputRequestTypeDef = TypedDict(
    "ListDeploymentConfigsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {
        "deploymentConfigsList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentGroupsInputRequestTypeDef = TypedDict(
    "_RequiredListDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalListDeploymentGroupsInputRequestTypeDef = TypedDict(
    "_OptionalListDeploymentGroupsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListDeploymentGroupsInputRequestTypeDef(
    _RequiredListDeploymentGroupsInputRequestTypeDef,
    _OptionalListDeploymentGroupsInputRequestTypeDef,
):
    pass

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentInstancesInputRequestTypeDef = TypedDict(
    "_RequiredListDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
_OptionalListDeploymentInstancesInputRequestTypeDef = TypedDict(
    "_OptionalListDeploymentInstancesInputRequestTypeDef",
    {
        "nextToken": str,
        "instanceStatusFilter": List[InstanceStatusType],
        "instanceTypeFilter": List[InstanceTypeType],
    },
    total=False,
)

class ListDeploymentInstancesInputRequestTypeDef(
    _RequiredListDeploymentInstancesInputRequestTypeDef,
    _OptionalListDeploymentInstancesInputRequestTypeDef,
):
    pass

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {
        "instancesList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentTargetsInputRequestTypeDef = TypedDict(
    "ListDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": str,
        "nextToken": str,
        "targetFilters": Dict[TargetFilterNameType, List[str]],
    },
    total=False,
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef",
    {
        "targetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "externalId": str,
        "includeOnlyStatuses": List[DeploymentStatusType],
        "createTimeRange": "TimeRangeTypeDef",
        "nextToken": str,
    },
    total=False,
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGitHubAccountTokenNamesInputRequestTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {
        "tokenNameList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "ListOnPremisesInstancesInputRequestTypeDef",
    {
        "registrationStatus": RegistrationStatusType,
        "tagFilters": List["TagFilterTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {
        "instanceNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerInfoTypeDef = TypedDict(
    "LoadBalancerInfoTypeDef",
    {
        "elbInfoList": List["ELBInfoTypeDef"],
        "targetGroupInfoList": List["TargetGroupInfoTypeDef"],
        "targetGroupPairInfoList": List["TargetGroupPairInfoTypeDef"],
    },
    total=False,
)

MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef",
    {
        "type": MinimumHealthyHostsTypeType,
        "value": int,
    },
    total=False,
)

OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[List["TagFilterTypeDef"]],
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

PutLifecycleEventHookExecutionStatusInputRequestTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    {
        "deploymentId": str,
        "lifecycleEventHookExecutionId": str,
        "status": LifecycleEventStatusType,
    },
    total=False,
)

PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    {
        "lifecycleEventHookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RawStringTypeDef = TypedDict(
    "RawStringTypeDef",
    {
        "content": str,
        "sha256": str,
    },
    total=False,
)

_RequiredRegisterApplicationRevisionInputRequestTypeDef = TypedDict(
    "_RequiredRegisterApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
    },
)
_OptionalRegisterApplicationRevisionInputRequestTypeDef = TypedDict(
    "_OptionalRegisterApplicationRevisionInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class RegisterApplicationRevisionInputRequestTypeDef(
    _RequiredRegisterApplicationRevisionInputRequestTypeDef,
    _OptionalRegisterApplicationRevisionInputRequestTypeDef,
):
    pass

_RequiredRegisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "_RequiredRegisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalRegisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "_OptionalRegisterOnPremisesInstanceInputRequestTypeDef",
    {
        "iamSessionArn": str,
        "iamUserArn": str,
    },
    total=False,
)

class RegisterOnPremisesInstanceInputRequestTypeDef(
    _RequiredRegisterOnPremisesInstanceInputRequestTypeDef,
    _OptionalRegisterOnPremisesInstanceInputRequestTypeDef,
):
    pass

RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": str,
        "autoUpdateOutdatedInstancesDeploymentIds": List[str],
    },
    total=False,
)

RemoveTagsFromOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "instanceNames": List[str],
    },
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

RevisionInfoTypeDef = TypedDict(
    "RevisionInfoTypeDef",
    {
        "revisionLocation": "RevisionLocationTypeDef",
        "genericRevisionInfo": "GenericRevisionInfoTypeDef",
    },
    total=False,
)

RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": RevisionLocationTypeType,
        "s3Location": "S3LocationTypeDef",
        "gitHubLocation": "GitHubLocationTypeDef",
        "string": "RawStringTypeDef",
        "appSpecContent": "AppSpecContentTypeDef",
    },
    total=False,
)

RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {
        "rollbackDeploymentId": str,
        "rollbackTriggeringDeploymentId": str,
        "rollbackMessage": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": BundleTypeType,
        "version": str,
        "eTag": str,
    },
    total=False,
)

SkipWaitTimeForInstanceTerminationInputRequestTypeDef = TypedDict(
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    {
        "deploymentId": str,
    },
    total=False,
)

_RequiredStopDeploymentInputRequestTypeDef = TypedDict(
    "_RequiredStopDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
_OptionalStopDeploymentInputRequestTypeDef = TypedDict(
    "_OptionalStopDeploymentInputRequestTypeDef",
    {
        "autoRollbackEnabled": bool,
    },
    total=False,
)

class StopDeploymentInputRequestTypeDef(
    _RequiredStopDeploymentInputRequestTypeDef, _OptionalStopDeploymentInputRequestTypeDef
):
    pass

StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
    {
        "status": StopStatusType,
        "statusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Type": TagFilterTypeType,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetGroupInfoTypeDef = TypedDict(
    "TargetGroupInfoTypeDef",
    {
        "name": str,
    },
    total=False,
)

TargetGroupPairInfoTypeDef = TypedDict(
    "TargetGroupPairInfoTypeDef",
    {
        "targetGroups": List["TargetGroupInfoTypeDef"],
        "prodTrafficRoute": "TrafficRouteTypeDef",
        "testTrafficRoute": "TrafficRouteTypeDef",
    },
    total=False,
)

TargetInstancesTypeDef = TypedDict(
    "TargetInstancesTypeDef",
    {
        "tagFilters": List["EC2TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "ec2TagSet": "EC2TagSetTypeDef",
    },
    total=False,
)

TimeBasedCanaryTypeDef = TypedDict(
    "TimeBasedCanaryTypeDef",
    {
        "canaryPercentage": int,
        "canaryInterval": int,
    },
    total=False,
)

TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef",
    {
        "linearPercentage": int,
        "linearInterval": int,
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "start": Union[datetime, str],
        "end": Union[datetime, str],
    },
    total=False,
)

TrafficRouteTypeDef = TypedDict(
    "TrafficRouteTypeDef",
    {
        "listenerArns": List[str],
    },
    total=False,
)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": TrafficRoutingTypeType,
        "timeBasedCanary": "TimeBasedCanaryTypeDef",
        "timeBasedLinear": "TimeBasedLinearTypeDef",
    },
    total=False,
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[TriggerEventTypeType],
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateApplicationInputRequestTypeDef = TypedDict(
    "UpdateApplicationInputRequestTypeDef",
    {
        "applicationName": str,
        "newApplicationName": str,
    },
    total=False,
)

_RequiredUpdateDeploymentGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "currentDeploymentGroupName": str,
    },
)
_OptionalUpdateDeploymentGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentGroupInputRequestTypeDef",
    {
        "newDeploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "serviceRoleArn": str,
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "deploymentStyle": "DeploymentStyleTypeDef",
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "ecsServices": List["ECSServiceTypeDef"],
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
    },
    total=False,
)

class UpdateDeploymentGroupInputRequestTypeDef(
    _RequiredUpdateDeploymentGroupInputRequestTypeDef,
    _OptionalUpdateDeploymentGroupInputRequestTypeDef,
):
    pass

UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
