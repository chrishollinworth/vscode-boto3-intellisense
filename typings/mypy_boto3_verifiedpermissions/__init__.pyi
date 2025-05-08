"""
Main interface for verifiedpermissions service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_verifiedpermissions import (
        Client,
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
        VerifiedPermissionsClient,
    )

    session = Session()
    client: VerifiedPermissionsClient = session.client("verifiedpermissions")

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
