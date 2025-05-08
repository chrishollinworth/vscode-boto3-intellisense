"""
Main interface for artifact service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_artifact import (
        ArtifactClient,
        Client,
        ListCustomerAgreementsPaginator,
        ListReportsPaginator,
    )

    session = Session()
    client: ArtifactClient = session.client("artifact")

    list_customer_agreements_paginator: ListCustomerAgreementsPaginator = client.get_paginator("list_customer_agreements")
    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    ```
"""

from .client import ArtifactClient
from .paginator import ListCustomerAgreementsPaginator, ListReportsPaginator

Client = ArtifactClient

__all__ = ("ArtifactClient", "Client", "ListCustomerAgreementsPaginator", "ListReportsPaginator")
