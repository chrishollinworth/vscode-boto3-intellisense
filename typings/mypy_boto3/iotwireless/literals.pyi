"""
Type annotations for iotwireless service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/literals.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.literals import ApplicationConfigTypeType

    data: ApplicationConfigTypeType = "SemtechGeolocation"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationConfigTypeType",
    "BatteryLevelType",
    "ConnectionStatusType",
    "DeviceProfileTypeType",
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
    "ImportTaskStatusType",
    "LogLevelType",
    "MessageTypeType",
    "MulticastFrameInfoType",
    "OnboardStatusType",
    "PartnerTypeType",
    "PositionConfigurationFecType",
    "PositionConfigurationStatusType",
    "PositionResourceTypeType",
    "PositionSolverProviderType",
    "PositionSolverTypeType",
    "PositioningConfigStatusType",
    "SigningAlgType",
    "SupportedRfRegionType",
    "WirelessDeviceEventType",
    "WirelessDeviceFrameInfoType",
    "WirelessDeviceIdTypeType",
    "WirelessDeviceSidewalkStatusType",
    "WirelessDeviceTypeType",
    "WirelessGatewayEventType",
    "WirelessGatewayIdTypeType",
    "WirelessGatewayServiceTypeType",
    "WirelessGatewayTaskDefinitionTypeType",
    "WirelessGatewayTaskStatusType",
    "WirelessGatewayTypeType",
)

ApplicationConfigTypeType = Literal["SemtechGeolocation"]
BatteryLevelType = Literal["critical", "low", "normal"]
ConnectionStatusType = Literal["Connected", "Disconnected"]
DeviceProfileTypeType = Literal["LoRaWAN", "Sidewalk"]
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
ImportTaskStatusType = Literal[
    "COMPLETE", "DELETING", "FAILED", "INITIALIZED", "INITIALIZING", "PENDING"
]
LogLevelType = Literal["DISABLED", "ERROR", "INFO"]
MessageTypeType = Literal[
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_RESP",
    "CUSTOM_COMMAND_ID_SET",
]
MulticastFrameInfoType = Literal["DISABLED", "ENABLED"]
OnboardStatusType = Literal["FAILED", "INITIALIZED", "ONBOARDED", "PENDING"]
PartnerTypeType = Literal["Sidewalk"]
PositionConfigurationFecType = Literal["NONE", "ROSE"]
PositionConfigurationStatusType = Literal["Disabled", "Enabled"]
PositionResourceTypeType = Literal["WirelessDevice", "WirelessGateway"]
PositionSolverProviderType = Literal["Semtech"]
PositionSolverTypeType = Literal["GNSS"]
PositioningConfigStatusType = Literal["Disabled", "Enabled"]
SigningAlgType = Literal["Ed25519", "P256r1"]
SupportedRfRegionType = Literal[
    "AS923-1",
    "AS923-2",
    "AS923-3",
    "AS923-4",
    "AU915",
    "CN470",
    "CN779",
    "EU433",
    "EU868",
    "IN865",
    "KR920",
    "RU864",
    "US915",
]
WirelessDeviceEventType = Literal["Downlink_Data", "Join", "Registration", "Rejoin", "Uplink_Data"]
WirelessDeviceFrameInfoType = Literal["DISABLED", "ENABLED"]
WirelessDeviceIdTypeType = Literal[
    "DevEui", "SidewalkManufacturingSn", "ThingName", "WirelessDeviceId"
]
WirelessDeviceSidewalkStatusType = Literal["ACTIVATED", "PROVISIONED", "REGISTERED", "UNKNOWN"]
WirelessDeviceTypeType = Literal["LoRaWAN", "Sidewalk"]
WirelessGatewayEventType = Literal["CUPS_Request", "Certificate"]
WirelessGatewayIdTypeType = Literal["GatewayEui", "ThingName", "WirelessGatewayId"]
WirelessGatewayServiceTypeType = Literal["CUPS", "LNS"]
WirelessGatewayTaskDefinitionTypeType = Literal["UPDATE"]
WirelessGatewayTaskStatusType = Literal[
    "COMPLETED", "FAILED", "FIRST_RETRY", "IN_PROGRESS", "PENDING", "SECOND_RETRY"
]
WirelessGatewayTypeType = Literal["LoRaWAN"]
