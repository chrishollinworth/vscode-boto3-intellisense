"""
Type annotations for chime-sdk-meetings service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_meetings.client import ChimeSDKMeetingsClient

    session = Session()
    client: ChimeSDKMeetingsClient = session.client("chime-sdk-meetings")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchCreateAttendeeRequestTypeDef,
    BatchCreateAttendeeResponseTypeDef,
    BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef,
    CreateAttendeeRequestTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateMeetingRequestTypeDef,
    CreateMeetingResponseTypeDef,
    CreateMeetingWithAttendeesRequestTypeDef,
    CreateMeetingWithAttendeesResponseTypeDef,
    DeleteAttendeeRequestTypeDef,
    DeleteMeetingRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAttendeeRequestTypeDef,
    GetAttendeeResponseTypeDef,
    GetMeetingRequestTypeDef,
    GetMeetingResponseTypeDef,
    ListAttendeesRequestTypeDef,
    ListAttendeesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartMeetingTranscriptionRequestTypeDef,
    StopMeetingTranscriptionRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAttendeeCapabilitiesRequestTypeDef,
    UpdateAttendeeCapabilitiesResponseTypeDef,
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

__all__ = ("ChimeSDKMeetingsClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKMeetingsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings.html#ChimeSDKMeetings.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#generate_presigned_url)
        """

    def batch_create_attendee(
        self, **kwargs: Unpack[BatchCreateAttendeeRequestTypeDef]
    ) -> BatchCreateAttendeeResponseTypeDef:
        """
        Creates up to 100 attendees for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/batch_create_attendee.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#batch_create_attendee)
        """

    def batch_update_attendee_capabilities_except(
        self, **kwargs: Unpack[BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates <code>AttendeeCapabilities</code> except the capabilities listed in an
        <code>ExcludedAttendeeIds</code> table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/batch_update_attendee_capabilities_except.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#batch_update_attendee_capabilities_except)
        """

    def create_attendee(
        self, **kwargs: Unpack[CreateAttendeeRequestTypeDef]
    ) -> CreateAttendeeResponseTypeDef:
        """
        Creates a new attendee for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/create_attendee.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#create_attendee)
        """

    def create_meeting(
        self, **kwargs: Unpack[CreateMeetingRequestTypeDef]
    ) -> CreateMeetingResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region with no
        initial attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/create_meeting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#create_meeting)
        """

    def create_meeting_with_attendees(
        self, **kwargs: Unpack[CreateMeetingWithAttendeesRequestTypeDef]
    ) -> CreateMeetingWithAttendeesResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region, with
        attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/create_meeting_with_attendees.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#create_meeting_with_attendees)
        """

    def delete_attendee(
        self, **kwargs: Unpack[DeleteAttendeeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an attendee from the specified Amazon Chime SDK meeting and deletes
        their <code>JoinToken</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/delete_attendee.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#delete_attendee)
        """

    def delete_meeting(
        self, **kwargs: Unpack[DeleteMeetingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/delete_meeting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#delete_meeting)
        """

    def get_attendee(
        self, **kwargs: Unpack[GetAttendeeRequestTypeDef]
    ) -> GetAttendeeResponseTypeDef:
        """
        Gets the Amazon Chime SDK attendee details for a specified meeting ID and
        attendee ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/get_attendee.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#get_attendee)
        """

    def get_meeting(self, **kwargs: Unpack[GetMeetingRequestTypeDef]) -> GetMeetingResponseTypeDef:
        """
        Gets the Amazon Chime SDK meeting details for the specified meeting ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/get_meeting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#get_meeting)
        """

    def list_attendees(
        self, **kwargs: Unpack[ListAttendeesRequestTypeDef]
    ) -> ListAttendeesResponseTypeDef:
        """
        Lists the attendees for the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/list_attendees.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#list_attendees)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags available for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#list_tags_for_resource)
        """

    def start_meeting_transcription(
        self, **kwargs: Unpack[StartMeetingTranscriptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts transcription for the specified <code>meetingId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/start_meeting_transcription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#start_meeting_transcription)
        """

    def stop_meeting_transcription(
        self, **kwargs: Unpack[StopMeetingTranscriptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops transcription for the specified <code>meetingId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/stop_meeting_transcription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#stop_meeting_transcription)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        The resource that supports tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#untag_resource)
        """

    def update_attendee_capabilities(
        self, **kwargs: Unpack[UpdateAttendeeCapabilitiesRequestTypeDef]
    ) -> UpdateAttendeeCapabilitiesResponseTypeDef:
        """
        The capabilities that you want to update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings/client/update_attendee_capabilities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/client/#update_attendee_capabilities)
        """
