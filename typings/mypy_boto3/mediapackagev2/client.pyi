"""
Type annotations for mediapackagev2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackagev2 import mediapackagev2Client

    client: mediapackagev2Client = boto3.client("mediapackagev2")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ContainerTypeType
from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListOriginEndpointsPaginator,
)
from .type_defs import (
    CreateChannelGroupResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateDashManifestConfigurationTypeDef,
    CreateHlsManifestConfigurationTypeDef,
    CreateLowLatencyHlsManifestConfigurationTypeDef,
    CreateOriginEndpointResponseTypeDef,
    GetChannelGroupResponseTypeDef,
    GetChannelPolicyResponseTypeDef,
    GetChannelResponseTypeDef,
    GetOriginEndpointPolicyResponseTypeDef,
    GetOriginEndpointResponseTypeDef,
    ListChannelGroupsResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SegmentTypeDef,
    UpdateChannelGroupResponseTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("mediapackagev2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class mediapackagev2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        mediapackagev2Client exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#close)
        """

    def create_channel(
        self,
        *,
        ChannelGroupName: str,
        ChannelName: str,
        ClientToken: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateChannelResponseTypeDef:
        """
        Create a channel to start receiving content streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#create_channel)
        """

    def create_channel_group(
        self,
        *,
        ChannelGroupName: str,
        ClientToken: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateChannelGroupResponseTypeDef:
        """
        Create a channel group to group your channels and origin endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.create_channel_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#create_channel_group)
        """

    def create_origin_endpoint(
        self,
        *,
        ChannelGroupName: str,
        ChannelName: str,
        OriginEndpointName: str,
        ContainerType: ContainerTypeType,
        Segment: "SegmentTypeDef" = None,
        ClientToken: str = None,
        Description: str = None,
        StartoverWindowSeconds: int = None,
        HlsManifests: List["CreateHlsManifestConfigurationTypeDef"] = None,
        LowLatencyHlsManifests: List["CreateLowLatencyHlsManifestConfigurationTypeDef"] = None,
        DashManifests: List["CreateDashManifestConfigurationTypeDef"] = None,
        Tags: Dict[str, str] = None
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        The endpoint is attached to a channel, and represents the output of the live
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.create_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#create_origin_endpoint)
        """

    def delete_channel(self, *, ChannelGroupName: str, ChannelName: str) -> Dict[str, Any]:
        """
        Delete a channel to stop AWS Elemental MediaPackage from receiving further
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#delete_channel)
        """

    def delete_channel_group(self, *, ChannelGroupName: str) -> Dict[str, Any]:
        """
        Delete a channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.delete_channel_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#delete_channel_group)
        """

    def delete_channel_policy(self, *, ChannelGroupName: str, ChannelName: str) -> Dict[str, Any]:
        """
        Delete a channel policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.delete_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#delete_channel_policy)
        """

    def delete_origin_endpoint(
        self, *, ChannelGroupName: str, ChannelName: str, OriginEndpointName: str
    ) -> Dict[str, Any]:
        """
        Origin endpoints can serve content until they're deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.delete_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#delete_origin_endpoint)
        """

    def delete_origin_endpoint_policy(
        self, *, ChannelGroupName: str, ChannelName: str, OriginEndpointName: str
    ) -> Dict[str, Any]:
        """
        Delete an origin endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.delete_origin_endpoint_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#delete_origin_endpoint_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#generate_presigned_url)
        """

    def get_channel(self, *, ChannelGroupName: str, ChannelName: str) -> GetChannelResponseTypeDef:
        """
        Retrieves the specified channel that's configured in AWS Elemental MediaPackage,
        including the origin endpoints that are associated with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.get_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#get_channel)
        """

    def get_channel_group(self, *, ChannelGroupName: str) -> GetChannelGroupResponseTypeDef:
        """
        Retrieves the specified channel group that's configured in AWS Elemental
        MediaPackage, including the channels and origin endpoints that are associated
        with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.get_channel_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#get_channel_group)
        """

    def get_channel_policy(
        self, *, ChannelGroupName: str, ChannelName: str
    ) -> GetChannelPolicyResponseTypeDef:
        """
        Retrieves the specified channel policy that's configured in AWS Elemental
        MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.get_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#get_channel_policy)
        """

    def get_origin_endpoint(
        self, *, ChannelGroupName: str, ChannelName: str, OriginEndpointName: str
    ) -> GetOriginEndpointResponseTypeDef:
        """
        Retrieves the specified origin endpoint that's configured in AWS Elemental
        MediaPackage to obtain its playback URL and to view the packaging settings that
        it's currently using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.get_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#get_origin_endpoint)
        """

    def get_origin_endpoint_policy(
        self, *, ChannelGroupName: str, ChannelName: str, OriginEndpointName: str
    ) -> GetOriginEndpointPolicyResponseTypeDef:
        """
        Retrieves the specified origin endpoint policy that's configured in AWS
        Elemental MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.get_origin_endpoint_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#get_origin_endpoint_policy)
        """

    def list_channel_groups(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelGroupsResponseTypeDef:
        """
        Retrieves all channel groups that are configured in AWS Elemental MediaPackage,
        including the channels and origin endpoints that are associated with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.list_channel_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#list_channel_groups)
        """

    def list_channels(
        self, *, ChannelGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves all channels in a specific channel group that are configured in AWS
        Elemental MediaPackage, including the origin endpoints that are associated with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#list_channels)
        """

    def list_origin_endpoints(
        self,
        *,
        ChannelGroupName: str,
        ChannelName: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        Retrieves all origin endpoints in a specific channel that are configured in AWS
        Elemental MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.list_origin_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#list_origin_endpoints)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#list_tags_for_resource)
        """

    def put_channel_policy(
        self, *, ChannelGroupName: str, ChannelName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.put_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#put_channel_policy)
        """

    def put_origin_endpoint_policy(
        self, *, ChannelGroupName: str, ChannelName: str, OriginEndpointName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.put_origin_endpoint_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#put_origin_endpoint_policy)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Assigns one of more tags (key-value pairs) to the specified MediaPackage
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#untag_resource)
        """

    def update_channel(
        self, *, ChannelGroupName: str, ChannelName: str, ETag: str = None, Description: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        Update the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#update_channel)
        """

    def update_channel_group(
        self, *, ChannelGroupName: str, ETag: str = None, Description: str = None
    ) -> UpdateChannelGroupResponseTypeDef:
        """
        Update the specified channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.update_channel_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#update_channel_group)
        """

    def update_origin_endpoint(
        self,
        *,
        ChannelGroupName: str,
        ChannelName: str,
        OriginEndpointName: str,
        ContainerType: ContainerTypeType,
        Segment: "SegmentTypeDef" = None,
        Description: str = None,
        StartoverWindowSeconds: int = None,
        HlsManifests: List["CreateHlsManifestConfigurationTypeDef"] = None,
        LowLatencyHlsManifests: List["CreateLowLatencyHlsManifestConfigurationTypeDef"] = None,
        DashManifests: List["CreateDashManifestConfigurationTypeDef"] = None,
        ETag: str = None
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        Update the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Client.update_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client.html#update_origin_endpoint)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_channel_groups"]
    ) -> ListChannelGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannelGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelgroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListOriginEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listoriginendpointspaginator)
        """
