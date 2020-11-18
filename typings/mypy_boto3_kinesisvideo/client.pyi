# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesisvideo service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisvideo import KinesisVideoClient

    client: KinesisVideoClient = boto3.client("kinesisvideo")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_kinesisvideo.paginator import ListSignalingChannelsPaginator, ListStreamsPaginator
from mypy_boto3_kinesisvideo.type_defs import (
    ChannelNameConditionTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamOutputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamOutputTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    SingleMasterChannelEndpointConfigurationTypeDef,
    SingleMasterConfigurationTypeDef,
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
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagsPerResourceExceededLimitException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]


class KinesisVideoClient:
    """
    [KinesisVideo.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)
        """

    def create_signaling_channel(
        self,
        ChannelName: str,
        ChannelType: Literal["SINGLE_MASTER"] = None,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        [Client.create_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)
        """

    def create_stream(
        self,
        StreamName: str,
        DeviceName: str = None,
        MediaType: str = None,
        KmsKeyId: str = None,
        DataRetentionInHours: int = None,
        Tags: Dict[str, str] = None,
    ) -> CreateStreamOutputTypeDef:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)
        """

    def delete_signaling_channel(
        self, ChannelARN: str, CurrentVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)
        """

    def delete_stream(self, StreamARN: str, CurrentVersion: str = None) -> Dict[str, Any]:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)
        """

    def describe_signaling_channel(
        self, ChannelName: str = None, ChannelARN: str = None
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        [Client.describe_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)
        """

    def describe_stream(
        self, StreamName: str = None, StreamARN: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)
        """

    def get_data_endpoint(
        self,
        APIName: Literal[
            "PUT_MEDIA",
            "GET_MEDIA",
            "LIST_FRAGMENTS",
            "GET_MEDIA_FOR_FRAGMENT_LIST",
            "GET_HLS_STREAMING_SESSION_URL",
            "GET_DASH_STREAMING_SESSION_URL",
            "GET_CLIP",
        ],
        StreamName: str = None,
        StreamARN: str = None,
    ) -> GetDataEndpointOutputTypeDef:
        """
        [Client.get_data_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)
        """

    def get_signaling_channel_endpoint(
        self,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: SingleMasterChannelEndpointConfigurationTypeDef = None,
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        [Client.get_signaling_channel_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)
        """

    def list_signaling_channels(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        [Client.list_signaling_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)
        """

    def list_streams(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        StreamNameCondition: StreamNameConditionTypeDef = None,
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)
        """

    def list_tags_for_stream(
        self, NextToken: str = None, StreamARN: str = None, StreamName: str = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        [Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)
        """

    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)
        """

    def tag_stream(
        self, Tags: Dict[str, str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.tag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)
        """

    def untag_resource(self, ResourceARN: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)
        """

    def untag_stream(
        self, TagKeyList: List[str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.untag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)
        """

    def update_data_retention(
        self,
        CurrentVersion: str,
        Operation: Literal["INCREASE_DATA_RETENTION", "DECREASE_DATA_RETENTION"],
        DataRetentionChangeInHours: int,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_data_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)
        """

    def update_signaling_channel(
        self,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)
        """

    def update_stream(
        self,
        CurrentVersion: str,
        StreamName: str = None,
        StreamARN: str = None,
        DeviceName: str = None,
        MediaType: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signaling_channels"]
    ) -> ListSignalingChannelsPaginator:
        """
        [Paginator.ListSignalingChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
        """
