"""
Type annotations for cloudformation service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudformation import CloudFormationServiceResource
    import mypy_boto3_cloudformation.service_resource as cloudformation_resources

    resource: CloudFormationServiceResource = boto3.resource("cloudformation")

    my_event: cloudformation_resources.Event = resource.Event(...)
    my_stack: cloudformation_resources.Stack = resource.Stack(...)
    my_stack_resource: cloudformation_resources.StackResource = resource.StackResource(...)
    my_stack_resource_summary: cloudformation_resources.StackResourceSummary = resource.StackResourceSummary(...)
```
"""

from datetime import datetime
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import CloudFormationClient
from .literals import CapabilityType, DeletionModeType, OnFailureType
from .type_defs import (
    ParameterTypeDef,
    RollbackConfigurationTypeDef,
    TagTypeDef,
    UpdateStackOutputTypeDef,
)

__all__ = (
    "CloudFormationServiceResource",
    "Event",
    "Stack",
    "StackResource",
    "StackResourceSummary",
    "ServiceResourceStacksCollection",
    "StackEventsCollection",
    "StackResourceSummariesCollection",
)

class ServiceResourceStacksCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#serviceresourcestackscollection)
    """

    def all(self) -> "ServiceResourceStacksCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, StackName: str = None, NextToken: str = None
    ) -> "ServiceResourceStacksCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Return at most this many Stacks.
        """

    def page_size(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Fetch at most this many Stacks per service request.
        """

    def pages(self) -> Iterator[List["Stack"]]:
        """
        A generator which yields pages of Stacks.
        """

    def __iter__(self) -> Iterator["Stack"]:
        """
        A generator which yields Stacks.
        """

class StackEventsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.events)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackeventscollection)
    """

    def all(self) -> "StackEventsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, StackName: str = None, NextToken: str = None
    ) -> "StackEventsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "StackEventsCollection":
        """
        Return at most this many Events.
        """

    def page_size(self, count: int) -> "StackEventsCollection":
        """
        Fetch at most this many Events per service request.
        """

    def pages(self) -> Iterator[List["Event"]]:
        """
        A generator which yields pages of Events.
        """

    def __iter__(self) -> Iterator["Event"]:
        """
        A generator which yields Events.
        """

class StackResourceSummariesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.resource_summaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcesummariescollection)
    """

    def all(self) -> "StackResourceSummariesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, NextToken: str = None
    ) -> "StackResourceSummariesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "StackResourceSummariesCollection":
        """
        Return at most this many StackResourceSummarys.
        """

    def page_size(self, count: int) -> "StackResourceSummariesCollection":
        """
        Fetch at most this many StackResourceSummarys per service request.
        """

    def pages(self) -> Iterator[List["StackResourceSummary"]]:
        """
        A generator which yields pages of StackResourceSummarys.
        """

    def __iter__(self) -> Iterator["StackResourceSummary"]:
        """
        A generator which yields StackResourceSummarys.
        """

class Event(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#event)
    """

    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: str
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    hook_type: str
    hook_status: str
    hook_status_reason: str
    hook_invocation_point: str
    hook_failure_mode: str
    detailed_status: str
    id: str

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Event.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#eventget_available_subresources-method)
        """

_Event = Event

class Stack(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stack)
    """

    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List[Any]
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: Dict[str, Any]
    stack_status: str
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List[Any]
    timeout_in_minutes: int
    capabilities: List[Any]
    outputs: List[Any]
    role_arn: str
    tags: List[Any]
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: Dict[str, Any]
    retain_except_on_create: bool
    deletion_mode: str
    detailed_status: str
    name: str
    events: StackEventsCollection
    resource_summaries: StackResourceSummariesCollection

    def Resource(self, logical_id: str) -> "_StackResource":
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.Resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresource-method)
        """

    def cancel_update(self, *, ClientRequestToken: str = None) -> None:
        """
        Cancels an update on the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.cancel_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackcancel_update-method)
        """

    def delete(
        self,
        *,
        RetainResources: List[str] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None,
        DeletionMode: DeletionModeType = None
    ) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stacks` to update the attributes
        of the Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stacks` to update the attributes
        of the Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackreload-method)
        """

    def update(
        self,
        *,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[CapabilityType] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        DisableRollback: bool = None,
        ClientRequestToken: str = None,
        RetainExceptOnCreate: bool = None
    ) -> UpdateStackOutputTypeDef:
        """
        Updates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.Stack.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackupdate-method)
        """

_Stack = Stack

class StackResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresource)
    """

    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: Dict[str, Any]
    module_info: Dict[str, Any]
    stack_name: str
    logical_id: str

    def Stack(self) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResource.Stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcestack-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourceget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stack_resource` to update the
        attributes of the StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResource.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourceload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stack_resource` to update the
        attributes of the StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResource.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcereload-method)
        """

_StackResource = StackResource

class StackResourceSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcesummary)
    """

    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict[str, Any]
    module_info: Dict[str, Any]
    stack_name: str
    logical_id: str

    def Resource(self) -> _StackResource:
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.Resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcesummaryresource-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#stackresourcesummaryget_available_subresources-method)
        """

_StackResourceSummary = StackResourceSummary

class CloudFormationResourceMeta(ResourceMeta):
    client: CloudFormationClient

class CloudFormationServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html)
    """

    meta: "CloudFormationResourceMeta"
    stacks: ServiceResourceStacksCollection

    def Event(self, id: str) -> _Event:
        """
        Creates a Event resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourceevent-method)
        """

    def Stack(self, name: str) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourcestack-method)
        """

    def StackResource(self, stack_name: str, logical_id: str) -> _StackResource:
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourcestackresource-method)
        """

    def StackResourceSummary(self, stack_name: str, logical_id: str) -> _StackResourceSummary:
        """
        Creates a StackResourceSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourcestackresourcesummary-method)
        """

    def create_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[str] = None,
        Capabilities: List[CapabilityType] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        OnFailure: OnFailureType = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
        RetainExceptOnCreate: bool = None
    ) -> _Stack:
        """
        Creates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.create_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourcecreate_stack-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudformation.html#CloudFormation.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/service_resource.html#cloudformationserviceresourceget_available_subresources-method)
        """
