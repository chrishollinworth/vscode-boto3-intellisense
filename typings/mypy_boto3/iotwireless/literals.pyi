"""
Type annotations for iotwireless service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/literals.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.literals import BatteryLevelType

    data: BatteryLevelType = "critical"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BatteryLevelType",
    "ConnectionStatusType",
    "DeviceStateType",
    "DlClassType",
    "DownlinkModeType",
    "EventNotificationPartnerTypeType",
    "EventNotificationResourceTypeType",
    "EventNotificationTopicStatusType",
    "EventType",
    "ExpressionTypeType",
    "FuotaDeviceStatusType",
    "FuotaTaskStatusType",
    "IdentifierTypeType",
    "LogLevelType",
    "MessageTypeType",
    "PartnerTypeType",
    "PositionConfigurationFecType",
    "PositionConfigurationStatusType",
    "PositionResourceTypeType",
    "PositionSolverProviderType",
    "PositionSolverTypeType",
    "SigningAlgType",
    "SupportedRfRegionType",
    "WirelessDeviceEventType",
    "WirelessDeviceFrameInfoType",
    "WirelessDeviceIdTypeType",
    "WirelessDeviceTypeType",
    "WirelessGatewayEventType",
    "WirelessGatewayIdTypeType",
    "WirelessGatewayServiceTypeType",
    "WirelessGatewayTaskDefinitionTypeType",
    "WirelessGatewayTaskStatusType",
    "WirelessGatewayTypeType",
)

BatteryLevelType = Literal["critical", "low", "normal"]
ConnectionStatusType = Literal["Connected", "Disconnected"]
DeviceStateType = Literal[
    "Provisioned", "RegisteredNotSeen", "RegisteredReachable", "RegisteredUnreachable"
]
DlClassType = Literal["ClassB", "ClassC"]
DownlinkModeType = Literal["CONCURRENT", "SEQUENTIAL", "USING_UPLINK_GATEWAY"]
EventNotificationPartnerTypeType = Literal["Sidewalk"]
EventNotificationResourceTypeType = Literal["SidewalkAccount", "WirelessDevice", "WirelessGateway"]
EventNotificationTopicStatusType = Literal["Disabled", "Enabled"]
EventType = Literal["ack", "discovered", "lost", "nack", "passthrough"]
ExpressionTypeType = Literal["MqttTopic", "RuleName"]
FuotaDeviceStatusType = Literal[
    "FragAlgo_unsupported",
    "FragIndex_unsupported",
    "Initial",
    "MICError",
    "MemoryError",
    "MissingFrag",
    "Not_enough_memory",
    "Package_Not_Supported",
    "SessionCnt_replay",
    "Successful",
    "Wrong_descriptor",
]
FuotaTaskStatusType = Literal[
    "Delete_Waiting", "FuotaDone", "FuotaSession_Waiting", "In_FuotaSession", "Pending"
]
IdentifierTypeType = Literal[
    "DevEui", "GatewayEui", "PartnerAccountId", "WirelessDeviceId", "WirelessGatewayId"
]
LogLevelType = Literal["DISABLED", "ERROR", "INFO"]
MessageTypeType = Literal[
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_RESP",
    "CUSTOM_COMMAND_ID_SET",
]
PartnerTypeType = Literal["Sidewalk"]
PositionConfigurationFecType = Literal["NONE", "ROSE"]
PositionConfigurationStatusType = Literal["Disabled", "Enabled"]
PositionResourceTypeType = Literal["WirelessDevice", "WirelessGateway"]
PositionSolverProviderType = Literal["Semtech"]
PositionSolverTypeType = Literal["GNSS"]
SigningAlgType = Literal["Ed25519", "P256r1"]
SupportedRfRegionType = Literal["AS923-1", "AU915", "EU868", "US915"]
WirelessDeviceEventType = Literal["Downlink_Data", "Join", "Registration", "Rejoin", "Uplink_Data"]
WirelessDeviceFrameInfoType = Literal["DISABLED", "ENABLED"]
WirelessDeviceIdTypeType = Literal[
    "DevEui", "SidewalkManufacturingSn", "ThingName", "WirelessDeviceId"
]
WirelessDeviceTypeType = Literal["LoRaWAN", "Sidewalk"]
WirelessGatewayEventType = Literal["CUPS_Request", "Certificate"]
WirelessGatewayIdTypeType = Literal["GatewayEui", "ThingName", "WirelessGatewayId"]
WirelessGatewayServiceTypeType = Literal["CUPS", "LNS"]
WirelessGatewayTaskDefinitionTypeType = Literal["UPDATE"]
WirelessGatewayTaskStatusType = Literal[
    "COMPLETED", "FAILED", "FIRST_RETRY", "IN_PROGRESS", "PENDING", "SECOND_RETRY"
]
WirelessGatewayTypeType = Literal["LoRaWAN"]
