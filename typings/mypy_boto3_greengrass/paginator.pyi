# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for greengrass service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_greengrass import GreengrassClient
    from mypy_boto3_greengrass.paginator import (
        ListBulkDeploymentDetailedReportsPaginator,
        ListBulkDeploymentsPaginator,
        ListConnectorDefinitionVersionsPaginator,
        ListConnectorDefinitionsPaginator,
        ListCoreDefinitionVersionsPaginator,
        ListCoreDefinitionsPaginator,
        ListDeploymentsPaginator,
        ListDeviceDefinitionVersionsPaginator,
        ListDeviceDefinitionsPaginator,
        ListFunctionDefinitionVersionsPaginator,
        ListFunctionDefinitionsPaginator,
        ListGroupVersionsPaginator,
        ListGroupsPaginator,
        ListLoggerDefinitionVersionsPaginator,
        ListLoggerDefinitionsPaginator,
        ListResourceDefinitionVersionsPaginator,
        ListResourceDefinitionsPaginator,
        ListSubscriptionDefinitionVersionsPaginator,
        ListSubscriptionDefinitionsPaginator,
    )

    client: GreengrassClient = boto3.client("greengrass")

    list_bulk_deployment_detailed_reports_paginator: ListBulkDeploymentDetailedReportsPaginator = client.get_paginator("list_bulk_deployment_detailed_reports")
    list_bulk_deployments_paginator: ListBulkDeploymentsPaginator = client.get_paginator("list_bulk_deployments")
    list_connector_definition_versions_paginator: ListConnectorDefinitionVersionsPaginator = client.get_paginator("list_connector_definition_versions")
    list_connector_definitions_paginator: ListConnectorDefinitionsPaginator = client.get_paginator("list_connector_definitions")
    list_core_definition_versions_paginator: ListCoreDefinitionVersionsPaginator = client.get_paginator("list_core_definition_versions")
    list_core_definitions_paginator: ListCoreDefinitionsPaginator = client.get_paginator("list_core_definitions")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_device_definition_versions_paginator: ListDeviceDefinitionVersionsPaginator = client.get_paginator("list_device_definition_versions")
    list_device_definitions_paginator: ListDeviceDefinitionsPaginator = client.get_paginator("list_device_definitions")
    list_function_definition_versions_paginator: ListFunctionDefinitionVersionsPaginator = client.get_paginator("list_function_definition_versions")
    list_function_definitions_paginator: ListFunctionDefinitionsPaginator = client.get_paginator("list_function_definitions")
    list_group_versions_paginator: ListGroupVersionsPaginator = client.get_paginator("list_group_versions")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_logger_definition_versions_paginator: ListLoggerDefinitionVersionsPaginator = client.get_paginator("list_logger_definition_versions")
    list_logger_definitions_paginator: ListLoggerDefinitionsPaginator = client.get_paginator("list_logger_definitions")
    list_resource_definition_versions_paginator: ListResourceDefinitionVersionsPaginator = client.get_paginator("list_resource_definition_versions")
    list_resource_definitions_paginator: ListResourceDefinitionsPaginator = client.get_paginator("list_resource_definitions")
    list_subscription_definition_versions_paginator: ListSubscriptionDefinitionVersionsPaginator = client.get_paginator("list_subscription_definition_versions")
    list_subscription_definitions_paginator: ListSubscriptionDefinitionsPaginator = client.get_paginator("list_subscription_definitions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_greengrass.type_defs import (
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBulkDeploymentDetailedReportsPaginator",
    "ListBulkDeploymentsPaginator",
    "ListConnectorDefinitionVersionsPaginator",
    "ListConnectorDefinitionsPaginator",
    "ListCoreDefinitionVersionsPaginator",
    "ListCoreDefinitionsPaginator",
    "ListDeploymentsPaginator",
    "ListDeviceDefinitionVersionsPaginator",
    "ListDeviceDefinitionsPaginator",
    "ListFunctionDefinitionVersionsPaginator",
    "ListFunctionDefinitionsPaginator",
    "ListGroupVersionsPaginator",
    "ListGroupsPaginator",
    "ListLoggerDefinitionVersionsPaginator",
    "ListLoggerDefinitionsPaginator",
    "ListResourceDefinitionVersionsPaginator",
    "ListResourceDefinitionsPaginator",
    "ListSubscriptionDefinitionVersionsPaginator",
    "ListSubscriptionDefinitionsPaginator",
)


class ListBulkDeploymentDetailedReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
    """

    def paginate(
        self, BulkDeploymentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBulkDeploymentDetailedReportsResponseTypeDef]:
        """
        [ListBulkDeploymentDetailedReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports.paginate)
        """


class ListBulkDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBulkDeploymentsResponseTypeDef]:
        """
        [ListBulkDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments.paginate)
        """


class ListConnectorDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
    """

    def paginate(
        self, ConnectorDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorDefinitionVersionsResponseTypeDef]:
        """
        [ListConnectorDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions.paginate)
        """


class ListConnectorDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorDefinitionsResponseTypeDef]:
        """
        [ListConnectorDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions.paginate)
        """


class ListCoreDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)
    """

    def paginate(
        self, CoreDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDefinitionVersionsResponseTypeDef]:
        """
        [ListCoreDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions.paginate)
        """


class ListCoreDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDefinitionsResponseTypeDef]:
        """
        [ListCoreDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)
    """

    def paginate(
        self, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments.paginate)
        """


class ListDeviceDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
    """

    def paginate(
        self, DeviceDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceDefinitionVersionsResponseTypeDef]:
        """
        [ListDeviceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions.paginate)
        """


class ListDeviceDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceDefinitionsResponseTypeDef]:
        """
        [ListDeviceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions.paginate)
        """


class ListFunctionDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
    """

    def paginate(
        self, FunctionDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionDefinitionVersionsResponseTypeDef]:
        """
        [ListFunctionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions.paginate)
        """


class ListFunctionDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionDefinitionsResponseTypeDef]:
        """
        [ListFunctionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions.paginate)
        """


class ListGroupVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)
    """

    def paginate(
        self, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupVersionsResponseTypeDef]:
        """
        [ListGroupVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListGroups.paginate)
        """


class ListLoggerDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
    """

    def paginate(
        self, LoggerDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLoggerDefinitionVersionsResponseTypeDef]:
        """
        [ListLoggerDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions.paginate)
        """


class ListLoggerDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLoggerDefinitionsResponseTypeDef]:
        """
        [ListLoggerDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions.paginate)
        """


class ListResourceDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)
    """

    def paginate(
        self, ResourceDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDefinitionVersionsResponseTypeDef]:
        """
        [ListResourceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions.paginate)
        """


class ListResourceDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDefinitionsResponseTypeDef]:
        """
        [ListResourceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions.paginate)
        """


class ListSubscriptionDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
    """

    def paginate(
        self, SubscriptionDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionDefinitionVersionsResponseTypeDef]:
        """
        [ListSubscriptionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions.paginate)
        """


class ListSubscriptionDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionDefinitionsResponseTypeDef]:
        """
        [ListSubscriptionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions.paginate)
        """
