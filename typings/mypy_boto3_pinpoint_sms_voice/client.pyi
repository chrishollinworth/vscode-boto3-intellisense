# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for pinpoint-sms-voice service client

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_sms_voice import PinpointSMSVoiceClient

    client: PinpointSMSVoiceClient = boto3.client("pinpoint-sms-voice")
    ```
"""
from typing import Any, Dict, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_pinpoint_sms_voice.type_defs import (
    EventDestinationDefinitionTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    SendVoiceMessageResponseTypeDef,
    VoiceMessageContentTypeDef,
)

__all__ = ("PinpointSMSVoiceClient",)


class Exceptions:
    AlreadyExistsException: Type[Boto3ClientError]
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InternalServiceErrorException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]


class PinpointSMSVoiceClient:
    """
    [PinpointSMSVoice.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.can_paginate)
        """

    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set_event_destination)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set_event_destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.generate_presigned_url)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.get_configuration_set_event_destinations)
        """

    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: VoiceMessageContentTypeDef = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> SendVoiceMessageResponseTypeDef:
        """
        [Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.send_voice_message)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.update_configuration_set_event_destination)
        """
