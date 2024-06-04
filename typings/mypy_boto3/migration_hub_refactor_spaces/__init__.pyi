"""
Main interface for migration-hub-refactor-spaces service.

Usage::

    ```python
    import boto3
    from mypy_boto3_migration_hub_refactor_spaces import (
        Client,
        ListApplicationsPaginator,
        ListEnvironmentVpcsPaginator,
        ListEnvironmentsPaginator,
        ListRoutesPaginator,
        ListServicesPaginator,
        MigrationHubRefactorSpacesClient,
    )

    session = boto3.Session()

    client: MigrationHubRefactorSpacesClient = boto3.client("migration-hub-refactor-spaces")
    session_client: MigrationHubRefactorSpacesClient = session.client("migration-hub-refactor-spaces")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_environment_vpcs_paginator: ListEnvironmentVpcsPaginator = client.get_paginator("list_environment_vpcs")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_routes_paginator: ListRoutesPaginator = client.get_paginator("list_routes")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from .client import MigrationHubRefactorSpacesClient
from .paginator import (
    ListApplicationsPaginator,
    ListEnvironmentsPaginator,
    ListEnvironmentVpcsPaginator,
    ListRoutesPaginator,
    ListServicesPaginator,
)

Client = MigrationHubRefactorSpacesClient

__all__ = (
    "Client",
    "ListApplicationsPaginator",
    "ListEnvironmentVpcsPaginator",
    "ListEnvironmentsPaginator",
    "ListRoutesPaginator",
    "ListServicesPaginator",
    "MigrationHubRefactorSpacesClient",
)
