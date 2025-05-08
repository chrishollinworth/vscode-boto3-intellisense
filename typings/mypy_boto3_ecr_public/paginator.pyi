"""
Type annotations for ecr-public service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ecr_public.client import ECRPublicClient
    from mypy_boto3_ecr_public.paginator import (
        DescribeImageTagsPaginator,
        DescribeImagesPaginator,
        DescribeRegistriesPaginator,
        DescribeRepositoriesPaginator,
    )

    session = Session()
    client: ECRPublicClient = session.client("ecr-public")

    describe_image_tags_paginator: DescribeImageTagsPaginator = client.get_paginator("describe_image_tags")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_registries_paginator: DescribeRegistriesPaginator = client.get_paginator("describe_registries")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeImagesRequestPaginateTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeImageTagsRequestPaginateTypeDef,
    DescribeImageTagsResponseTypeDef,
    DescribeRegistriesRequestPaginateTypeDef,
    DescribeRegistriesResponseTypeDef,
    DescribeRepositoriesRequestPaginateTypeDef,
    DescribeRepositoriesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeImageTagsPaginator",
    "DescribeImagesPaginator",
    "DescribeRegistriesPaginator",
    "DescribeRepositoriesPaginator",
)

if TYPE_CHECKING:
    _DescribeImageTagsPaginatorBase = Paginator[DescribeImageTagsResponseTypeDef]
else:
    _DescribeImageTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImageTagsPaginator(_DescribeImageTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeImageTags.html#ECRPublic.Paginator.DescribeImageTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeimagetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImageTagsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImageTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeImageTags.html#ECRPublic.Paginator.DescribeImageTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeimagetagspaginator)
        """

if TYPE_CHECKING:
    _DescribeImagesPaginatorBase = Paginator[DescribeImagesResponseTypeDef]
else:
    _DescribeImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImagesPaginator(_DescribeImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeImages.html#ECRPublic.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeImages.html#ECRPublic.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeRegistriesPaginatorBase = Paginator[DescribeRegistriesResponseTypeDef]
else:
    _DescribeRegistriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRegistriesPaginator(_DescribeRegistriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeRegistries.html#ECRPublic.Paginator.DescribeRegistries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeregistriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRegistriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRegistriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeRegistries.html#ECRPublic.Paginator.DescribeRegistries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describeregistriespaginator)
        """

if TYPE_CHECKING:
    _DescribeRepositoriesPaginatorBase = Paginator[DescribeRepositoriesResponseTypeDef]
else:
    _DescribeRepositoriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRepositoriesPaginator(_DescribeRepositoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeRepositories.html#ECRPublic.Paginator.DescribeRepositories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describerepositoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRepositoriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRepositoriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public/paginator/DescribeRepositories.html#ECRPublic.Paginator.DescribeRepositories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators/#describerepositoriespaginator)
        """
