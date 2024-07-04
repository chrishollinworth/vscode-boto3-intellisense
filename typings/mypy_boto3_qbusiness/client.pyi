"""
Type annotations for qbusiness service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_qbusiness import QBusinessClient

    client: QBusinessClient = boto3.client("qbusiness")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ChatModeType,
    DataSourceSyncJobStatusType,
    IndexTypeType,
    MembershipTypeType,
    PluginStateType,
    PluginTypeType,
    ResponseScopeType,
    RetrieverTypeType,
    WebExperienceSamplePromptsControlModeType,
)
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
from .type_defs import (
    ActionExecutionTypeDef,
    AttachmentInputTypeDef,
    AttachmentsConfigurationTypeDef,
    AttributeFilterTypeDef,
    AuthChallengeResponseTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchPutDocumentResponseTypeDef,
    BlockedPhrasesConfigurationUpdateTypeDef,
    ChatModeConfigurationTypeDef,
    ChatSyncOutputTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreatePluginResponseTypeDef,
    CreateRetrieverResponseTypeDef,
    CreateWebExperienceResponseTypeDef,
    CreatorModeConfigurationTypeDef,
    CustomPluginConfigurationTypeDef,
    DataSourceVpcConfigurationTypeDef,
    DeleteDocumentTypeDef,
    DocumentAttributeConfigurationTypeDef,
    DocumentEnrichmentConfigurationTypeDef,
    DocumentTypeDef,
    EncryptionConfigurationTypeDef,
    GetApplicationResponseTypeDef,
    GetChatControlsConfigurationResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetGroupResponseTypeDef,
    GetIndexResponseTypeDef,
    GetPluginResponseTypeDef,
    GetRetrieverResponseTypeDef,
    GetUserResponseTypeDef,
    GetWebExperienceResponseTypeDef,
    GroupMembersTypeDef,
    IndexCapacityConfigurationTypeDef,
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
    ListTagsForResourceResponseTypeDef,
    ListWebExperiencesResponseTypeDef,
    MessageUsefulnessFeedbackTypeDef,
    PluginAuthConfigurationTypeDef,
    QAppsConfigurationTypeDef,
    RetrieverConfigurationTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    TagTypeDef,
    TopicConfigurationTypeDef,
    UpdateUserResponseTypeDef,
    UserAliasTypeDef,
    WebExperienceAuthConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QBusinessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LicenseNotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QBusinessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QBusinessClient exceptions.
        """

    def batch_delete_document(
        self,
        *,
        applicationId: str,
        indexId: str,
        documents: List["DeleteDocumentTypeDef"],
        dataSourceSyncId: str = None
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        Asynchronously deletes one or more documents added using the `BatchPutDocument`
        API from an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.batch_delete_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#batch_delete_document)
        """

    def batch_put_document(
        self,
        *,
        applicationId: str,
        indexId: str,
        documents: List["DocumentTypeDef"],
        roleArn: str = None,
        dataSourceSyncId: str = None
    ) -> BatchPutDocumentResponseTypeDef:
        """
        Adds one or more documents to an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.batch_put_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#batch_put_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#can_paginate)
        """

    def chat_sync(
        self,
        *,
        applicationId: str,
        userId: str = None,
        userGroups: List[str] = None,
        userMessage: str = None,
        attachments: List["AttachmentInputTypeDef"] = None,
        actionExecution: "ActionExecutionTypeDef" = None,
        authChallengeResponse: "AuthChallengeResponseTypeDef" = None,
        conversationId: str = None,
        parentMessageId: str = None,
        attributeFilter: "AttributeFilterTypeDef" = None,
        chatMode: ChatModeType = None,
        chatModeConfiguration: "ChatModeConfigurationTypeDef" = None,
        clientToken: str = None
    ) -> ChatSyncOutputTypeDef:
        """
        Starts or continues a non-streaming Amazon Q Business conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.chat_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#chat_sync)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#close)
        """

    def create_application(
        self,
        *,
        displayName: str,
        roleArn: str = None,
        identityCenterInstanceArn: str = None,
        description: str = None,
        encryptionConfiguration: "EncryptionConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        clientToken: str = None,
        attachmentsConfiguration: "AttachmentsConfigurationTypeDef" = None,
        qAppsConfiguration: "QAppsConfigurationTypeDef" = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_application)
        """

    def create_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        displayName: str,
        configuration: Dict[str, Any],
        vpcConfiguration: "DataSourceVpcConfigurationTypeDef" = None,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        syncSchedule: str = None,
        roleArn: str = None,
        clientToken: str = None,
        documentEnrichmentConfiguration: "DocumentEnrichmentConfigurationTypeDef" = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source connector for an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_data_source)
        """

    def create_index(
        self,
        *,
        applicationId: str,
        displayName: str,
        type: IndexTypeType = None,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        capacityConfiguration: "IndexCapacityConfigurationTypeDef" = None,
        clientToken: str = None
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_index)
        """

    def create_plugin(
        self,
        *,
        applicationId: str,
        displayName: str,
        type: PluginTypeType,
        authConfiguration: "PluginAuthConfigurationTypeDef",
        serverUrl: str = None,
        customPluginConfiguration: "CustomPluginConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        clientToken: str = None
    ) -> CreatePluginResponseTypeDef:
        """
        Creates an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_plugin)
        """

    def create_retriever(
        self,
        *,
        applicationId: str,
        type: RetrieverTypeType,
        displayName: str,
        configuration: "RetrieverConfigurationTypeDef",
        roleArn: str = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRetrieverResponseTypeDef:
        """
        Adds a retriever to your Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_retriever)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_retriever)
        """

    def create_user(
        self,
        *,
        applicationId: str,
        userId: str,
        userAliases: List["UserAliasTypeDef"] = None,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Creates a universally unique identifier (UUID) mapped to a list of local user
        ids within an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_user)
        """

    def create_web_experience(
        self,
        *,
        applicationId: str,
        title: str = None,
        subtitle: str = None,
        welcomeMessage: str = None,
        samplePromptsControlMode: WebExperienceSamplePromptsControlModeType = None,
        roleArn: str = None,
        tags: List["TagTypeDef"] = None,
        clientToken: str = None
    ) -> CreateWebExperienceResponseTypeDef:
        """
        Creates an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.create_web_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#create_web_experience)
        """

    def delete_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_application)
        """

    def delete_chat_controls_configuration(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes chat controls configured for an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_chat_controls_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_chat_controls_configuration)
        """

    def delete_conversation(
        self, *, conversationId: str, applicationId: str, userId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business web experience conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_conversation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_conversation)
        """

    def delete_data_source(
        self, *, applicationId: str, indexId: str, dataSourceId: str
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_data_source)
        """

    def delete_group(
        self, *, applicationId: str, indexId: str, groupName: str, dataSourceId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a group so that all users and sub groups that belong to the group can no
        longer access documents only available to that group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_group)
        """

    def delete_index(self, *, applicationId: str, indexId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_index)
        """

    def delete_plugin(self, *, applicationId: str, pluginId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_plugin)
        """

    def delete_retriever(self, *, applicationId: str, retrieverId: str) -> Dict[str, Any]:
        """
        Deletes the retriever used by an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_retriever)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_retriever)
        """

    def delete_user(self, *, applicationId: str, userId: str) -> Dict[str, Any]:
        """
        Deletes a user by email id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_user)
        """

    def delete_web_experience(self, *, applicationId: str, webExperienceId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.delete_web_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#delete_web_experience)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#generate_presigned_url)
        """

    def get_application(self, *, applicationId: str) -> GetApplicationResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_application)
        """

    def get_chat_controls_configuration(
        self, *, applicationId: str, maxResults: int = None, nextToken: str = None
    ) -> GetChatControlsConfigurationResponseTypeDef:
        """
        Gets information about an chat controls configured for an existing Amazon Q
        Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_chat_controls_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_chat_controls_configuration)
        """

    def get_data_source(
        self, *, applicationId: str, indexId: str, dataSourceId: str
    ) -> GetDataSourceResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_data_source)
        """

    def get_group(
        self, *, applicationId: str, indexId: str, groupName: str, dataSourceId: str = None
    ) -> GetGroupResponseTypeDef:
        """
        Describes a group by group name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_group)
        """

    def get_index(self, *, applicationId: str, indexId: str) -> GetIndexResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_index)
        """

    def get_plugin(self, *, applicationId: str, pluginId: str) -> GetPluginResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_plugin)
        """

    def get_retriever(self, *, applicationId: str, retrieverId: str) -> GetRetrieverResponseTypeDef:
        """
        Gets information about an existing retriever used by an Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_retriever)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_retriever)
        """

    def get_user(self, *, applicationId: str, userId: str) -> GetUserResponseTypeDef:
        """
        Describes the universally unique identifier (UUID) associated with a local user
        in a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_user)
        """

    def get_web_experience(
        self, *, applicationId: str, webExperienceId: str
    ) -> GetWebExperienceResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.get_web_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#get_web_experience)
        """

    def list_applications(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists Amazon Q Business applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_applications)
        """

    def list_conversations(
        self,
        *,
        applicationId: str,
        userId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListConversationsResponseTypeDef:
        """
        Lists one or more Amazon Q Business conversations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_conversations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_conversations)
        """

    def list_data_source_sync_jobs(
        self,
        *,
        dataSourceId: str,
        applicationId: str,
        indexId: str,
        nextToken: str = None,
        maxResults: int = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        statusFilter: DataSourceSyncJobStatusType = None
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        Get information about an Amazon Q Business data source connector
        synchronization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_data_source_sync_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_data_source_sync_jobs)
        """

    def list_data_sources(
        self, *, applicationId: str, indexId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the Amazon Q Business data source connectors that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_data_sources)
        """

    def list_documents(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListDocumentsResponseTypeDef:
        """
        A list of documents attached to an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_documents)
        """

    def list_groups(
        self,
        *,
        applicationId: str,
        indexId: str,
        updatedEarlierThan: Union[datetime, str],
        dataSourceId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        Provides a list of groups that are mapped to users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_groups)
        """

    def list_indices(
        self, *, applicationId: str, nextToken: str = None, maxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the Amazon Q Business indices you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_indices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_indices)
        """

    def list_messages(
        self,
        *,
        conversationId: str,
        applicationId: str,
        userId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListMessagesResponseTypeDef:
        """
        Gets a list of messages associated with an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_messages)
        """

    def list_plugins(
        self, *, applicationId: str, nextToken: str = None, maxResults: int = None
    ) -> ListPluginsResponseTypeDef:
        """
        Lists configured Amazon Q Business plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_plugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_plugins)
        """

    def list_retrievers(
        self, *, applicationId: str, nextToken: str = None, maxResults: int = None
    ) -> ListRetrieversResponseTypeDef:
        """
        Lists the retriever used by an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_retrievers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_retrievers)
        """

    def list_tags_for_resource(self, *, resourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_tags_for_resource)
        """

    def list_web_experiences(
        self, *, applicationId: str, nextToken: str = None, maxResults: int = None
    ) -> ListWebExperiencesResponseTypeDef:
        """
        Lists one or more Amazon Q Business Web Experiences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.list_web_experiences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#list_web_experiences)
        """

    def put_feedback(
        self,
        *,
        applicationId: str,
        conversationId: str,
        messageId: str,
        userId: str = None,
        messageCopiedAt: Union[datetime, str] = None,
        messageUsefulness: "MessageUsefulnessFeedbackTypeDef" = None
    ) -> None:
        """
        Enables your end user to provide feedback on their Amazon Q Business generated
        chat responses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#put_feedback)
        """

    def put_group(
        self,
        *,
        applicationId: str,
        indexId: str,
        groupName: str,
        type: MembershipTypeType,
        groupMembers: "GroupMembersTypeDef",
        dataSourceId: str = None
    ) -> Dict[str, Any]:
        """
        Create, or updates, a mapping of users—who have access to a document—to groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.put_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#put_group)
        """

    def start_data_source_sync_job(
        self, *, dataSourceId: str, applicationId: str, indexId: str
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        Starts a data source connector synchronization job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.start_data_source_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#start_data_source_sync_job)
        """

    def stop_data_source_sync_job(
        self, *, dataSourceId: str, applicationId: str, indexId: str
    ) -> Dict[str, Any]:
        """
        Stops an Amazon Q Business data source connector synchronization job already in
        progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.stop_data_source_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#stop_data_source_sync_job)
        """

    def tag_resource(self, *, resourceARN: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tag to the specified Amazon Q Business application or data
        source resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from an Amazon Q Business application or a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#untag_resource)
        """

    def update_application(
        self,
        *,
        applicationId: str,
        identityCenterInstanceArn: str = None,
        displayName: str = None,
        description: str = None,
        roleArn: str = None,
        attachmentsConfiguration: "AttachmentsConfigurationTypeDef" = None,
        qAppsConfiguration: "QAppsConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_application)
        """

    def update_chat_controls_configuration(
        self,
        *,
        applicationId: str,
        clientToken: str = None,
        responseScope: ResponseScopeType = None,
        blockedPhrasesConfigurationUpdate: "BlockedPhrasesConfigurationUpdateTypeDef" = None,
        topicConfigurationsToCreateOrUpdate: List["TopicConfigurationTypeDef"] = None,
        topicConfigurationsToDelete: List["TopicConfigurationTypeDef"] = None,
        creatorModeConfiguration: "CreatorModeConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an set of chat controls configured for an existing Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_chat_controls_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_chat_controls_configuration)
        """

    def update_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceId: str,
        displayName: str = None,
        configuration: Dict[str, Any] = None,
        vpcConfiguration: "DataSourceVpcConfigurationTypeDef" = None,
        description: str = None,
        syncSchedule: str = None,
        roleArn: str = None,
        documentEnrichmentConfiguration: "DocumentEnrichmentConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_data_source)
        """

    def update_index(
        self,
        *,
        applicationId: str,
        indexId: str,
        displayName: str = None,
        description: str = None,
        capacityConfiguration: "IndexCapacityConfigurationTypeDef" = None,
        documentAttributeConfigurations: List["DocumentAttributeConfigurationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_index)
        """

    def update_plugin(
        self,
        *,
        applicationId: str,
        pluginId: str,
        displayName: str = None,
        state: PluginStateType = None,
        serverUrl: str = None,
        customPluginConfiguration: "CustomPluginConfigurationTypeDef" = None,
        authConfiguration: "PluginAuthConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_plugin)
        """

    def update_retriever(
        self,
        *,
        applicationId: str,
        retrieverId: str,
        configuration: "RetrieverConfigurationTypeDef" = None,
        displayName: str = None,
        roleArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates the retriever used for your Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_retriever)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_retriever)
        """

    def update_user(
        self,
        *,
        applicationId: str,
        userId: str,
        userAliasesToUpdate: List["UserAliasTypeDef"] = None,
        userAliasesToDelete: List["UserAliasTypeDef"] = None
    ) -> UpdateUserResponseTypeDef:
        """
        Updates a information associated with a user id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_user)
        """

    def update_web_experience(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
        roleArn: str = None,
        authenticationConfiguration: "WebExperienceAuthConfigurationTypeDef" = None,
        title: str = None,
        subtitle: str = None,
        welcomeMessage: str = None,
        samplePromptsControlMode: WebExperienceSamplePromptsControlModeType = None
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Client.update_web_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client.html#update_web_experience)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_chat_controls_configuration"]
    ) -> GetChatControlsConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.GetChatControlsConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#getchatcontrolsconfigurationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listapplicationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_conversations"]
    ) -> ListConversationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListConversations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listconversationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_sync_jobs"]
    ) -> ListDataSourceSyncJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSourceSyncJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcesyncjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdatasourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_documents"]) -> ListDocumentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListDocuments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listdocumentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_indices"]) -> ListIndicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListIndices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listindicespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_messages"]) -> ListMessagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListMessages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listmessagespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_plugins"]) -> ListPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListPlugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listpluginspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_retrievers"]) -> ListRetrieversPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListRetrievers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listretrieverspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_web_experiences"]
    ) -> ListWebExperiencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/qbusiness.html#QBusiness.Paginator.ListWebExperiences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/paginators.html#listwebexperiencespaginator)
        """
