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
from typing import Any, Dict, List

from .literals import (
    BatteryLevelType,
    ConnectionStatusType,
    DeviceStateType,
    EventType,
    ExpressionTypeType,
    LogLevelType,
    MessageTypeType,
    SigningAlgType,
    WirelessDeviceEventType,
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
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    "CertificateListTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileRequestRequestTypeDef",
    "CreateDeviceProfileResponseTypeDef",
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
    "DeleteServiceProfileRequestRequestTypeDef",
    "DeleteWirelessDeviceRequestRequestTypeDef",
    "DeleteWirelessGatewayRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceProfileRequestRequestTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "GetLogLevelsByResourceTypesResponseTypeDef",
    "GetPartnerAccountRequestRequestTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "GetResourceLogLevelRequestRequestTypeDef",
    "GetResourceLogLevelResponseTypeDef",
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
    "ListDestinationsRequestRequestTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesRequestRequestTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "ListPartnerAccountsRequestRequestTypeDef",
    "ListPartnerAccountsResponseTypeDef",
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
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANDeviceTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANGatewayTypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "PutResourceLogLevelRequestRequestTypeDef",
    "ResetResourceLogLevelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendDataToWirelessDeviceRequestRequestTypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestWirelessDeviceRequestRequestTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    "UpdatePartnerAccountRequestRequestTypeDef",
    "UpdateWirelessDeviceRequestRequestTypeDef",
    "UpdateWirelessGatewayRequestRequestTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
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
    },
    total=False,
)

AbpV1_1TypeDef = TypedDict(
    "AbpV1_1TypeDef",
    {
        "DevAddr": str,
        "SessionKeys": "SessionKeysAbpV1_1TypeDef",
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

CertificateListTypeDef = TypedDict(
    "CertificateListTypeDef",
    {
        "SigningAlg": SigningAlgType,
        "Value": str,
    },
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

DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef = TypedDict(
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
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

GetLogLevelsByResourceTypesResponseTypeDef = TypedDict(
    "GetLogLevelsByResourceTypesResponseTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
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

LoRaWANListDeviceTypeDef = TypedDict(
    "LoRaWANListDeviceTypeDef",
    {
        "DevEui": str,
    },
    total=False,
)

LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef",
    {
        "FPort": int,
    },
    total=False,
)

LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef",
    {
        "AddGwMetadata": bool,
    },
    total=False,
)

LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef",
    {
        "DeviceProfileId": str,
        "ServiceProfileId": str,
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

OtaaV1_0_xTypeDef = TypedDict(
    "OtaaV1_0_xTypeDef",
    {
        "AppKey": str,
        "AppEui": str,
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

SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef",
    {
        "Seq": int,
        "MessageType": MessageTypeType,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
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

UpdateLogLevelsByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
    },
    total=False,
)

UpdatePartnerAccountRequestRequestTypeDef = TypedDict(
    "UpdatePartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": "SidewalkUpdateAccountTypeDef",
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

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
