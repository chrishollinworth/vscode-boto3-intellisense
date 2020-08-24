"""
Main interface for fms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_fms import (
        Client,
        FMSClient,
        ListComplianceStatusPaginator,
        ListMemberAccountsPaginator,
        ListPoliciesPaginator,
    )

    session = boto3.Session()

    client: FMSClient = boto3.client("fms")
    session_client: FMSClient = session.client("fms")

    list_compliance_status_paginator: ListComplianceStatusPaginator = client.get_paginator("list_compliance_status")
    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    ```
"""
from mypy_boto3_fms.client import FMSClient
from mypy_boto3_fms.paginator import (
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
)

Client = FMSClient


__all__ = (
    "Client",
    "FMSClient",
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
)
