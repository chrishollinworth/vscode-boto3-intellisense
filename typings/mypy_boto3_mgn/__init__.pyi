"""
Main interface for mgn service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mgn import (
        Client,
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeLaunchConfigurationTemplatesPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceServersPaginator,
        DescribeVcenterClientsPaginator,
        ListApplicationsPaginator,
        ListExportErrorsPaginator,
        ListExportsPaginator,
        ListImportErrorsPaginator,
        ListImportsPaginator,
        ListSourceServerActionsPaginator,
        ListTemplateActionsPaginator,
        ListWavesPaginator,
        mgnClient,
    )

    session = boto3.Session()

    client: mgnClient = boto3.client("mgn")
    session_client: mgnClient = session.client("mgn")

    describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
    describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
    describe_launch_configuration_templates_paginator: DescribeLaunchConfigurationTemplatesPaginator = client.get_paginator("describe_launch_configuration_templates")
    describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
    describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
    describe_vcenter_clients_paginator: DescribeVcenterClientsPaginator = client.get_paginator("describe_vcenter_clients")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_export_errors_paginator: ListExportErrorsPaginator = client.get_paginator("list_export_errors")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_import_errors_paginator: ListImportErrorsPaginator = client.get_paginator("list_import_errors")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_source_server_actions_paginator: ListSourceServerActionsPaginator = client.get_paginator("list_source_server_actions")
    list_template_actions_paginator: ListTemplateActionsPaginator = client.get_paginator("list_template_actions")
    list_waves_paginator: ListWavesPaginator = client.get_paginator("list_waves")
    ```
"""
from .client import mgnClient
from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeLaunchConfigurationTemplatesPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceServersPaginator,
    DescribeVcenterClientsPaginator,
    ListApplicationsPaginator,
    ListExportErrorsPaginator,
    ListExportsPaginator,
    ListImportErrorsPaginator,
    ListImportsPaginator,
    ListSourceServerActionsPaginator,
    ListTemplateActionsPaginator,
    ListWavesPaginator,
)

Client = mgnClient

__all__ = (
    "Client",
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeLaunchConfigurationTemplatesPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceServersPaginator",
    "DescribeVcenterClientsPaginator",
    "ListApplicationsPaginator",
    "ListExportErrorsPaginator",
    "ListExportsPaginator",
    "ListImportErrorsPaginator",
    "ListImportsPaginator",
    "ListSourceServerActionsPaginator",
    "ListTemplateActionsPaginator",
    "ListWavesPaginator",
    "mgnClient",
)
