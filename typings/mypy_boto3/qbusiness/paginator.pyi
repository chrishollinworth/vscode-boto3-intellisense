"""
Type annotations for qbusiness service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_qbusiness import QBusinessClient
    from mypy_boto3_qbusiness.paginator import (
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
    )

    client: QBusinessClient = boto3.client("qbusiness")

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

from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DataSourceSyncJobStatusType
from .type_defs import (
    GetChatControlsConfigurationResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListConversationsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListDocumentsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListMessagesResponseTypeDef,
    ListPluginsResponseTypeDef,
    ListRetrieversResponseTypeDef,
    ListWebExperiencesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
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
)

class GetChatControlsConfigurationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.GetChatControlsConfiguration)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#getchatcontrolsconfigurationpaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetChatControlsConfigurationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.GetChatControlsConfiguration.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#getchatcontrolsconfigurationpaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listapplicationspaginator)
        """

class ListConversationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListConversations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listconversationspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        userId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConversationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListConversations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listconversationspaginator)
        """

class ListDataSourceSyncJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSourceSyncJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcesyncjobspaginator)
    """

    def paginate(
        self,
        *,
        dataSourceId: str,
        applicationId: str,
        indexId: str,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        statusFilter: DataSourceSyncJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourceSyncJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSourceSyncJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcesyncjobspaginator)
        """

class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcespaginator)
    """

    def paginate(
        self, *, applicationId: str, indexId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcespaginator)
        """

class ListDocumentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDocuments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdocumentspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListDocuments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdocumentspaginator)
        """

class ListGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listgroupspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        indexId: str,
        updatedEarlierThan: Union[datetime, str],
        dataSourceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listgroupspaginator)
        """

class ListIndicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListIndices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listindicespaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListIndices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listindicespaginator)
        """

class ListMessagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListMessages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listmessagespaginator)
    """

    def paginate(
        self,
        *,
        conversationId: str,
        applicationId: str,
        userId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListMessages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listmessagespaginator)
        """

class ListPluginsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListPlugins)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listpluginspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPluginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListPlugins.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listpluginspaginator)
        """

class ListRetrieversPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListRetrievers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listretrieverspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRetrieversResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListRetrievers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listretrieverspaginator)
        """

class ListWebExperiencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListWebExperiences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listwebexperiencespaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWebExperiencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qbusiness.html#QBusiness.Paginator.ListWebExperiences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listwebexperiencespaginator)
        """
