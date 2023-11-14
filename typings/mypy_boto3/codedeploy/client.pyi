"""
Type annotations for codedeploy service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codedeploy import CodeDeployClient

    client: CodeDeployClient = boto3.client("codedeploy")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApplicationRevisionSortByType,
    ComputePlatformType,
    DeploymentStatusType,
    DeploymentWaitTypeType,
    FileExistsBehaviorType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleEventStatusType,
    ListStateFilterActionType,
    OutdatedInstancesStrategyType,
    RegistrationStatusType,
    SortOrderType,
    TargetFilterNameType,
)
from .paginator import (
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
from .type_defs import (
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
from .waiter import DeploymentSuccessfulWaiter

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

class CodeDeployClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeDeployClient exceptions.
        """
    def add_tags_to_on_premises_instances(
        self, *, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        Adds tags to on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.add_tags_to_on_premises_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#add_tags_to_on_premises_instances)
        """
    def batch_get_application_revisions(
        self, *, applicationName: str, revisions: List["RevisionLocationTypeDef"]
    ) -> BatchGetApplicationRevisionsOutputTypeDef:
        """
        Gets information about one or more application revisions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_application_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_application_revisions)
        """
    def batch_get_applications(
        self, *, applicationNames: List[str]
    ) -> BatchGetApplicationsOutputTypeDef:
        """
        Gets information about one or more applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_applications)
        """
    def batch_get_deployment_groups(
        self, *, applicationName: str, deploymentGroupNames: List[str]
    ) -> BatchGetDeploymentGroupsOutputTypeDef:
        """
        Gets information about one or more deployment groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_deployment_groups)
        """
    def batch_get_deployment_instances(
        self, *, deploymentId: str, instanceIds: List[str]
    ) -> BatchGetDeploymentInstancesOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_deployment_instances)
        """
    def batch_get_deployment_targets(
        self, *, deploymentId: str = None, targetIds: List[str] = None
    ) -> BatchGetDeploymentTargetsOutputTypeDef:
        """
        Returns an array of one or more targets associated with a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_deployment_targets)
        """
    def batch_get_deployments(
        self, *, deploymentIds: List[str]
    ) -> BatchGetDeploymentsOutputTypeDef:
        """
        Gets information about one or more deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_deployments)
        """
    def batch_get_on_premises_instances(
        self, *, instanceNames: List[str]
    ) -> BatchGetOnPremisesInstancesOutputTypeDef:
        """
        Gets information about one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_on_premises_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#batch_get_on_premises_instances)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#close)
        """
    def continue_deployment(
        self, *, deploymentId: str = None, deploymentWaitType: DeploymentWaitTypeType = None
    ) -> None:
        """
        For a blue/green deployment, starts the process of rerouting traffic from
        instances in the original environment to instances in the replacement
        environment without waiting for a specified wait time to elapse.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.continue_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#continue_deployment)
        """
    def create_application(
        self,
        *,
        applicationName: str,
        computePlatform: ComputePlatformType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateApplicationOutputTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#create_application)
        """
    def create_deployment(
        self,
        *,
        applicationName: str,
        deploymentGroupName: str = None,
        revision: "RevisionLocationTypeDef" = None,
        deploymentConfigName: str = None,
        description: str = None,
        ignoreApplicationStopFailures: bool = None,
        targetInstances: "TargetInstancesTypeDef" = None,
        autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef" = None,
        updateOutdatedInstancesOnly: bool = None,
        fileExistsBehavior: FileExistsBehaviorType = None,
        overrideAlarmConfiguration: "AlarmConfigurationTypeDef" = None
    ) -> CreateDeploymentOutputTypeDef:
        """
        Deploys an application revision through the specified deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#create_deployment)
        """
    def create_deployment_config(
        self,
        *,
        deploymentConfigName: str,
        minimumHealthyHosts: "MinimumHealthyHostsTypeDef" = None,
        trafficRoutingConfig: "TrafficRoutingConfigTypeDef" = None,
        computePlatform: ComputePlatformType = None
    ) -> CreateDeploymentConfigOutputTypeDef:
        """
        Creates a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#create_deployment_config)
        """
    def create_deployment_group(
        self,
        *,
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
        outdatedInstancesStrategy: OutdatedInstancesStrategyType = None,
        deploymentStyle: "DeploymentStyleTypeDef" = None,
        blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
        loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
        ec2TagSet: "EC2TagSetTypeDef" = None,
        ecsServices: List["ECSServiceTypeDef"] = None,
        onPremisesTagSet: "OnPremisesTagSetTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDeploymentGroupOutputTypeDef:
        """
        Creates a deployment group to which application revisions are deployed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#create_deployment_group)
        """
    def delete_application(self, *, applicationName: str) -> None:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#delete_application)
        """
    def delete_deployment_config(self, *, deploymentConfigName: str) -> None:
        """
        Deletes a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#delete_deployment_config)
        """
    def delete_deployment_group(
        self, *, applicationName: str, deploymentGroupName: str
    ) -> DeleteDeploymentGroupOutputTypeDef:
        """
        Deletes a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#delete_deployment_group)
        """
    def delete_git_hub_account_token(
        self, *, tokenName: str = None
    ) -> DeleteGitHubAccountTokenOutputTypeDef:
        """
        Deletes a GitHub account connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.delete_git_hub_account_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#delete_git_hub_account_token)
        """
    def delete_resources_by_external_id(self, *, externalId: str = None) -> Dict[str, Any]:
        """
        Deletes resources linked to an external ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.delete_resources_by_external_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#delete_resources_by_external_id)
        """
    def deregister_on_premises_instance(self, *, instanceName: str) -> None:
        """
        Deregisters an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.deregister_on_premises_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#deregister_on_premises_instance)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#generate_presigned_url)
        """
    def get_application(self, *, applicationName: str) -> GetApplicationOutputTypeDef:
        """
        Gets information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_application)
        """
    def get_application_revision(
        self, *, applicationName: str, revision: "RevisionLocationTypeDef"
    ) -> GetApplicationRevisionOutputTypeDef:
        """
        Gets information about an application revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_application_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_application_revision)
        """
    def get_deployment(self, *, deploymentId: str) -> GetDeploymentOutputTypeDef:
        """
        Gets information about a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_deployment)
        """
    def get_deployment_config(
        self, *, deploymentConfigName: str
    ) -> GetDeploymentConfigOutputTypeDef:
        """
        Gets information about a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_deployment_config)
        """
    def get_deployment_group(
        self, *, applicationName: str, deploymentGroupName: str
    ) -> GetDeploymentGroupOutputTypeDef:
        """
        Gets information about a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_deployment_group)
        """
    def get_deployment_instance(
        self, *, deploymentId: str, instanceId: str
    ) -> GetDeploymentInstanceOutputTypeDef:
        """
        Gets information about an instance as part of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_deployment_instance)
        """
    def get_deployment_target(
        self, *, deploymentId: str = None, targetId: str = None
    ) -> GetDeploymentTargetOutputTypeDef:
        """
        Returns information about a deployment target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_deployment_target)
        """
    def get_on_premises_instance(self, *, instanceName: str) -> GetOnPremisesInstanceOutputTypeDef:
        """
        Gets information about an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.get_on_premises_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#get_on_premises_instance)
        """
    def list_application_revisions(
        self,
        *,
        applicationName: str,
        sortBy: ApplicationRevisionSortByType = None,
        sortOrder: SortOrderType = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: ListStateFilterActionType = None,
        nextToken: str = None
    ) -> ListApplicationRevisionsOutputTypeDef:
        """
        Lists information about revisions for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_application_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_application_revisions)
        """
    def list_applications(self, *, nextToken: str = None) -> ListApplicationsOutputTypeDef:
        """
        Lists the applications registered with the user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_applications)
        """
    def list_deployment_configs(
        self, *, nextToken: str = None
    ) -> ListDeploymentConfigsOutputTypeDef:
        """
        Lists the deployment configurations with the user or Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_deployment_configs)
        """
    def list_deployment_groups(
        self, *, applicationName: str, nextToken: str = None
    ) -> ListDeploymentGroupsOutputTypeDef:
        """
        Lists the deployment groups for an application registered with the Amazon Web
        Services user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_deployment_groups)
        """
    def list_deployment_instances(
        self,
        *,
        deploymentId: str,
        nextToken: str = None,
        instanceStatusFilter: List[InstanceStatusType] = None,
        instanceTypeFilter: List[InstanceTypeType] = None
    ) -> ListDeploymentInstancesOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_deployment_instances)
        """
    def list_deployment_targets(
        self,
        *,
        deploymentId: str = None,
        nextToken: str = None,
        targetFilters: Dict[TargetFilterNameType, List[str]] = None
    ) -> ListDeploymentTargetsOutputTypeDef:
        """
        Returns an array of target IDs that are associated a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_deployment_targets)
        """
    def list_deployments(
        self,
        *,
        applicationName: str = None,
        deploymentGroupName: str = None,
        externalId: str = None,
        includeOnlyStatuses: List[DeploymentStatusType] = None,
        createTimeRange: "TimeRangeTypeDef" = None,
        nextToken: str = None
    ) -> ListDeploymentsOutputTypeDef:
        """
        Lists the deployments in a deployment group for an application registered with
        the user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_deployments)
        """
    def list_git_hub_account_token_names(
        self, *, nextToken: str = None
    ) -> ListGitHubAccountTokenNamesOutputTypeDef:
        """
        Lists the names of stored connections to GitHub accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_git_hub_account_token_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_git_hub_account_token_names)
        """
    def list_on_premises_instances(
        self,
        *,
        registrationStatus: RegistrationStatusType = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        nextToken: str = None
    ) -> ListOnPremisesInstancesOutputTypeDef:
        """
        Gets a list of names for one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_on_premises_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_on_premises_instances)
        """
    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags for the resource identified by a specified Amazon
        Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#list_tags_for_resource)
        """
    def put_lifecycle_event_hook_execution_status(
        self,
        *,
        deploymentId: str = None,
        lifecycleEventHookExecutionId: str = None,
        status: LifecycleEventStatusType = None
    ) -> PutLifecycleEventHookExecutionStatusOutputTypeDef:
        """
        Sets the result of a Lambda validation function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.put_lifecycle_event_hook_execution_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#put_lifecycle_event_hook_execution_status)
        """
    def register_application_revision(
        self, *, applicationName: str, revision: "RevisionLocationTypeDef", description: str = None
    ) -> None:
        """
        Registers with CodeDeploy a revision for the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.register_application_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#register_application_revision)
        """
    def register_on_premises_instance(
        self, *, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None
    ) -> None:
        """
        Registers an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.register_on_premises_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#register_on_premises_instance)
        """
    def remove_tags_from_on_premises_instances(
        self, *, tags: List["TagTypeDef"], instanceNames: List[str]
    ) -> None:
        """
        Removes one or more tags from one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.remove_tags_from_on_premises_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#remove_tags_from_on_premises_instances)
        """
    def skip_wait_time_for_instance_termination(self, *, deploymentId: str = None) -> None:
        """
        In a blue/green deployment, overrides any specified wait time and starts
        terminating instances immediately after the traffic routing is complete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.skip_wait_time_for_instance_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#skip_wait_time_for_instance_termination)
        """
    def stop_deployment(
        self, *, deploymentId: str, autoRollbackEnabled: bool = None
    ) -> StopDeploymentOutputTypeDef:
        """
        Attempts to stop an ongoing deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.stop_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#stop_deployment)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates the list of tags in the input `Tags` parameter with the resource
        identified by the `ResourceArn` input parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Disassociates a resource from a list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#untag_resource)
        """
    def update_application(
        self, *, applicationName: str = None, newApplicationName: str = None
    ) -> None:
        """
        Changes the name of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#update_application)
        """
    def update_deployment_group(
        self,
        *,
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
        outdatedInstancesStrategy: OutdatedInstancesStrategyType = None,
        deploymentStyle: "DeploymentStyleTypeDef" = None,
        blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef" = None,
        loadBalancerInfo: "LoadBalancerInfoTypeDef" = None,
        ec2TagSet: "EC2TagSetTypeDef" = None,
        ecsServices: List["ECSServiceTypeDef"] = None,
        onPremisesTagSet: "OnPremisesTagSetTypeDef" = None
    ) -> UpdateDeploymentGroupOutputTypeDef:
        """
        Changes information about a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Client.update_deployment_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client.html#update_deployment_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_revisions"]
    ) -> ListApplicationRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listapplicationrevisionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_configs"]
    ) -> ListDeploymentConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listdeploymentconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_groups"]
    ) -> ListDeploymentGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listdeploymentgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_instances"]
    ) -> ListDeploymentInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listdeploymentinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_targets"]
    ) -> ListDeploymentTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listdeploymenttargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listdeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> ListGitHubAccountTokenNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listgithubaccounttokennamespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> ListOnPremisesInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators.html#listonpremisesinstancespaginator)
        """
    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> DeploymentSuccessfulWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/waiters.html#deploymentsuccessfulwaiter)
        """
