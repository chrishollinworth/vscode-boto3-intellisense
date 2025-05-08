"""
Type annotations for mediapackage service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackage.client import MediaPackageClient

    session = Session()
    client: MediaPackageClient = session.client("mediapackage")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListChannelsPaginator, ListHarvestJobsPaginator, ListOriginEndpointsPaginator
from .type_defs import (
    ConfigureLogsRequestTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateHarvestJobRequestTypeDef,
    CreateHarvestJobResponseTypeDef,
    CreateOriginEndpointRequestTypeDef,
    CreateOriginEndpointResponseTypeDef,
    DeleteChannelRequestTypeDef,
    DeleteOriginEndpointRequestTypeDef,
    DescribeChannelRequestTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeHarvestJobRequestTypeDef,
    DescribeHarvestJobResponseTypeDef,
    DescribeOriginEndpointRequestTypeDef,
    DescribeOriginEndpointResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListHarvestJobsRequestTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsRequestTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RotateChannelCredentialsRequestTypeDef,
    RotateChannelCredentialsResponseTypeDef,
    RotateIngestEndpointCredentialsRequestTypeDef,
    RotateIngestEndpointCredentialsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointRequestTypeDef,
    UpdateOriginEndpointResponseTypeDef,
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

__all__ = ("MediaPackageClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class MediaPackageClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaPackageClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#generate_presigned_url)
        """

    def configure_logs(
        self, **kwargs: Unpack[ConfigureLogsRequestTypeDef]
    ) -> ConfigureLogsResponseTypeDef:
        """
        Changes the Channel's properities to configure log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/configure_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#configure_logs)
        """

    def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/create_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#create_channel)
        """

    def create_harvest_job(
        self, **kwargs: Unpack[CreateHarvestJobRequestTypeDef]
    ) -> CreateHarvestJobResponseTypeDef:
        """
        Creates a new HarvestJob record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/create_harvest_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#create_harvest_job)
        """

    def create_origin_endpoint(
        self, **kwargs: Unpack[CreateOriginEndpointRequestTypeDef]
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        Creates a new OriginEndpoint record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/create_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#create_origin_endpoint)
        """

    def delete_channel(self, **kwargs: Unpack[DeleteChannelRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an existing Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/delete_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#delete_channel)
        """

    def delete_origin_endpoint(
        self, **kwargs: Unpack[DeleteOriginEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/delete_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#delete_origin_endpoint)
        """

    def describe_channel(
        self, **kwargs: Unpack[DescribeChannelRequestTypeDef]
    ) -> DescribeChannelResponseTypeDef:
        """
        Gets details about a Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/describe_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#describe_channel)
        """

    def describe_harvest_job(
        self, **kwargs: Unpack[DescribeHarvestJobRequestTypeDef]
    ) -> DescribeHarvestJobResponseTypeDef:
        """
        Gets details about an existing HarvestJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/describe_harvest_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#describe_harvest_job)
        """

    def describe_origin_endpoint(
        self, **kwargs: Unpack[DescribeOriginEndpointRequestTypeDef]
    ) -> DescribeOriginEndpointResponseTypeDef:
        """
        Gets details about an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/describe_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#describe_origin_endpoint)
        """

    def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Returns a collection of Channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/list_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#list_channels)
        """

    def list_harvest_jobs(
        self, **kwargs: Unpack[ListHarvestJobsRequestTypeDef]
    ) -> ListHarvestJobsResponseTypeDef:
        """
        Returns a collection of HarvestJob records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/list_harvest_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#list_harvest_jobs)
        """

    def list_origin_endpoints(
        self, **kwargs: Unpack[ListOriginEndpointsRequestTypeDef]
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        Returns a collection of OriginEndpoint records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/list_origin_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#list_origin_endpoints)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#list_tags_for_resource)
        """

    def rotate_channel_credentials(
        self, **kwargs: Unpack[RotateChannelCredentialsRequestTypeDef]
    ) -> RotateChannelCredentialsResponseTypeDef:
        """
        Changes the Channel's first IngestEndpoint's username and password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/rotate_channel_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#rotate_channel_credentials)
        """

    def rotate_ingest_endpoint_credentials(
        self, **kwargs: Unpack[RotateIngestEndpointCredentialsRequestTypeDef]
    ) -> RotateIngestEndpointCredentialsResponseTypeDef:
        """
        Rotate the IngestEndpoint's username and password, as specified by the
        IngestEndpoint's id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/rotate_ingest_endpoint_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#rotate_ingest_endpoint_credentials)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#untag_resource)
        """

    def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates an existing Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/update_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#update_channel)
        """

    def update_origin_endpoint(
        self, **kwargs: Unpack[UpdateOriginEndpointRequestTypeDef]
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        Updates an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/update_origin_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#update_origin_endpoint)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_harvest_jobs"]
    ) -> ListHarvestJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client/#get_paginator)
        """
