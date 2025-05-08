"""
Type annotations for mediapackage-vod service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackage_vod.client import MediaPackageVodClient

    session = Session()
    client: MediaPackageVodClient = session.client("mediapackage-vod")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)
from .type_defs import (
    ConfigureLogsRequestTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateAssetRequestTypeDef,
    CreateAssetResponseTypeDef,
    CreatePackagingConfigurationRequestTypeDef,
    CreatePackagingConfigurationResponseTypeDef,
    CreatePackagingGroupRequestTypeDef,
    CreatePackagingGroupResponseTypeDef,
    DeleteAssetRequestTypeDef,
    DeletePackagingConfigurationRequestTypeDef,
    DeletePackagingGroupRequestTypeDef,
    DescribeAssetRequestTypeDef,
    DescribeAssetResponseTypeDef,
    DescribePackagingConfigurationRequestTypeDef,
    DescribePackagingConfigurationResponseTypeDef,
    DescribePackagingGroupRequestTypeDef,
    DescribePackagingGroupResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListAssetsRequestTypeDef,
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsRequestTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsRequestTypeDef,
    ListPackagingGroupsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePackagingGroupRequestTypeDef,
    UpdatePackagingGroupResponseTypeDef,
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

__all__ = ("MediaPackageVodClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class MediaPackageVodClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaPackageVodClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#generate_presigned_url)
        """

    def configure_logs(
        self, **kwargs: Unpack[ConfigureLogsRequestTypeDef]
    ) -> ConfigureLogsResponseTypeDef:
        """
        Changes the packaging group's properities to configure log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/configure_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#configure_logs)
        """

    def create_asset(
        self, **kwargs: Unpack[CreateAssetRequestTypeDef]
    ) -> CreateAssetResponseTypeDef:
        """
        Creates a new MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/create_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_asset)
        """

    def create_packaging_configuration(
        self, **kwargs: Unpack[CreatePackagingConfigurationRequestTypeDef]
    ) -> CreatePackagingConfigurationResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/create_packaging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_packaging_configuration)
        """

    def create_packaging_group(
        self, **kwargs: Unpack[CreatePackagingGroupRequestTypeDef]
    ) -> CreatePackagingGroupResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/create_packaging_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_packaging_group)
        """

    def delete_asset(self, **kwargs: Unpack[DeleteAssetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an existing MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/delete_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_asset)
        """

    def delete_packaging_configuration(
        self, **kwargs: Unpack[DeletePackagingConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/delete_packaging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_packaging_configuration)
        """

    def delete_packaging_group(
        self, **kwargs: Unpack[DeletePackagingGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/delete_packaging_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_packaging_group)
        """

    def describe_asset(
        self, **kwargs: Unpack[DescribeAssetRequestTypeDef]
    ) -> DescribeAssetResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/describe_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_asset)
        """

    def describe_packaging_configuration(
        self, **kwargs: Unpack[DescribePackagingConfigurationRequestTypeDef]
    ) -> DescribePackagingConfigurationResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/describe_packaging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_packaging_configuration)
        """

    def describe_packaging_group(
        self, **kwargs: Unpack[DescribePackagingGroupRequestTypeDef]
    ) -> DescribePackagingGroupResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/describe_packaging_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_packaging_group)
        """

    def list_assets(self, **kwargs: Unpack[ListAssetsRequestTypeDef]) -> ListAssetsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD Asset resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/list_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_assets)
        """

    def list_packaging_configurations(
        self, **kwargs: Unpack[ListPackagingConfigurationsRequestTypeDef]
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingConfiguration resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/list_packaging_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_packaging_configurations)
        """

    def list_packaging_groups(
        self, **kwargs: Unpack[ListPackagingGroupsRequestTypeDef]
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingGroup resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/list_packaging_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_packaging_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#untag_resource)
        """

    def update_packaging_group(
        self, **kwargs: Unpack[UpdatePackagingGroupRequestTypeDef]
    ) -> UpdatePackagingGroupResponseTypeDef:
        """
        Updates a specific packaging group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/update_packaging_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#update_packaging_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assets"]
    ) -> ListAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> ListPackagingConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_packaging_groups"]
    ) -> ListPackagingGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """
