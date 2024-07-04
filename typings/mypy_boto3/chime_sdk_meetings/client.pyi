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
    AttendeeCapabilitiesTypeDef,
    AttendeeIdItemTypeDef,
    BatchCreateAttendeeResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateMeetingResponseTypeDef,
    CreateMeetingWithAttendeesResponseTypeDef,
    GetAttendeeResponseTypeDef,
    GetMeetingResponseTypeDef,
    ListAttendeesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MeetingFeaturesConfigurationTypeDef,
    NotificationsConfigurationTypeDef,
    TagTypeDef,
    TranscriptionConfigurationTypeDef,
    UpdateAttendeeCapabilitiesResponseTypeDef,
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
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class ChimeSDKMeetingsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client)
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
        Creates up to 100 attendees for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.batch_create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#batch_create_attendee)
        """

    def batch_update_attendee_capabilities_except(
        self,
        *,
        MeetingId: str,
        ExcludedAttendeeIds: List["AttendeeIdItemTypeDef"],
        Capabilities: "AttendeeCapabilitiesTypeDef"
    ) -> None:
        """
        Updates `AttendeeCapabilities` except the capabilities listed in an
        `ExcludedAttendeeIds` table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.batch_update_attendee_capabilities_except)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#batch_update_attendee_capabilities_except)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#close)
        """

    def create_attendee(
        self,
        *,
        MeetingId: str,
        ExternalUserId: str,
        Capabilities: "AttendeeCapabilitiesTypeDef" = None
    ) -> CreateAttendeeResponseTypeDef:
        """
        Creates a new attendee for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#create_attendee)
        """

    def create_meeting(
        self,
        *,
        ClientRequestToken: str,
        MediaRegion: str,
        ExternalMeetingId: str,
        MeetingHostId: str = None,
        NotificationsConfiguration: "NotificationsConfigurationTypeDef" = None,
        MeetingFeatures: "MeetingFeaturesConfigurationTypeDef" = None,
        PrimaryMeetingId: str = None,
        TenantIds: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMeetingResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region with no
        initial attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_meeting)
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
        MeetingFeatures: "MeetingFeaturesConfigurationTypeDef" = None,
        NotificationsConfiguration: "NotificationsConfigurationTypeDef" = None,
        PrimaryMeetingId: str = None,
        TenantIds: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMeetingWithAttendeesResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region, with
        attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.create_meeting_with_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#create_meeting_with_attendees)
        """

    def delete_attendee(self, *, MeetingId: str, AttendeeId: str) -> None:
        """
        Deletes an attendee from the specified Amazon Chime SDK meeting and deletes
        their `JoinToken`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.delete_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#delete_attendee)
        """

    def delete_meeting(self, *, MeetingId: str) -> None:
        """
        Deletes the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.delete_meeting)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#generate_presigned_url)
        """

    def get_attendee(self, *, MeetingId: str, AttendeeId: str) -> GetAttendeeResponseTypeDef:
        """
        Gets the Amazon Chime SDK attendee details for a specified meeting ID and
        attendee ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.get_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#get_attendee)
        """

    def get_meeting(self, *, MeetingId: str) -> GetMeetingResponseTypeDef:
        """
        Gets the Amazon Chime SDK meeting details for the specified meeting ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.get_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#get_meeting)
        """

    def list_attendees(
        self, *, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseTypeDef:
        """
        Lists the attendees for the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.list_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#list_attendees)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags available for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#list_tags_for_resource)
        """

    def start_meeting_transcription(
        self, *, MeetingId: str, TranscriptionConfiguration: "TranscriptionConfigurationTypeDef"
    ) -> None:
        """
        Starts transcription for the specified `meetingId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.start_meeting_transcription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#start_meeting_transcription)
        """

    def stop_meeting_transcription(self, *, MeetingId: str) -> None:
        """
        Stops transcription for the specified `meetingId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.stop_meeting_transcription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#stop_meeting_transcription)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        The resource that supports tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#untag_resource)
        """

    def update_attendee_capabilities(
        self, *, MeetingId: str, AttendeeId: str, Capabilities: "AttendeeCapabilitiesTypeDef"
    ) -> UpdateAttendeeCapabilitiesResponseTypeDef:
        """
        The capabilities that you want to update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client.update_attendee_capabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client.html#update_attendee_capabilities)
        """
