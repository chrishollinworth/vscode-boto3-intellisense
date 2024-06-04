"""
Type annotations for route53-recovery-cluster service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53_recovery_cluster import Route53RecoveryClusterClient
    from mypy_boto3_route53_recovery_cluster.paginator import (
        ListRoutingControlsPaginator,
    )

    client: Route53RecoveryClusterClient = boto3.client("route53-recovery-cluster")

    list_routing_controls_paginator: ListRoutingControlsPaginator = client.get_paginator("list_routing_controls")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListRoutingControlsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListRoutingControlsPaginator",)

class ListRoutingControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Paginator.ListRoutingControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators.html#listroutingcontrolspaginator)
    """

    def paginate(
        self, *, ControlPanelArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutingControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Paginator.ListRoutingControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators.html#listroutingcontrolspaginator)
        """
