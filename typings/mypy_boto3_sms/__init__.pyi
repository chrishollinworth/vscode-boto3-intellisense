"""
Main interface for sms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sms import (
        Client,
        GetConnectorsPaginator,
        GetReplicationJobsPaginator,
        GetReplicationRunsPaginator,
        GetServersPaginator,
        ListAppsPaginator,
        SMSClient,
    )

    session = boto3.Session()

    client: SMSClient = boto3.client("sms")
    session_client: SMSClient = session.client("sms")

    get_connectors_paginator: GetConnectorsPaginator = client.get_paginator("get_connectors")
    get_replication_jobs_paginator: GetReplicationJobsPaginator = client.get_paginator("get_replication_jobs")
    get_replication_runs_paginator: GetReplicationRunsPaginator = client.get_paginator("get_replication_runs")
    get_servers_paginator: GetServersPaginator = client.get_paginator("get_servers")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    ```
"""
from mypy_boto3_sms.client import SMSClient
from mypy_boto3_sms.paginator import (
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
