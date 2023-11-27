"""
Type annotations for migration-hub-refactor-spaces service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_migration_hub_refactor_spaces import MigrationHubRefactorSpacesClient
    from mypy_boto3_migration_hub_refactor_spaces.paginator import (
        ListApplicationsPaginator,
        ListEnvironmentVpcsPaginator,
        ListEnvironmentsPaginator,
        ListRoutesPaginator,
        ListServicesPaginator,
    )

    client: MigrationHubRefactorSpacesClient = boto3.client("migration-hub-refactor-spaces")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_environment_vpcs_paginator: ListEnvironmentVpcsPaginator = client.get_paginator("list_environment_vpcs")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_routes_paginator: ListRoutesPaginator = client.get_paginator("list_routes")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListEnvironmentVpcsResponseTypeDef,
    ListRoutesResponseTypeDef,
    ListServicesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationsPaginator",
    "ListEnvironmentVpcsPaginator",
    "ListEnvironmentsPaginator",
    "ListRoutesPaginator",
    "ListServicesPaginator",
)

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, EnvironmentIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listapplicationspaginator)
        """

class ListEnvironmentVpcsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListEnvironmentVpcs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listenvironmentvpcspaginator)
    """

    def paginate(
        self, *, EnvironmentIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentVpcsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListEnvironmentVpcs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listenvironmentvpcspaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listenvironmentspaginator)
        """

class ListRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listroutespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listroutespaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listservicespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/migration-hub-refactor-spaces.html#MigrationHubRefactorSpaces.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators.html#listservicespaginator)
        """
