"""
Type annotations for migration-hub-refactor-spaces service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient
    from mypy_boto3_migration_hub_refactor_spaces.paginator import (
        ListApplicationsPaginator,
        ListEnvironmentVpcsPaginator,
        ListEnvironmentsPaginator,
        ListRoutesPaginator,
        ListServicesPaginator,
    )

    session = Session()
    client: MigrationHubRefactorSpacesClient = session.client("migration-hub-refactor-spaces")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_environment_vpcs_paginator: ListEnvironmentVpcsPaginator = client.get_paginator("list_environment_vpcs")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_routes_paginator: ListRoutesPaginator = client.get_paginator("list_routes")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListEnvironmentVpcsRequestPaginateTypeDef,
    ListEnvironmentVpcsResponseTypeDef,
    ListRoutesRequestPaginateTypeDef,
    ListRoutesResponseTypeDef,
    ListServicesRequestPaginateTypeDef,
    ListServicesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationsPaginator",
    "ListEnvironmentVpcsPaginator",
    "ListEnvironmentsPaginator",
    "ListRoutesPaginator",
    "ListServicesPaginator",
)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListApplications.html#MigrationHubRefactorSpaces.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListApplications.html#MigrationHubRefactorSpaces.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentVpcsPaginatorBase = Paginator[ListEnvironmentVpcsResponseTypeDef]
else:
    _ListEnvironmentVpcsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentVpcsPaginator(_ListEnvironmentVpcsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListEnvironmentVpcs.html#MigrationHubRefactorSpaces.Paginator.ListEnvironmentVpcs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listenvironmentvpcspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentVpcsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentVpcsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListEnvironmentVpcs.html#MigrationHubRefactorSpaces.Paginator.ListEnvironmentVpcs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listenvironmentvpcspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsResponseTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListEnvironments.html#MigrationHubRefactorSpaces.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListEnvironments.html#MigrationHubRefactorSpaces.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListRoutesPaginatorBase = Paginator[ListRoutesResponseTypeDef]
else:
    _ListRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutesPaginator(_ListRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListRoutes.html#MigrationHubRefactorSpaces.Paginator.ListRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutesRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListRoutes.html#MigrationHubRefactorSpaces.Paginator.ListRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listroutespaginator)
        """

if TYPE_CHECKING:
    _ListServicesPaginatorBase = Paginator[ListServicesResponseTypeDef]
else:
    _ListServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesPaginator(_ListServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListServices.html#MigrationHubRefactorSpaces.Paginator.ListServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesRequestPaginateTypeDef]
    ) -> PageIterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces/paginator/ListServices.html#MigrationHubRefactorSpaces.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/paginators/#listservicespaginator)
        """
