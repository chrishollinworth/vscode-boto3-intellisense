"""
Main interface for ds service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ds import (
        Client,
        DescribeClientAuthenticationSettingsPaginator,
        DescribeDirectoriesPaginator,
        DescribeDomainControllersPaginator,
        DescribeLDAPSSettingsPaginator,
        DescribeRegionsPaginator,
        DescribeSharedDirectoriesPaginator,
        DescribeSnapshotsPaginator,
        DescribeTrustsPaginator,
        DescribeUpdateDirectoryPaginator,
        DirectoryServiceClient,
        ListCertificatesPaginator,
        ListIpRoutesPaginator,
        ListLogSubscriptionsPaginator,
        ListSchemaExtensionsPaginator,
        ListTagsForResourcePaginator,
    )

    session = boto3.Session()

    client: DirectoryServiceClient = boto3.client("ds")
    session_client: DirectoryServiceClient = session.client("ds")

    describe_client_authentication_settings_paginator: DescribeClientAuthenticationSettingsPaginator = client.get_paginator("describe_client_authentication_settings")
    describe_directories_paginator: DescribeDirectoriesPaginator = client.get_paginator("describe_directories")
    describe_domain_controllers_paginator: DescribeDomainControllersPaginator = client.get_paginator("describe_domain_controllers")
    describe_ldaps_settings_paginator: DescribeLDAPSSettingsPaginator = client.get_paginator("describe_ldaps_settings")
    describe_regions_paginator: DescribeRegionsPaginator = client.get_paginator("describe_regions")
    describe_shared_directories_paginator: DescribeSharedDirectoriesPaginator = client.get_paginator("describe_shared_directories")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_trusts_paginator: DescribeTrustsPaginator = client.get_paginator("describe_trusts")
    describe_update_directory_paginator: DescribeUpdateDirectoryPaginator = client.get_paginator("describe_update_directory")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_ip_routes_paginator: ListIpRoutesPaginator = client.get_paginator("list_ip_routes")
    list_log_subscriptions_paginator: ListLogSubscriptionsPaginator = client.get_paginator("list_log_subscriptions")
    list_schema_extensions_paginator: ListSchemaExtensionsPaginator = client.get_paginator("list_schema_extensions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import DirectoryServiceClient
from .paginator import (
    DescribeClientAuthenticationSettingsPaginator,
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeLDAPSSettingsPaginator,
    DescribeRegionsPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    DescribeUpdateDirectoryPaginator,
    ListCertificatesPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
)

Client = DirectoryServiceClient

__all__ = (
    "Client",
    "DescribeClientAuthenticationSettingsPaginator",
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeLDAPSSettingsPaginator",
    "DescribeRegionsPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "DescribeUpdateDirectoryPaginator",
    "DirectoryServiceClient",
    "ListCertificatesPaginator",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)
