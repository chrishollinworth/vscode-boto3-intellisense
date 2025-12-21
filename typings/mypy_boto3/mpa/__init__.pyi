"""
Main interface for mpa service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mpa import (
        Client,
        ListApprovalTeamsPaginator,
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyVersionsPaginator,
        ListResourcePoliciesPaginator,
        ListSessionsPaginator,
        MultipartyApprovalClient,
    )

    session = Session()
    client: MultipartyApprovalClient = session.client("mpa")

    list_approval_teams_paginator: ListApprovalTeamsPaginator = client.get_paginator("list_approval_teams")
    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_versions_paginator: ListPolicyVersionsPaginator = client.get_paginator("list_policy_versions")
    list_resource_policies_paginator: ListResourcePoliciesPaginator = client.get_paginator("list_resource_policies")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

from .client import MultipartyApprovalClient
from .paginator import (
    ListApprovalTeamsPaginator,
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListResourcePoliciesPaginator,
    ListSessionsPaginator,
)

Client = MultipartyApprovalClient

__all__ = (
    "Client",
    "ListApprovalTeamsPaginator",
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyVersionsPaginator",
    "ListResourcePoliciesPaginator",
    "ListSessionsPaginator",
    "MultipartyApprovalClient",
)
