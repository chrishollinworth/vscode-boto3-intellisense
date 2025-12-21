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
        ListCentralizationRulesForOrganizationPaginator,
        ListResourceTelemetryForOrganizationPaginator,
        ListResourceTelemetryPaginator,
        ListS3TableIntegrationsPaginator,
        ListTelemetryPipelinesPaginator,
        ListTelemetryRulesForOrganizationPaginator,
        ListTelemetryRulesPaginator,
    )

    session = Session()
    client: CloudWatchObservabilityAdminServiceClient = session.client("observabilityadmin")

    list_centralization_rules_for_organization_paginator: ListCentralizationRulesForOrganizationPaginator = client.get_paginator("list_centralization_rules_for_organization")
    list_resource_telemetry_for_organization_paginator: ListResourceTelemetryForOrganizationPaginator = client.get_paginator("list_resource_telemetry_for_organization")
    list_resource_telemetry_paginator: ListResourceTelemetryPaginator = client.get_paginator("list_resource_telemetry")
    list_s3_table_integrations_paginator: ListS3TableIntegrationsPaginator = client.get_paginator("list_s3_table_integrations")
    list_telemetry_pipelines_paginator: ListTelemetryPipelinesPaginator = client.get_paginator("list_telemetry_pipelines")
    list_telemetry_rules_for_organization_paginator: ListTelemetryRulesForOrganizationPaginator = client.get_paginator("list_telemetry_rules_for_organization")
    list_telemetry_rules_paginator: ListTelemetryRulesPaginator = client.get_paginator("list_telemetry_rules")
    ```
"""

from .client import CloudWatchObservabilityAdminServiceClient
from .paginator import (
    ListCentralizationRulesForOrganizationPaginator,
    ListResourceTelemetryForOrganizationPaginator,
    ListResourceTelemetryPaginator,
    ListS3TableIntegrationsPaginator,
    ListTelemetryPipelinesPaginator,
    ListTelemetryRulesForOrganizationPaginator,
    ListTelemetryRulesPaginator,
)

Client = CloudWatchObservabilityAdminServiceClient

__all__ = (
    "Client",
    "CloudWatchObservabilityAdminServiceClient",
    "ListCentralizationRulesForOrganizationPaginator",
    "ListResourceTelemetryForOrganizationPaginator",
    "ListResourceTelemetryPaginator",
    "ListS3TableIntegrationsPaginator",
    "ListTelemetryPipelinesPaginator",
    "ListTelemetryRulesForOrganizationPaginator",
    "ListTelemetryRulesPaginator",
)
