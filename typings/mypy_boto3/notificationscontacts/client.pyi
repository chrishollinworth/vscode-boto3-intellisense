"""
Type annotations for notificationscontacts service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_notificationscontacts.client import UserNotificationsContactsClient

    session = Session()
    client: UserNotificationsContactsClient = session.client("notificationscontacts")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListEmailContactsPaginator
from .type_defs import (
    ActivateEmailContactRequestTypeDef,
    CreateEmailContactRequestTypeDef,
    CreateEmailContactResponseTypeDef,
    DeleteEmailContactRequestTypeDef,
    GetEmailContactRequestTypeDef,
    GetEmailContactResponseTypeDef,
    ListEmailContactsRequestTypeDef,
    ListEmailContactsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SendActivationCodeRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("UserNotificationsContactsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class UserNotificationsContactsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts.html#UserNotificationsContacts.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        UserNotificationsContactsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts.html#UserNotificationsContacts.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#generate_presigned_url)
        """

    def activate_email_contact(
        self, **kwargs: Unpack[ActivateEmailContactRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Activates an email contact using an activation code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/activate_email_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#activate_email_contact)
        """

    def create_email_contact(
        self, **kwargs: Unpack[CreateEmailContactRequestTypeDef]
    ) -> CreateEmailContactResponseTypeDef:
        """
        Creates an email contact for the provided email address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/create_email_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#create_email_contact)
        """

    def delete_email_contact(
        self, **kwargs: Unpack[DeleteEmailContactRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an email contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/delete_email_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#delete_email_contact)
        """

    def get_email_contact(
        self, **kwargs: Unpack[GetEmailContactRequestTypeDef]
    ) -> GetEmailContactResponseTypeDef:
        """
        Returns an email contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/get_email_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#get_email_contact)
        """

    def list_email_contacts(
        self, **kwargs: Unpack[ListEmailContactsRequestTypeDef]
    ) -> ListEmailContactsResponseTypeDef:
        """
        Lists all email contacts created under the Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/list_email_contacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#list_email_contacts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#list_tags_for_resource)
        """

    def send_activation_code(
        self, **kwargs: Unpack[SendActivationCodeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends an activation email to the email address associated with the specified
        email contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/send_activation_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#send_activation_code)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#untag_resource)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_email_contacts"]
    ) -> ListEmailContactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notificationscontacts/client/#get_paginator)
        """
