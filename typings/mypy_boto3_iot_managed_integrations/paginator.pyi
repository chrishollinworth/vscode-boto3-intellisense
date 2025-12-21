"""
Type annotations for iot-managed-integrations service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iot_managed_integrations.client import ManagedintegrationsforIoTDeviceManagementClient
    from mypy_boto3_iot_managed_integrations.paginator import (
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

    session = Session()
    client: ManagedintegrationsforIoTDeviceManagementClient = session.client("iot-managed-integrations")

    list_account_associations_paginator: ListAccountAssociationsPaginator = client.get_paginator("list_account_associations")
    list_cloud_connectors_paginator: ListCloudConnectorsPaginator = client.get_paginator("list_cloud_connectors")
    list_connector_destinations_paginator: ListConnectorDestinationsPaginator = client.get_paginator("list_connector_destinations")
    list_credential_lockers_paginator: ListCredentialLockersPaginator = client.get_paginator("list_credential_lockers")
    list_destinations_paginator: ListDestinationsPaginator = client.get_paginator("list_destinations")
    list_device_discoveries_paginator: ListDeviceDiscoveriesPaginator = client.get_paginator("list_device_discoveries")
    list_discovered_devices_paginator: ListDiscoveredDevicesPaginator = client.get_paginator("list_discovered_devices")
    list_event_log_configurations_paginator: ListEventLogConfigurationsPaginator = client.get_paginator("list_event_log_configurations")
    list_managed_thing_account_associations_paginator: ListManagedThingAccountAssociationsPaginator = client.get_paginator("list_managed_thing_account_associations")
    list_managed_thing_schemas_paginator: ListManagedThingSchemasPaginator = client.get_paginator("list_managed_thing_schemas")
    list_managed_things_paginator: ListManagedThingsPaginator = client.get_paginator("list_managed_things")
    list_notification_configurations_paginator: ListNotificationConfigurationsPaginator = client.get_paginator("list_notification_configurations")
    list_ota_task_configurations_paginator: ListOtaTaskConfigurationsPaginator = client.get_paginator("list_ota_task_configurations")
    list_ota_task_executions_paginator: ListOtaTaskExecutionsPaginator = client.get_paginator("list_ota_task_executions")
    list_ota_tasks_paginator: ListOtaTasksPaginator = client.get_paginator("list_ota_tasks")
    list_provisioning_profiles_paginator: ListProvisioningProfilesPaginator = client.get_paginator("list_provisioning_profiles")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountAssociationsRequestPaginateTypeDef,
    ListAccountAssociationsResponseTypeDef,
    ListCloudConnectorsRequestPaginateTypeDef,
    ListCloudConnectorsResponseTypeDef,
    ListConnectorDestinationsRequestPaginateTypeDef,
    ListConnectorDestinationsResponseTypeDef,
    ListCredentialLockersRequestPaginateTypeDef,
    ListCredentialLockersResponseTypeDef,
    ListDestinationsRequestPaginateTypeDef,
    ListDestinationsResponseTypeDef,
    ListDeviceDiscoveriesRequestPaginateTypeDef,
    ListDeviceDiscoveriesResponseTypeDef,
    ListDiscoveredDevicesRequestPaginateTypeDef,
    ListDiscoveredDevicesResponseTypeDef,
    ListEventLogConfigurationsRequestPaginateTypeDef,
    ListEventLogConfigurationsResponseTypeDef,
    ListManagedThingAccountAssociationsRequestPaginateTypeDef,
    ListManagedThingAccountAssociationsResponseTypeDef,
    ListManagedThingSchemasRequestPaginateTypeDef,
    ListManagedThingSchemasResponseTypeDef,
    ListManagedThingsRequestPaginateTypeDef,
    ListManagedThingsResponseTypeDef,
    ListNotificationConfigurationsRequestPaginateTypeDef,
    ListNotificationConfigurationsResponseTypeDef,
    ListOtaTaskConfigurationsRequestPaginateTypeDef,
    ListOtaTaskConfigurationsResponseTypeDef,
    ListOtaTaskExecutionsRequestPaginateTypeDef,
    ListOtaTaskExecutionsResponseTypeDef,
    ListOtaTasksRequestPaginateTypeDef,
    ListOtaTasksResponseTypeDef,
    ListProvisioningProfilesRequestPaginateTypeDef,
    ListProvisioningProfilesResponseTypeDef,
    ListSchemaVersionsRequestPaginateTypeDef,
    ListSchemaVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAccountAssociationsPaginator",
    "ListCloudConnectorsPaginator",
    "ListConnectorDestinationsPaginator",
    "ListCredentialLockersPaginator",
    "ListDestinationsPaginator",
    "ListDeviceDiscoveriesPaginator",
    "ListDiscoveredDevicesPaginator",
    "ListEventLogConfigurationsPaginator",
    "ListManagedThingAccountAssociationsPaginator",
    "ListManagedThingSchemasPaginator",
    "ListManagedThingsPaginator",
    "ListNotificationConfigurationsPaginator",
    "ListOtaTaskConfigurationsPaginator",
    "ListOtaTaskExecutionsPaginator",
    "ListOtaTasksPaginator",
    "ListProvisioningProfilesPaginator",
    "ListSchemaVersionsPaginator",
)

if TYPE_CHECKING:
    _ListAccountAssociationsPaginatorBase = Paginator[ListAccountAssociationsResponseTypeDef]
else:
    _ListAccountAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountAssociationsPaginator(_ListAccountAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListAccountAssociations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListAccountAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listaccountassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListAccountAssociations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListAccountAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listaccountassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCloudConnectorsPaginatorBase = Paginator[ListCloudConnectorsResponseTypeDef]
else:
    _ListCloudConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCloudConnectorsPaginator(_ListCloudConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListCloudConnectors.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListCloudConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listcloudconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCloudConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListCloudConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListCloudConnectors.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListCloudConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listcloudconnectorspaginator)
        """

if TYPE_CHECKING:
    _ListConnectorDestinationsPaginatorBase = Paginator[ListConnectorDestinationsResponseTypeDef]
else:
    _ListConnectorDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorDestinationsPaginator(_ListConnectorDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListConnectorDestinations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListConnectorDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listconnectordestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListConnectorDestinations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListConnectorDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listconnectordestinationspaginator)
        """

if TYPE_CHECKING:
    _ListCredentialLockersPaginatorBase = Paginator[ListCredentialLockersResponseTypeDef]
else:
    _ListCredentialLockersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCredentialLockersPaginator(_ListCredentialLockersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListCredentialLockers.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListCredentialLockers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listcredentiallockerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCredentialLockersRequestPaginateTypeDef]
    ) -> PageIterator[ListCredentialLockersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListCredentialLockers.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListCredentialLockers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listcredentiallockerspaginator)
        """

if TYPE_CHECKING:
    _ListDestinationsPaginatorBase = Paginator[ListDestinationsResponseTypeDef]
else:
    _ListDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDestinationsPaginator(_ListDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDestinations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[ListDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDestinations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdestinationspaginator)
        """

if TYPE_CHECKING:
    _ListDeviceDiscoveriesPaginatorBase = Paginator[ListDeviceDiscoveriesResponseTypeDef]
else:
    _ListDeviceDiscoveriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceDiscoveriesPaginator(_ListDeviceDiscoveriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDeviceDiscoveries.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDeviceDiscoveries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdevicediscoveriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceDiscoveriesRequestPaginateTypeDef]
    ) -> PageIterator[ListDeviceDiscoveriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDeviceDiscoveries.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDeviceDiscoveries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdevicediscoveriespaginator)
        """

if TYPE_CHECKING:
    _ListDiscoveredDevicesPaginatorBase = Paginator[ListDiscoveredDevicesResponseTypeDef]
else:
    _ListDiscoveredDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDiscoveredDevicesPaginator(_ListDiscoveredDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDiscoveredDevices.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDiscoveredDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdiscovereddevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDiscoveredDevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListDiscoveredDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListDiscoveredDevices.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListDiscoveredDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listdiscovereddevicespaginator)
        """

if TYPE_CHECKING:
    _ListEventLogConfigurationsPaginatorBase = Paginator[ListEventLogConfigurationsResponseTypeDef]
else:
    _ListEventLogConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventLogConfigurationsPaginator(_ListEventLogConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListEventLogConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListEventLogConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listeventlogconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventLogConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventLogConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListEventLogConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListEventLogConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listeventlogconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListManagedThingAccountAssociationsPaginatorBase = Paginator[
        ListManagedThingAccountAssociationsResponseTypeDef
    ]
else:
    _ListManagedThingAccountAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedThingAccountAssociationsPaginator(
    _ListManagedThingAccountAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThingAccountAssociations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThingAccountAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingaccountassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedThingAccountAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedThingAccountAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThingAccountAssociations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThingAccountAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingaccountassociationspaginator)
        """

if TYPE_CHECKING:
    _ListManagedThingSchemasPaginatorBase = Paginator[ListManagedThingSchemasResponseTypeDef]
else:
    _ListManagedThingSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedThingSchemasPaginator(_ListManagedThingSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThingSchemas.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThingSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedThingSchemasRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedThingSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThingSchemas.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThingSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingschemaspaginator)
        """

if TYPE_CHECKING:
    _ListManagedThingsPaginatorBase = Paginator[ListManagedThingsResponseTypeDef]
else:
    _ListManagedThingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedThingsPaginator(_ListManagedThingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThings.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedThingsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedThingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListManagedThings.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListManagedThings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listmanagedthingspaginator)
        """

if TYPE_CHECKING:
    _ListNotificationConfigurationsPaginatorBase = Paginator[
        ListNotificationConfigurationsResponseTypeDef
    ]
else:
    _ListNotificationConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationConfigurationsPaginator(_ListNotificationConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListNotificationConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListNotificationConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listnotificationconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListNotificationConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListNotificationConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listnotificationconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListOtaTaskConfigurationsPaginatorBase = Paginator[ListOtaTaskConfigurationsResponseTypeDef]
else:
    _ListOtaTaskConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOtaTaskConfigurationsPaginator(_ListOtaTaskConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTaskConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTaskConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOtaTaskConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListOtaTaskConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTaskConfigurations.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTaskConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListOtaTaskExecutionsPaginatorBase = Paginator[ListOtaTaskExecutionsResponseTypeDef]
else:
    _ListOtaTaskExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOtaTaskExecutionsPaginator(_ListOtaTaskExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTaskExecutions.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTaskExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOtaTaskExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListOtaTaskExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTaskExecutions.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTaskExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListOtaTasksPaginatorBase = Paginator[ListOtaTasksResponseTypeDef]
else:
    _ListOtaTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListOtaTasksPaginator(_ListOtaTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTasks.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOtaTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListOtaTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListOtaTasks.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListOtaTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listotataskspaginator)
        """

if TYPE_CHECKING:
    _ListProvisioningProfilesPaginatorBase = Paginator[ListProvisioningProfilesResponseTypeDef]
else:
    _ListProvisioningProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProvisioningProfilesPaginator(_ListProvisioningProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListProvisioningProfiles.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListProvisioningProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listprovisioningprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProvisioningProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListProvisioningProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListProvisioningProfiles.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListProvisioningProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listprovisioningprofilespaginator)
        """

if TYPE_CHECKING:
    _ListSchemaVersionsPaginatorBase = Paginator[ListSchemaVersionsResponseTypeDef]
else:
    _ListSchemaVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemaVersionsPaginator(_ListSchemaVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListSchemaVersions.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListSchemaVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listschemaversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemaVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemaVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-managed-integrations/paginator/ListSchemaVersions.html#ManagedintegrationsforIoTDeviceManagement.Paginator.ListSchemaVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/paginators/#listschemaversionspaginator)
        """
