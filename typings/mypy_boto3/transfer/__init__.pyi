"""
Main interface for transfer service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_transfer import (
        Client,
        ListAccessesPaginator,
        ListAgreementsPaginator,
        ListCertificatesPaginator,
        ListConnectorsPaginator,
        ListExecutionsPaginator,
        ListFileTransferResultsPaginator,
        ListProfilesPaginator,
        ListSecurityPoliciesPaginator,
        ListServersPaginator,
        ListTagsForResourcePaginator,
        ListUsersPaginator,
        ListWebAppsPaginator,
        ListWorkflowsPaginator,
        ServerOfflineWaiter,
        ServerOnlineWaiter,
        TransferClient,
    )

    session = Session()
    client: TransferClient = session.client("transfer")

    server_offline_waiter: ServerOfflineWaiter = client.get_waiter("server_offline")
    server_online_waiter: ServerOnlineWaiter = client.get_waiter("server_online")

    list_accesses_paginator: ListAccessesPaginator = client.get_paginator("list_accesses")
    list_agreements_paginator: ListAgreementsPaginator = client.get_paginator("list_agreements")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_file_transfer_results_paginator: ListFileTransferResultsPaginator = client.get_paginator("list_file_transfer_results")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_security_policies_paginator: ListSecurityPoliciesPaginator = client.get_paginator("list_security_policies")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_web_apps_paginator: ListWebAppsPaginator = client.get_paginator("list_web_apps")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from .client import TransferClient
from .paginator import (
    ListAccessesPaginator,
    ListAgreementsPaginator,
    ListCertificatesPaginator,
    ListConnectorsPaginator,
    ListExecutionsPaginator,
    ListFileTransferResultsPaginator,
    ListProfilesPaginator,
    ListSecurityPoliciesPaginator,
    ListServersPaginator,
    ListTagsForResourcePaginator,
    ListUsersPaginator,
    ListWebAppsPaginator,
    ListWorkflowsPaginator,
)
from .waiter import ServerOfflineWaiter, ServerOnlineWaiter

Client = TransferClient

__all__ = (
    "Client",
    "ListAccessesPaginator",
    "ListAgreementsPaginator",
    "ListCertificatesPaginator",
    "ListConnectorsPaginator",
    "ListExecutionsPaginator",
    "ListFileTransferResultsPaginator",
    "ListProfilesPaginator",
    "ListSecurityPoliciesPaginator",
    "ListServersPaginator",
    "ListTagsForResourcePaginator",
    "ListUsersPaginator",
    "ListWebAppsPaginator",
    "ListWorkflowsPaginator",
    "ServerOfflineWaiter",
    "ServerOnlineWaiter",
    "TransferClient",
)
