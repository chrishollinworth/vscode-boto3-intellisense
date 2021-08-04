"""
Type annotations for ecs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ecs import ECSClient

    client: ECSClient = boto3.client("ecs")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ClusterFieldType,
    CompatibilityType,
    ContainerInstanceStatusType,
    DesiredStatusType,
    IpcModeType,
    LaunchTypeType,
    NetworkModeType,
    PidModeType,
    PropagateTagsType,
    SchedulingStrategyType,
    SettingNameType,
    SortOrderType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
)
from .paginator import (
    ListAccountSettingsPaginator,
    ListAttributesPaginator,
    ListClustersPaginator,
    ListContainerInstancesPaginator,
    ListServicesPaginator,
    ListTaskDefinitionFamiliesPaginator,
    ListTaskDefinitionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    AttachmentStateChangeTypeDef,
    AttributeTypeDef,
    AutoScalingGroupProviderTypeDef,
    AutoScalingGroupProviderUpdateTypeDef,
    CapacityProviderStrategyItemTypeDef,
    ClusterConfigurationTypeDef,
    ClusterSettingTypeDef,
    ContainerDefinitionTypeDef,
    ContainerStateChangeTypeDef,
    CreateCapacityProviderResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateTaskSetResponseTypeDef,
    DeleteAccountSettingResponseTypeDef,
    DeleteAttributesResponseTypeDef,
    DeleteCapacityProviderResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTaskSetResponseTypeDef,
    DeploymentConfigurationTypeDef,
    DeploymentControllerTypeDef,
    DeregisterContainerInstanceResponseTypeDef,
    DeregisterTaskDefinitionResponseTypeDef,
    DescribeCapacityProvidersResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeContainerInstancesResponseTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeTaskDefinitionResponseTypeDef,
    DescribeTaskSetsResponseTypeDef,
    DescribeTasksResponseTypeDef,
    DiscoverPollEndpointResponseTypeDef,
    EphemeralStorageTypeDef,
    ExecuteCommandResponseTypeDef,
    InferenceAcceleratorTypeDef,
    ListAccountSettingsResponseTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LoadBalancerTypeDef,
    ManagedAgentStateChangeTypeDef,
    NetworkBindingTypeDef,
    NetworkConfigurationTypeDef,
    PlacementConstraintTypeDef,
    PlacementStrategyTypeDef,
    PlatformDeviceTypeDef,
    ProxyConfigurationTypeDef,
    PutAccountSettingDefaultResponseTypeDef,
    PutAccountSettingResponseTypeDef,
    PutAttributesResponseTypeDef,
    PutClusterCapacityProvidersResponseTypeDef,
    RegisterContainerInstanceResponseTypeDef,
    RegisterTaskDefinitionResponseTypeDef,
    ResourceTypeDef,
    RunTaskResponseTypeDef,
    ScaleTypeDef,
    ServiceRegistryTypeDef,
    StartTaskResponseTypeDef,
    StopTaskResponseTypeDef,
    SubmitAttachmentStateChangesResponseTypeDef,
    SubmitContainerStateChangeResponseTypeDef,
    SubmitTaskStateChangeResponseTypeDef,
    TagTypeDef,
    TaskDefinitionPlacementConstraintTypeDef,
    TaskOverrideTypeDef,
    UpdateCapacityProviderResponseTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateClusterSettingsResponseTypeDef,
    UpdateContainerAgentResponseTypeDef,
    UpdateContainerInstancesStateResponseTypeDef,
    UpdateServicePrimaryTaskSetResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTaskSetResponseTypeDef,
    VersionInfoTypeDef,
    VolumeTypeDef,
)
from .waiter import (
    ServicesInactiveWaiter,
    ServicesStableWaiter,
    TasksRunningWaiter,
    TasksStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ECSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AttributeLimitExceededException: Type[BotocoreClientError]
    BlockedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ClusterContainsContainerInstancesException: Type[BotocoreClientError]
    ClusterContainsServicesException: Type[BotocoreClientError]
    ClusterContainsTasksException: Type[BotocoreClientError]
    ClusterNotFoundException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingVersionException: Type[BotocoreClientError]
    NoUpdateAvailableException: Type[BotocoreClientError]
    PlatformTaskDefinitionIncompatibilityException: Type[BotocoreClientError]
    PlatformUnknownException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceNotActiveException: Type[BotocoreClientError]
    ServiceNotFoundException: Type[BotocoreClientError]
    TargetNotConnectedException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TaskSetNotFoundException: Type[BotocoreClientError]
    UnsupportedFeatureException: Type[BotocoreClientError]
    UpdateInProgressException: Type[BotocoreClientError]

class ECSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        ECSClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#can_paginate)
        """
    def create_capacity_provider(
        self,
        *,
        name: str,
        autoScalingGroupProvider: "AutoScalingGroupProviderTypeDef",
        tags: List["TagTypeDef"] = None
    ) -> CreateCapacityProviderResponseTypeDef:
        """
        Creates a new capacity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.create_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create_capacity_provider)
        """
    def create_cluster(
        self,
        *,
        clusterName: str = None,
        tags: List["TagTypeDef"] = None,
        settings: List["ClusterSettingTypeDef"] = None,
        configuration: "ClusterConfigurationTypeDef" = None,
        capacityProviders: List[str] = None,
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a new Amazon ECS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create_cluster)
        """
    def create_service(
        self,
        *,
        serviceName: str,
        cluster: str = None,
        taskDefinition: str = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        desiredCount: int = None,
        clientToken: str = None,
        launchType: LaunchTypeType = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        role: str = None,
        deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        healthCheckGracePeriodSeconds: int = None,
        schedulingStrategy: SchedulingStrategyType = None,
        deploymentController: "DeploymentControllerTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        enableECSManagedTags: bool = None,
        propagateTags: PropagateTagsType = None,
        enableExecuteCommand: bool = None
    ) -> CreateServiceResponseTypeDef:
        """
        Runs and maintains a desired number of tasks from a specified task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create_service)
        """
    def create_task_set(
        self,
        *,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        launchType: LaunchTypeType = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        scale: "ScaleTypeDef" = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateTaskSetResponseTypeDef:
        """
        Create a task set in the specified cluster and service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.create_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create_task_set)
        """
    def delete_account_setting(
        self, *, name: SettingNameType, principalArn: str = None
    ) -> DeleteAccountSettingResponseTypeDef:
        """
        Disables an account setting for a specified IAM user, IAM role, or the root user
        for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_account_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_account_setting)
        """
    def delete_attributes(
        self, *, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> DeleteAttributesResponseTypeDef:
        """
        Deletes one or more custom attributes from an Amazon ECS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_attributes)
        """
    def delete_capacity_provider(
        self, *, capacityProvider: str
    ) -> DeleteCapacityProviderResponseTypeDef:
        """
        Deletes the specified capacity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_capacity_provider)
        """
    def delete_cluster(self, *, cluster: str) -> DeleteClusterResponseTypeDef:
        """
        Deletes the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_cluster)
        """
    def delete_service(
        self, *, service: str, cluster: str = None, force: bool = None
    ) -> DeleteServiceResponseTypeDef:
        """
        Deletes a specified service within a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_service)
        """
    def delete_task_set(
        self, *, cluster: str, service: str, taskSet: str, force: bool = None
    ) -> DeleteTaskSetResponseTypeDef:
        """
        Deletes a specified task set within a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.delete_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete_task_set)
        """
    def deregister_container_instance(
        self, *, containerInstance: str, cluster: str = None, force: bool = None
    ) -> DeregisterContainerInstanceResponseTypeDef:
        """
        Deregisters an Amazon ECS container instance from the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.deregister_container_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#deregister_container_instance)
        """
    def deregister_task_definition(
        self, *, taskDefinition: str
    ) -> DeregisterTaskDefinitionResponseTypeDef:
        """
        Deregisters the specified task definition by family and revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.deregister_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#deregister_task_definition)
        """
    def describe_capacity_providers(
        self,
        *,
        capacityProviders: List[str] = None,
        include: List[Literal["TAGS"]] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeCapacityProvidersResponseTypeDef:
        """
        Describes one or more of your capacity providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_capacity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_capacity_providers)
        """
    def describe_clusters(
        self, *, clusters: List[str] = None, include: List[ClusterFieldType] = None
    ) -> DescribeClustersResponseTypeDef:
        """
        Describes one or more of your clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_clusters)
        """
    def describe_container_instances(
        self,
        *,
        containerInstances: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None
    ) -> DescribeContainerInstancesResponseTypeDef:
        """
        Describes one or more container instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_container_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_container_instances)
        """
    def describe_services(
        self, *, services: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeServicesResponseTypeDef:
        """
        Describes the specified services running in your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_services)
        """
    def describe_task_definition(
        self, *, taskDefinition: str, include: List[Literal["TAGS"]] = None
    ) -> DescribeTaskDefinitionResponseTypeDef:
        """
        Describes a task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_task_definition)
        """
    def describe_task_sets(
        self,
        *,
        cluster: str,
        service: str,
        taskSets: List[str] = None,
        include: List[Literal["TAGS"]] = None
    ) -> DescribeTaskSetsResponseTypeDef:
        """
        Describes the task sets in the specified cluster and service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_task_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_task_sets)
        """
    def describe_tasks(
        self, *, tasks: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeTasksResponseTypeDef:
        """
        Describes a specified task or tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.describe_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe_tasks)
        """
    def discover_poll_endpoint(
        self, *, containerInstance: str = None, cluster: str = None
    ) -> DiscoverPollEndpointResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.discover_poll_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#discover_poll_endpoint)
        """
    def execute_command(
        self,
        *,
        command: str,
        interactive: bool,
        task: str,
        cluster: str = None,
        container: str = None
    ) -> ExecuteCommandResponseTypeDef:
        """
        Runs a command remotely on a container within a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.execute_command)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#execute_command)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#generate_presigned_url)
        """
    def list_account_settings(
        self,
        *,
        name: SettingNameType = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAccountSettingsResponseTypeDef:
        """
        Lists the account settings for a specified principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_account_settings)
        """
    def list_attributes(
        self,
        *,
        targetType: Literal["container-instance"],
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAttributesResponseTypeDef:
        """
        Lists the attributes for Amazon ECS resources within a specified target type and
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_attributes)
        """
    def list_clusters(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListClustersResponseTypeDef:
        """
        Returns a list of existing clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_clusters)
        """
    def list_container_instances(
        self,
        *,
        cluster: str = None,
        filter: str = None,
        nextToken: str = None,
        maxResults: int = None,
        status: ContainerInstanceStatusType = None
    ) -> ListContainerInstancesResponseTypeDef:
        """
        Returns a list of container instances in a specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_container_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_container_instances)
        """
    def list_services(
        self,
        *,
        cluster: str = None,
        nextToken: str = None,
        maxResults: int = None,
        launchType: LaunchTypeType = None,
        schedulingStrategy: SchedulingStrategyType = None
    ) -> ListServicesResponseTypeDef:
        """
        Returns a list of services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_services)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon ECS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_tags_for_resource)
        """
    def list_task_definition_families(
        self,
        *,
        familyPrefix: str = None,
        status: TaskDefinitionFamilyStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTaskDefinitionFamiliesResponseTypeDef:
        """
        Returns a list of task definition families that are registered to your account
        (which may include task definition families that no longer have any `ACTIVE`
        task definition revisions).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_task_definition_families)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_task_definition_families)
        """
    def list_task_definitions(
        self,
        *,
        familyPrefix: str = None,
        status: TaskDefinitionStatusType = None,
        sort: SortOrderType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTaskDefinitionsResponseTypeDef:
        """
        Returns a list of task definitions that are registered to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_task_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_task_definitions)
        """
    def list_tasks(
        self,
        *,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        nextToken: str = None,
        maxResults: int = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: DesiredStatusType = None,
        launchType: LaunchTypeType = None
    ) -> ListTasksResponseTypeDef:
        """
        Returns a list of tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list_tasks)
        """
    def put_account_setting(
        self, *, name: SettingNameType, value: str, principalArn: str = None
    ) -> PutAccountSettingResponseTypeDef:
        """
        Modifies an account setting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.put_account_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put_account_setting)
        """
    def put_account_setting_default(
        self, *, name: SettingNameType, value: str
    ) -> PutAccountSettingDefaultResponseTypeDef:
        """
        Modifies an account setting for all IAM users on an account for whom no
        individual account setting has been specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.put_account_setting_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put_account_setting_default)
        """
    def put_attributes(
        self, *, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> PutAttributesResponseTypeDef:
        """
        Create or update an attribute on an Amazon ECS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.put_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put_attributes)
        """
    def put_cluster_capacity_providers(
        self,
        *,
        cluster: str,
        capacityProviders: List[str],
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"]
    ) -> PutClusterCapacityProvidersResponseTypeDef:
        """
        Modifies the available capacity providers and the default capacity provider
        strategy for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.put_cluster_capacity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put_cluster_capacity_providers)
        """
    def register_container_instance(
        self,
        *,
        cluster: str = None,
        instanceIdentityDocument: str = None,
        instanceIdentityDocumentSignature: str = None,
        totalResources: List["ResourceTypeDef"] = None,
        versionInfo: "VersionInfoTypeDef" = None,
        containerInstanceArn: str = None,
        attributes: List["AttributeTypeDef"] = None,
        platformDevices: List["PlatformDeviceTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> RegisterContainerInstanceResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.register_container_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#register_container_instance)
        """
    def register_task_definition(
        self,
        *,
        family: str,
        containerDefinitions: List["ContainerDefinitionTypeDef"],
        taskRoleArn: str = None,
        executionRoleArn: str = None,
        networkMode: NetworkModeType = None,
        volumes: List["VolumeTypeDef"] = None,
        placementConstraints: List["TaskDefinitionPlacementConstraintTypeDef"] = None,
        requiresCompatibilities: List[CompatibilityType] = None,
        cpu: str = None,
        memory: str = None,
        tags: List["TagTypeDef"] = None,
        pidMode: PidModeType = None,
        ipcMode: IpcModeType = None,
        proxyConfiguration: "ProxyConfigurationTypeDef" = None,
        inferenceAccelerators: List["InferenceAcceleratorTypeDef"] = None,
        ephemeralStorage: "EphemeralStorageTypeDef" = None
    ) -> RegisterTaskDefinitionResponseTypeDef:
        """
        Registers a new task definition from the supplied `family` and
        `containerDefinitions`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.register_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#register_task_definition)
        """
    def run_task(
        self,
        *,
        taskDefinition: str,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        cluster: str = None,
        count: int = None,
        enableECSManagedTags: bool = None,
        enableExecuteCommand: bool = None,
        group: str = None,
        launchType: LaunchTypeType = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        platformVersion: str = None,
        propagateTags: PropagateTagsType = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None
    ) -> RunTaskResponseTypeDef:
        """
        Starts a new task using the specified task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.run_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#run_task)
        """
    def start_task(
        self,
        *,
        containerInstances: List[str],
        taskDefinition: str,
        cluster: str = None,
        enableECSManagedTags: bool = None,
        enableExecuteCommand: bool = None,
        group: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        propagateTags: PropagateTagsType = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None
    ) -> StartTaskResponseTypeDef:
        """
        Starts a new task from the specified task definition on the specified container
        instance or instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.start_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#start_task)
        """
    def stop_task(
        self, *, task: str, cluster: str = None, reason: str = None
    ) -> StopTaskResponseTypeDef:
        """
        Stops a running task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.stop_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#stop_task)
        """
    def submit_attachment_state_changes(
        self, *, attachments: List["AttachmentStateChangeTypeDef"], cluster: str = None
    ) -> SubmitAttachmentStateChangesResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.submit_attachment_state_changes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit_attachment_state_changes)
        """
    def submit_container_state_change(
        self,
        *,
        cluster: str = None,
        task: str = None,
        containerName: str = None,
        runtimeId: str = None,
        status: str = None,
        exitCode: int = None,
        reason: str = None,
        networkBindings: List["NetworkBindingTypeDef"] = None
    ) -> SubmitContainerStateChangeResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.submit_container_state_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit_container_state_change)
        """
    def submit_task_state_change(
        self,
        *,
        cluster: str = None,
        task: str = None,
        status: str = None,
        reason: str = None,
        containers: List["ContainerStateChangeTypeDef"] = None,
        attachments: List["AttachmentStateChangeTypeDef"] = None,
        managedAgents: List["ManagedAgentStateChangeTypeDef"] = None,
        pullStartedAt: Union[datetime, str] = None,
        pullStoppedAt: Union[datetime, str] = None,
        executionStoppedAt: Union[datetime, str] = None
    ) -> SubmitTaskStateChangeResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.submit_task_state_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit_task_state_change)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#untag_resource)
        """
    def update_capacity_provider(
        self, *, name: str, autoScalingGroupProvider: "AutoScalingGroupProviderUpdateTypeDef"
    ) -> UpdateCapacityProviderResponseTypeDef:
        """
        Modifies the parameters for a capacity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_capacity_provider)
        """
    def update_cluster(
        self,
        *,
        cluster: str,
        settings: List["ClusterSettingTypeDef"] = None,
        configuration: "ClusterConfigurationTypeDef" = None
    ) -> UpdateClusterResponseTypeDef:
        """
        Updates the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_cluster)
        """
    def update_cluster_settings(
        self, *, cluster: str, settings: List["ClusterSettingTypeDef"]
    ) -> UpdateClusterSettingsResponseTypeDef:
        """
        Modifies the settings to use for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_cluster_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_cluster_settings)
        """
    def update_container_agent(
        self, *, containerInstance: str, cluster: str = None
    ) -> UpdateContainerAgentResponseTypeDef:
        """
        Updates the Amazon ECS container agent on a specified container instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_container_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_container_agent)
        """
    def update_container_instances_state(
        self,
        *,
        containerInstances: List[str],
        status: ContainerInstanceStatusType,
        cluster: str = None
    ) -> UpdateContainerInstancesStateResponseTypeDef:
        """
        Modifies the status of an Amazon ECS container instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_container_instances_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_container_instances_state)
        """
    def update_service(
        self,
        *,
        service: str,
        cluster: str = None,
        desiredCount: int = None,
        taskDefinition: str = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        platformVersion: str = None,
        forceNewDeployment: bool = None,
        healthCheckGracePeriodSeconds: int = None,
        enableExecuteCommand: bool = None
    ) -> UpdateServiceResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_service)
        """
    def update_service_primary_task_set(
        self, *, cluster: str, service: str, primaryTaskSet: str
    ) -> UpdateServicePrimaryTaskSetResponseTypeDef:
        """
        Modifies which task set in a service is the primary task set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_service_primary_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_service_primary_task_set)
        """
    def update_task_set(
        self, *, cluster: str, service: str, taskSet: str, scale: "ScaleTypeDef"
    ) -> UpdateTaskSetResponseTypeDef:
        """
        Modifies a task set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Client.update_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update_task_set)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_settings"]
    ) -> ListAccountSettingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listaccountsettingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_attributes"]) -> ListAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listattributespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_container_instances"]
    ) -> ListContainerInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listcontainerinstancespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definition_families"]
    ) -> ListTaskDefinitionFamiliesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskdefinitionfamiliespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definitions"]
    ) -> ListTaskDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskdefinitionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Paginator.ListTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["services_inactive"]) -> ServicesInactiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Waiter.ServicesInactive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesinactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["services_stable"]) -> ServicesStableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Waiter.ServicesStable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesstablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["tasks_running"]) -> TasksRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Waiter.TasksRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksrunningwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["tasks_stopped"]) -> TasksStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/ecs.html#ECS.Waiter.TasksStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksstoppedwaiter)
        """
