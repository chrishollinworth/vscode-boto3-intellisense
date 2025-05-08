"""
Main interface for observabilityadmin service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_observabilityadmin import (
        Client,
        CloudWatchObservabilityAdminServiceClient,
        ListResourceTelemetryForOrganizationPaginator,
        ListResourceTelemetryPaginator,
    )

    session = Session()
    client: CloudWatchObservabilityAdminServiceClient = session.client("observabilityadmin")

    list_resource_telemetry_for_organization_paginator: ListResourceTelemetryForOrganizationPaginator = client.get_paginator("list_resource_telemetry_for_organization")
    list_resource_telemetry_paginator: ListResourceTelemetryPaginator = client.get_paginator("list_resource_telemetry")
    ```
"""

from .client import CloudWatchObservabilityAdminServiceClient
from .paginator import ListResourceTelemetryForOrganizationPaginator, ListResourceTelemetryPaginator

Client = CloudWatchObservabilityAdminServiceClient

__all__ = (
    "Client",
    "CloudWatchObservabilityAdminServiceClient",
    "ListResourceTelemetryForOrganizationPaginator",
    "ListResourceTelemetryPaginator",
)
