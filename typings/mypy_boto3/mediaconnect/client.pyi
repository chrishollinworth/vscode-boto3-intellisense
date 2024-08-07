"""
Type annotations for mediaconnect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediaconnect import MediaConnectClient

    client: MediaConnectClient = boto3.client("mediaconnect")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BridgePlacementType,
    DesiredStateType,
    EntitlementStatusType,
    MediaStreamTypeType,
    ProtocolType,
)
from .paginator import (
    ListBridgesPaginator,
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListGatewayInstancesPaginator,
    ListGatewaysPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from .type_defs import (
    AddBridgeOutputRequestTypeDef,
    AddBridgeOutputsResponseTypeDef,
    AddBridgeSourceRequestTypeDef,
    AddBridgeSourcesResponseTypeDef,
    AddEgressGatewayBridgeRequestTypeDef,
    AddFlowMediaStreamsResponseTypeDef,
    AddFlowOutputsResponseTypeDef,
    AddFlowSourcesResponseTypeDef,
    AddFlowVpcInterfacesResponseTypeDef,
    AddIngressGatewayBridgeRequestTypeDef,
    AddMaintenanceTypeDef,
    AddMediaStreamRequestTypeDef,
    AddOutputRequestTypeDef,
    CreateBridgeResponseTypeDef,
    CreateFlowResponseTypeDef,
    CreateGatewayResponseTypeDef,
    DeleteBridgeResponseTypeDef,
    DeleteFlowResponseTypeDef,
    DeleteGatewayResponseTypeDef,
    DeregisterGatewayInstanceResponseTypeDef,
    DescribeBridgeResponseTypeDef,
    DescribeFlowResponseTypeDef,
    DescribeFlowSourceMetadataResponseTypeDef,
    DescribeGatewayInstanceResponseTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationResponseTypeDef,
    FailoverConfigTypeDef,
    GatewayNetworkTypeDef,
    GrantEntitlementRequestTypeDef,
    GrantFlowEntitlementsResponseTypeDef,
    ListBridgesResponseTypeDef,
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    ListGatewayInstancesResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MediaStreamAttributesRequestTypeDef,
    MediaStreamOutputConfigurationRequestTypeDef,
    MediaStreamSourceConfigurationRequestTypeDef,
    PurchaseOfferingResponseTypeDef,
    RemoveBridgeOutputResponseTypeDef,
    RemoveBridgeSourceResponseTypeDef,
    RemoveFlowMediaStreamResponseTypeDef,
    RemoveFlowOutputResponseTypeDef,
    RemoveFlowSourceResponseTypeDef,
    RemoveFlowVpcInterfaceResponseTypeDef,
    RevokeFlowEntitlementResponseTypeDef,
    SetSourceRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowResponseTypeDef,
    UpdateBridgeFlowSourceRequestTypeDef,
    UpdateBridgeNetworkOutputRequestTypeDef,
    UpdateBridgeNetworkSourceRequestTypeDef,
    UpdateBridgeOutputResponseTypeDef,
    UpdateBridgeResponseTypeDef,
    UpdateBridgeSourceResponseTypeDef,
    UpdateBridgeStateResponseTypeDef,
    UpdateEgressGatewayBridgeRequestTypeDef,
    UpdateEncryptionTypeDef,
    UpdateFailoverConfigTypeDef,
    UpdateFlowEntitlementResponseTypeDef,
    UpdateFlowMediaStreamResponseTypeDef,
    UpdateFlowOutputResponseTypeDef,
    UpdateFlowResponseTypeDef,
    UpdateFlowSourceResponseTypeDef,
    UpdateGatewayBridgeSourceRequestTypeDef,
    UpdateGatewayInstanceResponseTypeDef,
    UpdateIngressGatewayBridgeRequestTypeDef,
    UpdateMaintenanceTypeDef,
    VpcInterfaceAttachmentTypeDef,
    VpcInterfaceRequestTypeDef,
)
from .waiter import FlowActiveWaiter, FlowDeletedWaiter, FlowStandbyWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MediaConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AddFlowOutputs420Exception: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CreateBridge420Exception: Type[BotocoreClientError]
    CreateFlow420Exception: Type[BotocoreClientError]
    CreateGateway420Exception: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GrantFlowEntitlements420Exception: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class MediaConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaConnectClient exceptions.
        """

    def add_bridge_outputs(
        self, *, BridgeArn: str, Outputs: List["AddBridgeOutputRequestTypeDef"]
    ) -> AddBridgeOutputsResponseTypeDef:
        """
        Adds outputs to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_bridge_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_bridge_outputs)
        """

    def add_bridge_sources(
        self, *, BridgeArn: str, Sources: List["AddBridgeSourceRequestTypeDef"]
    ) -> AddBridgeSourcesResponseTypeDef:
        """
        Adds sources to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_bridge_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_bridge_sources)
        """

    def add_flow_media_streams(
        self, *, FlowArn: str, MediaStreams: List["AddMediaStreamRequestTypeDef"]
    ) -> AddFlowMediaStreamsResponseTypeDef:
        """
        Adds media streams to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_media_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_flow_media_streams)
        """

    def add_flow_outputs(
        self, *, FlowArn: str, Outputs: List["AddOutputRequestTypeDef"]
    ) -> AddFlowOutputsResponseTypeDef:
        """
        Adds outputs to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_flow_outputs)
        """

    def add_flow_sources(
        self, *, FlowArn: str, Sources: List["SetSourceRequestTypeDef"]
    ) -> AddFlowSourcesResponseTypeDef:
        """
        Adds Sources to flow See also: `AWS API Documentation <https://docs.aws.amazon.c
        om/goto/WebAPI/mediaconnect-2018-11-14/AddFlowSources>`_ **Request Syntax**
        response = client.add_flow_sources( FlowArn='string', Sources=[ { 'Decryption':
        { ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_flow_sources)
        """

    def add_flow_vpc_interfaces(
        self, *, FlowArn: str, VpcInterfaces: List["VpcInterfaceRequestTypeDef"]
    ) -> AddFlowVpcInterfacesResponseTypeDef:
        """
        Adds VPC interfaces to flow See also: `AWS API Documentation <https://docs.aws.a
        mazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowVpcInterfaces>`_ **Request
        Syntax** response = client.add_flow_vpc_interfaces( FlowArn='string',
        VpcInterfaces=[ { 'Nam...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_vpc_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#add_flow_vpc_interfaces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#close)
        """

    def create_bridge(
        self,
        *,
        Name: str,
        PlacementArn: str,
        Sources: List["AddBridgeSourceRequestTypeDef"],
        EgressGatewayBridge: "AddEgressGatewayBridgeRequestTypeDef" = None,
        IngressGatewayBridge: "AddIngressGatewayBridgeRequestTypeDef" = None,
        Outputs: List["AddBridgeOutputRequestTypeDef"] = None,
        SourceFailoverConfig: "FailoverConfigTypeDef" = None
    ) -> CreateBridgeResponseTypeDef:
        """
        Creates a new bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.create_bridge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#create_bridge)
        """

    def create_flow(
        self,
        *,
        Name: str,
        AvailabilityZone: str = None,
        Entitlements: List["GrantEntitlementRequestTypeDef"] = None,
        MediaStreams: List["AddMediaStreamRequestTypeDef"] = None,
        Outputs: List["AddOutputRequestTypeDef"] = None,
        Source: "SetSourceRequestTypeDef" = None,
        SourceFailoverConfig: "FailoverConfigTypeDef" = None,
        Sources: List["SetSourceRequestTypeDef"] = None,
        VpcInterfaces: List["VpcInterfaceRequestTypeDef"] = None,
        Maintenance: "AddMaintenanceTypeDef" = None
    ) -> CreateFlowResponseTypeDef:
        """
        Creates a new flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.create_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#create_flow)
        """

    def create_gateway(
        self, *, EgressCidrBlocks: List[str], Name: str, Networks: List["GatewayNetworkTypeDef"]
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a new gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.create_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#create_gateway)
        """

    def delete_bridge(self, *, BridgeArn: str) -> DeleteBridgeResponseTypeDef:
        """
        Deletes a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.delete_bridge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#delete_bridge)
        """

    def delete_flow(self, *, FlowArn: str) -> DeleteFlowResponseTypeDef:
        """
        Deletes a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.delete_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#delete_flow)
        """

    def delete_gateway(self, *, GatewayArn: str) -> DeleteGatewayResponseTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.delete_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#delete_gateway)
        """

    def deregister_gateway_instance(
        self, *, GatewayInstanceArn: str, Force: bool = None
    ) -> DeregisterGatewayInstanceResponseTypeDef:
        """
        Deregisters an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.deregister_gateway_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#deregister_gateway_instance)
        """

    def describe_bridge(self, *, BridgeArn: str) -> DescribeBridgeResponseTypeDef:
        """
        Displays the details of a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_bridge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_bridge)
        """

    def describe_flow(self, *, FlowArn: str) -> DescribeFlowResponseTypeDef:
        """
        Displays the details of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_flow)
        """

    def describe_flow_source_metadata(
        self, *, FlowArn: str
    ) -> DescribeFlowSourceMetadataResponseTypeDef:
        """
        Displays details of the flow's source stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow_source_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_flow_source_metadata)
        """

    def describe_gateway(self, *, GatewayArn: str) -> DescribeGatewayResponseTypeDef:
        """
        Displays the details of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_gateway)
        """

    def describe_gateway_instance(
        self, *, GatewayInstanceArn: str
    ) -> DescribeGatewayInstanceResponseTypeDef:
        """
        Displays the details of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_gateway_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_gateway_instance)
        """

    def describe_offering(self, *, OfferingArn: str) -> DescribeOfferingResponseTypeDef:
        """
        Displays the details of an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_offering)
        """

    def describe_reservation(self, *, ReservationArn: str) -> DescribeReservationResponseTypeDef:
        """
        Displays the details of a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.describe_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#describe_reservation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#generate_presigned_url)
        """

    def grant_flow_entitlements(
        self, *, Entitlements: List["GrantEntitlementRequestTypeDef"], FlowArn: str
    ) -> GrantFlowEntitlementsResponseTypeDef:
        """
        Grants entitlements to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.grant_flow_entitlements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#grant_flow_entitlements)
        """

    def list_bridges(
        self, *, FilterArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListBridgesResponseTypeDef:
        """
        Displays a list of bridges that are associated with this account and an
        optionally specified Arn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_bridges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_bridges)
        """

    def list_entitlements(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListEntitlementsResponseTypeDef:
        """
        Displays a list of all entitlements that have been granted to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_entitlements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_entitlements)
        """

    def list_flows(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListFlowsResponseTypeDef:
        """
        Displays a list of flows that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_flows)
        """

    def list_gateway_instances(
        self, *, FilterArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListGatewayInstancesResponseTypeDef:
        """
        Displays a list of instances associated with the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_gateway_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_gateway_instances)
        """

    def list_gateways(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListGatewaysResponseTypeDef:
        """
        Displays a list of gateways that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_gateways)
        """

    def list_offerings(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListOfferingsResponseTypeDef:
        """
        Displays a list of all offerings that are available to this account in the
        current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_offerings)
        """

    def list_reservations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListReservationsResponseTypeDef:
        """
        Displays a list of all reservations that have been purchased by this account in
        the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_reservations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags on an AWS Elemental MediaConnect resource See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-
        14/ListTagsForResource>`_ **Request Syntax** response =
        client.list_tags_for_resource( ResourceArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#list_tags_for_resource)
        """

    def purchase_offering(
        self, *, OfferingArn: str, ReservationName: str, Start: str
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Submits a request to purchase an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.purchase_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#purchase_offering)
        """

    def remove_bridge_output(
        self, *, BridgeArn: str, OutputName: str
    ) -> RemoveBridgeOutputResponseTypeDef:
        """
        Removes an output from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_bridge_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_bridge_output)
        """

    def remove_bridge_source(
        self, *, BridgeArn: str, SourceName: str
    ) -> RemoveBridgeSourceResponseTypeDef:
        """
        Removes a source from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_bridge_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_bridge_source)
        """

    def remove_flow_media_stream(
        self, *, FlowArn: str, MediaStreamName: str
    ) -> RemoveFlowMediaStreamResponseTypeDef:
        """
        Removes a media stream from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_media_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_flow_media_stream)
        """

    def remove_flow_output(
        self, *, FlowArn: str, OutputArn: str
    ) -> RemoveFlowOutputResponseTypeDef:
        """
        Removes an output from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_flow_output)
        """

    def remove_flow_source(
        self, *, FlowArn: str, SourceArn: str
    ) -> RemoveFlowSourceResponseTypeDef:
        """
        Removes a source from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_flow_source)
        """

    def remove_flow_vpc_interface(
        self, *, FlowArn: str, VpcInterfaceName: str
    ) -> RemoveFlowVpcInterfaceResponseTypeDef:
        """
        Removes a VPC Interface from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_vpc_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#remove_flow_vpc_interface)
        """

    def revoke_flow_entitlement(
        self, *, EntitlementArn: str, FlowArn: str
    ) -> RevokeFlowEntitlementResponseTypeDef:
        """
        Revokes an entitlement from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.revoke_flow_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#revoke_flow_entitlement)
        """

    def start_flow(self, *, FlowArn: str) -> StartFlowResponseTypeDef:
        """
        Starts a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.start_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#start_flow)
        """

    def stop_flow(self, *, FlowArn: str) -> StopFlowResponseTypeDef:
        """
        Stops a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.stop_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#stop_flow)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Associates the specified tags to a resource with the specified resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#untag_resource)
        """

    def update_bridge(
        self,
        *,
        BridgeArn: str,
        EgressGatewayBridge: "UpdateEgressGatewayBridgeRequestTypeDef" = None,
        IngressGatewayBridge: "UpdateIngressGatewayBridgeRequestTypeDef" = None,
        SourceFailoverConfig: "UpdateFailoverConfigTypeDef" = None
    ) -> UpdateBridgeResponseTypeDef:
        """
        Updates the bridge See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateBridge>`_
        **Request Syntax** response = client.update_bridge( BridgeArn='string',
        EgressGatewayBridge={ 'MaxBitrate': 123 }, Ingres...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_bridge)
        """

    def update_bridge_output(
        self,
        *,
        BridgeArn: str,
        OutputName: str,
        NetworkOutput: "UpdateBridgeNetworkOutputRequestTypeDef" = None
    ) -> UpdateBridgeOutputResponseTypeDef:
        """
        Updates an existing bridge output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_bridge_output)
        """

    def update_bridge_source(
        self,
        *,
        BridgeArn: str,
        SourceName: str,
        FlowSource: "UpdateBridgeFlowSourceRequestTypeDef" = None,
        NetworkSource: "UpdateBridgeNetworkSourceRequestTypeDef" = None
    ) -> UpdateBridgeSourceResponseTypeDef:
        """
        Updates an existing bridge source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_bridge_source)
        """

    def update_bridge_state(
        self, *, BridgeArn: str, DesiredState: DesiredStateType
    ) -> UpdateBridgeStateResponseTypeDef:
        """
        Updates the bridge state See also: `AWS API Documentation <https://docs.aws.amaz
        on.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateBridgeState>`_ **Request
        Syntax** response = client.update_bridge_state( BridgeArn='string',
        DesiredState='ACTIVE'|'STANDBY'|'DELETED' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_bridge_state)
        """

    def update_flow(
        self,
        *,
        FlowArn: str,
        SourceFailoverConfig: "UpdateFailoverConfigTypeDef" = None,
        Maintenance: "UpdateMaintenanceTypeDef" = None
    ) -> UpdateFlowResponseTypeDef:
        """
        Updates flow See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlow>`_
        **Request Syntax** response = client.update_flow( FlowArn='string',
        SourceFailoverConfig={ 'FailoverMode': 'MERGE'|'FAILOVER', 'Rec...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_flow)
        """

    def update_flow_entitlement(
        self,
        *,
        EntitlementArn: str,
        FlowArn: str,
        Description: str = None,
        Encryption: "UpdateEncryptionTypeDef" = None,
        EntitlementStatus: EntitlementStatusType = None,
        Subscribers: List[str] = None
    ) -> UpdateFlowEntitlementResponseTypeDef:
        """
        You can change an entitlement's description, subscribers, and encryption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_flow_entitlement)
        """

    def update_flow_media_stream(
        self,
        *,
        FlowArn: str,
        MediaStreamName: str,
        Attributes: "MediaStreamAttributesRequestTypeDef" = None,
        ClockRate: int = None,
        Description: str = None,
        MediaStreamType: MediaStreamTypeType = None,
        VideoFormat: str = None
    ) -> UpdateFlowMediaStreamResponseTypeDef:
        """
        Updates an existing media stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_media_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_flow_media_stream)
        """

    def update_flow_output(
        self,
        *,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: List[str] = None,
        Description: str = None,
        Destination: str = None,
        Encryption: "UpdateEncryptionTypeDef" = None,
        MaxLatency: int = None,
        MediaStreamOutputConfigurations: List[
            "MediaStreamOutputConfigurationRequestTypeDef"
        ] = None,
        MinLatency: int = None,
        Port: int = None,
        Protocol: ProtocolType = None,
        RemoteId: str = None,
        SenderControlPort: int = None,
        SenderIpAddress: str = None,
        SmoothingLatency: int = None,
        StreamId: str = None,
        VpcInterfaceAttachment: "VpcInterfaceAttachmentTypeDef" = None
    ) -> UpdateFlowOutputResponseTypeDef:
        """
        Updates an existing flow output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_flow_output)
        """

    def update_flow_source(
        self,
        *,
        FlowArn: str,
        SourceArn: str,
        Decryption: "UpdateEncryptionTypeDef" = None,
        Description: str = None,
        EntitlementArn: str = None,
        IngestPort: int = None,
        MaxBitrate: int = None,
        MaxLatency: int = None,
        MaxSyncBuffer: int = None,
        MediaStreamSourceConfigurations: List[
            "MediaStreamSourceConfigurationRequestTypeDef"
        ] = None,
        MinLatency: int = None,
        Protocol: ProtocolType = None,
        SenderControlPort: int = None,
        SenderIpAddress: str = None,
        SourceListenerAddress: str = None,
        SourceListenerPort: int = None,
        StreamId: str = None,
        VpcInterfaceName: str = None,
        WhitelistCidr: str = None,
        GatewayBridgeSource: "UpdateGatewayBridgeSourceRequestTypeDef" = None
    ) -> UpdateFlowSourceResponseTypeDef:
        """
        Updates the source of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_flow_source)
        """

    def update_gateway_instance(
        self, *, GatewayInstanceArn: str, BridgePlacement: BridgePlacementType = None
    ) -> UpdateGatewayInstanceResponseTypeDef:
        """
        Updates the configuration of an existing Gateway Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Client.update_gateway_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client.html#update_gateway_instance)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bridges"]) -> ListBridgesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListBridges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listbridgespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entitlements"]
    ) -> ListEntitlementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listentitlementspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_flows"]) -> ListFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listflowspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_gateway_instances"]
    ) -> ListGatewayInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListGatewayInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listgatewayinstancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listgatewayspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Paginator.ListReservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators.html#listreservationspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_active"]) -> FlowActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_deleted"]) -> FlowDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowdeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_standby"]) -> FlowStandbyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowStandby)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowstandbywaiter)
        """
