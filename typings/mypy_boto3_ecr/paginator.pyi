"""
Type annotations for ecr service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ecr import ECRClient
    from mypy_boto3_ecr.paginator import (
        DescribeImageScanFindingsPaginator,
        DescribeImagesPaginator,
        DescribePullThroughCacheRulesPaginator,
        DescribeRepositoriesPaginator,
        GetLifecyclePolicyPreviewPaginator,
        ListImagesPaginator,
    )

    client: ECRClient = boto3.client("ecr")

    describe_image_scan_findings_paginator: DescribeImageScanFindingsPaginator = client.get_paginator("describe_image_scan_findings")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_pull_through_cache_rules_paginator: DescribePullThroughCacheRulesPaginator = client.get_paginator("describe_pull_through_cache_rules")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    get_lifecycle_policy_preview_paginator: GetLifecyclePolicyPreviewPaginator = client.get_paginator("get_lifecycle_policy_preview")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeImageScanFindingsResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseTypeDef,
    DescribePullThroughCacheRulesResponseTypeDef,
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
    "DescribePullThroughCacheRulesPaginator",
    "DescribeRepositoriesPaginator",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)

class DescribeImageScanFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagescanfindingspaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImageScanFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagescanfindingspaginator)
        """

class DescribeImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagespaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: "DescribeImagesFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagespaginator)
        """

class DescribePullThroughCacheRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribePullThroughCacheRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describepullthroughcacherulespaginator)
    """

    def paginate(
        self,
        *,
        registryId: str = None,
        ecrRepositoryPrefixes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePullThroughCacheRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribePullThroughCacheRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describepullthroughcacherulespaginator)
        """

class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describerepositoriespaginator)
    """

    def paginate(
        self,
        *,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRepositoriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.DescribeRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describerepositoriespaginator)
        """

class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#getlifecyclepolicypreviewpaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        filter: "LifecyclePolicyPreviewFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLifecyclePolicyPreviewResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#getlifecyclepolicypreviewpaginator)
        """

class ListImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.ListImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#listimagespaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        filter: "ListImagesFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ecr.html#ECR.Paginator.ListImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#listimagespaginator)
        """
