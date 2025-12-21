"""
Type annotations for socialmessaging service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_socialmessaging.client import EndUserMessagingSocialClient

    session = Session()
    client: EndUserMessagingSocialClient = session.client("socialmessaging")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListLinkedWhatsAppBusinessAccountsPaginator,
    ListWhatsAppMessageTemplatesPaginator,
    ListWhatsAppTemplateLibraryPaginator,
)
from .type_defs import (
    AssociateWhatsAppBusinessAccountInputTypeDef,
    AssociateWhatsAppBusinessAccountOutputTypeDef,
    CreateWhatsAppMessageTemplateFromLibraryInputTypeDef,
    CreateWhatsAppMessageTemplateFromLibraryOutputTypeDef,
    CreateWhatsAppMessageTemplateInputTypeDef,
    CreateWhatsAppMessageTemplateMediaInputTypeDef,
    CreateWhatsAppMessageTemplateMediaOutputTypeDef,
    CreateWhatsAppMessageTemplateOutputTypeDef,
    DeleteWhatsAppMessageMediaInputTypeDef,
    DeleteWhatsAppMessageMediaOutputTypeDef,
    DeleteWhatsAppMessageTemplateInputTypeDef,
    DisassociateWhatsAppBusinessAccountInputTypeDef,
    GetLinkedWhatsAppBusinessAccountInputTypeDef,
    GetLinkedWhatsAppBusinessAccountOutputTypeDef,
    GetLinkedWhatsAppBusinessAccountPhoneNumberInputTypeDef,
    GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef,
    GetWhatsAppMessageMediaInputTypeDef,
    GetWhatsAppMessageMediaOutputTypeDef,
    GetWhatsAppMessageTemplateInputTypeDef,
    GetWhatsAppMessageTemplateOutputTypeDef,
    ListLinkedWhatsAppBusinessAccountsInputTypeDef,
    ListLinkedWhatsAppBusinessAccountsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWhatsAppMessageTemplatesInputTypeDef,
    ListWhatsAppMessageTemplatesOutputTypeDef,
    ListWhatsAppTemplateLibraryInputTypeDef,
    ListWhatsAppTemplateLibraryOutputTypeDef,
    PostWhatsAppMessageMediaInputTypeDef,
    PostWhatsAppMessageMediaOutputTypeDef,
    PutWhatsAppBusinessAccountEventDestinationsInputTypeDef,
    SendWhatsAppMessageInputTypeDef,
    SendWhatsAppMessageOutputTypeDef,
    TagResourceInputTypeDef,
    TagResourceOutputTypeDef,
    UntagResourceInputTypeDef,
    UntagResourceOutputTypeDef,
    UpdateWhatsAppMessageTemplateInputTypeDef,
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

__all__ = ("EndUserMessagingSocialClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedByMetaException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidParametersException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottledRequestException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EndUserMessagingSocialClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging.html#EndUserMessagingSocial.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EndUserMessagingSocialClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging.html#EndUserMessagingSocial.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#generate_presigned_url)
        """

    def associate_whatsapp_business_account(
        self, **kwargs: Unpack[AssociateWhatsAppBusinessAccountInputTypeDef]
    ) -> AssociateWhatsAppBusinessAccountOutputTypeDef:
        """
        This is only used through the Amazon Web Services console during sign-up to
        associate your WhatsApp Business Account to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/associate_whatsapp_business_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#associate_whatsapp_business_account)
        """

    def create_whatsapp_message_template(
        self, **kwargs: Unpack[CreateWhatsAppMessageTemplateInputTypeDef]
    ) -> CreateWhatsAppMessageTemplateOutputTypeDef:
        """
        Creates a new WhatsApp message template from a custom definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/create_whatsapp_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#create_whatsapp_message_template)
        """

    def create_whatsapp_message_template_from_library(
        self, **kwargs: Unpack[CreateWhatsAppMessageTemplateFromLibraryInputTypeDef]
    ) -> CreateWhatsAppMessageTemplateFromLibraryOutputTypeDef:
        """
        Creates a new WhatsApp message template using a template from Meta's template
        library.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/create_whatsapp_message_template_from_library.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#create_whatsapp_message_template_from_library)
        """

    def create_whatsapp_message_template_media(
        self, **kwargs: Unpack[CreateWhatsAppMessageTemplateMediaInputTypeDef]
    ) -> CreateWhatsAppMessageTemplateMediaOutputTypeDef:
        """
        Uploads media for use in a WhatsApp message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/create_whatsapp_message_template_media.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#create_whatsapp_message_template_media)
        """

    def delete_whatsapp_message_media(
        self, **kwargs: Unpack[DeleteWhatsAppMessageMediaInputTypeDef]
    ) -> DeleteWhatsAppMessageMediaOutputTypeDef:
        """
        Delete a media object from the WhatsApp service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/delete_whatsapp_message_media.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#delete_whatsapp_message_media)
        """

    def delete_whatsapp_message_template(
        self, **kwargs: Unpack[DeleteWhatsAppMessageTemplateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a WhatsApp message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/delete_whatsapp_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#delete_whatsapp_message_template)
        """

    def disassociate_whatsapp_business_account(
        self, **kwargs: Unpack[DisassociateWhatsAppBusinessAccountInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociate a WhatsApp Business Account (WABA) from your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/disassociate_whatsapp_business_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#disassociate_whatsapp_business_account)
        """

    def get_linked_whatsapp_business_account(
        self, **kwargs: Unpack[GetLinkedWhatsAppBusinessAccountInputTypeDef]
    ) -> GetLinkedWhatsAppBusinessAccountOutputTypeDef:
        """
        Get the details of your linked WhatsApp Business Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_linked_whatsapp_business_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_linked_whatsapp_business_account)
        """

    def get_linked_whatsapp_business_account_phone_number(
        self, **kwargs: Unpack[GetLinkedWhatsAppBusinessAccountPhoneNumberInputTypeDef]
    ) -> GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef:
        """
        Use your WhatsApp phone number id to get the WABA account id and phone number
        details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_linked_whatsapp_business_account_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_linked_whatsapp_business_account_phone_number)
        """

    def get_whatsapp_message_media(
        self, **kwargs: Unpack[GetWhatsAppMessageMediaInputTypeDef]
    ) -> GetWhatsAppMessageMediaOutputTypeDef:
        """
        Get a media file from the WhatsApp service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_whatsapp_message_media.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_whatsapp_message_media)
        """

    def get_whatsapp_message_template(
        self, **kwargs: Unpack[GetWhatsAppMessageTemplateInputTypeDef]
    ) -> GetWhatsAppMessageTemplateOutputTypeDef:
        """
        Retrieves a specific WhatsApp message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_whatsapp_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_whatsapp_message_template)
        """

    def list_linked_whatsapp_business_accounts(
        self, **kwargs: Unpack[ListLinkedWhatsAppBusinessAccountsInputTypeDef]
    ) -> ListLinkedWhatsAppBusinessAccountsOutputTypeDef:
        """
        List all WhatsApp Business Accounts linked to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/list_linked_whatsapp_business_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#list_linked_whatsapp_business_accounts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List all tags associated with a resource, such as a phone number or WABA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#list_tags_for_resource)
        """

    def list_whatsapp_message_templates(
        self, **kwargs: Unpack[ListWhatsAppMessageTemplatesInputTypeDef]
    ) -> ListWhatsAppMessageTemplatesOutputTypeDef:
        """
        Lists WhatsApp message templates for a specific WhatsApp Business Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/list_whatsapp_message_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#list_whatsapp_message_templates)
        """

    def list_whatsapp_template_library(
        self, **kwargs: Unpack[ListWhatsAppTemplateLibraryInputTypeDef]
    ) -> ListWhatsAppTemplateLibraryOutputTypeDef:
        """
        Lists templates available in Meta's template library for WhatsApp messaging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/list_whatsapp_template_library.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#list_whatsapp_template_library)
        """

    def post_whatsapp_message_media(
        self, **kwargs: Unpack[PostWhatsAppMessageMediaInputTypeDef]
    ) -> PostWhatsAppMessageMediaOutputTypeDef:
        """
        Upload a media file to the WhatsApp service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/post_whatsapp_message_media.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#post_whatsapp_message_media)
        """

    def put_whatsapp_business_account_event_destinations(
        self, **kwargs: Unpack[PutWhatsAppBusinessAccountEventDestinationsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Add an event destination to log event data from WhatsApp for a WhatsApp
        Business Account (WABA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/put_whatsapp_business_account_event_destinations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#put_whatsapp_business_account_event_destinations)
        """

    def send_whatsapp_message(
        self, **kwargs: Unpack[SendWhatsAppMessageInputTypeDef]
    ) -> SendWhatsAppMessageOutputTypeDef:
        """
        Send a WhatsApp message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/send_whatsapp_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#send_whatsapp_message)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> TagResourceOutputTypeDef:
        """
        Adds or overwrites only the specified tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> UntagResourceOutputTypeDef:
        """
        Removes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#untag_resource)
        """

    def update_whatsapp_message_template(
        self, **kwargs: Unpack[UpdateWhatsAppMessageTemplateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing WhatsApp message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/update_whatsapp_message_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#update_whatsapp_message_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_linked_whatsapp_business_accounts"]
    ) -> ListLinkedWhatsAppBusinessAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_whatsapp_message_templates"]
    ) -> ListWhatsAppMessageTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_whatsapp_template_library"]
    ) -> ListWhatsAppTemplateLibraryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/socialmessaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/client/#get_paginator)
        """
