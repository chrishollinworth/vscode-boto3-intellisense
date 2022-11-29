"""
Type annotations for iotwireless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef

    data: AbpV1_0_xTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BatteryLevelType,
    ConnectionStatusType,
    DeviceStateType,
    DlClassType,
    DownlinkModeType,
    EventNotificationResourceTypeType,
    EventNotificationTopicStatusType,
    EventType,
    ExpressionTypeType,
    FuotaDeviceStatusType,
    FuotaTaskStatusType,
    IdentifierTypeType,
    LogLevelType,
    MessageTypeType,
    PositionConfigurationFecType,
    PositionConfigurationStatusType,
    PositioningConfigStatusType,
    PositionResourceTypeType,
    SigningAlgType,
    SupportedRfRegionType,
    WirelessDeviceEventType,
    WirelessDeviceFrameInfoType,
    WirelessDeviceIdTypeType,
    WirelessDeviceTypeType,
    WirelessGatewayEventType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
    WirelessGatewayTaskStatusType,
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
    "AbpV1_0_xTypeDef",
    "AbpV1_1TypeDef",
    "AccuracyTypeDef",
    "ApplicationConfigTypeDef",
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    "BeaconingTypeDef",
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    "CdmaLocalIdTypeDef",
    "CdmaNmrObjTypeDef",
    "CdmaObjTypeDef",
    "CellTowersTypeDef",
    "CertificateListTypeDef",
    "ConnectionStatusEventConfigurationTypeDef",
    "ConnectionStatusResourceTypeEventConfigurationTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileRequestRequestTypeDef",
    "CreateDeviceProfileResponseTypeDef",
    "CreateFuotaTaskRequestRequestTypeDef",
    "CreateFuotaTaskResponseTypeDef",
    "CreateMulticastGroupRequestRequestTypeDef",
    "CreateMulticastGroupResponseTypeDef",
    "CreateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "CreateNetworkAnalyzerConfigurationResponseTypeDef",
    "CreateServiceProfileRequestRequestTypeDef",
    "CreateServiceProfileResponseTypeDef",
    "CreateWirelessDeviceRequestRequestTypeDef",
    "CreateWirelessDeviceResponseTypeDef",
    "CreateWirelessGatewayRequestRequestTypeDef",
    "CreateWirelessGatewayResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    "CreateWirelessGatewayTaskResponseTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteDeviceProfileRequestRequestTypeDef",
    "DeleteFuotaTaskRequestRequestTypeDef",
    "DeleteMulticastGroupRequestRequestTypeDef",
    "DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "DeleteQueuedMessagesRequestRequestTypeDef",
    "DeleteServiceProfileRequestRequestTypeDef",
    "DeleteWirelessDeviceRequestRequestTypeDef",
    "DeleteWirelessGatewayRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "DeviceRegistrationStateEventConfigurationTypeDef",
    "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    "DownlinkQueueMessageTypeDef",
    "EventConfigurationItemTypeDef",
    "EventNotificationItemConfigurationsTypeDef",
    "FPortsTypeDef",
    "FuotaTaskTypeDef",
    "GatewayListItemTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceProfileRequestRequestTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "GetEventConfigurationByResourceTypesResponseTypeDef",
    "GetFuotaTaskRequestRequestTypeDef",
    "GetFuotaTaskResponseTypeDef",
    "GetLogLevelsByResourceTypesResponseTypeDef",
    "GetMulticastGroupRequestRequestTypeDef",
    "GetMulticastGroupResponseTypeDef",
    "GetMulticastGroupSessionRequestRequestTypeDef",
    "GetMulticastGroupSessionResponseTypeDef",
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    "GetPartnerAccountRequestRequestTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "GetPositionConfigurationRequestRequestTypeDef",
    "GetPositionConfigurationResponseTypeDef",
    "GetPositionEstimateRequestRequestTypeDef",
    "GetPositionEstimateResponseTypeDef",
    "GetPositionRequestRequestTypeDef",
    "GetPositionResponseTypeDef",
    "GetResourceEventConfigurationRequestRequestTypeDef",
    "GetResourceEventConfigurationResponseTypeDef",
    "GetResourceLogLevelRequestRequestTypeDef",
    "GetResourceLogLevelResponseTypeDef",
    "GetResourcePositionRequestRequestTypeDef",
    "GetResourcePositionResponseTypeDef",
    "GetServiceEndpointRequestRequestTypeDef",
    "GetServiceEndpointResponseTypeDef",
    "GetServiceProfileRequestRequestTypeDef",
    "GetServiceProfileResponseTypeDef",
    "GetWirelessDeviceRequestRequestTypeDef",
    "GetWirelessDeviceResponseTypeDef",
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    "GetWirelessDeviceStatisticsResponseTypeDef",
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    "GetWirelessGatewayCertificateResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    "GetWirelessGatewayRequestRequestTypeDef",
    "GetWirelessGatewayResponseTypeDef",
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    "GetWirelessGatewayStatisticsResponseTypeDef",
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    "GetWirelessGatewayTaskResponseTypeDef",
    "GlobalIdentityTypeDef",
    "GnssTypeDef",
    "GsmLocalIdTypeDef",
    "GsmNmrObjTypeDef",
    "GsmObjTypeDef",
    "IpTypeDef",
    "JoinEventConfigurationTypeDef",
    "JoinResourceTypeEventConfigurationTypeDef",
    "ListDestinationsRequestRequestTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesRequestRequestTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "ListEventConfigurationsRequestRequestTypeDef",
    "ListEventConfigurationsResponseTypeDef",
    "ListFuotaTasksRequestRequestTypeDef",
    "ListFuotaTasksResponseTypeDef",
    "ListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    "ListMulticastGroupsRequestRequestTypeDef",
    "ListMulticastGroupsResponseTypeDef",
    "ListNetworkAnalyzerConfigurationsRequestRequestTypeDef",
    "ListNetworkAnalyzerConfigurationsResponseTypeDef",
    "ListPartnerAccountsRequestRequestTypeDef",
    "ListPartnerAccountsResponseTypeDef",
    "ListPositionConfigurationsRequestRequestTypeDef",
    "ListPositionConfigurationsResponseTypeDef",
    "ListQueuedMessagesRequestRequestTypeDef",
    "ListQueuedMessagesResponseTypeDef",
    "ListServiceProfilesRequestRequestTypeDef",
    "ListServiceProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWirelessDevicesRequestRequestTypeDef",
    "ListWirelessDevicesResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    "ListWirelessGatewaysRequestRequestTypeDef",
    "ListWirelessGatewaysResponseTypeDef",
    "LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef",
    "LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef",
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANDeviceTypeDef",
    "LoRaWANFuotaTaskGetInfoTypeDef",
    "LoRaWANFuotaTaskTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANGatewayTypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "LoRaWANJoinEventNotificationConfigurationsTypeDef",
    "LoRaWANJoinResourceTypeEventConfigurationTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANMulticastGetTypeDef",
    "LoRaWANMulticastMetadataTypeDef",
    "LoRaWANMulticastSessionTypeDef",
    "LoRaWANMulticastTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANStartFuotaTaskTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "LteLocalIdTypeDef",
    "LteNmrObjTypeDef",
    "LteObjTypeDef",
    "MessageDeliveryStatusEventConfigurationTypeDef",
    "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
    "MulticastGroupByFuotaTaskTypeDef",
    "MulticastGroupTypeDef",
    "MulticastWirelessMetadataTypeDef",
    "NetworkAnalyzerConfigurationsTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "ParticipatingGatewaysTypeDef",
    "PositionConfigurationItemTypeDef",
    "PositionSolverConfigurationsTypeDef",
    "PositionSolverDetailsTypeDef",
    "PositioningTypeDef",
    "ProximityEventConfigurationTypeDef",
    "ProximityResourceTypeEventConfigurationTypeDef",
    "PutPositionConfigurationRequestRequestTypeDef",
    "PutResourceLogLevelRequestRequestTypeDef",
    "ResetResourceLogLevelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SemtechGnssConfigurationTypeDef",
    "SemtechGnssDetailTypeDef",
    "SendDataToMulticastGroupRequestRequestTypeDef",
    "SendDataToMulticastGroupResponseTypeDef",
    "SendDataToWirelessDeviceRequestRequestTypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkEventNotificationConfigurationsTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkResourceTypeEventConfigurationTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "StartFuotaTaskRequestRequestTypeDef",
    "StartMulticastGroupSessionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TdscdmaLocalIdTypeDef",
    "TdscdmaNmrObjTypeDef",
    "TdscdmaObjTypeDef",
    "TestWirelessDeviceRequestRequestTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "TraceContentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAbpV1_0_xTypeDef",
    "UpdateAbpV1_1TypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdateEventConfigurationByResourceTypesRequestRequestTypeDef",
    "UpdateFPortsTypeDef",
    "UpdateFuotaTaskRequestRequestTypeDef",
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    "UpdateMulticastGroupRequestRequestTypeDef",
    "UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "UpdatePartnerAccountRequestRequestTypeDef",
    "UpdatePositionRequestRequestTypeDef",
    "UpdateResourceEventConfigurationRequestRequestTypeDef",
    "UpdateResourcePositionRequestRequestTypeDef",
    "UpdateWirelessDeviceRequestRequestTypeDef",
    "UpdateWirelessGatewayRequestRequestTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "WcdmaLocalIdTypeDef",
    "WcdmaNmrObjTypeDef",
    "WcdmaObjTypeDef",
    "WiFiAccessPointTypeDef",
    "WirelessDeviceEventLogOptionTypeDef",
    "WirelessDeviceLogOptionTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "WirelessGatewayEventLogOptionTypeDef",
    "WirelessGatewayLogOptionTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "WirelessMetadataTypeDef",
)

AbpV1_0_xTypeDef = TypedDict(
    "AbpV1_0_xTypeDef",
    {
        "DevAddr": str,
        "SessionKeys": "SessionKeysAbpV1_0_xTypeDef",
        "FCntStart": int,
    },
    total=False,
)

AbpV1_1TypeDef = TypedDict(
    "AbpV1_1TypeDef",
    {
        "DevAddr": str,
        "SessionKeys": "SessionKeysAbpV1_1TypeDef",
        "FCntStart": int,
    },
    total=False,
)

AccuracyTypeDef = TypedDict(
    "AccuracyTypeDef",
    {
        "HorizontalAccuracy": float,
        "VerticalAccuracy": float,
    },
    total=False,
)

ApplicationConfigTypeDef = TypedDict(
    "ApplicationConfigTypeDef",
    {
        "FPort": int,
        "Type": Literal["SemtechGeolocation"],
        "DestinationName": str,
    },
    total=False,
)

_RequiredAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
    },
)
_OptionalAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef(
    _RequiredAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef,
    _OptionalAssociateAwsAccountWithPartnerAccountRequestRequestTypeDef,
):
    pass

AssociateAwsAccountWithPartnerAccountResponseTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)

AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

AssociateWirelessDeviceWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

AssociateWirelessGatewayWithCertificateRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    {
        "Id": str,
        "IotCertificateId": str,
    },
)

AssociateWirelessGatewayWithCertificateResponseTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateWirelessGatewayWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

BeaconingTypeDef = TypedDict(
    "BeaconingTypeDef",
    {
        "DataRate": int,
        "Frequencies": List[int],
    },
    total=False,
)

CancelMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

CdmaLocalIdTypeDef = TypedDict(
    "CdmaLocalIdTypeDef",
    {
        "PnOffset": int,
        "CdmaChannel": int,
    },
)

_RequiredCdmaNmrObjTypeDef = TypedDict(
    "_RequiredCdmaNmrObjTypeDef",
    {
        "PnOffset": int,
        "CdmaChannel": int,
    },
)
_OptionalCdmaNmrObjTypeDef = TypedDict(
    "_OptionalCdmaNmrObjTypeDef",
    {
        "PilotPower": int,
        "BaseStationId": int,
    },
    total=False,
)

class CdmaNmrObjTypeDef(_RequiredCdmaNmrObjTypeDef, _OptionalCdmaNmrObjTypeDef):
    pass

_RequiredCdmaObjTypeDef = TypedDict(
    "_RequiredCdmaObjTypeDef",
    {
        "SystemId": int,
        "NetworkId": int,
        "BaseStationId": int,
    },
)
_OptionalCdmaObjTypeDef = TypedDict(
    "_OptionalCdmaObjTypeDef",
    {
        "RegistrationZone": int,
        "CdmaLocalId": "CdmaLocalIdTypeDef",
        "PilotPower": int,
        "BaseLat": float,
        "BaseLng": float,
        "CdmaNmr": List["CdmaNmrObjTypeDef"],
    },
    total=False,
)

class CdmaObjTypeDef(_RequiredCdmaObjTypeDef, _OptionalCdmaObjTypeDef):
    pass

CellTowersTypeDef = TypedDict(
    "CellTowersTypeDef",
    {
        "Gsm": List["GsmObjTypeDef"],
        "Wcdma": List["WcdmaObjTypeDef"],
        "Tdscdma": List["TdscdmaObjTypeDef"],
        "Lte": List["LteObjTypeDef"],
        "Cdma": List["CdmaObjTypeDef"],
    },
    total=False,
)

CertificateListTypeDef = TypedDict(
    "CertificateListTypeDef",
    {
        "SigningAlg": SigningAlgType,
        "Value": str,
    },
)

ConnectionStatusEventConfigurationTypeDef = TypedDict(
    "ConnectionStatusEventConfigurationTypeDef",
    {
        "LoRaWAN": "LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef",
        "WirelessGatewayIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

ConnectionStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "ConnectionStatusResourceTypeEventConfigurationTypeDef",
    {
        "LoRaWAN": "LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

_RequiredCreateDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "RoleArn": str,
    },
)
_OptionalCreateDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDestinationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateDestinationRequestRequestTypeDef(
    _RequiredCreateDestinationRequestRequestTypeDef, _OptionalCreateDestinationRequestRequestTypeDef
):
    pass

CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceProfileRequestRequestTypeDef = TypedDict(
    "CreateDeviceProfileRequestRequestTypeDef",
    {
        "Name": str,
        "LoRaWAN": "LoRaWANDeviceProfileTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

CreateDeviceProfileResponseTypeDef = TypedDict(
    "CreateDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFuotaTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFuotaTaskRequestRequestTypeDef",
    {
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
    },
)
_OptionalCreateFuotaTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFuotaTaskRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ClientRequestToken": str,
        "LoRaWAN": "LoRaWANFuotaTaskTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFuotaTaskRequestRequestTypeDef(
    _RequiredCreateFuotaTaskRequestRequestTypeDef, _OptionalCreateFuotaTaskRequestRequestTypeDef
):
    pass

CreateFuotaTaskResponseTypeDef = TypedDict(
    "CreateFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMulticastGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMulticastGroupRequestRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANMulticastTypeDef",
    },
)
_OptionalCreateMulticastGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMulticastGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMulticastGroupRequestRequestTypeDef(
    _RequiredCreateMulticastGroupRequestRequestTypeDef,
    _OptionalCreateMulticastGroupRequestRequestTypeDef,
):
    pass

CreateMulticastGroupResponseTypeDef = TypedDict(
    "CreateMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "TraceContent": "TraceContentTypeDef",
        "WirelessDevices": List[str],
        "WirelessGateways": List[str],
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateNetworkAnalyzerConfigurationRequestRequestTypeDef(
    _RequiredCreateNetworkAnalyzerConfigurationRequestRequestTypeDef,
    _OptionalCreateNetworkAnalyzerConfigurationRequestRequestTypeDef,
):
    pass

CreateNetworkAnalyzerConfigurationResponseTypeDef = TypedDict(
    "CreateNetworkAnalyzerConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceProfileRequestRequestTypeDef = TypedDict(
    "CreateServiceProfileRequestRequestTypeDef",
    {
        "Name": str,
        "LoRaWAN": "LoRaWANServiceProfileTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

CreateServiceProfileResponseTypeDef = TypedDict(
    "CreateServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessDeviceRequestRequestTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "DestinationName": str,
    },
)
_OptionalCreateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessDeviceRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ClientRequestToken": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Tags": List["TagTypeDef"],
        "Positioning": PositioningConfigStatusType,
    },
    total=False,
)

class CreateWirelessDeviceRequestRequestTypeDef(
    _RequiredCreateWirelessDeviceRequestRequestTypeDef,
    _OptionalCreateWirelessDeviceRequestRequestTypeDef,
):
    pass

CreateWirelessDeviceResponseTypeDef = TypedDict(
    "CreateWirelessDeviceResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessGatewayRequestRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayTypeDef",
    },
)
_OptionalCreateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessGatewayRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateWirelessGatewayRequestRequestTypeDef(
    _RequiredCreateWirelessGatewayRequestRequestTypeDef,
    _OptionalCreateWirelessGatewayRequestRequestTypeDef,
):
    pass

CreateWirelessGatewayResponseTypeDef = TypedDict(
    "CreateWirelessGatewayResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "AutoCreateTasks": bool,
    },
)
_OptionalCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Name": str,
        "Update": "UpdateWirelessGatewayTaskCreateTypeDef",
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef(
    _RequiredCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef,
    _OptionalCreateWirelessGatewayTaskDefinitionRequestRequestTypeDef,
):
    pass

CreateWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessGatewayTaskDefinitionId": str,
    },
)

CreateWirelessGatewayTaskResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayTaskDefinitionId": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDeviceProfileRequestRequestTypeDef = TypedDict(
    "DeleteDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteFuotaTaskRequestRequestTypeDef = TypedDict(
    "DeleteFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteMulticastGroupRequestRequestTypeDef = TypedDict(
    "DeleteMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)

_RequiredDeleteQueuedMessagesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
        "MessageId": str,
    },
)
_OptionalDeleteQueuedMessagesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteQueuedMessagesRequestRequestTypeDef",
    {
        "WirelessDeviceType": WirelessDeviceTypeType,
    },
    total=False,
)

class DeleteQueuedMessagesRequestRequestTypeDef(
    _RequiredDeleteQueuedMessagesRequestRequestTypeDef,
    _OptionalDeleteQueuedMessagesRequestRequestTypeDef,
):
    pass

DeleteServiceProfileRequestRequestTypeDef = TypedDict(
    "DeleteServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessDeviceRequestRequestTypeDef = TypedDict(
    "DeleteWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DestinationsTypeDef = TypedDict(
    "DestinationsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)

DeviceProfileTypeDef = TypedDict(
    "DeviceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
    },
    total=False,
)

DeviceRegistrationStateEventConfigurationTypeDef = TypedDict(
    "DeviceRegistrationStateEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkEventNotificationConfigurationsTypeDef",
        "WirelessDeviceIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

DeviceRegistrationStateResourceTypeEventConfigurationTypeDef = TypedDict(
    "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef = TypedDict(
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)

DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

DisassociateWirelessDeviceFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DownlinkQueueMessageTypeDef = TypedDict(
    "DownlinkQueueMessageTypeDef",
    {
        "MessageId": str,
        "TransmitMode": int,
        "ReceivedAt": str,
        "LoRaWAN": "LoRaWANSendDataToDeviceTypeDef",
    },
    total=False,
)

EventConfigurationItemTypeDef = TypedDict(
    "EventConfigurationItemTypeDef",
    {
        "Identifier": str,
        "IdentifierType": IdentifierTypeType,
        "PartnerType": Literal["Sidewalk"],
        "Events": "EventNotificationItemConfigurationsTypeDef",
    },
    total=False,
)

EventNotificationItemConfigurationsTypeDef = TypedDict(
    "EventNotificationItemConfigurationsTypeDef",
    {
        "DeviceRegistrationState": "DeviceRegistrationStateEventConfigurationTypeDef",
        "Proximity": "ProximityEventConfigurationTypeDef",
        "Join": "JoinEventConfigurationTypeDef",
        "ConnectionStatus": "ConnectionStatusEventConfigurationTypeDef",
        "MessageDeliveryStatus": "MessageDeliveryStatusEventConfigurationTypeDef",
    },
    total=False,
)

FPortsTypeDef = TypedDict(
    "FPortsTypeDef",
    {
        "Fuota": int,
        "Multicast": int,
        "ClockSync": int,
        "Positioning": "PositioningTypeDef",
        "Applications": List["ApplicationConfigTypeDef"],
    },
    total=False,
)

FuotaTaskTypeDef = TypedDict(
    "FuotaTaskTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

GatewayListItemTypeDef = TypedDict(
    "GatewayListItemTypeDef",
    {
        "GatewayId": str,
        "DownlinkFrequency": int,
    },
)

GetDestinationRequestRequestTypeDef = TypedDict(
    "GetDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Expression": str,
        "ExpressionType": ExpressionTypeType,
        "Description": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceProfileRequestRequestTypeDef = TypedDict(
    "GetDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetDeviceProfileResponseTypeDef = TypedDict(
    "GetDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANDeviceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventConfigurationByResourceTypesResponseTypeDef = TypedDict(
    "GetEventConfigurationByResourceTypesResponseTypeDef",
    {
        "DeviceRegistrationState": "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
        "Proximity": "ProximityResourceTypeEventConfigurationTypeDef",
        "Join": "JoinResourceTypeEventConfigurationTypeDef",
        "ConnectionStatus": "ConnectionStatusResourceTypeEventConfigurationTypeDef",
        "MessageDeliveryStatus": "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFuotaTaskRequestRequestTypeDef = TypedDict(
    "GetFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFuotaTaskResponseTypeDef = TypedDict(
    "GetFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Status": FuotaTaskStatusType,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANFuotaTaskGetInfoTypeDef",
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogLevelsByResourceTypesResponseTypeDef = TypedDict(
    "GetLogLevelsByResourceTypesResponseTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMulticastGroupRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetMulticastGroupResponseTypeDef = TypedDict(
    "GetMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": str,
        "LoRaWAN": "LoRaWANMulticastGetTypeDef",
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetMulticastGroupSessionResponseTypeDef = TypedDict(
    "GetMulticastGroupSessionResponseTypeDef",
    {
        "LoRaWAN": "LoRaWANMulticastSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)

GetNetworkAnalyzerConfigurationResponseTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    {
        "TraceContent": "TraceContentTypeDef",
        "WirelessDevices": List[str],
        "WirelessGateways": List[str],
        "Description": str,
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartnerAccountRequestRequestTypeDef = TypedDict(
    "GetPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

GetPartnerAccountResponseTypeDef = TypedDict(
    "GetPartnerAccountResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoWithFingerprintTypeDef",
        "AccountLinked": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPositionConfigurationRequestRequestTypeDef = TypedDict(
    "GetPositionConfigurationRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)

GetPositionConfigurationResponseTypeDef = TypedDict(
    "GetPositionConfigurationResponseTypeDef",
    {
        "Solvers": "PositionSolverDetailsTypeDef",
        "Destination": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPositionEstimateRequestRequestTypeDef = TypedDict(
    "GetPositionEstimateRequestRequestTypeDef",
    {
        "WiFiAccessPoints": List["WiFiAccessPointTypeDef"],
        "CellTowers": "CellTowersTypeDef",
        "Ip": "IpTypeDef",
        "Gnss": "GnssTypeDef",
        "Timestamp": Union[datetime, str],
    },
    total=False,
)

GetPositionEstimateResponseTypeDef = TypedDict(
    "GetPositionEstimateResponseTypeDef",
    {
        "GeoJsonPayload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPositionRequestRequestTypeDef = TypedDict(
    "GetPositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)

GetPositionResponseTypeDef = TypedDict(
    "GetPositionResponseTypeDef",
    {
        "Position": List[float],
        "Accuracy": "AccuracyTypeDef",
        "SolverType": Literal["GNSS"],
        "SolverProvider": Literal["Semtech"],
        "SolverVersion": str,
        "Timestamp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": IdentifierTypeType,
    },
)
_OptionalGetResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceEventConfigurationRequestRequestTypeDef",
    {
        "PartnerType": Literal["Sidewalk"],
    },
    total=False,
)

class GetResourceEventConfigurationRequestRequestTypeDef(
    _RequiredGetResourceEventConfigurationRequestRequestTypeDef,
    _OptionalGetResourceEventConfigurationRequestRequestTypeDef,
):
    pass

GetResourceEventConfigurationResponseTypeDef = TypedDict(
    "GetResourceEventConfigurationResponseTypeDef",
    {
        "DeviceRegistrationState": "DeviceRegistrationStateEventConfigurationTypeDef",
        "Proximity": "ProximityEventConfigurationTypeDef",
        "Join": "JoinEventConfigurationTypeDef",
        "ConnectionStatus": "ConnectionStatusEventConfigurationTypeDef",
        "MessageDeliveryStatus": "MessageDeliveryStatusEventConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "GetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)

GetResourceLogLevelResponseTypeDef = TypedDict(
    "GetResourceLogLevelResponseTypeDef",
    {
        "LogLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePositionRequestRequestTypeDef = TypedDict(
    "GetResourcePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)

GetResourcePositionResponseTypeDef = TypedDict(
    "GetResourcePositionResponseTypeDef",
    {
        "GeoJsonPayload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceEndpointRequestRequestTypeDef = TypedDict(
    "GetServiceEndpointRequestRequestTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
    },
    total=False,
)

GetServiceEndpointResponseTypeDef = TypedDict(
    "GetServiceEndpointResponseTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
        "ServiceEndpoint": str,
        "ServerTrust": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceProfileRequestRequestTypeDef = TypedDict(
    "GetServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceProfileResponseTypeDef = TypedDict(
    "GetServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANGetServiceProfileInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessDeviceIdTypeType,
    },
)

GetWirelessDeviceResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Sidewalk": "SidewalkDeviceTypeDef",
        "Positioning": PositioningConfigStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    {
        "WirelessDeviceId": str,
    },
)

GetWirelessDeviceStatisticsResponseTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsResponseTypeDef",
    {
        "WirelessDeviceId": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANDeviceMetadataTypeDef",
        "Sidewalk": "SidewalkDeviceMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayCertificateRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayCertificateResponseTypeDef = TypedDict(
    "GetWirelessGatewayCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "LoRaWANNetworkServerCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayFirmwareInformationRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayFirmwareInformationResponseTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayCurrentVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessGatewayIdTypeType,
    },
)

GetWirelessGatewayResponseTypeDef = TypedDict(
    "GetWirelessGatewayResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    {
        "WirelessGatewayId": str,
    },
)

GetWirelessGatewayStatisticsResponseTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "LastUplinkReceivedAt": str,
        "ConnectionStatus": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": str,
        "Update": "UpdateWirelessGatewayTaskCreateTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "WirelessGatewayTaskDefinitionId": str,
        "LastUplinkReceivedAt": str,
        "TaskCreatedAt": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalIdentityTypeDef = TypedDict(
    "GlobalIdentityTypeDef",
    {
        "Lac": int,
        "GeranCid": int,
    },
)

_RequiredGnssTypeDef = TypedDict(
    "_RequiredGnssTypeDef",
    {
        "Payload": str,
    },
)
_OptionalGnssTypeDef = TypedDict(
    "_OptionalGnssTypeDef",
    {
        "CaptureTime": float,
        "CaptureTimeAccuracy": float,
        "AssistPosition": List[float],
        "AssistAltitude": float,
        "Use2DSolver": bool,
    },
    total=False,
)

class GnssTypeDef(_RequiredGnssTypeDef, _OptionalGnssTypeDef):
    pass

GsmLocalIdTypeDef = TypedDict(
    "GsmLocalIdTypeDef",
    {
        "Bsic": int,
        "Bcch": int,
    },
)

_RequiredGsmNmrObjTypeDef = TypedDict(
    "_RequiredGsmNmrObjTypeDef",
    {
        "Bsic": int,
        "Bcch": int,
    },
)
_OptionalGsmNmrObjTypeDef = TypedDict(
    "_OptionalGsmNmrObjTypeDef",
    {
        "RxLevel": int,
        "GlobalIdentity": "GlobalIdentityTypeDef",
    },
    total=False,
)

class GsmNmrObjTypeDef(_RequiredGsmNmrObjTypeDef, _OptionalGsmNmrObjTypeDef):
    pass

_RequiredGsmObjTypeDef = TypedDict(
    "_RequiredGsmObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "Lac": int,
        "GeranCid": int,
    },
)
_OptionalGsmObjTypeDef = TypedDict(
    "_OptionalGsmObjTypeDef",
    {
        "GsmLocalId": "GsmLocalIdTypeDef",
        "GsmTimingAdvance": int,
        "RxLevel": int,
        "GsmNmr": List["GsmNmrObjTypeDef"],
    },
    total=False,
)

class GsmObjTypeDef(_RequiredGsmObjTypeDef, _OptionalGsmObjTypeDef):
    pass

IpTypeDef = TypedDict(
    "IpTypeDef",
    {
        "IpAddress": str,
    },
)

JoinEventConfigurationTypeDef = TypedDict(
    "JoinEventConfigurationTypeDef",
    {
        "LoRaWAN": "LoRaWANJoinEventNotificationConfigurationsTypeDef",
        "WirelessDeviceIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

JoinResourceTypeEventConfigurationTypeDef = TypedDict(
    "JoinResourceTypeEventConfigurationTypeDef",
    {
        "LoRaWAN": "LoRaWANJoinResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

ListDestinationsRequestRequestTypeDef = TypedDict(
    "ListDestinationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {
        "NextToken": str,
        "DestinationList": List["DestinationsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceProfilesRequestRequestTypeDef = TypedDict(
    "ListDeviceProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDeviceProfilesResponseTypeDef = TypedDict(
    "ListDeviceProfilesResponseTypeDef",
    {
        "NextToken": str,
        "DeviceProfileList": List["DeviceProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventConfigurationsRequestRequestTypeDef",
    {
        "ResourceType": EventNotificationResourceTypeType,
    },
)
_OptionalListEventConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEventConfigurationsRequestRequestTypeDef(
    _RequiredListEventConfigurationsRequestRequestTypeDef,
    _OptionalListEventConfigurationsRequestRequestTypeDef,
):
    pass

ListEventConfigurationsResponseTypeDef = TypedDict(
    "ListEventConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "EventConfigurationsList": List["EventConfigurationItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFuotaTasksRequestRequestTypeDef = TypedDict(
    "ListFuotaTasksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFuotaTasksResponseTypeDef = TypedDict(
    "ListFuotaTasksResponseTypeDef",
    {
        "NextToken": str,
        "FuotaTaskList": List["FuotaTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMulticastGroupsByFuotaTaskRequestRequestTypeDef = TypedDict(
    "_RequiredListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalListMulticastGroupsByFuotaTaskRequestRequestTypeDef = TypedDict(
    "_OptionalListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMulticastGroupsByFuotaTaskRequestRequestTypeDef(
    _RequiredListMulticastGroupsByFuotaTaskRequestRequestTypeDef,
    _OptionalListMulticastGroupsByFuotaTaskRequestRequestTypeDef,
):
    pass

ListMulticastGroupsByFuotaTaskResponseTypeDef = TypedDict(
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    {
        "NextToken": str,
        "MulticastGroupList": List["MulticastGroupByFuotaTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMulticastGroupsRequestRequestTypeDef = TypedDict(
    "ListMulticastGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMulticastGroupsResponseTypeDef = TypedDict(
    "ListMulticastGroupsResponseTypeDef",
    {
        "NextToken": str,
        "MulticastGroupList": List["MulticastGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworkAnalyzerConfigurationsRequestRequestTypeDef = TypedDict(
    "ListNetworkAnalyzerConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListNetworkAnalyzerConfigurationsResponseTypeDef = TypedDict(
    "ListNetworkAnalyzerConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "NetworkAnalyzerConfigurationList": List["NetworkAnalyzerConfigurationsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerAccountsRequestRequestTypeDef = TypedDict(
    "ListPartnerAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPartnerAccountsResponseTypeDef = TypedDict(
    "ListPartnerAccountsResponseTypeDef",
    {
        "NextToken": str,
        "Sidewalk": List["SidewalkAccountInfoWithFingerprintTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPositionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPositionConfigurationsRequestRequestTypeDef",
    {
        "ResourceType": PositionResourceTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPositionConfigurationsResponseTypeDef = TypedDict(
    "ListPositionConfigurationsResponseTypeDef",
    {
        "PositionConfigurationList": List["PositionConfigurationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuedMessagesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalListQueuedMessagesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueuedMessagesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WirelessDeviceType": WirelessDeviceTypeType,
    },
    total=False,
)

class ListQueuedMessagesRequestRequestTypeDef(
    _RequiredListQueuedMessagesRequestRequestTypeDef,
    _OptionalListQueuedMessagesRequestRequestTypeDef,
):
    pass

ListQueuedMessagesResponseTypeDef = TypedDict(
    "ListQueuedMessagesResponseTypeDef",
    {
        "NextToken": str,
        "DownlinkQueueMessagesList": List["DownlinkQueueMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceProfilesRequestRequestTypeDef = TypedDict(
    "ListServiceProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServiceProfilesResponseTypeDef = TypedDict(
    "ListServiceProfilesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceProfileList": List["ServiceProfileTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessDevicesRequestRequestTypeDef = TypedDict(
    "ListWirelessDevicesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "DestinationName": str,
        "DeviceProfileId": str,
        "ServiceProfileId": str,
        "WirelessDeviceType": WirelessDeviceTypeType,
        "FuotaTaskId": str,
        "MulticastGroupId": str,
    },
    total=False,
)

ListWirelessDevicesResponseTypeDef = TypedDict(
    "ListWirelessDevicesResponseTypeDef",
    {
        "NextToken": str,
        "WirelessDeviceList": List["WirelessDeviceStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "TaskDefinitionType": Literal["UPDATE"],
    },
    total=False,
)

ListWirelessGatewayTaskDefinitionsResponseTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    {
        "NextToken": str,
        "TaskDefinitions": List["UpdateWirelessGatewayTaskEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewaysRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewaysRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWirelessGatewaysResponseTypeDef = TypedDict(
    "ListWirelessGatewaysResponseTypeDef",
    {
        "NextToken": str,
        "WirelessGatewayList": List["WirelessGatewayStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef = TypedDict(
    "LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef",
    {
        "GatewayEuiEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef",
    {
        "WirelessGatewayEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

LoRaWANDeviceMetadataTypeDef = TypedDict(
    "LoRaWANDeviceMetadataTypeDef",
    {
        "DevEui": str,
        "FPort": int,
        "DataRate": int,
        "Frequency": int,
        "Timestamp": str,
        "Gateways": List["LoRaWANGatewayMetadataTypeDef"],
    },
    total=False,
)

LoRaWANDeviceProfileTypeDef = TypedDict(
    "LoRaWANDeviceProfileTypeDef",
    {
        "SupportsClassB": bool,
        "ClassBTimeout": int,
        "PingSlotPeriod": int,
        "PingSlotDr": int,
        "PingSlotFreq": int,
        "SupportsClassC": bool,
        "ClassCTimeout": int,
        "MacVersion": str,
        "RegParamsRevision": str,
        "RxDelay1": int,
        "RxDrOffset1": int,
        "RxDataRate2": int,
        "RxFreq2": int,
        "FactoryPresetFreqsList": List[int],
        "MaxEirp": int,
        "MaxDutyCycle": int,
        "RfRegion": str,
        "SupportsJoin": bool,
        "Supports32BitFCnt": bool,
    },
    total=False,
)

LoRaWANDeviceTypeDef = TypedDict(
    "LoRaWANDeviceTypeDef",
    {
        "DevEui": str,
        "DeviceProfileId": str,
        "ServiceProfileId": str,
        "OtaaV1_1": "OtaaV1_1TypeDef",
        "OtaaV1_0_x": "OtaaV1_0_xTypeDef",
        "AbpV1_1": "AbpV1_1TypeDef",
        "AbpV1_0_x": "AbpV1_0_xTypeDef",
        "FPorts": "FPortsTypeDef",
    },
    total=False,
)

LoRaWANFuotaTaskGetInfoTypeDef = TypedDict(
    "LoRaWANFuotaTaskGetInfoTypeDef",
    {
        "RfRegion": str,
        "StartTime": datetime,
    },
    total=False,
)

LoRaWANFuotaTaskTypeDef = TypedDict(
    "LoRaWANFuotaTaskTypeDef",
    {
        "RfRegion": SupportedRfRegionType,
    },
    total=False,
)

LoRaWANGatewayCurrentVersionTypeDef = TypedDict(
    "LoRaWANGatewayCurrentVersionTypeDef",
    {
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

LoRaWANGatewayMetadataTypeDef = TypedDict(
    "LoRaWANGatewayMetadataTypeDef",
    {
        "GatewayEui": str,
        "Snr": float,
        "Rssi": float,
    },
    total=False,
)

LoRaWANGatewayTypeDef = TypedDict(
    "LoRaWANGatewayTypeDef",
    {
        "GatewayEui": str,
        "RfRegion": str,
        "JoinEuiFilters": List[List[str]],
        "NetIdFilters": List[str],
        "SubBands": List[int],
        "Beaconing": "BeaconingTypeDef",
    },
    total=False,
)

LoRaWANGatewayVersionTypeDef = TypedDict(
    "LoRaWANGatewayVersionTypeDef",
    {
        "PackageVersion": str,
        "Model": str,
        "Station": str,
    },
    total=False,
)

LoRaWANGetServiceProfileInfoTypeDef = TypedDict(
    "LoRaWANGetServiceProfileInfoTypeDef",
    {
        "UlRate": int,
        "UlBucketSize": int,
        "UlRatePolicy": str,
        "DlRate": int,
        "DlBucketSize": int,
        "DlRatePolicy": str,
        "AddGwMetadata": bool,
        "DevStatusReqFreq": int,
        "ReportDevStatusBattery": bool,
        "ReportDevStatusMargin": bool,
        "DrMin": int,
        "DrMax": int,
        "ChannelMask": str,
        "PrAllowed": bool,
        "HrAllowed": bool,
        "RaAllowed": bool,
        "NwkGeoLoc": bool,
        "TargetPer": int,
        "MinGwDiversity": int,
    },
    total=False,
)

LoRaWANJoinEventNotificationConfigurationsTypeDef = TypedDict(
    "LoRaWANJoinEventNotificationConfigurationsTypeDef",
    {
        "DevEuiEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

LoRaWANJoinResourceTypeEventConfigurationTypeDef = TypedDict(
    "LoRaWANJoinResourceTypeEventConfigurationTypeDef",
    {
        "WirelessDeviceEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

LoRaWANListDeviceTypeDef = TypedDict(
    "LoRaWANListDeviceTypeDef",
    {
        "DevEui": str,
    },
    total=False,
)

LoRaWANMulticastGetTypeDef = TypedDict(
    "LoRaWANMulticastGetTypeDef",
    {
        "RfRegion": SupportedRfRegionType,
        "DlClass": DlClassType,
        "NumberOfDevicesRequested": int,
        "NumberOfDevicesInGroup": int,
    },
    total=False,
)

LoRaWANMulticastMetadataTypeDef = TypedDict(
    "LoRaWANMulticastMetadataTypeDef",
    {
        "FPort": int,
    },
    total=False,
)

LoRaWANMulticastSessionTypeDef = TypedDict(
    "LoRaWANMulticastSessionTypeDef",
    {
        "DlDr": int,
        "DlFreq": int,
        "SessionStartTime": datetime,
        "SessionTimeout": int,
    },
    total=False,
)

LoRaWANMulticastTypeDef = TypedDict(
    "LoRaWANMulticastTypeDef",
    {
        "RfRegion": SupportedRfRegionType,
        "DlClass": DlClassType,
    },
    total=False,
)

LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef",
    {
        "FPort": int,
        "ParticipatingGateways": "ParticipatingGatewaysTypeDef",
    },
    total=False,
)

LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef",
    {
        "AddGwMetadata": bool,
        "DrMin": int,
        "DrMax": int,
    },
    total=False,
)

LoRaWANStartFuotaTaskTypeDef = TypedDict(
    "LoRaWANStartFuotaTaskTypeDef",
    {
        "StartTime": Union[datetime, str],
    },
    total=False,
)

LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef",
    {
        "DeviceProfileId": str,
        "ServiceProfileId": str,
        "AbpV1_1": "UpdateAbpV1_1TypeDef",
        "AbpV1_0_x": "UpdateAbpV1_0_xTypeDef",
        "FPorts": "UpdateFPortsTypeDef",
    },
    total=False,
)

LoRaWANUpdateGatewayTaskCreateTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    {
        "UpdateSignature": str,
        "SigKeyCrc": int,
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
        "UpdateVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

LoRaWANUpdateGatewayTaskEntryTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    {
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
        "UpdateVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

LteLocalIdTypeDef = TypedDict(
    "LteLocalIdTypeDef",
    {
        "Pci": int,
        "Earfcn": int,
    },
)

_RequiredLteNmrObjTypeDef = TypedDict(
    "_RequiredLteNmrObjTypeDef",
    {
        "Pci": int,
        "Earfcn": int,
        "EutranCid": int,
    },
)
_OptionalLteNmrObjTypeDef = TypedDict(
    "_OptionalLteNmrObjTypeDef",
    {
        "Rsrp": int,
        "Rsrq": float,
    },
    total=False,
)

class LteNmrObjTypeDef(_RequiredLteNmrObjTypeDef, _OptionalLteNmrObjTypeDef):
    pass

_RequiredLteObjTypeDef = TypedDict(
    "_RequiredLteObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "EutranCid": int,
    },
)
_OptionalLteObjTypeDef = TypedDict(
    "_OptionalLteObjTypeDef",
    {
        "Tac": int,
        "LteLocalId": "LteLocalIdTypeDef",
        "LteTimingAdvance": int,
        "Rsrp": int,
        "Rsrq": float,
        "NrCapable": bool,
        "LteNmr": List["LteNmrObjTypeDef"],
    },
    total=False,
)

class LteObjTypeDef(_RequiredLteObjTypeDef, _OptionalLteObjTypeDef):
    pass

MessageDeliveryStatusEventConfigurationTypeDef = TypedDict(
    "MessageDeliveryStatusEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkEventNotificationConfigurationsTypeDef",
        "WirelessDeviceIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

MessageDeliveryStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

MulticastGroupByFuotaTaskTypeDef = TypedDict(
    "MulticastGroupByFuotaTaskTypeDef",
    {
        "Id": str,
    },
    total=False,
)

MulticastGroupTypeDef = TypedDict(
    "MulticastGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

MulticastWirelessMetadataTypeDef = TypedDict(
    "MulticastWirelessMetadataTypeDef",
    {
        "LoRaWAN": "LoRaWANMulticastMetadataTypeDef",
    },
    total=False,
)

NetworkAnalyzerConfigurationsTypeDef = TypedDict(
    "NetworkAnalyzerConfigurationsTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

OtaaV1_0_xTypeDef = TypedDict(
    "OtaaV1_0_xTypeDef",
    {
        "AppKey": str,
        "AppEui": str,
        "GenAppKey": str,
    },
    total=False,
)

OtaaV1_1TypeDef = TypedDict(
    "OtaaV1_1TypeDef",
    {
        "AppKey": str,
        "NwkKey": str,
        "JoinEui": str,
    },
    total=False,
)

ParticipatingGatewaysTypeDef = TypedDict(
    "ParticipatingGatewaysTypeDef",
    {
        "DownlinkMode": DownlinkModeType,
        "GatewayList": List["GatewayListItemTypeDef"],
        "TransmissionInterval": int,
    },
)

PositionConfigurationItemTypeDef = TypedDict(
    "PositionConfigurationItemTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
        "Solvers": "PositionSolverDetailsTypeDef",
        "Destination": str,
    },
    total=False,
)

PositionSolverConfigurationsTypeDef = TypedDict(
    "PositionSolverConfigurationsTypeDef",
    {
        "SemtechGnss": "SemtechGnssConfigurationTypeDef",
    },
    total=False,
)

PositionSolverDetailsTypeDef = TypedDict(
    "PositionSolverDetailsTypeDef",
    {
        "SemtechGnss": "SemtechGnssDetailTypeDef",
    },
    total=False,
)

PositioningTypeDef = TypedDict(
    "PositioningTypeDef",
    {
        "ClockSync": int,
        "Stream": int,
        "Gnss": int,
    },
    total=False,
)

ProximityEventConfigurationTypeDef = TypedDict(
    "ProximityEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkEventNotificationConfigurationsTypeDef",
        "WirelessDeviceIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

ProximityResourceTypeEventConfigurationTypeDef = TypedDict(
    "ProximityResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": "SidewalkResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

_RequiredPutPositionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutPositionConfigurationRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)
_OptionalPutPositionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutPositionConfigurationRequestRequestTypeDef",
    {
        "Solvers": "PositionSolverConfigurationsTypeDef",
        "Destination": str,
    },
    total=False,
)

class PutPositionConfigurationRequestRequestTypeDef(
    _RequiredPutPositionConfigurationRequestRequestTypeDef,
    _OptionalPutPositionConfigurationRequestRequestTypeDef,
):
    pass

PutResourceLogLevelRequestRequestTypeDef = TypedDict(
    "PutResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
        "LogLevel": LogLevelType,
    },
)

ResetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "ResetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)

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

SemtechGnssConfigurationTypeDef = TypedDict(
    "SemtechGnssConfigurationTypeDef",
    {
        "Status": PositionConfigurationStatusType,
        "Fec": PositionConfigurationFecType,
    },
)

SemtechGnssDetailTypeDef = TypedDict(
    "SemtechGnssDetailTypeDef",
    {
        "Provider": Literal["Semtech"],
        "Type": Literal["GNSS"],
        "Status": PositionConfigurationStatusType,
        "Fec": PositionConfigurationFecType,
    },
    total=False,
)

SendDataToMulticastGroupRequestRequestTypeDef = TypedDict(
    "SendDataToMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "PayloadData": str,
        "WirelessMetadata": "MulticastWirelessMetadataTypeDef",
    },
)

SendDataToMulticastGroupResponseTypeDef = TypedDict(
    "SendDataToMulticastGroupResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendDataToWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredSendDataToWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
        "TransmitMode": int,
        "PayloadData": str,
    },
)
_OptionalSendDataToWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalSendDataToWirelessDeviceRequestRequestTypeDef",
    {
        "WirelessMetadata": "WirelessMetadataTypeDef",
    },
    total=False,
)

class SendDataToWirelessDeviceRequestRequestTypeDef(
    _RequiredSendDataToWirelessDeviceRequestRequestTypeDef,
    _OptionalSendDataToWirelessDeviceRequestRequestTypeDef,
):
    pass

SendDataToWirelessDeviceResponseTypeDef = TypedDict(
    "SendDataToWirelessDeviceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceProfileTypeDef = TypedDict(
    "ServiceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
    },
    total=False,
)

SessionKeysAbpV1_0_xTypeDef = TypedDict(
    "SessionKeysAbpV1_0_xTypeDef",
    {
        "NwkSKey": str,
        "AppSKey": str,
    },
    total=False,
)

SessionKeysAbpV1_1TypeDef = TypedDict(
    "SessionKeysAbpV1_1TypeDef",
    {
        "FNwkSIntKey": str,
        "SNwkSIntKey": str,
        "NwkSEncKey": str,
        "AppSKey": str,
    },
    total=False,
)

SidewalkAccountInfoTypeDef = TypedDict(
    "SidewalkAccountInfoTypeDef",
    {
        "AmazonId": str,
        "AppServerPrivateKey": str,
    },
    total=False,
)

SidewalkAccountInfoWithFingerprintTypeDef = TypedDict(
    "SidewalkAccountInfoWithFingerprintTypeDef",
    {
        "AmazonId": str,
        "Fingerprint": str,
        "Arn": str,
    },
    total=False,
)

SidewalkDeviceMetadataTypeDef = TypedDict(
    "SidewalkDeviceMetadataTypeDef",
    {
        "Rssi": int,
        "BatteryLevel": BatteryLevelType,
        "Event": EventType,
        "DeviceState": DeviceStateType,
    },
    total=False,
)

SidewalkDeviceTypeDef = TypedDict(
    "SidewalkDeviceTypeDef",
    {
        "AmazonId": str,
        "SidewalkId": str,
        "SidewalkManufacturingSn": str,
        "DeviceCertificates": List["CertificateListTypeDef"],
    },
    total=False,
)

SidewalkEventNotificationConfigurationsTypeDef = TypedDict(
    "SidewalkEventNotificationConfigurationsTypeDef",
    {
        "AmazonIdEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

SidewalkListDeviceTypeDef = TypedDict(
    "SidewalkListDeviceTypeDef",
    {
        "AmazonId": str,
        "SidewalkId": str,
        "SidewalkManufacturingSn": str,
        "DeviceCertificates": List["CertificateListTypeDef"],
    },
    total=False,
)

SidewalkResourceTypeEventConfigurationTypeDef = TypedDict(
    "SidewalkResourceTypeEventConfigurationTypeDef",
    {
        "WirelessDeviceEventTopic": EventNotificationTopicStatusType,
    },
    total=False,
)

SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef",
    {
        "Seq": int,
        "MessageType": MessageTypeType,
        "AckModeRetryDurationSecs": int,
    },
    total=False,
)

SidewalkUpdateAccountTypeDef = TypedDict(
    "SidewalkUpdateAccountTypeDef",
    {
        "AppServerPrivateKey": str,
    },
    total=False,
)

_RequiredStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "_RequiredStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "_OptionalStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "QueryString": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef(
    _RequiredStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef,
    _OptionalStartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef,
):
    pass

_RequiredStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "_RequiredStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "_OptionalStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "QueryString": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef(
    _RequiredStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef,
    _OptionalStartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef,
):
    pass

_RequiredStartFuotaTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalStartFuotaTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartFuotaTaskRequestRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANStartFuotaTaskTypeDef",
    },
    total=False,
)

class StartFuotaTaskRequestRequestTypeDef(
    _RequiredStartFuotaTaskRequestRequestTypeDef, _OptionalStartFuotaTaskRequestRequestTypeDef
):
    pass

StartMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "StartMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
        "LoRaWAN": "LoRaWANMulticastSessionTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TdscdmaLocalIdTypeDef = TypedDict(
    "TdscdmaLocalIdTypeDef",
    {
        "Uarfcn": int,
        "CellParams": int,
    },
)

_RequiredTdscdmaNmrObjTypeDef = TypedDict(
    "_RequiredTdscdmaNmrObjTypeDef",
    {
        "Uarfcn": int,
        "CellParams": int,
    },
)
_OptionalTdscdmaNmrObjTypeDef = TypedDict(
    "_OptionalTdscdmaNmrObjTypeDef",
    {
        "UtranCid": int,
        "Rscp": int,
        "PathLoss": int,
    },
    total=False,
)

class TdscdmaNmrObjTypeDef(_RequiredTdscdmaNmrObjTypeDef, _OptionalTdscdmaNmrObjTypeDef):
    pass

_RequiredTdscdmaObjTypeDef = TypedDict(
    "_RequiredTdscdmaObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "UtranCid": int,
    },
)
_OptionalTdscdmaObjTypeDef = TypedDict(
    "_OptionalTdscdmaObjTypeDef",
    {
        "Lac": int,
        "TdscdmaLocalId": "TdscdmaLocalIdTypeDef",
        "TdscdmaTimingAdvance": int,
        "Rscp": int,
        "PathLoss": int,
        "TdscdmaNmr": List["TdscdmaNmrObjTypeDef"],
    },
    total=False,
)

class TdscdmaObjTypeDef(_RequiredTdscdmaObjTypeDef, _OptionalTdscdmaObjTypeDef):
    pass

TestWirelessDeviceRequestRequestTypeDef = TypedDict(
    "TestWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

TestWirelessDeviceResponseTypeDef = TypedDict(
    "TestWirelessDeviceResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TraceContentTypeDef = TypedDict(
    "TraceContentTypeDef",
    {
        "WirelessDeviceFrameInfo": WirelessDeviceFrameInfoType,
        "LogLevel": LogLevelType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAbpV1_0_xTypeDef = TypedDict(
    "UpdateAbpV1_0_xTypeDef",
    {
        "FCntStart": int,
    },
    total=False,
)

UpdateAbpV1_1TypeDef = TypedDict(
    "UpdateAbpV1_1TypeDef",
    {
        "FCntStart": int,
    },
    total=False,
)

_RequiredUpdateDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDestinationRequestRequestTypeDef",
    {
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)

class UpdateDestinationRequestRequestTypeDef(
    _RequiredUpdateDestinationRequestRequestTypeDef, _OptionalUpdateDestinationRequestRequestTypeDef
):
    pass

UpdateEventConfigurationByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateEventConfigurationByResourceTypesRequestRequestTypeDef",
    {
        "DeviceRegistrationState": "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
        "Proximity": "ProximityResourceTypeEventConfigurationTypeDef",
        "Join": "JoinResourceTypeEventConfigurationTypeDef",
        "ConnectionStatus": "ConnectionStatusResourceTypeEventConfigurationTypeDef",
        "MessageDeliveryStatus": "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
    },
    total=False,
)

UpdateFPortsTypeDef = TypedDict(
    "UpdateFPortsTypeDef",
    {
        "Positioning": "PositioningTypeDef",
        "Applications": List["ApplicationConfigTypeDef"],
    },
    total=False,
)

_RequiredUpdateFuotaTaskRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateFuotaTaskRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFuotaTaskRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANFuotaTaskTypeDef",
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
    },
    total=False,
)

class UpdateFuotaTaskRequestRequestTypeDef(
    _RequiredUpdateFuotaTaskRequestRequestTypeDef, _OptionalUpdateFuotaTaskRequestRequestTypeDef
):
    pass

UpdateLogLevelsByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
    },
    total=False,
)

_RequiredUpdateMulticastGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateMulticastGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMulticastGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANMulticastTypeDef",
    },
    total=False,
)

class UpdateMulticastGroupRequestRequestTypeDef(
    _RequiredUpdateMulticastGroupRequestRequestTypeDef,
    _OptionalUpdateMulticastGroupRequestRequestTypeDef,
):
    pass

_RequiredUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)
_OptionalUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "TraceContent": "TraceContentTypeDef",
        "WirelessDevicesToAdd": List[str],
        "WirelessDevicesToRemove": List[str],
        "WirelessGatewaysToAdd": List[str],
        "WirelessGatewaysToRemove": List[str],
        "Description": str,
    },
    total=False,
)

class UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef(
    _RequiredUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef,
    _OptionalUpdateNetworkAnalyzerConfigurationRequestRequestTypeDef,
):
    pass

UpdatePartnerAccountRequestRequestTypeDef = TypedDict(
    "UpdatePartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": "SidewalkUpdateAccountTypeDef",
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

UpdatePositionRequestRequestTypeDef = TypedDict(
    "UpdatePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
        "Position": List[float],
    },
)

_RequiredUpdateResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": IdentifierTypeType,
    },
)
_OptionalUpdateResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceEventConfigurationRequestRequestTypeDef",
    {
        "PartnerType": Literal["Sidewalk"],
        "DeviceRegistrationState": "DeviceRegistrationStateEventConfigurationTypeDef",
        "Proximity": "ProximityEventConfigurationTypeDef",
        "Join": "JoinEventConfigurationTypeDef",
        "ConnectionStatus": "ConnectionStatusEventConfigurationTypeDef",
        "MessageDeliveryStatus": "MessageDeliveryStatusEventConfigurationTypeDef",
    },
    total=False,
)

class UpdateResourceEventConfigurationRequestRequestTypeDef(
    _RequiredUpdateResourceEventConfigurationRequestRequestTypeDef,
    _OptionalUpdateResourceEventConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateResourcePositionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourcePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)
_OptionalUpdateResourcePositionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourcePositionRequestRequestTypeDef",
    {
        "GeoJsonPayload": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class UpdateResourcePositionRequestRequestTypeDef(
    _RequiredUpdateResourcePositionRequestRequestTypeDef,
    _OptionalUpdateResourcePositionRequestRequestTypeDef,
):
    pass

_RequiredUpdateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWirelessDeviceRequestRequestTypeDef",
    {
        "DestinationName": str,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANUpdateDeviceTypeDef",
        "Positioning": PositioningConfigStatusType,
    },
    total=False,
)

class UpdateWirelessDeviceRequestRequestTypeDef(
    _RequiredUpdateWirelessDeviceRequestRequestTypeDef,
    _OptionalUpdateWirelessDeviceRequestRequestTypeDef,
):
    pass

_RequiredUpdateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWirelessGatewayRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "JoinEuiFilters": List[List[str]],
        "NetIdFilters": List[str],
    },
    total=False,
)

class UpdateWirelessGatewayRequestRequestTypeDef(
    _RequiredUpdateWirelessGatewayRequestRequestTypeDef,
    _OptionalUpdateWirelessGatewayRequestRequestTypeDef,
):
    pass

UpdateWirelessGatewayTaskCreateTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskCreateTypeDef",
    {
        "UpdateDataSource": str,
        "UpdateDataRole": str,
        "LoRaWAN": "LoRaWANUpdateGatewayTaskCreateTypeDef",
    },
    total=False,
)

UpdateWirelessGatewayTaskEntryTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskEntryTypeDef",
    {
        "Id": str,
        "LoRaWAN": "LoRaWANUpdateGatewayTaskEntryTypeDef",
        "Arn": str,
    },
    total=False,
)

WcdmaLocalIdTypeDef = TypedDict(
    "WcdmaLocalIdTypeDef",
    {
        "Uarfcndl": int,
        "Psc": int,
    },
)

_RequiredWcdmaNmrObjTypeDef = TypedDict(
    "_RequiredWcdmaNmrObjTypeDef",
    {
        "Uarfcndl": int,
        "Psc": int,
        "UtranCid": int,
    },
)
_OptionalWcdmaNmrObjTypeDef = TypedDict(
    "_OptionalWcdmaNmrObjTypeDef",
    {
        "Rscp": int,
        "PathLoss": int,
    },
    total=False,
)

class WcdmaNmrObjTypeDef(_RequiredWcdmaNmrObjTypeDef, _OptionalWcdmaNmrObjTypeDef):
    pass

_RequiredWcdmaObjTypeDef = TypedDict(
    "_RequiredWcdmaObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "UtranCid": int,
    },
)
_OptionalWcdmaObjTypeDef = TypedDict(
    "_OptionalWcdmaObjTypeDef",
    {
        "Lac": int,
        "WcdmaLocalId": "WcdmaLocalIdTypeDef",
        "Rscp": int,
        "PathLoss": int,
        "WcdmaNmr": List["WcdmaNmrObjTypeDef"],
    },
    total=False,
)

class WcdmaObjTypeDef(_RequiredWcdmaObjTypeDef, _OptionalWcdmaObjTypeDef):
    pass

WiFiAccessPointTypeDef = TypedDict(
    "WiFiAccessPointTypeDef",
    {
        "MacAddress": str,
        "Rss": int,
    },
)

WirelessDeviceEventLogOptionTypeDef = TypedDict(
    "WirelessDeviceEventLogOptionTypeDef",
    {
        "Event": WirelessDeviceEventType,
        "LogLevel": LogLevelType,
    },
)

_RequiredWirelessDeviceLogOptionTypeDef = TypedDict(
    "_RequiredWirelessDeviceLogOptionTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "LogLevel": LogLevelType,
    },
)
_OptionalWirelessDeviceLogOptionTypeDef = TypedDict(
    "_OptionalWirelessDeviceLogOptionTypeDef",
    {
        "Events": List["WirelessDeviceEventLogOptionTypeDef"],
    },
    total=False,
)

class WirelessDeviceLogOptionTypeDef(
    _RequiredWirelessDeviceLogOptionTypeDef, _OptionalWirelessDeviceLogOptionTypeDef
):
    pass

WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "DestinationName": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANListDeviceTypeDef",
        "Sidewalk": "SidewalkListDeviceTypeDef",
        "FuotaDeviceStatus": FuotaDeviceStatusType,
        "MulticastDeviceStatus": str,
        "McGroupId": int,
    },
    total=False,
)

WirelessGatewayEventLogOptionTypeDef = TypedDict(
    "WirelessGatewayEventLogOptionTypeDef",
    {
        "Event": WirelessGatewayEventType,
        "LogLevel": LogLevelType,
    },
)

_RequiredWirelessGatewayLogOptionTypeDef = TypedDict(
    "_RequiredWirelessGatewayLogOptionTypeDef",
    {
        "Type": Literal["LoRaWAN"],
        "LogLevel": LogLevelType,
    },
)
_OptionalWirelessGatewayLogOptionTypeDef = TypedDict(
    "_OptionalWirelessGatewayLogOptionTypeDef",
    {
        "Events": List["WirelessGatewayEventLogOptionTypeDef"],
    },
    total=False,
)

class WirelessGatewayLogOptionTypeDef(
    _RequiredWirelessGatewayLogOptionTypeDef, _OptionalWirelessGatewayLogOptionTypeDef
):
    pass

WirelessGatewayStatisticsTypeDef = TypedDict(
    "WirelessGatewayStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "LastUplinkReceivedAt": str,
    },
    total=False,
)

WirelessMetadataTypeDef = TypedDict(
    "WirelessMetadataTypeDef",
    {
        "LoRaWAN": "LoRaWANSendDataToDeviceTypeDef",
        "Sidewalk": "SidewalkSendDataToDeviceTypeDef",
    },
    total=False,
)
