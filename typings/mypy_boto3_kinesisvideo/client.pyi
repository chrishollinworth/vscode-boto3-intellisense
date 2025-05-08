"""
Type annotations for kinesisvideo service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kinesisvideo.client import KinesisVideoClient

    session = Session()
    client: KinesisVideoClient = session.client("kinesisvideo")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeMappedResourceConfigurationPaginator,
    ListEdgeAgentConfigurationsPaginator,
    ListSignalingChannelsPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    CreateSignalingChannelInputTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamInputTypeDef,
    CreateStreamOutputTypeDef,
    DeleteEdgeConfigurationInputTypeDef,
    DeleteSignalingChannelInputTypeDef,
    DeleteStreamInputTypeDef,
    DescribeEdgeConfigurationInputTypeDef,
    DescribeEdgeConfigurationOutputTypeDef,
    DescribeImageGenerationConfigurationInputTypeDef,
    DescribeImageGenerationConfigurationOutputTypeDef,
    DescribeMappedResourceConfigurationInputTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    DescribeMediaStorageConfigurationInputTypeDef,
    DescribeMediaStorageConfigurationOutputTypeDef,
    DescribeNotificationConfigurationInputTypeDef,
    DescribeNotificationConfigurationOutputTypeDef,
    DescribeSignalingChannelInputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamInputTypeDef,
    DescribeStreamOutputTypeDef,
    GetDataEndpointInputTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointInputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ListEdgeAgentConfigurationsInputTypeDef,
    ListEdgeAgentConfigurationsOutputTypeDef,
    ListSignalingChannelsInputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsInputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamInputTypeDef,
    ListTagsForStreamOutputTypeDef,
    StartEdgeConfigurationUpdateInputTypeDef,
    StartEdgeConfigurationUpdateOutputTypeDef,
    TagResourceInputTypeDef,
    TagStreamInputTypeDef,
    UntagResourceInputTypeDef,
    UntagStreamInputTypeDef,
    UpdateDataRetentionInputTypeDef,
    UpdateImageGenerationConfigurationInputTypeDef,
    UpdateMediaStorageConfigurationInputTypeDef,
    UpdateNotificationConfigurationInputTypeDef,
    UpdateSignalingChannelInputTypeDef,
    UpdateStreamInputTypeDef,
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

__all__ = ("KinesisVideoClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    AccountChannelLimitExceededException: Type[BotocoreClientError]
    AccountStreamLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    DeviceStreamLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidDeviceException: Type[BotocoreClientError]
    InvalidResourceFormatException: Type[BotocoreClientError]
    NoDataRetentionException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    StreamEdgeConfigurationNotFoundException: Type[BotocoreClientError]
    TagsPerResourceExceededLimitException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]

class KinesisVideoClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#generate_presigned_url)
        """

    def create_signaling_channel(
        self, **kwargs: Unpack[CreateSignalingChannelInputTypeDef]
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        Creates a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/create_signaling_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#create_signaling_channel)
        """

    def create_stream(
        self, **kwargs: Unpack[CreateStreamInputTypeDef]
    ) -> CreateStreamOutputTypeDef:
        """
        Creates a new Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/create_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#create_stream)
        """

    def delete_edge_configuration(
        self, **kwargs: Unpack[DeleteEdgeConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        An asynchronous API that deletes a stream's existing edge configuration, as
        well as the corresponding media from the Edge Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/delete_edge_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#delete_edge_configuration)
        """

    def delete_signaling_channel(
        self, **kwargs: Unpack[DeleteSignalingChannelInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/delete_signaling_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#delete_signaling_channel)
        """

    def delete_stream(self, **kwargs: Unpack[DeleteStreamInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a Kinesis video stream and the data contained in the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/delete_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#delete_stream)
        """

    def describe_edge_configuration(
        self, **kwargs: Unpack[DescribeEdgeConfigurationInputTypeDef]
    ) -> DescribeEdgeConfigurationOutputTypeDef:
        """
        Describes a stream's edge configuration that was set using the
        <code>StartEdgeConfigurationUpdate</code> API and the latest status of the edge
        agent's recorder and uploader jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_edge_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_edge_configuration)
        """

    def describe_image_generation_configuration(
        self, **kwargs: Unpack[DescribeImageGenerationConfigurationInputTypeDef]
    ) -> DescribeImageGenerationConfigurationOutputTypeDef:
        """
        Gets the <code>ImageGenerationConfiguration</code> for a given Kinesis video
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_image_generation_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_image_generation_configuration)
        """

    def describe_mapped_resource_configuration(
        self, **kwargs: Unpack[DescribeMappedResourceConfigurationInputTypeDef]
    ) -> DescribeMappedResourceConfigurationOutputTypeDef:
        """
        Returns the most current information about the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_mapped_resource_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_mapped_resource_configuration)
        """

    def describe_media_storage_configuration(
        self, **kwargs: Unpack[DescribeMediaStorageConfigurationInputTypeDef]
    ) -> DescribeMediaStorageConfigurationOutputTypeDef:
        """
        Returns the most current information about the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_media_storage_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_media_storage_configuration)
        """

    def describe_notification_configuration(
        self, **kwargs: Unpack[DescribeNotificationConfigurationInputTypeDef]
    ) -> DescribeNotificationConfigurationOutputTypeDef:
        """
        Gets the <code>NotificationConfiguration</code> for a given Kinesis video
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_notification_configuration)
        """

    def describe_signaling_channel(
        self, **kwargs: Unpack[DescribeSignalingChannelInputTypeDef]
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        Returns the most current information about the signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_signaling_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_signaling_channel)
        """

    def describe_stream(
        self, **kwargs: Unpack[DescribeStreamInputTypeDef]
    ) -> DescribeStreamOutputTypeDef:
        """
        Returns the most current information about the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/describe_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#describe_stream)
        """

    def get_data_endpoint(
        self, **kwargs: Unpack[GetDataEndpointInputTypeDef]
    ) -> GetDataEndpointOutputTypeDef:
        """
        Gets an endpoint for a specified stream for either reading or writing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_data_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_data_endpoint)
        """

    def get_signaling_channel_endpoint(
        self, **kwargs: Unpack[GetSignalingChannelEndpointInputTypeDef]
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        Provides an endpoint for the specified signaling channel to send and receive
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_signaling_channel_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_signaling_channel_endpoint)
        """

    def list_edge_agent_configurations(
        self, **kwargs: Unpack[ListEdgeAgentConfigurationsInputTypeDef]
    ) -> ListEdgeAgentConfigurationsOutputTypeDef:
        """
        Returns an array of edge configurations associated with the specified Edge
        Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/list_edge_agent_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#list_edge_agent_configurations)
        """

    def list_signaling_channels(
        self, **kwargs: Unpack[ListSignalingChannelsInputTypeDef]
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        Returns an array of <code>ChannelInfo</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/list_signaling_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#list_signaling_channels)
        """

    def list_streams(self, **kwargs: Unpack[ListStreamsInputTypeDef]) -> ListStreamsOutputTypeDef:
        """
        Returns an array of <code>StreamInfo</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/list_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#list_streams)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#list_tags_for_resource)
        """

    def list_tags_for_stream(
        self, **kwargs: Unpack[ListTagsForStreamInputTypeDef]
    ) -> ListTagsForStreamOutputTypeDef:
        """
        Returns a list of tags associated with the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/list_tags_for_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#list_tags_for_stream)
        """

    def start_edge_configuration_update(
        self, **kwargs: Unpack[StartEdgeConfigurationUpdateInputTypeDef]
    ) -> StartEdgeConfigurationUpdateOutputTypeDef:
        """
        An asynchronous API that updates a stream's existing edge configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/start_edge_configuration_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#start_edge_configuration_update)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#tag_resource)
        """

    def tag_stream(self, **kwargs: Unpack[TagStreamInputTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/tag_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#tag_stream)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#untag_resource)
        """

    def untag_stream(self, **kwargs: Unpack[UntagStreamInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/untag_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#untag_stream)
        """

    def update_data_retention(
        self, **kwargs: Unpack[UpdateDataRetentionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Increases or decreases the stream's data retention period by the value that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_data_retention.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_data_retention)
        """

    def update_image_generation_configuration(
        self, **kwargs: Unpack[UpdateImageGenerationConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the <code>StreamInfo</code> and
        <code>ImageProcessingConfiguration</code> fields.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_image_generation_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_image_generation_configuration)
        """

    def update_media_storage_configuration(
        self, **kwargs: Unpack[UpdateMediaStorageConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a <code>SignalingChannel</code> to a stream to store the media.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_media_storage_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_media_storage_configuration)
        """

    def update_notification_configuration(
        self, **kwargs: Unpack[UpdateNotificationConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the notification information for a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_notification_configuration)
        """

    def update_signaling_channel(
        self, **kwargs: Unpack[UpdateSignalingChannelInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the existing signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_signaling_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_signaling_channel)
        """

    def update_stream(self, **kwargs: Unpack[UpdateStreamInputTypeDef]) -> Dict[str, Any]:
        """
        Updates stream metadata, such as the device name and media type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/update_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#update_stream)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_mapped_resource_configuration"]
    ) -> DescribeMappedResourceConfigurationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_edge_agent_configurations"]
    ) -> ListEdgeAgentConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signaling_channels"]
    ) -> ListSignalingChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_streams"]
    ) -> ListStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client/#get_paginator)
        """
