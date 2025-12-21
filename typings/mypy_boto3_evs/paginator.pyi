"""
Type annotations for evs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_evs.client import EVSClient
    from mypy_boto3_evs.paginator import (
        ListEnvironmentHostsPaginator,
        ListEnvironmentVlansPaginator,
        ListEnvironmentsPaginator,
    )

    session = Session()
    client: EVSClient = session.client("evs")

    list_environment_hosts_paginator: ListEnvironmentHostsPaginator = client.get_paginator("list_environment_hosts")
    list_environment_vlans_paginator: ListEnvironmentVlansPaginator = client.get_paginator("list_environment_vlans")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEnvironmentHostsRequestPaginateTypeDef,
    ListEnvironmentHostsResponseTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListEnvironmentVlansRequestPaginateTypeDef,
    ListEnvironmentVlansResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEnvironmentHostsPaginator",
    "ListEnvironmentVlansPaginator",
    "ListEnvironmentsPaginator",
)

if TYPE_CHECKING:
    _ListEnvironmentHostsPaginatorBase = Paginator[ListEnvironmentHostsResponseTypeDef]
else:
    _ListEnvironmentHostsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentHostsPaginator(_ListEnvironmentHostsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironmentHosts.html#EVS.Paginator.ListEnvironmentHosts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmenthostspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentHostsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentHostsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironmentHosts.html#EVS.Paginator.ListEnvironmentHosts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmenthostspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentVlansPaginatorBase = Paginator[ListEnvironmentVlansResponseTypeDef]
else:
    _ListEnvironmentVlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentVlansPaginator(_ListEnvironmentVlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironmentVlans.html#EVS.Paginator.ListEnvironmentVlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmentvlanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentVlansRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentVlansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironmentVlans.html#EVS.Paginator.ListEnvironmentVlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmentvlanspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsResponseTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironments.html#EVS.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evs/paginator/ListEnvironments.html#EVS.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evs/paginators/#listenvironmentspaginator)
        """
