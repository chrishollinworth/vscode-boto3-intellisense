"""
Main interface for kafkaconnect service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kafkaconnect import (
        Client,
        KafkaConnectClient,
        ListConnectorsPaginator,
        ListCustomPluginsPaginator,
        ListWorkerConfigurationsPaginator,
    )

    session = boto3.Session()

    client: KafkaConnectClient = boto3.client("kafkaconnect")
    session_client: KafkaConnectClient = session.client("kafkaconnect")

    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_custom_plugins_paginator: ListCustomPluginsPaginator = client.get_paginator("list_custom_plugins")
    list_worker_configurations_paginator: ListWorkerConfigurationsPaginator = client.get_paginator("list_worker_configurations")
    ```
"""
from .client import KafkaConnectClient
from .paginator import (
    ListConnectorsPaginator,
    ListCustomPluginsPaginator,
    ListWorkerConfigurationsPaginator,
)

Client = KafkaConnectClient

__all__ = (
    "Client",
    "KafkaConnectClient",
    "ListConnectorsPaginator",
    "ListCustomPluginsPaginator",
    "ListWorkerConfigurationsPaginator",
)
