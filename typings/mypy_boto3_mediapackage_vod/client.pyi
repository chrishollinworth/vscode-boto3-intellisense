# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediapackage-vod service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage_vod import MediaPackageVodClient

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_mediapackage_vod.paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)
from mypy_boto3_mediapackage_vod.type_defs import (
    AuthorizationTypeDef,
    CmafPackageTypeDef,
    CreateAssetResponseTypeDef,
    CreatePackagingConfigurationResponseTypeDef,
    CreatePackagingGroupResponseTypeDef,
    DashPackageTypeDef,
    DescribeAssetResponseTypeDef,
    DescribePackagingConfigurationResponseTypeDef,
    DescribePackagingGroupResponseTypeDef,
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


class MediaPackageVodClient:
    """
    [MediaPackageVod.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)
        """

    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateAssetResponseTypeDef:
        """
        [Client.create_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)
        """

    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: "CmafPackageTypeDef" = None,
        DashPackage: "DashPackageTypeDef" = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        MssPackage: "MssPackageTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreatePackagingConfigurationResponseTypeDef:
        """
        [Client.create_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)
        """

    def create_packaging_group(
        self, Id: str, Authorization: "AuthorizationTypeDef" = None, Tags: Dict[str, str] = None
    ) -> CreatePackagingGroupResponseTypeDef:
        """
        [Client.create_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)
        """

    def delete_asset(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)
        """

    def delete_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)
        """

    def delete_packaging_group(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)
        """

    def describe_asset(self, Id: str) -> DescribeAssetResponseTypeDef:
        """
        [Client.describe_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)
        """

    def describe_packaging_configuration(
        self, Id: str
    ) -> DescribePackagingConfigurationResponseTypeDef:
        """
        [Client.describe_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)
        """

    def describe_packaging_group(self, Id: str) -> DescribePackagingGroupResponseTypeDef:
        """
        [Client.describe_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)
        """

    def list_assets(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListAssetsResponseTypeDef:
        """
        [Client.list_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)
        """

    def list_packaging_configurations(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        [Client.list_packaging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)
        """

    def list_packaging_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        [Client.list_packaging_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.untag_resource)
        """

    def update_packaging_group(
        self, Id: str, Authorization: "AuthorizationTypeDef" = None
    ) -> UpdatePackagingGroupResponseTypeDef:
        """
        [Client.update_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Client.update_packaging_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> ListPackagingConfigurationsPaginator:
        """
        [Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> ListPackagingGroupsPaginator:
        """
        [Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
        """
