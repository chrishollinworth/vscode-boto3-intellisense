"""
Main interface for iotwireless service type definitions.

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef

    data: AbpV1_0_xTypeDef = {...}
    ```
"""
import sys
from typing import List

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
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
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
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "TagTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileResponseTypeDef",
    "CreateServiceProfileResponseTypeDef",
    "CreateWirelessDeviceResponseTypeDef",
    "CreateWirelessGatewayResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    "CreateWirelessGatewayTaskResponseTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "GetServiceEndpointResponseTypeDef",
    "GetServiceProfileResponseTypeDef",
    "GetWirelessDeviceResponseTypeDef",
    "GetWirelessDeviceStatisticsResponseTypeDef",
    "GetWirelessGatewayCertificateResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    "GetWirelessGatewayResponseTypeDef",
    "GetWirelessGatewayStatisticsResponseTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    "GetWirelessGatewayTaskResponseTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "ListPartnerAccountsResponseTypeDef",
    "ListServiceProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWirelessDevicesResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    "ListWirelessGatewaysResponseTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "WirelessMetadataTypeDef",
)

AbpV1_0_xTypeDef = TypedDict(
    "AbpV1_0_xTypeDef", {"DevAddr": str, "SessionKeys": "SessionKeysAbpV1_0_xTypeDef"}, total=False
)

AbpV1_1TypeDef = TypedDict(
    "AbpV1_1TypeDef", {"DevAddr": str, "SessionKeys": "SessionKeysAbpV1_1TypeDef"}, total=False
)

DestinationsTypeDef = TypedDict(
    "DestinationsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ExpressionType": Literal["RuleName", "MqttTopic"],
        "Expression": str,
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)

DeviceProfileTypeDef = TypedDict(
    "DeviceProfileTypeDef", {"Arn": str, "Name": str, "Id": str}, total=False
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
    {"CurrentVersion": "LoRaWANGatewayVersionTypeDef"},
    total=False,
)

LoRaWANGatewayMetadataTypeDef = TypedDict(
    "LoRaWANGatewayMetadataTypeDef", {"GatewayEui": str, "Snr": float, "Rssi": float}, total=False
)

LoRaWANGatewayTypeDef = TypedDict(
    "LoRaWANGatewayTypeDef", {"GatewayEui": str, "RfRegion": str}, total=False
)

LoRaWANGatewayVersionTypeDef = TypedDict(
    "LoRaWANGatewayVersionTypeDef",
    {"PackageVersion": str, "Model": str, "Station": str},
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

LoRaWANListDeviceTypeDef = TypedDict("LoRaWANListDeviceTypeDef", {"DevEui": str}, total=False)

LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef", {"FPort": int}, total=False
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

OtaaV1_0_xTypeDef = TypedDict("OtaaV1_0_xTypeDef", {"AppKey": str, "AppEui": str}, total=False)

OtaaV1_1TypeDef = TypedDict(
    "OtaaV1_1TypeDef", {"AppKey": str, "NwkKey": str, "JoinEui": str}, total=False
)

ServiceProfileTypeDef = TypedDict(
    "ServiceProfileTypeDef", {"Arn": str, "Name": str, "Id": str}, total=False
)

SessionKeysAbpV1_0_xTypeDef = TypedDict(
    "SessionKeysAbpV1_0_xTypeDef", {"NwkSKey": str, "AppSKey": str}, total=False
)

SessionKeysAbpV1_1TypeDef = TypedDict(
    "SessionKeysAbpV1_1TypeDef",
    {"FNwkSIntKey": str, "SNwkSIntKey": str, "NwkSEncKey": str, "AppSKey": str},
    total=False,
)

SidewalkAccountInfoTypeDef = TypedDict(
    "SidewalkAccountInfoTypeDef", {"AmazonId": str, "AppServerPrivateKey": str}, total=False
)

SidewalkAccountInfoWithFingerprintTypeDef = TypedDict(
    "SidewalkAccountInfoWithFingerprintTypeDef", {"AmazonId": str, "Fingerprint": str}, total=False
)

SidewalkListDeviceTypeDef = TypedDict("SidewalkListDeviceTypeDef", {"AmazonId": str}, total=False)

SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef", {"Seq": int}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

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
    {"Id": str, "LoRaWAN": "LoRaWANUpdateGatewayTaskEntryTypeDef"},
    total=False,
)

WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Type": Literal["Sidewalk", "LoRaWAN"],
        "Name": str,
        "DestinationName": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANListDeviceTypeDef",
        "Sidewalk": "SidewalkListDeviceTypeDef",
    },
    total=False,
)

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

AssociateAwsAccountWithPartnerAccountResponseTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    {"Sidewalk": "SidewalkAccountInfoTypeDef"},
    total=False,
)

AssociateWirelessGatewayWithCertificateResponseTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateResponseTypeDef", {"IotCertificateId": str}, total=False
)

CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef", {"Arn": str, "Name": str}, total=False
)

CreateDeviceProfileResponseTypeDef = TypedDict(
    "CreateDeviceProfileResponseTypeDef", {"Arn": str, "Id": str}, total=False
)

CreateServiceProfileResponseTypeDef = TypedDict(
    "CreateServiceProfileResponseTypeDef", {"Arn": str, "Id": str}, total=False
)

CreateWirelessDeviceResponseTypeDef = TypedDict(
    "CreateWirelessDeviceResponseTypeDef", {"Arn": str, "Id": str}, total=False
)

CreateWirelessGatewayResponseTypeDef = TypedDict(
    "CreateWirelessGatewayResponseTypeDef", {"Arn": str, "Id": str}, total=False
)

CreateWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef", {"Id": str}, total=False
)

CreateWirelessGatewayTaskResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayTaskDefinitionId": str,
        "Status": Literal[
            "PENDING", "IN_PROGRESS", "FIRST_RETRY", "SECOND_RETRY", "COMPLETED", "FAILED"
        ],
    },
    total=False,
)

GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Expression": str,
        "ExpressionType": Literal["RuleName", "MqttTopic"],
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)

GetDeviceProfileResponseTypeDef = TypedDict(
    "GetDeviceProfileResponseTypeDef",
    {"Arn": str, "Name": str, "Id": str, "LoRaWAN": "LoRaWANDeviceProfileTypeDef"},
    total=False,
)

GetPartnerAccountResponseTypeDef = TypedDict(
    "GetPartnerAccountResponseTypeDef",
    {"Sidewalk": "SidewalkAccountInfoWithFingerprintTypeDef", "AccountLinked": bool},
    total=False,
)

GetServiceEndpointResponseTypeDef = TypedDict(
    "GetServiceEndpointResponseTypeDef",
    {"ServiceType": Literal["CUPS", "LNS"], "ServiceEndpoint": str, "ServerTrust": str},
    total=False,
)

GetServiceProfileResponseTypeDef = TypedDict(
    "GetServiceProfileResponseTypeDef",
    {"Arn": str, "Name": str, "Id": str, "LoRaWAN": "LoRaWANGetServiceProfileInfoTypeDef"},
    total=False,
)

GetWirelessDeviceResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseTypeDef",
    {
        "Type": Literal["Sidewalk", "LoRaWAN"],
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
    },
    total=False,
)

GetWirelessDeviceStatisticsResponseTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsResponseTypeDef",
    {
        "WirelessDeviceId": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANDeviceMetadataTypeDef",
    },
    total=False,
)

GetWirelessGatewayCertificateResponseTypeDef = TypedDict(
    "GetWirelessGatewayCertificateResponseTypeDef",
    {"IotCertificateId": str, "LoRaWANNetworkServerCertificateId": str},
    total=False,
)

GetWirelessGatewayFirmwareInformationResponseTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    {"LoRaWAN": "LoRaWANGatewayCurrentVersionTypeDef"},
    total=False,
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
    },
    total=False,
)

GetWirelessGatewayStatisticsResponseTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsResponseTypeDef",
    {"WirelessGatewayId": str, "LastUplinkReceivedAt": str},
    total=False,
)

GetWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    {"AutoCreateTasks": bool, "Name": str, "Update": "UpdateWirelessGatewayTaskCreateTypeDef"},
    total=False,
)

GetWirelessGatewayTaskResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "WirelessGatewayTaskDefinitionId": str,
        "LastUplinkReceivedAt": str,
        "TaskCreatedAt": str,
        "Status": Literal[
            "PENDING", "IN_PROGRESS", "FIRST_RETRY", "SECOND_RETRY", "COMPLETED", "FAILED"
        ],
    },
    total=False,
)

ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {"NextToken": str, "DestinationList": List["DestinationsTypeDef"]},
    total=False,
)

ListDeviceProfilesResponseTypeDef = TypedDict(
    "ListDeviceProfilesResponseTypeDef",
    {"NextToken": str, "DeviceProfileList": List["DeviceProfileTypeDef"]},
    total=False,
)

ListPartnerAccountsResponseTypeDef = TypedDict(
    "ListPartnerAccountsResponseTypeDef",
    {"NextToken": str, "Sidewalk": List["SidewalkAccountInfoWithFingerprintTypeDef"]},
    total=False,
)

ListServiceProfilesResponseTypeDef = TypedDict(
    "ListServiceProfilesResponseTypeDef",
    {"NextToken": str, "ServiceProfileList": List["ServiceProfileTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListWirelessDevicesResponseTypeDef = TypedDict(
    "ListWirelessDevicesResponseTypeDef",
    {"NextToken": str, "WirelessDeviceList": List["WirelessDeviceStatisticsTypeDef"]},
    total=False,
)

ListWirelessGatewayTaskDefinitionsResponseTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    {"NextToken": str, "TaskDefinitions": List["UpdateWirelessGatewayTaskEntryTypeDef"]},
    total=False,
)

ListWirelessGatewaysResponseTypeDef = TypedDict(
    "ListWirelessGatewaysResponseTypeDef",
    {"NextToken": str, "WirelessGatewayList": List["WirelessGatewayStatisticsTypeDef"]},
    total=False,
)

LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef", {"AddGwMetadata": bool}, total=False
)

LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef", {"DeviceProfileId": str, "ServiceProfileId": str}, total=False
)

SendDataToWirelessDeviceResponseTypeDef = TypedDict(
    "SendDataToWirelessDeviceResponseTypeDef", {"MessageId": str}, total=False
)

SidewalkUpdateAccountTypeDef = TypedDict(
    "SidewalkUpdateAccountTypeDef", {"AppServerPrivateKey": str}, total=False
)

TestWirelessDeviceResponseTypeDef = TypedDict(
    "TestWirelessDeviceResponseTypeDef", {"Result": str}, total=False
)

WirelessMetadataTypeDef = TypedDict(
    "WirelessMetadataTypeDef",
    {"LoRaWAN": "LoRaWANSendDataToDeviceTypeDef", "Sidewalk": "SidewalkSendDataToDeviceTypeDef"},
    total=False,
)
