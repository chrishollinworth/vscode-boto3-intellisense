"""
Type annotations for opsworks service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_opsworks.service_resource import OpsWorksServiceResource
    import mypy_boto3_opsworks.service_resource as opsworks_resources

    session = Session()
    resource: OpsWorksServiceResource = session.resource("opsworks")

    my_layer: opsworks_resources.Layer = resource.Layer(...)
    my_stack: opsworks_resources.Stack = resource.Stack(...)
    my_stack_summary: opsworks_resources.StackSummary = resource.StackSummary(...)
```
"""

from __future__ import annotations

import sys

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import OpsWorksClient
from .literals import LayerAttributesKeysType, LayerTypeType, RootDeviceTypeType
from .type_defs import (
    ChefConfigurationTypeDef,
    CloudWatchLogsConfigurationOutputTypeDef,
    CreateLayerRequestStackCreateLayerTypeDef,
    CreateStackRequestServiceResourceCreateStackTypeDef,
    InstancesCountTypeDef,
    LifecycleEventConfigurationTypeDef,
    RecipesOutputTypeDef,
    SourceTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Dict, Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = (
    "Layer",
    "OpsWorksServiceResource",
    "ServiceResourceStacksCollection",
    "Stack",
    "StackLayersCollection",
    "StackSummary",
)

class ServiceResourceStacksCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#OpsWorks.ServiceResource.stacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
    """
    def all(self) -> ServiceResourceStacksCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#OpsWorks.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def filter(  # type: ignore[override]
        self, *, StackIds: Sequence[str] = ...
    ) -> ServiceResourceStacksCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def limit(self, count: int) -> ServiceResourceStacksCollection:
        """
        Return at most this many Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def page_size(self, count: int) -> ServiceResourceStacksCollection:
        """
        Fetch at most this many Stacks per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def pages(self) -> Iterator[List[Stack]]:
        """
        A generator which yields pages of Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def __iter__(self) -> Iterator[Stack]:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/stacks.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#serviceresourcestackscollection)
        """

class StackLayersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#OpsWorks.Stack.layers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
    """
    def all(self) -> StackLayersCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#OpsWorks.Stack.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

    def filter(  # type: ignore[override]
        self, *, StackId: str = ..., LayerIds: Sequence[str] = ...
    ) -> StackLayersCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

    def limit(self, count: int) -> StackLayersCollection:
        """
        Return at most this many Layers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

    def page_size(self, count: int) -> StackLayersCollection:
        """
        Fetch at most this many Layers per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

    def pages(self) -> Iterator[List[Layer]]:
        """
        A generator which yields pages of Layers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

    def __iter__(self) -> Iterator[Layer]:
        """
        A generator which yields Layers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/layers.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacklayers)
        """

class Layer(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/layer/index.html#OpsWorks.Layer)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#layer)
    """

    id: str
    stack: Stack
    arn: str
    stack_id: str
    layer_id: str
    type: LayerTypeType
    name: str
    shortname: str
    attributes: Dict[LayerAttributesKeysType, str]
    cloud_watch_logs_configuration: CloudWatchLogsConfigurationOutputTypeDef
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List[str]
    default_security_group_names: List[str]
    packages: List[str]
    volume_configurations: List[VolumeConfigurationTypeDef]
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: RecipesOutputTypeDef
    custom_recipes: RecipesOutputTypeDef
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: LifecycleEventConfigurationTypeDef
    meta: OpsWorksResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/layer/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#layerget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes a specified layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/layer/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#layerdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/layer/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#layerload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/layer/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#layerreload-method)
        """

_Layer = Layer

class Stack(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/index.html#OpsWorks.Stack)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stack)
    """

    id: str
    layers: StackLayersCollection
    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict[Literal["Color"], str]
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: StackConfigurationManagerTypeDef
    chef_configuration: ChefConfigurationTypeDef
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: SourceTypeDef
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: RootDeviceTypeType
    agent_version: str
    meta: OpsWorksResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stackget_available_subresources-method)
        """

    def create_layer(self, **kwargs: Unpack[CreateLayerRequestStackCreateLayerTypeDef]) -> _Layer:
        """
        Creates a layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/create_layer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stackcreate_layer-method)
        """

    def delete(self) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stackdelete-method)
        """

    def Summary(self) -> _StackSummary:
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/Summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummary-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stackload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stack/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stackreload-method)
        """

_Stack = Stack

class StackSummary(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stacksummary/index.html#OpsWorks.StackSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummary)
    """

    stack_id: str
    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: InstancesCountTypeDef
    meta: OpsWorksResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this StackSummary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stacksummary/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummaryget_available_subresources-method)
        """

    def Stack(self) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stacksummary/Stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummarystack-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stacksummary/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummaryload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/stacksummary/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#stacksummaryreload-method)
        """

_StackSummary = StackSummary

class OpsWorksResourceMeta(ResourceMeta):
    client: OpsWorksClient  # type: ignore[override]

class OpsWorksServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/)
    """

    meta: OpsWorksResourceMeta  # type: ignore[override]
    stacks: ServiceResourceStacksCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#opsworksserviceresourceget_available_subresources-method)
        """

    def create_stack(
        self, **kwargs: Unpack[CreateStackRequestServiceResourceCreateStackTypeDef]
    ) -> _Stack:
        """
        Creates a new stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/create_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#opsworksserviceresourcecreate_stack-method)
        """

    def Layer(self, id: str) -> _Layer:
        """
        Creates a Layer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/Layer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#opsworksserviceresourcelayer-method)
        """

    def Stack(self, id: str) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/Stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#opsworksserviceresourcestack-method)
        """

    def StackSummary(self, stack_id: str) -> _StackSummary:
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/service-resource/StackSummary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/service_resource/#opsworksserviceresourcestacksummary-method)
        """
