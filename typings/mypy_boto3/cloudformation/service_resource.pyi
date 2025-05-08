"""
Type annotations for cloudformation service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudformation.service_resource import CloudFormationServiceResource
    import mypy_boto3_cloudformation.service_resource as cloudformation_resources

    session = Session()
    resource: CloudFormationServiceResource = session.resource("cloudformation")

    my_event: cloudformation_resources.Event = resource.Event(...)
    my_stack: cloudformation_resources.Stack = resource.Stack(...)
    my_stack_resource: cloudformation_resources.StackResource = resource.StackResource(...)
    my_stack_resource_summary: cloudformation_resources.StackResourceSummary = resource.StackResourceSummary(...)
```
"""

from __future__ import annotations

import sys
from datetime import datetime

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import CloudFormationClient
from .literals import (
    CapabilityType,
    DeletionModeType,
    DetailedStatusType,
    HookFailureModeType,
    HookStatusType,
    ResourceStatusType,
    StackStatusType,
)
from .type_defs import (
    CancelUpdateStackInputStackCancelUpdateTypeDef,
    CreateStackInputServiceResourceCreateStackTypeDef,
    DeleteStackInputStackDeleteTypeDef,
    ModuleInfoTypeDef,
    OutputTypeDef,
    ParameterTypeDef,
    RollbackConfigurationOutputTypeDef,
    StackDriftInformationTypeDef,
    StackResourceDriftInformationSummaryTypeDef,
    StackResourceDriftInformationTypeDef,
    TagTypeDef,
    UpdateStackInputStackUpdateTypeDef,
    UpdateStackOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = (
    "CloudFormationServiceResource",
    "Event",
    "ServiceResourceStacksCollection",
    "Stack",
    "StackEventsCollection",
    "StackResource",
    "StackResourceSummariesCollection",
    "StackResourceSummary",
)

class ServiceResourceStacksCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#CloudFormation.ServiceResource.stacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
    """
    def all(self) -> ServiceResourceStacksCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#CloudFormation.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def filter(  # type: ignore[override]
        self, *, StackName: str = ..., NextToken: str = ...
    ) -> ServiceResourceStacksCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def limit(self, count: int) -> ServiceResourceStacksCollection:
        """
        Return at most this many Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def page_size(self, count: int) -> ServiceResourceStacksCollection:
        """
        Fetch at most this many Stacks per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def pages(self) -> Iterator[List[Stack]]:
        """
        A generator which yields pages of Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def __iter__(self) -> Iterator[Stack]:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/stacks.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#serviceresourcestackscollection)
        """

class StackEventsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#CloudFormation.Stack.events)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
    """
    def all(self) -> StackEventsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#CloudFormation.Stack.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

    def filter(  # type: ignore[override]
        self, *, StackName: str = ..., NextToken: str = ...
    ) -> StackEventsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

    def limit(self, count: int) -> StackEventsCollection:
        """
        Return at most this many Events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

    def page_size(self, count: int) -> StackEventsCollection:
        """
        Fetch at most this many Events per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

    def pages(self) -> Iterator[List[Event]]:
        """
        A generator which yields pages of Events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

    def __iter__(self) -> Iterator[Event]:
        """
        A generator which yields Events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/events.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackevents)
        """

class StackResourceSummariesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#CloudFormation.Stack.resource_summaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
    """
    def all(self) -> StackResourceSummariesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#CloudFormation.Stack.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> StackResourceSummariesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

    def limit(self, count: int) -> StackResourceSummariesCollection:
        """
        Return at most this many StackResourceSummarys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

    def page_size(self, count: int) -> StackResourceSummariesCollection:
        """
        Fetch at most this many StackResourceSummarys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

    def pages(self) -> Iterator[List[StackResourceSummary]]:
        """
        A generator which yields pages of StackResourceSummarys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

    def __iter__(self) -> Iterator[StackResourceSummary]:
        """
        A generator which yields StackResourceSummarys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/resource_summaries.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource_summaries)
        """

class Event(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/event/index.html#CloudFormation.Event)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#event)
    """

    id: str
    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: ResourceStatusType
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    hook_type: str
    hook_status: HookStatusType
    hook_status_reason: str
    hook_invocation_point: Literal["PRE_PROVISION"]
    hook_failure_mode: HookFailureModeType
    detailed_status: DetailedStatusType
    meta: CloudFormationResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/event/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#eventget_available_subresources-method)
        """

_Event = Event

class Stack(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/index.html#CloudFormation.Stack)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stack)
    """

    name: str
    events: StackEventsCollection
    resource_summaries: StackResourceSummariesCollection
    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List[ParameterTypeDef]
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: RollbackConfigurationOutputTypeDef
    stack_status: StackStatusType
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List[str]
    timeout_in_minutes: int
    capabilities: List[CapabilityType]
    outputs: List[OutputTypeDef]
    role_arn: str
    tags: List[TagTypeDef]
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: StackDriftInformationTypeDef
    retain_except_on_create: bool
    deletion_mode: DeletionModeType
    detailed_status: DetailedStatusType
    meta: CloudFormationResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackget_available_subresources-method)
        """

    def cancel_update(
        self, **kwargs: Unpack[CancelUpdateStackInputStackCancelUpdateTypeDef]
    ) -> None:
        """
        Cancels an update on the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/cancel_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackcancel_update-method)
        """

    def delete(self, **kwargs: Unpack[DeleteStackInputStackDeleteTypeDef]) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackdelete-method)
        """

    def update(
        self, **kwargs: Unpack[UpdateStackInputStackUpdateTypeDef]
    ) -> UpdateStackOutputTypeDef:
        """
        Updates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackupdate-method)
        """

    def Resource(self, logical_id: str) -> _StackResource:
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/Resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stack/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackreload-method)
        """

_Stack = Stack

class StackResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresource/index.html#CloudFormation.StackResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresource)
    """

    stack_name: str
    logical_id: str
    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: ResourceStatusType
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: StackResourceDriftInformationTypeDef
    module_info: ModuleInfoTypeDef
    meta: CloudFormationResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this StackResource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourceget_available_subresources-method)
        """

    def Stack(self) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresource/Stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourcestack-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresource/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourceload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresource/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourcereload-method)
        """

_StackResource = StackResource

class StackResourceSummary(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresourcesummary/index.html#CloudFormation.StackResourceSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourcesummary)
    """

    stack_name: str
    logical_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: ResourceStatusType
    resource_status_reason: str
    drift_information: StackResourceDriftInformationSummaryTypeDef
    module_info: ModuleInfoTypeDef
    meta: CloudFormationResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this StackResourceSummary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresourcesummary/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourcesummaryget_available_subresources-method)
        """

    def Resource(self) -> _StackResource:
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/stackresourcesummary/Resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#stackresourcesummaryresource-method)
        """

_StackResourceSummary = StackResourceSummary

class CloudFormationResourceMeta(ResourceMeta):
    client: CloudFormationClient  # type: ignore[override]

class CloudFormationServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/)
    """

    meta: CloudFormationResourceMeta  # type: ignore[override]
    stacks: ServiceResourceStacksCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourceget_available_subresources-method)
        """

    def create_stack(
        self, **kwargs: Unpack[CreateStackInputServiceResourceCreateStackTypeDef]
    ) -> _Stack:
        """
        Creates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/create_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourcecreate_stack-method)
        """

    def Event(self, id: str) -> _Event:
        """
        Creates a Event resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/Event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourceevent-method)
        """

    def Stack(self, name: str) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/Stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourcestack-method)
        """

    def StackResource(self, stack_name: str, logical_id: str) -> _StackResource:
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/StackResource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourcestackresource-method)
        """

    def StackResourceSummary(self, stack_name: str, logical_id: str) -> _StackResourceSummary:
        """
        Creates a StackResourceSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/service-resource/StackResourceSummary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource/#cloudformationserviceresourcestackresourcesummary-method)
        """
