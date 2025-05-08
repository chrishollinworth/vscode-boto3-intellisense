"""
Type annotations for connectparticipant service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectparticipant.client import ConnectParticipantClient

    session = Session()
    client: ConnectParticipantClient = session.client("connectparticipant")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CancelParticipantAuthenticationRequestTypeDef,
    CompleteAttachmentUploadRequestTypeDef,
    CreateParticipantConnectionRequestTypeDef,
    CreateParticipantConnectionResponseTypeDef,
    DescribeViewRequestTypeDef,
    DescribeViewResponseTypeDef,
    DisconnectParticipantRequestTypeDef,
    GetAttachmentRequestTypeDef,
    GetAttachmentResponseTypeDef,
    GetAuthenticationUrlRequestTypeDef,
    GetAuthenticationUrlResponseTypeDef,
    GetTranscriptRequestTypeDef,
    GetTranscriptResponseTypeDef,
    SendEventRequestTypeDef,
    SendEventResponseTypeDef,
    SendMessageRequestTypeDef,
    SendMessageResponseTypeDef,
    StartAttachmentUploadRequestTypeDef,
    StartAttachmentUploadResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ConnectParticipantClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ConnectParticipantClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectParticipantClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#generate_presigned_url)
        """

    def cancel_participant_authentication(
        self, **kwargs: Unpack[CancelParticipantAuthenticationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the authentication session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/cancel_participant_authentication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#cancel_participant_authentication)
        """

    def complete_attachment_upload(
        self, **kwargs: Unpack[CompleteAttachmentUploadRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Allows you to confirm that the attachment has been uploaded using the
        pre-signed URL provided in StartAttachmentUpload API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/complete_attachment_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#complete_attachment_upload)
        """

    def create_participant_connection(
        self, **kwargs: Unpack[CreateParticipantConnectionRequestTypeDef]
    ) -> CreateParticipantConnectionResponseTypeDef:
        """
        Creates the participant's connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/create_participant_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#create_participant_connection)
        """

    def describe_view(
        self, **kwargs: Unpack[DescribeViewRequestTypeDef]
    ) -> DescribeViewResponseTypeDef:
        """
        Retrieves the view for the specified view token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/describe_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#describe_view)
        """

    def disconnect_participant(
        self, **kwargs: Unpack[DisconnectParticipantRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disconnects a participant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/disconnect_participant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#disconnect_participant)
        """

    def get_attachment(
        self, **kwargs: Unpack[GetAttachmentRequestTypeDef]
    ) -> GetAttachmentResponseTypeDef:
        """
        Provides a pre-signed URL for download of a completed attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/get_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#get_attachment)
        """

    def get_authentication_url(
        self, **kwargs: Unpack[GetAuthenticationUrlRequestTypeDef]
    ) -> GetAuthenticationUrlResponseTypeDef:
        """
        Retrieves the AuthenticationUrl for the current authentication session for the
        AuthenticateCustomer flow block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/get_authentication_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#get_authentication_url)
        """

    def get_transcript(
        self, **kwargs: Unpack[GetTranscriptRequestTypeDef]
    ) -> GetTranscriptResponseTypeDef:
        """
        Retrieves a transcript of the session, including details about any attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/get_transcript.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#get_transcript)
        """

    def send_event(self, **kwargs: Unpack[SendEventRequestTypeDef]) -> SendEventResponseTypeDef:
        """
        The
        <code>application/vnd.amazonaws.connect.event.connection.acknowledged</code>
        ContentType will no longer be supported starting December 31, 2024.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/send_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#send_event)
        """

    def send_message(
        self, **kwargs: Unpack[SendMessageRequestTypeDef]
    ) -> SendMessageResponseTypeDef:
        """
        Sends a message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/send_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#send_message)
        """

    def start_attachment_upload(
        self, **kwargs: Unpack[StartAttachmentUploadRequestTypeDef]
    ) -> StartAttachmentUploadResponseTypeDef:
        """
        Provides a pre-signed Amazon S3 URL in response for uploading the file directly
        to S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant/client/start_attachment_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/client/#start_attachment_upload)
        """
