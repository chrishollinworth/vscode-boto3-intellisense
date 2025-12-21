"""
Main interface for qbusiness service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qbusiness import (
        Client,
        GetChatControlsConfigurationPaginator,
        ListApplicationsPaginator,
        ListAttachmentsPaginator,
        ListChatResponseConfigurationsPaginator,
        ListConversationsPaginator,
        ListDataAccessorsPaginator,
        ListDataSourceSyncJobsPaginator,
        ListDataSourcesPaginator,
        ListDocumentsPaginator,
        ListGroupsPaginator,
        ListIndicesPaginator,
        ListMessagesPaginator,
        ListPluginActionsPaginator,
        ListPluginTypeActionsPaginator,
        ListPluginTypeMetadataPaginator,
        ListPluginsPaginator,
        ListRetrieversPaginator,
        ListSubscriptionsPaginator,
        ListWebExperiencesPaginator,
        QBusinessClient,
        SearchRelevantContentPaginator,
    )

    session = Session()
    client: QBusinessClient = session.client("qbusiness")

    get_chat_controls_configuration_paginator: GetChatControlsConfigurationPaginator = client.get_paginator("get_chat_controls_configuration")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_attachments_paginator: ListAttachmentsPaginator = client.get_paginator("list_attachments")
    list_chat_response_configurations_paginator: ListChatResponseConfigurationsPaginator = client.get_paginator("list_chat_response_configurations")
    list_conversations_paginator: ListConversationsPaginator = client.get_paginator("list_conversations")
    list_data_accessors_paginator: ListDataAccessorsPaginator = client.get_paginator("list_data_accessors")
    list_data_source_sync_jobs_paginator: ListDataSourceSyncJobsPaginator = client.get_paginator("list_data_source_sync_jobs")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_documents_paginator: ListDocumentsPaginator = client.get_paginator("list_documents")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_indices_paginator: ListIndicesPaginator = client.get_paginator("list_indices")
    list_messages_paginator: ListMessagesPaginator = client.get_paginator("list_messages")
    list_plugin_actions_paginator: ListPluginActionsPaginator = client.get_paginator("list_plugin_actions")
    list_plugin_type_actions_paginator: ListPluginTypeActionsPaginator = client.get_paginator("list_plugin_type_actions")
    list_plugin_type_metadata_paginator: ListPluginTypeMetadataPaginator = client.get_paginator("list_plugin_type_metadata")
    list_plugins_paginator: ListPluginsPaginator = client.get_paginator("list_plugins")
    list_retrievers_paginator: ListRetrieversPaginator = client.get_paginator("list_retrievers")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_web_experiences_paginator: ListWebExperiencesPaginator = client.get_paginator("list_web_experiences")
    search_relevant_content_paginator: SearchRelevantContentPaginator = client.get_paginator("search_relevant_content")
    ```
"""

from .client import QBusinessClient
from .paginator import (
    GetChatControlsConfigurationPaginator,
    ListApplicationsPaginator,
    ListAttachmentsPaginator,
    ListChatResponseConfigurationsPaginator,
    ListConversationsPaginator,
    ListDataAccessorsPaginator,
    ListDataSourcesPaginator,
    ListDataSourceSyncJobsPaginator,
    ListDocumentsPaginator,
    ListGroupsPaginator,
    ListIndicesPaginator,
    ListMessagesPaginator,
    ListPluginActionsPaginator,
    ListPluginsPaginator,
    ListPluginTypeActionsPaginator,
    ListPluginTypeMetadataPaginator,
    ListRetrieversPaginator,
    ListSubscriptionsPaginator,
    ListWebExperiencesPaginator,
    SearchRelevantContentPaginator,
)

Client = QBusinessClient

__all__ = (
    "Client",
    "GetChatControlsConfigurationPaginator",
    "ListApplicationsPaginator",
    "ListAttachmentsPaginator",
    "ListChatResponseConfigurationsPaginator",
    "ListConversationsPaginator",
    "ListDataAccessorsPaginator",
    "ListDataSourceSyncJobsPaginator",
    "ListDataSourcesPaginator",
    "ListDocumentsPaginator",
    "ListGroupsPaginator",
    "ListIndicesPaginator",
    "ListMessagesPaginator",
    "ListPluginActionsPaginator",
    "ListPluginTypeActionsPaginator",
    "ListPluginTypeMetadataPaginator",
    "ListPluginsPaginator",
    "ListRetrieversPaginator",
    "ListSubscriptionsPaginator",
    "ListWebExperiencesPaginator",
    "QBusinessClient",
    "SearchRelevantContentPaginator",
)
