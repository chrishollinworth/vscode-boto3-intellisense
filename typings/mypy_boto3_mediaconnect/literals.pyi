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
    "ColorimetryType",
    "DurationUnitsType",
    "EncoderProfileType",
    "EncodingNameType",
    "EntitlementStatusType",
    "FailoverModeType",
    "FlowActiveWaiterName",
    "FlowDeletedWaiterName",
    "FlowStandbyWaiterName",
    "KeyTypeType",
    "ListEntitlementsPaginatorName",
    "ListFlowsPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
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
ColorimetryType = Literal["BT2020", "BT2100", "BT601", "BT709", "ST2065-1", "ST2065-3", "XYZ"]
DurationUnitsType = Literal["MONTHS"]
EncoderProfileType = Literal["high", "main"]
EncodingNameType = Literal["jxsv", "pcm", "raw", "smpte291"]
EntitlementStatusType = Literal["DISABLED", "ENABLED"]
FailoverModeType = Literal["FAILOVER", "MERGE"]
FlowActiveWaiterName = Literal["flow_active"]
FlowDeletedWaiterName = Literal["flow_deleted"]
FlowStandbyWaiterName = Literal["flow_standby"]
KeyTypeType = Literal["speke", "srt-password", "static-key"]
ListEntitlementsPaginatorName = Literal["list_entitlements"]
ListFlowsPaginatorName = Literal["list_flows"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
MediaStreamTypeType = Literal["ancillary-data", "audio", "video"]
NetworkInterfaceTypeType = Literal["efa", "ena"]
PriceUnitsType = Literal["HOURLY"]
ProtocolType = Literal[
    "cdi", "rist", "rtp", "rtp-fec", "srt-listener", "st2110-jpegxs", "zixi-pull", "zixi-push"
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
