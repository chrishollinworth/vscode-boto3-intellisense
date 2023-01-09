"""
Type annotations for kinesisvideo service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisvideo import KinesisVideoClient

    client: KinesisVideoClient = boto3.client("kinesisvideo")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import APINameType, ChannelTypeType, UpdateDataRetentionOperationType
from .paginator import (
    DescribeMappedResourceConfigurationPaginator,
    ListSignalingChannelsPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    ChannelNameConditionTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamOutputTypeDef,
    DescribeEdgeConfigurationOutputTypeDef,
    DescribeImageGenerationConfigurationOutputTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    DescribeMediaStorageConfigurationOutputTypeDef,
    DescribeNotificationConfigurationOutputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamOutputTypeDef,
    EdgeConfigTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ImageGenerationConfigurationTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    MediaStorageConfigurationTypeDef,
    NotificationConfigurationTypeDef,
    SingleMasterChannelEndpointConfigurationTypeDef,
    SingleMasterConfigurationTypeDef,
    StartEdgeConfigurationUpdateOutputTypeDef,
    StreamNameConditionTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KinesisVideoClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#close)
        """
    def create_signaling_channel(
        self,
        *,
        ChannelName: str,
        ChannelType: ChannelTypeType = None,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        Creates a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#create_signaling_channel)
        """
    def create_stream(
        self,
        *,
        StreamName: str,
        DeviceName: str = None,
        MediaType: str = None,
        KmsKeyId: str = None,
        DataRetentionInHours: int = None,
        Tags: Dict[str, str] = None
    ) -> CreateStreamOutputTypeDef:
        """
        Creates a new Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#create_stream)
        """
    def delete_signaling_channel(
        self, *, ChannelARN: str, CurrentVersion: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#delete_signaling_channel)
        """
    def delete_stream(self, *, StreamARN: str, CurrentVersion: str = None) -> Dict[str, Any]:
        """
        Deletes a Kinesis video stream and the data contained in the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#delete_stream)
        """
    def describe_edge_configuration(
        self, *, StreamName: str = None, StreamARN: str = None
    ) -> DescribeEdgeConfigurationOutputTypeDef:
        """
        Describes a stream’s edge configuration that was set using the
        `StartEdgeConfigurationUpdate` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_edge_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_edge_configuration)
        """
    def describe_image_generation_configuration(
        self, *, StreamName: str = None, StreamARN: str = None
    ) -> DescribeImageGenerationConfigurationOutputTypeDef:
        """
        Gets the `ImageGenerationConfiguration` for a given Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_image_generation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_image_generation_configuration)
        """
    def describe_mapped_resource_configuration(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMappedResourceConfigurationOutputTypeDef:
        """
        Returns the most current information about the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_mapped_resource_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_mapped_resource_configuration)
        """
    def describe_media_storage_configuration(
        self, *, ChannelName: str = None, ChannelARN: str = None
    ) -> DescribeMediaStorageConfigurationOutputTypeDef:
        """
        Returns the most current information about the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_media_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_media_storage_configuration)
        """
    def describe_notification_configuration(
        self, *, StreamName: str = None, StreamARN: str = None
    ) -> DescribeNotificationConfigurationOutputTypeDef:
        """
        Gets the `NotificationConfiguration` for a given Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_notification_configuration)
        """
    def describe_signaling_channel(
        self, *, ChannelName: str = None, ChannelARN: str = None
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        Returns the most current information about the signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_signaling_channel)
        """
    def describe_stream(
        self, *, StreamName: str = None, StreamARN: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        Returns the most current information about the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe_stream)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#generate_presigned_url)
        """
    def get_data_endpoint(
        self, *, APIName: APINameType, StreamName: str = None, StreamARN: str = None
    ) -> GetDataEndpointOutputTypeDef:
        """
        Gets an endpoint for a specified stream for either reading or writing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#get_data_endpoint)
        """
    def get_signaling_channel_endpoint(
        self,
        *,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: "SingleMasterChannelEndpointConfigurationTypeDef" = None
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        Provides an endpoint for the specified signaling channel to send and receive
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#get_signaling_channel_endpoint)
        """
    def list_signaling_channels(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        ChannelNameCondition: "ChannelNameConditionTypeDef" = None
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        Returns an array of `ChannelInfo` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list_signaling_channels)
        """
    def list_streams(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        StreamNameCondition: "StreamNameConditionTypeDef" = None
    ) -> ListStreamsOutputTypeDef:
        """
        Returns an array of `StreamInfo` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list_streams)
        """
    def list_tags_for_resource(
        self, *, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list_tags_for_resource)
        """
    def list_tags_for_stream(
        self, *, NextToken: str = None, StreamARN: str = None, StreamName: str = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        Returns a list of tags associated with the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list_tags_for_stream)
        """
    def start_edge_configuration_update(
        self, *, EdgeConfig: "EdgeConfigTypeDef", StreamName: str = None, StreamARN: str = None
    ) -> StartEdgeConfigurationUpdateOutputTypeDef:
        """
        An asynchronous API that updates a stream’s existing edge configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.start_edge_configuration_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#start_edge_configuration_update)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more tags to a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#tag_resource)
        """
    def tag_stream(
        self, *, Tags: Dict[str, str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        Adds one or more tags to a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#tag_stream)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#untag_resource)
        """
    def untag_stream(
        self, *, TagKeyList: List[str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        Removes one or more tags from a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#untag_stream)
        """
    def update_data_retention(
        self,
        *,
        CurrentVersion: str,
        Operation: UpdateDataRetentionOperationType,
        DataRetentionChangeInHours: int,
        StreamName: str = None,
        StreamARN: str = None
    ) -> Dict[str, Any]:
        """
        Increases or decreases the stream's data retention period by the value that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_data_retention)
        """
    def update_image_generation_configuration(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        ImageGenerationConfiguration: "ImageGenerationConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the `StreamInfo` and `ImageProcessingConfiguration` fields.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_image_generation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_image_generation_configuration)
        """
    def update_media_storage_configuration(
        self, *, ChannelARN: str, MediaStorageConfiguration: "MediaStorageConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Associates a `SignalingChannel` to a stream to store the media.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_media_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_media_storage_configuration)
        """
    def update_notification_configuration(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the notification information for a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_notification_configuration)
        """
    def update_signaling_channel(
        self,
        *,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the existing signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_signaling_channel)
        """
    def update_stream(
        self,
        *,
        CurrentVersion: str,
        StreamName: str = None,
        StreamARN: str = None,
        DeviceName: str = None,
        MediaType: str = None
    ) -> Dict[str, Any]:
        """
        Updates stream metadata, such as the device name and media type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update_stream)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mapped_resource_configuration"]
    ) -> DescribeMappedResourceConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#describemappedresourceconfigurationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_signaling_channels"]
    ) -> ListSignalingChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listsignalingchannelspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#liststreamspaginator)
        """
