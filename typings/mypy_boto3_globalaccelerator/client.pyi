"""
Type annotations for globalaccelerator service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import GlobalAcceleratorClient

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ClientAffinityType, HealthCheckProtocolType, IpAddressTypeType, ProtocolType
from .paginator import (
    ListAcceleratorsPaginator,
    ListByoipCidrsPaginator,
    ListCrossAccountAttachmentsPaginator,
    ListCrossAccountResourcesPaginator,
    ListCustomRoutingAcceleratorsPaginator,
    ListCustomRoutingEndpointGroupsPaginator,
    ListCustomRoutingListenersPaginator,
    ListCustomRoutingPortMappingsByDestinationPaginator,
    ListCustomRoutingPortMappingsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)
from .type_defs import (
    AddCustomRoutingEndpointsResponseTypeDef,
    AddEndpointsResponseTypeDef,
    AdvertiseByoipCidrResponseTypeDef,
    CidrAuthorizationContextTypeDef,
    CreateAcceleratorResponseTypeDef,
    CreateCrossAccountAttachmentResponseTypeDef,
    CreateCustomRoutingAcceleratorResponseTypeDef,
    CreateCustomRoutingEndpointGroupResponseTypeDef,
    CreateCustomRoutingListenerResponseTypeDef,
    CreateEndpointGroupResponseTypeDef,
    CreateListenerResponseTypeDef,
    CustomRoutingDestinationConfigurationTypeDef,
    CustomRoutingEndpointConfigurationTypeDef,
    DeprovisionByoipCidrResponseTypeDef,
    DescribeAcceleratorAttributesResponseTypeDef,
    DescribeAcceleratorResponseTypeDef,
    DescribeCrossAccountAttachmentResponseTypeDef,
    DescribeCustomRoutingAcceleratorAttributesResponseTypeDef,
    DescribeCustomRoutingAcceleratorResponseTypeDef,
    DescribeCustomRoutingEndpointGroupResponseTypeDef,
    DescribeCustomRoutingListenerResponseTypeDef,
    DescribeEndpointGroupResponseTypeDef,
    DescribeListenerResponseTypeDef,
    EndpointConfigurationTypeDef,
    EndpointIdentifierTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListCrossAccountAttachmentsResponseTypeDef,
    ListCrossAccountResourceAccountsResponseTypeDef,
    ListCrossAccountResourcesResponseTypeDef,
    ListCustomRoutingAcceleratorsResponseTypeDef,
    ListCustomRoutingEndpointGroupsResponseTypeDef,
    ListCustomRoutingListenersResponseTypeDef,
    ListCustomRoutingPortMappingsByDestinationResponseTypeDef,
    ListCustomRoutingPortMappingsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PortOverrideTypeDef,
    PortRangeTypeDef,
    ProvisionByoipCidrResponseTypeDef,
    ResourceTypeDef,
    TagTypeDef,
    UpdateAcceleratorAttributesResponseTypeDef,
    UpdateAcceleratorResponseTypeDef,
    UpdateCrossAccountAttachmentResponseTypeDef,
    UpdateCustomRoutingAcceleratorAttributesResponseTypeDef,
    UpdateCustomRoutingAcceleratorResponseTypeDef,
    UpdateCustomRoutingListenerResponseTypeDef,
    UpdateEndpointGroupResponseTypeDef,
    UpdateListenerResponseTypeDef,
    WithdrawByoipCidrResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GlobalAcceleratorClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AcceleratorNotDisabledException: Type[BotocoreClientError]
    AcceleratorNotFoundException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AssociatedEndpointGroupFoundException: Type[BotocoreClientError]
    AssociatedListenerFoundException: Type[BotocoreClientError]
    AttachmentNotFoundException: Type[BotocoreClientError]
    ByoipCidrNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EndpointAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupNotFoundException: Type[BotocoreClientError]
    EndpointNotFoundException: Type[BotocoreClientError]
    IncorrectCidrStateException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidPortRangeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]
    TransactionInProgressException: Type[BotocoreClientError]

class GlobalAcceleratorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GlobalAcceleratorClient exceptions.
        """

    def add_custom_routing_endpoints(
        self,
        *,
        EndpointConfigurations: List["CustomRoutingEndpointConfigurationTypeDef"],
        EndpointGroupArn: str
    ) -> AddCustomRoutingEndpointsResponseTypeDef:
        """
        Associate a virtual private cloud (VPC) subnet endpoint with your custom routing
        accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.add_custom_routing_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#add_custom_routing_endpoints)
        """

    def add_endpoints(
        self, *, EndpointConfigurations: List["EndpointConfigurationTypeDef"], EndpointGroupArn: str
    ) -> AddEndpointsResponseTypeDef:
        """
        Add endpoints to an endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.add_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#add_endpoints)
        """

    def advertise_byoip_cidr(self, *, Cidr: str) -> AdvertiseByoipCidrResponseTypeDef:
        """
        Advertises an IPv4 address range that is provisioned for use with your Amazon
        Web Services resources through bring your own IP addresses (BYOIP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.advertise_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#advertise_byoip_cidr)
        """

    def allow_custom_routing_traffic(
        self,
        *,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        AllowAllTrafficToEndpoint: bool = None
    ) -> None:
        """
        Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC
        subnet endpoint that can receive traffic for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.allow_custom_routing_traffic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#allow_custom_routing_traffic)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#close)
        """

    def create_accelerator(
        self,
        *,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: IpAddressTypeType = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAcceleratorResponseTypeDef:
        """
        Create an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_accelerator)
        """

    def create_cross_account_attachment(
        self,
        *,
        Name: str,
        IdempotencyToken: str,
        Principals: List[str] = None,
        Resources: List["ResourceTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCrossAccountAttachmentResponseTypeDef:
        """
        Create a cross-account attachment in Global Accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_cross_account_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_cross_account_attachment)
        """

    def create_custom_routing_accelerator(
        self,
        *,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: IpAddressTypeType = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCustomRoutingAcceleratorResponseTypeDef:
        """
        Create a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_accelerator)
        """

    def create_custom_routing_endpoint_group(
        self,
        *,
        ListenerArn: str,
        EndpointGroupRegion: str,
        DestinationConfigurations: List["CustomRoutingDestinationConfigurationTypeDef"],
        IdempotencyToken: str
    ) -> CreateCustomRoutingEndpointGroupResponseTypeDef:
        """
        Create an endpoint group for the specified listener for a custom routing
        accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_endpoint_group)
        """

    def create_custom_routing_listener(
        self, *, AcceleratorArn: str, PortRanges: List["PortRangeTypeDef"], IdempotencyToken: str
    ) -> CreateCustomRoutingListenerResponseTypeDef:
        """
        Create a listener to process inbound connections from clients to a custom
        routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_listener)
        """

    def create_endpoint_group(
        self,
        *,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List["EndpointConfigurationTypeDef"] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: HealthCheckProtocolType = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None
    ) -> CreateEndpointGroupResponseTypeDef:
        """
        Create an endpoint group for the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_endpoint_group)
        """

    def create_listener(
        self,
        *,
        AcceleratorArn: str,
        PortRanges: List["PortRangeTypeDef"],
        Protocol: ProtocolType,
        IdempotencyToken: str,
        ClientAffinity: ClientAffinityType = None
    ) -> CreateListenerResponseTypeDef:
        """
        Create a listener to process inbound connections from clients to an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_listener)
        """

    def delete_accelerator(self, *, AcceleratorArn: str) -> None:
        """
        Delete an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_accelerator)
        """

    def delete_cross_account_attachment(self, *, AttachmentArn: str) -> None:
        """
        Delete a cross-account attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_cross_account_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_cross_account_attachment)
        """

    def delete_custom_routing_accelerator(self, *, AcceleratorArn: str) -> None:
        """
        Delete a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_accelerator)
        """

    def delete_custom_routing_endpoint_group(self, *, EndpointGroupArn: str) -> None:
        """
        Delete an endpoint group from a listener for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_endpoint_group)
        """

    def delete_custom_routing_listener(self, *, ListenerArn: str) -> None:
        """
        Delete a listener for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_listener)
        """

    def delete_endpoint_group(self, *, EndpointGroupArn: str) -> None:
        """
        Delete an endpoint group from a listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_endpoint_group)
        """

    def delete_listener(self, *, ListenerArn: str) -> None:
        """
        Delete a listener from an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_listener)
        """

    def deny_custom_routing_traffic(
        self,
        *,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        DenyAllTrafficToEndpoint: bool = None
    ) -> None:
        """
        Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC
        subnet endpoint that cannot receive traffic for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deny_custom_routing_traffic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#deny_custom_routing_traffic)
        """

    def deprovision_byoip_cidr(self, *, Cidr: str) -> DeprovisionByoipCidrResponseTypeDef:
        """
        Releases the specified address range that you provisioned to use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP) and
        deletes the corresponding address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deprovision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#deprovision_byoip_cidr)
        """

    def describe_accelerator(self, *, AcceleratorArn: str) -> DescribeAcceleratorResponseTypeDef:
        """
        Describe an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_accelerator)
        """

    def describe_accelerator_attributes(
        self, *, AcceleratorArn: str
    ) -> DescribeAcceleratorAttributesResponseTypeDef:
        """
        Describe the attributes of an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_accelerator_attributes)
        """

    def describe_cross_account_attachment(
        self, *, AttachmentArn: str
    ) -> DescribeCrossAccountAttachmentResponseTypeDef:
        """
        Gets configuration information about a cross-account attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_cross_account_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_cross_account_attachment)
        """

    def describe_custom_routing_accelerator(
        self, *, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorResponseTypeDef:
        """
        Describe a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_accelerator)
        """

    def describe_custom_routing_accelerator_attributes(
        self, *, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        Describe the attributes of a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_accelerator_attributes)
        """

    def describe_custom_routing_endpoint_group(
        self, *, EndpointGroupArn: str
    ) -> DescribeCustomRoutingEndpointGroupResponseTypeDef:
        """
        Describe an endpoint group for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_endpoint_group)
        """

    def describe_custom_routing_listener(
        self, *, ListenerArn: str
    ) -> DescribeCustomRoutingListenerResponseTypeDef:
        """
        The description of a listener for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_listener)
        """

    def describe_endpoint_group(
        self, *, EndpointGroupArn: str
    ) -> DescribeEndpointGroupResponseTypeDef:
        """
        Describe an endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_endpoint_group)
        """

    def describe_listener(self, *, ListenerArn: str) -> DescribeListenerResponseTypeDef:
        """
        Describe a listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_listener)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#generate_presigned_url)
        """

    def list_accelerators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAcceleratorsResponseTypeDef:
        """
        List the accelerators for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_accelerators)
        """

    def list_byoip_cidrs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListByoipCidrsResponseTypeDef:
        """
        Lists the IP address ranges that were specified in calls to `ProvisionByoipCidr
        <https://docs.aws.amazon.com/global-
        accelerator/latest/api/ProvisionByoipCidr.html>`__, including the current state
        and a history of state changes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_byoip_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_byoip_cidrs)
        """

    def list_cross_account_attachments(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCrossAccountAttachmentsResponseTypeDef:
        """
        List the cross-account attachments that have been created in Global Accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_cross_account_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_cross_account_attachments)
        """

    def list_cross_account_resource_accounts(
        self,
    ) -> ListCrossAccountResourceAccountsResponseTypeDef:
        """
        List the accounts that have cross-account resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_cross_account_resource_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_cross_account_resource_accounts)
        """

    def list_cross_account_resources(
        self,
        *,
        ResourceOwnerAwsAccountId: str,
        AcceleratorArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCrossAccountResourcesResponseTypeDef:
        """
        List the cross-account resources available to work with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_cross_account_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_cross_account_resources)
        """

    def list_custom_routing_accelerators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingAcceleratorsResponseTypeDef:
        """
        List the custom routing accelerators for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_accelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_accelerators)
        """

    def list_custom_routing_endpoint_groups(
        self, *, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingEndpointGroupsResponseTypeDef:
        """
        List the endpoint groups that are associated with a listener for a custom
        routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_endpoint_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_endpoint_groups)
        """

    def list_custom_routing_listeners(
        self, *, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingListenersResponseTypeDef:
        """
        List the listeners for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_listeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_listeners)
        """

    def list_custom_routing_port_mappings(
        self,
        *,
        AcceleratorArn: str,
        EndpointGroupArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomRoutingPortMappingsResponseTypeDef:
        """
        Provides a complete mapping from the public accelerator IP address and port to
        destination EC2 instance IP addresses and ports in the virtual public cloud
        (VPC) subnet endpoint for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_port_mappings)
        """

    def list_custom_routing_port_mappings_by_destination(
        self,
        *,
        EndpointId: str,
        DestinationAddress: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomRoutingPortMappingsByDestinationResponseTypeDef:
        """
        List the port mappings for a specific EC2 instance (destination) in a VPC subnet
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings_by_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_port_mappings_by_destination)
        """

    def list_endpoint_groups(
        self, *, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEndpointGroupsResponseTypeDef:
        """
        List the endpoint groups that are associated with a listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_endpoint_groups)
        """

    def list_listeners(
        self, *, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        List the listeners for an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_listeners)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags for an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_tags_for_resource)
        """

    def provision_byoip_cidr(
        self, *, Cidr: str, CidrAuthorizationContext: "CidrAuthorizationContextTypeDef"
    ) -> ProvisionByoipCidrResponseTypeDef:
        """
        Provisions an IP address range to use with your Amazon Web Services resources
        through bring your own IP addresses (BYOIP) and creates a corresponding address
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.provision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#provision_byoip_cidr)
        """

    def remove_custom_routing_endpoints(
        self, *, EndpointIds: List[str], EndpointGroupArn: str
    ) -> None:
        """
        Remove endpoints from a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.remove_custom_routing_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#remove_custom_routing_endpoints)
        """

    def remove_endpoints(
        self, *, EndpointIdentifiers: List["EndpointIdentifierTypeDef"], EndpointGroupArn: str
    ) -> None:
        """
        Remove endpoints from an endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.remove_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#remove_endpoints)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add tags to an accelerator resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from a Global Accelerator resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#untag_resource)
        """

    def update_accelerator(
        self,
        *,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: IpAddressTypeType = None,
        Enabled: bool = None
    ) -> UpdateAcceleratorResponseTypeDef:
        """
        Update an accelerator to make changes, such as the following * Change the name
        of the accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_accelerator)
        """

    def update_accelerator_attributes(
        self,
        *,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None
    ) -> UpdateAcceleratorAttributesResponseTypeDef:
        """
        Update the attributes for an accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_accelerator_attributes)
        """

    def update_cross_account_attachment(
        self,
        *,
        AttachmentArn: str,
        Name: str = None,
        AddPrincipals: List[str] = None,
        RemovePrincipals: List[str] = None,
        AddResources: List["ResourceTypeDef"] = None,
        RemoveResources: List["ResourceTypeDef"] = None
    ) -> UpdateCrossAccountAttachmentResponseTypeDef:
        """
        Update a cross-account attachment to add or remove principals or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_cross_account_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_cross_account_attachment)
        """

    def update_custom_routing_accelerator(
        self,
        *,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: IpAddressTypeType = None,
        Enabled: bool = None
    ) -> UpdateCustomRoutingAcceleratorResponseTypeDef:
        """
        Update a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_accelerator)
        """

    def update_custom_routing_accelerator_attributes(
        self,
        *,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None
    ) -> UpdateCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        Update the attributes for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_accelerator_attributes)
        """

    def update_custom_routing_listener(
        self, *, ListenerArn: str, PortRanges: List["PortRangeTypeDef"]
    ) -> UpdateCustomRoutingListenerResponseTypeDef:
        """
        Update a listener for a custom routing accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_listener)
        """

    def update_endpoint_group(
        self,
        *,
        EndpointGroupArn: str,
        EndpointConfigurations: List["EndpointConfigurationTypeDef"] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: HealthCheckProtocolType = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None
    ) -> UpdateEndpointGroupResponseTypeDef:
        """
        Update an endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_endpoint_group)
        """

    def update_listener(
        self,
        *,
        ListenerArn: str,
        PortRanges: List["PortRangeTypeDef"] = None,
        Protocol: ProtocolType = None,
        ClientAffinity: ClientAffinityType = None
    ) -> UpdateListenerResponseTypeDef:
        """
        Update a listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_listener)
        """

    def withdraw_byoip_cidr(self, *, Cidr: str) -> WithdrawByoipCidrResponseTypeDef:
        """
        Stops advertising an address range that is provisioned as an address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Client.withdraw_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> ListAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listacceleratorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_byoip_cidrs"]) -> ListByoipCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listbyoipcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cross_account_attachments"]
    ) -> ListCrossAccountAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCrossAccountAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcrossaccountattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cross_account_resources"]
    ) -> ListCrossAccountResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCrossAccountResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcrossaccountresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_accelerators"]
    ) -> ListCustomRoutingAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingacceleratorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_endpoint_groups"]
    ) -> ListCustomRoutingEndpointGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingEndpointGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingendpointgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_listeners"]
    ) -> ListCustomRoutingListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutinglistenerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings"]
    ) -> ListCustomRoutingPortMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingportmappingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings_by_destination"]
    ) -> ListCustomRoutingPortMappingsByDestinationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingportmappingsbydestinationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> ListEndpointGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listendpointgroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listlistenerspaginator)
        """
