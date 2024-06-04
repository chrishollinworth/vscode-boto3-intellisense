"""
Main interface for qbusiness service.

Usage::

    ```python
    import boto3
    from mypy_boto3_qbusiness import (
        Client,
        GetChatControlsConfigurationPaginator,
        ListApplicationsPaginator,
        ListConversationsPaginator,
        ListDataSourceSyncJobsPaginator,
        ListDataSourcesPaginator,
        ListDocumentsPaginator,
        ListGroupsPaginator,
        ListIndicesPaginator,
        ListMessagesPaginator,
        ListPluginsPaginator,
        ListRetrieversPaginator,
        ListWebExperiencesPaginator,
        QBusinessClient,
    )

    session = boto3.Session()

    client: QBusinessClient = boto3.client("qbusiness")
    session_client: QBusinessClient = session.client("qbusiness")

    get_chat_controls_configuration_paginator: GetChatControlsConfigurationPaginator = client.get_paginator("get_chat_controls_configuration")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_conversations_paginator: ListConversationsPaginator = client.get_paginator("list_conversations")
    list_data_source_sync_jobs_paginator: ListDataSourceSyncJobsPaginator = client.get_paginator("list_data_source_sync_jobs")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_documents_paginator: ListDocumentsPaginator = client.get_paginator("list_documents")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_indices_paginator: ListIndicesPaginator = client.get_paginator("list_indices")
    list_messages_paginator: ListMessagesPaginator = client.get_paginator("list_messages")
    list_plugins_paginator: ListPluginsPaginator = client.get_paginator("list_plugins")
    list_retrievers_paginator: ListRetrieversPaginator = client.get_paginator("list_retrievers")
    list_web_experiences_paginator: ListWebExperiencesPaginator = client.get_paginator("list_web_experiences")
    ```
"""

from .client import QBusinessClient
from .paginator import (
    GetChatControlsConfigurationPaginator,
    ListApplicationsPaginator,
    ListConversationsPaginator,
    ListDataSourcesPaginator,
    ListDataSourceSyncJobsPaginator,
    ListDocumentsPaginator,
    ListGroupsPaginator,
    ListIndicesPaginator,
    ListMessagesPaginator,
    ListPluginsPaginator,
    ListRetrieversPaginator,
    ListWebExperiencesPaginator,
)

Client = QBusinessClient

__all__ = (
    "Client",
    "GetChatControlsConfigurationPaginator",
    "ListApplicationsPaginator",
    "ListConversationsPaginator",
    "ListDataSourceSyncJobsPaginator",
    "ListDataSourcesPaginator",
    "ListDocumentsPaginator",
    "ListGroupsPaginator",
    "ListIndicesPaginator",
    "ListMessagesPaginator",
    "ListPluginsPaginator",
    "ListRetrieversPaginator",
    "ListWebExperiencesPaginator",
    "QBusinessClient",
)
