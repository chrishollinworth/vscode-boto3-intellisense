"""
Type annotations for qconnect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_qconnect import QConnectClient

    client: QConnectClient = boto3.client("qconnect")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import KnowledgeBaseTypeType, TargetTypeType
from .paginator import (
    ListAssistantAssociationsPaginator,
    ListAssistantsPaginator,
    ListContentsPaginator,
    ListImportJobsPaginator,
    ListKnowledgeBasesPaginator,
    ListQuickResponsesPaginator,
    QueryAssistantPaginator,
    SearchContentPaginator,
    SearchQuickResponsesPaginator,
    SearchSessionsPaginator,
)
from .type_defs import (
    AssistantAssociationInputDataTypeDef,
    ContentFeedbackDataTypeDef,
    CreateAssistantAssociationResponseTypeDef,
    CreateAssistantResponseTypeDef,
    CreateContentResponseTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreateQuickResponseResponseTypeDef,
    CreateSessionResponseTypeDef,
    ExternalSourceConfigurationTypeDef,
    GetAssistantAssociationResponseTypeDef,
    GetAssistantResponseTypeDef,
    GetContentResponseTypeDef,
    GetContentSummaryResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetQuickResponseResponseTypeDef,
    GetRecommendationsResponseTypeDef,
    GetSessionResponseTypeDef,
    GroupingConfigurationTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotifyRecommendationsReceivedResponseTypeDef,
    PutFeedbackResponseTypeDef,
    QueryAssistantResponseTypeDef,
    QueryConditionTypeDef,
    QuickResponseDataProviderTypeDef,
    QuickResponseSearchExpressionTypeDef,
    RenderingConfigurationTypeDef,
    SearchContentResponseTypeDef,
    SearchExpressionTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsResponseTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SourceConfigurationTypeDef,
    StartContentUploadResponseTypeDef,
    StartImportJobResponseTypeDef,
    TagFilterTypeDef,
    UpdateContentResponseTypeDef,
    UpdateKnowledgeBaseTemplateUriResponseTypeDef,
    UpdateQuickResponseResponseTypeDef,
    UpdateSessionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QConnectClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#close)
        """

    def create_assistant(
        self,
        *,
        name: str,
        type: Literal["AGENT"],
        clientToken: str = None,
        description: str = None,
        serverSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateAssistantResponseTypeDef:
        """
        Creates an Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_assistant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_assistant)
        """

    def create_assistant_association(
        self,
        *,
        assistantId: str,
        association: "AssistantAssociationInputDataTypeDef",
        associationType: Literal["KNOWLEDGE_BASE"],
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssistantAssociationResponseTypeDef:
        """
        Creates an association between an Amazon Q in Connect assistant and another
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_assistant_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_assistant_association)
        """

    def create_content(
        self,
        *,
        knowledgeBaseId: str,
        name: str,
        uploadId: str,
        clientToken: str = None,
        metadata: Dict[str, str] = None,
        overrideLinkOutUri: str = None,
        tags: Dict[str, str] = None,
        title: str = None
    ) -> CreateContentResponseTypeDef:
        """
        Creates Amazon Q in Connect content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_content)
        """

    def create_knowledge_base(
        self,
        *,
        knowledgeBaseType: KnowledgeBaseTypeType,
        name: str,
        clientToken: str = None,
        description: str = None,
        renderingConfiguration: "RenderingConfigurationTypeDef" = None,
        serverSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
        sourceConfiguration: "SourceConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_knowledge_base)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_knowledge_base)
        """

    def create_quick_response(
        self,
        *,
        content: "QuickResponseDataProviderTypeDef",
        knowledgeBaseId: str,
        name: str,
        channels: List[str] = None,
        clientToken: str = None,
        contentType: str = None,
        description: str = None,
        groupingConfiguration: "GroupingConfigurationTypeDef" = None,
        isActive: bool = None,
        language: str = None,
        shortcutKey: str = None,
        tags: Dict[str, str] = None
    ) -> CreateQuickResponseResponseTypeDef:
        """
        Creates an Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_quick_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_quick_response)
        """

    def create_session(
        self,
        *,
        assistantId: str,
        name: str,
        clientToken: str = None,
        description: str = None,
        tagFilter: "TagFilterTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.create_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#create_session)
        """

    def delete_assistant(self, *, assistantId: str) -> Dict[str, Any]:
        """
        Deletes an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_assistant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_assistant)
        """

    def delete_assistant_association(
        self, *, assistantAssociationId: str, assistantId: str
    ) -> Dict[str, Any]:
        """
        Deletes an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_assistant_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_assistant_association)
        """

    def delete_content(self, *, contentId: str, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_content)
        """

    def delete_import_job(self, *, importJobId: str, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the quick response import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_import_job)
        """

    def delete_knowledge_base(self, *, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_knowledge_base)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_knowledge_base)
        """

    def delete_quick_response(
        self, *, knowledgeBaseId: str, quickResponseId: str
    ) -> Dict[str, Any]:
        """
        Deletes a quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.delete_quick_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#delete_quick_response)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#generate_presigned_url)
        """

    def get_assistant(self, *, assistantId: str) -> GetAssistantResponseTypeDef:
        """
        Retrieves information about an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_assistant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_assistant)
        """

    def get_assistant_association(
        self, *, assistantAssociationId: str, assistantId: str
    ) -> GetAssistantAssociationResponseTypeDef:
        """
        Retrieves information about an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_assistant_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_assistant_association)
        """

    def get_content(self, *, contentId: str, knowledgeBaseId: str) -> GetContentResponseTypeDef:
        """
        Retrieves content, including a pre-signed URL to download the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_content)
        """

    def get_content_summary(
        self, *, contentId: str, knowledgeBaseId: str
    ) -> GetContentSummaryResponseTypeDef:
        """
        Retrieves summary information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_content_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_content_summary)
        """

    def get_import_job(
        self, *, importJobId: str, knowledgeBaseId: str
    ) -> GetImportJobResponseTypeDef:
        """
        Retrieves the started import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_import_job)
        """

    def get_knowledge_base(self, *, knowledgeBaseId: str) -> GetKnowledgeBaseResponseTypeDef:
        """
        Retrieves information about the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_knowledge_base)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_knowledge_base)
        """

    def get_quick_response(
        self, *, knowledgeBaseId: str, quickResponseId: str
    ) -> GetQuickResponseResponseTypeDef:
        """
        Retrieves the quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_quick_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_quick_response)
        """

    def get_recommendations(
        self,
        *,
        assistantId: str,
        sessionId: str,
        maxResults: int = None,
        waitTimeSeconds: int = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_recommendations)
        """

    def get_session(self, *, assistantId: str, sessionId: str) -> GetSessionResponseTypeDef:
        """
        Retrieves information for a specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.get_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#get_session)
        """

    def list_assistant_associations(
        self, *, assistantId: str, maxResults: int = None, nextToken: str = None
    ) -> ListAssistantAssociationsResponseTypeDef:
        """
        Lists information about assistant associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_assistant_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_assistant_associations)
        """

    def list_assistants(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAssistantsResponseTypeDef:
        """
        Lists information about assistants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_assistants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_assistants)
        """

    def list_contents(
        self, *, knowledgeBaseId: str, maxResults: int = None, nextToken: str = None
    ) -> ListContentsResponseTypeDef:
        """
        Lists the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_contents)
        """

    def list_import_jobs(
        self, *, knowledgeBaseId: str, maxResults: int = None, nextToken: str = None
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists information about import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_import_jobs)
        """

    def list_knowledge_bases(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_knowledge_bases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_knowledge_bases)
        """

    def list_quick_responses(
        self, *, knowledgeBaseId: str, maxResults: int = None, nextToken: str = None
    ) -> ListQuickResponsesResponseTypeDef:
        """
        Lists information about quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_quick_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_quick_responses)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#list_tags_for_resource)
        """

    def notify_recommendations_received(
        self, *, assistantId: str, recommendationIds: List[str], sessionId: str
    ) -> NotifyRecommendationsReceivedResponseTypeDef:
        """
        Removes the specified recommendations from the specified assistant's queue of
        newly available recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.notify_recommendations_received)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#notify_recommendations_received)
        """

    def put_feedback(
        self,
        *,
        assistantId: str,
        contentFeedback: "ContentFeedbackDataTypeDef",
        targetId: str,
        targetType: TargetTypeType
    ) -> PutFeedbackResponseTypeDef:
        """
        Provides feedback against the specified assistant for the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#put_feedback)
        """

    def query_assistant(
        self,
        *,
        assistantId: str,
        queryText: str,
        maxResults: int = None,
        nextToken: str = None,
        queryCondition: List["QueryConditionTypeDef"] = None,
        sessionId: str = None
    ) -> QueryAssistantResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.query_assistant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#query_assistant)
        """

    def remove_knowledge_base_template_uri(self, *, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Removes a URI template from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.remove_knowledge_base_template_uri)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#remove_knowledge_base_template_uri)
        """

    def search_content(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: "SearchExpressionTypeDef",
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchContentResponseTypeDef:
        """
        Searches for content in a specified knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.search_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#search_content)
        """

    def search_quick_responses(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: "QuickResponseSearchExpressionTypeDef",
        attributes: Dict[str, str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchQuickResponsesResponseTypeDef:
        """
        Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect
        knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.search_quick_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#search_quick_responses)
        """

    def search_sessions(
        self,
        *,
        assistantId: str,
        searchExpression: "SearchExpressionTypeDef",
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchSessionsResponseTypeDef:
        """
        Searches for sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.search_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#search_sessions)
        """

    def start_content_upload(
        self, *, contentType: str, knowledgeBaseId: str, presignedUrlTimeToLive: int = None
    ) -> StartContentUploadResponseTypeDef:
        """
        Get a URL to upload content to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.start_content_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#start_content_upload)
        """

    def start_import_job(
        self,
        *,
        importJobType: Literal["QUICK_RESPONSES"],
        knowledgeBaseId: str,
        uploadId: str,
        clientToken: str = None,
        externalSourceConfiguration: "ExternalSourceConfigurationTypeDef" = None,
        metadata: Dict[str, str] = None
    ) -> StartImportJobResponseTypeDef:
        """
        Start an asynchronous job to import Amazon Q in Connect resources from an
        uploaded source file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.start_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#start_import_job)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#untag_resource)
        """

    def update_content(
        self,
        *,
        contentId: str,
        knowledgeBaseId: str,
        metadata: Dict[str, str] = None,
        overrideLinkOutUri: str = None,
        removeOverrideLinkOutUri: bool = None,
        revisionId: str = None,
        title: str = None,
        uploadId: str = None
    ) -> UpdateContentResponseTypeDef:
        """
        Updates information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.update_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#update_content)
        """

    def update_knowledge_base_template_uri(
        self, *, knowledgeBaseId: str, templateUri: str
    ) -> UpdateKnowledgeBaseTemplateUriResponseTypeDef:
        """
        Updates the template URI of a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.update_knowledge_base_template_uri)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#update_knowledge_base_template_uri)
        """

    def update_quick_response(
        self,
        *,
        knowledgeBaseId: str,
        quickResponseId: str,
        channels: List[str] = None,
        content: "QuickResponseDataProviderTypeDef" = None,
        contentType: str = None,
        description: str = None,
        groupingConfiguration: "GroupingConfigurationTypeDef" = None,
        isActive: bool = None,
        language: str = None,
        name: str = None,
        removeDescription: bool = None,
        removeGroupingConfiguration: bool = None,
        removeShortcutKey: bool = None,
        shortcutKey: str = None
    ) -> UpdateQuickResponseResponseTypeDef:
        """
        Updates an existing Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.update_quick_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#update_quick_response)
        """

    def update_session(
        self,
        *,
        assistantId: str,
        sessionId: str,
        description: str = None,
        tagFilter: "TagFilterTypeDef" = None
    ) -> UpdateSessionResponseTypeDef:
        """
        Updates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Client.update_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client.html#update_session)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assistant_associations"]
    ) -> ListAssistantAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListAssistantAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listassistantassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assistants"]) -> ListAssistantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListAssistants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listassistantspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contents"]) -> ListContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListContents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listcontentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_import_jobs"]) -> ListImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listimportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListKnowledgeBases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listknowledgebasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_responses"]
    ) -> ListQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.ListQuickResponses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#listquickresponsespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query_assistant"]) -> QueryAssistantPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.QueryAssistant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#queryassistantpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_content"]) -> SearchContentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.SearchContent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#searchcontentpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quick_responses"]
    ) -> SearchQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.SearchQuickResponses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#searchquickresponsespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_sessions"]) -> SearchSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/qconnect.html#QConnect.Paginator.SearchSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators.html#searchsessionspaginator)
        """
