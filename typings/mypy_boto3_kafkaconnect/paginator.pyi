"""
Type annotations for kafkaconnect service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kafkaconnect.client import KafkaConnectClient
    from mypy_boto3_kafkaconnect.paginator import (
        ListConnectorOperationsPaginator,
        ListConnectorsPaginator,
        ListCustomPluginsPaginator,
        ListWorkerConfigurationsPaginator,
    )

    session = Session()
    client: KafkaConnectClient = session.client("kafkaconnect")

    list_connector_operations_paginator: ListConnectorOperationsPaginator = client.get_paginator("list_connector_operations")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_custom_plugins_paginator: ListCustomPluginsPaginator = client.get_paginator("list_custom_plugins")
    list_worker_configurations_paginator: ListWorkerConfigurationsPaginator = client.get_paginator("list_worker_configurations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConnectorOperationsRequestPaginateTypeDef,
    ListConnectorOperationsResponseTypeDef,
    ListConnectorsRequestPaginateTypeDef,
    ListConnectorsResponseTypeDef,
    ListCustomPluginsRequestPaginateTypeDef,
    ListCustomPluginsResponseTypeDef,
    ListWorkerConfigurationsRequestPaginateTypeDef,
    ListWorkerConfigurationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListConnectorOperationsPaginator",
    "ListConnectorsPaginator",
    "ListCustomPluginsPaginator",
    "ListWorkerConfigurationsPaginator",
)

if TYPE_CHECKING:
    _ListConnectorOperationsPaginatorBase = Paginator[ListConnectorOperationsResponseTypeDef]
else:
    _ListConnectorOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorOperationsPaginator(_ListConnectorOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListConnectorOperations.html#KafkaConnect.Paginator.ListConnectorOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listconnectoroperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListConnectorOperations.html#KafkaConnect.Paginator.ListConnectorOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listconnectoroperationspaginator)
        """

if TYPE_CHECKING:
    _ListConnectorsPaginatorBase = Paginator[ListConnectorsResponseTypeDef]
else:
    _ListConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorsPaginator(_ListConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListConnectors.html#KafkaConnect.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListConnectors.html#KafkaConnect.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listconnectorspaginator)
        """

if TYPE_CHECKING:
    _ListCustomPluginsPaginatorBase = Paginator[ListCustomPluginsResponseTypeDef]
else:
    _ListCustomPluginsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomPluginsPaginator(_ListCustomPluginsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListCustomPlugins.html#KafkaConnect.Paginator.ListCustomPlugins)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listcustompluginspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomPluginsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomPluginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListCustomPlugins.html#KafkaConnect.Paginator.ListCustomPlugins.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listcustompluginspaginator)
        """

if TYPE_CHECKING:
    _ListWorkerConfigurationsPaginatorBase = Paginator[ListWorkerConfigurationsResponseTypeDef]
else:
    _ListWorkerConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkerConfigurationsPaginator(_ListWorkerConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListWorkerConfigurations.html#KafkaConnect.Paginator.ListWorkerConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listworkerconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkerConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkerConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/paginator/ListWorkerConfigurations.html#KafkaConnect.Paginator.ListWorkerConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators/#listworkerconfigurationspaginator)
        """
