"""
Main interface for partnercentral-account service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_account import (
        Client,
        ListConnectionInvitationsPaginator,
        ListConnectionsPaginator,
        ListPartnersPaginator,
        PartnerCentralAccountAPIClient,
    )

    session = Session()
    client: PartnerCentralAccountAPIClient = session.client("partnercentral-account")

    list_connection_invitations_paginator: ListConnectionInvitationsPaginator = client.get_paginator("list_connection_invitations")
    list_connections_paginator: ListConnectionsPaginator = client.get_paginator("list_connections")
    list_partners_paginator: ListPartnersPaginator = client.get_paginator("list_partners")
    ```
"""

from .client import PartnerCentralAccountAPIClient
from .paginator import (
    ListConnectionInvitationsPaginator,
    ListConnectionsPaginator,
    ListPartnersPaginator,
)

Client = PartnerCentralAccountAPIClient

__all__ = (
    "Client",
    "ListConnectionInvitationsPaginator",
    "ListConnectionsPaginator",
    "ListPartnersPaginator",
    "PartnerCentralAccountAPIClient",
)
