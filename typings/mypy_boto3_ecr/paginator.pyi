# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ecr service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ecr import ECRClient
    from mypy_boto3_ecr.paginator import (
        DescribeImageScanFindingsPaginator,
        DescribeImagesPaginator,
        DescribeRepositoriesPaginator,
        GetLifecyclePolicyPreviewPaginator,
        ListImagesPaginator,
    )

    client: ECRClient = boto3.client("ecr")

    describe_image_scan_findings_paginator: DescribeImageScanFindingsPaginator = client.get_paginator("describe_image_scan_findings")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    get_lifecycle_policy_preview_paginator: GetLifecyclePolicyPreviewPaginator = client.get_paginator("get_lifecycle_policy_preview")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ecr.type_defs import (
    DescribeImageScanFindingsResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    GetLifecyclePolicyPreviewResponseTypeDef,
    ImageIdentifierTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    ListImagesFilterTypeDef,
    ListImagesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)


class DescribeImageScanFindingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
    """

    def paginate(
        self,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImageScanFindingsResponseTypeDef]:
        """
        [DescribeImageScanFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImages)
    """

    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: DescribeImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImagesResponseTypeDef]:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImages.paginate)
        """


class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
    """

    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeRepositoriesResponseTypeDef]:
        """
        [DescribeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeRepositories.paginate)
        """


class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    """
    [Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
    """

    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetLifecyclePolicyPreviewResponseTypeDef]:
        """
        [GetLifecyclePolicyPreview.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview.paginate)
        """


class ListImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.ListImages)
    """

    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: ListImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [ListImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.ListImages.paginate)
        """
