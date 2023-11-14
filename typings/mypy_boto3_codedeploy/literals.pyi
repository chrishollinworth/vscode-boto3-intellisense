"""
Type annotations for codedeploy service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/literals.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.literals import ApplicationRevisionSortByType

    data: ApplicationRevisionSortByType = "firstUsedTime"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationRevisionSortByType",
    "AutoRollbackEventType",
    "BundleTypeType",
    "ComputePlatformType",
    "DeploymentCreatorType",
    "DeploymentOptionType",
    "DeploymentReadyActionType",
    "DeploymentStatusType",
    "DeploymentSuccessfulWaiterName",
    "DeploymentTargetTypeType",
    "DeploymentTypeType",
    "DeploymentWaitTypeType",
    "EC2TagFilterTypeType",
    "ErrorCodeType",
    "FileExistsBehaviorType",
    "GreenFleetProvisioningActionType",
    "InstanceActionType",
    "InstanceStatusType",
    "InstanceTypeType",
    "LifecycleErrorCodeType",
    "LifecycleEventStatusType",
    "ListApplicationRevisionsPaginatorName",
    "ListApplicationsPaginatorName",
    "ListDeploymentConfigsPaginatorName",
    "ListDeploymentGroupsPaginatorName",
    "ListDeploymentInstancesPaginatorName",
    "ListDeploymentTargetsPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListGitHubAccountTokenNamesPaginatorName",
    "ListOnPremisesInstancesPaginatorName",
    "ListStateFilterActionType",
    "MinimumHealthyHostsTypeType",
    "OutdatedInstancesStrategyType",
    "RegistrationStatusType",
    "RevisionLocationTypeType",
    "SortOrderType",
    "StopStatusType",
    "TagFilterTypeType",
    "TargetFilterNameType",
    "TargetLabelType",
    "TargetStatusType",
    "TrafficRoutingTypeType",
    "TriggerEventTypeType",
)

ApplicationRevisionSortByType = Literal["firstUsedTime", "lastUsedTime", "registerTime"]
AutoRollbackEventType = Literal[
    "DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"
]
BundleTypeType = Literal["JSON", "YAML", "tar", "tgz", "zip"]
ComputePlatformType = Literal["ECS", "Lambda", "Server"]
DeploymentCreatorType = Literal[
    "CloudFormation",
    "CloudFormationRollback",
    "CodeDeploy",
    "CodeDeployAutoUpdate",
    "autoscaling",
    "codeDeployRollback",
    "user",
]
DeploymentOptionType = Literal["WITHOUT_TRAFFIC_CONTROL", "WITH_TRAFFIC_CONTROL"]
DeploymentReadyActionType = Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"]
DeploymentStatusType = Literal[
    "Baking", "Created", "Failed", "InProgress", "Queued", "Ready", "Stopped", "Succeeded"
]
DeploymentSuccessfulWaiterName = Literal["deployment_successful"]
DeploymentTargetTypeType = Literal[
    "CloudFormationTarget", "ECSTarget", "InstanceTarget", "LambdaTarget"
]
DeploymentTypeType = Literal["BLUE_GREEN", "IN_PLACE"]
DeploymentWaitTypeType = Literal["READY_WAIT", "TERMINATION_WAIT"]
EC2TagFilterTypeType = Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]
ErrorCodeType = Literal[
    "AGENT_ISSUE",
    "ALARM_ACTIVE",
    "APPLICATION_MISSING",
    "AUTOSCALING_VALIDATION_ERROR",
    "AUTO_SCALING_CONFIGURATION",
    "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
    "CLOUDFORMATION_STACK_FAILURE",
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
]
FileExistsBehaviorType = Literal["DISALLOW", "OVERWRITE", "RETAIN"]
GreenFleetProvisioningActionType = Literal["COPY_AUTO_SCALING_GROUP", "DISCOVER_EXISTING"]
InstanceActionType = Literal["KEEP_ALIVE", "TERMINATE"]
InstanceStatusType = Literal[
    "Failed", "InProgress", "Pending", "Ready", "Skipped", "Succeeded", "Unknown"
]
InstanceTypeType = Literal["Blue", "Green"]
LifecycleErrorCodeType = Literal[
    "ScriptFailed",
    "ScriptMissing",
    "ScriptNotExecutable",
    "ScriptTimedOut",
    "Success",
    "UnknownError",
]
LifecycleEventStatusType = Literal[
    "Failed", "InProgress", "Pending", "Skipped", "Succeeded", "Unknown"
]
ListApplicationRevisionsPaginatorName = Literal["list_application_revisions"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListDeploymentConfigsPaginatorName = Literal["list_deployment_configs"]
ListDeploymentGroupsPaginatorName = Literal["list_deployment_groups"]
ListDeploymentInstancesPaginatorName = Literal["list_deployment_instances"]
ListDeploymentTargetsPaginatorName = Literal["list_deployment_targets"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListGitHubAccountTokenNamesPaginatorName = Literal["list_git_hub_account_token_names"]
ListOnPremisesInstancesPaginatorName = Literal["list_on_premises_instances"]
ListStateFilterActionType = Literal["exclude", "ignore", "include"]
MinimumHealthyHostsTypeType = Literal["FLEET_PERCENT", "HOST_COUNT"]
OutdatedInstancesStrategyType = Literal["IGNORE", "UPDATE"]
RegistrationStatusType = Literal["Deregistered", "Registered"]
RevisionLocationTypeType = Literal["AppSpecContent", "GitHub", "S3", "String"]
SortOrderType = Literal["ascending", "descending"]
StopStatusType = Literal["Pending", "Succeeded"]
TagFilterTypeType = Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]
TargetFilterNameType = Literal["ServerInstanceLabel", "TargetStatus"]
TargetLabelType = Literal["Blue", "Green"]
TargetStatusType = Literal[
    "Failed", "InProgress", "Pending", "Ready", "Skipped", "Succeeded", "Unknown"
]
TrafficRoutingTypeType = Literal["AllAtOnce", "TimeBasedCanary", "TimeBasedLinear"]
TriggerEventTypeType = Literal[
    "DeploymentFailure",
    "DeploymentReady",
    "DeploymentRollback",
    "DeploymentStart",
    "DeploymentStop",
    "DeploymentSuccess",
    "InstanceFailure",
    "InstanceReady",
    "InstanceStart",
    "InstanceSuccess",
]
