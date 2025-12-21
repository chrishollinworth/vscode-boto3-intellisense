"""
Type annotations for mediaconnect service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediaconnect.client import MediaConnectClient

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBridgesPaginator,
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListGatewayInstancesPaginator,
    ListGatewaysPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
    ListRouterInputsPaginator,
    ListRouterNetworkInterfacesPaginator,
    ListRouterOutputsPaginator,
)
from .type_defs import (
    AddBridgeOutputsRequestTypeDef,
    AddBridgeOutputsResponseTypeDef,
    AddBridgeSourcesRequestTypeDef,
    AddBridgeSourcesResponseTypeDef,
    AddFlowMediaStreamsRequestTypeDef,
    AddFlowMediaStreamsResponseTypeDef,
    AddFlowOutputsRequestTypeDef,
    AddFlowOutputsResponseTypeDef,
    AddFlowSourcesRequestTypeDef,
    AddFlowSourcesResponseTypeDef,
    AddFlowVpcInterfacesRequestTypeDef,
    AddFlowVpcInterfacesResponseTypeDef,
    BatchGetRouterInputRequestTypeDef,
    BatchGetRouterInputResponseTypeDef,
    BatchGetRouterNetworkInterfaceRequestTypeDef,
    BatchGetRouterNetworkInterfaceResponseTypeDef,
    BatchGetRouterOutputRequestTypeDef,
    BatchGetRouterOutputResponseTypeDef,
    CreateBridgeRequestTypeDef,
    CreateBridgeResponseTypeDef,
    CreateFlowRequestTypeDef,
    CreateFlowResponseTypeDef,
    CreateGatewayRequestTypeDef,
    CreateGatewayResponseTypeDef,
    CreateRouterInputRequestTypeDef,
    CreateRouterInputResponseTypeDef,
    CreateRouterNetworkInterfaceRequestTypeDef,
    CreateRouterNetworkInterfaceResponseTypeDef,
    CreateRouterOutputRequestTypeDef,
    CreateRouterOutputResponseTypeDef,
    DeleteBridgeRequestTypeDef,
    DeleteBridgeResponseTypeDef,
    DeleteFlowRequestTypeDef,
    DeleteFlowResponseTypeDef,
    DeleteGatewayRequestTypeDef,
    DeleteGatewayResponseTypeDef,
    DeleteRouterInputRequestTypeDef,
    DeleteRouterInputResponseTypeDef,
    DeleteRouterNetworkInterfaceRequestTypeDef,
    DeleteRouterNetworkInterfaceResponseTypeDef,
    DeleteRouterOutputRequestTypeDef,
    DeleteRouterOutputResponseTypeDef,
    DeregisterGatewayInstanceRequestTypeDef,
    DeregisterGatewayInstanceResponseTypeDef,
    DescribeBridgeRequestTypeDef,
    DescribeBridgeResponseTypeDef,
    DescribeFlowRequestTypeDef,
    DescribeFlowResponseTypeDef,
    DescribeFlowSourceMetadataRequestTypeDef,
    DescribeFlowSourceMetadataResponseTypeDef,
    DescribeFlowSourceThumbnailRequestTypeDef,
    DescribeFlowSourceThumbnailResponseTypeDef,
    DescribeGatewayInstanceRequestTypeDef,
    DescribeGatewayInstanceResponseTypeDef,
    DescribeGatewayRequestTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeOfferingRequestTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationRequestTypeDef,
    DescribeReservationResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetRouterInputRequestTypeDef,
    GetRouterInputResponseTypeDef,
    GetRouterInputSourceMetadataRequestTypeDef,
    GetRouterInputSourceMetadataResponseTypeDef,
    GetRouterInputThumbnailRequestTypeDef,
    GetRouterInputThumbnailResponseTypeDef,
    GetRouterNetworkInterfaceRequestTypeDef,
    GetRouterNetworkInterfaceResponseTypeDef,
    GetRouterOutputRequestTypeDef,
    GetRouterOutputResponseTypeDef,
    GrantFlowEntitlementsRequestTypeDef,
    GrantFlowEntitlementsResponseTypeDef,
    ListBridgesRequestTypeDef,
    ListBridgesResponseTypeDef,
    ListEntitlementsRequestTypeDef,
    ListEntitlementsResponseTypeDef,
    ListFlowsRequestTypeDef,
    ListFlowsResponseTypeDef,
    ListGatewayInstancesRequestTypeDef,
    ListGatewayInstancesResponseTypeDef,
    ListGatewaysRequestTypeDef,
    ListGatewaysResponseTypeDef,
    ListOfferingsRequestTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsRequestTypeDef,
    ListReservationsResponseTypeDef,
    ListRouterInputsRequestTypeDef,
    ListRouterInputsResponseTypeDef,
    ListRouterNetworkInterfacesRequestTypeDef,
    ListRouterNetworkInterfacesResponseTypeDef,
    ListRouterOutputsRequestTypeDef,
    ListRouterOutputsResponseTypeDef,
    ListTagsForGlobalResourceRequestTypeDef,
    ListTagsForGlobalResourceResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PurchaseOfferingRequestTypeDef,
    PurchaseOfferingResponseTypeDef,
    RemoveBridgeOutputRequestTypeDef,
    RemoveBridgeOutputResponseTypeDef,
    RemoveBridgeSourceRequestTypeDef,
    RemoveBridgeSourceResponseTypeDef,
    RemoveFlowMediaStreamRequestTypeDef,
    RemoveFlowMediaStreamResponseTypeDef,
    RemoveFlowOutputRequestTypeDef,
    RemoveFlowOutputResponseTypeDef,
    RemoveFlowSourceRequestTypeDef,
    RemoveFlowSourceResponseTypeDef,
    RemoveFlowVpcInterfaceRequestTypeDef,
    RemoveFlowVpcInterfaceResponseTypeDef,
    RestartRouterInputRequestTypeDef,
    RestartRouterInputResponseTypeDef,
    RestartRouterOutputRequestTypeDef,
    RestartRouterOutputResponseTypeDef,
    RevokeFlowEntitlementRequestTypeDef,
    RevokeFlowEntitlementResponseTypeDef,
    StartFlowRequestTypeDef,
    StartFlowResponseTypeDef,
    StartRouterInputRequestTypeDef,
    StartRouterInputResponseTypeDef,
    StartRouterOutputRequestTypeDef,
    StartRouterOutputResponseTypeDef,
    StopFlowRequestTypeDef,
    StopFlowResponseTypeDef,
    StopRouterInputRequestTypeDef,
    StopRouterInputResponseTypeDef,
    StopRouterOutputRequestTypeDef,
    StopRouterOutputResponseTypeDef,
    TagGlobalResourceRequestTypeDef,
    TagResourceRequestTypeDef,
    TakeRouterInputRequestTypeDef,
    TakeRouterInputResponseTypeDef,
    UntagGlobalResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBridgeOutputRequestTypeDef,
    UpdateBridgeOutputResponseTypeDef,
    UpdateBridgeRequestTypeDef,
    UpdateBridgeResponseTypeDef,
    UpdateBridgeSourceRequestTypeDef,
    UpdateBridgeSourceResponseTypeDef,
    UpdateBridgeStateRequestTypeDef,
    UpdateBridgeStateResponseTypeDef,
    UpdateFlowEntitlementRequestTypeDef,
    UpdateFlowEntitlementResponseTypeDef,
    UpdateFlowMediaStreamRequestTypeDef,
    UpdateFlowMediaStreamResponseTypeDef,
    UpdateFlowOutputRequestTypeDef,
    UpdateFlowOutputResponseTypeDef,
    UpdateFlowRequestTypeDef,
    UpdateFlowResponseTypeDef,
    UpdateFlowSourceRequestTypeDef,
    UpdateFlowSourceResponseTypeDef,
    UpdateGatewayInstanceRequestTypeDef,
    UpdateGatewayInstanceResponseTypeDef,
    UpdateRouterInputRequestTypeDef,
    UpdateRouterInputResponseTypeDef,
    UpdateRouterNetworkInterfaceRequestTypeDef,
    UpdateRouterNetworkInterfaceResponseTypeDef,
    UpdateRouterOutputRequestTypeDef,
    UpdateRouterOutputResponseTypeDef,
)
from .waiter import (
    FlowActiveWaiter,
    FlowDeletedWaiter,
    FlowStandbyWaiter,
    InputActiveWaiter,
    InputDeletedWaiter,
    InputStandbyWaiter,
    OutputActiveWaiter,
    OutputDeletedWaiter,
    OutputRoutedWaiter,
    OutputStandbyWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MediaConnectClient",)

class Exceptions(BaseClientExceptions):
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
    RouterInputServiceQuotaExceededException: Type[BotocoreClientError]
    RouterNetworkInterfaceServiceQuotaExceededException: Type[BotocoreClientError]
    RouterOutputServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class MediaConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#generate_presigned_url)
        """

    def add_bridge_outputs(
        self, **kwargs: Unpack[AddBridgeOutputsRequestTypeDef]
    ) -> AddBridgeOutputsResponseTypeDef:
        """
        Adds outputs to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_bridge_outputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_bridge_outputs)
        """

    def add_bridge_sources(
        self, **kwargs: Unpack[AddBridgeSourcesRequestTypeDef]
    ) -> AddBridgeSourcesResponseTypeDef:
        """
        Adds sources to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_bridge_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_bridge_sources)
        """

    def add_flow_media_streams(
        self, **kwargs: Unpack[AddFlowMediaStreamsRequestTypeDef]
    ) -> AddFlowMediaStreamsResponseTypeDef:
        """
        Adds media streams to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_flow_media_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_flow_media_streams)
        """

    def add_flow_outputs(
        self, **kwargs: Unpack[AddFlowOutputsRequestTypeDef]
    ) -> AddFlowOutputsResponseTypeDef:
        """
        Adds outputs to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_flow_outputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_flow_outputs)
        """

    def add_flow_sources(
        self, **kwargs: Unpack[AddFlowSourcesRequestTypeDef]
    ) -> AddFlowSourcesResponseTypeDef:
        """
        Adds sources to a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_flow_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_flow_sources)
        """

    def add_flow_vpc_interfaces(
        self, **kwargs: Unpack[AddFlowVpcInterfacesRequestTypeDef]
    ) -> AddFlowVpcInterfacesResponseTypeDef:
        """
        Adds VPC interfaces to a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/add_flow_vpc_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#add_flow_vpc_interfaces)
        """

    def batch_get_router_input(
        self, **kwargs: Unpack[BatchGetRouterInputRequestTypeDef]
    ) -> BatchGetRouterInputResponseTypeDef:
        """
        Retrieves information about multiple router inputs in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/batch_get_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#batch_get_router_input)
        """

    def batch_get_router_network_interface(
        self, **kwargs: Unpack[BatchGetRouterNetworkInterfaceRequestTypeDef]
    ) -> BatchGetRouterNetworkInterfaceResponseTypeDef:
        """
        Retrieves information about multiple router network interfaces in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/batch_get_router_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#batch_get_router_network_interface)
        """

    def batch_get_router_output(
        self, **kwargs: Unpack[BatchGetRouterOutputRequestTypeDef]
    ) -> BatchGetRouterOutputResponseTypeDef:
        """
        Retrieves information about multiple router outputs in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/batch_get_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#batch_get_router_output)
        """

    def create_bridge(
        self, **kwargs: Unpack[CreateBridgeRequestTypeDef]
    ) -> CreateBridgeResponseTypeDef:
        """
        Creates a new bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_bridge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_bridge)
        """

    def create_flow(self, **kwargs: Unpack[CreateFlowRequestTypeDef]) -> CreateFlowResponseTypeDef:
        """
        Creates a new flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_flow)
        """

    def create_gateway(
        self, **kwargs: Unpack[CreateGatewayRequestTypeDef]
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a new gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_gateway)
        """

    def create_router_input(
        self, **kwargs: Unpack[CreateRouterInputRequestTypeDef]
    ) -> CreateRouterInputResponseTypeDef:
        """
        Creates a new router input in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_router_input)
        """

    def create_router_network_interface(
        self, **kwargs: Unpack[CreateRouterNetworkInterfaceRequestTypeDef]
    ) -> CreateRouterNetworkInterfaceResponseTypeDef:
        """
        Creates a new router network interface in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_router_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_router_network_interface)
        """

    def create_router_output(
        self, **kwargs: Unpack[CreateRouterOutputRequestTypeDef]
    ) -> CreateRouterOutputResponseTypeDef:
        """
        Creates a new router output in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/create_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#create_router_output)
        """

    def delete_bridge(
        self, **kwargs: Unpack[DeleteBridgeRequestTypeDef]
    ) -> DeleteBridgeResponseTypeDef:
        """
        Deletes a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_bridge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_bridge)
        """

    def delete_flow(self, **kwargs: Unpack[DeleteFlowRequestTypeDef]) -> DeleteFlowResponseTypeDef:
        """
        Deletes a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_flow)
        """

    def delete_gateway(
        self, **kwargs: Unpack[DeleteGatewayRequestTypeDef]
    ) -> DeleteGatewayResponseTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_gateway)
        """

    def delete_router_input(
        self, **kwargs: Unpack[DeleteRouterInputRequestTypeDef]
    ) -> DeleteRouterInputResponseTypeDef:
        """
        Deletes a router input from AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_router_input)
        """

    def delete_router_network_interface(
        self, **kwargs: Unpack[DeleteRouterNetworkInterfaceRequestTypeDef]
    ) -> DeleteRouterNetworkInterfaceResponseTypeDef:
        """
        Deletes a router network interface from AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_router_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_router_network_interface)
        """

    def delete_router_output(
        self, **kwargs: Unpack[DeleteRouterOutputRequestTypeDef]
    ) -> DeleteRouterOutputResponseTypeDef:
        """
        Deletes a router output from AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/delete_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#delete_router_output)
        """

    def deregister_gateway_instance(
        self, **kwargs: Unpack[DeregisterGatewayInstanceRequestTypeDef]
    ) -> DeregisterGatewayInstanceResponseTypeDef:
        """
        Deregisters an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/deregister_gateway_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#deregister_gateway_instance)
        """

    def describe_bridge(
        self, **kwargs: Unpack[DescribeBridgeRequestTypeDef]
    ) -> DescribeBridgeResponseTypeDef:
        """
        Displays the details of a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_bridge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_bridge)
        """

    def describe_flow(
        self, **kwargs: Unpack[DescribeFlowRequestTypeDef]
    ) -> DescribeFlowResponseTypeDef:
        """
        Displays the details of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_flow)
        """

    def describe_flow_source_metadata(
        self, **kwargs: Unpack[DescribeFlowSourceMetadataRequestTypeDef]
    ) -> DescribeFlowSourceMetadataResponseTypeDef:
        """
        The <code>DescribeFlowSourceMetadata</code> API is used to view information
        about the flow's source transport stream and programs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_flow_source_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_flow_source_metadata)
        """

    def describe_flow_source_thumbnail(
        self, **kwargs: Unpack[DescribeFlowSourceThumbnailRequestTypeDef]
    ) -> DescribeFlowSourceThumbnailResponseTypeDef:
        """
        Describes the thumbnail for the flow source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_flow_source_thumbnail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_flow_source_thumbnail)
        """

    def describe_gateway(
        self, **kwargs: Unpack[DescribeGatewayRequestTypeDef]
    ) -> DescribeGatewayResponseTypeDef:
        """
        Displays the details of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_gateway)
        """

    def describe_gateway_instance(
        self, **kwargs: Unpack[DescribeGatewayInstanceRequestTypeDef]
    ) -> DescribeGatewayInstanceResponseTypeDef:
        """
        Displays the details of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_gateway_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_gateway_instance)
        """

    def describe_offering(
        self, **kwargs: Unpack[DescribeOfferingRequestTypeDef]
    ) -> DescribeOfferingResponseTypeDef:
        """
        Displays the details of an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_offering)
        """

    def describe_reservation(
        self, **kwargs: Unpack[DescribeReservationRequestTypeDef]
    ) -> DescribeReservationResponseTypeDef:
        """
        Displays the details of a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/describe_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#describe_reservation)
        """

    def get_router_input(
        self, **kwargs: Unpack[GetRouterInputRequestTypeDef]
    ) -> GetRouterInputResponseTypeDef:
        """
        Retrieves information about a specific router input in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_router_input)
        """

    def get_router_input_source_metadata(
        self, **kwargs: Unpack[GetRouterInputSourceMetadataRequestTypeDef]
    ) -> GetRouterInputSourceMetadataResponseTypeDef:
        """
        Retrieves detailed metadata information about a specific router input source,
        including stream details and connection state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_router_input_source_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_router_input_source_metadata)
        """

    def get_router_input_thumbnail(
        self, **kwargs: Unpack[GetRouterInputThumbnailRequestTypeDef]
    ) -> GetRouterInputThumbnailResponseTypeDef:
        """
        Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_router_input_thumbnail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_router_input_thumbnail)
        """

    def get_router_network_interface(
        self, **kwargs: Unpack[GetRouterNetworkInterfaceRequestTypeDef]
    ) -> GetRouterNetworkInterfaceResponseTypeDef:
        """
        Retrieves information about a specific router network interface in AWS
        Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_router_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_router_network_interface)
        """

    def get_router_output(
        self, **kwargs: Unpack[GetRouterOutputRequestTypeDef]
    ) -> GetRouterOutputResponseTypeDef:
        """
        Retrieves information about a specific router output in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_router_output)
        """

    def grant_flow_entitlements(
        self, **kwargs: Unpack[GrantFlowEntitlementsRequestTypeDef]
    ) -> GrantFlowEntitlementsResponseTypeDef:
        """
        Grants entitlements to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/grant_flow_entitlements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#grant_flow_entitlements)
        """

    def list_bridges(
        self, **kwargs: Unpack[ListBridgesRequestTypeDef]
    ) -> ListBridgesResponseTypeDef:
        """
        Displays a list of bridges that are associated with this account and an
        optionally specified Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_bridges.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_bridges)
        """

    def list_entitlements(
        self, **kwargs: Unpack[ListEntitlementsRequestTypeDef]
    ) -> ListEntitlementsResponseTypeDef:
        """
        Displays a list of all entitlements that have been granted to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_entitlements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_entitlements)
        """

    def list_flows(self, **kwargs: Unpack[ListFlowsRequestTypeDef]) -> ListFlowsResponseTypeDef:
        """
        Displays a list of flows that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_flows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_flows)
        """

    def list_gateway_instances(
        self, **kwargs: Unpack[ListGatewayInstancesRequestTypeDef]
    ) -> ListGatewayInstancesResponseTypeDef:
        """
        Displays a list of instances associated with the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_gateway_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_gateway_instances)
        """

    def list_gateways(
        self, **kwargs: Unpack[ListGatewaysRequestTypeDef]
    ) -> ListGatewaysResponseTypeDef:
        """
        Displays a list of gateways that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_gateways)
        """

    def list_offerings(
        self, **kwargs: Unpack[ListOfferingsRequestTypeDef]
    ) -> ListOfferingsResponseTypeDef:
        """
        Displays a list of all offerings that are available to this account in the
        current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_offerings)
        """

    def list_reservations(
        self, **kwargs: Unpack[ListReservationsRequestTypeDef]
    ) -> ListReservationsResponseTypeDef:
        """
        Displays a list of all reservations that have been purchased by this account in
        the current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_reservations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_reservations)
        """

    def list_router_inputs(
        self, **kwargs: Unpack[ListRouterInputsRequestTypeDef]
    ) -> ListRouterInputsResponseTypeDef:
        """
        Retrieves a list of router inputs in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_router_inputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_router_inputs)
        """

    def list_router_network_interfaces(
        self, **kwargs: Unpack[ListRouterNetworkInterfacesRequestTypeDef]
    ) -> ListRouterNetworkInterfacesResponseTypeDef:
        """
        Retrieves a list of router network interfaces in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_router_network_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_router_network_interfaces)
        """

    def list_router_outputs(
        self, **kwargs: Unpack[ListRouterOutputsRequestTypeDef]
    ) -> ListRouterOutputsResponseTypeDef:
        """
        Retrieves a list of router outputs in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_router_outputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_router_outputs)
        """

    def list_tags_for_global_resource(
        self, **kwargs: Unpack[ListTagsForGlobalResourceRequestTypeDef]
    ) -> ListTagsForGlobalResourceResponseTypeDef:
        """
        Lists the tags associated with a global resource in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_tags_for_global_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_tags_for_global_resource)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags on a MediaConnect resource in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#list_tags_for_resource)
        """

    def purchase_offering(
        self, **kwargs: Unpack[PurchaseOfferingRequestTypeDef]
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Submits a request to purchase an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/purchase_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#purchase_offering)
        """

    def remove_bridge_output(
        self, **kwargs: Unpack[RemoveBridgeOutputRequestTypeDef]
    ) -> RemoveBridgeOutputResponseTypeDef:
        """
        Removes an output from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_bridge_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_bridge_output)
        """

    def remove_bridge_source(
        self, **kwargs: Unpack[RemoveBridgeSourceRequestTypeDef]
    ) -> RemoveBridgeSourceResponseTypeDef:
        """
        Removes a source from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_bridge_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_bridge_source)
        """

    def remove_flow_media_stream(
        self, **kwargs: Unpack[RemoveFlowMediaStreamRequestTypeDef]
    ) -> RemoveFlowMediaStreamResponseTypeDef:
        """
        Removes a media stream from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_flow_media_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_flow_media_stream)
        """

    def remove_flow_output(
        self, **kwargs: Unpack[RemoveFlowOutputRequestTypeDef]
    ) -> RemoveFlowOutputResponseTypeDef:
        """
        Removes an output from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_flow_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_flow_output)
        """

    def remove_flow_source(
        self, **kwargs: Unpack[RemoveFlowSourceRequestTypeDef]
    ) -> RemoveFlowSourceResponseTypeDef:
        """
        Removes a source from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_flow_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_flow_source)
        """

    def remove_flow_vpc_interface(
        self, **kwargs: Unpack[RemoveFlowVpcInterfaceRequestTypeDef]
    ) -> RemoveFlowVpcInterfaceResponseTypeDef:
        """
        Removes a VPC Interface from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/remove_flow_vpc_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#remove_flow_vpc_interface)
        """

    def restart_router_input(
        self, **kwargs: Unpack[RestartRouterInputRequestTypeDef]
    ) -> RestartRouterInputResponseTypeDef:
        """
        Restarts a router input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/restart_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#restart_router_input)
        """

    def restart_router_output(
        self, **kwargs: Unpack[RestartRouterOutputRequestTypeDef]
    ) -> RestartRouterOutputResponseTypeDef:
        """
        Restarts a router output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/restart_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#restart_router_output)
        """

    def revoke_flow_entitlement(
        self, **kwargs: Unpack[RevokeFlowEntitlementRequestTypeDef]
    ) -> RevokeFlowEntitlementResponseTypeDef:
        """
        Revokes an entitlement from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/revoke_flow_entitlement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#revoke_flow_entitlement)
        """

    def start_flow(self, **kwargs: Unpack[StartFlowRequestTypeDef]) -> StartFlowResponseTypeDef:
        """
        Starts a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/start_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#start_flow)
        """

    def start_router_input(
        self, **kwargs: Unpack[StartRouterInputRequestTypeDef]
    ) -> StartRouterInputResponseTypeDef:
        """
        Starts a router input in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/start_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#start_router_input)
        """

    def start_router_output(
        self, **kwargs: Unpack[StartRouterOutputRequestTypeDef]
    ) -> StartRouterOutputResponseTypeDef:
        """
        Starts a router output in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/start_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#start_router_output)
        """

    def stop_flow(self, **kwargs: Unpack[StopFlowRequestTypeDef]) -> StopFlowResponseTypeDef:
        """
        Stops a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/stop_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#stop_flow)
        """

    def stop_router_input(
        self, **kwargs: Unpack[StopRouterInputRequestTypeDef]
    ) -> StopRouterInputResponseTypeDef:
        """
        Stops a router input in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/stop_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#stop_router_input)
        """

    def stop_router_output(
        self, **kwargs: Unpack[StopRouterOutputRequestTypeDef]
    ) -> StopRouterOutputResponseTypeDef:
        """
        Stops a router output in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/stop_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#stop_router_output)
        """

    def tag_global_resource(
        self, **kwargs: Unpack[TagGlobalResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to a global resource in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/tag_global_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#tag_global_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code> in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#tag_resource)
        """

    def take_router_input(
        self, **kwargs: Unpack[TakeRouterInputRequestTypeDef]
    ) -> TakeRouterInputResponseTypeDef:
        """
        Associates a router input with a router output in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/take_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#take_router_input)
        """

    def untag_global_resource(
        self, **kwargs: Unpack[UntagGlobalResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from a global resource in AWS Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/untag_global_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#untag_global_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes specified tags from a resource in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#untag_resource)
        """

    def update_bridge(
        self, **kwargs: Unpack[UpdateBridgeRequestTypeDef]
    ) -> UpdateBridgeResponseTypeDef:
        """
        Updates the bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_bridge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_bridge)
        """

    def update_bridge_output(
        self, **kwargs: Unpack[UpdateBridgeOutputRequestTypeDef]
    ) -> UpdateBridgeOutputResponseTypeDef:
        """
        Updates an existing bridge output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_bridge_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_bridge_output)
        """

    def update_bridge_source(
        self, **kwargs: Unpack[UpdateBridgeSourceRequestTypeDef]
    ) -> UpdateBridgeSourceResponseTypeDef:
        """
        Updates an existing bridge source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_bridge_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_bridge_source)
        """

    def update_bridge_state(
        self, **kwargs: Unpack[UpdateBridgeStateRequestTypeDef]
    ) -> UpdateBridgeStateResponseTypeDef:
        """
        Updates the bridge state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_bridge_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_bridge_state)
        """

    def update_flow(self, **kwargs: Unpack[UpdateFlowRequestTypeDef]) -> UpdateFlowResponseTypeDef:
        """
        Updates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_flow)
        """

    def update_flow_entitlement(
        self, **kwargs: Unpack[UpdateFlowEntitlementRequestTypeDef]
    ) -> UpdateFlowEntitlementResponseTypeDef:
        """
        Updates an entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_flow_entitlement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_flow_entitlement)
        """

    def update_flow_media_stream(
        self, **kwargs: Unpack[UpdateFlowMediaStreamRequestTypeDef]
    ) -> UpdateFlowMediaStreamResponseTypeDef:
        """
        Updates an existing media stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_flow_media_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_flow_media_stream)
        """

    def update_flow_output(
        self, **kwargs: Unpack[UpdateFlowOutputRequestTypeDef]
    ) -> UpdateFlowOutputResponseTypeDef:
        """
        Updates an existing flow output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_flow_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_flow_output)
        """

    def update_flow_source(
        self, **kwargs: Unpack[UpdateFlowSourceRequestTypeDef]
    ) -> UpdateFlowSourceResponseTypeDef:
        """
        Updates the source of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_flow_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_flow_source)
        """

    def update_gateway_instance(
        self, **kwargs: Unpack[UpdateGatewayInstanceRequestTypeDef]
    ) -> UpdateGatewayInstanceResponseTypeDef:
        """
        Updates an existing gateway instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_gateway_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_gateway_instance)
        """

    def update_router_input(
        self, **kwargs: Unpack[UpdateRouterInputRequestTypeDef]
    ) -> UpdateRouterInputResponseTypeDef:
        """
        Updates the configuration of an existing router input in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_router_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_router_input)
        """

    def update_router_network_interface(
        self, **kwargs: Unpack[UpdateRouterNetworkInterfaceRequestTypeDef]
    ) -> UpdateRouterNetworkInterfaceResponseTypeDef:
        """
        Updates the configuration of an existing router network interface in AWS
        Elemental MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_router_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_router_network_interface)
        """

    def update_router_output(
        self, **kwargs: Unpack[UpdateRouterOutputRequestTypeDef]
    ) -> UpdateRouterOutputResponseTypeDef:
        """
        Updates the configuration of an existing router output in AWS Elemental
        MediaConnect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/update_router_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#update_router_output)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bridges"]
    ) -> ListBridgesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entitlements"]
    ) -> ListEntitlementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flows"]
    ) -> ListFlowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateway_instances"]
    ) -> ListGatewayInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateways"]
    ) -> ListGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_offerings"]
    ) -> ListOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_router_inputs"]
    ) -> ListRouterInputsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_router_network_interfaces"]
    ) -> ListRouterNetworkInterfacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_router_outputs"]
    ) -> ListRouterOutputsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["flow_active"]
    ) -> FlowActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["flow_deleted"]
    ) -> FlowDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["flow_standby"]
    ) -> FlowStandbyWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_active"]
    ) -> InputActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_deleted"]
    ) -> InputDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_standby"]
    ) -> InputStandbyWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["output_active"]
    ) -> OutputActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["output_deleted"]
    ) -> OutputDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["output_routed"]
    ) -> OutputRoutedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["output_standby"]
    ) -> OutputStandbyWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#get_waiter)
        """
