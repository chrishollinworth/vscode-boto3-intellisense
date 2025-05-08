"""
Main interface for sms service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sms import (
        Client,
        GetConnectorsPaginator,
        GetReplicationJobsPaginator,
        GetReplicationRunsPaginator,
        GetServersPaginator,
        ListAppsPaginator,
        SMSClient,
    )

    session = Session()
    client: SMSClient = session.client("sms")

    get_connectors_paginator: GetConnectorsPaginator = client.get_paginator("get_connectors")
    get_replication_jobs_paginator: GetReplicationJobsPaginator = client.get_paginator("get_replication_jobs")
    get_replication_runs_paginator: GetReplicationRunsPaginator = client.get_paginator("get_replication_runs")
    get_servers_paginator: GetServersPaginator = client.get_paginator("get_servers")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    ```
"""

from .client import SMSClient
from .paginator import (
    GetConnectorsPaginator,
    GetReplicationJobsPaginator,
    GetReplicationRunsPaginator,
    GetServersPaginator,
    ListAppsPaginator,
)

Client = SMSClient

__all__ = (
    "Client",
    "GetConnectorsPaginator",
    "GetReplicationJobsPaginator",
    "GetReplicationRunsPaginator",
    "GetServersPaginator",
    "ListAppsPaginator",
    "SMSClient",
)
