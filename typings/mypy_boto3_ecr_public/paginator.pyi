"""
Main interface for ecr-public service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ecr_public import ECRPublicClient
    from mypy_boto3_ecr_public.paginator import (
        DescribeImageTagsPaginator,
        DescribeImagesPaginator,
        DescribeRegistriesPaginator,
        DescribeRepositoriesPaginator,
    )

    client: ECRPublicClient = boto3.client("ecr-public")

    describe_image_tags_paginator: DescribeImageTagsPaginator = client.get_paginator("describe_image_tags")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_registries_paginator: DescribeRegistriesPaginator = client.get_paginator("describe_registries")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ecr_public.type_defs import (
    DescribeImagesResponseTypeDef,
    DescribeImageTagsResponseTypeDef,
    DescribeRegistriesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    ImageIdentifierTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeImageTagsPaginator",
    "DescribeImagesPaginator",
    "DescribeRegistriesPaginator",
    "DescribeRepositoriesPaginator",
)


class DescribeImageTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImageTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImageTags)
    """

    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImageTagsResponseTypeDef]:
        """
        [DescribeImageTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImageTags.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImages)
    """

    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImagesResponseTypeDef]:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImages.paginate)
        """


class DescribeRegistriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRegistries)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRegistriesResponseTypeDef]:
        """
        [DescribeRegistries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRegistries.paginate)
        """


class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRepositories)
    """

    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeRepositoriesResponseTypeDef]:
        """
        [DescribeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRepositories.paginate)
        """
