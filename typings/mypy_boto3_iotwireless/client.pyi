"""
Main interface for iotwireless service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotwireless import IoTWirelessClient

    client: IoTWirelessClient = boto3.client("iotwireless")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotwireless.type_defs import (
    AssociateAwsAccountWithPartnerAccountResponseTypeDef,
    AssociateWirelessGatewayWithCertificateResponseTypeDef,
    CreateDestinationResponseTypeDef,
    CreateDeviceProfileResponseTypeDef,
    CreateServiceProfileResponseTypeDef,
    CreateWirelessDeviceResponseTypeDef,
    CreateWirelessGatewayResponseTypeDef,
    CreateWirelessGatewayTaskDefinitionResponseTypeDef,
    CreateWirelessGatewayTaskResponseTypeDef,
    GetDestinationResponseTypeDef,
    GetDeviceProfileResponseTypeDef,
    GetPartnerAccountResponseTypeDef,
    GetServiceEndpointResponseTypeDef,
    GetServiceProfileResponseTypeDef,
    GetWirelessDeviceResponseTypeDef,
    GetWirelessDeviceStatisticsResponseTypeDef,
    GetWirelessGatewayCertificateResponseTypeDef,
    GetWirelessGatewayFirmwareInformationResponseTypeDef,
    GetWirelessGatewayResponseTypeDef,
    GetWirelessGatewayStatisticsResponseTypeDef,
    GetWirelessGatewayTaskDefinitionResponseTypeDef,
    GetWirelessGatewayTaskResponseTypeDef,
    ListDestinationsResponseTypeDef,
    ListDeviceProfilesResponseTypeDef,
    ListPartnerAccountsResponseTypeDef,
    ListServiceProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWirelessDevicesResponseTypeDef,
    ListWirelessGatewaysResponseTypeDef,
    ListWirelessGatewayTaskDefinitionsResponseTypeDef,
    LoRaWANDeviceProfileTypeDef,
    LoRaWANDeviceTypeDef,
    LoRaWANGatewayTypeDef,
    LoRaWANServiceProfileTypeDef,
    LoRaWANUpdateDeviceTypeDef,
    SendDataToWirelessDeviceResponseTypeDef,
    SidewalkAccountInfoTypeDef,
    SidewalkUpdateAccountTypeDef,
    TagTypeDef,
    TestWirelessDeviceResponseTypeDef,
    UpdateWirelessGatewayTaskCreateTypeDef,
    WirelessMetadataTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTWirelessClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTWirelessClient:
    """
    [IoTWireless.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_aws_account_with_partner_account(
        self, Sidewalk: "SidewalkAccountInfoTypeDef", ClientRequestToken: str = None
    ) -> AssociateAwsAccountWithPartnerAccountResponseTypeDef:
        """
        [Client.associate_aws_account_with_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.associate_aws_account_with_partner_account)
        """

    def associate_wireless_device_with_thing(self, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        [Client.associate_wireless_device_with_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_thing)
        """

    def associate_wireless_gateway_with_certificate(
        self, Id: str, IotCertificateId: str
    ) -> AssociateWirelessGatewayWithCertificateResponseTypeDef:
        """
        [Client.associate_wireless_gateway_with_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_certificate)
        """

    def associate_wireless_gateway_with_thing(self, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        [Client.associate_wireless_gateway_with_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_thing)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.can_paginate)
        """

    def create_destination(
        self,
        Name: str,
        ExpressionType: Literal["RuleName", "MqttTopic"],
        Expression: str,
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
    ) -> CreateDestinationResponseTypeDef:
        """
        [Client.create_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_destination)
        """

    def create_device_profile(
        self,
        Name: str = None,
        LoRaWAN: "LoRaWANDeviceProfileTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
    ) -> CreateDeviceProfileResponseTypeDef:
        """
        [Client.create_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_device_profile)
        """

    def create_service_profile(
        self,
        Name: str = None,
        LoRaWAN: LoRaWANServiceProfileTypeDef = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
    ) -> CreateServiceProfileResponseTypeDef:
        """
        [Client.create_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_service_profile)
        """

    def create_wireless_device(
        self,
        Type: Literal["Sidewalk", "LoRaWAN"],
        DestinationName: str,
        Name: str = None,
        Description: str = None,
        ClientRequestToken: str = None,
        LoRaWAN: "LoRaWANDeviceTypeDef" = None,
    ) -> CreateWirelessDeviceResponseTypeDef:
        """
        [Client.create_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_device)
        """

    def create_wireless_gateway(
        self,
        LoRaWAN: "LoRaWANGatewayTypeDef",
        Name: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
    ) -> CreateWirelessGatewayResponseTypeDef:
        """
        [Client.create_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway)
        """

    def create_wireless_gateway_task(
        self, Id: str, WirelessGatewayTaskDefinitionId: str
    ) -> CreateWirelessGatewayTaskResponseTypeDef:
        """
        [Client.create_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task)
        """

    def create_wireless_gateway_task_definition(
        self,
        AutoCreateTasks: bool,
        Name: str = None,
        Update: "UpdateWirelessGatewayTaskCreateTypeDef" = None,
        ClientRequestToken: str = None,
    ) -> CreateWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        [Client.create_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task_definition)
        """

    def delete_destination(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_destination)
        """

    def delete_device_profile(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_device_profile)
        """

    def delete_service_profile(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_service_profile)
        """

    def delete_wireless_device(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_device)
        """

    def delete_wireless_gateway(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway)
        """

    def delete_wireless_gateway_task(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task)
        """

    def delete_wireless_gateway_task_definition(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task_definition)
        """

    def disassociate_aws_account_from_partner_account(
        self, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_aws_account_from_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.disassociate_aws_account_from_partner_account)
        """

    def disassociate_wireless_device_from_thing(self, Id: str) -> Dict[str, Any]:
        """
        [Client.disassociate_wireless_device_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_thing)
        """

    def disassociate_wireless_gateway_from_certificate(self, Id: str) -> Dict[str, Any]:
        """
        [Client.disassociate_wireless_gateway_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_certificate)
        """

    def disassociate_wireless_gateway_from_thing(self, Id: str) -> Dict[str, Any]:
        """
        [Client.disassociate_wireless_gateway_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_thing)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.generate_presigned_url)
        """

    def get_destination(self, Name: str) -> GetDestinationResponseTypeDef:
        """
        [Client.get_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_destination)
        """

    def get_device_profile(self, Id: str) -> GetDeviceProfileResponseTypeDef:
        """
        [Client.get_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_device_profile)
        """

    def get_partner_account(
        self, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> GetPartnerAccountResponseTypeDef:
        """
        [Client.get_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_partner_account)
        """

    def get_service_endpoint(
        self, ServiceType: Literal["CUPS", "LNS"] = None
    ) -> GetServiceEndpointResponseTypeDef:
        """
        [Client.get_service_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_service_endpoint)
        """

    def get_service_profile(self, Id: str) -> GetServiceProfileResponseTypeDef:
        """
        [Client.get_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_service_profile)
        """

    def get_wireless_device(
        self, Identifier: str, IdentifierType: Literal["WirelessDeviceId", "DevEui", "ThingName"]
    ) -> GetWirelessDeviceResponseTypeDef:
        """
        [Client.get_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device)
        """

    def get_wireless_device_statistics(
        self, WirelessDeviceId: str
    ) -> GetWirelessDeviceStatisticsResponseTypeDef:
        """
        [Client.get_wireless_device_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device_statistics)
        """

    def get_wireless_gateway(
        self,
        Identifier: str,
        IdentifierType: Literal["GatewayEui", "WirelessGatewayId", "ThingName"],
    ) -> GetWirelessGatewayResponseTypeDef:
        """
        [Client.get_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway)
        """

    def get_wireless_gateway_certificate(
        self, Id: str
    ) -> GetWirelessGatewayCertificateResponseTypeDef:
        """
        [Client.get_wireless_gateway_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_certificate)
        """

    def get_wireless_gateway_firmware_information(
        self, Id: str
    ) -> GetWirelessGatewayFirmwareInformationResponseTypeDef:
        """
        [Client.get_wireless_gateway_firmware_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_firmware_information)
        """

    def get_wireless_gateway_statistics(
        self, WirelessGatewayId: str
    ) -> GetWirelessGatewayStatisticsResponseTypeDef:
        """
        [Client.get_wireless_gateway_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_statistics)
        """

    def get_wireless_gateway_task(self, Id: str) -> GetWirelessGatewayTaskResponseTypeDef:
        """
        [Client.get_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task)
        """

    def get_wireless_gateway_task_definition(
        self, Id: str
    ) -> GetWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        [Client.get_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task_definition)
        """

    def list_destinations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListDestinationsResponseTypeDef:
        """
        [Client.list_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_destinations)
        """

    def list_device_profiles(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDeviceProfilesResponseTypeDef:
        """
        [Client.list_device_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_device_profiles)
        """

    def list_partner_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPartnerAccountsResponseTypeDef:
        """
        [Client.list_partner_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_partner_accounts)
        """

    def list_service_profiles(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListServiceProfilesResponseTypeDef:
        """
        [Client.list_service_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_service_profiles)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_tags_for_resource)
        """

    def list_wireless_devices(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        DestinationName: str = None,
        DeviceProfileId: str = None,
        ServiceProfileId: str = None,
        WirelessDeviceType: Literal["Sidewalk", "LoRaWAN"] = None,
    ) -> ListWirelessDevicesResponseTypeDef:
        """
        [Client.list_wireless_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_devices)
        """

    def list_wireless_gateway_task_definitions(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        TaskDefinitionType: Literal["UPDATE"] = None,
    ) -> ListWirelessGatewayTaskDefinitionsResponseTypeDef:
        """
        [Client.list_wireless_gateway_task_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateway_task_definitions)
        """

    def list_wireless_gateways(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWirelessGatewaysResponseTypeDef:
        """
        [Client.list_wireless_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateways)
        """

    def send_data_to_wireless_device(
        self,
        Id: str,
        TransmitMode: int,
        PayloadData: str,
        WirelessMetadata: WirelessMetadataTypeDef = None,
    ) -> SendDataToWirelessDeviceResponseTypeDef:
        """
        [Client.send_data_to_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_wireless_device)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.tag_resource)
        """

    def test_wireless_device(self, Id: str) -> TestWirelessDeviceResponseTypeDef:
        """
        [Client.test_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.test_wireless_device)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.untag_resource)
        """

    def update_destination(
        self,
        Name: str,
        ExpressionType: Literal["RuleName", "MqttTopic"] = None,
        Expression: str = None,
        Description: str = None,
        RoleArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.update_destination)
        """

    def update_partner_account(
        self,
        Sidewalk: SidewalkUpdateAccountTypeDef,
        PartnerAccountId: str,
        PartnerType: Literal["Sidewalk"],
    ) -> Dict[str, Any]:
        """
        [Client.update_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.update_partner_account)
        """

    def update_wireless_device(
        self,
        Id: str,
        DestinationName: str = None,
        Name: str = None,
        Description: str = None,
        LoRaWAN: LoRaWANUpdateDeviceTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_device)
        """

    def update_wireless_gateway(
        self, Id: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_gateway)
        """
