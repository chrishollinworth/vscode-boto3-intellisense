"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddBridgeFlowSourceRequestTypeDef

    data: AddBridgeFlowSourceRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AlgorithmType,
    BridgePlacementType,
    BridgeStateType,
    ColorimetryType,
    ConnectionStatusType,
    DesiredStateType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverModeType,
    GatewayStateType,
    InstanceStateType,
    KeyTypeType,
    MaintenanceDayType,
    MediaStreamTypeType,
    NetworkInterfaceTypeType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddBridgeFlowSourceRequestTypeDef",
    "AddBridgeNetworkOutputRequestTypeDef",
    "AddBridgeNetworkSourceRequestTypeDef",
    "AddBridgeOutputRequestTypeDef",
    "AddBridgeOutputsRequestRequestTypeDef",
    "AddBridgeOutputsResponseTypeDef",
    "AddBridgeSourceRequestTypeDef",
    "AddBridgeSourcesRequestRequestTypeDef",
    "AddBridgeSourcesResponseTypeDef",
    "AddEgressGatewayBridgeRequestTypeDef",
    "AddFlowMediaStreamsRequestRequestTypeDef",
    "AddFlowMediaStreamsResponseTypeDef",
    "AddFlowOutputsRequestRequestTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesRequestRequestTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddIngressGatewayBridgeRequestTypeDef",
    "AddMaintenanceTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "BridgeFlowOutputTypeDef",
    "BridgeFlowSourceTypeDef",
    "BridgeNetworkOutputTypeDef",
    "BridgeNetworkSourceTypeDef",
    "BridgeOutputTypeDef",
    "BridgeSourceTypeDef",
    "BridgeTypeDef",
    "CreateBridgeRequestRequestTypeDef",
    "CreateBridgeResponseTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CreateGatewayRequestRequestTypeDef",
    "CreateGatewayResponseTypeDef",
    "DeleteBridgeRequestRequestTypeDef",
    "DeleteBridgeResponseTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DeleteFlowResponseTypeDef",
    "DeleteGatewayRequestRequestTypeDef",
    "DeleteGatewayResponseTypeDef",
    "DeregisterGatewayInstanceRequestRequestTypeDef",
    "DeregisterGatewayInstanceResponseTypeDef",
    "DescribeBridgeRequestRequestTypeDef",
    "DescribeBridgeResponseTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeFlowSourceMetadataRequestRequestTypeDef",
    "DescribeFlowSourceMetadataResponseTypeDef",
    "DescribeGatewayInstanceRequestRequestTypeDef",
    "DescribeGatewayInstanceResponseTypeDef",
    "DescribeGatewayRequestRequestTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EgressGatewayBridgeTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "FrameResolutionTypeDef",
    "GatewayBridgeSourceTypeDef",
    "GatewayInstanceTypeDef",
    "GatewayNetworkTypeDef",
    "GatewayTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsRequestRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "IngressGatewayBridgeTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListBridgesRequestRequestTypeDef",
    "ListBridgesResponseTypeDef",
    "ListEntitlementsRequestRequestTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListGatewayInstancesRequestRequestTypeDef",
    "ListGatewayInstancesResponseTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedBridgeTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "ListedGatewayInstanceTypeDef",
    "ListedGatewayTypeDef",
    "MaintenanceTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "MediaStreamTypeDef",
    "MessageDetailTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveBridgeOutputRequestRequestTypeDef",
    "RemoveBridgeOutputResponseTypeDef",
    "RemoveBridgeSourceRequestRequestTypeDef",
    "RemoveBridgeSourceResponseTypeDef",
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputRequestRequestTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceRequestRequestTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeFlowEntitlementRequestRequestTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetGatewayBridgeSourceRequestTypeDef",
    "SetSourceRequestTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TransportMediaInfoTypeDef",
    "TransportStreamProgramTypeDef",
    "TransportStreamTypeDef",
    "TransportTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBridgeFlowSourceRequestTypeDef",
    "UpdateBridgeNetworkOutputRequestTypeDef",
    "UpdateBridgeNetworkSourceRequestTypeDef",
    "UpdateBridgeOutputRequestRequestTypeDef",
    "UpdateBridgeOutputResponseTypeDef",
    "UpdateBridgeRequestRequestTypeDef",
    "UpdateBridgeResponseTypeDef",
    "UpdateBridgeSourceRequestRequestTypeDef",
    "UpdateBridgeSourceResponseTypeDef",
    "UpdateBridgeStateRequestRequestTypeDef",
    "UpdateBridgeStateResponseTypeDef",
    "UpdateEgressGatewayBridgeRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementRequestRequestTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "UpdateFlowOutputRequestRequestTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceRequestRequestTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "UpdateGatewayBridgeSourceRequestTypeDef",
    "UpdateGatewayInstanceRequestRequestTypeDef",
    "UpdateGatewayInstanceResponseTypeDef",
    "UpdateIngressGatewayBridgeRequestTypeDef",
    "UpdateMaintenanceTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddBridgeFlowSourceRequestTypeDef = TypedDict(
    "_RequiredAddBridgeFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "Name": str,
    },
)
_OptionalAddBridgeFlowSourceRequestTypeDef = TypedDict(
    "_OptionalAddBridgeFlowSourceRequestTypeDef",
    {
        "FlowVpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class AddBridgeFlowSourceRequestTypeDef(
    _RequiredAddBridgeFlowSourceRequestTypeDef, _OptionalAddBridgeFlowSourceRequestTypeDef
):
    pass

AddBridgeNetworkOutputRequestTypeDef = TypedDict(
    "AddBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)

AddBridgeNetworkSourceRequestTypeDef = TypedDict(
    "AddBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
    },
)

AddBridgeOutputRequestTypeDef = TypedDict(
    "AddBridgeOutputRequestTypeDef",
    {
        "NetworkOutput": "AddBridgeNetworkOutputRequestTypeDef",
    },
    total=False,
)

AddBridgeOutputsRequestRequestTypeDef = TypedDict(
    "AddBridgeOutputsRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "Outputs": List["AddBridgeOutputRequestTypeDef"],
    },
)

AddBridgeOutputsResponseTypeDef = TypedDict(
    "AddBridgeOutputsResponseTypeDef",
    {
        "BridgeArn": str,
        "Outputs": List["BridgeOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddBridgeSourceRequestTypeDef = TypedDict(
    "AddBridgeSourceRequestTypeDef",
    {
        "FlowSource": "AddBridgeFlowSourceRequestTypeDef",
        "NetworkSource": "AddBridgeNetworkSourceRequestTypeDef",
    },
    total=False,
)

AddBridgeSourcesRequestRequestTypeDef = TypedDict(
    "AddBridgeSourcesRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "Sources": List["AddBridgeSourceRequestTypeDef"],
    },
)

AddBridgeSourcesResponseTypeDef = TypedDict(
    "AddBridgeSourcesResponseTypeDef",
    {
        "BridgeArn": str,
        "Sources": List["BridgeSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddEgressGatewayBridgeRequestTypeDef = TypedDict(
    "AddEgressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
    },
)

AddFlowMediaStreamsRequestRequestTypeDef = TypedDict(
    "AddFlowMediaStreamsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
    },
)

AddFlowMediaStreamsResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowOutputsRequestRequestTypeDef = TypedDict(
    "AddFlowOutputsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["AddOutputRequestTypeDef"],
    },
)

AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowSourcesRequestRequestTypeDef = TypedDict(
    "AddFlowSourcesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SetSourceRequestTypeDef"],
    },
)

AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowVpcInterfacesRequestRequestTypeDef = TypedDict(
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
    },
)

AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddIngressGatewayBridgeRequestTypeDef = TypedDict(
    "AddIngressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
        "MaxOutputs": int,
    },
)

AddMaintenanceTypeDef = TypedDict(
    "AddMaintenanceTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceStartHour": str,
    },
)

_RequiredAddMediaStreamRequestTypeDef = TypedDict(
    "_RequiredAddMediaStreamRequestTypeDef",
    {
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalAddMediaStreamRequestTypeDef = TypedDict(
    "_OptionalAddMediaStreamRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)

class AddMediaStreamRequestTypeDef(
    _RequiredAddMediaStreamRequestTypeDef, _OptionalAddMediaStreamRequestTypeDef
):
    pass

_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SenderControlPort": int,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class AddOutputRequestTypeDef(_RequiredAddOutputRequestTypeDef, _OptionalAddOutputRequestTypeDef):
    pass

BridgeFlowOutputTypeDef = TypedDict(
    "BridgeFlowOutputTypeDef",
    {
        "FlowArn": str,
        "FlowSourceArn": str,
        "Name": str,
    },
)

_RequiredBridgeFlowSourceTypeDef = TypedDict(
    "_RequiredBridgeFlowSourceTypeDef",
    {
        "FlowArn": str,
        "Name": str,
    },
)
_OptionalBridgeFlowSourceTypeDef = TypedDict(
    "_OptionalBridgeFlowSourceTypeDef",
    {
        "FlowVpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
        "OutputArn": str,
    },
    total=False,
)

class BridgeFlowSourceTypeDef(_RequiredBridgeFlowSourceTypeDef, _OptionalBridgeFlowSourceTypeDef):
    pass

BridgeNetworkOutputTypeDef = TypedDict(
    "BridgeNetworkOutputTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)

BridgeNetworkSourceTypeDef = TypedDict(
    "BridgeNetworkSourceTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
    },
)

BridgeOutputTypeDef = TypedDict(
    "BridgeOutputTypeDef",
    {
        "FlowOutput": "BridgeFlowOutputTypeDef",
        "NetworkOutput": "BridgeNetworkOutputTypeDef",
    },
    total=False,
)

BridgeSourceTypeDef = TypedDict(
    "BridgeSourceTypeDef",
    {
        "FlowSource": "BridgeFlowSourceTypeDef",
        "NetworkSource": "BridgeNetworkSourceTypeDef",
    },
    total=False,
)

_RequiredBridgeTypeDef = TypedDict(
    "_RequiredBridgeTypeDef",
    {
        "BridgeArn": str,
        "BridgeState": BridgeStateType,
        "Name": str,
        "PlacementArn": str,
    },
)
_OptionalBridgeTypeDef = TypedDict(
    "_OptionalBridgeTypeDef",
    {
        "BridgeMessages": List["MessageDetailTypeDef"],
        "EgressGatewayBridge": "EgressGatewayBridgeTypeDef",
        "IngressGatewayBridge": "IngressGatewayBridgeTypeDef",
        "Outputs": List["BridgeOutputTypeDef"],
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["BridgeSourceTypeDef"],
    },
    total=False,
)

class BridgeTypeDef(_RequiredBridgeTypeDef, _OptionalBridgeTypeDef):
    pass

_RequiredCreateBridgeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBridgeRequestRequestTypeDef",
    {
        "Name": str,
        "PlacementArn": str,
        "Sources": List["AddBridgeSourceRequestTypeDef"],
    },
)
_OptionalCreateBridgeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBridgeRequestRequestTypeDef",
    {
        "EgressGatewayBridge": "AddEgressGatewayBridgeRequestTypeDef",
        "IngressGatewayBridge": "AddIngressGatewayBridgeRequestTypeDef",
        "Outputs": List["AddBridgeOutputRequestTypeDef"],
        "SourceFailoverConfig": "FailoverConfigTypeDef",
    },
    total=False,
)

class CreateBridgeRequestRequestTypeDef(
    _RequiredCreateBridgeRequestRequestTypeDef, _OptionalCreateBridgeRequestRequestTypeDef
):
    pass

CreateBridgeResponseTypeDef = TypedDict(
    "CreateBridgeResponseTypeDef",
    {
        "Bridge": "BridgeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
        "Outputs": List["AddOutputRequestTypeDef"],
        "Source": "SetSourceRequestTypeDef",
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SetSourceRequestTypeDef"],
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
        "Maintenance": "AddMaintenanceTypeDef",
    },
    total=False,
)

class CreateFlowRequestRequestTypeDef(
    _RequiredCreateFlowRequestRequestTypeDef, _OptionalCreateFlowRequestRequestTypeDef
):
    pass

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGatewayRequestRequestTypeDef = TypedDict(
    "CreateGatewayRequestRequestTypeDef",
    {
        "EgressCidrBlocks": List[str],
        "Name": str,
        "Networks": List["GatewayNetworkTypeDef"],
    },
)

CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef",
    {
        "Gateway": "GatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBridgeRequestRequestTypeDef = TypedDict(
    "DeleteBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
    },
)

DeleteBridgeResponseTypeDef = TypedDict(
    "DeleteBridgeResponseTypeDef",
    {
        "BridgeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayRequestRequestTypeDef = TypedDict(
    "DeleteGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DeleteGatewayResponseTypeDef = TypedDict(
    "DeleteGatewayResponseTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeregisterGatewayInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
    },
)
_OptionalDeregisterGatewayInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterGatewayInstanceRequestRequestTypeDef",
    {
        "Force": bool,
    },
    total=False,
)

class DeregisterGatewayInstanceRequestRequestTypeDef(
    _RequiredDeregisterGatewayInstanceRequestRequestTypeDef,
    _OptionalDeregisterGatewayInstanceRequestRequestTypeDef,
):
    pass

DeregisterGatewayInstanceResponseTypeDef = TypedDict(
    "DeregisterGatewayInstanceResponseTypeDef",
    {
        "GatewayInstanceArn": str,
        "InstanceState": InstanceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBridgeRequestRequestTypeDef = TypedDict(
    "DescribeBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
    },
)

DescribeBridgeResponseTypeDef = TypedDict(
    "DescribeBridgeResponseTypeDef",
    {
        "Bridge": "BridgeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "Messages": "MessagesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowSourceMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFlowSourceMetadataRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DescribeFlowSourceMetadataResponseTypeDef = TypedDict(
    "DescribeFlowSourceMetadataResponseTypeDef",
    {
        "FlowArn": str,
        "Messages": List["MessageDetailTypeDef"],
        "Timestamp": datetime,
        "TransportMediaInfo": "TransportMediaInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayInstanceRequestRequestTypeDef = TypedDict(
    "DescribeGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
    },
)

DescribeGatewayInstanceResponseTypeDef = TypedDict(
    "DescribeGatewayInstanceResponseTypeDef",
    {
        "GatewayInstance": "GatewayInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayRequestRequestTypeDef = TypedDict(
    "DescribeGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DescribeGatewayResponseTypeDef = TypedDict(
    "DescribeGatewayResponseTypeDef",
    {
        "Gateway": "GatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
    },
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Offering": "OfferingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationArn": str,
    },
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConfigurationRequestTypeDef = TypedDict(
    "DestinationConfigurationRequestTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceTypeDef",
        "OutboundIp": str,
    },
)

_RequiredEgressGatewayBridgeTypeDef = TypedDict(
    "_RequiredEgressGatewayBridgeTypeDef",
    {
        "MaxBitrate": int,
    },
)
_OptionalEgressGatewayBridgeTypeDef = TypedDict(
    "_OptionalEgressGatewayBridgeTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

class EgressGatewayBridgeTypeDef(
    _RequiredEgressGatewayBridgeTypeDef, _OptionalEgressGatewayBridgeTypeDef
):
    pass

EncodingParametersRequestTypeDef = TypedDict(
    "EncodingParametersRequestTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

EncodingParametersTypeDef = TypedDict(
    "EncodingParametersTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass

_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
    },
    total=False,
)

class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass

FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

_RequiredFlowTypeDef = TypedDict(
    "_RequiredFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "Source": "SourceTypeDef",
        "Status": StatusType,
    },
)
_OptionalFlowTypeDef = TypedDict(
    "_OptionalFlowTypeDef",
    {
        "Description": str,
        "EgressIp": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SourceTypeDef"],
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
        "Maintenance": "MaintenanceTypeDef",
    },
    total=False,
)

class FlowTypeDef(_RequiredFlowTypeDef, _OptionalFlowTypeDef):
    pass

FmtpRequestTypeDef = TypedDict(
    "FmtpRequestTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

FmtpTypeDef = TypedDict(
    "FmtpTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

FrameResolutionTypeDef = TypedDict(
    "FrameResolutionTypeDef",
    {
        "FrameHeight": int,
        "FrameWidth": int,
    },
)

_RequiredGatewayBridgeSourceTypeDef = TypedDict(
    "_RequiredGatewayBridgeSourceTypeDef",
    {
        "BridgeArn": str,
    },
)
_OptionalGatewayBridgeSourceTypeDef = TypedDict(
    "_OptionalGatewayBridgeSourceTypeDef",
    {
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class GatewayBridgeSourceTypeDef(
    _RequiredGatewayBridgeSourceTypeDef, _OptionalGatewayBridgeSourceTypeDef
):
    pass

_RequiredGatewayInstanceTypeDef = TypedDict(
    "_RequiredGatewayInstanceTypeDef",
    {
        "BridgePlacement": BridgePlacementType,
        "ConnectionStatus": ConnectionStatusType,
        "GatewayArn": str,
        "GatewayInstanceArn": str,
        "InstanceId": str,
        "InstanceState": InstanceStateType,
        "RunningBridgeCount": int,
    },
)
_OptionalGatewayInstanceTypeDef = TypedDict(
    "_OptionalGatewayInstanceTypeDef",
    {
        "InstanceMessages": List["MessageDetailTypeDef"],
    },
    total=False,
)

class GatewayInstanceTypeDef(_RequiredGatewayInstanceTypeDef, _OptionalGatewayInstanceTypeDef):
    pass

GatewayNetworkTypeDef = TypedDict(
    "GatewayNetworkTypeDef",
    {
        "CidrBlock": str,
        "Name": str,
    },
)

_RequiredGatewayTypeDef = TypedDict(
    "_RequiredGatewayTypeDef",
    {
        "EgressCidrBlocks": List[str],
        "GatewayArn": str,
        "Name": str,
        "Networks": List["GatewayNetworkTypeDef"],
    },
)
_OptionalGatewayTypeDef = TypedDict(
    "_OptionalGatewayTypeDef",
    {
        "GatewayMessages": List["MessageDetailTypeDef"],
        "GatewayState": GatewayStateType,
    },
    total=False,
)

class GatewayTypeDef(_RequiredGatewayTypeDef, _OptionalGatewayTypeDef):
    pass

_RequiredGrantEntitlementRequestTypeDef = TypedDict(
    "_RequiredGrantEntitlementRequestTypeDef",
    {
        "Subscribers": List[str],
    },
)
_OptionalGrantEntitlementRequestTypeDef = TypedDict(
    "_OptionalGrantEntitlementRequestTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Name": str,
    },
    total=False,
)

class GrantEntitlementRequestTypeDef(
    _RequiredGrantEntitlementRequestTypeDef, _OptionalGrantEntitlementRequestTypeDef
):
    pass

GrantFlowEntitlementsRequestRequestTypeDef = TypedDict(
    "GrantFlowEntitlementsRequestRequestTypeDef",
    {
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "FlowArn": str,
    },
)

GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIngressGatewayBridgeTypeDef = TypedDict(
    "_RequiredIngressGatewayBridgeTypeDef",
    {
        "MaxBitrate": int,
        "MaxOutputs": int,
    },
)
_OptionalIngressGatewayBridgeTypeDef = TypedDict(
    "_OptionalIngressGatewayBridgeTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

class IngressGatewayBridgeTypeDef(
    _RequiredIngressGatewayBridgeTypeDef, _OptionalIngressGatewayBridgeTypeDef
):
    pass

InputConfigurationRequestTypeDef = TypedDict(
    "InputConfigurationRequestTypeDef",
    {
        "InputPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "InputIp": str,
        "InputPort": int,
        "Interface": "InterfaceTypeDef",
    },
)

InterfaceRequestTypeDef = TypedDict(
    "InterfaceRequestTypeDef",
    {
        "Name": str,
    },
)

InterfaceTypeDef = TypedDict(
    "InterfaceTypeDef",
    {
        "Name": str,
    },
)

ListBridgesRequestRequestTypeDef = TypedDict(
    "ListBridgesRequestRequestTypeDef",
    {
        "FilterArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListBridgesResponseTypeDef = TypedDict(
    "ListBridgesResponseTypeDef",
    {
        "Bridges": List["ListedBridgeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitlementsRequestRequestTypeDef = TypedDict(
    "ListEntitlementsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {
        "Entitlements": List["ListedEntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "Flows": List["ListedFlowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewayInstancesRequestRequestTypeDef = TypedDict(
    "ListGatewayInstancesRequestRequestTypeDef",
    {
        "FilterArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGatewayInstancesResponseTypeDef = TypedDict(
    "ListGatewayInstancesResponseTypeDef",
    {
        "Instances": List["ListedGatewayInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "Gateways": List["ListedGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListedBridgeTypeDef = TypedDict(
    "ListedBridgeTypeDef",
    {
        "BridgeArn": str,
        "BridgeState": BridgeStateType,
        "BridgeType": str,
        "Name": str,
        "PlacementArn": str,
    },
)

_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "EntitlementName": str,
    },
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
    },
    total=False,
)

class ListedEntitlementTypeDef(
    _RequiredListedEntitlementTypeDef, _OptionalListedEntitlementTypeDef
):
    pass

_RequiredListedFlowTypeDef = TypedDict(
    "_RequiredListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": SourceTypeType,
        "Status": StatusType,
    },
)
_OptionalListedFlowTypeDef = TypedDict(
    "_OptionalListedFlowTypeDef",
    {
        "Maintenance": "MaintenanceTypeDef",
    },
    total=False,
)

class ListedFlowTypeDef(_RequiredListedFlowTypeDef, _OptionalListedFlowTypeDef):
    pass

_RequiredListedGatewayInstanceTypeDef = TypedDict(
    "_RequiredListedGatewayInstanceTypeDef",
    {
        "GatewayArn": str,
        "GatewayInstanceArn": str,
        "InstanceId": str,
    },
)
_OptionalListedGatewayInstanceTypeDef = TypedDict(
    "_OptionalListedGatewayInstanceTypeDef",
    {
        "InstanceState": InstanceStateType,
    },
    total=False,
)

class ListedGatewayInstanceTypeDef(
    _RequiredListedGatewayInstanceTypeDef, _OptionalListedGatewayInstanceTypeDef
):
    pass

ListedGatewayTypeDef = TypedDict(
    "ListedGatewayTypeDef",
    {
        "GatewayArn": str,
        "GatewayState": GatewayStateType,
        "Name": str,
    },
)

MaintenanceTypeDef = TypedDict(
    "MaintenanceTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceDeadline": str,
        "MaintenanceScheduledDate": str,
        "MaintenanceStartHour": str,
    },
    total=False,
)

MediaStreamAttributesRequestTypeDef = TypedDict(
    "MediaStreamAttributesRequestTypeDef",
    {
        "Fmtp": "FmtpRequestTypeDef",
        "Lang": str,
    },
    total=False,
)

_RequiredMediaStreamAttributesTypeDef = TypedDict(
    "_RequiredMediaStreamAttributesTypeDef",
    {
        "Fmtp": "FmtpTypeDef",
    },
)
_OptionalMediaStreamAttributesTypeDef = TypedDict(
    "_OptionalMediaStreamAttributesTypeDef",
    {
        "Lang": str,
    },
    total=False,
)

class MediaStreamAttributesTypeDef(
    _RequiredMediaStreamAttributesTypeDef, _OptionalMediaStreamAttributesTypeDef
):
    pass

_RequiredMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationRequestTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationRequestTypeDef"],
        "EncodingParameters": "EncodingParametersRequestTypeDef",
    },
    total=False,
)

class MediaStreamOutputConfigurationRequestTypeDef(
    _RequiredMediaStreamOutputConfigurationRequestTypeDef,
    _OptionalMediaStreamOutputConfigurationRequestTypeDef,
):
    pass

_RequiredMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationTypeDef"],
        "EncodingParameters": "EncodingParametersTypeDef",
    },
    total=False,
)

class MediaStreamOutputConfigurationTypeDef(
    _RequiredMediaStreamOutputConfigurationTypeDef, _OptionalMediaStreamOutputConfigurationTypeDef
):
    pass

_RequiredMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationRequestTypeDef",
    {
        "InputConfigurations": List["InputConfigurationRequestTypeDef"],
    },
    total=False,
)

class MediaStreamSourceConfigurationRequestTypeDef(
    _RequiredMediaStreamSourceConfigurationRequestTypeDef,
    _OptionalMediaStreamSourceConfigurationRequestTypeDef,
):
    pass

_RequiredMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationTypeDef",
    {
        "InputConfigurations": List["InputConfigurationTypeDef"],
    },
    total=False,
)

class MediaStreamSourceConfigurationTypeDef(
    _RequiredMediaStreamSourceConfigurationTypeDef, _OptionalMediaStreamSourceConfigurationTypeDef
):
    pass

_RequiredMediaStreamTypeDef = TypedDict(
    "_RequiredMediaStreamTypeDef",
    {
        "Fmt": int,
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalMediaStreamTypeDef = TypedDict(
    "_OptionalMediaStreamTypeDef",
    {
        "Attributes": "MediaStreamAttributesTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)

class MediaStreamTypeDef(_RequiredMediaStreamTypeDef, _OptionalMediaStreamTypeDef):
    pass

_RequiredMessageDetailTypeDef = TypedDict(
    "_RequiredMessageDetailTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)
_OptionalMessageDetailTypeDef = TypedDict(
    "_OptionalMessageDetailTypeDef",
    {
        "ResourceName": str,
    },
    total=False,
)

class MessageDetailTypeDef(_RequiredMessageDetailTypeDef, _OptionalMessageDetailTypeDef):
    pass

MessagesTypeDef = TypedDict(
    "MessagesTypeDef",
    {
        "Errors": List[str],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ResourceSpecification": "ResourceSpecificationTypeDef",
    },
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Name": str,
        "OutputArn": str,
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementArn": str,
        "ListenerAddress": str,
        "MediaLiveInputArn": str,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationTypeDef"],
        "Port": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
        "BridgeArn": str,
        "BridgePorts": List[int],
    },
    total=False,
)

class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
        "ReservationName": str,
        "Start": str,
    },
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveBridgeOutputRequestRequestTypeDef = TypedDict(
    "RemoveBridgeOutputRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
    },
)

RemoveBridgeOutputResponseTypeDef = TypedDict(
    "RemoveBridgeOutputResponseTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveBridgeSourceRequestRequestTypeDef = TypedDict(
    "RemoveBridgeSourceRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
    },
)

RemoveBridgeSourceResponseTypeDef = TypedDict(
    "RemoveBridgeSourceResponseTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)

RemoveFlowMediaStreamResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowOutputRequestRequestTypeDef = TypedDict(
    "RemoveFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowSourceRequestRequestTypeDef = TypedDict(
    "RemoveFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)

RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowVpcInterfaceRequestRequestTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaceName": str,
    },
)

RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ReservationArn": str,
        "ReservationName": str,
        "ReservationState": ReservationStateType,
        "ResourceSpecification": "ResourceSpecificationTypeDef",
        "Start": str,
    },
)

_RequiredResourceSpecificationTypeDef = TypedDict(
    "_RequiredResourceSpecificationTypeDef",
    {
        "ResourceType": Literal["Mbps_Outbound_Bandwidth"],
    },
)
_OptionalResourceSpecificationTypeDef = TypedDict(
    "_OptionalResourceSpecificationTypeDef",
    {
        "ReservedBitrate": int,
    },
    total=False,
)

class ResourceSpecificationTypeDef(
    _RequiredResourceSpecificationTypeDef, _OptionalResourceSpecificationTypeDef
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RevokeFlowEntitlementRequestRequestTypeDef = TypedDict(
    "RevokeFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetGatewayBridgeSourceRequestTypeDef = TypedDict(
    "_RequiredSetGatewayBridgeSourceRequestTypeDef",
    {
        "BridgeArn": str,
    },
)
_OptionalSetGatewayBridgeSourceRequestTypeDef = TypedDict(
    "_OptionalSetGatewayBridgeSourceRequestTypeDef",
    {
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class SetGatewayBridgeSourceRequestTypeDef(
    _RequiredSetGatewayBridgeSourceRequestTypeDef, _OptionalSetGatewayBridgeSourceRequestTypeDef
):
    pass

SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Protocol": ProtocolType,
        "SenderControlPort": int,
        "SenderIpAddress": str,
        "SourceListenerAddress": str,
        "SourceListenerPort": int,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
        "GatewayBridgeSource": "SetGatewayBridgeSourceRequestTypeDef",
    },
    total=False,
)

SourcePriorityTypeDef = TypedDict(
    "SourcePriorityTypeDef",
    {
        "PrimarySource": str,
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Name": str,
        "SourceArn": str,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationTypeDef"],
        "SenderControlPort": int,
        "SenderIpAddress": str,
        "Transport": "TransportTypeDef",
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
        "GatewayBridgeSource": "GatewayBridgeSourceTypeDef",
    },
    total=False,
)

class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TransportMediaInfoTypeDef = TypedDict(
    "TransportMediaInfoTypeDef",
    {
        "Programs": List["TransportStreamProgramTypeDef"],
    },
)

_RequiredTransportStreamProgramTypeDef = TypedDict(
    "_RequiredTransportStreamProgramTypeDef",
    {
        "PcrPid": int,
        "ProgramNumber": int,
        "ProgramPid": int,
        "Streams": List["TransportStreamTypeDef"],
    },
)
_OptionalTransportStreamProgramTypeDef = TypedDict(
    "_OptionalTransportStreamProgramTypeDef",
    {
        "ProgramName": str,
    },
    total=False,
)

class TransportStreamProgramTypeDef(
    _RequiredTransportStreamProgramTypeDef, _OptionalTransportStreamProgramTypeDef
):
    pass

_RequiredTransportStreamTypeDef = TypedDict(
    "_RequiredTransportStreamTypeDef",
    {
        "Pid": int,
        "StreamType": str,
    },
)
_OptionalTransportStreamTypeDef = TypedDict(
    "_OptionalTransportStreamTypeDef",
    {
        "Channels": int,
        "Codec": str,
        "FrameRate": str,
        "FrameResolution": "FrameResolutionTypeDef",
        "SampleRate": int,
        "SampleSize": int,
    },
    total=False,
)

class TransportStreamTypeDef(_RequiredTransportStreamTypeDef, _OptionalTransportStreamTypeDef):
    pass

_RequiredTransportTypeDef = TypedDict(
    "_RequiredTransportTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MinLatency": int,
        "RemoteId": str,
        "SenderControlPort": int,
        "SenderIpAddress": str,
        "SmoothingLatency": int,
        "SourceListenerAddress": str,
        "SourceListenerPort": int,
        "StreamId": str,
    },
    total=False,
)

class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateBridgeFlowSourceRequestTypeDef = TypedDict(
    "UpdateBridgeFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "FlowVpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

UpdateBridgeNetworkOutputRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
    total=False,
)

UpdateBridgeNetworkSourceRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
    },
    total=False,
)

_RequiredUpdateBridgeOutputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBridgeOutputRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
    },
)
_OptionalUpdateBridgeOutputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBridgeOutputRequestRequestTypeDef",
    {
        "NetworkOutput": "UpdateBridgeNetworkOutputRequestTypeDef",
    },
    total=False,
)

class UpdateBridgeOutputRequestRequestTypeDef(
    _RequiredUpdateBridgeOutputRequestRequestTypeDef,
    _OptionalUpdateBridgeOutputRequestRequestTypeDef,
):
    pass

UpdateBridgeOutputResponseTypeDef = TypedDict(
    "UpdateBridgeOutputResponseTypeDef",
    {
        "BridgeArn": str,
        "Output": "BridgeOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBridgeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
    },
)
_OptionalUpdateBridgeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBridgeRequestRequestTypeDef",
    {
        "EgressGatewayBridge": "UpdateEgressGatewayBridgeRequestTypeDef",
        "IngressGatewayBridge": "UpdateIngressGatewayBridgeRequestTypeDef",
        "SourceFailoverConfig": "UpdateFailoverConfigTypeDef",
    },
    total=False,
)

class UpdateBridgeRequestRequestTypeDef(
    _RequiredUpdateBridgeRequestRequestTypeDef, _OptionalUpdateBridgeRequestRequestTypeDef
):
    pass

UpdateBridgeResponseTypeDef = TypedDict(
    "UpdateBridgeResponseTypeDef",
    {
        "Bridge": "BridgeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBridgeSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBridgeSourceRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
    },
)
_OptionalUpdateBridgeSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBridgeSourceRequestRequestTypeDef",
    {
        "FlowSource": "UpdateBridgeFlowSourceRequestTypeDef",
        "NetworkSource": "UpdateBridgeNetworkSourceRequestTypeDef",
    },
    total=False,
)

class UpdateBridgeSourceRequestRequestTypeDef(
    _RequiredUpdateBridgeSourceRequestRequestTypeDef,
    _OptionalUpdateBridgeSourceRequestRequestTypeDef,
):
    pass

UpdateBridgeSourceResponseTypeDef = TypedDict(
    "UpdateBridgeSourceResponseTypeDef",
    {
        "BridgeArn": str,
        "Source": "BridgeSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBridgeStateRequestRequestTypeDef = TypedDict(
    "UpdateBridgeStateRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "DesiredState": DesiredStateType,
    },
)

UpdateBridgeStateResponseTypeDef = TypedDict(
    "UpdateBridgeStateResponseTypeDef",
    {
        "BridgeArn": str,
        "DesiredState": DesiredStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEgressGatewayBridgeRequestTypeDef = TypedDict(
    "UpdateEgressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
    },
    total=False,
)

UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

UpdateFailoverConfigTypeDef = TypedDict(
    "UpdateFailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

_RequiredUpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)
_OptionalUpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowEntitlementRequestRequestTypeDef",
    {
        "Description": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Subscribers": List[str],
    },
    total=False,
)

class UpdateFlowEntitlementRequestRequestTypeDef(
    _RequiredUpdateFlowEntitlementRequestRequestTypeDef,
    _OptionalUpdateFlowEntitlementRequestRequestTypeDef,
):
    pass

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)
_OptionalUpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "MediaStreamType": MediaStreamTypeType,
        "VideoFormat": str,
    },
    total=False,
)

class UpdateFlowMediaStreamRequestRequestTypeDef(
    _RequiredUpdateFlowMediaStreamRequestRequestTypeDef,
    _OptionalUpdateFlowMediaStreamRequestRequestTypeDef,
):
    pass

UpdateFlowMediaStreamResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": "MediaStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)
_OptionalUpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowOutputRequestRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Port": int,
        "Protocol": ProtocolType,
        "RemoteId": str,
        "SenderControlPort": int,
        "SenderIpAddress": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class UpdateFlowOutputRequestRequestTypeDef(
    _RequiredUpdateFlowOutputRequestRequestTypeDef, _OptionalUpdateFlowOutputRequestRequestTypeDef
):
    pass

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "Output": "OutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
_OptionalUpdateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestRequestTypeDef",
    {
        "SourceFailoverConfig": "UpdateFailoverConfigTypeDef",
        "Maintenance": "UpdateMaintenanceTypeDef",
    },
    total=False,
)

class UpdateFlowRequestRequestTypeDef(
    _RequiredUpdateFlowRequestRequestTypeDef, _OptionalUpdateFlowRequestRequestTypeDef
):
    pass

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)
_OptionalUpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowSourceRequestRequestTypeDef",
    {
        "Decryption": "UpdateEncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Protocol": ProtocolType,
        "SenderControlPort": int,
        "SenderIpAddress": str,
        "SourceListenerAddress": str,
        "SourceListenerPort": int,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
        "GatewayBridgeSource": "UpdateGatewayBridgeSourceRequestTypeDef",
    },
    total=False,
)

class UpdateFlowSourceRequestRequestTypeDef(
    _RequiredUpdateFlowSourceRequestRequestTypeDef, _OptionalUpdateFlowSourceRequestRequestTypeDef
):
    pass

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "Source": "SourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayBridgeSourceRequestTypeDef = TypedDict(
    "UpdateGatewayBridgeSourceRequestTypeDef",
    {
        "BridgeArn": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

_RequiredUpdateGatewayInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
    },
)
_OptionalUpdateGatewayInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayInstanceRequestRequestTypeDef",
    {
        "BridgePlacement": BridgePlacementType,
    },
    total=False,
)

class UpdateGatewayInstanceRequestRequestTypeDef(
    _RequiredUpdateGatewayInstanceRequestRequestTypeDef,
    _OptionalUpdateGatewayInstanceRequestRequestTypeDef,
):
    pass

UpdateGatewayInstanceResponseTypeDef = TypedDict(
    "UpdateGatewayInstanceResponseTypeDef",
    {
        "BridgePlacement": BridgePlacementType,
        "GatewayInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIngressGatewayBridgeRequestTypeDef = TypedDict(
    "UpdateIngressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
        "MaxOutputs": int,
    },
    total=False,
)

UpdateMaintenanceTypeDef = TypedDict(
    "UpdateMaintenanceTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceScheduledDate": str,
        "MaintenanceStartHour": str,
    },
    total=False,
)

VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef",
    {
        "VpcInterfaceName": str,
    },
    total=False,
)

_RequiredVpcInterfaceRequestTypeDef = TypedDict(
    "_RequiredVpcInterfaceRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)
_OptionalVpcInterfaceRequestTypeDef = TypedDict(
    "_OptionalVpcInterfaceRequestTypeDef",
    {
        "NetworkInterfaceType": NetworkInterfaceTypeType,
    },
    total=False,
)

class VpcInterfaceRequestTypeDef(
    _RequiredVpcInterfaceRequestTypeDef, _OptionalVpcInterfaceRequestTypeDef
):
    pass

VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "NetworkInterfaceType": NetworkInterfaceTypeType,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
