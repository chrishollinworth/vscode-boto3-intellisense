"""
Type annotations for route53-recovery-control-config service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53_recovery_control_config import Route53RecoveryControlConfigClient
    from mypy_boto3_route53_recovery_control_config.paginator import (
        ListAssociatedRoute53HealthChecksPaginator,
        ListClustersPaginator,
        ListControlPanelsPaginator,
        ListRoutingControlsPaginator,
        ListSafetyRulesPaginator,
    )

    client: Route53RecoveryControlConfigClient = boto3.client("route53-recovery-control-config")

    list_associated_route53_health_checks_paginator: ListAssociatedRoute53HealthChecksPaginator = client.get_paginator("list_associated_route53_health_checks")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_control_panels_paginator: ListControlPanelsPaginator = client.get_paginator("list_control_panels")
    list_routing_controls_paginator: ListRoutingControlsPaginator = client.get_paginator("list_routing_controls")
    list_safety_rules_paginator: ListSafetyRulesPaginator = client.get_paginator("list_safety_rules")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAssociatedRoute53HealthChecksResponseTypeDef,
    ListClustersResponseTypeDef,
    ListControlPanelsResponseTypeDef,
    ListRoutingControlsResponseTypeDef,
    ListSafetyRulesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAssociatedRoute53HealthChecksPaginator",
    "ListClustersPaginator",
    "ListControlPanelsPaginator",
    "ListRoutingControlsPaginator",
    "ListSafetyRulesPaginator",
)

class ListAssociatedRoute53HealthChecksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListAssociatedRoute53HealthChecks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listassociatedroute53healthcheckspaginator)
    """

    def paginate(
        self, *, RoutingControlArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedRoute53HealthChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListAssociatedRoute53HealthChecks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listassociatedroute53healthcheckspaginator)
        """

class ListClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listclusterspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listclusterspaginator)
        """

class ListControlPanelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListControlPanels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listcontrolpanelspaginator)
    """

    def paginate(
        self, *, ClusterArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListControlPanelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListControlPanels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listcontrolpanelspaginator)
        """

class ListRoutingControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListRoutingControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listroutingcontrolspaginator)
    """

    def paginate(
        self, *, ControlPanelArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutingControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListRoutingControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listroutingcontrolspaginator)
        """

class ListSafetyRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListSafetyRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listsafetyrulespaginator)
    """

    def paginate(
        self, *, ControlPanelArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSafetyRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Paginator.ListSafetyRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators.html#listsafetyrulespaginator)
        """
