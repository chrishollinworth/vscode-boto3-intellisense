"""
Main interface for ecr-public service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ecr_public import (
        Client,
        DescribeImageTagsPaginator,
        DescribeImagesPaginator,
        DescribeRegistriesPaginator,
        DescribeRepositoriesPaginator,
        ECRPublicClient,
    )

    session = Session()
    client: ECRPublicClient = session.client("ecr-public")

    describe_image_tags_paginator: DescribeImageTagsPaginator = client.get_paginator("describe_image_tags")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_registries_paginator: DescribeRegistriesPaginator = client.get_paginator("describe_registries")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    ```
"""

from .client import ECRPublicClient
from .paginator import (
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
