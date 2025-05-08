"""
Type annotations for greengrass service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_greengrass.client import GreengrassClient
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

    session = Session()
    client: GreengrassClient = session.client("greengrass")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBulkDeploymentDetailedReportsRequestPaginateTypeDef,
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsRequestPaginateTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionsRequestPaginateTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListConnectorDefinitionVersionsRequestPaginateTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsRequestPaginateTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsRequestPaginateTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListDeploymentsRequestPaginateTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionsRequestPaginateTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListDeviceDefinitionVersionsRequestPaginateTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsRequestPaginateTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsRequestPaginateTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListGroupVersionsRequestPaginateTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListLoggerDefinitionsRequestPaginateTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListLoggerDefinitionVersionsRequestPaginateTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsRequestPaginateTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsRequestPaginateTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsRequestPaginateTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsRequestPaginateTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListBulkDeploymentDetailedReportsPaginatorBase = Paginator[
        ListBulkDeploymentDetailedReportsResponseTypeDef
    ]
else:
    _ListBulkDeploymentDetailedReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBulkDeploymentDetailedReportsPaginator(_ListBulkDeploymentDetailedReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListBulkDeploymentDetailedReports.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listbulkdeploymentdetailedreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBulkDeploymentDetailedReportsRequestPaginateTypeDef]
    ) -> PageIterator[ListBulkDeploymentDetailedReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListBulkDeploymentDetailedReports.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listbulkdeploymentdetailedreportspaginator)
        """

if TYPE_CHECKING:
    _ListBulkDeploymentsPaginatorBase = Paginator[ListBulkDeploymentsResponseTypeDef]
else:
    _ListBulkDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBulkDeploymentsPaginator(_ListBulkDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListBulkDeployments.html#Greengrass.Paginator.ListBulkDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listbulkdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBulkDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListBulkDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListBulkDeployments.html#Greengrass.Paginator.ListBulkDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listbulkdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListConnectorDefinitionVersionsPaginatorBase = Paginator[
        ListConnectorDefinitionVersionsResponseTypeDef
    ]
else:
    _ListConnectorDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorDefinitionVersionsPaginator(_ListConnectorDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListConnectorDefinitionVersions.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listconnectordefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListConnectorDefinitionVersions.html#Greengrass.Paginator.ListConnectorDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listconnectordefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListConnectorDefinitionsPaginatorBase = Paginator[ListConnectorDefinitionsResponseTypeDef]
else:
    _ListConnectorDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorDefinitionsPaginator(_ListConnectorDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListConnectorDefinitions.html#Greengrass.Paginator.ListConnectorDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listconnectordefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListConnectorDefinitions.html#Greengrass.Paginator.ListConnectorDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listconnectordefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListCoreDefinitionVersionsPaginatorBase = Paginator[ListCoreDefinitionVersionsResponseTypeDef]
else:
    _ListCoreDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoreDefinitionVersionsPaginator(_ListCoreDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListCoreDefinitionVersions.html#Greengrass.Paginator.ListCoreDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listcoredefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoreDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCoreDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListCoreDefinitionVersions.html#Greengrass.Paginator.ListCoreDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listcoredefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListCoreDefinitionsPaginatorBase = Paginator[ListCoreDefinitionsResponseTypeDef]
else:
    _ListCoreDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoreDefinitionsPaginator(_ListCoreDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListCoreDefinitions.html#Greengrass.Paginator.ListCoreDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listcoredefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoreDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCoreDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListCoreDefinitions.html#Greengrass.Paginator.ListCoreDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listcoredefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsResponseTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeployments.html#Greengrass.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeployments.html#Greengrass.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListDeviceDefinitionVersionsPaginatorBase = Paginator[
        ListDeviceDefinitionVersionsResponseTypeDef
    ]
else:
    _ListDeviceDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceDefinitionVersionsPaginator(_ListDeviceDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeviceDefinitionVersions.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdevicedefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeviceDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeviceDefinitionVersions.html#Greengrass.Paginator.ListDeviceDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdevicedefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListDeviceDefinitionsPaginatorBase = Paginator[ListDeviceDefinitionsResponseTypeDef]
else:
    _ListDeviceDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceDefinitionsPaginator(_ListDeviceDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeviceDefinitions.html#Greengrass.Paginator.ListDeviceDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdevicedefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeviceDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListDeviceDefinitions.html#Greengrass.Paginator.ListDeviceDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listdevicedefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListFunctionDefinitionVersionsPaginatorBase = Paginator[
        ListFunctionDefinitionVersionsResponseTypeDef
    ]
else:
    _ListFunctionDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFunctionDefinitionVersionsPaginator(_ListFunctionDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListFunctionDefinitionVersions.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listfunctiondefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFunctionDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListFunctionDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListFunctionDefinitionVersions.html#Greengrass.Paginator.ListFunctionDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listfunctiondefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListFunctionDefinitionsPaginatorBase = Paginator[ListFunctionDefinitionsResponseTypeDef]
else:
    _ListFunctionDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFunctionDefinitionsPaginator(_ListFunctionDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListFunctionDefinitions.html#Greengrass.Paginator.ListFunctionDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listfunctiondefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFunctionDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListFunctionDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListFunctionDefinitions.html#Greengrass.Paginator.ListFunctionDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listfunctiondefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListGroupVersionsPaginatorBase = Paginator[ListGroupVersionsResponseTypeDef]
else:
    _ListGroupVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupVersionsPaginator(_ListGroupVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListGroupVersions.html#Greengrass.Paginator.ListGroupVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listgroupversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListGroupVersions.html#Greengrass.Paginator.ListGroupVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listgroupversionspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListGroups.html#Greengrass.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListGroups.html#Greengrass.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListLoggerDefinitionVersionsPaginatorBase = Paginator[
        ListLoggerDefinitionVersionsResponseTypeDef
    ]
else:
    _ListLoggerDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLoggerDefinitionVersionsPaginator(_ListLoggerDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListLoggerDefinitionVersions.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listloggerdefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLoggerDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLoggerDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListLoggerDefinitionVersions.html#Greengrass.Paginator.ListLoggerDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listloggerdefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListLoggerDefinitionsPaginatorBase = Paginator[ListLoggerDefinitionsResponseTypeDef]
else:
    _ListLoggerDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLoggerDefinitionsPaginator(_ListLoggerDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListLoggerDefinitions.html#Greengrass.Paginator.ListLoggerDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listloggerdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLoggerDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLoggerDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListLoggerDefinitions.html#Greengrass.Paginator.ListLoggerDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listloggerdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListResourceDefinitionVersionsPaginatorBase = Paginator[
        ListResourceDefinitionVersionsResponseTypeDef
    ]
else:
    _ListResourceDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceDefinitionVersionsPaginator(_ListResourceDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListResourceDefinitionVersions.html#Greengrass.Paginator.ListResourceDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listresourcedefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListResourceDefinitionVersions.html#Greengrass.Paginator.ListResourceDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listresourcedefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListResourceDefinitionsPaginatorBase = Paginator[ListResourceDefinitionsResponseTypeDef]
else:
    _ListResourceDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceDefinitionsPaginator(_ListResourceDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListResourceDefinitions.html#Greengrass.Paginator.ListResourceDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listresourcedefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListResourceDefinitions.html#Greengrass.Paginator.ListResourceDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listresourcedefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionDefinitionVersionsPaginatorBase = Paginator[
        ListSubscriptionDefinitionVersionsResponseTypeDef
    ]
else:
    _ListSubscriptionDefinitionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionDefinitionVersionsPaginator(_ListSubscriptionDefinitionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListSubscriptionDefinitionVersions.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listsubscriptiondefinitionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionDefinitionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionDefinitionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListSubscriptionDefinitionVersions.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listsubscriptiondefinitionversionspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionDefinitionsPaginatorBase = Paginator[
        ListSubscriptionDefinitionsResponseTypeDef
    ]
else:
    _ListSubscriptionDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionDefinitionsPaginator(_ListSubscriptionDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListSubscriptionDefinitions.html#Greengrass.Paginator.ListSubscriptionDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listsubscriptiondefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass/paginator/ListSubscriptionDefinitions.html#Greengrass.Paginator.ListSubscriptionDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators/#listsubscriptiondefinitionspaginator)
        """
