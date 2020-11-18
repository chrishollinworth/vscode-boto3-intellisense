# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for codedeploy service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codedeploy import CodeDeployClient

    client: CodeDeployClient = boto3.client("codedeploy")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_codedeploy.paginator import (
    ListApplicationRevisionsPaginator,
    ListApplicationsPaginator,
    ListDeploymentConfigsPaginator,
    ListDeploymentGroupsPaginator,
    ListDeploymentInstancesPaginator,
    ListDeploymentsPaginator,
    ListDeploymentTargetsPaginator,
    ListGitHubAccountTokenNamesPaginator,
    ListOnPremisesInstancesPaginator,
)
from mypy_boto3_codedeploy.type_defs import (
    AlarmConfigurationTypeDef,
    AutoRollbackConfigurationTypeDef,
    BatchGetApplicationRevisionsOutputTypeDef,
    BatchGetApplicationsOutputTypeDef,
    BatchGetDeploymentGroupsOutputTypeDef,
    BatchGetDeploymentInstancesOutputTypeDef,
    BatchGetDeploymentsOutputTypeDef,
    BatchGetDeploymentTargetsOutputTypeDef,
    BatchGetOnPremisesInstancesOutputTypeDef,
    BlueGreenDeploymentConfigurationTypeDef,
    CreateApplicationOutputTypeDef,
    CreateDeploymentConfigOutputTypeDef,
    CreateDeploymentGroupOutputTypeDef,
    CreateDeploymentOutputTypeDef,
    DeleteDeploymentGroupOutputTypeDef,
    DeleteGitHubAccountTokenOutputTypeDef,
    DeploymentStyleTypeDef,
    EC2TagFilterTypeDef,
    EC2TagSetTypeDef,
    ECSServiceTypeDef,
    GetApplicationOutputTypeDef,
    GetApplicationRevisionOutputTypeDef,
    GetDeploymentConfigOutputTypeDef,
    GetDeploymentGroupOutputTypeDef,
    GetDeploymentInstanceOutputTypeDef,
    GetDeploymentOutputTypeDef,
    GetDeploymentTargetOutputTypeDef,
    GetOnPremisesInstanceOutputTypeDef,
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoadBalancerInfoTypeDef,
    MinimumHealthyHostsTypeDef,
    OnPremisesTagSetTypeDef,
    PutLifecycleEventHookExecutionStatusOutputTypeDef,
    RevisionLocationTypeDef,
    StopDeploymentOutputTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
    TargetInstancesTypeDef,
    TimeRangeTypeDef,
    TrafficRoutingConfigTypeDef,
    TriggerConfigTypeDef,
    UpdateDeploymentGroupOutputTypeDef,
)
from mypy_boto3_codedeploy.waiter import DeploymentSuccessfulWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeDeployClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlarmsLimitExceededException: Type[BotocoreClientError]
    ApplicationAlreadyExistsException: Type[BotocoreClientError]
    ApplicationDoesNotExistException: Type[BotocoreClientError]
    ApplicationLimitExceededException: Type[BotocoreClientError]
    ApplicationNameRequiredException: Type[BotocoreClientError]
    ArnNotSupportedException: Type[BotocoreClientError]
    BatchLimitExceededException: Type[BotocoreClientError]
    BucketNameFilterRequiredException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DeploymentAlreadyCompletedException: Type[BotocoreClientError]
    DeploymentAlreadyStartedException: Type[BotocoreClientError]
    DeploymentConfigAlreadyExistsException: Type[BotocoreClientError]
    DeploymentConfigDoesNotExistException: Type[BotocoreClientError]
    DeploymentConfigInUseException: Type[BotocoreClientError]
    DeploymentConfigLimitExceededException: Type[BotocoreClientError]
    DeploymentConfigNameRequiredException: Type[BotocoreClientError]
    DeploymentDoesNotExistException: Type[BotocoreClientError]
    DeploymentGroupAlreadyExistsException: Type[BotocoreClientError]
    DeploymentGroupDoesNotExistException: Type[BotocoreClientError]
    DeploymentGroupLimitExceededException: Type[BotocoreClientError]
    DeploymentGroupNameRequiredException: Type[BotocoreClientError]
    DeploymentIdRequiredException: Type[BotocoreClientError]
    DeploymentIsNotInReadyStateException: Type[BotocoreClientError]
    DeploymentLimitExceededException: Type[BotocoreClientError]
    DeploymentNotStartedException: Type[BotocoreClientError]
    DeploymentTargetDoesNotExistException: Type[BotocoreClientError]
    DeploymentTargetIdRequiredException: Type[BotocoreClientError]
    DeploymentTargetListSizeExceededException: Type[BotocoreClientError]
    DescriptionTooLongException: Type[BotocoreClientError]
    ECSServiceMappingLimitExceededException: Type[BotocoreClientError]
    GitHubAccountTokenDoesNotExistException: Type[BotocoreClientError]
    GitHubAccountTokenNameRequiredException: Type[BotocoreClientError]
    IamArnRequiredException: Type[BotocoreClientError]
    IamSessionArnAlreadyRegisteredException: Type[BotocoreClientError]
    IamUserArnAlreadyRegisteredException: Type[BotocoreClientError]
    IamUserArnRequiredException: Type[BotocoreClientError]
    InstanceDoesNotExistException: Type[BotocoreClientError]
    InstanceIdRequiredException: Type[BotocoreClientError]
    InstanceLimitExceededException: Type[BotocoreClientError]
    InstanceNameAlreadyRegisteredException: Type[BotocoreClientError]
    InstanceNameRequiredException: Type[BotocoreClientError]
    InstanceNotRegisteredException: Type[BotocoreClientError]
    InvalidAlarmConfigException: Type[BotocoreClientError]
    InvalidApplicationNameException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidAutoRollbackConfigException: Type[BotocoreClientError]
    InvalidAutoScalingGroupException: Type[BotocoreClientError]
    InvalidBlueGreenDeploymentConfigurationException: Type[BotocoreClientError]
    InvalidBucketNameFilterException: Type[BotocoreClientError]
    InvalidComputePlatformException: Type[BotocoreClientError]
    InvalidDeployedStateFilterException: Type[BotocoreClientError]
    InvalidDeploymentConfigIdException: Type[BotocoreClientError]
    InvalidDeploymentConfigNameException: Type[BotocoreClientError]
    InvalidDeploymentGroupNameException: Type[BotocoreClientError]
    InvalidDeploymentIdException: Type[BotocoreClientError]
    InvalidDeploymentInstanceTypeException: Type[BotocoreClientError]
    InvalidDeploymentStatusException: Type[BotocoreClientError]
    InvalidDeploymentStyleException: Type[BotocoreClientError]
    InvalidDeploymentTargetIdException: Type[BotocoreClientError]
    InvalidDeploymentWaitTypeException: Type[BotocoreClientError]
    InvalidEC2TagCombinationException: Type[BotocoreClientError]
    InvalidEC2TagException: Type[BotocoreClientError]
    InvalidECSServiceException: Type[BotocoreClientError]
    InvalidExternalIdException: Type[BotocoreClientError]
    InvalidFileExistsBehaviorException: Type[BotocoreClientError]
    InvalidGitHubAccountTokenException: Type[BotocoreClientError]
    InvalidGitHubAccountTokenNameException: Type[BotocoreClientError]
    InvalidIamSessionArnException: Type[BotocoreClientError]
    InvalidIamUserArnException: Type[BotocoreClientError]
    InvalidIgnoreApplicationStopFailuresValueException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidInstanceIdException: Type[BotocoreClientError]
    InvalidInstanceNameException: Type[BotocoreClientError]
    InvalidInstanceStatusException: Type[BotocoreClientError]
    InvalidInstanceTypeException: Type[BotocoreClientError]
    InvalidKeyPrefixFilterException: Type[BotocoreClientError]
    InvalidLifecycleEventHookExecutionIdException: Type[BotocoreClientError]
    InvalidLifecycleEventHookExecutionStatusException: Type[BotocoreClientError]
    InvalidLoadBalancerInfoException: Type[BotocoreClientError]
    InvalidMinimumHealthyHostValueException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidOnPremisesTagCombinationException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRegistrationStatusException: Type[BotocoreClientError]
    InvalidRevisionException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    InvalidSortByException: Type[BotocoreClientError]
    InvalidSortOrderException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    InvalidTagFilterException: Type[BotocoreClientError]
    InvalidTagsToAddException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    InvalidTargetFilterNameException: Type[BotocoreClientError]
    InvalidTargetGroupPairException: Type[BotocoreClientError]
    InvalidTargetInstancesException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    InvalidTrafficRoutingConfigurationException: Type[BotocoreClientError]
    InvalidTriggerConfigException: Type[BotocoreClientError]
    InvalidUpdateOutdatedInstancesOnlyValueException: Type[BotocoreClientError]
    LifecycleEventAlreadyCompletedException: Type[BotocoreClientError]
    LifecycleHookLimitExceededException: Type[BotocoreClientError]
    MultipleIamArnsProvidedException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceArnRequiredException: Type[BotocoreClientError]
    ResourceValidationException: Type[BotocoreClientError]
    RevisionDoesNotExistException: Type[BotocoreClientError]
    RevisionRequiredException: Type[BotocoreClientError]
    RoleRequiredException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    TagRequiredException: Type[BotocoreClientError]
    TagSetListLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TriggerTargetsLimitExceededException: Type[BotocoreClientError]
    UnsupportedActionForDeploymentTypeException: Type[BotocoreClientError]


class CodeDeployClient:
    """
    [CodeDeploy.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags_to_on_premises_instances(
        self, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        [Client.add_tags_to_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.add_tags_to_on_premises_instances)
        """

    def batch_get_application_revisions(
        self, applicationName: str, revisions: List["RevisionLocationTypeDef"]
    ) -> BatchGetApplicationRevisionsOutputTypeDef:
        """
        [Client.batch_get_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_application_revisions)
        """

    def batch_get_applications(
        self, applicationNames: List[str]
    ) -> BatchGetApplicationsOutputTypeDef:
        """
        [Client.batch_get_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_applications)
        """

    def batch_get_deployment_groups(
        self, applicationName: str, deploymentGroupNames: List[str]
    ) -> BatchGetDeploymentGroupsOutputTypeDef:
        """
        [Client.batch_get_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_groups)
        """

    def batch_get_deployment_instances(
        self, deploymentId: str, instanceIds: List[str]
    ) -> BatchGetDeploymentInstancesOutputTypeDef:
        """
        [Client.batch_get_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_instances)
        """

    def batch_get_deployment_targets(
        self, deploymentId: str = None, targetIds: List[str] = None
    ) -> BatchGetDeploymentTargetsOutputTypeDef:
        """
        [Client.batch_get_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_targets)
        """

    def batch_get_deployments(self, deploymentIds: List[str]) -> BatchGetDeploymentsOutputTypeDef:
        """
        [Client.batch_get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployments)
        """

    def batch_get_on_premises_instances(
        self, instanceNames: List[str]
    ) -> BatchGetOnPremisesInstancesOutputTypeDef:
        """
        [Client.batch_get_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_on_premises_instances)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.can_paginate)
        """

    def continue_deployment(
        self,
        deploymentId: str = None,
        deploymentWaitType: Literal["READY_WAIT", "TERMINATION_WAIT"] = None,
    ) -> None:
        """
        [Client.continue_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.continue_deployment)
        """

    def create_application(
        self,
        applicationName: str,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationOutputTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.create_application)
        """

    def create_deployment(
        self,
        applicationName: str,
        deploymentGroupName: str = None,
        revision: "RevisionLocationTypeDef" = None,
        deploymentConfigName: str = None,
        description: str = None,
        ignoreApplicationStopFailures: bool = None,
        targetInstances: "TargetInstancesTypeDef" = None,
        autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
        updateOutdatedInstancesOnly: bool = None,
        fileExistsBehavior: Literal["DISALLOW", "OVERWRITE", "RETAIN"] = None,
    ) -> CreateDeploymentOutputTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment)
        """

    def create_deployment_config(
        self,
        deploymentConfigName: str,
        minimumHealthyHosts: "MinimumHealthyHostsTypeDef" = None,
        trafficRoutingConfig: "TrafficRoutingConfigTypeDef" = None,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
    ) -> CreateDeploymentConfigOutputTypeDef:
        """
        [Client.create_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_config)
        """

    def create_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
        serviceRoleArn: str,
        deploymentConfigName: str = None,
        ec2TagFilters: List["EC2TagFilterTypeDef"] = None,
        onPremisesInstanceTagFilters: List["TagFilterTypeDef"] = None,
        autoScalingGroups: List[str] = None,
        triggerConfigurations: List["TriggerConfigTypeDef"] = None,
        alarmConfiguration: "AlarmConfigurationTypeDef" = None,
        autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
        deploymentStyle: "DeploymentStyleTypeDef" = None,
        blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
        loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
        ec2TagSet: "EC2TagSetTypeDef" = None,
        ecsServices: List["ECSServiceTypeDef"] = None,
        onPremisesTagSet: "OnPremisesTagSetTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDeploymentGroupOutputTypeDef:
        """
        [Client.create_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_group)
        """

    def delete_application(self, applicationName: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.delete_application)
        """

    def delete_deployment_config(self, deploymentConfigName: str) -> None:
        """
        [Client.delete_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_config)
        """

    def delete_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> DeleteDeploymentGroupOutputTypeDef:
        """
        [Client.delete_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_group)
        """

    def delete_git_hub_account_token(
        self, tokenName: str = None
    ) -> DeleteGitHubAccountTokenOutputTypeDef:
        """
        [Client.delete_git_hub_account_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.delete_git_hub_account_token)
        """

    def delete_resources_by_external_id(self, externalId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resources_by_external_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.delete_resources_by_external_id)
        """

    def deregister_on_premises_instance(self, instanceName: str) -> None:
        """
        [Client.deregister_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.deregister_on_premises_instance)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.generate_presigned_url)
        """

    def get_application(self, applicationName: str) -> GetApplicationOutputTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_application)
        """

    def get_application_revision(
        self, applicationName: str, revision: "RevisionLocationTypeDef"
    ) -> GetApplicationRevisionOutputTypeDef:
        """
        [Client.get_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_application_revision)
        """

    def get_deployment(self, deploymentId: str) -> GetDeploymentOutputTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment)
        """

    def get_deployment_config(self, deploymentConfigName: str) -> GetDeploymentConfigOutputTypeDef:
        """
        [Client.get_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_config)
        """

    def get_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> GetDeploymentGroupOutputTypeDef:
        """
        [Client.get_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_group)
        """

    def get_deployment_instance(
        self, deploymentId: str, instanceId: str
    ) -> GetDeploymentInstanceOutputTypeDef:
        """
        [Client.get_deployment_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_instance)
        """

    def get_deployment_target(
        self, deploymentId: str = None, targetId: str = None
    ) -> GetDeploymentTargetOutputTypeDef:
        """
        [Client.get_deployment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_target)
        """

    def get_on_premises_instance(self, instanceName: str) -> GetOnPremisesInstanceOutputTypeDef:
        """
        [Client.get_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.get_on_premises_instance)
        """

    def list_application_revisions(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        nextToken: str = None,
    ) -> ListApplicationRevisionsOutputTypeDef:
        """
        [Client.list_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_application_revisions)
        """

    def list_applications(self, nextToken: str = None) -> ListApplicationsOutputTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_applications)
        """

    def list_deployment_configs(self, nextToken: str = None) -> ListDeploymentConfigsOutputTypeDef:
        """
        [Client.list_deployment_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_configs)
        """

    def list_deployment_groups(
        self, applicationName: str, nextToken: str = None
    ) -> ListDeploymentGroupsOutputTypeDef:
        """
        [Client.list_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_groups)
        """

    def list_deployment_instances(
        self,
        deploymentId: str,
        nextToken: str = None,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
    ) -> ListDeploymentInstancesOutputTypeDef:
        """
        [Client.list_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_instances)
        """

    def list_deployment_targets(
        self,
        deploymentId: str = None,
        nextToken: str = None,
        targetFilters: Dict[Literal["TargetStatus", "ServerInstanceLabel"], List[str]] = None,
    ) -> ListDeploymentTargetsOutputTypeDef:
        """
        [Client.list_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_targets)
        """

    def list_deployments(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        externalId: str = None,
        includeOnlyStatuses: List[
            Literal[
                "Created",
                "Queued",
                "InProgress",
                "Baking",
                "Succeeded",
                "Failed",
                "Stopped",
                "Ready",
            ]
        ] = None,
        createTimeRange: TimeRangeTypeDef = None,
        nextToken: str = None,
    ) -> ListDeploymentsOutputTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_deployments)
        """

    def list_git_hub_account_token_names(
        self, nextToken: str = None
    ) -> ListGitHubAccountTokenNamesOutputTypeDef:
        """
        [Client.list_git_hub_account_token_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_git_hub_account_token_names)
        """

    def list_on_premises_instances(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        nextToken: str = None,
    ) -> ListOnPremisesInstancesOutputTypeDef:
        """
        [Client.list_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_on_premises_instances)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.list_tags_for_resource)
        """

    def put_lifecycle_event_hook_execution_status(
        self,
        deploymentId: str = None,
        lifecycleEventHookExecutionId: str = None,
        status: Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"
        ] = None,
    ) -> PutLifecycleEventHookExecutionStatusOutputTypeDef:
        """
        [Client.put_lifecycle_event_hook_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.put_lifecycle_event_hook_execution_status)
        """

    def register_application_revision(
        self, applicationName: str, revision: "RevisionLocationTypeDef", description: str = None
    ) -> None:
        """
        [Client.register_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.register_application_revision)
        """

    def register_on_premises_instance(
        self, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None
    ) -> None:
        """
        [Client.register_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.register_on_premises_instance)
        """

    def remove_tags_from_on_premises_instances(
        self, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        [Client.remove_tags_from_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.remove_tags_from_on_premises_instances)
        """

    def skip_wait_time_for_instance_termination(self, deploymentId: str = None) -> None:
        """
        [Client.skip_wait_time_for_instance_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.skip_wait_time_for_instance_termination)
        """

    def stop_deployment(
        self, deploymentId: str, autoRollbackEnabled: bool = None
    ) -> StopDeploymentOutputTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.stop_deployment)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.untag_resource)
        """

    def update_application(
        self, applicationName: str = None, newApplicationName: str = None
    ) -> None:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.update_application)
        """

    def update_deployment_group(
        self,
        applicationName: str,
        currentDeploymentGroupName: str,
        newDeploymentGroupName: str = None,
        deploymentConfigName: str = None,
        ec2TagFilters: List["EC2TagFilterTypeDef"] = None,
        onPremisesInstanceTagFilters: List["TagFilterTypeDef"] = None,
        autoScalingGroups: List[str] = None,
        serviceRoleArn: str = None,
        triggerConfigurations: List["TriggerConfigTypeDef"] = None,
        alarmConfiguration: "AlarmConfigurationTypeDef" = None,
        autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
        deploymentStyle: "DeploymentStyleTypeDef" = None,
        blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
        loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
        ec2TagSet: "EC2TagSetTypeDef" = None,
        ecsServices: List["ECSServiceTypeDef"] = None,
        onPremisesTagSet: "OnPremisesTagSetTypeDef" = None,
    ) -> UpdateDeploymentGroupOutputTypeDef:
        """
        [Client.update_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Client.update_deployment_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_revisions"]
    ) -> ListApplicationRevisionsPaginator:
        """
        [Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_configs"]
    ) -> ListDeploymentConfigsPaginator:
        """
        [Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_groups"]
    ) -> ListDeploymentGroupsPaginator:
        """
        [Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_instances"]
    ) -> ListDeploymentInstancesPaginator:
        """
        [Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_targets"]
    ) -> ListDeploymentTargetsPaginator:
        """
        [Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> ListGitHubAccountTokenNamesPaginator:
        """
        [Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> ListOnPremisesInstancesPaginator:
        """
        [Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
        """

    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> DeploymentSuccessfulWaiter:
        """
        [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
        """
