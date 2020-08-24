"""
Main interface for macie service.

Usage::

    ```python
    import boto3
    from mypy_boto3_macie import (
        Client,
        ListMemberAccountsPaginator,
        ListS3ResourcesPaginator,
        MacieClient,
    )

    session = boto3.Session()

    client: MacieClient = boto3.client("macie")
    session_client: MacieClient = session.client("macie")

    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_s3_resources_paginator: ListS3ResourcesPaginator = client.get_paginator("list_s3_resources")
    ```
"""
from mypy_boto3_macie.client import MacieClient
from mypy_boto3_macie.paginator import ListMemberAccountsPaginator, ListS3ResourcesPaginator

Client = MacieClient


__all__ = ("Client", "ListMemberAccountsPaginator", "ListS3ResourcesPaginator", "MacieClient")
