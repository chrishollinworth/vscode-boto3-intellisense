"""
Type annotations for qbusiness service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_qbusiness.client import QBusinessClient
    from mypy_boto3_qbusiness.paginator import (
        GetChatControlsConfigurationPaginator,
        ListApplicationsPaginator,
        ListAttachmentsPaginator,
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
        SearchRelevantContentPaginator,
    )

    session = Session()
    client: QBusinessClient = session.client("qbusiness")

    get_chat_controls_configuration_paginator: GetChatControlsConfigurationPaginator = client.get_paginator("get_chat_controls_configuration")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_attachments_paginator: ListAttachmentsPaginator = client.get_paginator("list_attachments")
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetChatControlsConfigurationRequestPaginateTypeDef,
    GetChatControlsConfigurationResponseTypeDef,
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListAttachmentsRequestPaginateTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConversationsRequestPaginateTypeDef,
    ListConversationsResponseTypeDef,
    ListDataAccessorsRequestPaginateTypeDef,
    ListDataAccessorsResponseTypeDef,
    ListDataSourcesRequestPaginateTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsRequestPaginateTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListDocumentsRequestPaginateTypeDef,
    ListDocumentsResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListIndicesRequestPaginateTypeDef,
    ListIndicesResponseTypeDef,
    ListMessagesRequestPaginateTypeDef,
    ListMessagesResponseTypeDef,
    ListPluginActionsRequestPaginateTypeDef,
    ListPluginActionsResponseTypeDef,
    ListPluginsRequestPaginateTypeDef,
    ListPluginsResponseTypeDef,
    ListPluginTypeActionsRequestPaginateTypeDef,
    ListPluginTypeActionsResponseTypeDef,
    ListPluginTypeMetadataRequestPaginateTypeDef,
    ListPluginTypeMetadataResponseTypeDef,
    ListRetrieversRequestPaginateTypeDef,
    ListRetrieversResponseTypeDef,
    ListSubscriptionsRequestPaginateTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListWebExperiencesRequestPaginateTypeDef,
    ListWebExperiencesResponseTypeDef,
    SearchRelevantContentRequestPaginateTypeDef,
    SearchRelevantContentResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetChatControlsConfigurationPaginator",
    "ListApplicationsPaginator",
    "ListAttachmentsPaginator",
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
    "SearchRelevantContentPaginator",
)

if TYPE_CHECKING:
    _GetChatControlsConfigurationPaginatorBase = Paginator[
        GetChatControlsConfigurationResponseTypeDef
    ]
else:
    _GetChatControlsConfigurationPaginatorBase = Paginator  # type: ignore[assignment]

class GetChatControlsConfigurationPaginator(_GetChatControlsConfigurationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/GetChatControlsConfiguration.html#QBusiness.Paginator.GetChatControlsConfiguration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#getchatcontrolsconfigurationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetChatControlsConfigurationRequestPaginateTypeDef]
    ) -> PageIterator[GetChatControlsConfigurationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/GetChatControlsConfiguration.html#QBusiness.Paginator.GetChatControlsConfiguration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#getchatcontrolsconfigurationpaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListApplications.html#QBusiness.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListApplications.html#QBusiness.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListAttachmentsPaginatorBase = Paginator[ListAttachmentsResponseTypeDef]
else:
    _ListAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttachmentsPaginator(_ListAttachmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListAttachments.html#QBusiness.Paginator.ListAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAttachmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListAttachments.html#QBusiness.Paginator.ListAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listattachmentspaginator)
        """

if TYPE_CHECKING:
    _ListConversationsPaginatorBase = Paginator[ListConversationsResponseTypeDef]
else:
    _ListConversationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConversationsPaginator(_ListConversationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListConversations.html#QBusiness.Paginator.ListConversations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listconversationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConversationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConversationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListConversations.html#QBusiness.Paginator.ListConversations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listconversationspaginator)
        """

if TYPE_CHECKING:
    _ListDataAccessorsPaginatorBase = Paginator[ListDataAccessorsResponseTypeDef]
else:
    _ListDataAccessorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataAccessorsPaginator(_ListDataAccessorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataAccessors.html#QBusiness.Paginator.ListDataAccessors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdataaccessorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataAccessorsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataAccessorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataAccessors.html#QBusiness.Paginator.ListDataAccessors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdataaccessorspaginator)
        """

if TYPE_CHECKING:
    _ListDataSourceSyncJobsPaginatorBase = Paginator[ListDataSourceSyncJobsResponseTypeDef]
else:
    _ListDataSourceSyncJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourceSyncJobsPaginator(_ListDataSourceSyncJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataSourceSyncJobs.html#QBusiness.Paginator.ListDataSourceSyncJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdatasourcesyncjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourceSyncJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSourceSyncJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataSourceSyncJobs.html#QBusiness.Paginator.ListDataSourceSyncJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdatasourcesyncjobspaginator)
        """

if TYPE_CHECKING:
    _ListDataSourcesPaginatorBase = Paginator[ListDataSourcesResponseTypeDef]
else:
    _ListDataSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourcesPaginator(_ListDataSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataSources.html#QBusiness.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdatasourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDataSources.html#QBusiness.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdatasourcespaginator)
        """

if TYPE_CHECKING:
    _ListDocumentsPaginatorBase = Paginator[ListDocumentsResponseTypeDef]
else:
    _ListDocumentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDocumentsPaginator(_ListDocumentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDocuments.html#QBusiness.Paginator.ListDocuments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdocumentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDocumentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDocumentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListDocuments.html#QBusiness.Paginator.ListDocuments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listdocumentspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListGroups.html#QBusiness.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListGroups.html#QBusiness.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListIndicesPaginatorBase = Paginator[ListIndicesResponseTypeDef]
else:
    _ListIndicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIndicesPaginator(_ListIndicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListIndices.html#QBusiness.Paginator.ListIndices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listindicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIndicesRequestPaginateTypeDef]
    ) -> PageIterator[ListIndicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListIndices.html#QBusiness.Paginator.ListIndices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listindicespaginator)
        """

if TYPE_CHECKING:
    _ListMessagesPaginatorBase = Paginator[ListMessagesResponseTypeDef]
else:
    _ListMessagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMessagesPaginator(_ListMessagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListMessages.html#QBusiness.Paginator.ListMessages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listmessagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMessagesRequestPaginateTypeDef]
    ) -> PageIterator[ListMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListMessages.html#QBusiness.Paginator.ListMessages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listmessagespaginator)
        """

if TYPE_CHECKING:
    _ListPluginActionsPaginatorBase = Paginator[ListPluginActionsResponseTypeDef]
else:
    _ListPluginActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPluginActionsPaginator(_ListPluginActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginActions.html#QBusiness.Paginator.ListPluginActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listpluginactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPluginActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPluginActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginActions.html#QBusiness.Paginator.ListPluginActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listpluginactionspaginator)
        """

if TYPE_CHECKING:
    _ListPluginTypeActionsPaginatorBase = Paginator[ListPluginTypeActionsResponseTypeDef]
else:
    _ListPluginTypeActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPluginTypeActionsPaginator(_ListPluginTypeActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginTypeActions.html#QBusiness.Paginator.ListPluginTypeActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listplugintypeactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPluginTypeActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPluginTypeActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginTypeActions.html#QBusiness.Paginator.ListPluginTypeActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listplugintypeactionspaginator)
        """

if TYPE_CHECKING:
    _ListPluginTypeMetadataPaginatorBase = Paginator[ListPluginTypeMetadataResponseTypeDef]
else:
    _ListPluginTypeMetadataPaginatorBase = Paginator  # type: ignore[assignment]

class ListPluginTypeMetadataPaginator(_ListPluginTypeMetadataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginTypeMetadata.html#QBusiness.Paginator.ListPluginTypeMetadata)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listplugintypemetadatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPluginTypeMetadataRequestPaginateTypeDef]
    ) -> PageIterator[ListPluginTypeMetadataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPluginTypeMetadata.html#QBusiness.Paginator.ListPluginTypeMetadata.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listplugintypemetadatapaginator)
        """

if TYPE_CHECKING:
    _ListPluginsPaginatorBase = Paginator[ListPluginsResponseTypeDef]
else:
    _ListPluginsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPluginsPaginator(_ListPluginsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPlugins.html#QBusiness.Paginator.ListPlugins)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listpluginspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPluginsRequestPaginateTypeDef]
    ) -> PageIterator[ListPluginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListPlugins.html#QBusiness.Paginator.ListPlugins.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listpluginspaginator)
        """

if TYPE_CHECKING:
    _ListRetrieversPaginatorBase = Paginator[ListRetrieversResponseTypeDef]
else:
    _ListRetrieversPaginatorBase = Paginator  # type: ignore[assignment]

class ListRetrieversPaginator(_ListRetrieversPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListRetrievers.html#QBusiness.Paginator.ListRetrievers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listretrieverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRetrieversRequestPaginateTypeDef]
    ) -> PageIterator[ListRetrieversResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListRetrievers.html#QBusiness.Paginator.ListRetrievers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listretrieverspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionsPaginatorBase = Paginator[ListSubscriptionsResponseTypeDef]
else:
    _ListSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionsPaginator(_ListSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListSubscriptions.html#QBusiness.Paginator.ListSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListSubscriptions.html#QBusiness.Paginator.ListSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListWebExperiencesPaginatorBase = Paginator[ListWebExperiencesResponseTypeDef]
else:
    _ListWebExperiencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWebExperiencesPaginator(_ListWebExperiencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListWebExperiences.html#QBusiness.Paginator.ListWebExperiences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listwebexperiencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWebExperiencesRequestPaginateTypeDef]
    ) -> PageIterator[ListWebExperiencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/ListWebExperiences.html#QBusiness.Paginator.ListWebExperiences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#listwebexperiencespaginator)
        """

if TYPE_CHECKING:
    _SearchRelevantContentPaginatorBase = Paginator[SearchRelevantContentResponseTypeDef]
else:
    _SearchRelevantContentPaginatorBase = Paginator  # type: ignore[assignment]

class SearchRelevantContentPaginator(_SearchRelevantContentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/SearchRelevantContent.html#QBusiness.Paginator.SearchRelevantContent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#searchrelevantcontentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchRelevantContentRequestPaginateTypeDef]
    ) -> PageIterator[SearchRelevantContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/paginator/SearchRelevantContent.html#QBusiness.Paginator.SearchRelevantContent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators/#searchrelevantcontentpaginator)
        """
