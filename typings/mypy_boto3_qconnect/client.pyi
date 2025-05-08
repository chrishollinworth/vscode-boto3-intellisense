"""
Type annotations for qconnect service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qconnect.client import QConnectClient

    session = Session()
    client: QConnectClient = session.client("qconnect")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAIAgentsPaginator,
    ListAIAgentVersionsPaginator,
    ListAIGuardrailsPaginator,
    ListAIGuardrailVersionsPaginator,
    ListAIPromptsPaginator,
    ListAIPromptVersionsPaginator,
    ListAssistantAssociationsPaginator,
    ListAssistantsPaginator,
    ListContentAssociationsPaginator,
    ListContentsPaginator,
    ListImportJobsPaginator,
    ListKnowledgeBasesPaginator,
    ListMessagesPaginator,
    ListMessageTemplatesPaginator,
    ListMessageTemplateVersionsPaginator,
    ListQuickResponsesPaginator,
    QueryAssistantPaginator,
    SearchContentPaginator,
    SearchMessageTemplatesPaginator,
    SearchQuickResponsesPaginator,
    SearchSessionsPaginator,
)
from .type_defs import (
    ActivateMessageTemplateRequestTypeDef,
    ActivateMessageTemplateResponseTypeDef,
    CreateAIAgentRequestTypeDef,
    CreateAIAgentResponseTypeDef,
    CreateAIAgentVersionRequestTypeDef,
    CreateAIAgentVersionResponseTypeDef,
    CreateAIGuardrailRequestTypeDef,
    CreateAIGuardrailResponseTypeDef,
    CreateAIGuardrailVersionRequestTypeDef,
    CreateAIGuardrailVersionResponseTypeDef,
    CreateAIPromptRequestTypeDef,
    CreateAIPromptResponseTypeDef,
    CreateAIPromptVersionRequestTypeDef,
    CreateAIPromptVersionResponseTypeDef,
    CreateAssistantAssociationRequestTypeDef,
    CreateAssistantAssociationResponseTypeDef,
    CreateAssistantRequestTypeDef,
    CreateAssistantResponseTypeDef,
    CreateContentAssociationRequestTypeDef,
    CreateContentAssociationResponseTypeDef,
    CreateContentRequestTypeDef,
    CreateContentResponseTypeDef,
    CreateKnowledgeBaseRequestTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreateMessageTemplateAttachmentRequestTypeDef,
    CreateMessageTemplateAttachmentResponseTypeDef,
    CreateMessageTemplateRequestTypeDef,
    CreateMessageTemplateResponseTypeDef,
    CreateMessageTemplateVersionRequestTypeDef,
    CreateMessageTemplateVersionResponseTypeDef,
    CreateQuickResponseRequestTypeDef,
    CreateQuickResponseResponseTypeDef,
    CreateSessionRequestTypeDef,
    CreateSessionResponseTypeDef,
    DeactivateMessageTemplateRequestTypeDef,
    DeactivateMessageTemplateResponseTypeDef,
    DeleteAIAgentRequestTypeDef,
    DeleteAIAgentVersionRequestTypeDef,
    DeleteAIGuardrailRequestTypeDef,
    DeleteAIGuardrailVersionRequestTypeDef,
    DeleteAIPromptRequestTypeDef,
    DeleteAIPromptVersionRequestTypeDef,
    DeleteAssistantAssociationRequestTypeDef,
    DeleteAssistantRequestTypeDef,
    DeleteContentAssociationRequestTypeDef,
    DeleteContentRequestTypeDef,
    DeleteImportJobRequestTypeDef,
    DeleteKnowledgeBaseRequestTypeDef,
    DeleteMessageTemplateAttachmentRequestTypeDef,
    DeleteMessageTemplateRequestTypeDef,
    DeleteQuickResponseRequestTypeDef,
    GetAIAgentRequestTypeDef,
    GetAIAgentResponseTypeDef,
    GetAIGuardrailRequestTypeDef,
    GetAIGuardrailResponseTypeDef,
    GetAIPromptRequestTypeDef,
    GetAIPromptResponseTypeDef,
    GetAssistantAssociationRequestTypeDef,
    GetAssistantAssociationResponseTypeDef,
    GetAssistantRequestTypeDef,
    GetAssistantResponseTypeDef,
    GetContentAssociationRequestTypeDef,
    GetContentAssociationResponseTypeDef,
    GetContentRequestTypeDef,
    GetContentResponseTypeDef,
    GetContentSummaryRequestTypeDef,
    GetContentSummaryResponseTypeDef,
    GetImportJobRequestTypeDef,
    GetImportJobResponseTypeDef,
    GetKnowledgeBaseRequestTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetMessageTemplateRequestTypeDef,
    GetMessageTemplateResponseTypeDef,
    GetNextMessageRequestTypeDef,
    GetNextMessageResponseTypeDef,
    GetQuickResponseRequestTypeDef,
    GetQuickResponseResponseTypeDef,
    GetRecommendationsRequestTypeDef,
    GetRecommendationsResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    ListAIAgentsRequestTypeDef,
    ListAIAgentsResponseTypeDef,
    ListAIAgentVersionsRequestTypeDef,
    ListAIAgentVersionsResponseTypeDef,
    ListAIGuardrailsRequestTypeDef,
    ListAIGuardrailsResponseTypeDef,
    ListAIGuardrailVersionsRequestTypeDef,
    ListAIGuardrailVersionsResponseTypeDef,
    ListAIPromptsRequestTypeDef,
    ListAIPromptsResponseTypeDef,
    ListAIPromptVersionsRequestTypeDef,
    ListAIPromptVersionsResponseTypeDef,
    ListAssistantAssociationsRequestTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentAssociationsRequestTypeDef,
    ListContentAssociationsResponseTypeDef,
    ListContentsRequestTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListMessagesRequestTypeDef,
    ListMessagesResponseTypeDef,
    ListMessageTemplatesRequestTypeDef,
    ListMessageTemplatesResponseTypeDef,
    ListMessageTemplateVersionsRequestTypeDef,
    ListMessageTemplateVersionsResponseTypeDef,
    ListQuickResponsesRequestTypeDef,
    ListQuickResponsesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotifyRecommendationsReceivedRequestTypeDef,
    NotifyRecommendationsReceivedResponseTypeDef,
    PutFeedbackRequestTypeDef,
    PutFeedbackResponseTypeDef,
    QueryAssistantRequestTypeDef,
    QueryAssistantResponseTypeDef,
    RemoveAssistantAIAgentRequestTypeDef,
    RemoveKnowledgeBaseTemplateUriRequestTypeDef,
    RenderMessageTemplateRequestTypeDef,
    RenderMessageTemplateResponseTypeDef,
    SearchContentRequestTypeDef,
    SearchContentResponseTypeDef,
    SearchMessageTemplatesRequestTypeDef,
    SearchMessageTemplatesResponseTypeDef,
    SearchQuickResponsesRequestTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsRequestTypeDef,
    SearchSessionsResponseTypeDef,
    SendMessageRequestTypeDef,
    SendMessageResponseTypeDef,
    StartContentUploadRequestTypeDef,
    StartContentUploadResponseTypeDef,
    StartImportJobRequestTypeDef,
    StartImportJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAIAgentRequestTypeDef,
    UpdateAIAgentResponseTypeDef,
    UpdateAIGuardrailRequestTypeDef,
    UpdateAIGuardrailResponseTypeDef,
    UpdateAIPromptRequestTypeDef,
    UpdateAIPromptResponseTypeDef,
    UpdateAssistantAIAgentRequestTypeDef,
    UpdateAssistantAIAgentResponseTypeDef,
    UpdateContentRequestTypeDef,
    UpdateContentResponseTypeDef,
    UpdateKnowledgeBaseTemplateUriRequestTypeDef,
    UpdateKnowledgeBaseTemplateUriResponseTypeDef,
    UpdateMessageTemplateMetadataRequestTypeDef,
    UpdateMessageTemplateMetadataResponseTypeDef,
    UpdateMessageTemplateRequestTypeDef,
    UpdateMessageTemplateResponseTypeDef,
    UpdateQuickResponseRequestTypeDef,
    UpdateQuickResponseResponseTypeDef,
    UpdateSessionDataRequestTypeDef,
    UpdateSessionDataResponseTypeDef,
    UpdateSessionRequestTypeDef,
    UpdateSessionResponseTypeDef,
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

__all__ = ("QConnectClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#generate_presigned_url)
        """

    def activate_message_template(
        self, **kwargs: Unpack[ActivateMessageTemplateRequestTypeDef]
    ) -> ActivateMessageTemplateResponseTypeDef:
        """
        Activates a specific version of the Amazon Q in Connect message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/activate_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#activate_message_template)
        """

    def create_ai_agent(
        self, **kwargs: Unpack[CreateAIAgentRequestTypeDef]
    ) -> CreateAIAgentResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_agent)
        """

    def create_ai_agent_version(
        self, **kwargs: Unpack[CreateAIAgentVersionRequestTypeDef]
    ) -> CreateAIAgentVersionResponseTypeDef:
        """
        Creates and Amazon Q in Connect AI Agent version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_agent_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_agent_version)
        """

    def create_ai_guardrail(
        self, **kwargs: Unpack[CreateAIGuardrailRequestTypeDef]
    ) -> CreateAIGuardrailResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_guardrail)
        """

    def create_ai_guardrail_version(
        self, **kwargs: Unpack[CreateAIGuardrailVersionRequestTypeDef]
    ) -> CreateAIGuardrailVersionResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Guardrail version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_guardrail_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_guardrail_version)
        """

    def create_ai_prompt(
        self, **kwargs: Unpack[CreateAIPromptRequestTypeDef]
    ) -> CreateAIPromptResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_prompt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_prompt)
        """

    def create_ai_prompt_version(
        self, **kwargs: Unpack[CreateAIPromptVersionRequestTypeDef]
    ) -> CreateAIPromptVersionResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Prompt version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_ai_prompt_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_prompt_version)
        """

    def create_assistant(
        self, **kwargs: Unpack[CreateAssistantRequestTypeDef]
    ) -> CreateAssistantResponseTypeDef:
        """
        Creates an Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_assistant)
        """

    def create_assistant_association(
        self, **kwargs: Unpack[CreateAssistantAssociationRequestTypeDef]
    ) -> CreateAssistantAssociationResponseTypeDef:
        """
        Creates an association between an Amazon Q in Connect assistant and another
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_assistant_association)
        """

    def create_content(
        self, **kwargs: Unpack[CreateContentRequestTypeDef]
    ) -> CreateContentResponseTypeDef:
        """
        Creates Amazon Q in Connect content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_content)
        """

    def create_content_association(
        self, **kwargs: Unpack[CreateContentAssociationRequestTypeDef]
    ) -> CreateContentAssociationResponseTypeDef:
        """
        Creates an association between a content resource in a knowledge base and <a
        href="https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html">step-by-step
        guides</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_content_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_content_association)
        """

    def create_knowledge_base(
        self, **kwargs: Unpack[CreateKnowledgeBaseRequestTypeDef]
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_knowledge_base)
        """

    def create_message_template(
        self, **kwargs: Unpack[CreateMessageTemplateRequestTypeDef]
    ) -> CreateMessageTemplateResponseTypeDef:
        """
        Creates an Amazon Q in Connect message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_message_template)
        """

    def create_message_template_attachment(
        self, **kwargs: Unpack[CreateMessageTemplateAttachmentRequestTypeDef]
    ) -> CreateMessageTemplateAttachmentResponseTypeDef:
        """
        Uploads an attachment file to the specified Amazon Q in Connect message
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_message_template_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_message_template_attachment)
        """

    def create_message_template_version(
        self, **kwargs: Unpack[CreateMessageTemplateVersionRequestTypeDef]
    ) -> CreateMessageTemplateVersionResponseTypeDef:
        """
        Creates a new Amazon Q in Connect message template version from the current
        content and configuration of a message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_message_template_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_message_template_version)
        """

    def create_quick_response(
        self, **kwargs: Unpack[CreateQuickResponseRequestTypeDef]
    ) -> CreateQuickResponseResponseTypeDef:
        """
        Creates an Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_quick_response)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/create_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_session)
        """

    def deactivate_message_template(
        self, **kwargs: Unpack[DeactivateMessageTemplateRequestTypeDef]
    ) -> DeactivateMessageTemplateResponseTypeDef:
        """
        Deactivates a specific version of the Amazon Q in Connect message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/deactivate_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#deactivate_message_template)
        """

    def delete_ai_agent(self, **kwargs: Unpack[DeleteAIAgentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_agent)
        """

    def delete_ai_agent_version(
        self, **kwargs: Unpack[DeleteAIAgentVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Agent Version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_agent_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_agent_version)
        """

    def delete_ai_guardrail(
        self, **kwargs: Unpack[DeleteAIGuardrailRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_guardrail)
        """

    def delete_ai_guardrail_version(
        self, **kwargs: Unpack[DeleteAIGuardrailVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete and Amazon Q in Connect AI Guardrail version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_guardrail_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_guardrail_version)
        """

    def delete_ai_prompt(self, **kwargs: Unpack[DeleteAIPromptRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_prompt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_prompt)
        """

    def delete_ai_prompt_version(
        self, **kwargs: Unpack[DeleteAIPromptVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete and Amazon Q in Connect AI Prompt version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_ai_prompt_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_prompt_version)
        """

    def delete_assistant(self, **kwargs: Unpack[DeleteAssistantRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_assistant)
        """

    def delete_assistant_association(
        self, **kwargs: Unpack[DeleteAssistantAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_assistant_association)
        """

    def delete_content(self, **kwargs: Unpack[DeleteContentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_content)
        """

    def delete_content_association(
        self, **kwargs: Unpack[DeleteContentAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the content association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_content_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_content_association)
        """

    def delete_import_job(self, **kwargs: Unpack[DeleteImportJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the quick response import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_import_job)
        """

    def delete_knowledge_base(
        self, **kwargs: Unpack[DeleteKnowledgeBaseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_knowledge_base)
        """

    def delete_message_template(
        self, **kwargs: Unpack[DeleteMessageTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect message template entirely or a specific version
        of the message template if version is supplied in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_message_template)
        """

    def delete_message_template_attachment(
        self, **kwargs: Unpack[DeleteMessageTemplateAttachmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the attachment file from the Amazon Q in Connect message template that
        is referenced by <code>$LATEST</code> qualifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_message_template_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_message_template_attachment)
        """

    def delete_quick_response(
        self, **kwargs: Unpack[DeleteQuickResponseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/delete_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_quick_response)
        """

    def get_ai_agent(self, **kwargs: Unpack[GetAIAgentRequestTypeDef]) -> GetAIAgentResponseTypeDef:
        """
        Gets an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_ai_agent)
        """

    def get_ai_guardrail(
        self, **kwargs: Unpack[GetAIGuardrailRequestTypeDef]
    ) -> GetAIGuardrailResponseTypeDef:
        """
        Gets the Amazon Q in Connect AI Guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_ai_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_ai_guardrail)
        """

    def get_ai_prompt(
        self, **kwargs: Unpack[GetAIPromptRequestTypeDef]
    ) -> GetAIPromptResponseTypeDef:
        """
        Gets and Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_ai_prompt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_ai_prompt)
        """

    def get_assistant(
        self, **kwargs: Unpack[GetAssistantRequestTypeDef]
    ) -> GetAssistantResponseTypeDef:
        """
        Retrieves information about an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_assistant)
        """

    def get_assistant_association(
        self, **kwargs: Unpack[GetAssistantAssociationRequestTypeDef]
    ) -> GetAssistantAssociationResponseTypeDef:
        """
        Retrieves information about an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_assistant_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_assistant_association)
        """

    def get_content(self, **kwargs: Unpack[GetContentRequestTypeDef]) -> GetContentResponseTypeDef:
        """
        Retrieves content, including a pre-signed URL to download the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content)
        """

    def get_content_association(
        self, **kwargs: Unpack[GetContentAssociationRequestTypeDef]
    ) -> GetContentAssociationResponseTypeDef:
        """
        Returns the content association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_content_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content_association)
        """

    def get_content_summary(
        self, **kwargs: Unpack[GetContentSummaryRequestTypeDef]
    ) -> GetContentSummaryResponseTypeDef:
        """
        Retrieves summary information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_content_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content_summary)
        """

    def get_import_job(
        self, **kwargs: Unpack[GetImportJobRequestTypeDef]
    ) -> GetImportJobResponseTypeDef:
        """
        Retrieves the started import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_import_job)
        """

    def get_knowledge_base(
        self, **kwargs: Unpack[GetKnowledgeBaseRequestTypeDef]
    ) -> GetKnowledgeBaseResponseTypeDef:
        """
        Retrieves information about the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_knowledge_base.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_knowledge_base)
        """

    def get_message_template(
        self, **kwargs: Unpack[GetMessageTemplateRequestTypeDef]
    ) -> GetMessageTemplateResponseTypeDef:
        """
        Retrieves the Amazon Q in Connect message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_message_template)
        """

    def get_next_message(
        self, **kwargs: Unpack[GetNextMessageRequestTypeDef]
    ) -> GetNextMessageResponseTypeDef:
        """
        Retrieves next message on an Amazon Q in Connect session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_next_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_next_message)
        """

    def get_quick_response(
        self, **kwargs: Unpack[GetQuickResponseRequestTypeDef]
    ) -> GetQuickResponseResponseTypeDef:
        """
        Retrieves the quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_quick_response)
        """

    def get_recommendations(
        self, **kwargs: Unpack[GetRecommendationsRequestTypeDef]
    ) -> GetRecommendationsResponseTypeDef:
        """
        This API will be discontinued starting June 1, 2024.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_recommendations)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Retrieves information for a specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_session)
        """

    def list_ai_agent_versions(
        self, **kwargs: Unpack[ListAIAgentVersionsRequestTypeDef]
    ) -> ListAIAgentVersionsResponseTypeDef:
        """
        List AI Agent versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_agent_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_agent_versions)
        """

    def list_ai_agents(
        self, **kwargs: Unpack[ListAIAgentsRequestTypeDef]
    ) -> ListAIAgentsResponseTypeDef:
        """
        Lists AI Agents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_agents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_agents)
        """

    def list_ai_guardrail_versions(
        self, **kwargs: Unpack[ListAIGuardrailVersionsRequestTypeDef]
    ) -> ListAIGuardrailVersionsResponseTypeDef:
        """
        Lists AI Guardrail versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_guardrail_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_guardrail_versions)
        """

    def list_ai_guardrails(
        self, **kwargs: Unpack[ListAIGuardrailsRequestTypeDef]
    ) -> ListAIGuardrailsResponseTypeDef:
        """
        Lists the AI Guardrails available on the Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_guardrails.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_guardrails)
        """

    def list_ai_prompt_versions(
        self, **kwargs: Unpack[ListAIPromptVersionsRequestTypeDef]
    ) -> ListAIPromptVersionsResponseTypeDef:
        """
        Lists AI Prompt versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_prompt_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_prompt_versions)
        """

    def list_ai_prompts(
        self, **kwargs: Unpack[ListAIPromptsRequestTypeDef]
    ) -> ListAIPromptsResponseTypeDef:
        """
        Lists the AI Prompts available on the Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_ai_prompts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_prompts)
        """

    def list_assistant_associations(
        self, **kwargs: Unpack[ListAssistantAssociationsRequestTypeDef]
    ) -> ListAssistantAssociationsResponseTypeDef:
        """
        Lists information about assistant associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_assistant_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_assistant_associations)
        """

    def list_assistants(
        self, **kwargs: Unpack[ListAssistantsRequestTypeDef]
    ) -> ListAssistantsResponseTypeDef:
        """
        Lists information about assistants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_assistants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_assistants)
        """

    def list_content_associations(
        self, **kwargs: Unpack[ListContentAssociationsRequestTypeDef]
    ) -> ListContentAssociationsResponseTypeDef:
        """
        Lists the content associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_content_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_content_associations)
        """

    def list_contents(
        self, **kwargs: Unpack[ListContentsRequestTypeDef]
    ) -> ListContentsResponseTypeDef:
        """
        Lists the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_contents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_contents)
        """

    def list_import_jobs(
        self, **kwargs: Unpack[ListImportJobsRequestTypeDef]
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists information about import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_import_jobs)
        """

    def list_knowledge_bases(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestTypeDef]
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_knowledge_bases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_knowledge_bases)
        """

    def list_message_template_versions(
        self, **kwargs: Unpack[ListMessageTemplateVersionsRequestTypeDef]
    ) -> ListMessageTemplateVersionsResponseTypeDef:
        """
        Lists all the available versions for the specified Amazon Q in Connect message
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_message_template_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_message_template_versions)
        """

    def list_message_templates(
        self, **kwargs: Unpack[ListMessageTemplatesRequestTypeDef]
    ) -> ListMessageTemplatesResponseTypeDef:
        """
        Lists all the available Amazon Q in Connect message templates for the specified
        knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_message_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_message_templates)
        """

    def list_messages(
        self, **kwargs: Unpack[ListMessagesRequestTypeDef]
    ) -> ListMessagesResponseTypeDef:
        """
        Lists messages on an Amazon Q in Connect session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_messages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_messages)
        """

    def list_quick_responses(
        self, **kwargs: Unpack[ListQuickResponsesRequestTypeDef]
    ) -> ListQuickResponsesResponseTypeDef:
        """
        Lists information about quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_quick_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_quick_responses)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_tags_for_resource)
        """

    def notify_recommendations_received(
        self, **kwargs: Unpack[NotifyRecommendationsReceivedRequestTypeDef]
    ) -> NotifyRecommendationsReceivedResponseTypeDef:
        """
        Removes the specified recommendations from the specified assistant's queue of
        newly available recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/notify_recommendations_received.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#notify_recommendations_received)
        """

    def put_feedback(
        self, **kwargs: Unpack[PutFeedbackRequestTypeDef]
    ) -> PutFeedbackResponseTypeDef:
        """
        Provides feedback against the specified assistant for the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/put_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#put_feedback)
        """

    def query_assistant(
        self, **kwargs: Unpack[QueryAssistantRequestTypeDef]
    ) -> QueryAssistantResponseTypeDef:
        """
        This API will be discontinued starting June 1, 2024.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/query_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#query_assistant)
        """

    def remove_assistant_ai_agent(
        self, **kwargs: Unpack[RemoveAssistantAIAgentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the AI Agent that is set for use by default on an Amazon Q in Connect
        Assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/remove_assistant_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#remove_assistant_ai_agent)
        """

    def remove_knowledge_base_template_uri(
        self, **kwargs: Unpack[RemoveKnowledgeBaseTemplateUriRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a URI template from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/remove_knowledge_base_template_uri.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#remove_knowledge_base_template_uri)
        """

    def render_message_template(
        self, **kwargs: Unpack[RenderMessageTemplateRequestTypeDef]
    ) -> RenderMessageTemplateResponseTypeDef:
        """
        Renders the Amazon Q in Connect message template based on the attribute values
        provided and generates the message content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/render_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#render_message_template)
        """

    def search_content(
        self, **kwargs: Unpack[SearchContentRequestTypeDef]
    ) -> SearchContentResponseTypeDef:
        """
        Searches for content in a specified knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/search_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_content)
        """

    def search_message_templates(
        self, **kwargs: Unpack[SearchMessageTemplatesRequestTypeDef]
    ) -> SearchMessageTemplatesResponseTypeDef:
        """
        Searches for Amazon Q in Connect message templates in the specified knowledge
        base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/search_message_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_message_templates)
        """

    def search_quick_responses(
        self, **kwargs: Unpack[SearchQuickResponsesRequestTypeDef]
    ) -> SearchQuickResponsesResponseTypeDef:
        """
        Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect
        knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/search_quick_responses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_quick_responses)
        """

    def search_sessions(
        self, **kwargs: Unpack[SearchSessionsRequestTypeDef]
    ) -> SearchSessionsResponseTypeDef:
        """
        Searches for sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/search_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_sessions)
        """

    def send_message(
        self, **kwargs: Unpack[SendMessageRequestTypeDef]
    ) -> SendMessageResponseTypeDef:
        """
        Submits a message to the Amazon Q in Connect session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/send_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#send_message)
        """

    def start_content_upload(
        self, **kwargs: Unpack[StartContentUploadRequestTypeDef]
    ) -> StartContentUploadResponseTypeDef:
        """
        Get a URL to upload content to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/start_content_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#start_content_upload)
        """

    def start_import_job(
        self, **kwargs: Unpack[StartImportJobRequestTypeDef]
    ) -> StartImportJobResponseTypeDef:
        """
        Start an asynchronous job to import Amazon Q in Connect resources from an
        uploaded source file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/start_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#start_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#untag_resource)
        """

    def update_ai_agent(
        self, **kwargs: Unpack[UpdateAIAgentRequestTypeDef]
    ) -> UpdateAIAgentResponseTypeDef:
        """
        Updates an AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_ai_agent)
        """

    def update_ai_guardrail(
        self, **kwargs: Unpack[UpdateAIGuardrailRequestTypeDef]
    ) -> UpdateAIGuardrailResponseTypeDef:
        """
        Updates an AI Guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_ai_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_ai_guardrail)
        """

    def update_ai_prompt(
        self, **kwargs: Unpack[UpdateAIPromptRequestTypeDef]
    ) -> UpdateAIPromptResponseTypeDef:
        """
        Updates an AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_ai_prompt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_ai_prompt)
        """

    def update_assistant_ai_agent(
        self, **kwargs: Unpack[UpdateAssistantAIAgentRequestTypeDef]
    ) -> UpdateAssistantAIAgentResponseTypeDef:
        """
        Updates the AI Agent that is set for use by default on an Amazon Q in Connect
        Assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_assistant_ai_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_assistant_ai_agent)
        """

    def update_content(
        self, **kwargs: Unpack[UpdateContentRequestTypeDef]
    ) -> UpdateContentResponseTypeDef:
        """
        Updates information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_content)
        """

    def update_knowledge_base_template_uri(
        self, **kwargs: Unpack[UpdateKnowledgeBaseTemplateUriRequestTypeDef]
    ) -> UpdateKnowledgeBaseTemplateUriResponseTypeDef:
        """
        Updates the template URI of a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_knowledge_base_template_uri.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_knowledge_base_template_uri)
        """

    def update_message_template(
        self, **kwargs: Unpack[UpdateMessageTemplateRequestTypeDef]
    ) -> UpdateMessageTemplateResponseTypeDef:
        """
        Updates the Amazon Q in Connect message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_message_template)
        """

    def update_message_template_metadata(
        self, **kwargs: Unpack[UpdateMessageTemplateMetadataRequestTypeDef]
    ) -> UpdateMessageTemplateMetadataResponseTypeDef:
        """
        Updates the Amazon Q in Connect message template metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_message_template_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_message_template_metadata)
        """

    def update_quick_response(
        self, **kwargs: Unpack[UpdateQuickResponseRequestTypeDef]
    ) -> UpdateQuickResponseResponseTypeDef:
        """
        Updates an existing Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_quick_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_quick_response)
        """

    def update_session(
        self, **kwargs: Unpack[UpdateSessionRequestTypeDef]
    ) -> UpdateSessionResponseTypeDef:
        """
        Updates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_session)
        """

    def update_session_data(
        self, **kwargs: Unpack[UpdateSessionDataRequestTypeDef]
    ) -> UpdateSessionDataResponseTypeDef:
        """
        Updates the data stored on an Amazon Q in Connect Session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/update_session_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_session_data)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_agent_versions"]
    ) -> ListAIAgentVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_agents"]
    ) -> ListAIAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_guardrail_versions"]
    ) -> ListAIGuardrailVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_guardrails"]
    ) -> ListAIGuardrailsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_prompt_versions"]
    ) -> ListAIPromptVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ai_prompts"]
    ) -> ListAIPromptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assistant_associations"]
    ) -> ListAssistantAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assistants"]
    ) -> ListAssistantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_content_associations"]
    ) -> ListContentAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contents"]
    ) -> ListContentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_import_jobs"]
    ) -> ListImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_message_template_versions"]
    ) -> ListMessageTemplateVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_message_templates"]
    ) -> ListMessageTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_messages"]
    ) -> ListMessagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_quick_responses"]
    ) -> ListQuickResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["query_assistant"]
    ) -> QueryAssistantPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_content"]
    ) -> SearchContentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_message_templates"]
    ) -> SearchMessageTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_quick_responses"]
    ) -> SearchQuickResponsesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_sessions"]
    ) -> SearchSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """
