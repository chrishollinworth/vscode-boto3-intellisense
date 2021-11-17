"""
Type annotations for iotwireless service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotwireless import IoTWirelessClient

    client: IoTWirelessClient = boto3.client("iotwireless")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ExpressionTypeType,
    LogLevelType,
    WirelessDeviceIdTypeType,
    WirelessDeviceTypeType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
)
from .type_defs import (
    AssociateAwsAccountWithPartnerAccountResponseTypeDef,
    AssociateWirelessGatewayWithCertificateResponseTypeDef,
    CreateDestinationResponseTypeDef,
    CreateDeviceProfileResponseTypeDef,
    CreateFuotaTaskResponseTypeDef,
    CreateMulticastGroupResponseTypeDef,
    CreateServiceProfileResponseTypeDef,
    CreateWirelessDeviceResponseTypeDef,
    CreateWirelessGatewayResponseTypeDef,
    CreateWirelessGatewayTaskDefinitionResponseTypeDef,
    CreateWirelessGatewayTaskResponseTypeDef,
    DeviceRegistrationStateEventConfigurationTypeDef,
    GetDestinationResponseTypeDef,
    GetDeviceProfileResponseTypeDef,
    GetFuotaTaskResponseTypeDef,
    GetLogLevelsByResourceTypesResponseTypeDef,
    GetMulticastGroupResponseTypeDef,
    GetMulticastGroupSessionResponseTypeDef,
    GetPartnerAccountResponseTypeDef,
    GetResourceEventConfigurationResponseTypeDef,
    GetResourceLogLevelResponseTypeDef,
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
    ListFuotaTasksResponseTypeDef,
    ListMulticastGroupsByFuotaTaskResponseTypeDef,
    ListMulticastGroupsResponseTypeDef,
    ListPartnerAccountsResponseTypeDef,
    ListServiceProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWirelessDevicesResponseTypeDef,
    ListWirelessGatewaysResponseTypeDef,
    ListWirelessGatewayTaskDefinitionsResponseTypeDef,
    LoRaWANDeviceProfileTypeDef,
    LoRaWANDeviceTypeDef,
    LoRaWANFuotaTaskTypeDef,
    LoRaWANGatewayTypeDef,
    LoRaWANMulticastSessionTypeDef,
    LoRaWANMulticastTypeDef,
    LoRaWANServiceProfileTypeDef,
    LoRaWANStartFuotaTaskTypeDef,
    LoRaWANUpdateDeviceTypeDef,
    MulticastWirelessMetadataTypeDef,
    ProximityEventConfigurationTypeDef,
    SendDataToMulticastGroupResponseTypeDef,
    SendDataToWirelessDeviceResponseTypeDef,
    SidewalkAccountInfoTypeDef,
    SidewalkUpdateAccountTypeDef,
    TagTypeDef,
    TestWirelessDeviceResponseTypeDef,
    UpdateWirelessGatewayTaskCreateTypeDef,
    WirelessDeviceLogOptionTypeDef,
    WirelessGatewayLogOptionTypeDef,
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

class IoTWirelessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        IoTWirelessClient exceptions.
        """
    def associate_aws_account_with_partner_account(
        self,
        *,
        Sidewalk: "SidewalkAccountInfoTypeDef",
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> AssociateAwsAccountWithPartnerAccountResponseTypeDef:
        """
        Associates a partner account with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_aws_account_with_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_aws_account_with_partner_account)
        """
    def associate_multicast_group_with_fuota_task(
        self, *, Id: str, MulticastGroupId: str
    ) -> Dict[str, Any]:
        """
        Associate a multicast group with a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_multicast_group_with_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_multicast_group_with_fuota_task)
        """
    def associate_wireless_device_with_fuota_task(
        self, *, Id: str, WirelessDeviceId: str
    ) -> Dict[str, Any]:
        """
        Associate a wireless device with a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_device_with_fuota_task)
        """
    def associate_wireless_device_with_multicast_group(
        self, *, Id: str, WirelessDeviceId: str
    ) -> Dict[str, Any]:
        """
        Associates a wireless device with a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_device_with_multicast_group)
        """
    def associate_wireless_device_with_thing(self, *, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        Associates a wireless device with a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_device_with_thing)
        """
    def associate_wireless_gateway_with_certificate(
        self, *, Id: str, IotCertificateId: str
    ) -> AssociateWirelessGatewayWithCertificateResponseTypeDef:
        """
        Associates a wireless gateway with a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_gateway_with_certificate)
        """
    def associate_wireless_gateway_with_thing(self, *, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        Associates a wireless gateway with a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_gateway_with_thing)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#can_paginate)
        """
    def cancel_multicast_group_session(self, *, Id: str) -> Dict[str, Any]:
        """
        Cancels an existing multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.cancel_multicast_group_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#cancel_multicast_group_session)
        """
    def create_destination(
        self,
        *,
        Name: str,
        ExpressionType: ExpressionTypeType,
        Expression: str,
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateDestinationResponseTypeDef:
        """
        Creates a new destination that maps a device message to an AWS IoT rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_destination)
        """
    def create_device_profile(
        self,
        *,
        Name: str = None,
        LoRaWAN: "LoRaWANDeviceProfileTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateDeviceProfileResponseTypeDef:
        """
        Creates a new device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_device_profile)
        """
    def create_fuota_task(
        self,
        *,
        FirmwareUpdateImage: str,
        FirmwareUpdateRole: str,
        Name: str = None,
        Description: str = None,
        ClientRequestToken: str = None,
        LoRaWAN: "LoRaWANFuotaTaskTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFuotaTaskResponseTypeDef:
        """
        Creates a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_fuota_task)
        """
    def create_multicast_group(
        self,
        *,
        LoRaWAN: "LoRaWANMulticastTypeDef",
        Name: str = None,
        Description: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMulticastGroupResponseTypeDef:
        """
        Creates a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_multicast_group)
        """
    def create_service_profile(
        self,
        *,
        Name: str = None,
        LoRaWAN: "LoRaWANServiceProfileTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateServiceProfileResponseTypeDef:
        """
        Creates a new service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_service_profile)
        """
    def create_wireless_device(
        self,
        *,
        Type: WirelessDeviceTypeType,
        DestinationName: str,
        Name: str = None,
        Description: str = None,
        ClientRequestToken: str = None,
        LoRaWAN: "LoRaWANDeviceTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWirelessDeviceResponseTypeDef:
        """
        Provisions a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_device)
        """
    def create_wireless_gateway(
        self,
        *,
        LoRaWAN: "LoRaWANGatewayTypeDef",
        Name: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateWirelessGatewayResponseTypeDef:
        """
        Provisions a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway)
        """
    def create_wireless_gateway_task(
        self, *, Id: str, WirelessGatewayTaskDefinitionId: str
    ) -> CreateWirelessGatewayTaskResponseTypeDef:
        """
        Creates a task for a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway_task)
        """
    def create_wireless_gateway_task_definition(
        self,
        *,
        AutoCreateTasks: bool,
        Name: str = None,
        Update: "UpdateWirelessGatewayTaskCreateTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        Creates a gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway_task_definition)
        """
    def delete_destination(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_destination)
        """
    def delete_device_profile(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_device_profile)
        """
    def delete_fuota_task(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_fuota_task)
        """
    def delete_multicast_group(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a multicast group if it is not in use by a fuota task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_multicast_group)
        """
    def delete_service_profile(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_service_profile)
        """
    def delete_wireless_device(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_device)
        """
    def delete_wireless_gateway(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway)
        """
    def delete_wireless_gateway_task(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a wireless gateway task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway_task)
        """
    def delete_wireless_gateway_task_definition(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a wireless gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway_task_definition)
        """
    def disassociate_aws_account_from_partner_account(
        self, *, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> Dict[str, Any]:
        """
        Disassociates your AWS account from a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_aws_account_from_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_aws_account_from_partner_account)
        """
    def disassociate_multicast_group_from_fuota_task(
        self, *, Id: str, MulticastGroupId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a multicast group from a fuota task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_multicast_group_from_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_multicast_group_from_fuota_task)
        """
    def disassociate_wireless_device_from_fuota_task(
        self, *, Id: str, WirelessDeviceId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless device from a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_device_from_fuota_task)
        """
    def disassociate_wireless_device_from_multicast_group(
        self, *, Id: str, WirelessDeviceId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless device from a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_device_from_multicast_group)
        """
    def disassociate_wireless_device_from_thing(self, *, Id: str) -> Dict[str, Any]:
        """
        Disassociates a wireless device from its currently associated thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_device_from_thing)
        """
    def disassociate_wireless_gateway_from_certificate(self, *, Id: str) -> Dict[str, Any]:
        """
        Disassociates a wireless gateway from its currently associated certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_gateway_from_certificate)
        """
    def disassociate_wireless_gateway_from_thing(self, *, Id: str) -> Dict[str, Any]:
        """
        Disassociates a wireless gateway from its currently associated thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_gateway_from_thing)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#generate_presigned_url)
        """
    def get_destination(self, *, Name: str) -> GetDestinationResponseTypeDef:
        """
        Gets information about a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_destination)
        """
    def get_device_profile(self, *, Id: str) -> GetDeviceProfileResponseTypeDef:
        """
        Gets information about a device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_device_profile)
        """
    def get_fuota_task(self, *, Id: str) -> GetFuotaTaskResponseTypeDef:
        """
        Gets information about a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_fuota_task)
        """
    def get_log_levels_by_resource_types(self) -> GetLogLevelsByResourceTypesResponseTypeDef:
        """
        Returns current default log levels or log levels by resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_log_levels_by_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_log_levels_by_resource_types)
        """
    def get_multicast_group(self, *, Id: str) -> GetMulticastGroupResponseTypeDef:
        """
        Gets information about a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_multicast_group)
        """
    def get_multicast_group_session(self, *, Id: str) -> GetMulticastGroupSessionResponseTypeDef:
        """
        Gets information about a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_multicast_group_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_multicast_group_session)
        """
    def get_partner_account(
        self, *, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> GetPartnerAccountResponseTypeDef:
        """
        Gets information about a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_partner_account)
        """
    def get_resource_event_configuration(
        self,
        *,
        Identifier: str,
        IdentifierType: Literal["PartnerAccountId"],
        PartnerType: Literal["Sidewalk"] = None
    ) -> GetResourceEventConfigurationResponseTypeDef:
        """
        Get the event configuration for a particular resource identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_resource_event_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_resource_event_configuration)
        """
    def get_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str
    ) -> GetResourceLogLevelResponseTypeDef:
        """
        Fetches the log-level override, if any, for a given resource-ID and resource-
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_resource_log_level)
        """
    def get_service_endpoint(
        self, *, ServiceType: WirelessGatewayServiceTypeType = None
    ) -> GetServiceEndpointResponseTypeDef:
        """
        Gets the account-specific endpoint for Configuration and Update Server (CUPS)
        protocol or LoRaWAN Network Server (LNS) connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_service_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_service_endpoint)
        """
    def get_service_profile(self, *, Id: str) -> GetServiceProfileResponseTypeDef:
        """
        Gets information about a service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_service_profile)
        """
    def get_wireless_device(
        self, *, Identifier: str, IdentifierType: WirelessDeviceIdTypeType
    ) -> GetWirelessDeviceResponseTypeDef:
        """
        Gets information about a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_device)
        """
    def get_wireless_device_statistics(
        self, *, WirelessDeviceId: str
    ) -> GetWirelessDeviceStatisticsResponseTypeDef:
        """
        Gets operating information about a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_device_statistics)
        """
    def get_wireless_gateway(
        self, *, Identifier: str, IdentifierType: WirelessGatewayIdTypeType
    ) -> GetWirelessGatewayResponseTypeDef:
        """
        Gets information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway)
        """
    def get_wireless_gateway_certificate(
        self, *, Id: str
    ) -> GetWirelessGatewayCertificateResponseTypeDef:
        """
        Gets the ID of the certificate that is currently associated with a wireless
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_certificate)
        """
    def get_wireless_gateway_firmware_information(
        self, *, Id: str
    ) -> GetWirelessGatewayFirmwareInformationResponseTypeDef:
        """
        Gets the firmware version and other information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_firmware_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_firmware_information)
        """
    def get_wireless_gateway_statistics(
        self, *, WirelessGatewayId: str
    ) -> GetWirelessGatewayStatisticsResponseTypeDef:
        """
        Gets operating information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_statistics)
        """
    def get_wireless_gateway_task(self, *, Id: str) -> GetWirelessGatewayTaskResponseTypeDef:
        """
        Gets information about a wireless gateway task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_task)
        """
    def get_wireless_gateway_task_definition(
        self, *, Id: str
    ) -> GetWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        Gets information about a wireless gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_task_definition)
        """
    def list_destinations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDestinationsResponseTypeDef:
        """
        Lists the destinations registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_destinations)
        """
    def list_device_profiles(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDeviceProfilesResponseTypeDef:
        """
        Lists the device profiles registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_device_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_device_profiles)
        """
    def list_fuota_tasks(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListFuotaTasksResponseTypeDef:
        """
        Lists the FUOTA tasks registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_fuota_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_fuota_tasks)
        """
    def list_multicast_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListMulticastGroupsResponseTypeDef:
        """
        Lists the multicast groups registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_multicast_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_multicast_groups)
        """
    def list_multicast_groups_by_fuota_task(
        self, *, Id: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMulticastGroupsByFuotaTaskResponseTypeDef:
        """
        List all multicast groups associated with a fuota task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_multicast_groups_by_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_multicast_groups_by_fuota_task)
        """
    def list_partner_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPartnerAccountsResponseTypeDef:
        """
        Lists the partner accounts associated with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_partner_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_partner_accounts)
        """
    def list_service_profiles(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListServiceProfilesResponseTypeDef:
        """
        Lists the service profiles registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_service_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_service_profiles)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_tags_for_resource)
        """
    def list_wireless_devices(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        DestinationName: str = None,
        DeviceProfileId: str = None,
        ServiceProfileId: str = None,
        WirelessDeviceType: WirelessDeviceTypeType = None,
        FuotaTaskId: str = None,
        MulticastGroupId: str = None
    ) -> ListWirelessDevicesResponseTypeDef:
        """
        Lists the wireless devices registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_devices)
        """
    def list_wireless_gateway_task_definitions(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        TaskDefinitionType: Literal["UPDATE"] = None
    ) -> ListWirelessGatewayTaskDefinitionsResponseTypeDef:
        """
        List the wireless gateway tasks definitions registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateway_task_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_gateway_task_definitions)
        """
    def list_wireless_gateways(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListWirelessGatewaysResponseTypeDef:
        """
        Lists the wireless gateways registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_gateways)
        """
    def put_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str, LogLevel: LogLevelType
    ) -> Dict[str, Any]:
        """
        Sets the log-level override for a resource-ID and resource-type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.put_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#put_resource_log_level)
        """
    def reset_all_resource_log_levels(self) -> Dict[str, Any]:
        """
        Removes the log-level overrides for all resources; both wireless devices and
        wireless gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.reset_all_resource_log_levels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#reset_all_resource_log_levels)
        """
    def reset_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str
    ) -> Dict[str, Any]:
        """
        Removes the log-level override, if any, for a specific resource-ID and resource-
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.reset_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#reset_resource_log_level)
        """
    def send_data_to_multicast_group(
        self, *, Id: str, PayloadData: str, WirelessMetadata: "MulticastWirelessMetadataTypeDef"
    ) -> SendDataToMulticastGroupResponseTypeDef:
        """
        Sends the specified data to a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#send_data_to_multicast_group)
        """
    def send_data_to_wireless_device(
        self,
        *,
        Id: str,
        TransmitMode: int,
        PayloadData: str,
        WirelessMetadata: "WirelessMetadataTypeDef" = None
    ) -> SendDataToWirelessDeviceResponseTypeDef:
        """
        Sends a decrypted application data frame to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#send_data_to_wireless_device)
        """
    def start_bulk_associate_wireless_device_with_multicast_group(
        self, *, Id: str, QueryString: str = None, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Starts a bulk association of all qualifying wireless devices with a multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.start_bulk_associate_wireless_device_with_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#start_bulk_associate_wireless_device_with_multicast_group)
        """
    def start_bulk_disassociate_wireless_device_from_multicast_group(
        self, *, Id: str, QueryString: str = None, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Starts a bulk disassociatin of all qualifying wireless devices from a multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.start_bulk_disassociate_wireless_device_from_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#start_bulk_disassociate_wireless_device_from_multicast_group)
        """
    def start_fuota_task(
        self, *, Id: str, LoRaWAN: "LoRaWANStartFuotaTaskTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Starts a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.start_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#start_fuota_task)
        """
    def start_multicast_group_session(
        self, *, Id: str, LoRaWAN: "LoRaWANMulticastSessionTypeDef"
    ) -> Dict[str, Any]:
        """
        Starts a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.start_multicast_group_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#start_multicast_group_session)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#tag_resource)
        """
    def test_wireless_device(self, *, Id: str) -> TestWirelessDeviceResponseTypeDef:
        """
        Simulates a provisioned device by sending an uplink data payload of `Hello` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.test_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#test_wireless_device)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#untag_resource)
        """
    def update_destination(
        self,
        *,
        Name: str,
        ExpressionType: ExpressionTypeType = None,
        Expression: str = None,
        Description: str = None,
        RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates properties of a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_destination)
        """
    def update_fuota_task(
        self,
        *,
        Id: str,
        Name: str = None,
        Description: str = None,
        LoRaWAN: "LoRaWANFuotaTaskTypeDef" = None,
        FirmwareUpdateImage: str = None,
        FirmwareUpdateRole: str = None
    ) -> Dict[str, Any]:
        """
        Updates properties of a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_fuota_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_fuota_task)
        """
    def update_log_levels_by_resource_types(
        self,
        *,
        DefaultLogLevel: LogLevelType = None,
        WirelessDeviceLogOptions: List["WirelessDeviceLogOptionTypeDef"] = None,
        WirelessGatewayLogOptions: List["WirelessGatewayLogOptionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Set default log level, or log levels by resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_log_levels_by_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_log_levels_by_resource_types)
        """
    def update_multicast_group(
        self,
        *,
        Id: str,
        Name: str = None,
        Description: str = None,
        LoRaWAN: "LoRaWANMulticastTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates properties of a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_multicast_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_multicast_group)
        """
    def update_partner_account(
        self,
        *,
        Sidewalk: "SidewalkUpdateAccountTypeDef",
        PartnerAccountId: str,
        PartnerType: Literal["Sidewalk"]
    ) -> Dict[str, Any]:
        """
        Updates properties of a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_partner_account)
        """
    def update_resource_event_configuration(
        self,
        *,
        Identifier: str,
        IdentifierType: Literal["PartnerAccountId"],
        PartnerType: Literal["Sidewalk"] = None,
        DeviceRegistrationState: "DeviceRegistrationStateEventConfigurationTypeDef" = None,
        Proximity: "ProximityEventConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Update the event configuration for a particular resource identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_resource_event_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_resource_event_configuration)
        """
    def update_wireless_device(
        self,
        *,
        Id: str,
        DestinationName: str = None,
        Name: str = None,
        Description: str = None,
        LoRaWAN: "LoRaWANUpdateDeviceTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates properties of a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_wireless_device)
        """
    def update_wireless_gateway(
        self,
        *,
        Id: str,
        Name: str = None,
        Description: str = None,
        JoinEuiFilters: List[List[str]] = None,
        NetIdFilters: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates properties of a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_wireless_gateway)
        """
