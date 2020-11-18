# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for opsworks service ServiceResource

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworks import OpsWorksServiceResource
    import mypy_boto3_opsworks.service_resource as opsworks_resources

    resource: OpsWorksServiceResource = boto3.resource("opsworks")

    my_layer: opsworks_resources.Layer = resource.Layer(...)
    my_stack: opsworks_resources.Stack = resource.Stack(...)
    my_stack_summary: opsworks_resources.StackSummary = resource.StackSummary(...)
```
"""
import sys
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_opsworks.type_defs import (
    ChefConfigurationTypeDef,
    CloudWatchLogsConfigurationTypeDef,
    LifecycleEventConfigurationTypeDef,
    RecipesTypeDef,
    SourceTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "OpsWorksServiceResource",
    "Layer",
    "Stack",
    "StackSummary",
    "ServiceResourceStacksCollection",
    "StackLayersCollection",
)


class ServiceResourceStacksCollection(ResourceCollection):
    """
    [ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
    """

    def all(self) -> "ServiceResourceStacksCollection":
        pass

    def filter(  # type: ignore
        self, StackIds: List[str] = None
    ) -> "ServiceResourceStacksCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceStacksCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceStacksCollection":
        pass

    def pages(self) -> Iterator[List["Stack"]]:
        pass

    def __iter__(self) -> Iterator["Stack"]:
        pass


class StackLayersCollection(ResourceCollection):
    """
    [Stack.layers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.layers)
    """

    def all(self) -> "StackLayersCollection":
        pass

    def filter(  # type: ignore
        self, StackId: str = None, LayerIds: List[str] = None
    ) -> "StackLayersCollection":
        pass

    def limit(self, count: int) -> "StackLayersCollection":
        pass

    def page_size(self, count: int) -> "StackLayersCollection":
        pass

    def pages(self) -> Iterator[List["Layer"]]:
        pass

    def __iter__(self) -> Iterator["Layer"]:
        pass


class Layer(Boto3ServiceResource):
    """
    [Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
    """

    arn: str
    stack_id: str
    layer_id: str
    type: str
    name: str
    shortname: str
    attributes: Dict[str, Any]
    cloud_watch_logs_configuration: Dict[str, Any]
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List[Any]
    default_security_group_names: List[Any]
    packages: List[Any]
    volume_configurations: List[Any]
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: Dict[str, Any]
    custom_recipes: Dict[str, Any]
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: Dict[str, Any]
    id: str
    stack: "Stack"

    def delete(self) -> None:
        """
        [Layer.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Layer.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Layer.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Layer.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Layer.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Layer.load)
        """

    def reload(self) -> None:
        """
        [Layer.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Layer.reload)
        """


_Layer = Layer


class StackSummary(Boto3ServiceResource):
    """
    [StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
    """

    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: Dict[str, Any]
    stack_id: str

    def Stack(self) -> "_Stack":
        """
        [StackSummary.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.StackSummary.Stack)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [StackSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.StackSummary.get_available_subresources)
        """

    def load(self) -> None:
        """
        [StackSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.StackSummary.load)
        """

    def reload(self) -> None:
        """
        [StackSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.StackSummary.reload)
        """


_StackSummary = StackSummary


class Stack(Boto3ServiceResource):
    """
    [Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
    """

    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict[str, Any]
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: Dict[str, Any]
    chef_configuration: Dict[str, Any]
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: Dict[str, Any]
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: str
    agent_version: str
    id: str
    layers: StackLayersCollection

    def Summary(self) -> _StackSummary:
        """
        [Stack.Summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.Summary)
        """

    def create_layer(
        self,
        Type: Literal[
            "aws-flow-ruby",
            "ecs-cluster",
            "java-app",
            "lb",
            "web",
            "php-app",
            "rails-app",
            "nodejs-app",
            "memcached",
            "db-master",
            "monitoring-master",
            "custom",
        ],
        Name: str,
        Shortname: str,
        Attributes: Dict[
            Literal[
                "EcsClusterArn",
                "EnableHaproxyStats",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "HaproxyStatsPassword",
                "HaproxyHealthCheckUrl",
                "HaproxyHealthCheckMethod",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "GangliaUrl",
                "GangliaUser",
                "GangliaPassword",
                "MemcachedMemory",
                "NodejsVersion",
                "RubyVersion",
                "RubygemsVersion",
                "ManageBundler",
                "BundlerVersion",
                "RailsStack",
                "PassengerVersion",
                "Jvm",
                "JvmVersion",
                "JvmOptions",
                "JavaAppServer",
                "JavaAppServerVersion",
            ],
            str,
        ] = None,
        CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List["VolumeConfigurationTypeDef"] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: "RecipesTypeDef" = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = None,
    ) -> _Layer:
        """
        [Stack.create_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.create_layer)
        """

    def delete(self) -> None:
        """
        [Stack.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Stack.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Stack.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.load)
        """

    def reload(self) -> None:
        """
        [Stack.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Stack.reload)
        """


_Stack = Stack


class OpsWorksServiceResource(Boto3ServiceResource):
    """
    [OpsWorks.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource)
    """

    stacks: ServiceResourceStacksCollection

    def Layer(self, id: str) -> _Layer:
        """
        [ServiceResource.Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
        """

    def Stack(self, id: str) -> _Stack:
        """
        [ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
        """

    def StackSummary(self, stack_id: str) -> _StackSummary:
        """
        [ServiceResource.StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
        """

    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = None,
        Attributes: Dict[Literal["Color"], str] = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
        ChefConfiguration: "ChefConfigurationTypeDef" = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: "SourceTypeDef" = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: Literal["ebs", "instance-store"] = None,
        AgentVersion: str = None,
    ) -> _Stack:
        """
        [ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.create_stack)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.ServiceResource.get_available_subresources)
        """
