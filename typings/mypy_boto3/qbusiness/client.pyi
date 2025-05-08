"""
Type annotations for qbusiness service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qbusiness.client import QBusinessClient

    session = Session()
    client: QBusinessClient = session.client("qbusiness")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetChatControlsConfigurationPaginator,
    ListApplicationsPaginator,
    ListAttachmentsPaginator,
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
from .type_defs import (
    AssociatePermissionRequestTypeDef,
    AssociatePermissionResponseTypeDef,
    BatchDeleteDocumentRequestTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchPutDocumentRequestTypeDef,
    BatchPutDocumentResponseTypeDef,
    CancelSubscriptionRequestTypeDef,
    CancelSubscriptionResponseTypeDef,
    ChatInputTypeDef,
    ChatOutputTypeDef,
    ChatSyncInputTypeDef,
    ChatSyncOutputTypeDef,
    CheckDocumentAccessRequestTypeDef,
    CheckDocumentAccessResponseTypeDef,
    CreateAnonymousWebExperienceUrlRequestTypeDef,
    CreateAnonymousWebExperienceUrlResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataAccessorRequestTypeDef,
    CreateDataAccessorResponseTypeDef,
    CreateDataSourceRequestTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateIndexRequestTypeDef,
    CreateIndexResponseTypeDef,
    CreatePluginRequestTypeDef,
    CreatePluginResponseTypeDef,
    CreateRetrieverRequestTypeDef,
    CreateRetrieverResponseTypeDef,
    CreateSubscriptionRequestTypeDef,
    CreateSubscriptionResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateWebExperienceRequestTypeDef,
    CreateWebExperienceResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteAttachmentRequestTypeDef,
    DeleteChatControlsConfigurationRequestTypeDef,
    DeleteConversationRequestTypeDef,
    DeleteDataAccessorRequestTypeDef,
    DeleteDataSourceRequestTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteIndexRequestTypeDef,
    DeletePluginRequestTypeDef,
    DeleteRetrieverRequestTypeDef,
    DeleteUserRequestTypeDef,
    DeleteWebExperienceRequestTypeDef,
    DisassociatePermissionRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetChatControlsConfigurationRequestTypeDef,
    GetChatControlsConfigurationResponseTypeDef,
    GetDataAccessorRequestTypeDef,
    GetDataAccessorResponseTypeDef,
    GetDataSourceRequestTypeDef,
    GetDataSourceResponseTypeDef,
    GetGroupRequestTypeDef,
    GetGroupResponseTypeDef,
    GetIndexRequestTypeDef,
    GetIndexResponseTypeDef,
    GetMediaRequestTypeDef,
    GetMediaResponseTypeDef,
    GetPluginRequestTypeDef,
    GetPluginResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    GetRetrieverRequestTypeDef,
    GetRetrieverResponseTypeDef,
    GetUserRequestTypeDef,
    GetUserResponseTypeDef,
    GetWebExperienceRequestTypeDef,
    GetWebExperienceResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListAttachmentsRequestTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConversationsRequestTypeDef,
    ListConversationsResponseTypeDef,
    ListDataAccessorsRequestTypeDef,
    ListDataAccessorsResponseTypeDef,
    ListDataSourcesRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsRequestTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListDocumentsRequestTypeDef,
    ListDocumentsResponseTypeDef,
    ListGroupsRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListIndicesRequestTypeDef,
    ListIndicesResponseTypeDef,
    ListMessagesRequestTypeDef,
    ListMessagesResponseTypeDef,
    ListPluginActionsRequestTypeDef,
    ListPluginActionsResponseTypeDef,
    ListPluginsRequestTypeDef,
    ListPluginsResponseTypeDef,
    ListPluginTypeActionsRequestTypeDef,
    ListPluginTypeActionsResponseTypeDef,
    ListPluginTypeMetadataRequestTypeDef,
    ListPluginTypeMetadataResponseTypeDef,
    ListRetrieversRequestTypeDef,
    ListRetrieversResponseTypeDef,
    ListSubscriptionsRequestTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebExperiencesRequestTypeDef,
    ListWebExperiencesResponseTypeDef,
    PutFeedbackRequestTypeDef,
    PutGroupRequestTypeDef,
    SearchRelevantContentRequestTypeDef,
    SearchRelevantContentResponseTypeDef,
    StartDataSourceSyncJobRequestTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    StopDataSourceSyncJobRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateChatControlsConfigurationRequestTypeDef,
    UpdateDataAccessorRequestTypeDef,
    UpdateDataSourceRequestTypeDef,
    UpdateIndexRequestTypeDef,
    UpdatePluginRequestTypeDef,
    UpdateRetrieverRequestTypeDef,
    UpdateSubscriptionRequestTypeDef,
    UpdateSubscriptionResponseTypeDef,
    UpdateUserRequestTypeDef,
    UpdateUserResponseTypeDef,
    UpdateWebExperienceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("QBusinessClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ExternalResourceException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LicenseNotFoundException: Type[BotocoreClientError]
    MediaTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QBusinessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QBusinessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#generate_presigned_url)
        """

    def associate_permission(
        self, **kwargs: Unpack[AssociatePermissionRequestTypeDef]
    ) -> AssociatePermissionResponseTypeDef:
        """
        Adds or updates a permission policy for a Amazon Q Business application,
        allowing cross-account access for an ISV.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/associate_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#associate_permission)
        """

    def batch_delete_document(
        self, **kwargs: Unpack[BatchDeleteDocumentRequestTypeDef]
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        Asynchronously deletes one or more documents added using the
        <code>BatchPutDocument</code> API from an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/batch_delete_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#batch_delete_document)
        """

    def batch_put_document(
        self, **kwargs: Unpack[BatchPutDocumentRequestTypeDef]
    ) -> BatchPutDocumentResponseTypeDef:
        """
        Adds one or more documents to an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/batch_put_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#batch_put_document)
        """

    def cancel_subscription(
        self, **kwargs: Unpack[CancelSubscriptionRequestTypeDef]
    ) -> CancelSubscriptionResponseTypeDef:
        """
        Unsubscribes a user or a group from their pricing tier in an Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/cancel_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#cancel_subscription)
        """

    def chat(self, **kwargs: Unpack[ChatInputTypeDef]) -> ChatOutputTypeDef:
        """
        Starts or continues a streaming Amazon Q Business conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/chat.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#chat)
        """

    def chat_sync(self, **kwargs: Unpack[ChatSyncInputTypeDef]) -> ChatSyncOutputTypeDef:
        """
        Starts or continues a non-streaming Amazon Q Business conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/chat_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#chat_sync)
        """

    def check_document_access(
        self, **kwargs: Unpack[CheckDocumentAccessRequestTypeDef]
    ) -> CheckDocumentAccessResponseTypeDef:
        """
        Verifies if a user has access permissions for a specified document and returns
        the actual ACL attached to the document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/check_document_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#check_document_access)
        """

    def create_anonymous_web_experience_url(
        self, **kwargs: Unpack[CreateAnonymousWebExperienceUrlRequestTypeDef]
    ) -> CreateAnonymousWebExperienceUrlResponseTypeDef:
        """
        Creates a unique URL for anonymous Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_anonymous_web_experience_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_anonymous_web_experience_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_application)
        """

    def create_data_accessor(
        self, **kwargs: Unpack[CreateDataAccessorRequestTypeDef]
    ) -> CreateDataAccessorResponseTypeDef:
        """
        Creates a new data accessor for an ISV to access data from a Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_data_accessor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_data_accessor)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceRequestTypeDef]
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source connector for an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_data_source)
        """

    def create_index(
        self, **kwargs: Unpack[CreateIndexRequestTypeDef]
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_index)
        """

    def create_plugin(
        self, **kwargs: Unpack[CreatePluginRequestTypeDef]
    ) -> CreatePluginResponseTypeDef:
        """
        Creates an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_plugin)
        """

    def create_retriever(
        self, **kwargs: Unpack[CreateRetrieverRequestTypeDef]
    ) -> CreateRetrieverResponseTypeDef:
        """
        Adds a retriever to your Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_retriever.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_retriever)
        """

    def create_subscription(
        self, **kwargs: Unpack[CreateSubscriptionRequestTypeDef]
    ) -> CreateSubscriptionResponseTypeDef:
        """
        Subscribes an IAM Identity Center user or a group to a pricing tier for an
        Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_subscription)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a universally unique identifier (UUID) mapped to a list of local user
        ids within an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_user)
        """

    def create_web_experience(
        self, **kwargs: Unpack[CreateWebExperienceRequestTypeDef]
    ) -> CreateWebExperienceResponseTypeDef:
        """
        Creates an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/create_web_experience.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#create_web_experience)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_application)
        """

    def delete_attachment(self, **kwargs: Unpack[DeleteAttachmentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an attachment associated with a specific Amazon Q Business conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_attachment)
        """

    def delete_chat_controls_configuration(
        self, **kwargs: Unpack[DeleteChatControlsConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes chat controls configured for an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_chat_controls_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_chat_controls_configuration)
        """

    def delete_conversation(
        self, **kwargs: Unpack[DeleteConversationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business web experience conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_conversation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_conversation)
        """

    def delete_data_accessor(
        self, **kwargs: Unpack[DeleteDataAccessorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified data accessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_data_accessor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_data_accessor)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_data_source)
        """

    def delete_group(self, **kwargs: Unpack[DeleteGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a group so that all users and sub groups that belong to the group can
        no longer access documents only available to that group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_group)
        """

    def delete_index(self, **kwargs: Unpack[DeleteIndexRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_index)
        """

    def delete_plugin(self, **kwargs: Unpack[DeletePluginRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_plugin)
        """

    def delete_retriever(self, **kwargs: Unpack[DeleteRetrieverRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the retriever used by an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_retriever.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_retriever)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a user by email id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_user)
        """

    def delete_web_experience(
        self, **kwargs: Unpack[DeleteWebExperienceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/delete_web_experience.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#delete_web_experience)
        """

    def disassociate_permission(
        self, **kwargs: Unpack[DisassociatePermissionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a permission policy from a Amazon Q Business application, revoking the
        cross-account access that was previously granted to an ISV.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/disassociate_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#disassociate_permission)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_application)
        """

    def get_chat_controls_configuration(
        self, **kwargs: Unpack[GetChatControlsConfigurationRequestTypeDef]
    ) -> GetChatControlsConfigurationResponseTypeDef:
        """
        Gets information about chat controls configured for an existing Amazon Q
        Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_chat_controls_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_chat_controls_configuration)
        """

    def get_data_accessor(
        self, **kwargs: Unpack[GetDataAccessorRequestTypeDef]
    ) -> GetDataAccessorResponseTypeDef:
        """
        Retrieves information about a specified data accessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_data_accessor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_data_accessor)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceRequestTypeDef]
    ) -> GetDataSourceResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_data_source)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Describes a group by group name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_group)
        """

    def get_index(self, **kwargs: Unpack[GetIndexRequestTypeDef]) -> GetIndexResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_index)
        """

    def get_media(self, **kwargs: Unpack[GetMediaRequestTypeDef]) -> GetMediaResponseTypeDef:
        """
        Returns the image bytes corresponding to a media object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_media.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_media)
        """

    def get_plugin(self, **kwargs: Unpack[GetPluginRequestTypeDef]) -> GetPluginResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_plugin)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Retrieves the current permission policy for a Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_policy)
        """

    def get_retriever(
        self, **kwargs: Unpack[GetRetrieverRequestTypeDef]
    ) -> GetRetrieverResponseTypeDef:
        """
        Gets information about an existing retriever used by an Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_retriever.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_retriever)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Describes the universally unique identifier (UUID) associated with a local user
        in a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_user)
        """

    def get_web_experience(
        self, **kwargs: Unpack[GetWebExperienceRequestTypeDef]
    ) -> GetWebExperienceResponseTypeDef:
        """
        Gets information about an existing Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_web_experience.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_web_experience)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists Amazon Q Business applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_applications)
        """

    def list_attachments(
        self, **kwargs: Unpack[ListAttachmentsRequestTypeDef]
    ) -> ListAttachmentsResponseTypeDef:
        """
        Gets a list of attachments associated with an Amazon Q Business web experience
        or a list of attachements associated with a specific Amazon Q Business
        conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_attachments)
        """

    def list_conversations(
        self, **kwargs: Unpack[ListConversationsRequestTypeDef]
    ) -> ListConversationsResponseTypeDef:
        """
        Lists one or more Amazon Q Business conversations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_conversations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_conversations)
        """

    def list_data_accessors(
        self, **kwargs: Unpack[ListDataAccessorsRequestTypeDef]
    ) -> ListDataAccessorsResponseTypeDef:
        """
        Lists the data accessors for a Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_data_accessors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_data_accessors)
        """

    def list_data_source_sync_jobs(
        self, **kwargs: Unpack[ListDataSourceSyncJobsRequestTypeDef]
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        Get information about an Amazon Q Business data source connector
        synchronization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_data_source_sync_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_data_source_sync_jobs)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the Amazon Q Business data source connectors that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_data_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_data_sources)
        """

    def list_documents(
        self, **kwargs: Unpack[ListDocumentsRequestTypeDef]
    ) -> ListDocumentsResponseTypeDef:
        """
        A list of documents attached to an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_documents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_documents)
        """

    def list_groups(self, **kwargs: Unpack[ListGroupsRequestTypeDef]) -> ListGroupsResponseTypeDef:
        """
        Provides a list of groups that are mapped to users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_groups)
        """

    def list_indices(
        self, **kwargs: Unpack[ListIndicesRequestTypeDef]
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the Amazon Q Business indices you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_indices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_indices)
        """

    def list_messages(
        self, **kwargs: Unpack[ListMessagesRequestTypeDef]
    ) -> ListMessagesResponseTypeDef:
        """
        Gets a list of messages associated with an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_messages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_messages)
        """

    def list_plugin_actions(
        self, **kwargs: Unpack[ListPluginActionsRequestTypeDef]
    ) -> ListPluginActionsResponseTypeDef:
        """
        Lists configured Amazon Q Business actions for a specific plugin in an Amazon Q
        Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_plugin_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_plugin_actions)
        """

    def list_plugin_type_actions(
        self, **kwargs: Unpack[ListPluginTypeActionsRequestTypeDef]
    ) -> ListPluginTypeActionsResponseTypeDef:
        """
        Lists configured Amazon Q Business actions for any plugin type—both built-in
        and custom.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_plugin_type_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_plugin_type_actions)
        """

    def list_plugin_type_metadata(
        self, **kwargs: Unpack[ListPluginTypeMetadataRequestTypeDef]
    ) -> ListPluginTypeMetadataResponseTypeDef:
        """
        Lists metadata for all Amazon Q Business plugin types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_plugin_type_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_plugin_type_metadata)
        """

    def list_plugins(
        self, **kwargs: Unpack[ListPluginsRequestTypeDef]
    ) -> ListPluginsResponseTypeDef:
        """
        Lists configured Amazon Q Business plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_plugins.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_plugins)
        """

    def list_retrievers(
        self, **kwargs: Unpack[ListRetrieversRequestTypeDef]
    ) -> ListRetrieversResponseTypeDef:
        """
        Lists the retriever used by an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_retrievers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_retrievers)
        """

    def list_subscriptions(
        self, **kwargs: Unpack[ListSubscriptionsRequestTypeDef]
    ) -> ListSubscriptionsResponseTypeDef:
        """
        Lists all subscriptions created in an Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_subscriptions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_tags_for_resource)
        """

    def list_web_experiences(
        self, **kwargs: Unpack[ListWebExperiencesRequestTypeDef]
    ) -> ListWebExperiencesResponseTypeDef:
        """
        Lists one or more Amazon Q Business Web Experiences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/list_web_experiences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#list_web_experiences)
        """

    def put_feedback(
        self, **kwargs: Unpack[PutFeedbackRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables your end user to provide feedback on their Amazon Q Business generated
        chat responses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/put_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#put_feedback)
        """

    def put_group(self, **kwargs: Unpack[PutGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Create, or updates, a mapping of users—who have access to a document—to groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/put_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#put_group)
        """

    def search_relevant_content(
        self, **kwargs: Unpack[SearchRelevantContentRequestTypeDef]
    ) -> SearchRelevantContentResponseTypeDef:
        """
        Searches for relevant content in a Amazon Q Business application based on a
        query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/search_relevant_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#search_relevant_content)
        """

    def start_data_source_sync_job(
        self, **kwargs: Unpack[StartDataSourceSyncJobRequestTypeDef]
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        Starts a data source connector synchronization job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/start_data_source_sync_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#start_data_source_sync_job)
        """

    def stop_data_source_sync_job(
        self, **kwargs: Unpack[StopDataSourceSyncJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an Amazon Q Business data source connector synchronization job already in
        progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/stop_data_source_sync_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#stop_data_source_sync_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tag to the specified Amazon Q Business application or data
        source resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from an Amazon Q Business application or a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_application)
        """

    def update_chat_controls_configuration(
        self, **kwargs: Unpack[UpdateChatControlsConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a set of chat controls configured for an existing Amazon Q Business
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_chat_controls_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_chat_controls_configuration)
        """

    def update_data_accessor(
        self, **kwargs: Unpack[UpdateDataAccessorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing data accessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_data_accessor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_data_accessor)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q Business data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_data_source)
        """

    def update_index(self, **kwargs: Unpack[UpdateIndexRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_index)
        """

    def update_plugin(self, **kwargs: Unpack[UpdatePluginRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_plugin)
        """

    def update_retriever(self, **kwargs: Unpack[UpdateRetrieverRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the retriever used for your Amazon Q Business application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_retriever.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_retriever)
        """

    def update_subscription(
        self, **kwargs: Unpack[UpdateSubscriptionRequestTypeDef]
    ) -> UpdateSubscriptionResponseTypeDef:
        """
        Updates the pricing tier for an Amazon Q Business subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_subscription)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> UpdateUserResponseTypeDef:
        """
        Updates a information associated with a user id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_user)
        """

    def update_web_experience(
        self, **kwargs: Unpack[UpdateWebExperienceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q Business web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/update_web_experience.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#update_web_experience)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_chat_controls_configuration"]
    ) -> GetChatControlsConfigurationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attachments"]
    ) -> ListAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_conversations"]
    ) -> ListConversationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_accessors"]
    ) -> ListDataAccessorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_source_sync_jobs"]
    ) -> ListDataSourceSyncJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_documents"]
    ) -> ListDocumentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_indices"]
    ) -> ListIndicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_messages"]
    ) -> ListMessagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plugin_actions"]
    ) -> ListPluginActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plugin_type_actions"]
    ) -> ListPluginTypeActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plugin_type_metadata"]
    ) -> ListPluginTypeMetadataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plugins"]
    ) -> ListPluginsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_retrievers"]
    ) -> ListRetrieversPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_web_experiences"]
    ) -> ListWebExperiencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_relevant_content"]
    ) -> SearchRelevantContentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/client/#get_paginator)
        """
