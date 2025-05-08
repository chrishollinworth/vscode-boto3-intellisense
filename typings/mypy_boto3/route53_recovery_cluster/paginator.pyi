"""
Type annotations for route53-recovery-cluster service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53_recovery_cluster.client import Route53RecoveryClusterClient
    from mypy_boto3_route53_recovery_cluster.paginator import (
        ListRoutingControlsPaginator,
    )

    session = Session()
    client: Route53RecoveryClusterClient = session.client("route53-recovery-cluster")

    list_routing_controls_paginator: ListRoutingControlsPaginator = client.get_paginator("list_routing_controls")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListRoutingControlsRequestPaginateTypeDef, ListRoutingControlsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRoutingControlsPaginator",)

if TYPE_CHECKING:
    _ListRoutingControlsPaginatorBase = Paginator[ListRoutingControlsResponseTypeDef]
else:
    _ListRoutingControlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutingControlsPaginator(_ListRoutingControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/paginator/ListRoutingControls.html#Route53RecoveryCluster.Paginator.ListRoutingControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators/#listroutingcontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutingControlsRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutingControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/paginator/ListRoutingControls.html#Route53RecoveryCluster.Paginator.ListRoutingControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators/#listroutingcontrolspaginator)
        """
