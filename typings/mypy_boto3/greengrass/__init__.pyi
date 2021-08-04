"""
Main interface for greengrass service.

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrass import (
        Client,
        GreengrassClient,
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

    session = boto3.Session()

    client: GreengrassClient = boto3.client("greengrass")
    session_client: GreengrassClient = session.client("greengrass")

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
from .client import GreengrassClient
from .paginator import (
    ListBulkDeploymentDetailedReportsPaginator,
    ListBulkDeploymentsPaginator,
    ListConnectorDefinitionsPaginator,
    ListConnectorDefinitionVersionsPaginator,
    ListCoreDefinitionsPaginator,
    ListCoreDefinitionVersionsPaginator,
    ListDeploymentsPaginator,
    ListDeviceDefinitionsPaginator,
    ListDeviceDefinitionVersionsPaginator,
    ListFunctionDefinitionsPaginator,
    ListFunctionDefinitionVersionsPaginator,
    ListGroupsPaginator,
    ListGroupVersionsPaginator,
    ListLoggerDefinitionsPaginator,
    ListLoggerDefinitionVersionsPaginator,
    ListResourceDefinitionsPaginator,
    ListResourceDefinitionVersionsPaginator,
    ListSubscriptionDefinitionsPaginator,
    ListSubscriptionDefinitionVersionsPaginator,
)

Client = GreengrassClient

__all__ = (
    "Client",
    "GreengrassClient",
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
