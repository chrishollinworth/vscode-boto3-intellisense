# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediaconnect service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediaconnect import MediaConnectClient

    client: MediaConnectClient = boto3.client("mediaconnect")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_mediaconnect.paginator import (
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from mypy_boto3_mediaconnect.type_defs import (
    AddFlowOutputsResponseTypeDef,
    AddFlowSourcesResponseTypeDef,
    AddFlowVpcInterfacesResponseTypeDef,
    AddOutputRequestTypeDef,
    CreateFlowResponseTypeDef,
    DeleteFlowResponseTypeDef,
    DescribeFlowResponseTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationResponseTypeDef,
    FailoverConfigTypeDef,
    GrantEntitlementRequestTypeDef,
    GrantFlowEntitlementsResponseTypeDef,
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PurchaseOfferingResponseTypeDef,
    RemoveFlowOutputResponseTypeDef,
    RemoveFlowSourceResponseTypeDef,
    RemoveFlowVpcInterfaceResponseTypeDef,
    RevokeFlowEntitlementResponseTypeDef,
    SetSourceRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowResponseTypeDef,
    UpdateEncryptionTypeDef,
    UpdateFailoverConfigTypeDef,
    UpdateFlowEntitlementResponseTypeDef,
    UpdateFlowOutputResponseTypeDef,
    UpdateFlowResponseTypeDef,
    UpdateFlowSourceResponseTypeDef,
    VpcInterfaceAttachmentTypeDef,
    VpcInterfaceRequestTypeDef,
)

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
    CreateFlow420Exception: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GrantFlowEntitlements420Exception: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class MediaConnectClient:
    """
    [MediaConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_flow_outputs(
        self, FlowArn: str, Outputs: List[AddOutputRequestTypeDef]
    ) -> AddFlowOutputsResponseTypeDef:
        """
        [Client.add_flow_outputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_outputs)
        """

    def add_flow_sources(
        self, FlowArn: str, Sources: List[SetSourceRequestTypeDef]
    ) -> AddFlowSourcesResponseTypeDef:
        """
        [Client.add_flow_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_sources)
        """

    def add_flow_vpc_interfaces(
        self, FlowArn: str, VpcInterfaces: List[VpcInterfaceRequestTypeDef]
    ) -> AddFlowVpcInterfacesResponseTypeDef:
        """
        [Client.add_flow_vpc_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_vpc_interfaces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.can_paginate)
        """

    def create_flow(
        self,
        Name: str,
        AvailabilityZone: str = None,
        Entitlements: List[GrantEntitlementRequestTypeDef] = None,
        Outputs: List[AddOutputRequestTypeDef] = None,
        Source: SetSourceRequestTypeDef = None,
        SourceFailoverConfig: "FailoverConfigTypeDef" = None,
        Sources: List[SetSourceRequestTypeDef] = None,
        VpcInterfaces: List[VpcInterfaceRequestTypeDef] = None,
    ) -> CreateFlowResponseTypeDef:
        """
        [Client.create_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.create_flow)
        """

    def delete_flow(self, FlowArn: str) -> DeleteFlowResponseTypeDef:
        """
        [Client.delete_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.delete_flow)
        """

    def describe_flow(self, FlowArn: str) -> DescribeFlowResponseTypeDef:
        """
        [Client.describe_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow)
        """

    def describe_offering(self, OfferingArn: str) -> DescribeOfferingResponseTypeDef:
        """
        [Client.describe_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.describe_offering)
        """

    def describe_reservation(self, ReservationArn: str) -> DescribeReservationResponseTypeDef:
        """
        [Client.describe_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.describe_reservation)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.generate_presigned_url)
        """

    def grant_flow_entitlements(
        self, Entitlements: List[GrantEntitlementRequestTypeDef], FlowArn: str
    ) -> GrantFlowEntitlementsResponseTypeDef:
        """
        [Client.grant_flow_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.grant_flow_entitlements)
        """

    def list_entitlements(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListEntitlementsResponseTypeDef:
        """
        [Client.list_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.list_entitlements)
        """

    def list_flows(self, MaxResults: int = None, NextToken: str = None) -> ListFlowsResponseTypeDef:
        """
        [Client.list_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.list_flows)
        """

    def list_offerings(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListOfferingsResponseTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.list_offerings)
        """

    def list_reservations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListReservationsResponseTypeDef:
        """
        [Client.list_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.list_reservations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.list_tags_for_resource)
        """

    def purchase_offering(
        self, OfferingArn: str, ReservationName: str, Start: str
    ) -> PurchaseOfferingResponseTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.purchase_offering)
        """

    def remove_flow_output(self, FlowArn: str, OutputArn: str) -> RemoveFlowOutputResponseTypeDef:
        """
        [Client.remove_flow_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_output)
        """

    def remove_flow_source(self, FlowArn: str, SourceArn: str) -> RemoveFlowSourceResponseTypeDef:
        """
        [Client.remove_flow_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_source)
        """

    def remove_flow_vpc_interface(
        self, FlowArn: str, VpcInterfaceName: str
    ) -> RemoveFlowVpcInterfaceResponseTypeDef:
        """
        [Client.remove_flow_vpc_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_vpc_interface)
        """

    def revoke_flow_entitlement(
        self, EntitlementArn: str, FlowArn: str
    ) -> RevokeFlowEntitlementResponseTypeDef:
        """
        [Client.revoke_flow_entitlement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.revoke_flow_entitlement)
        """

    def start_flow(self, FlowArn: str) -> StartFlowResponseTypeDef:
        """
        [Client.start_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.start_flow)
        """

    def stop_flow(self, FlowArn: str) -> StopFlowResponseTypeDef:
        """
        [Client.stop_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.stop_flow)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.untag_resource)
        """

    def update_flow(
        self, FlowArn: str, SourceFailoverConfig: UpdateFailoverConfigTypeDef = None
    ) -> UpdateFlowResponseTypeDef:
        """
        [Client.update_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.update_flow)
        """

    def update_flow_entitlement(
        self,
        EntitlementArn: str,
        FlowArn: str,
        Description: str = None,
        Encryption: UpdateEncryptionTypeDef = None,
        EntitlementStatus: Literal["ENABLED", "DISABLED"] = None,
        Subscribers: List[str] = None,
    ) -> UpdateFlowEntitlementResponseTypeDef:
        """
        [Client.update_flow_entitlement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_entitlement)
        """

    def update_flow_output(
        self,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: List[str] = None,
        Description: str = None,
        Destination: str = None,
        Encryption: UpdateEncryptionTypeDef = None,
        MaxLatency: int = None,
        Port: int = None,
        Protocol: Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"] = None,
        RemoteId: str = None,
        SmoothingLatency: int = None,
        StreamId: str = None,
        VpcInterfaceAttachment: "VpcInterfaceAttachmentTypeDef" = None,
    ) -> UpdateFlowOutputResponseTypeDef:
        """
        [Client.update_flow_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_output)
        """

    def update_flow_source(
        self,
        FlowArn: str,
        SourceArn: str,
        Decryption: UpdateEncryptionTypeDef = None,
        Description: str = None,
        EntitlementArn: str = None,
        IngestPort: int = None,
        MaxBitrate: int = None,
        MaxLatency: int = None,
        Protocol: Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"] = None,
        StreamId: str = None,
        VpcInterfaceName: str = None,
        WhitelistCidr: str = None,
    ) -> UpdateFlowSourceResponseTypeDef:
        """
        [Client.update_flow_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_source)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entitlements"]
    ) -> ListEntitlementsPaginator:
        """
        [Paginator.ListEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_flows"]) -> ListFlowsPaginator:
        """
        [Paginator.ListFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListReservations)
        """
