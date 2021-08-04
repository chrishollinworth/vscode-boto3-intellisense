"""
Type annotations for amplify service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amplify import AmplifyClient
    from mypy_boto3_amplify.paginator import (
        ListAppsPaginator,
        ListBranchesPaginator,
        ListDomainAssociationsPaginator,
        ListJobsPaginator,
    )

    client: AmplifyClient = boto3.client("amplify")

    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_branches_paginator: ListBranchesPaginator = client.get_paginator("list_branches")
    list_domain_associations_paginator: ListDomainAssociationsPaginator = client.get_paginator("list_domain_associations")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAppsResultTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)

class ListAppsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListApps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listappspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listappspaginator)
        """

class ListBranchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListBranches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listbranchespaginator)
    """

    def paginate(
        self, *, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBranchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListBranches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listbranchespaginator)
        """

class ListDomainAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listdomainassociationspaginator)
    """

    def paginate(
        self, *, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listdomainassociationspaginator)
        """

class ListJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listjobspaginator)
    """

    def paginate(
        self, *, appId: str, branchName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amplify.html#Amplify.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators.html#listjobspaginator)
        """
