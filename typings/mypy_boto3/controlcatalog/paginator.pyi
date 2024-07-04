"""
Type annotations for controlcatalog service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_controlcatalog import ControlCatalogClient
    from mypy_boto3_controlcatalog.paginator import (
        ListCommonControlsPaginator,
        ListDomainsPaginator,
        ListObjectivesPaginator,
    )

    client: ControlCatalogClient = boto3.client("controlcatalog")

    list_common_controls_paginator: ListCommonControlsPaginator = client.get_paginator("list_common_controls")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_objectives_paginator: ListObjectivesPaginator = client.get_paginator("list_objectives")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    CommonControlFilterTypeDef,
    ListCommonControlsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListObjectivesResponseTypeDef,
    ObjectiveFilterTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListCommonControlsPaginator", "ListDomainsPaginator", "ListObjectivesPaginator")

class ListCommonControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListCommonControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listcommoncontrolspaginator)
    """

    def paginate(
        self,
        *,
        CommonControlFilter: "CommonControlFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCommonControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListCommonControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listcommoncontrolspaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listdomainspaginator)
        """

class ListObjectivesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListObjectives)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listobjectivespaginator)
    """

    def paginate(
        self,
        *,
        ObjectiveFilter: "ObjectiveFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListObjectivesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListObjectives.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listobjectivespaginator)
        """
