"""
Main interface for ecr service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr import (
        Client,
        DescribeImageScanFindingsPaginator,
        DescribeImagesPaginator,
        DescribeRepositoriesPaginator,
        ECRClient,
        GetLifecyclePolicyPreviewPaginator,
        ImageScanCompleteWaiter,
        LifecyclePolicyPreviewCompleteWaiter,
        ListImagesPaginator,
    )

    session = boto3.Session()

    client: ECRClient = boto3.client("ecr")
    session_client: ECRClient = session.client("ecr")

    image_scan_complete_waiter: ImageScanCompleteWaiter = client.get_waiter("image_scan_complete")
    lifecycle_policy_preview_complete_waiter: LifecyclePolicyPreviewCompleteWaiter = client.get_waiter("lifecycle_policy_preview_complete")

    describe_image_scan_findings_paginator: DescribeImageScanFindingsPaginator = client.get_paginator("describe_image_scan_findings")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    get_lifecycle_policy_preview_paginator: GetLifecyclePolicyPreviewPaginator = client.get_paginator("get_lifecycle_policy_preview")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    ```
"""
from .client import ECRClient
from .paginator import (
    DescribeImageScanFindingsPaginator,
    DescribeImagesPaginator,
    DescribeRepositoriesPaginator,
    GetLifecyclePolicyPreviewPaginator,
    ListImagesPaginator,
)
from .waiter import ImageScanCompleteWaiter, LifecyclePolicyPreviewCompleteWaiter

Client = ECRClient

__all__ = (
    "Client",
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "ECRClient",
    "GetLifecyclePolicyPreviewPaginator",
    "ImageScanCompleteWaiter",
    "LifecyclePolicyPreviewCompleteWaiter",
    "ListImagesPaginator",
)
