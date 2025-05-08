"""
Type annotations for ivs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ivs.client import IVSClient

    session = Session()
    client: IVSClient = session.client("ivs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListChannelsPaginator,
    ListPlaybackKeyPairsPaginator,
    ListRecordingConfigurationsPaginator,
    ListStreamKeysPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    BatchGetChannelRequestTypeDef,
    BatchGetChannelResponseTypeDef,
    BatchGetStreamKeyRequestTypeDef,
    BatchGetStreamKeyResponseTypeDef,
    BatchStartViewerSessionRevocationRequestTypeDef,
    BatchStartViewerSessionRevocationResponseTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreatePlaybackRestrictionPolicyRequestTypeDef,
    CreatePlaybackRestrictionPolicyResponseTypeDef,
    CreateRecordingConfigurationRequestTypeDef,
    CreateRecordingConfigurationResponseTypeDef,
    CreateStreamKeyRequestTypeDef,
    CreateStreamKeyResponseTypeDef,
    DeleteChannelRequestTypeDef,
    DeletePlaybackKeyPairRequestTypeDef,
    DeletePlaybackRestrictionPolicyRequestTypeDef,
    DeleteRecordingConfigurationRequestTypeDef,
    DeleteStreamKeyRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChannelRequestTypeDef,
    GetChannelResponseTypeDef,
    GetPlaybackKeyPairRequestTypeDef,
    GetPlaybackKeyPairResponseTypeDef,
    GetPlaybackRestrictionPolicyRequestTypeDef,
    GetPlaybackRestrictionPolicyResponseTypeDef,
    GetRecordingConfigurationRequestTypeDef,
    GetRecordingConfigurationResponseTypeDef,
    GetStreamKeyRequestTypeDef,
    GetStreamKeyResponseTypeDef,
    GetStreamRequestTypeDef,
    GetStreamResponseTypeDef,
    GetStreamSessionRequestTypeDef,
    GetStreamSessionResponseTypeDef,
    ImportPlaybackKeyPairRequestTypeDef,
    ImportPlaybackKeyPairResponseTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsRequestTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListPlaybackRestrictionPoliciesRequestTypeDef,
    ListPlaybackRestrictionPoliciesResponseTypeDef,
    ListRecordingConfigurationsRequestTypeDef,
    ListRecordingConfigurationsResponseTypeDef,
    ListStreamKeysRequestTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamSessionsRequestTypeDef,
    ListStreamSessionsResponseTypeDef,
    ListStreamsRequestTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutMetadataRequestTypeDef,
    StartViewerSessionRevocationRequestTypeDef,
    StopStreamRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdatePlaybackRestrictionPolicyRequestTypeDef,
    UpdatePlaybackRestrictionPolicyResponseTypeDef,
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

__all__ = ("IVSClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ChannelNotBroadcasting: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StreamUnavailable: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IVSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IVSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#generate_presigned_url)
        """

    def batch_get_channel(
        self, **kwargs: Unpack[BatchGetChannelRequestTypeDef]
    ) -> BatchGetChannelResponseTypeDef:
        """
        Performs <a>GetChannel</a> on multiple ARNs simultaneously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/batch_get_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#batch_get_channel)
        """

    def batch_get_stream_key(
        self, **kwargs: Unpack[BatchGetStreamKeyRequestTypeDef]
    ) -> BatchGetStreamKeyResponseTypeDef:
        """
        Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/batch_get_stream_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#batch_get_stream_key)
        """

    def batch_start_viewer_session_revocation(
        self, **kwargs: Unpack[BatchStartViewerSessionRevocationRequestTypeDef]
    ) -> BatchStartViewerSessionRevocationResponseTypeDef:
        """
        Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer
        ID pairs simultaneously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/batch_start_viewer_session_revocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#batch_start_viewer_session_revocation)
        """

    def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new channel and an associated stream key to start streaming.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/create_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#create_channel)
        """

    def create_playback_restriction_policy(
        self, **kwargs: Unpack[CreatePlaybackRestrictionPolicyRequestTypeDef]
    ) -> CreatePlaybackRestrictionPolicyResponseTypeDef:
        """
        Creates a new playback restriction policy, for constraining playback by
        countries and/or origins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/create_playback_restriction_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#create_playback_restriction_policy)
        """

    def create_recording_configuration(
        self, **kwargs: Unpack[CreateRecordingConfigurationRequestTypeDef]
    ) -> CreateRecordingConfigurationResponseTypeDef:
        """
        Creates a new recording configuration, used to enable recording to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/create_recording_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#create_recording_configuration)
        """

    def create_stream_key(
        self, **kwargs: Unpack[CreateStreamKeyRequestTypeDef]
    ) -> CreateStreamKeyResponseTypeDef:
        """
        Creates a stream key, used to initiate a stream, for the specified channel ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/create_stream_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#create_stream_key)
        """

    def delete_channel(
        self, **kwargs: Unpack[DeleteChannelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified channel and its associated stream keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/delete_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#delete_channel)
        """

    def delete_playback_key_pair(
        self, **kwargs: Unpack[DeletePlaybackKeyPairRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified authorization key pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/delete_playback_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#delete_playback_key_pair)
        """

    def delete_playback_restriction_policy(
        self, **kwargs: Unpack[DeletePlaybackRestrictionPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified playback restriction policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/delete_playback_restriction_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#delete_playback_restriction_policy)
        """

    def delete_recording_configuration(
        self, **kwargs: Unpack[DeleteRecordingConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the recording configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/delete_recording_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#delete_recording_configuration)
        """

    def delete_stream_key(
        self, **kwargs: Unpack[DeleteStreamKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the stream key for the specified ARN, so it can no longer be used to
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/delete_stream_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#delete_stream_key)
        """

    def get_channel(self, **kwargs: Unpack[GetChannelRequestTypeDef]) -> GetChannelResponseTypeDef:
        """
        Gets the channel configuration for the specified channel ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_channel)
        """

    def get_playback_key_pair(
        self, **kwargs: Unpack[GetPlaybackKeyPairRequestTypeDef]
    ) -> GetPlaybackKeyPairResponseTypeDef:
        """
        Gets a specified playback authorization key pair and returns the
        <code>arn</code> and <code>fingerprint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_playback_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_playback_key_pair)
        """

    def get_playback_restriction_policy(
        self, **kwargs: Unpack[GetPlaybackRestrictionPolicyRequestTypeDef]
    ) -> GetPlaybackRestrictionPolicyResponseTypeDef:
        """
        Gets the specified playback restriction policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_playback_restriction_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_playback_restriction_policy)
        """

    def get_recording_configuration(
        self, **kwargs: Unpack[GetRecordingConfigurationRequestTypeDef]
    ) -> GetRecordingConfigurationResponseTypeDef:
        """
        Gets the recording configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_recording_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_recording_configuration)
        """

    def get_stream(self, **kwargs: Unpack[GetStreamRequestTypeDef]) -> GetStreamResponseTypeDef:
        """
        Gets information about the active (live) stream on a specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_stream)
        """

    def get_stream_key(
        self, **kwargs: Unpack[GetStreamKeyRequestTypeDef]
    ) -> GetStreamKeyResponseTypeDef:
        """
        Gets stream-key information for a specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_stream_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_stream_key)
        """

    def get_stream_session(
        self, **kwargs: Unpack[GetStreamSessionRequestTypeDef]
    ) -> GetStreamSessionResponseTypeDef:
        """
        Gets metadata on a specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_stream_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_stream_session)
        """

    def import_playback_key_pair(
        self, **kwargs: Unpack[ImportPlaybackKeyPairRequestTypeDef]
    ) -> ImportPlaybackKeyPairResponseTypeDef:
        """
        Imports the public portion of a new key pair and returns its <code>arn</code>
        and <code>fingerprint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/import_playback_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#import_playback_key_pair)
        """

    def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Gets summary information about all channels in your account, in the Amazon Web
        Services region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_channels)
        """

    def list_playback_key_pairs(
        self, **kwargs: Unpack[ListPlaybackKeyPairsRequestTypeDef]
    ) -> ListPlaybackKeyPairsResponseTypeDef:
        """
        Gets summary information about playback key pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_playback_key_pairs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_playback_key_pairs)
        """

    def list_playback_restriction_policies(
        self, **kwargs: Unpack[ListPlaybackRestrictionPoliciesRequestTypeDef]
    ) -> ListPlaybackRestrictionPoliciesResponseTypeDef:
        """
        Gets summary information about playback restriction policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_playback_restriction_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_playback_restriction_policies)
        """

    def list_recording_configurations(
        self, **kwargs: Unpack[ListRecordingConfigurationsRequestTypeDef]
    ) -> ListRecordingConfigurationsResponseTypeDef:
        """
        Gets summary information about all recording configurations in your account, in
        the Amazon Web Services region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_recording_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_recording_configurations)
        """

    def list_stream_keys(
        self, **kwargs: Unpack[ListStreamKeysRequestTypeDef]
    ) -> ListStreamKeysResponseTypeDef:
        """
        Gets summary information about stream keys for the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_stream_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_stream_keys)
        """

    def list_stream_sessions(
        self, **kwargs: Unpack[ListStreamSessionsRequestTypeDef]
    ) -> ListStreamSessionsResponseTypeDef:
        """
        Gets a summary of current and previous streams for a specified channel in your
        account, in the AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_stream_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_stream_sessions)
        """

    def list_streams(
        self, **kwargs: Unpack[ListStreamsRequestTypeDef]
    ) -> ListStreamsResponseTypeDef:
        """
        Gets summary information about live streams in your account, in the Amazon Web
        Services region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_streams)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about Amazon Web Services tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#list_tags_for_resource)
        """

    def put_metadata(
        self, **kwargs: Unpack[PutMetadataRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Inserts metadata into the active stream of the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/put_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#put_metadata)
        """

    def start_viewer_session_revocation(
        self, **kwargs: Unpack[StartViewerSessionRevocationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts the process of revoking the viewer session associated with a specified
        channel ARN and viewer ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/start_viewer_session_revocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#start_viewer_session_revocation)
        """

    def stop_stream(self, **kwargs: Unpack[StopStreamRequestTypeDef]) -> Dict[str, Any]:
        """
        Disconnects the incoming RTMPS stream for the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/stop_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#stop_stream)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for the Amazon Web Services resource with the specified
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#untag_resource)
        """

    def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/update_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#update_channel)
        """

    def update_playback_restriction_policy(
        self, **kwargs: Unpack[UpdatePlaybackRestrictionPolicyRequestTypeDef]
    ) -> UpdatePlaybackRestrictionPolicyResponseTypeDef:
        """
        Updates a specified playback restriction policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/update_playback_restriction_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#update_playback_restriction_policy)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_playback_key_pairs"]
    ) -> ListPlaybackKeyPairsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recording_configurations"]
    ) -> ListRecordingConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_keys"]
    ) -> ListStreamKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_streams"]
    ) -> ListStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/client/#get_paginator)
        """
