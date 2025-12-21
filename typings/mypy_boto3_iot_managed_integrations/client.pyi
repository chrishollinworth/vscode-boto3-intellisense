"""
Type annotations for iot-managed-integrations service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iot_managed_integrations.client import ManagedintegrationsforIoTDeviceManagementClient

    session = Session()
    client: ManagedintegrationsforIoTDeviceManagementClient = session.client("iot-managed-integrations")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccountAssociationsPaginator,
    ListCloudConnectorsPaginator,
    ListConnectorDestinationsPaginator,
    ListCredentialLockersPaginator,
    ListDestinationsPaginator,
    ListDeviceDiscoveriesPaginator,
    ListDiscoveredDevicesPaginator,
    ListEventLogConfigurationsPaginator,
    ListManagedThingAccountAssociationsPaginator,
    ListManagedThingSchemasPaginator,
    ListManagedThingsPaginator,
    ListNotificationConfigurationsPaginator,
    ListOtaTaskConfigurationsPaginator,
    ListOtaTaskExecutionsPaginator,
    ListOtaTasksPaginator,
    ListProvisioningProfilesPaginator,
    ListSchemaVersionsPaginator,
)
from .type_defs import (
    CreateAccountAssociationRequestTypeDef,
    CreateAccountAssociationResponseTypeDef,
    CreateCloudConnectorRequestTypeDef,
    CreateCloudConnectorResponseTypeDef,
    CreateConnectorDestinationRequestTypeDef,
    CreateConnectorDestinationResponseTypeDef,
    CreateCredentialLockerRequestTypeDef,
    CreateCredentialLockerResponseTypeDef,
    CreateDestinationRequestTypeDef,
    CreateDestinationResponseTypeDef,
    CreateEventLogConfigurationRequestTypeDef,
    CreateEventLogConfigurationResponseTypeDef,
    CreateManagedThingRequestTypeDef,
    CreateManagedThingResponseTypeDef,
    CreateNotificationConfigurationRequestTypeDef,
    CreateNotificationConfigurationResponseTypeDef,
    CreateOtaTaskConfigurationRequestTypeDef,
    CreateOtaTaskConfigurationResponseTypeDef,
    CreateOtaTaskRequestTypeDef,
    CreateOtaTaskResponseTypeDef,
    CreateProvisioningProfileRequestTypeDef,
    CreateProvisioningProfileResponseTypeDef,
    DeleteAccountAssociationRequestTypeDef,
    DeleteCloudConnectorRequestTypeDef,
    DeleteConnectorDestinationRequestTypeDef,
    DeleteCredentialLockerRequestTypeDef,
    DeleteDestinationRequestTypeDef,
    DeleteEventLogConfigurationRequestTypeDef,
    DeleteManagedThingRequestTypeDef,
    DeleteNotificationConfigurationRequestTypeDef,
    DeleteOtaTaskConfigurationRequestTypeDef,
    DeleteOtaTaskRequestTypeDef,
    DeleteProvisioningProfileRequestTypeDef,
    DeregisterAccountAssociationRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccountAssociationRequestTypeDef,
    GetAccountAssociationResponseTypeDef,
    GetCloudConnectorRequestTypeDef,
    GetCloudConnectorResponseTypeDef,
    GetConnectorDestinationRequestTypeDef,
    GetConnectorDestinationResponseTypeDef,
    GetCredentialLockerRequestTypeDef,
    GetCredentialLockerResponseTypeDef,
    GetCustomEndpointResponseTypeDef,
    GetDefaultEncryptionConfigurationResponseTypeDef,
    GetDestinationRequestTypeDef,
    GetDestinationResponseTypeDef,
    GetDeviceDiscoveryRequestTypeDef,
    GetDeviceDiscoveryResponseTypeDef,
    GetEventLogConfigurationRequestTypeDef,
    GetEventLogConfigurationResponseTypeDef,
    GetHubConfigurationResponseTypeDef,
    GetManagedThingCapabilitiesRequestTypeDef,
    GetManagedThingCapabilitiesResponseTypeDef,
    GetManagedThingCertificateRequestTypeDef,
    GetManagedThingCertificateResponseTypeDef,
    GetManagedThingConnectivityDataRequestTypeDef,
    GetManagedThingConnectivityDataResponseTypeDef,
    GetManagedThingMetaDataRequestTypeDef,
    GetManagedThingMetaDataResponseTypeDef,
    GetManagedThingRequestTypeDef,
    GetManagedThingResponseTypeDef,
    GetManagedThingStateRequestTypeDef,
    GetManagedThingStateResponseTypeDef,
    GetNotificationConfigurationRequestTypeDef,
    GetNotificationConfigurationResponseTypeDef,
    GetOtaTaskConfigurationRequestTypeDef,
    GetOtaTaskConfigurationResponseTypeDef,
    GetOtaTaskRequestTypeDef,
    GetOtaTaskResponseTypeDef,
    GetProvisioningProfileRequestTypeDef,
    GetProvisioningProfileResponseTypeDef,
    GetRuntimeLogConfigurationRequestTypeDef,
    GetRuntimeLogConfigurationResponseTypeDef,
    GetSchemaVersionRequestTypeDef,
    GetSchemaVersionResponseTypeDef,
    ListAccountAssociationsRequestTypeDef,
    ListAccountAssociationsResponseTypeDef,
    ListCloudConnectorsRequestTypeDef,
    ListCloudConnectorsResponseTypeDef,
    ListConnectorDestinationsRequestTypeDef,
    ListConnectorDestinationsResponseTypeDef,
    ListCredentialLockersRequestTypeDef,
    ListCredentialLockersResponseTypeDef,
    ListDestinationsRequestTypeDef,
    ListDestinationsResponseTypeDef,
    ListDeviceDiscoveriesRequestTypeDef,
    ListDeviceDiscoveriesResponseTypeDef,
    ListDiscoveredDevicesRequestTypeDef,
    ListDiscoveredDevicesResponseTypeDef,
    ListEventLogConfigurationsRequestTypeDef,
    ListEventLogConfigurationsResponseTypeDef,
    ListManagedThingAccountAssociationsRequestTypeDef,
    ListManagedThingAccountAssociationsResponseTypeDef,
    ListManagedThingSchemasRequestTypeDef,
    ListManagedThingSchemasResponseTypeDef,
    ListManagedThingsRequestTypeDef,
    ListManagedThingsResponseTypeDef,
    ListNotificationConfigurationsRequestTypeDef,
    ListNotificationConfigurationsResponseTypeDef,
    ListOtaTaskConfigurationsRequestTypeDef,
    ListOtaTaskConfigurationsResponseTypeDef,
    ListOtaTaskExecutionsRequestTypeDef,
    ListOtaTaskExecutionsResponseTypeDef,
    ListOtaTasksRequestTypeDef,
    ListOtaTasksResponseTypeDef,
    ListProvisioningProfilesRequestTypeDef,
    ListProvisioningProfilesResponseTypeDef,
    ListSchemaVersionsRequestTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutDefaultEncryptionConfigurationRequestTypeDef,
    PutDefaultEncryptionConfigurationResponseTypeDef,
    PutHubConfigurationRequestTypeDef,
    PutHubConfigurationResponseTypeDef,
    PutRuntimeLogConfigurationRequestTypeDef,
    RegisterAccountAssociationRequestTypeDef,
    RegisterAccountAssociationResponseTypeDef,
    RegisterCustomEndpointResponseTypeDef,
    ResetRuntimeLogConfigurationRequestTypeDef,
    SendConnectorEventRequestTypeDef,
    SendConnectorEventResponseTypeDef,
    SendManagedThingCommandRequestTypeDef,
    SendManagedThingCommandResponseTypeDef,
    StartAccountAssociationRefreshRequestTypeDef,
    StartAccountAssociationRefreshResponseTypeDef,
    StartDeviceDiscoveryRequestTypeDef,
    StartDeviceDiscoveryResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccountAssociationRequestTypeDef,
    UpdateCloudConnectorRequestTypeDef,
    UpdateConnectorDestinationRequestTypeDef,
    UpdateDestinationRequestTypeDef,
    UpdateEventLogConfigurationRequestTypeDef,
    UpdateManagedThingRequestTypeDef,
    UpdateNotificationConfigurationRequestTypeDef,
    UpdateOtaTaskRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ManagedintegrationsforIoTDeviceManagementClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ManagedintegrationsforIoTDeviceManagementClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations.html#ManagedintegrationsforIoTDeviceManagement.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedintegrationsforIoTDeviceManagementClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations.html#ManagedintegrationsforIoTDeviceManagement.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#generate_presigned_url)
        """

    def create_account_association(
        self, **kwargs: Unpack[CreateAccountAssociationRequestTypeDef]
    ) -> CreateAccountAssociationResponseTypeDef:
        """
        Creates a new account association via the destination id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_account_association)
        """

    def create_cloud_connector(
        self, **kwargs: Unpack[CreateCloudConnectorRequestTypeDef]
    ) -> CreateCloudConnectorResponseTypeDef:
        """
        Creates a C2C (cloud-to-cloud) connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_cloud_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_cloud_connector)
        """

    def create_connector_destination(
        self, **kwargs: Unpack[CreateConnectorDestinationRequestTypeDef]
    ) -> CreateConnectorDestinationResponseTypeDef:
        """
        Create a connector destination for connecting a cloud-to-cloud (C2C) connector
        to the customer's Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_connector_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_connector_destination)
        """

    def create_credential_locker(
        self, **kwargs: Unpack[CreateCredentialLockerRequestTypeDef]
    ) -> CreateCredentialLockerResponseTypeDef:
        """
        Create a credential locker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_credential_locker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_credential_locker)
        """

    def create_destination(
        self, **kwargs: Unpack[CreateDestinationRequestTypeDef]
    ) -> CreateDestinationResponseTypeDef:
        """
        Create a notification destination such as Kinesis Data Streams that receive
        events and notifications from Managed integrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_destination)
        """

    def create_event_log_configuration(
        self, **kwargs: Unpack[CreateEventLogConfigurationRequestTypeDef]
    ) -> CreateEventLogConfigurationResponseTypeDef:
        """
        Set the event log configuration for the account, resource type, or specific
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_event_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_event_log_configuration)
        """

    def create_managed_thing(
        self, **kwargs: Unpack[CreateManagedThingRequestTypeDef]
    ) -> CreateManagedThingResponseTypeDef:
        """
        Creates a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_managed_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_managed_thing)
        """

    def create_notification_configuration(
        self, **kwargs: Unpack[CreateNotificationConfigurationRequestTypeDef]
    ) -> CreateNotificationConfigurationResponseTypeDef:
        """
        Creates a notification configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_notification_configuration)
        """

    def create_ota_task(
        self, **kwargs: Unpack[CreateOtaTaskRequestTypeDef]
    ) -> CreateOtaTaskResponseTypeDef:
        """
        Create an over-the-air (OTA) task to target a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_ota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_ota_task)
        """

    def create_ota_task_configuration(
        self, **kwargs: Unpack[CreateOtaTaskConfigurationRequestTypeDef]
    ) -> CreateOtaTaskConfigurationResponseTypeDef:
        """
        Create a configuraiton for the over-the-air (OTA) task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_ota_task_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_ota_task_configuration)
        """

    def create_provisioning_profile(
        self, **kwargs: Unpack[CreateProvisioningProfileRequestTypeDef]
    ) -> CreateProvisioningProfileResponseTypeDef:
        """
        Create a provisioning profile for a device to execute the provisioning flows
        using a provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/create_provisioning_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#create_provisioning_profile)
        """

    def delete_account_association(
        self, **kwargs: Unpack[DeleteAccountAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove a third-party account association for an end user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_account_association)
        """

    def delete_cloud_connector(
        self, **kwargs: Unpack[DeleteCloudConnectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a cloud connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_cloud_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_cloud_connector)
        """

    def delete_connector_destination(
        self, **kwargs: Unpack[DeleteConnectorDestinationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a connector destination linked to a cloud-to-cloud (C2C) connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_connector_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_connector_destination)
        """

    def delete_credential_locker(
        self, **kwargs: Unpack[DeleteCredentialLockerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a credential locker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_credential_locker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_credential_locker)
        """

    def delete_destination(
        self, **kwargs: Unpack[DeleteDestinationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a notification destination specified by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_destination)
        """

    def delete_event_log_configuration(
        self, **kwargs: Unpack[DeleteEventLogConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete an event log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_event_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_event_log_configuration)
        """

    def delete_managed_thing(
        self, **kwargs: Unpack[DeleteManagedThingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_managed_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_managed_thing)
        """

    def delete_notification_configuration(
        self, **kwargs: Unpack[DeleteNotificationConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a notification configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_notification_configuration)
        """

    def delete_ota_task(
        self, **kwargs: Unpack[DeleteOtaTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the over-the-air (OTA) task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_ota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_ota_task)
        """

    def delete_ota_task_configuration(
        self, **kwargs: Unpack[DeleteOtaTaskConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the over-the-air (OTA) task configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_ota_task_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_ota_task_configuration)
        """

    def delete_provisioning_profile(
        self, **kwargs: Unpack[DeleteProvisioningProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a provisioning profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/delete_provisioning_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#delete_provisioning_profile)
        """

    def deregister_account_association(
        self, **kwargs: Unpack[DeregisterAccountAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregister an account association from a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/deregister_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#deregister_account_association)
        """

    def get_account_association(
        self, **kwargs: Unpack[GetAccountAssociationRequestTypeDef]
    ) -> GetAccountAssociationResponseTypeDef:
        """
        Get an account association for an Amazon Web Services account linked to a
        customer-managed destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_account_association)
        """

    def get_cloud_connector(
        self, **kwargs: Unpack[GetCloudConnectorRequestTypeDef]
    ) -> GetCloudConnectorResponseTypeDef:
        """
        Get configuration details for a cloud connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_cloud_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_cloud_connector)
        """

    def get_connector_destination(
        self, **kwargs: Unpack[GetConnectorDestinationRequestTypeDef]
    ) -> GetConnectorDestinationResponseTypeDef:
        """
        Get connector destination details linked to a cloud-to-cloud (C2C) connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_connector_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_connector_destination)
        """

    def get_credential_locker(
        self, **kwargs: Unpack[GetCredentialLockerRequestTypeDef]
    ) -> GetCredentialLockerResponseTypeDef:
        """
        Get information on an existing credential locker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_credential_locker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_credential_locker)
        """

    def get_custom_endpoint(self) -> GetCustomEndpointResponseTypeDef:
        """
        Returns the IoT managed integrations custom endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_custom_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_custom_endpoint)
        """

    def get_default_encryption_configuration(
        self,
    ) -> GetDefaultEncryptionConfigurationResponseTypeDef:
        """
        Retrieves information about the default encryption configuration for the Amazon
        Web Services account in the default or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_default_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_default_encryption_configuration)
        """

    def get_destination(
        self, **kwargs: Unpack[GetDestinationRequestTypeDef]
    ) -> GetDestinationResponseTypeDef:
        """
        Gets a destination by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_destination)
        """

    def get_device_discovery(
        self, **kwargs: Unpack[GetDeviceDiscoveryRequestTypeDef]
    ) -> GetDeviceDiscoveryResponseTypeDef:
        """
        Get the current state of a device discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_device_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_device_discovery)
        """

    def get_event_log_configuration(
        self, **kwargs: Unpack[GetEventLogConfigurationRequestTypeDef]
    ) -> GetEventLogConfigurationResponseTypeDef:
        """
        Get an event log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_event_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_event_log_configuration)
        """

    def get_hub_configuration(self) -> GetHubConfigurationResponseTypeDef:
        """
        Get a hub configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_hub_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_hub_configuration)
        """

    def get_managed_thing(
        self, **kwargs: Unpack[GetManagedThingRequestTypeDef]
    ) -> GetManagedThingResponseTypeDef:
        """
        Get details of a managed thing including its attributes and capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing)
        """

    def get_managed_thing_capabilities(
        self, **kwargs: Unpack[GetManagedThingCapabilitiesRequestTypeDef]
    ) -> GetManagedThingCapabilitiesResponseTypeDef:
        """
        Get the capabilities for a managed thing using the device ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing_capabilities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing_capabilities)
        """

    def get_managed_thing_certificate(
        self, **kwargs: Unpack[GetManagedThingCertificateRequestTypeDef]
    ) -> GetManagedThingCertificateResponseTypeDef:
        """
        Retrieves the certificate PEM for a managed IoT thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing_certificate)
        """

    def get_managed_thing_connectivity_data(
        self, **kwargs: Unpack[GetManagedThingConnectivityDataRequestTypeDef]
    ) -> GetManagedThingConnectivityDataResponseTypeDef:
        """
        Get the connectivity status of a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing_connectivity_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing_connectivity_data)
        """

    def get_managed_thing_meta_data(
        self, **kwargs: Unpack[GetManagedThingMetaDataRequestTypeDef]
    ) -> GetManagedThingMetaDataResponseTypeDef:
        """
        Get the metadata information for a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing_meta_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing_meta_data)
        """

    def get_managed_thing_state(
        self, **kwargs: Unpack[GetManagedThingStateRequestTypeDef]
    ) -> GetManagedThingStateResponseTypeDef:
        """
        Returns the managed thing state for the given device Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_managed_thing_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_managed_thing_state)
        """

    def get_notification_configuration(
        self, **kwargs: Unpack[GetNotificationConfigurationRequestTypeDef]
    ) -> GetNotificationConfigurationResponseTypeDef:
        """
        Get a notification configuration for a specified event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_notification_configuration)
        """

    def get_ota_task(self, **kwargs: Unpack[GetOtaTaskRequestTypeDef]) -> GetOtaTaskResponseTypeDef:
        """
        Get details of the over-the-air (OTA) task by its task id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_ota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_ota_task)
        """

    def get_ota_task_configuration(
        self, **kwargs: Unpack[GetOtaTaskConfigurationRequestTypeDef]
    ) -> GetOtaTaskConfigurationResponseTypeDef:
        """
        Get a configuraiton for the over-the-air (OTA) task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_ota_task_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_ota_task_configuration)
        """

    def get_provisioning_profile(
        self, **kwargs: Unpack[GetProvisioningProfileRequestTypeDef]
    ) -> GetProvisioningProfileResponseTypeDef:
        """
        Get a provisioning profile by template name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_provisioning_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_provisioning_profile)
        """

    def get_runtime_log_configuration(
        self, **kwargs: Unpack[GetRuntimeLogConfigurationRequestTypeDef]
    ) -> GetRuntimeLogConfigurationResponseTypeDef:
        """
        Get the runtime log configuration for a specific managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_runtime_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_runtime_log_configuration)
        """

    def get_schema_version(
        self, **kwargs: Unpack[GetSchemaVersionRequestTypeDef]
    ) -> GetSchemaVersionResponseTypeDef:
        """
        Gets a schema version with the provided information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_schema_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_schema_version)
        """

    def list_account_associations(
        self, **kwargs: Unpack[ListAccountAssociationsRequestTypeDef]
    ) -> ListAccountAssociationsResponseTypeDef:
        """
        Lists all account associations, with optional filtering by connector
        destination ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_account_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_account_associations)
        """

    def list_cloud_connectors(
        self, **kwargs: Unpack[ListCloudConnectorsRequestTypeDef]
    ) -> ListCloudConnectorsResponseTypeDef:
        """
        Returns a list of connectors filtered by its Lambda Amazon Resource Name (ARN)
        and <code>type</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_cloud_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_cloud_connectors)
        """

    def list_connector_destinations(
        self, **kwargs: Unpack[ListConnectorDestinationsRequestTypeDef]
    ) -> ListConnectorDestinationsResponseTypeDef:
        """
        Lists all connector destinations, with optional filtering by cloud connector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_connector_destinations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_connector_destinations)
        """

    def list_credential_lockers(
        self, **kwargs: Unpack[ListCredentialLockersRequestTypeDef]
    ) -> ListCredentialLockersResponseTypeDef:
        """
        List information on an existing credential locker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_credential_lockers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_credential_lockers)
        """

    def list_destinations(
        self, **kwargs: Unpack[ListDestinationsRequestTypeDef]
    ) -> ListDestinationsResponseTypeDef:
        """
        List all notification destinations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_destinations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_destinations)
        """

    def list_device_discoveries(
        self, **kwargs: Unpack[ListDeviceDiscoveriesRequestTypeDef]
    ) -> ListDeviceDiscoveriesResponseTypeDef:
        """
        Lists all device discovery tasks, with optional filtering by type and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_device_discoveries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_device_discoveries)
        """

    def list_discovered_devices(
        self, **kwargs: Unpack[ListDiscoveredDevicesRequestTypeDef]
    ) -> ListDiscoveredDevicesResponseTypeDef:
        """
        Lists all devices discovered during a specific device discovery task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_discovered_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_discovered_devices)
        """

    def list_event_log_configurations(
        self, **kwargs: Unpack[ListEventLogConfigurationsRequestTypeDef]
    ) -> ListEventLogConfigurationsResponseTypeDef:
        """
        List all event log configurations for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_event_log_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_event_log_configurations)
        """

    def list_managed_thing_account_associations(
        self, **kwargs: Unpack[ListManagedThingAccountAssociationsRequestTypeDef]
    ) -> ListManagedThingAccountAssociationsResponseTypeDef:
        """
        Lists all account associations for a specific managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_managed_thing_account_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_managed_thing_account_associations)
        """

    def list_managed_thing_schemas(
        self, **kwargs: Unpack[ListManagedThingSchemasRequestTypeDef]
    ) -> ListManagedThingSchemasResponseTypeDef:
        """
        List schemas associated with a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_managed_thing_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_managed_thing_schemas)
        """

    def list_managed_things(
        self, **kwargs: Unpack[ListManagedThingsRequestTypeDef]
    ) -> ListManagedThingsResponseTypeDef:
        """
        Listing all managed things with provision for filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_managed_things.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_managed_things)
        """

    def list_notification_configurations(
        self, **kwargs: Unpack[ListNotificationConfigurationsRequestTypeDef]
    ) -> ListNotificationConfigurationsResponseTypeDef:
        """
        List all notification configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_notification_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_notification_configurations)
        """

    def list_ota_task_configurations(
        self, **kwargs: Unpack[ListOtaTaskConfigurationsRequestTypeDef]
    ) -> ListOtaTaskConfigurationsResponseTypeDef:
        """
        List all of the over-the-air (OTA) task configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_ota_task_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_ota_task_configurations)
        """

    def list_ota_task_executions(
        self, **kwargs: Unpack[ListOtaTaskExecutionsRequestTypeDef]
    ) -> ListOtaTaskExecutionsResponseTypeDef:
        """
        List all of the over-the-air (OTA) task executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_ota_task_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_ota_task_executions)
        """

    def list_ota_tasks(
        self, **kwargs: Unpack[ListOtaTasksRequestTypeDef]
    ) -> ListOtaTasksResponseTypeDef:
        """
        List all of the over-the-air (OTA) tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_ota_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_ota_tasks)
        """

    def list_provisioning_profiles(
        self, **kwargs: Unpack[ListProvisioningProfilesRequestTypeDef]
    ) -> ListProvisioningProfilesResponseTypeDef:
        """
        List the provisioning profiles within the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_provisioning_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_provisioning_profiles)
        """

    def list_schema_versions(
        self, **kwargs: Unpack[ListSchemaVersionsRequestTypeDef]
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        Lists schema versions with the provided information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_schema_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_schema_versions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#list_tags_for_resource)
        """

    def put_default_encryption_configuration(
        self, **kwargs: Unpack[PutDefaultEncryptionConfigurationRequestTypeDef]
    ) -> PutDefaultEncryptionConfigurationResponseTypeDef:
        """
        Sets the default encryption configuration for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/put_default_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#put_default_encryption_configuration)
        """

    def put_hub_configuration(
        self, **kwargs: Unpack[PutHubConfigurationRequestTypeDef]
    ) -> PutHubConfigurationResponseTypeDef:
        """
        Update a hub configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/put_hub_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#put_hub_configuration)
        """

    def put_runtime_log_configuration(
        self, **kwargs: Unpack[PutRuntimeLogConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Set the runtime log configuration for a specific managed thing or for all
        managed things as a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/put_runtime_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#put_runtime_log_configuration)
        """

    def register_account_association(
        self, **kwargs: Unpack[RegisterAccountAssociationRequestTypeDef]
    ) -> RegisterAccountAssociationResponseTypeDef:
        """
        Registers an account association with a managed thing, establishing a
        connection between a device and a third-party account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/register_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#register_account_association)
        """

    def register_custom_endpoint(self) -> RegisterCustomEndpointResponseTypeDef:
        """
        Customers can request IoT managed integrations to manage the server trust for
        them or bring their own external server trusts for the custom domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/register_custom_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#register_custom_endpoint)
        """

    def reset_runtime_log_configuration(
        self, **kwargs: Unpack[ResetRuntimeLogConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Reset a runtime log configuration for a specific managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/reset_runtime_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#reset_runtime_log_configuration)
        """

    def send_connector_event(
        self, **kwargs: Unpack[SendConnectorEventRequestTypeDef]
    ) -> SendConnectorEventResponseTypeDef:
        """
        Relays third-party device events for a connector such as a new device or a
        device state change event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/send_connector_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#send_connector_event)
        """

    def send_managed_thing_command(
        self, **kwargs: Unpack[SendManagedThingCommandRequestTypeDef]
    ) -> SendManagedThingCommandResponseTypeDef:
        """
        Send the command to the device represented by the managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/send_managed_thing_command.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#send_managed_thing_command)
        """

    def start_account_association_refresh(
        self, **kwargs: Unpack[StartAccountAssociationRefreshRequestTypeDef]
    ) -> StartAccountAssociationRefreshResponseTypeDef:
        """
        Initiates a refresh of an existing account association to update its
        authorization and connection status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/start_account_association_refresh.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#start_account_association_refresh)
        """

    def start_device_discovery(
        self, **kwargs: Unpack[StartDeviceDiscoveryRequestTypeDef]
    ) -> StartDeviceDiscoveryResponseTypeDef:
        """
        This API is used to start device discovery for hub-connected and
        third-party-connected devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/start_device_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#start_device_discovery)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#untag_resource)
        """

    def update_account_association(
        self, **kwargs: Unpack[UpdateAccountAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the properties of an existing account association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_account_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_account_association)
        """

    def update_cloud_connector(
        self, **kwargs: Unpack[UpdateCloudConnectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update an existing cloud connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_cloud_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_cloud_connector)
        """

    def update_connector_destination(
        self, **kwargs: Unpack[UpdateConnectorDestinationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the properties of an existing connector destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_connector_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_connector_destination)
        """

    def update_destination(
        self, **kwargs: Unpack[UpdateDestinationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update a destination specified by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_destination)
        """

    def update_event_log_configuration(
        self, **kwargs: Unpack[UpdateEventLogConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update an event log configuration by log configuration ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_event_log_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_event_log_configuration)
        """

    def update_managed_thing(
        self, **kwargs: Unpack[UpdateManagedThingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the attributes and capabilities associated with a managed thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_managed_thing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_managed_thing)
        """

    def update_notification_configuration(
        self, **kwargs: Unpack[UpdateNotificationConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update a notification configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_notification_configuration)
        """

    def update_ota_task(
        self, **kwargs: Unpack[UpdateOtaTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update an over-the-air (OTA) task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/update_ota_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#update_ota_task)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_associations"]
    ) -> ListAccountAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_connectors"]
    ) -> ListCloudConnectorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connector_destinations"]
    ) -> ListConnectorDestinationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_credential_lockers"]
    ) -> ListCredentialLockersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_destinations"]
    ) -> ListDestinationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_discoveries"]
    ) -> ListDeviceDiscoveriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_discovered_devices"]
    ) -> ListDiscoveredDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_log_configurations"]
    ) -> ListEventLogConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_thing_account_associations"]
    ) -> ListManagedThingAccountAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_thing_schemas"]
    ) -> ListManagedThingSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_things"]
    ) -> ListManagedThingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_notification_configurations"]
    ) -> ListNotificationConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ota_task_configurations"]
    ) -> ListOtaTaskConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ota_task_executions"]
    ) -> ListOtaTaskExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ota_tasks"]
    ) -> ListOtaTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_provisioning_profiles"]
    ) -> ListProvisioningProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/client/#get_paginator)
        """
