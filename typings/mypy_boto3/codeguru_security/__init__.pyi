"""
Main interface for codeguru-security service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_security import (
        Client,
        CodeGuruSecurityClient,
        GetFindingsPaginator,
        ListFindingsMetricsPaginator,
        ListScansPaginator,
    )

    session = boto3.Session()

    client: CodeGuruSecurityClient = boto3.client("codeguru-security")
    session_client: CodeGuruSecurityClient = session.client("codeguru-security")

    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    list_findings_metrics_paginator: ListFindingsMetricsPaginator = client.get_paginator("list_findings_metrics")
    list_scans_paginator: ListScansPaginator = client.get_paginator("list_scans")
    ```
"""

from .client import CodeGuruSecurityClient
from .paginator import GetFindingsPaginator, ListFindingsMetricsPaginator, ListScansPaginator

Client = CodeGuruSecurityClient

__all__ = (
    "Client",
    "CodeGuruSecurityClient",
    "GetFindingsPaginator",
    "ListFindingsMetricsPaginator",
    "ListScansPaginator",
)
