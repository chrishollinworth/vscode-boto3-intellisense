"""
Main interface for route53 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53 import (
        Client,
        ListCidrBlocksPaginator,
        ListCidrCollectionsPaginator,
        ListCidrLocationsPaginator,
        ListHealthChecksPaginator,
        ListHostedZonesPaginator,
        ListQueryLoggingConfigsPaginator,
        ListResourceRecordSetsPaginator,
        ListVPCAssociationAuthorizationsPaginator,
        ResourceRecordSetsChangedWaiter,
        Route53Client,
    )

    session = Session()
    client: Route53Client = session.client("route53")

    resource_record_sets_changed_waiter: ResourceRecordSetsChangedWaiter = client.get_waiter("resource_record_sets_changed")

    list_cidr_blocks_paginator: ListCidrBlocksPaginator = client.get_paginator("list_cidr_blocks")
    list_cidr_collections_paginator: ListCidrCollectionsPaginator = client.get_paginator("list_cidr_collections")
    list_cidr_locations_paginator: ListCidrLocationsPaginator = client.get_paginator("list_cidr_locations")
    list_health_checks_paginator: ListHealthChecksPaginator = client.get_paginator("list_health_checks")
    list_hosted_zones_paginator: ListHostedZonesPaginator = client.get_paginator("list_hosted_zones")
    list_query_logging_configs_paginator: ListQueryLoggingConfigsPaginator = client.get_paginator("list_query_logging_configs")
    list_resource_record_sets_paginator: ListResourceRecordSetsPaginator = client.get_paginator("list_resource_record_sets")
    list_vpc_association_authorizations_paginator: ListVPCAssociationAuthorizationsPaginator = client.get_paginator("list_vpc_association_authorizations")
    ```
"""

from .client import Route53Client
from .paginator import (
    ListCidrBlocksPaginator,
    ListCidrCollectionsPaginator,
    ListCidrLocationsPaginator,
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from .waiter import ResourceRecordSetsChangedWaiter

Client = Route53Client

__all__ = (
    "Client",
    "ListCidrBlocksPaginator",
    "ListCidrCollectionsPaginator",
    "ListCidrLocationsPaginator",
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
    "ResourceRecordSetsChangedWaiter",
    "Route53Client",
)
