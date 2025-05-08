"""
Type annotations for wisdom service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_wisdom.client import ConnectWisdomServiceClient

    session = Session()
    client: ConnectWisdomServiceClient = session.client("wisdom")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    CreateAssistantAssociationRequestTypeDef,
    CreateAssistantAssociationResponseTypeDef,
    CreateAssistantRequestTypeDef,
    CreateAssistantResponseTypeDef,
    CreateContentRequestTypeDef,
    CreateContentResponseTypeDef,
    CreateKnowledgeBaseRequestTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreateQuickResponseRequestTypeDef,
    CreateQuickResponseResponseTypeDef,
    CreateSessionRequestTypeDef,
    CreateSessionResponseTypeDef,
    DeleteAssistantAssociationRequestTypeDef,
    DeleteAssistantRequestTypeDef,
    DeleteContentRequestTypeDef,
    DeleteImportJobRequestTypeDef,
    DeleteKnowledgeBaseRequestTypeDef,
    DeleteQuickResponseRequestTypeDef,
    GetAssistantAssociationRequestTypeDef,
    GetAssistantAssociationResponseTypeDef,
    GetAssistantRequestTypeDef,
    GetAssistantResponseTypeDef,
    GetContentRequestTypeDef,
    GetContentResponseTypeDef,
    GetContentSummaryRequestTypeDef,
    GetContentSummaryResponseTypeDef,
    GetImportJobRequestTypeDef,
    GetImportJobResponseTypeDef,
    GetKnowledgeBaseRequestTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetQuickResponseRequestTypeDef,
    GetQuickResponseResponseTypeDef,
    GetRecommendationsRequestTypeDef,
    GetRecommendationsResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    ListAssistantAssociationsRequestTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsRequestTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesRequestTypeDef,
    ListQuickResponsesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotifyRecommendationsReceivedRequestTypeDef,
    NotifyRecommendationsReceivedResponseTypeDef,
    QueryAssistantRequestTypeDef,
    QueryAssistantResponseTypeDef,
    RemoveKnowledgeBaseTemplateUriRequestTypeDef,
    SearchContentRequestTypeDef,
    SearchContentResponseTypeDef,
    SearchQuickResponsesRequestTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsRequestTypeDef,
    SearchSessionsResponseTypeDef,
    StartContentUploadRequestTypeDef,
    StartContentUploadResponseTypeDef,
    StartImportJobRequestTypeDef,
    StartImportJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateContentRequestTypeDef,
    UpdateContentResponseTypeDef,
    UpdateKnowledgeBaseTemplateUriRequestTypeDef,
    UpdateKnowledgeBaseTemplateUriResponseTypeDef,
    UpdateQuickResponseRequestTypeDef,
    UpdateQuickResponseResponseTypeDef,
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

__all__ = ("ConnectWisdomServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ConnectWisdomServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom.html#ConnectWisdomService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectWisdomServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom.html#ConnectWisdomService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#generate_presigned_url)
        """

    def create_assistant(
        self, **kwargs: Unpack[CreateAssistantRequestTypeDef]
    ) -> CreateAssistantResponseTypeDef:
        """
        Creates an Amazon Connect Wisdom assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_assistant)
        """

    def create_assistant_association(
        self, **kwargs: Unpack[CreateAssistantAssociationRequestTypeDef]
    ) -> CreateAssistantAssociationResponseTypeDef:
        """
        Creates an association between an Amazon Connect Wisdom assistant and another
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_assistant_association)
        """

    def create_content(
        self, **kwargs: Unpack[CreateContentRequestTypeDef]
    ) -> CreateContentResponseTypeDef:
        """
        Creates Wisdom content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_content)
        """

    def create_knowledge_base(
        self, **kwargs: Unpack[CreateKnowledgeBaseRequestTypeDef]
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_knowledge_base)
        """

    def create_quick_response(
        self, **kwargs: Unpack[CreateQuickResponseRequestTypeDef]
    ) -> CreateQuickResponseResponseTypeDef:
        """
        Creates a Wisdom quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_quick_response)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/create_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#create_session)
        """

    def delete_assistant(self, **kwargs: Unpack[DeleteAssistantRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_assistant)
        """

    def delete_assistant_association(
        self, **kwargs: Unpack[DeleteAssistantAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_assistant_association)
        """

    def delete_content(self, **kwargs: Unpack[DeleteContentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_content)
        """

    def delete_import_job(self, **kwargs: Unpack[DeleteImportJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the quick response import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_import_job)
        """

    def delete_knowledge_base(
        self, **kwargs: Unpack[DeleteKnowledgeBaseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_knowledge_base)
        """

    def delete_quick_response(
        self, **kwargs: Unpack[DeleteQuickResponseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/delete_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#delete_quick_response)
        """

    def get_assistant(
        self, **kwargs: Unpack[GetAssistantRequestTypeDef]
    ) -> GetAssistantResponseTypeDef:
        """
        Retrieves information about an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_assistant)
        """

    def get_assistant_association(
        self, **kwargs: Unpack[GetAssistantAssociationRequestTypeDef]
    ) -> GetAssistantAssociationResponseTypeDef:
        """
        Retrieves information about an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_assistant_association)
        """

    def get_content(self, **kwargs: Unpack[GetContentRequestTypeDef]) -> GetContentResponseTypeDef:
        """
        Retrieves content, including a pre-signed URL to download the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_content)
        """

    def get_content_summary(
        self, **kwargs: Unpack[GetContentSummaryRequestTypeDef]
    ) -> GetContentSummaryResponseTypeDef:
        """
        Retrieves summary information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_content_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_content_summary)
        """

    def get_import_job(
        self, **kwargs: Unpack[GetImportJobRequestTypeDef]
    ) -> GetImportJobResponseTypeDef:
        """
        Retrieves the started import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_import_job)
        """

    def get_knowledge_base(
        self, **kwargs: Unpack[GetKnowledgeBaseRequestTypeDef]
    ) -> GetKnowledgeBaseResponseTypeDef:
        """
        Retrieves information about the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_knowledge_base)
        """

    def get_quick_response(
        self, **kwargs: Unpack[GetQuickResponseRequestTypeDef]
    ) -> GetQuickResponseResponseTypeDef:
        """
        Retrieves the quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_quick_response)
        """

    def get_recommendations(
        self, **kwargs: Unpack[GetRecommendationsRequestTypeDef]
    ) -> GetRecommendationsResponseTypeDef:
        """
        Retrieves recommendations for the specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_recommendations)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Retrieves information for a specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_session)
        """

    def list_assistant_associations(
        self, **kwargs: Unpack[ListAssistantAssociationsRequestTypeDef]
    ) -> ListAssistantAssociationsResponseTypeDef:
        """
        Lists information about assistant associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_assistant_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_assistant_associations)
        """

    def list_assistants(
        self, **kwargs: Unpack[ListAssistantsRequestTypeDef]
    ) -> ListAssistantsResponseTypeDef:
        """
        Lists information about assistants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_assistants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_assistants)
        """

    def list_contents(
        self, **kwargs: Unpack[ListContentsRequestTypeDef]
    ) -> ListContentsResponseTypeDef:
        """
        Lists the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_contents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_contents)
        """

    def list_import_jobs(
        self, **kwargs: Unpack[ListImportJobsRequestTypeDef]
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists information about import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_import_jobs)
        """

    def list_knowledge_bases(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestTypeDef]
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_knowledge_bases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_knowledge_bases)
        """

    def list_quick_responses(
        self, **kwargs: Unpack[ListQuickResponsesRequestTypeDef]
    ) -> ListQuickResponsesResponseTypeDef:
        """
        Lists information about quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_quick_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_quick_responses)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#list_tags_for_resource)
        """

    def notify_recommendations_received(
        self, **kwargs: Unpack[NotifyRecommendationsReceivedRequestTypeDef]
    ) -> NotifyRecommendationsReceivedResponseTypeDef:
        """
        Removes the specified recommendations from the specified assistant's queue of
        newly available recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/notify_recommendations_received.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#notify_recommendations_received)
        """

    def query_assistant(
        self, **kwargs: Unpack[QueryAssistantRequestTypeDef]
    ) -> QueryAssistantResponseTypeDef:
        """
        Performs a manual search against the specified assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/query_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#query_assistant)
        """

    def remove_knowledge_base_template_uri(
        self, **kwargs: Unpack[RemoveKnowledgeBaseTemplateUriRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a URI template from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/remove_knowledge_base_template_uri.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#remove_knowledge_base_template_uri)
        """

    def search_content(
        self, **kwargs: Unpack[SearchContentRequestTypeDef]
    ) -> SearchContentResponseTypeDef:
        """
        Searches for content in a specified knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/search_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#search_content)
        """

    def search_quick_responses(
        self, **kwargs: Unpack[SearchQuickResponsesRequestTypeDef]
    ) -> SearchQuickResponsesResponseTypeDef:
        """
        Searches existing Wisdom quick responses in a Wisdom knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/search_quick_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#search_quick_responses)
        """

    def search_sessions(
        self, **kwargs: Unpack[SearchSessionsRequestTypeDef]
    ) -> SearchSessionsResponseTypeDef:
        """
        Searches for sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/search_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#search_sessions)
        """

    def start_content_upload(
        self, **kwargs: Unpack[StartContentUploadRequestTypeDef]
    ) -> StartContentUploadResponseTypeDef:
        """
        Get a URL to upload content to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/start_content_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#start_content_upload)
        """

    def start_import_job(
        self, **kwargs: Unpack[StartImportJobRequestTypeDef]
    ) -> StartImportJobResponseTypeDef:
        """
        Start an asynchronous job to import Wisdom resources from an uploaded source
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/start_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#start_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#untag_resource)
        """

    def update_content(
        self, **kwargs: Unpack[UpdateContentRequestTypeDef]
    ) -> UpdateContentResponseTypeDef:
        """
        Updates information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/update_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#update_content)
        """

    def update_knowledge_base_template_uri(
        self, **kwargs: Unpack[UpdateKnowledgeBaseTemplateUriRequestTypeDef]
    ) -> UpdateKnowledgeBaseTemplateUriResponseTypeDef:
        """
        Updates the template URI of a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/update_knowledge_base_template_uri.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#update_knowledge_base_template_uri)
        """

    def update_quick_response(
        self, **kwargs: Unpack[UpdateQuickResponseRequestTypeDef]
    ) -> UpdateQuickResponseResponseTypeDef:
        """
        Updates an existing Wisdom quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/update_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#update_quick_response)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assistant_associations"]
    ) -> ListAssistantAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assistants"]
    ) -> ListAssistantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contents"]
    ) -> ListContentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_import_jobs"]
    ) -> ListImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_quick_responses"]
    ) -> ListQuickResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["query_assistant"]
    ) -> QueryAssistantPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_content"]
    ) -> SearchContentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_quick_responses"]
    ) -> SearchQuickResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_sessions"]
    ) -> SearchSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/client/#get_paginator)
        """
