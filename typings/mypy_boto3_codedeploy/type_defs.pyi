"""
Main interface for codedeploy service type definitions.

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AlarmConfigurationTypeDef

    data: AlarmConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "RawStringTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "StopDeploymentOutputTypeDef",
    "TimeRangeTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)

AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {"enabled": bool, "ignorePollAlarmFailure": bool, "alarms": List["AlarmTypeDef"]},
    total=False,
)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"name": str}, total=False)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef", {"content": str, "sha256": str}, total=False
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)

AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef", {"name": str, "hook": str}, total=False
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
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "resourceType": str,
        "targetVersionWeight": float,
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
        "computePlatform": Literal["Server", "Lambda", "ECS"],
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
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "lastSuccessfulDeployment": "LastDeploymentInfoTypeDef",
        "lastAttemptedDeployment": "LastDeploymentInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "computePlatform": Literal["Server", "Lambda", "ECS"],
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
        "status": Literal[
            "Created", "Queued", "InProgress", "Baking", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "errorInformation": "ErrorInformationTypeDef",
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": "DeploymentOverviewTypeDef",
        "description": str,
        "creator": Literal[
            "user",
            "autoscaling",
            "codeDeployRollback",
            "CodeDeploy",
            "CloudFormation",
            "CloudFormationRollback",
        ],
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
        "fileExistsBehavior": Literal["DISALLOW", "OVERWRITE", "RETAIN"],
        "deploymentStatusMessages": List[str],
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "externalId": str,
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
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": Literal[
            "InstanceTarget", "LambdaTarget", "ECSTarget", "CloudFormationTarget"
        ],
        "instanceTarget": "InstanceTargetTypeDef",
        "lambdaTarget": "LambdaTargetTypeDef",
        "ecsTarget": "ECSTargetTypeDef",
        "cloudFormationTarget": "CloudFormationTargetTypeDef",
    },
    total=False,
)

DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef", {"ec2TagSetList": List[List["EC2TagFilterTypeDef"]]}, total=False
)

ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef", {"serviceName": str, "clusterName": str}, total=False
)

ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
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
        "taskSetLabel": Literal["Blue", "Green"],
    },
    total=False,
)

ELBInfoTypeDef = TypedDict("ELBInfoTypeDef", {"name": str}, total=False)

ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef",
    {
        "code": Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
            "CLOUDFORMATION_STACK_FAILURE",
        ],
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

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef", {"repository": str, "commitId": str}, total=False
)

GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
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
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceType": Literal["Blue", "Green"],
    },
    total=False,
)

InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceLabel": Literal["Blue", "Green"],
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
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
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
        "status": Literal[
            "Created", "Queued", "InProgress", "Baking", "Succeeded", "Failed", "Stopped", "Ready"
        ],
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
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
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
    {"value": int, "type": Literal["HOST_COUNT", "FLEET_PERCENT"]},
    total=False,
)

OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef", {"onPremisesTagSetList": List[List["TagFilterTypeDef"]]}, total=False
)

RawStringTypeDef = TypedDict("RawStringTypeDef", {"content": str, "sha256": str}, total=False)

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
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": "S3LocationTypeDef",
        "gitHubLocation": "GitHubLocationTypeDef",
        "string": "RawStringTypeDef",
        "appSpecContent": "AppSpecContentTypeDef",
    },
    total=False,
)

RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TargetGroupInfoTypeDef = TypedDict("TargetGroupInfoTypeDef", {"name": str}, total=False)

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
    "TimeBasedCanaryTypeDef", {"canaryPercentage": int, "canaryInterval": int}, total=False
)

TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef", {"linearPercentage": int, "linearInterval": int}, total=False
)

TrafficRouteTypeDef = TypedDict("TrafficRouteTypeDef", {"listenerArns": List[str]}, total=False)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": Literal["TimeBasedCanary", "TimeBasedLinear", "AllAtOnce"],
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
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)

BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {"applicationName": str, "errorMessage": str, "revisions": List["RevisionInfoTypeDef"]},
    total=False,
)

BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {"applicationsInfo": List["ApplicationInfoTypeDef"]},
    total=False,
)

BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {"deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"], "errorMessage": str},
    total=False,
)

BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {"instancesSummary": List["InstanceSummaryTypeDef"], "errorMessage": str},
    total=False,
)

BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {"deploymentTargets": List["DeploymentTargetTypeDef"]},
    total=False,
)

BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {"deploymentsInfo": List["DeploymentInfoTypeDef"]},
    total=False,
)

BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
    {"instanceInfos": List["InstanceInfoTypeDef"]},
    total=False,
)

CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef", {"applicationId": str}, total=False
)

CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef", {"deploymentConfigId": str}, total=False
)

CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef", {"deploymentGroupId": str}, total=False
)

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef", {"deploymentId": str}, total=False
)

DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {"hooksNotCleanedUp": List["AutoScalingGroupTypeDef"]},
    total=False,
)

DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef", {"tokenName": str}, total=False
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef", {"application": "ApplicationInfoTypeDef"}, total=False
)

GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
    },
    total=False,
)

GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {"deploymentConfigInfo": "DeploymentConfigInfoTypeDef"},
    total=False,
)

GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {"deploymentGroupInfo": "DeploymentGroupInfoTypeDef"},
    total=False,
)

GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef", {"instanceSummary": "InstanceSummaryTypeDef"}, total=False
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef", {"deploymentInfo": "DeploymentInfoTypeDef"}, total=False
)

GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef", {"deploymentTarget": "DeploymentTargetTypeDef"}, total=False
)

GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef", {"instanceInfo": "InstanceInfoTypeDef"}, total=False
)

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {"revisions": List["RevisionLocationTypeDef"], "nextToken": str},
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef", {"applications": List[str], "nextToken": str}, total=False
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str},
    total=False,
)

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "nextToken": str},
    total=False,
)

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {"instancesList": List[str], "nextToken": str},
    total=False,
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef", {"targetIds": List[str], "nextToken": str}, total=False
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef", {"deployments": List[str], "nextToken": str}, total=False
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {"tokenNameList": List[str], "nextToken": str},
    total=False,
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {"instanceNames": List[str], "nextToken": str},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"Tags": List["TagTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    {"lifecycleEventHookExecutionId": str},
    total=False,
)

StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
    {"status": Literal["Pending", "Succeeded"], "statusMessage": str},
    total=False,
)

TimeRangeTypeDef = TypedDict("TimeRangeTypeDef", {"start": datetime, "end": datetime}, total=False)

UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
    {"hooksNotCleanedUp": List["AutoScalingGroupTypeDef"]},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
