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
    CreateBridgeRequestTypeDef,
    CreateBridgeResponseTypeDef,
    CreateFlowRequestTypeDef,
    CreateFlowResponseTypeDef,
    CreateGatewayRequestTypeDef,
    CreateGatewayResponseTypeDef,
    DeleteBridgeRequestTypeDef,
    DeleteBridgeResponseTypeDef,
    DeleteFlowRequestTypeDef,
    DeleteFlowResponseTypeDef,
    DeleteGatewayRequestTypeDef,
    DeleteGatewayResponseTypeDef,
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
    RevokeFlowEntitlementRequestTypeDef,
    RevokeFlowEntitlementResponseTypeDef,
    StartFlowRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowRequestTypeDef,
    StopFlowResponseTypeDef,
    TagResourceRequestTypeDef,
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
)
from .waiter import FlowActiveWaiter, FlowDeletedWaiter, FlowStandbyWaiter

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

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags on a MediaConnect resource.

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

    def stop_flow(self, **kwargs: Unpack[StopFlowRequestTypeDef]) -> StopFlowResponseTypeDef:
        """
        Stops a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/stop_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#stop_flow)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes specified tags from a resource.

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
