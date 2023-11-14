"""
Main interface for verifiedpermissions service.

Usage::

    ```python
    import boto3
    from mypy_boto3_verifiedpermissions import (
        Client,
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
        VerifiedPermissionsClient,
    )

    session = boto3.Session()

    client: VerifiedPermissionsClient = boto3.client("verifiedpermissions")
    session_client: VerifiedPermissionsClient = session.client("verifiedpermissions")

    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_stores_paginator: ListPolicyStoresPaginator = client.get_paginator("list_policy_stores")
    list_policy_templates_paginator: ListPolicyTemplatesPaginator = client.get_paginator("list_policy_templates")
    ```
"""
from .client import VerifiedPermissionsClient
from .paginator import (
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyStoresPaginator,
    ListPolicyTemplatesPaginator,
)

Client = VerifiedPermissionsClient

__all__ = (
    "Client",
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyStoresPaginator",
    "ListPolicyTemplatesPaginator",
    "VerifiedPermissionsClient",
)
