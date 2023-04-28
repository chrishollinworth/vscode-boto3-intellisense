"""
Type annotations for mediaconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.literals import AlgorithmType

    data: AlgorithmType = "aes128"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlgorithmType",
    "BridgePlacementType",
    "BridgeStateType",
    "ColorimetryType",
    "ConnectionStatusType",
    "DesiredStateType",
    "DurationUnitsType",
    "EncoderProfileType",
    "EncodingNameType",
    "EntitlementStatusType",
    "FailoverModeType",
    "FlowActiveWaiterName",
    "FlowDeletedWaiterName",
    "FlowStandbyWaiterName",
    "GatewayStateType",
    "InstanceStateType",
    "KeyTypeType",
    "ListBridgesPaginatorName",
    "ListEntitlementsPaginatorName",
    "ListFlowsPaginatorName",
    "ListGatewayInstancesPaginatorName",
    "ListGatewaysPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "MaintenanceDayType",
    "MediaStreamTypeType",
    "NetworkInterfaceTypeType",
    "PriceUnitsType",
    "ProtocolType",
    "RangeType",
    "ReservationStateType",
    "ResourceTypeType",
    "ScanModeType",
    "SourceTypeType",
    "StateType",
    "StatusType",
    "TcsType",
)

AlgorithmType = Literal["aes128", "aes192", "aes256"]
BridgePlacementType = Literal["AVAILABLE", "LOCKED"]
BridgeStateType = Literal[
    "ACTIVE",
    "CREATING",
    "DELETED",
    "DELETING",
    "DEPLOYING",
    "STANDBY",
    "STARTING",
    "START_FAILED",
    "START_PENDING",
    "STOPPING",
    "STOP_FAILED",
    "UPDATING",
]
ColorimetryType = Literal["BT2020", "BT2100", "BT601", "BT709", "ST2065-1", "ST2065-3", "XYZ"]
ConnectionStatusType = Literal["CONNECTED", "DISCONNECTED"]
DesiredStateType = Literal["ACTIVE", "DELETED", "STANDBY"]
DurationUnitsType = Literal["MONTHS"]
EncoderProfileType = Literal["high", "main"]
EncodingNameType = Literal["jxsv", "pcm", "raw", "smpte291"]
EntitlementStatusType = Literal["DISABLED", "ENABLED"]
FailoverModeType = Literal["FAILOVER", "MERGE"]
FlowActiveWaiterName = Literal["flow_active"]
FlowDeletedWaiterName = Literal["flow_deleted"]
FlowStandbyWaiterName = Literal["flow_standby"]
GatewayStateType = Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "ERROR", "UPDATING"]
InstanceStateType = Literal[
    "ACTIVE",
    "DEREGISTERED",
    "DEREGISTERING",
    "DEREGISTRATION_ERROR",
    "REGISTERING",
    "REGISTRATION_ERROR",
]
KeyTypeType = Literal["speke", "srt-password", "static-key"]
ListBridgesPaginatorName = Literal["list_bridges"]
ListEntitlementsPaginatorName = Literal["list_entitlements"]
ListFlowsPaginatorName = Literal["list_flows"]
ListGatewayInstancesPaginatorName = Literal["list_gateway_instances"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
MaintenanceDayType = Literal[
    "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
]
MediaStreamTypeType = Literal["ancillary-data", "audio", "video"]
NetworkInterfaceTypeType = Literal["efa", "ena"]
PriceUnitsType = Literal["HOURLY"]
ProtocolType = Literal[
    "cdi",
    "fujitsu-qos",
    "rist",
    "rtp",
    "rtp-fec",
    "srt-caller",
    "srt-listener",
    "st2110-jpegxs",
    "udp",
    "zixi-pull",
    "zixi-push",
]
RangeType = Literal["FULL", "FULLPROTECT", "NARROW"]
ReservationStateType = Literal["ACTIVE", "CANCELED", "EXPIRED", "PROCESSING"]
ResourceTypeType = Literal["Mbps_Outbound_Bandwidth"]
ScanModeType = Literal["interlace", "progressive", "progressive-segmented-frame"]
SourceTypeType = Literal["ENTITLED", "OWNED"]
StateType = Literal["DISABLED", "ENABLED"]
StatusType = Literal["ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"]
TcsType = Literal[
    "BT2100LINHLG", "BT2100LINPQ", "DENSITY", "HLG", "LINEAR", "PQ", "SDR", "ST2065-1", "ST428-1"
]
