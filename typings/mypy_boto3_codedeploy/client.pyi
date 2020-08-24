# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

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


class Exceptions:
    AlarmsLimitExceededException: Type[Boto3ClientError]
    ApplicationAlreadyExistsException: Type[Boto3ClientError]
    ApplicationDoesNotExistException: Type[Boto3ClientError]
    ApplicationLimitExceededException: Type[Boto3ClientError]
    ApplicationNameRequiredException: Type[Boto3ClientError]
    ArnNotSupportedException: Type[Boto3ClientError]
    BatchLimitExceededException: Type[Boto3ClientError]
    BucketNameFilterRequiredException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DeploymentAlreadyCompletedException: Type[Boto3ClientError]
    DeploymentAlreadyStartedException: Type[Boto3ClientError]
    DeploymentConfigAlreadyExistsException: Type[Boto3ClientError]
    DeploymentConfigDoesNotExistException: Type[Boto3ClientError]
    DeploymentConfigInUseException: Type[Boto3ClientError]
    DeploymentConfigLimitExceededException: Type[Boto3ClientError]
    DeploymentConfigNameRequiredException: Type[Boto3ClientError]
    DeploymentDoesNotExistException: Type[Boto3ClientError]
    DeploymentGroupAlreadyExistsException: Type[Boto3ClientError]
    DeploymentGroupDoesNotExistException: Type[Boto3ClientError]
    DeploymentGroupLimitExceededException: Type[Boto3ClientError]
    DeploymentGroupNameRequiredException: Type[Boto3ClientError]
    DeploymentIdRequiredException: Type[Boto3ClientError]
    DeploymentIsNotInReadyStateException: Type[Boto3ClientError]
    DeploymentLimitExceededException: Type[Boto3ClientError]
    DeploymentNotStartedException: Type[Boto3ClientError]
    DeploymentTargetDoesNotExistException: Type[Boto3ClientError]
    DeploymentTargetIdRequiredException: Type[Boto3ClientError]
    DeploymentTargetListSizeExceededException: Type[Boto3ClientError]
    DescriptionTooLongException: Type[Boto3ClientError]
    ECSServiceMappingLimitExceededException: Type[Boto3ClientError]
    GitHubAccountTokenDoesNotExistException: Type[Boto3ClientError]
    GitHubAccountTokenNameRequiredException: Type[Boto3ClientError]
    IamArnRequiredException: Type[Boto3ClientError]
    IamSessionArnAlreadyRegisteredException: Type[Boto3ClientError]
    IamUserArnAlreadyRegisteredException: Type[Boto3ClientError]
    IamUserArnRequiredException: Type[Boto3ClientError]
    InstanceDoesNotExistException: Type[Boto3ClientError]
    InstanceIdRequiredException: Type[Boto3ClientError]
    InstanceLimitExceededException: Type[Boto3ClientError]
    InstanceNameAlreadyRegisteredException: Type[Boto3ClientError]
    InstanceNameRequiredException: Type[Boto3ClientError]
    InstanceNotRegisteredException: Type[Boto3ClientError]
    InvalidAlarmConfigException: Type[Boto3ClientError]
    InvalidApplicationNameException: Type[Boto3ClientError]
    InvalidArnException: Type[Boto3ClientError]
    InvalidAutoRollbackConfigException: Type[Boto3ClientError]
    InvalidAutoScalingGroupException: Type[Boto3ClientError]
    InvalidBlueGreenDeploymentConfigurationException: Type[Boto3ClientError]
    InvalidBucketNameFilterException: Type[Boto3ClientError]
    InvalidComputePlatformException: Type[Boto3ClientError]
    InvalidDeployedStateFilterException: Type[Boto3ClientError]
    InvalidDeploymentConfigIdException: Type[Boto3ClientError]
    InvalidDeploymentConfigNameException: Type[Boto3ClientError]
    InvalidDeploymentGroupNameException: Type[Boto3ClientError]
    InvalidDeploymentIdException: Type[Boto3ClientError]
    InvalidDeploymentInstanceTypeException: Type[Boto3ClientError]
    InvalidDeploymentStatusException: Type[Boto3ClientError]
    InvalidDeploymentStyleException: Type[Boto3ClientError]
    InvalidDeploymentTargetIdException: Type[Boto3ClientError]
    InvalidDeploymentWaitTypeException: Type[Boto3ClientError]
    InvalidEC2TagCombinationException: Type[Boto3ClientError]
    InvalidEC2TagException: Type[Boto3ClientError]
    InvalidECSServiceException: Type[Boto3ClientError]
    InvalidExternalIdException: Type[Boto3ClientError]
    InvalidFileExistsBehaviorException: Type[Boto3ClientError]
    InvalidGitHubAccountTokenException: Type[Boto3ClientError]
    InvalidGitHubAccountTokenNameException: Type[Boto3ClientError]
    InvalidIamSessionArnException: Type[Boto3ClientError]
    InvalidIamUserArnException: Type[Boto3ClientError]
    InvalidIgnoreApplicationStopFailuresValueException: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    InvalidInstanceIdException: Type[Boto3ClientError]
    InvalidInstanceNameException: Type[Boto3ClientError]
    InvalidInstanceStatusException: Type[Boto3ClientError]
    InvalidInstanceTypeException: Type[Boto3ClientError]
    InvalidKeyPrefixFilterException: Type[Boto3ClientError]
    InvalidLifecycleEventHookExecutionIdException: Type[Boto3ClientError]
    InvalidLifecycleEventHookExecutionStatusException: Type[Boto3ClientError]
    InvalidLoadBalancerInfoException: Type[Boto3ClientError]
    InvalidMinimumHealthyHostValueException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidOnPremisesTagCombinationException: Type[Boto3ClientError]
    InvalidOperationException: Type[Boto3ClientError]
    InvalidRegistrationStatusException: Type[Boto3ClientError]
    InvalidRevisionException: Type[Boto3ClientError]
    InvalidRoleException: Type[Boto3ClientError]
    InvalidSortByException: Type[Boto3ClientError]
    InvalidSortOrderException: Type[Boto3ClientError]
    InvalidTagException: Type[Boto3ClientError]
    InvalidTagFilterException: Type[Boto3ClientError]
    InvalidTagsToAddException: Type[Boto3ClientError]
    InvalidTargetException: Type[Boto3ClientError]
    InvalidTargetFilterNameException: Type[Boto3ClientError]
    InvalidTargetGroupPairException: Type[Boto3ClientError]
    InvalidTargetInstancesException: Type[Boto3ClientError]
    InvalidTimeRangeException: Type[Boto3ClientError]
    InvalidTrafficRoutingConfigurationException: Type[Boto3ClientError]
    InvalidTriggerConfigException: Type[Boto3ClientError]
    InvalidUpdateOutdatedInstancesOnlyValueException: Type[Boto3ClientError]
    LifecycleEventAlreadyCompletedException: Type[Boto3ClientError]
    LifecycleHookLimitExceededException: Type[Boto3ClientError]
    MultipleIamArnsProvidedException: Type[Boto3ClientError]
    OperationNotSupportedException: Type[Boto3ClientError]
    ResourceArnRequiredException: Type[Boto3ClientError]
    ResourceValidationException: Type[Boto3ClientError]
    RevisionDoesNotExistException: Type[Boto3ClientError]
    RevisionRequiredException: Type[Boto3ClientError]
    RoleRequiredException: Type[Boto3ClientError]
    TagLimitExceededException: Type[Boto3ClientError]
    TagRequiredException: Type[Boto3ClientError]
    TagSetListLimitExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    TriggerTargetsLimitExceededException: Type[Boto3ClientError]
    UnsupportedActionForDeploymentTypeException: Type[Boto3ClientError]


class CodeDeployClient:
    """
    [CodeDeploy.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client)
    """

    exceptions: Exceptions

    def add_tags_to_on_premises_instances(
        self, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        [Client.add_tags_to_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.add_tags_to_on_premises_instances)
        """

    def batch_get_application_revisions(
        self, applicationName: str, revisions: List["RevisionLocationTypeDef"]
    ) -> BatchGetApplicationRevisionsOutputTypeDef:
        """
        [Client.batch_get_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_application_revisions)
        """

    def batch_get_applications(
        self, applicationNames: List[str]
    ) -> BatchGetApplicationsOutputTypeDef:
        """
        [Client.batch_get_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_applications)
        """

    def batch_get_deployment_groups(
        self, applicationName: str, deploymentGroupNames: List[str]
    ) -> BatchGetDeploymentGroupsOutputTypeDef:
        """
        [Client.batch_get_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_groups)
        """

    def batch_get_deployment_instances(
        self, deploymentId: str, instanceIds: List[str]
    ) -> BatchGetDeploymentInstancesOutputTypeDef:
        """
        [Client.batch_get_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_instances)
        """

    def batch_get_deployment_targets(
        self, deploymentId: str = None, targetIds: List[str] = None
    ) -> BatchGetDeploymentTargetsOutputTypeDef:
        """
        [Client.batch_get_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_targets)
        """

    def batch_get_deployments(self, deploymentIds: List[str]) -> BatchGetDeploymentsOutputTypeDef:
        """
        [Client.batch_get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployments)
        """

    def batch_get_on_premises_instances(
        self, instanceNames: List[str]
    ) -> BatchGetOnPremisesInstancesOutputTypeDef:
        """
        [Client.batch_get_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_on_premises_instances)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.can_paginate)
        """

    def continue_deployment(
        self,
        deploymentId: str = None,
        deploymentWaitType: Literal["READY_WAIT", "TERMINATION_WAIT"] = None,
    ) -> None:
        """
        [Client.continue_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.continue_deployment)
        """

    def create_application(
        self,
        applicationName: str,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationOutputTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.create_application)
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
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment)
        """

    def create_deployment_config(
        self,
        deploymentConfigName: str,
        minimumHealthyHosts: "MinimumHealthyHostsTypeDef" = None,
        trafficRoutingConfig: "TrafficRoutingConfigTypeDef" = None,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
    ) -> CreateDeploymentConfigOutputTypeDef:
        """
        [Client.create_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_config)
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
        [Client.create_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_group)
        """

    def delete_application(self, applicationName: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.delete_application)
        """

    def delete_deployment_config(self, deploymentConfigName: str) -> None:
        """
        [Client.delete_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_config)
        """

    def delete_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> DeleteDeploymentGroupOutputTypeDef:
        """
        [Client.delete_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_group)
        """

    def delete_git_hub_account_token(
        self, tokenName: str = None
    ) -> DeleteGitHubAccountTokenOutputTypeDef:
        """
        [Client.delete_git_hub_account_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.delete_git_hub_account_token)
        """

    def delete_resources_by_external_id(self, externalId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resources_by_external_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.delete_resources_by_external_id)
        """

    def deregister_on_premises_instance(self, instanceName: str) -> None:
        """
        [Client.deregister_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.deregister_on_premises_instance)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.generate_presigned_url)
        """

    def get_application(self, applicationName: str) -> GetApplicationOutputTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_application)
        """

    def get_application_revision(
        self, applicationName: str, revision: "RevisionLocationTypeDef"
    ) -> GetApplicationRevisionOutputTypeDef:
        """
        [Client.get_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_application_revision)
        """

    def get_deployment(self, deploymentId: str) -> GetDeploymentOutputTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment)
        """

    def get_deployment_config(self, deploymentConfigName: str) -> GetDeploymentConfigOutputTypeDef:
        """
        [Client.get_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_config)
        """

    def get_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> GetDeploymentGroupOutputTypeDef:
        """
        [Client.get_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_group)
        """

    def get_deployment_instance(
        self, deploymentId: str, instanceId: str
    ) -> GetDeploymentInstanceOutputTypeDef:
        """
        [Client.get_deployment_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_instance)
        """

    def get_deployment_target(
        self, deploymentId: str = None, targetId: str = None
    ) -> GetDeploymentTargetOutputTypeDef:
        """
        [Client.get_deployment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_target)
        """

    def get_on_premises_instance(self, instanceName: str) -> GetOnPremisesInstanceOutputTypeDef:
        """
        [Client.get_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.get_on_premises_instance)
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
        [Client.list_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_application_revisions)
        """

    def list_applications(self, nextToken: str = None) -> ListApplicationsOutputTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_applications)
        """

    def list_deployment_configs(self, nextToken: str = None) -> ListDeploymentConfigsOutputTypeDef:
        """
        [Client.list_deployment_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_configs)
        """

    def list_deployment_groups(
        self, applicationName: str, nextToken: str = None
    ) -> ListDeploymentGroupsOutputTypeDef:
        """
        [Client.list_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_groups)
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
        [Client.list_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_instances)
        """

    def list_deployment_targets(
        self,
        deploymentId: str = None,
        nextToken: str = None,
        targetFilters: Dict[Literal["TargetStatus", "ServerInstanceLabel"], List[str]] = None,
    ) -> ListDeploymentTargetsOutputTypeDef:
        """
        [Client.list_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_targets)
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
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_deployments)
        """

    def list_git_hub_account_token_names(
        self, nextToken: str = None
    ) -> ListGitHubAccountTokenNamesOutputTypeDef:
        """
        [Client.list_git_hub_account_token_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_git_hub_account_token_names)
        """

    def list_on_premises_instances(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        nextToken: str = None,
    ) -> ListOnPremisesInstancesOutputTypeDef:
        """
        [Client.list_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_on_premises_instances)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.list_tags_for_resource)
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
        [Client.put_lifecycle_event_hook_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.put_lifecycle_event_hook_execution_status)
        """

    def register_application_revision(
        self, applicationName: str, revision: "RevisionLocationTypeDef", description: str = None
    ) -> None:
        """
        [Client.register_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.register_application_revision)
        """

    def register_on_premises_instance(
        self, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None
    ) -> None:
        """
        [Client.register_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.register_on_premises_instance)
        """

    def remove_tags_from_on_premises_instances(
        self, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        [Client.remove_tags_from_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.remove_tags_from_on_premises_instances)
        """

    def skip_wait_time_for_instance_termination(self, deploymentId: str = None) -> None:
        """
        [Client.skip_wait_time_for_instance_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.skip_wait_time_for_instance_termination)
        """

    def stop_deployment(
        self, deploymentId: str, autoRollbackEnabled: bool = None
    ) -> StopDeploymentOutputTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.stop_deployment)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.untag_resource)
        """

    def update_application(
        self, applicationName: str = None, newApplicationName: str = None
    ) -> None:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.update_application)
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
        [Client.update_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Client.update_deployment_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_revisions"]
    ) -> ListApplicationRevisionsPaginator:
        """
        [Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_configs"]
    ) -> ListDeploymentConfigsPaginator:
        """
        [Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_groups"]
    ) -> ListDeploymentGroupsPaginator:
        """
        [Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_instances"]
    ) -> ListDeploymentInstancesPaginator:
        """
        [Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_targets"]
    ) -> ListDeploymentTargetsPaginator:
        """
        [Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> ListGitHubAccountTokenNamesPaginator:
        """
        [Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> ListOnPremisesInstancesPaginator:
        """
        [Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> DeploymentSuccessfulWaiter:
        """
        [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
        """
