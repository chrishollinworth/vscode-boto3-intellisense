"""
Main interface for kms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kms import (
        Client,
        DescribeCustomKeyStoresPaginator,
        KMSClient,
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeyRotationsPaginator,
        ListKeysPaginator,
        ListResourceTagsPaginator,
        ListRetirableGrantsPaginator,
    )

    session = boto3.Session()

    client: KMSClient = boto3.client("kms")
    session_client: KMSClient = session.client("kms")

    describe_custom_key_stores_paginator: DescribeCustomKeyStoresPaginator = client.get_paginator("describe_custom_key_stores")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_key_rotations_paginator: ListKeyRotationsPaginator = client.get_paginator("list_key_rotations")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_resource_tags_paginator: ListResourceTagsPaginator = client.get_paginator("list_resource_tags")
    list_retirable_grants_paginator: ListRetirableGrantsPaginator = client.get_paginator("list_retirable_grants")
    ```
"""

from .client import KMSClient
from .paginator import (
    DescribeCustomKeyStoresPaginator,
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeyRotationsPaginator,
    ListKeysPaginator,
    ListResourceTagsPaginator,
    ListRetirableGrantsPaginator,
)

Client = KMSClient

__all__ = (
    "Client",
    "DescribeCustomKeyStoresPaginator",
    "KMSClient",
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeyRotationsPaginator",
    "ListKeysPaginator",
    "ListResourceTagsPaginator",
    "ListRetirableGrantsPaginator",
)
