# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ecs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ecs import ECSClient

    client: ECSClient = boto3.client("ecs")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ecs.paginator import (
    ListAccountSettingsPaginator,
    ListAttributesPaginator,
    ListClustersPaginator,
    ListContainerInstancesPaginator,
    ListServicesPaginator,
    ListTaskDefinitionFamiliesPaginator,
    ListTaskDefinitionsPaginator,
    ListTasksPaginator,
)
from mypy_boto3_ecs.type_defs import (
    AttachmentStateChangeTypeDef,
    AttributeTypeDef,
    AutoScalingGroupProviderTypeDef,
    CapacityProviderStrategyItemTypeDef,
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
    UpdateClusterSettingsResponseTypeDef,
    UpdateContainerAgentResponseTypeDef,
    UpdateContainerInstancesStateResponseTypeDef,
    UpdateServicePrimaryTaskSetResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTaskSetResponseTypeDef,
    VersionInfoTypeDef,
    VolumeTypeDef,
)
from mypy_boto3_ecs.waiter import (
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
    TargetNotFoundException: Type[BotocoreClientError]
    TaskSetNotFoundException: Type[BotocoreClientError]
    UnsupportedFeatureException: Type[BotocoreClientError]
    UpdateInProgressException: Type[BotocoreClientError]


class ECSClient:
    """
    [ECS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.can_paginate)
        """

    def create_capacity_provider(
        self,
        name: str,
        autoScalingGroupProvider: "AutoScalingGroupProviderTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateCapacityProviderResponseTypeDef:
        """
        [Client.create_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.create_capacity_provider)
        """

    def create_cluster(
        self,
        clusterName: str = None,
        tags: List["TagTypeDef"] = None,
        settings: List["ClusterSettingTypeDef"] = None,
        capacityProviders: List[str] = None,
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.create_cluster)
        """

    def create_service(
        self,
        serviceName: str,
        cluster: str = None,
        taskDefinition: str = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        desiredCount: int = None,
        clientToken: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        role: str = None,
        deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        healthCheckGracePeriodSeconds: int = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
        deploymentController: "DeploymentControllerTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        enableECSManagedTags: bool = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
    ) -> CreateServiceResponseTypeDef:
        """
        [Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.create_service)
        """

    def create_task_set(
        self,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        scale: "ScaleTypeDef" = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateTaskSetResponseTypeDef:
        """
        [Client.create_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.create_task_set)
        """

    def delete_account_setting(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        principalArn: str = None,
    ) -> DeleteAccountSettingResponseTypeDef:
        """
        [Client.delete_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_account_setting)
        """

    def delete_attributes(
        self, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> DeleteAttributesResponseTypeDef:
        """
        [Client.delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_attributes)
        """

    def delete_capacity_provider(
        self, capacityProvider: str
    ) -> DeleteCapacityProviderResponseTypeDef:
        """
        [Client.delete_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_capacity_provider)
        """

    def delete_cluster(self, cluster: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_cluster)
        """

    def delete_service(
        self, service: str, cluster: str = None, force: bool = None
    ) -> DeleteServiceResponseTypeDef:
        """
        [Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_service)
        """

    def delete_task_set(
        self, cluster: str, service: str, taskSet: str, force: bool = None
    ) -> DeleteTaskSetResponseTypeDef:
        """
        [Client.delete_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.delete_task_set)
        """

    def deregister_container_instance(
        self, containerInstance: str, cluster: str = None, force: bool = None
    ) -> DeregisterContainerInstanceResponseTypeDef:
        """
        [Client.deregister_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.deregister_container_instance)
        """

    def deregister_task_definition(
        self, taskDefinition: str
    ) -> DeregisterTaskDefinitionResponseTypeDef:
        """
        [Client.deregister_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.deregister_task_definition)
        """

    def describe_capacity_providers(
        self,
        capacityProviders: List[str] = None,
        include: List[Literal["TAGS"]] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeCapacityProvidersResponseTypeDef:
        """
        [Client.describe_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_capacity_providers)
        """

    def describe_clusters(
        self,
        clusters: List[str] = None,
        include: List[Literal["ATTACHMENTS", "SETTINGS", "STATISTICS", "TAGS"]] = None,
    ) -> DescribeClustersResponseTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_clusters)
        """

    def describe_container_instances(
        self,
        containerInstances: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
    ) -> DescribeContainerInstancesResponseTypeDef:
        """
        [Client.describe_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_container_instances)
        """

    def describe_services(
        self, services: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_services)
        """

    def describe_task_definition(
        self, taskDefinition: str, include: List[Literal["TAGS"]] = None
    ) -> DescribeTaskDefinitionResponseTypeDef:
        """
        [Client.describe_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_task_definition)
        """

    def describe_task_sets(
        self,
        cluster: str,
        service: str,
        taskSets: List[str] = None,
        include: List[Literal["TAGS"]] = None,
    ) -> DescribeTaskSetsResponseTypeDef:
        """
        [Client.describe_task_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_task_sets)
        """

    def describe_tasks(
        self, tasks: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeTasksResponseTypeDef:
        """
        [Client.describe_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.describe_tasks)
        """

    def discover_poll_endpoint(
        self, containerInstance: str = None, cluster: str = None
    ) -> DiscoverPollEndpointResponseTypeDef:
        """
        [Client.discover_poll_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.discover_poll_endpoint)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.generate_presigned_url)
        """

    def list_account_settings(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ] = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAccountSettingsResponseTypeDef:
        """
        [Client.list_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_account_settings)
        """

    def list_attributes(
        self,
        targetType: Literal["container-instance"],
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAttributesResponseTypeDef:
        """
        [Client.list_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_attributes)
        """

    def list_clusters(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_clusters)
        """

    def list_container_instances(
        self,
        cluster: str = None,
        filter: str = None,
        nextToken: str = None,
        maxResults: int = None,
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ] = None,
    ) -> ListContainerInstancesResponseTypeDef:
        """
        [Client.list_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_container_instances)
        """

    def list_services(
        self,
        cluster: str = None,
        nextToken: str = None,
        maxResults: int = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
    ) -> ListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_services)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_tags_for_resource)
        """

    def list_task_definition_families(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE", "ALL"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTaskDefinitionFamiliesResponseTypeDef:
        """
        [Client.list_task_definition_families documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_task_definition_families)
        """

    def list_task_definitions(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        sort: Literal["ASC", "DESC"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTaskDefinitionsResponseTypeDef:
        """
        [Client.list_task_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_task_definitions)
        """

    def list_tasks(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        nextToken: str = None,
        maxResults: int = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: Literal["RUNNING", "PENDING", "STOPPED"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
    ) -> ListTasksResponseTypeDef:
        """
        [Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.list_tasks)
        """

    def put_account_setting(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        value: str,
        principalArn: str = None,
    ) -> PutAccountSettingResponseTypeDef:
        """
        [Client.put_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.put_account_setting)
        """

    def put_account_setting_default(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        value: str,
    ) -> PutAccountSettingDefaultResponseTypeDef:
        """
        [Client.put_account_setting_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.put_account_setting_default)
        """

    def put_attributes(
        self, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> PutAttributesResponseTypeDef:
        """
        [Client.put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.put_attributes)
        """

    def put_cluster_capacity_providers(
        self,
        cluster: str,
        capacityProviders: List[str],
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"],
    ) -> PutClusterCapacityProvidersResponseTypeDef:
        """
        [Client.put_cluster_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.put_cluster_capacity_providers)
        """

    def register_container_instance(
        self,
        cluster: str = None,
        instanceIdentityDocument: str = None,
        instanceIdentityDocumentSignature: str = None,
        totalResources: List["ResourceTypeDef"] = None,
        versionInfo: "VersionInfoTypeDef" = None,
        containerInstanceArn: str = None,
        attributes: List["AttributeTypeDef"] = None,
        platformDevices: List[PlatformDeviceTypeDef] = None,
        tags: List["TagTypeDef"] = None,
    ) -> RegisterContainerInstanceResponseTypeDef:
        """
        [Client.register_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.register_container_instance)
        """

    def register_task_definition(
        self,
        family: str,
        containerDefinitions: List["ContainerDefinitionTypeDef"],
        taskRoleArn: str = None,
        executionRoleArn: str = None,
        networkMode: Literal["bridge", "host", "awsvpc", "none"] = None,
        volumes: List["VolumeTypeDef"] = None,
        placementConstraints: List["TaskDefinitionPlacementConstraintTypeDef"] = None,
        requiresCompatibilities: List[Literal["EC2", "FARGATE"]] = None,
        cpu: str = None,
        memory: str = None,
        tags: List["TagTypeDef"] = None,
        pidMode: Literal["host", "task"] = None,
        ipcMode: Literal["host", "task", "none"] = None,
        proxyConfiguration: "ProxyConfigurationTypeDef" = None,
        inferenceAccelerators: List["InferenceAcceleratorTypeDef"] = None,
    ) -> RegisterTaskDefinitionResponseTypeDef:
        """
        [Client.register_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.register_task_definition)
        """

    def run_task(
        self,
        taskDefinition: str,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        cluster: str = None,
        count: int = None,
        enableECSManagedTags: bool = None,
        group: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        platformVersion: str = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> RunTaskResponseTypeDef:
        """
        [Client.run_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.run_task)
        """

    def start_task(
        self,
        containerInstances: List[str],
        taskDefinition: str,
        cluster: str = None,
        enableECSManagedTags: bool = None,
        group: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> StartTaskResponseTypeDef:
        """
        [Client.start_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.start_task)
        """

    def stop_task(
        self, task: str, cluster: str = None, reason: str = None
    ) -> StopTaskResponseTypeDef:
        """
        [Client.stop_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.stop_task)
        """

    def submit_attachment_state_changes(
        self, attachments: List[AttachmentStateChangeTypeDef], cluster: str = None
    ) -> SubmitAttachmentStateChangesResponseTypeDef:
        """
        [Client.submit_attachment_state_changes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.submit_attachment_state_changes)
        """

    def submit_container_state_change(
        self,
        cluster: str = None,
        task: str = None,
        containerName: str = None,
        runtimeId: str = None,
        status: str = None,
        exitCode: int = None,
        reason: str = None,
        networkBindings: List["NetworkBindingTypeDef"] = None,
    ) -> SubmitContainerStateChangeResponseTypeDef:
        """
        [Client.submit_container_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.submit_container_state_change)
        """

    def submit_task_state_change(
        self,
        cluster: str = None,
        task: str = None,
        status: str = None,
        reason: str = None,
        containers: List[ContainerStateChangeTypeDef] = None,
        attachments: List[AttachmentStateChangeTypeDef] = None,
        pullStartedAt: datetime = None,
        pullStoppedAt: datetime = None,
        executionStoppedAt: datetime = None,
    ) -> SubmitTaskStateChangeResponseTypeDef:
        """
        [Client.submit_task_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.submit_task_state_change)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.untag_resource)
        """

    def update_cluster_settings(
        self, cluster: str, settings: List["ClusterSettingTypeDef"]
    ) -> UpdateClusterSettingsResponseTypeDef:
        """
        [Client.update_cluster_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_cluster_settings)
        """

    def update_container_agent(
        self, containerInstance: str, cluster: str = None
    ) -> UpdateContainerAgentResponseTypeDef:
        """
        [Client.update_container_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_container_agent)
        """

    def update_container_instances_state(
        self,
        containerInstances: List[str],
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ],
        cluster: str = None,
    ) -> UpdateContainerInstancesStateResponseTypeDef:
        """
        [Client.update_container_instances_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_container_instances_state)
        """

    def update_service(
        self,
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
    ) -> UpdateServiceResponseTypeDef:
        """
        [Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_service)
        """

    def update_service_primary_task_set(
        self, cluster: str, service: str, primaryTaskSet: str
    ) -> UpdateServicePrimaryTaskSetResponseTypeDef:
        """
        [Client.update_service_primary_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_service_primary_task_set)
        """

    def update_task_set(
        self, cluster: str, service: str, taskSet: str, scale: "ScaleTypeDef"
    ) -> UpdateTaskSetResponseTypeDef:
        """
        [Client.update_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Client.update_task_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_settings"]
    ) -> ListAccountSettingsPaginator:
        """
        [Paginator.ListAccountSettings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_attributes"]) -> ListAttributesPaginator:
        """
        [Paginator.ListAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAttributes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_container_instances"]
    ) -> ListContainerInstancesPaginator:
        """
        [Paginator.ListContainerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListServices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definition_families"]
    ) -> ListTaskDefinitionFamiliesPaginator:
        """
        [Paginator.ListTaskDefinitionFamilies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definitions"]
    ) -> ListTaskDefinitionsPaginator:
        """
        [Paginator.ListTaskDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTasks)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["services_inactive"]) -> ServicesInactiveWaiter:
        """
        [Waiter.ServicesInactive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Waiter.ServicesInactive)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["services_stable"]) -> ServicesStableWaiter:
        """
        [Waiter.ServicesStable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Waiter.ServicesStable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["tasks_running"]) -> TasksRunningWaiter:
        """
        [Waiter.TasksRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Waiter.TasksRunning)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["tasks_stopped"]) -> TasksStoppedWaiter:
        """
        [Waiter.TasksStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Waiter.TasksStopped)
        """
