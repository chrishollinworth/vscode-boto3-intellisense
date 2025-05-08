"""
Main interface for rolesanywhere service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rolesanywhere import (
        Client,
        IAMRolesAnywhereClient,
        ListCrlsPaginator,
        ListProfilesPaginator,
        ListSubjectsPaginator,
        ListTrustAnchorsPaginator,
    )

    session = Session()
    client: IAMRolesAnywhereClient = session.client("rolesanywhere")

    list_crls_paginator: ListCrlsPaginator = client.get_paginator("list_crls")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_subjects_paginator: ListSubjectsPaginator = client.get_paginator("list_subjects")
    list_trust_anchors_paginator: ListTrustAnchorsPaginator = client.get_paginator("list_trust_anchors")
    ```
"""

from .client import IAMRolesAnywhereClient
from .paginator import (
    ListCrlsPaginator,
    ListProfilesPaginator,
    ListSubjectsPaginator,
    ListTrustAnchorsPaginator,
)

Client = IAMRolesAnywhereClient

__all__ = (
    "Client",
    "IAMRolesAnywhereClient",
    "ListCrlsPaginator",
    "ListProfilesPaginator",
    "ListSubjectsPaginator",
    "ListTrustAnchorsPaginator",
)
