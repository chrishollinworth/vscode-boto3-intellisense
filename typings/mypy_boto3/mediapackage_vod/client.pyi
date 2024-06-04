"""
Type annotations for mediapackage-vod service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage_vod import MediaPackageVodClient

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)
from .type_defs import (
    AuthorizationTypeDef,
    CmafPackageTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateAssetResponseTypeDef,
    CreatePackagingConfigurationResponseTypeDef,
    CreatePackagingGroupResponseTypeDef,
    DashPackageTypeDef,
    DescribeAssetResponseTypeDef,
    DescribePackagingConfigurationResponseTypeDef,
    DescribePackagingGroupResponseTypeDef,
    EgressAccessLogsTypeDef,
    HlsPackageTypeDef,
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MssPackageTypeDef,
    UpdatePackagingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MediaPackageVodClient",)

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

class MediaPackageVodClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaPackageVodClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#close)
        """

    def configure_logs(
        self, *, Id: str, EgressAccessLogs: "EgressAccessLogsTypeDef" = None
    ) -> ConfigureLogsResponseTypeDef:
        """
        Changes the packaging group's properities to configure log subscription See
        also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-
        vod-2018-11-07/ConfigureLogs>`_ **Request Syntax** response =
        client.configure_logs( EgressAccessLogs={ 'LogGroup...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.configure_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#configure_logs)
        """

    def create_asset(
        self,
        *,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateAssetResponseTypeDef:
        """
        Creates a new MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#create_asset)
        """

    def create_packaging_configuration(
        self,
        *,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: "CmafPackageTypeDef" = None,
        DashPackage: "DashPackageTypeDef" = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        MssPackage: "MssPackageTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreatePackagingConfigurationResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#create_packaging_configuration)
        """

    def create_packaging_group(
        self,
        *,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreatePackagingGroupResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#create_packaging_group)
        """

    def delete_asset(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes an existing MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#delete_asset)
        """

    def delete_packaging_configuration(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#delete_packaging_configuration)
        """

    def delete_packaging_group(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#delete_packaging_group)
        """

    def describe_asset(self, *, Id: str) -> DescribeAssetResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#describe_asset)
        """

    def describe_packaging_configuration(
        self, *, Id: str
    ) -> DescribePackagingConfigurationResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#describe_packaging_configuration)
        """

    def describe_packaging_group(self, *, Id: str) -> DescribePackagingGroupResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#describe_packaging_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#generate_presigned_url)
        """

    def list_assets(
        self, *, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListAssetsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD Asset resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#list_assets)
        """

    def list_packaging_configurations(
        self, *, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingConfiguration resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#list_packaging_configurations)
        """

    def list_packaging_groups(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingGroup resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#list_packaging_groups)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#untag_resource)
        """

    def update_packaging_group(
        self, *, Id: str, Authorization: "AuthorizationTypeDef" = None
    ) -> UpdatePackagingGroupResponseTypeDef:
        """
        Updates a specific packaging group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Client.update_packaging_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client.html#update_packaging_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listassetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> ListPackagingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackagingconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> ListPackagingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackaginggroupspaginator)
        """
