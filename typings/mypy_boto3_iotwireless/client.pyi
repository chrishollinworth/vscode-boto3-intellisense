"""
Type annotations for iotwireless service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotwireless.client import IoTWirelessClient

    session = Session()
    client: IoTWirelessClient = session.client("iotwireless")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssociateAwsAccountWithPartnerAccountRequestTypeDef,
    AssociateAwsAccountWithPartnerAccountResponseTypeDef,
    AssociateMulticastGroupWithFuotaTaskRequestTypeDef,
    AssociateWirelessDeviceWithFuotaTaskRequestTypeDef,
    AssociateWirelessDeviceWithMulticastGroupRequestTypeDef,
    AssociateWirelessDeviceWithThingRequestTypeDef,
    AssociateWirelessGatewayWithCertificateRequestTypeDef,
    AssociateWirelessGatewayWithCertificateResponseTypeDef,
    AssociateWirelessGatewayWithThingRequestTypeDef,
    CancelMulticastGroupSessionRequestTypeDef,
    CreateDestinationRequestTypeDef,
    CreateDestinationResponseTypeDef,
    CreateDeviceProfileRequestTypeDef,
    CreateDeviceProfileResponseTypeDef,
    CreateFuotaTaskRequestTypeDef,
    CreateFuotaTaskResponseTypeDef,
    CreateMulticastGroupRequestTypeDef,
    CreateMulticastGroupResponseTypeDef,
    CreateNetworkAnalyzerConfigurationRequestTypeDef,
    CreateNetworkAnalyzerConfigurationResponseTypeDef,
    CreateServiceProfileRequestTypeDef,
    CreateServiceProfileResponseTypeDef,
    CreateWirelessDeviceRequestTypeDef,
    CreateWirelessDeviceResponseTypeDef,
    CreateWirelessGatewayRequestTypeDef,
    CreateWirelessGatewayResponseTypeDef,
    CreateWirelessGatewayTaskDefinitionRequestTypeDef,
    CreateWirelessGatewayTaskDefinitionResponseTypeDef,
    CreateWirelessGatewayTaskRequestTypeDef,
    CreateWirelessGatewayTaskResponseTypeDef,
    DeleteDestinationRequestTypeDef,
    DeleteDeviceProfileRequestTypeDef,
    DeleteFuotaTaskRequestTypeDef,
    DeleteMulticastGroupRequestTypeDef,
    DeleteNetworkAnalyzerConfigurationRequestTypeDef,
    DeleteQueuedMessagesRequestTypeDef,
    DeleteServiceProfileRequestTypeDef,
    DeleteWirelessDeviceImportTaskRequestTypeDef,
    DeleteWirelessDeviceRequestTypeDef,
    DeleteWirelessGatewayRequestTypeDef,
    DeleteWirelessGatewayTaskDefinitionRequestTypeDef,
    DeleteWirelessGatewayTaskRequestTypeDef,
    DeregisterWirelessDeviceRequestTypeDef,
    DisassociateAwsAccountFromPartnerAccountRequestTypeDef,
    DisassociateMulticastGroupFromFuotaTaskRequestTypeDef,
    DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef,
    DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef,
    DisassociateWirelessDeviceFromThingRequestTypeDef,
    DisassociateWirelessGatewayFromCertificateRequestTypeDef,
    DisassociateWirelessGatewayFromThingRequestTypeDef,
    GetDestinationRequestTypeDef,
    GetDestinationResponseTypeDef,
    GetDeviceProfileRequestTypeDef,
    GetDeviceProfileResponseTypeDef,
    GetEventConfigurationByResourceTypesResponseTypeDef,
    GetFuotaTaskRequestTypeDef,
    GetFuotaTaskResponseTypeDef,
    GetLogLevelsByResourceTypesResponseTypeDef,
    GetMetricConfigurationResponseTypeDef,
    GetMetricsRequestTypeDef,
    GetMetricsResponseTypeDef,
    GetMulticastGroupRequestTypeDef,
    GetMulticastGroupResponseTypeDef,
    GetMulticastGroupSessionRequestTypeDef,
    GetMulticastGroupSessionResponseTypeDef,
    GetNetworkAnalyzerConfigurationRequestTypeDef,
    GetNetworkAnalyzerConfigurationResponseTypeDef,
    GetPartnerAccountRequestTypeDef,
    GetPartnerAccountResponseTypeDef,
    GetPositionConfigurationRequestTypeDef,
    GetPositionConfigurationResponseTypeDef,
    GetPositionEstimateRequestTypeDef,
    GetPositionEstimateResponseTypeDef,
    GetPositionRequestTypeDef,
    GetPositionResponseTypeDef,
    GetResourceEventConfigurationRequestTypeDef,
    GetResourceEventConfigurationResponseTypeDef,
    GetResourceLogLevelRequestTypeDef,
    GetResourceLogLevelResponseTypeDef,
    GetResourcePositionRequestTypeDef,
    GetResourcePositionResponseTypeDef,
    GetServiceEndpointRequestTypeDef,
    GetServiceEndpointResponseTypeDef,
    GetServiceProfileRequestTypeDef,
    GetServiceProfileResponseTypeDef,
    GetWirelessDeviceImportTaskRequestTypeDef,
    GetWirelessDeviceImportTaskResponseTypeDef,
    GetWirelessDeviceRequestTypeDef,
    GetWirelessDeviceResponseTypeDef,
    GetWirelessDeviceStatisticsRequestTypeDef,
    GetWirelessDeviceStatisticsResponseTypeDef,
    GetWirelessGatewayCertificateRequestTypeDef,
    GetWirelessGatewayCertificateResponseTypeDef,
    GetWirelessGatewayFirmwareInformationRequestTypeDef,
    GetWirelessGatewayFirmwareInformationResponseTypeDef,
    GetWirelessGatewayRequestTypeDef,
    GetWirelessGatewayResponseTypeDef,
    GetWirelessGatewayStatisticsRequestTypeDef,
    GetWirelessGatewayStatisticsResponseTypeDef,
    GetWirelessGatewayTaskDefinitionRequestTypeDef,
    GetWirelessGatewayTaskDefinitionResponseTypeDef,
    GetWirelessGatewayTaskRequestTypeDef,
    GetWirelessGatewayTaskResponseTypeDef,
    ListDestinationsRequestTypeDef,
    ListDestinationsResponseTypeDef,
    ListDeviceProfilesRequestTypeDef,
    ListDeviceProfilesResponseTypeDef,
    ListDevicesForWirelessDeviceImportTaskRequestTypeDef,
    ListDevicesForWirelessDeviceImportTaskResponseTypeDef,
    ListEventConfigurationsRequestTypeDef,
    ListEventConfigurationsResponseTypeDef,
    ListFuotaTasksRequestTypeDef,
    ListFuotaTasksResponseTypeDef,
    ListMulticastGroupsByFuotaTaskRequestTypeDef,
    ListMulticastGroupsByFuotaTaskResponseTypeDef,
    ListMulticastGroupsRequestTypeDef,
    ListMulticastGroupsResponseTypeDef,
    ListNetworkAnalyzerConfigurationsRequestTypeDef,
    ListNetworkAnalyzerConfigurationsResponseTypeDef,
    ListPartnerAccountsRequestTypeDef,
    ListPartnerAccountsResponseTypeDef,
    ListPositionConfigurationsRequestTypeDef,
    ListPositionConfigurationsResponseTypeDef,
    ListQueuedMessagesRequestTypeDef,
    ListQueuedMessagesResponseTypeDef,
    ListServiceProfilesRequestTypeDef,
    ListServiceProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWirelessDeviceImportTasksRequestTypeDef,
    ListWirelessDeviceImportTasksResponseTypeDef,
    ListWirelessDevicesRequestTypeDef,
    ListWirelessDevicesResponseTypeDef,
    ListWirelessGatewaysRequestTypeDef,
    ListWirelessGatewaysResponseTypeDef,
    ListWirelessGatewayTaskDefinitionsRequestTypeDef,
    ListWirelessGatewayTaskDefinitionsResponseTypeDef,
    PutPositionConfigurationRequestTypeDef,
    PutResourceLogLevelRequestTypeDef,
    ResetResourceLogLevelRequestTypeDef,
    SendDataToMulticastGroupRequestTypeDef,
    SendDataToMulticastGroupResponseTypeDef,
    SendDataToWirelessDeviceRequestTypeDef,
    SendDataToWirelessDeviceResponseTypeDef,
    StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef,
    StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef,
    StartFuotaTaskRequestTypeDef,
    StartMulticastGroupSessionRequestTypeDef,
    StartSingleWirelessDeviceImportTaskRequestTypeDef,
    StartSingleWirelessDeviceImportTaskResponseTypeDef,
    StartWirelessDeviceImportTaskRequestTypeDef,
    StartWirelessDeviceImportTaskResponseTypeDef,
    TagResourceRequestTypeDef,
    TestWirelessDeviceRequestTypeDef,
    TestWirelessDeviceResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDestinationRequestTypeDef,
    UpdateEventConfigurationByResourceTypesRequestTypeDef,
    UpdateFuotaTaskRequestTypeDef,
    UpdateLogLevelsByResourceTypesRequestTypeDef,
    UpdateMetricConfigurationRequestTypeDef,
    UpdateMulticastGroupRequestTypeDef,
    UpdateNetworkAnalyzerConfigurationRequestTypeDef,
    UpdatePartnerAccountRequestTypeDef,
    UpdatePositionRequestTypeDef,
    UpdateResourceEventConfigurationRequestTypeDef,
    UpdateResourcePositionRequestTypeDef,
    UpdateWirelessDeviceImportTaskRequestTypeDef,
    UpdateWirelessDeviceRequestTypeDef,
    UpdateWirelessGatewayRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("IoTWirelessClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTWirelessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#generate_presigned_url)
        """

    def associate_aws_account_with_partner_account(
        self, **kwargs: Unpack[AssociateAwsAccountWithPartnerAccountRequestTypeDef]
    ) -> AssociateAwsAccountWithPartnerAccountResponseTypeDef:
        """
        Associates a partner account with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_aws_account_with_partner_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_aws_account_with_partner_account)
        """

    def associate_multicast_group_with_fuota_task(
        self, **kwargs: Unpack[AssociateMulticastGroupWithFuotaTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associate a multicast group with a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_multicast_group_with_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_multicast_group_with_fuota_task)
        """

    def associate_wireless_device_with_fuota_task(
        self, **kwargs: Unpack[AssociateWirelessDeviceWithFuotaTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associate a wireless device with a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_wireless_device_with_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_wireless_device_with_fuota_task)
        """

    def associate_wireless_device_with_multicast_group(
        self, **kwargs: Unpack[AssociateWirelessDeviceWithMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a wireless device with a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_wireless_device_with_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_wireless_device_with_multicast_group)
        """

    def associate_wireless_device_with_thing(
        self, **kwargs: Unpack[AssociateWirelessDeviceWithThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a wireless device with a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_wireless_device_with_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_wireless_device_with_thing)
        """

    def associate_wireless_gateway_with_certificate(
        self, **kwargs: Unpack[AssociateWirelessGatewayWithCertificateRequestTypeDef]
    ) -> AssociateWirelessGatewayWithCertificateResponseTypeDef:
        """
        Associates a wireless gateway with a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_wireless_gateway_with_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_wireless_gateway_with_certificate)
        """

    def associate_wireless_gateway_with_thing(
        self, **kwargs: Unpack[AssociateWirelessGatewayWithThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a wireless gateway with a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/associate_wireless_gateway_with_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#associate_wireless_gateway_with_thing)
        """

    def cancel_multicast_group_session(
        self, **kwargs: Unpack[CancelMulticastGroupSessionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an existing multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/cancel_multicast_group_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#cancel_multicast_group_session)
        """

    def create_destination(
        self, **kwargs: Unpack[CreateDestinationRequestTypeDef]
    ) -> CreateDestinationResponseTypeDef:
        """
        Creates a new destination that maps a device message to an AWS IoT rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_destination)
        """

    def create_device_profile(
        self, **kwargs: Unpack[CreateDeviceProfileRequestTypeDef]
    ) -> CreateDeviceProfileResponseTypeDef:
        """
        Creates a new device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_device_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_device_profile)
        """

    def create_fuota_task(
        self, **kwargs: Unpack[CreateFuotaTaskRequestTypeDef]
    ) -> CreateFuotaTaskResponseTypeDef:
        """
        Creates a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_fuota_task)
        """

    def create_multicast_group(
        self, **kwargs: Unpack[CreateMulticastGroupRequestTypeDef]
    ) -> CreateMulticastGroupResponseTypeDef:
        """
        Creates a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_multicast_group)
        """

    def create_network_analyzer_configuration(
        self, **kwargs: Unpack[CreateNetworkAnalyzerConfigurationRequestTypeDef]
    ) -> CreateNetworkAnalyzerConfigurationResponseTypeDef:
        """
        Creates a new network analyzer configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_network_analyzer_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_network_analyzer_configuration)
        """

    def create_service_profile(
        self, **kwargs: Unpack[CreateServiceProfileRequestTypeDef]
    ) -> CreateServiceProfileResponseTypeDef:
        """
        Creates a new service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_service_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_service_profile)
        """

    def create_wireless_device(
        self, **kwargs: Unpack[CreateWirelessDeviceRequestTypeDef]
    ) -> CreateWirelessDeviceResponseTypeDef:
        """
        Provisions a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_wireless_device)
        """

    def create_wireless_gateway(
        self, **kwargs: Unpack[CreateWirelessGatewayRequestTypeDef]
    ) -> CreateWirelessGatewayResponseTypeDef:
        """
        Provisions a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_wireless_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_wireless_gateway)
        """

    def create_wireless_gateway_task(
        self, **kwargs: Unpack[CreateWirelessGatewayTaskRequestTypeDef]
    ) -> CreateWirelessGatewayTaskResponseTypeDef:
        """
        Creates a task for a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_wireless_gateway_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_wireless_gateway_task)
        """

    def create_wireless_gateway_task_definition(
        self, **kwargs: Unpack[CreateWirelessGatewayTaskDefinitionRequestTypeDef]
    ) -> CreateWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        Creates a gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/create_wireless_gateway_task_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#create_wireless_gateway_task_definition)
        """

    def delete_destination(
        self, **kwargs: Unpack[DeleteDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_destination)
        """

    def delete_device_profile(
        self, **kwargs: Unpack[DeleteDeviceProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_device_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_device_profile)
        """

    def delete_fuota_task(self, **kwargs: Unpack[DeleteFuotaTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_fuota_task)
        """

    def delete_multicast_group(
        self, **kwargs: Unpack[DeleteMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a multicast group if it is not in use by a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_multicast_group)
        """

    def delete_network_analyzer_configuration(
        self, **kwargs: Unpack[DeleteNetworkAnalyzerConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a network analyzer configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_network_analyzer_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_network_analyzer_configuration)
        """

    def delete_queued_messages(
        self, **kwargs: Unpack[DeleteQueuedMessagesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove queued messages from the downlink queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_queued_messages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_queued_messages)
        """

    def delete_service_profile(
        self, **kwargs: Unpack[DeleteServiceProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_service_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_service_profile)
        """

    def delete_wireless_device(
        self, **kwargs: Unpack[DeleteWirelessDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_wireless_device)
        """

    def delete_wireless_device_import_task(
        self, **kwargs: Unpack[DeleteWirelessDeviceImportTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete an import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_wireless_device_import_task)
        """

    def delete_wireless_gateway(
        self, **kwargs: Unpack[DeleteWirelessGatewayRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_wireless_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_wireless_gateway)
        """

    def delete_wireless_gateway_task(
        self, **kwargs: Unpack[DeleteWirelessGatewayTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a wireless gateway task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_wireless_gateway_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_wireless_gateway_task)
        """

    def delete_wireless_gateway_task_definition(
        self, **kwargs: Unpack[DeleteWirelessGatewayTaskDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a wireless gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/delete_wireless_gateway_task_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#delete_wireless_gateway_task_definition)
        """

    def deregister_wireless_device(
        self, **kwargs: Unpack[DeregisterWirelessDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregister a wireless device from AWS IoT Wireless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/deregister_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#deregister_wireless_device)
        """

    def disassociate_aws_account_from_partner_account(
        self, **kwargs: Unpack[DisassociateAwsAccountFromPartnerAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates your AWS account from a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_aws_account_from_partner_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_aws_account_from_partner_account)
        """

    def disassociate_multicast_group_from_fuota_task(
        self, **kwargs: Unpack[DisassociateMulticastGroupFromFuotaTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a multicast group from a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_multicast_group_from_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_multicast_group_from_fuota_task)
        """

    def disassociate_wireless_device_from_fuota_task(
        self, **kwargs: Unpack[DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless device from a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_wireless_device_from_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_wireless_device_from_fuota_task)
        """

    def disassociate_wireless_device_from_multicast_group(
        self, **kwargs: Unpack[DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless device from a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_wireless_device_from_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_wireless_device_from_multicast_group)
        """

    def disassociate_wireless_device_from_thing(
        self, **kwargs: Unpack[DisassociateWirelessDeviceFromThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless device from its currently associated thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_wireless_device_from_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_wireless_device_from_thing)
        """

    def disassociate_wireless_gateway_from_certificate(
        self, **kwargs: Unpack[DisassociateWirelessGatewayFromCertificateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless gateway from its currently associated certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_wireless_gateway_from_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_wireless_gateway_from_certificate)
        """

    def disassociate_wireless_gateway_from_thing(
        self, **kwargs: Unpack[DisassociateWirelessGatewayFromThingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a wireless gateway from its currently associated thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/disassociate_wireless_gateway_from_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#disassociate_wireless_gateway_from_thing)
        """

    def get_destination(
        self, **kwargs: Unpack[GetDestinationRequestTypeDef]
    ) -> GetDestinationResponseTypeDef:
        """
        Gets information about a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_destination)
        """

    def get_device_profile(
        self, **kwargs: Unpack[GetDeviceProfileRequestTypeDef]
    ) -> GetDeviceProfileResponseTypeDef:
        """
        Gets information about a device profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_device_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_device_profile)
        """

    def get_event_configuration_by_resource_types(
        self,
    ) -> GetEventConfigurationByResourceTypesResponseTypeDef:
        """
        Get the event configuration based on resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_event_configuration_by_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_event_configuration_by_resource_types)
        """

    def get_fuota_task(
        self, **kwargs: Unpack[GetFuotaTaskRequestTypeDef]
    ) -> GetFuotaTaskResponseTypeDef:
        """
        Gets information about a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_fuota_task)
        """

    def get_log_levels_by_resource_types(self) -> GetLogLevelsByResourceTypesResponseTypeDef:
        """
        Returns current default log levels or log levels by resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_log_levels_by_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_log_levels_by_resource_types)
        """

    def get_metric_configuration(self) -> GetMetricConfigurationResponseTypeDef:
        """
        Get the metric configuration status for this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_metric_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_metric_configuration)
        """

    def get_metrics(self, **kwargs: Unpack[GetMetricsRequestTypeDef]) -> GetMetricsResponseTypeDef:
        """
        Get the summary metrics for this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_metrics)
        """

    def get_multicast_group(
        self, **kwargs: Unpack[GetMulticastGroupRequestTypeDef]
    ) -> GetMulticastGroupResponseTypeDef:
        """
        Gets information about a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_multicast_group)
        """

    def get_multicast_group_session(
        self, **kwargs: Unpack[GetMulticastGroupSessionRequestTypeDef]
    ) -> GetMulticastGroupSessionResponseTypeDef:
        """
        Gets information about a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_multicast_group_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_multicast_group_session)
        """

    def get_network_analyzer_configuration(
        self, **kwargs: Unpack[GetNetworkAnalyzerConfigurationRequestTypeDef]
    ) -> GetNetworkAnalyzerConfigurationResponseTypeDef:
        """
        Get network analyzer configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_network_analyzer_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_network_analyzer_configuration)
        """

    def get_partner_account(
        self, **kwargs: Unpack[GetPartnerAccountRequestTypeDef]
    ) -> GetPartnerAccountResponseTypeDef:
        """
        Gets information about a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_partner_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_partner_account)
        """

    def get_position(
        self, **kwargs: Unpack[GetPositionRequestTypeDef]
    ) -> GetPositionResponseTypeDef:
        """
        Get the position information for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_position)
        """

    def get_position_configuration(
        self, **kwargs: Unpack[GetPositionConfigurationRequestTypeDef]
    ) -> GetPositionConfigurationResponseTypeDef:
        """
        Get position configuration for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_position_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_position_configuration)
        """

    def get_position_estimate(
        self, **kwargs: Unpack[GetPositionEstimateRequestTypeDef]
    ) -> GetPositionEstimateResponseTypeDef:
        """
        Get estimated position information as a payload in GeoJSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_position_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_position_estimate)
        """

    def get_resource_event_configuration(
        self, **kwargs: Unpack[GetResourceEventConfigurationRequestTypeDef]
    ) -> GetResourceEventConfigurationResponseTypeDef:
        """
        Get the event configuration for a particular resource identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_resource_event_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_resource_event_configuration)
        """

    def get_resource_log_level(
        self, **kwargs: Unpack[GetResourceLogLevelRequestTypeDef]
    ) -> GetResourceLogLevelResponseTypeDef:
        """
        Fetches the log-level override, if any, for a given resource ID and resource
        type..

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_resource_log_level.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_resource_log_level)
        """

    def get_resource_position(
        self, **kwargs: Unpack[GetResourcePositionRequestTypeDef]
    ) -> GetResourcePositionResponseTypeDef:
        """
        Get the position information for a given wireless device or a wireless gateway
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_resource_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_resource_position)
        """

    def get_service_endpoint(
        self, **kwargs: Unpack[GetServiceEndpointRequestTypeDef]
    ) -> GetServiceEndpointResponseTypeDef:
        """
        Gets the account-specific endpoint for Configuration and Update Server (CUPS)
        protocol or LoRaWAN Network Server (LNS) connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_service_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_service_endpoint)
        """

    def get_service_profile(
        self, **kwargs: Unpack[GetServiceProfileRequestTypeDef]
    ) -> GetServiceProfileResponseTypeDef:
        """
        Gets information about a service profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_service_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_service_profile)
        """

    def get_wireless_device(
        self, **kwargs: Unpack[GetWirelessDeviceRequestTypeDef]
    ) -> GetWirelessDeviceResponseTypeDef:
        """
        Gets information about a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_device)
        """

    def get_wireless_device_import_task(
        self, **kwargs: Unpack[GetWirelessDeviceImportTaskRequestTypeDef]
    ) -> GetWirelessDeviceImportTaskResponseTypeDef:
        """
        Get information about an import task and count of device onboarding summary
        information for the import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_device_import_task)
        """

    def get_wireless_device_statistics(
        self, **kwargs: Unpack[GetWirelessDeviceStatisticsRequestTypeDef]
    ) -> GetWirelessDeviceStatisticsResponseTypeDef:
        """
        Gets operating information about a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_device_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_device_statistics)
        """

    def get_wireless_gateway(
        self, **kwargs: Unpack[GetWirelessGatewayRequestTypeDef]
    ) -> GetWirelessGatewayResponseTypeDef:
        """
        Gets information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway)
        """

    def get_wireless_gateway_certificate(
        self, **kwargs: Unpack[GetWirelessGatewayCertificateRequestTypeDef]
    ) -> GetWirelessGatewayCertificateResponseTypeDef:
        """
        Gets the ID of the certificate that is currently associated with a wireless
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway_certificate)
        """

    def get_wireless_gateway_firmware_information(
        self, **kwargs: Unpack[GetWirelessGatewayFirmwareInformationRequestTypeDef]
    ) -> GetWirelessGatewayFirmwareInformationResponseTypeDef:
        """
        Gets the firmware version and other information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway_firmware_information.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway_firmware_information)
        """

    def get_wireless_gateway_statistics(
        self, **kwargs: Unpack[GetWirelessGatewayStatisticsRequestTypeDef]
    ) -> GetWirelessGatewayStatisticsResponseTypeDef:
        """
        Gets operating information about a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway_statistics)
        """

    def get_wireless_gateway_task(
        self, **kwargs: Unpack[GetWirelessGatewayTaskRequestTypeDef]
    ) -> GetWirelessGatewayTaskResponseTypeDef:
        """
        Gets information about a wireless gateway task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway_task)
        """

    def get_wireless_gateway_task_definition(
        self, **kwargs: Unpack[GetWirelessGatewayTaskDefinitionRequestTypeDef]
    ) -> GetWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        Gets information about a wireless gateway task definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/get_wireless_gateway_task_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#get_wireless_gateway_task_definition)
        """

    def list_destinations(
        self, **kwargs: Unpack[ListDestinationsRequestTypeDef]
    ) -> ListDestinationsResponseTypeDef:
        """
        Lists the destinations registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_destinations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_destinations)
        """

    def list_device_profiles(
        self, **kwargs: Unpack[ListDeviceProfilesRequestTypeDef]
    ) -> ListDeviceProfilesResponseTypeDef:
        """
        Lists the device profiles registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_device_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_device_profiles)
        """

    def list_devices_for_wireless_device_import_task(
        self, **kwargs: Unpack[ListDevicesForWirelessDeviceImportTaskRequestTypeDef]
    ) -> ListDevicesForWirelessDeviceImportTaskResponseTypeDef:
        """
        List the Sidewalk devices in an import task and their onboarding status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_devices_for_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_devices_for_wireless_device_import_task)
        """

    def list_event_configurations(
        self, **kwargs: Unpack[ListEventConfigurationsRequestTypeDef]
    ) -> ListEventConfigurationsResponseTypeDef:
        """
        List event configurations where at least one event topic has been enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_event_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_event_configurations)
        """

    def list_fuota_tasks(
        self, **kwargs: Unpack[ListFuotaTasksRequestTypeDef]
    ) -> ListFuotaTasksResponseTypeDef:
        """
        Lists the FUOTA tasks registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_fuota_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_fuota_tasks)
        """

    def list_multicast_groups(
        self, **kwargs: Unpack[ListMulticastGroupsRequestTypeDef]
    ) -> ListMulticastGroupsResponseTypeDef:
        """
        Lists the multicast groups registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_multicast_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_multicast_groups)
        """

    def list_multicast_groups_by_fuota_task(
        self, **kwargs: Unpack[ListMulticastGroupsByFuotaTaskRequestTypeDef]
    ) -> ListMulticastGroupsByFuotaTaskResponseTypeDef:
        """
        List all multicast groups associated with a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_multicast_groups_by_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_multicast_groups_by_fuota_task)
        """

    def list_network_analyzer_configurations(
        self, **kwargs: Unpack[ListNetworkAnalyzerConfigurationsRequestTypeDef]
    ) -> ListNetworkAnalyzerConfigurationsResponseTypeDef:
        """
        Lists the network analyzer configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_network_analyzer_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_network_analyzer_configurations)
        """

    def list_partner_accounts(
        self, **kwargs: Unpack[ListPartnerAccountsRequestTypeDef]
    ) -> ListPartnerAccountsResponseTypeDef:
        """
        Lists the partner accounts associated with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_partner_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_partner_accounts)
        """

    def list_position_configurations(
        self, **kwargs: Unpack[ListPositionConfigurationsRequestTypeDef]
    ) -> ListPositionConfigurationsResponseTypeDef:
        """
        List position configurations for a given resource, such as positioning solvers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_position_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_position_configurations)
        """

    def list_queued_messages(
        self, **kwargs: Unpack[ListQueuedMessagesRequestTypeDef]
    ) -> ListQueuedMessagesResponseTypeDef:
        """
        List queued messages in the downlink queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_queued_messages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_queued_messages)
        """

    def list_service_profiles(
        self, **kwargs: Unpack[ListServiceProfilesRequestTypeDef]
    ) -> ListServiceProfilesResponseTypeDef:
        """
        Lists the service profiles registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_service_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_service_profiles)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_tags_for_resource)
        """

    def list_wireless_device_import_tasks(
        self, **kwargs: Unpack[ListWirelessDeviceImportTasksRequestTypeDef]
    ) -> ListWirelessDeviceImportTasksResponseTypeDef:
        """
        List wireless devices that have been added to an import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_wireless_device_import_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_wireless_device_import_tasks)
        """

    def list_wireless_devices(
        self, **kwargs: Unpack[ListWirelessDevicesRequestTypeDef]
    ) -> ListWirelessDevicesResponseTypeDef:
        """
        Lists the wireless devices registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_wireless_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_wireless_devices)
        """

    def list_wireless_gateway_task_definitions(
        self, **kwargs: Unpack[ListWirelessGatewayTaskDefinitionsRequestTypeDef]
    ) -> ListWirelessGatewayTaskDefinitionsResponseTypeDef:
        """
        List the wireless gateway tasks definitions registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_wireless_gateway_task_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_wireless_gateway_task_definitions)
        """

    def list_wireless_gateways(
        self, **kwargs: Unpack[ListWirelessGatewaysRequestTypeDef]
    ) -> ListWirelessGatewaysResponseTypeDef:
        """
        Lists the wireless gateways registered to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/list_wireless_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#list_wireless_gateways)
        """

    def put_position_configuration(
        self, **kwargs: Unpack[PutPositionConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Put position configuration for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/put_position_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#put_position_configuration)
        """

    def put_resource_log_level(
        self, **kwargs: Unpack[PutResourceLogLevelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the log-level override for a resource ID and resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/put_resource_log_level.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#put_resource_log_level)
        """

    def reset_all_resource_log_levels(self) -> Dict[str, Any]:
        """
        Removes the log-level overrides for all resources; wireless devices, wireless
        gateways, and FUOTA tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/reset_all_resource_log_levels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#reset_all_resource_log_levels)
        """

    def reset_resource_log_level(
        self, **kwargs: Unpack[ResetResourceLogLevelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the log-level override, if any, for a specific resource ID and resource
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/reset_resource_log_level.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#reset_resource_log_level)
        """

    def send_data_to_multicast_group(
        self, **kwargs: Unpack[SendDataToMulticastGroupRequestTypeDef]
    ) -> SendDataToMulticastGroupResponseTypeDef:
        """
        Sends the specified data to a multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/send_data_to_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#send_data_to_multicast_group)
        """

    def send_data_to_wireless_device(
        self, **kwargs: Unpack[SendDataToWirelessDeviceRequestTypeDef]
    ) -> SendDataToWirelessDeviceResponseTypeDef:
        """
        Sends a decrypted application data frame to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/send_data_to_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#send_data_to_wireless_device)
        """

    def start_bulk_associate_wireless_device_with_multicast_group(
        self, **kwargs: Unpack[StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a bulk association of all qualifying wireless devices with a multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_bulk_associate_wireless_device_with_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_bulk_associate_wireless_device_with_multicast_group)
        """

    def start_bulk_disassociate_wireless_device_from_multicast_group(
        self, **kwargs: Unpack[StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a bulk disassociatin of all qualifying wireless devices from a multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_bulk_disassociate_wireless_device_from_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_bulk_disassociate_wireless_device_from_multicast_group)
        """

    def start_fuota_task(self, **kwargs: Unpack[StartFuotaTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_fuota_task)
        """

    def start_multicast_group_session(
        self, **kwargs: Unpack[StartMulticastGroupSessionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_multicast_group_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_multicast_group_session)
        """

    def start_single_wireless_device_import_task(
        self, **kwargs: Unpack[StartSingleWirelessDeviceImportTaskRequestTypeDef]
    ) -> StartSingleWirelessDeviceImportTaskResponseTypeDef:
        """
        Start import task for a single wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_single_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_single_wireless_device_import_task)
        """

    def start_wireless_device_import_task(
        self, **kwargs: Unpack[StartWirelessDeviceImportTaskRequestTypeDef]
    ) -> StartWirelessDeviceImportTaskResponseTypeDef:
        """
        Start import task for provisioning Sidewalk devices in bulk using an S3 CSV
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/start_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#start_wireless_device_import_task)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#tag_resource)
        """

    def test_wireless_device(
        self, **kwargs: Unpack[TestWirelessDeviceRequestTypeDef]
    ) -> TestWirelessDeviceResponseTypeDef:
        """
        Simulates a provisioned device by sending an uplink data payload of
        <code>Hello</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/test_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#test_wireless_device)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#untag_resource)
        """

    def update_destination(
        self, **kwargs: Unpack[UpdateDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates properties of a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_destination)
        """

    def update_event_configuration_by_resource_types(
        self, **kwargs: Unpack[UpdateEventConfigurationByResourceTypesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update the event configuration based on resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_event_configuration_by_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_event_configuration_by_resource_types)
        """

    def update_fuota_task(self, **kwargs: Unpack[UpdateFuotaTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates properties of a FUOTA task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_fuota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_fuota_task)
        """

    def update_log_levels_by_resource_types(
        self, **kwargs: Unpack[UpdateLogLevelsByResourceTypesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set default log level, or log levels by resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_log_levels_by_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_log_levels_by_resource_types)
        """

    def update_metric_configuration(
        self, **kwargs: Unpack[UpdateMetricConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update the summary metric configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_metric_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_metric_configuration)
        """

    def update_multicast_group(
        self, **kwargs: Unpack[UpdateMulticastGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates properties of a multicast group session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_multicast_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_multicast_group)
        """

    def update_network_analyzer_configuration(
        self, **kwargs: Unpack[UpdateNetworkAnalyzerConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update network analyzer configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_network_analyzer_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_network_analyzer_configuration)
        """

    def update_partner_account(
        self, **kwargs: Unpack[UpdatePartnerAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates properties of a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_partner_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_partner_account)
        """

    def update_position(self, **kwargs: Unpack[UpdatePositionRequestTypeDef]) -> Dict[str, Any]:
        """
        Update the position information of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_position)
        """

    def update_resource_event_configuration(
        self, **kwargs: Unpack[UpdateResourceEventConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update the event configuration for a particular resource identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_resource_event_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_resource_event_configuration)
        """

    def update_resource_position(
        self, **kwargs: Unpack[UpdateResourcePositionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update the position information of a given wireless device or a wireless
        gateway resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_resource_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_resource_position)
        """

    def update_wireless_device(
        self, **kwargs: Unpack[UpdateWirelessDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates properties of a wireless device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_wireless_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_wireless_device)
        """

    def update_wireless_device_import_task(
        self, **kwargs: Unpack[UpdateWirelessDeviceImportTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update an import task to add more devices to the task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_wireless_device_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_wireless_device_import_task)
        """

    def update_wireless_gateway(
        self, **kwargs: Unpack[UpdateWirelessGatewayRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates properties of a wireless gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless/client/update_wireless_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client/#update_wireless_gateway)
        """
