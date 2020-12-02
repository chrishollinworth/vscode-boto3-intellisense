"""
Main interface for ecr-public service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr_public import (
        Client,
        DescribeImageTagsPaginator,
        DescribeImagesPaginator,
        DescribeRegistriesPaginator,
        DescribeRepositoriesPaginator,
        ECRPublicClient,
    )

    session = boto3.Session()

    client: ECRPublicClient = boto3.client("ecr-public")
    session_client: ECRPublicClient = session.client("ecr-public")

    describe_image_tags_paginator: DescribeImageTagsPaginator = client.get_paginator("describe_image_tags")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_registries_paginator: DescribeRegistriesPaginator = client.get_paginator("describe_registries")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    ```
"""
from mypy_boto3_ecr_public.client import ECRPublicClient
from mypy_boto3_ecr_public.paginator import (
    DescribeImagesPaginator,
    DescribeImageTagsPaginator,
    DescribeRegistriesPaginator,
    DescribeRepositoriesPaginator,
)

Client = ECRPublicClient


__all__ = (
    "Client",
    "DescribeImageTagsPaginator",
    "DescribeImagesPaginator",
    "DescribeRegistriesPaginator",
    "DescribeRepositoriesPaginator",
    "ECRPublicClient",
)
