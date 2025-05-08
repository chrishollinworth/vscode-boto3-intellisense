"""
Type annotations for mediapackagev2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackagev2.client import Mediapackagev2Client

    session = Session()
    client: Mediapackagev2Client = session.client("mediapackagev2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListHarvestJobsPaginator,
    ListOriginEndpointsPaginator,
)
from .type_defs import (
    CancelHarvestJobRequestTypeDef,
    CreateChannelGroupRequestTypeDef,
    CreateChannelGroupResponseTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateHarvestJobRequestTypeDef,
    CreateHarvestJobResponseTypeDef,
    CreateOriginEndpointRequestTypeDef,
    CreateOriginEndpointResponseTypeDef,
    DeleteChannelGroupRequestTypeDef,
    DeleteChannelPolicyRequestTypeDef,
    DeleteChannelRequestTypeDef,
    DeleteOriginEndpointPolicyRequestTypeDef,
    DeleteOriginEndpointRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChannelGroupRequestTypeDef,
    GetChannelGroupResponseTypeDef,
    GetChannelPolicyRequestTypeDef,
    GetChannelPolicyResponseTypeDef,
    GetChannelRequestTypeDef,
    GetChannelResponseTypeDef,
    GetHarvestJobRequestTypeDef,
    GetHarvestJobResponseTypeDef,
    GetOriginEndpointPolicyRequestTypeDef,
    GetOriginEndpointPolicyResponseTypeDef,
    GetOriginEndpointRequestTypeDef,
    GetOriginEndpointResponseTypeDef,
    ListChannelGroupsRequestTypeDef,
    ListChannelGroupsResponseTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListHarvestJobsRequestTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsRequestTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutChannelPolicyRequestTypeDef,
    PutOriginEndpointPolicyRequestTypeDef,
    ResetChannelStateRequestTypeDef,
    ResetChannelStateResponseTypeDef,
    ResetOriginEndpointStateRequestTypeDef,
    ResetOriginEndpointStateResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateChannelGroupRequestTypeDef,
    UpdateChannelGroupResponseTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointRequestTypeDef,
    UpdateOriginEndpointResponseTypeDef,
)
from .waiter import HarvestJobFinishedWaiter

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

__all__ = ("Mediapackagev2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Mediapackagev2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Mediapackagev2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#generate_presigned_url)
        """

    def cancel_harvest_job(
        self, **kwargs: Unpack[CancelHarvestJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an in-progress harvest job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/cancel_harvest_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#cancel_harvest_job)
        """

    def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Create a channel to start receiving content streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/create_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_channel)
        """

    def create_channel_group(
        self, **kwargs: Unpack[CreateChannelGroupRequestTypeDef]
    ) -> CreateChannelGroupResponseTypeDef:
        """
        Create a channel group to group your channels and origin endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/create_channel_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_channel_group)
        """

    def create_harvest_job(
        self, **kwargs: Unpack[CreateHarvestJobRequestTypeDef]
    ) -> CreateHarvestJobResponseTypeDef:
        """
        Creates a new harvest job to export content from a MediaPackage v2 channel to
        an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/create_harvest_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_harvest_job)
        """

    def create_origin_endpoint(
        self, **kwargs: Unpack[CreateOriginEndpointRequestTypeDef]
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        The endpoint is attached to a channel, and represents the output of the live
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/create_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_origin_endpoint)
        """

    def delete_channel(self, **kwargs: Unpack[DeleteChannelRequestTypeDef]) -> Dict[str, Any]:
        """
        Delete a channel to stop AWS Elemental MediaPackage from receiving further
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/delete_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel)
        """

    def delete_channel_group(
        self, **kwargs: Unpack[DeleteChannelGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/delete_channel_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel_group)
        """

    def delete_channel_policy(
        self, **kwargs: Unpack[DeleteChannelPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a channel policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/delete_channel_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel_policy)
        """

    def delete_origin_endpoint(
        self, **kwargs: Unpack[DeleteOriginEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Origin endpoints can serve content until they're deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/delete_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_origin_endpoint)
        """

    def delete_origin_endpoint_policy(
        self, **kwargs: Unpack[DeleteOriginEndpointPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete an origin endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/delete_origin_endpoint_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_origin_endpoint_policy)
        """

    def get_channel(self, **kwargs: Unpack[GetChannelRequestTypeDef]) -> GetChannelResponseTypeDef:
        """
        Retrieves the specified channel that's configured in AWS Elemental
        MediaPackage, including the origin endpoints that are associated with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel)
        """

    def get_channel_group(
        self, **kwargs: Unpack[GetChannelGroupRequestTypeDef]
    ) -> GetChannelGroupResponseTypeDef:
        """
        Retrieves the specified channel group that's configured in AWS Elemental
        MediaPackage, including the channels and origin endpoints that are associated
        with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_channel_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel_group)
        """

    def get_channel_policy(
        self, **kwargs: Unpack[GetChannelPolicyRequestTypeDef]
    ) -> GetChannelPolicyResponseTypeDef:
        """
        Retrieves the specified channel policy that's configured in AWS Elemental
        MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_channel_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel_policy)
        """

    def get_harvest_job(
        self, **kwargs: Unpack[GetHarvestJobRequestTypeDef]
    ) -> GetHarvestJobResponseTypeDef:
        """
        Retrieves the details of a specific harvest job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_harvest_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_harvest_job)
        """

    def get_origin_endpoint(
        self, **kwargs: Unpack[GetOriginEndpointRequestTypeDef]
    ) -> GetOriginEndpointResponseTypeDef:
        """
        Retrieves the specified origin endpoint that's configured in AWS Elemental
        MediaPackage to obtain its playback URL and to view the packaging settings that
        it's currently using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_origin_endpoint)
        """

    def get_origin_endpoint_policy(
        self, **kwargs: Unpack[GetOriginEndpointPolicyRequestTypeDef]
    ) -> GetOriginEndpointPolicyResponseTypeDef:
        """
        Retrieves the specified origin endpoint policy that's configured in AWS
        Elemental MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_origin_endpoint_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_origin_endpoint_policy)
        """

    def list_channel_groups(
        self, **kwargs: Unpack[ListChannelGroupsRequestTypeDef]
    ) -> ListChannelGroupsResponseTypeDef:
        """
        Retrieves all channel groups that are configured in Elemental MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/list_channel_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_channel_groups)
        """

    def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves all channels in a specific channel group that are configured in AWS
        Elemental MediaPackage, including the origin endpoints that are associated with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/list_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_channels)
        """

    def list_harvest_jobs(
        self, **kwargs: Unpack[ListHarvestJobsRequestTypeDef]
    ) -> ListHarvestJobsResponseTypeDef:
        """
        Retrieves a list of harvest jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/list_harvest_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_harvest_jobs)
        """

    def list_origin_endpoints(
        self, **kwargs: Unpack[ListOriginEndpointsRequestTypeDef]
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        Retrieves all origin endpoints in a specific channel that are configured in AWS
        Elemental MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/list_origin_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_origin_endpoints)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_tags_for_resource)
        """

    def put_channel_policy(
        self, **kwargs: Unpack[PutChannelPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/put_channel_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#put_channel_policy)
        """

    def put_origin_endpoint_policy(
        self, **kwargs: Unpack[PutOriginEndpointPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/put_origin_endpoint_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#put_origin_endpoint_policy)
        """

    def reset_channel_state(
        self, **kwargs: Unpack[ResetChannelStateRequestTypeDef]
    ) -> ResetChannelStateResponseTypeDef:
        """
        Resetting the channel can help to clear errors from misconfigurations in the
        encoder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/reset_channel_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#reset_channel_state)
        """

    def reset_origin_endpoint_state(
        self, **kwargs: Unpack[ResetOriginEndpointStateRequestTypeDef]
    ) -> ResetOriginEndpointStateResponseTypeDef:
        """
        Resetting the origin endpoint can help to resolve unexpected behavior and other
        content packaging issues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/reset_origin_endpoint_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#reset_origin_endpoint_state)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns one of more tags (key-value pairs) to the specified MediaPackage
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#untag_resource)
        """

    def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Update the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/update_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_channel)
        """

    def update_channel_group(
        self, **kwargs: Unpack[UpdateChannelGroupRequestTypeDef]
    ) -> UpdateChannelGroupResponseTypeDef:
        """
        Update the specified channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/update_channel_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_channel_group)
        """

    def update_origin_endpoint(
        self, **kwargs: Unpack[UpdateOriginEndpointRequestTypeDef]
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        Update the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/update_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_origin_endpoint)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channel_groups"]
    ) -> ListChannelGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_harvest_jobs"]
    ) -> ListHarvestJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["harvest_job_finished"]
    ) -> HarvestJobFinishedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_waiter)
        """
