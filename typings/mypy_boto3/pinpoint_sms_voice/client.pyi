"""
Type annotations for pinpoint-sms-voice service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pinpoint_sms_voice.client import PinpointSMSVoiceClient

    session = Session()
    client: PinpointSMSVoiceClient = session.client("pinpoint-sms-voice")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateConfigurationSetEventDestinationRequestTypeDef,
    CreateConfigurationSetRequestTypeDef,
    DeleteConfigurationSetEventDestinationRequestTypeDef,
    DeleteConfigurationSetRequestTypeDef,
    GetConfigurationSetEventDestinationsRequestTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    SendVoiceMessageRequestTypeDef,
    SendVoiceMessageResponseTypeDef,
    UpdateConfigurationSetEventDestinationRequestTypeDef,
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

__all__ = ("PinpointSMSVoiceClient",)

class Exceptions(BaseClientExceptions):
    AlreadyExistsException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class PinpointSMSVoiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#generate_presigned_url)
        """

    def create_configuration_set(
        self, **kwargs: Unpack[CreateConfigurationSetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Create a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/create_configuration_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self, **kwargs: Unpack[CreateConfigurationSetEventDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Create a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/create_configuration_set_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#create_configuration_set_event_destination)
        """

    def delete_configuration_set(
        self, **kwargs: Unpack[DeleteConfigurationSetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/delete_configuration_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, **kwargs: Unpack[DeleteConfigurationSetEventDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/delete_configuration_set_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#delete_configuration_set_event_destination)
        """

    def get_configuration_set_event_destinations(
        self, **kwargs: Unpack[GetConfigurationSetEventDestinationsRequestTypeDef]
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        Obtain information about an event destination, including the types of events it
        reports, the Amazon Resource Name (ARN) of the destination, and the name of the
        event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/get_configuration_set_event_destinations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#get_configuration_set_event_destinations)
        """

    def send_voice_message(
        self, **kwargs: Unpack[SendVoiceMessageRequestTypeDef]
    ) -> SendVoiceMessageResponseTypeDef:
        """
        Create a new voice message and send it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/send_voice_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#send_voice_message)
        """

    def update_configuration_set_event_destination(
        self, **kwargs: Unpack[UpdateConfigurationSetEventDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update an event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice/client/update_configuration_set_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/client/#update_configuration_set_event_destination)
        """
