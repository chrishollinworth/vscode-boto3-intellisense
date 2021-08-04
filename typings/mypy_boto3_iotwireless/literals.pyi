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
    "EventType",
    "ExpressionTypeType",
    "LogLevelType",
    "MessageTypeType",
    "PartnerTypeType",
    "SigningAlgType",
    "WirelessDeviceEventType",
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
EventType = Literal["ack", "discovered", "lost", "nack", "passthrough"]
ExpressionTypeType = Literal["MqttTopic", "RuleName"]
LogLevelType = Literal["DISABLED", "ERROR", "INFO"]
MessageTypeType = Literal[
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_RESP",
    "CUSTOM_COMMAND_ID_SET",
]
PartnerTypeType = Literal["Sidewalk"]
SigningAlgType = Literal["Ed25519", "P256r1"]
WirelessDeviceEventType = Literal["Downlink_Data", "Join", "Registration", "Rejoin", "Uplink_Data"]
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
