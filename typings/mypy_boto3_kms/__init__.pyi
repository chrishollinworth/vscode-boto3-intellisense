"""
Main interface for kms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kms import (
        Client,
        KMSClient,
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeysPaginator,
    )

    session = boto3.Session()

    client: KMSClient = boto3.client("kms")
    session_client: KMSClient = session.client("kms")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""
from mypy_boto3_kms.client import KMSClient
from mypy_boto3_kms.paginator import (
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeysPaginator,
)

Client = KMSClient


__all__ = (
    "Client",
    "KMSClient",
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)
