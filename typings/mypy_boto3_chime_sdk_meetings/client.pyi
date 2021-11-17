"""
Type annotations for chime-sdk-meetings service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_meetings import ChimeSDKMeetingsClient

    client: ChimeSDKMeetingsClient = boto3.client("chime-sdk-meetings")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    BatchCreateAttendeeResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateMeetingResponseTypeDef,
    CreateMeetingWithAttendeesResponseTypeDef,
    GetAttendeeResponseTypeDef,
    GetMeetingResponseTypeDef,
    ListAttendeesResponseTypeDef,
    NotificationsConfigurationTypeDef,
    TranscriptionConfigurationTypeDef,
)

__all__ = ("ChimeSDKMeetingsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class ChimeSDKMeetingsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKMeetingsClient exceptions.
        """
    def batch_create_attendee(
        self, *, MeetingId: str, Attendees: List["CreateAttendeeRequestItemTypeDef"]
    ) -> BatchCreateAttendeeResponseTypeDef:
        """
        Creates a group of meeting attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.batch_create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#batch_create_attendee)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#can_paginate)
        """
    def create_attendee(
        self, *, MeetingId: str, ExternalUserId: str
    ) -> CreateAttendeeResponseTypeDef:
        """
        Creates a new attendee for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#create_attendee)
        """
    def create_meeting(
        self,
        *,
        ClientRequestToken: str,
        MediaRegion: str,
        ExternalMeetingId: str,
        MeetingHostId: str = None,
        NotificationsConfiguration: "NotificationsConfigurationTypeDef" = None
    ) -> CreateMeetingResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region with no
        initial attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#create_meeting)
        """
    def create_meeting_with_attendees(
        self,
        *,
        ClientRequestToken: str,
        MediaRegion: str,
        ExternalMeetingId: str,
        Attendees: List["CreateAttendeeRequestItemTypeDef"],
        MeetingHostId: str = None,
        NotificationsConfiguration: "NotificationsConfigurationTypeDef" = None
    ) -> CreateMeetingWithAttendeesResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region, with
        attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_meeting_with_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#create_meeting_with_attendees)
        """
    def delete_attendee(self, *, MeetingId: str, AttendeeId: str) -> None:
        """
        Deletes an attendee from the specified Amazon Chime SDK meeting and deletes
        their `JoinToken`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.delete_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#delete_attendee)
        """
    def delete_meeting(self, *, MeetingId: str) -> None:
        """
        Deletes the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.delete_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#delete_meeting)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#generate_presigned_url)
        """
    def get_attendee(self, *, MeetingId: str, AttendeeId: str) -> GetAttendeeResponseTypeDef:
        """
        Gets the Amazon Chime SDK attendee details for a specified meeting ID and
        attendee ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.get_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#get_attendee)
        """
    def get_meeting(self, *, MeetingId: str) -> GetMeetingResponseTypeDef:
        """
        Gets the Amazon Chime SDK meeting details for the specified meeting ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.get_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#get_meeting)
        """
    def list_attendees(
        self, *, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseTypeDef:
        """
        Lists the attendees for the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.list_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#list_attendees)
        """
    def start_meeting_transcription(
        self, *, MeetingId: str, TranscriptionConfiguration: "TranscriptionConfigurationTypeDef"
    ) -> None:
        """
        Starts transcription for the specified `meetingId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.start_meeting_transcription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#start_meeting_transcription)
        """
    def stop_meeting_transcription(self, *, MeetingId: str) -> None:
        """
        Stops transcription for the specified `meetingId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.stop_meeting_transcription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#stop_meeting_transcription)
        """
