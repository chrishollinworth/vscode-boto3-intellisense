"""
Type annotations for mediapackage service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage import MediaPackageClient

    client: MediaPackageClient = boto3.client("mediapackage")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import OriginationType
from .paginator import ListChannelsPaginator, ListHarvestJobsPaginator, ListOriginEndpointsPaginator
from .type_defs import (
    AuthorizationTypeDef,
    CmafPackageCreateOrUpdateParametersTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateHarvestJobResponseTypeDef,
    CreateOriginEndpointResponseTypeDef,
    DashPackageTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeHarvestJobResponseTypeDef,
    DescribeOriginEndpointResponseTypeDef,
    EgressAccessLogsTypeDef,
    HlsPackageTypeDef,
    IngressAccessLogsTypeDef,
    ListChannelsResponseTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MssPackageTypeDef,
    RotateChannelCredentialsResponseTypeDef,
    RotateIngestEndpointCredentialsResponseTypeDef,
    S3DestinationTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MediaPackageClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class MediaPackageClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaPackageClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#close)
        """
    def configure_logs(
        self,
        *,
        Id: str,
        EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
        IngressAccessLogs: "IngressAccessLogsTypeDef" = None
    ) -> ConfigureLogsResponseTypeDef:
        """
        Changes the Channel's properities to configure log subscription See also: `AWS
        API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-2017-10-
        12/ConfigureLogs>`_ **Request Syntax** response = client.configure_logs(
        EgressAccessLogs={ 'LogGroupName': 'str...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.configure_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#configure_logs)
        """
    def create_channel(
        self, *, Id: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_channel)
        """
    def create_harvest_job(
        self,
        *,
        EndTime: str,
        Id: str,
        OriginEndpointId: str,
        S3Destination: "S3DestinationTypeDef",
        StartTime: str
    ) -> CreateHarvestJobResponseTypeDef:
        """
        Creates a new HarvestJob record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.create_harvest_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_harvest_job)
        """
    def create_origin_endpoint(
        self,
        *,
        ChannelId: str,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        CmafPackage: "CmafPackageCreateOrUpdateParametersTypeDef" = None,
        DashPackage: "DashPackageTypeDef" = None,
        Description: str = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        ManifestName: str = None,
        MssPackage: "MssPackageTypeDef" = None,
        Origination: OriginationType = None,
        StartoverWindowSeconds: int = None,
        Tags: Dict[str, str] = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        Creates a new OriginEndpoint record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.create_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_origin_endpoint)
        """
    def delete_channel(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes an existing Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#delete_channel)
        """
    def delete_origin_endpoint(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.delete_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#delete_origin_endpoint)
        """
    def describe_channel(self, *, Id: str) -> DescribeChannelResponseTypeDef:
        """
        Gets details about a Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_channel)
        """
    def describe_harvest_job(self, *, Id: str) -> DescribeHarvestJobResponseTypeDef:
        """
        Gets details about an existing HarvestJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.describe_harvest_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_harvest_job)
        """
    def describe_origin_endpoint(self, *, Id: str) -> DescribeOriginEndpointResponseTypeDef:
        """
        Gets details about an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.describe_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_origin_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#generate_presigned_url)
        """
    def list_channels(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Returns a collection of Channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_channels)
        """
    def list_harvest_jobs(
        self,
        *,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListHarvestJobsResponseTypeDef:
        """
        Returns a collection of HarvestJob records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.list_harvest_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_harvest_jobs)
        """
    def list_origin_endpoints(
        self, *, ChannelId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        Returns a collection of OriginEndpoint records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.list_origin_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_origin_endpoints)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediap
        ackage-2017-10-12/ListTagsForResource>`_ **Request Syntax** response =
        client.list_tags_for_resource( ResourceArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_tags_for_resource)
        """
    def rotate_channel_credentials(self, *, Id: str) -> RotateChannelCredentialsResponseTypeDef:
        """
        Changes the Channel's first IngestEndpoint's username and password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.rotate_channel_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#rotate_channel_credentials)
        """
    def rotate_ingest_endpoint_credentials(
        self, *, Id: str, IngestEndpointId: str
    ) -> RotateIngestEndpointCredentialsResponseTypeDef:
        """
        Rotate the IngestEndpoint's username and password, as specified by the
        IngestEndpoint's id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.rotate_ingest_endpoint_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#rotate_ingest_endpoint_credentials)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-2017-10-12/TagResource>`_
        **Request Syntax** response = client.tag_resource( ResourceArn='string', Tags={
        'string': 'string' } ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediap
        ackage-2017-10-12/UntagResource>`_ **Request Syntax** response =
        client.untag_resource( ResourceArn='string', TagKeys=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#untag_resource)
        """
    def update_channel(self, *, Id: str, Description: str = None) -> UpdateChannelResponseTypeDef:
        """
        Updates an existing Channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#update_channel)
        """
    def update_origin_endpoint(
        self,
        *,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        CmafPackage: "CmafPackageCreateOrUpdateParametersTypeDef" = None,
        DashPackage: "DashPackageTypeDef" = None,
        Description: str = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        ManifestName: str = None,
        MssPackage: "MssPackageTypeDef" = None,
        Origination: OriginationType = None,
        StartoverWindowSeconds: int = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        Updates an existing OriginEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Client.update_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#update_origin_endpoint)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listchannelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_harvest_jobs"]
    ) -> ListHarvestJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listharvestjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listoriginendpointspaginator)
        """
