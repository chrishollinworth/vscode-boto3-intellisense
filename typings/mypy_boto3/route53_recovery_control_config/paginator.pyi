"""
Type annotations for route53-recovery-control-config service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53_recovery_control_config.client import Route53RecoveryControlConfigClient
    from mypy_boto3_route53_recovery_control_config.paginator import (
        ListAssociatedRoute53HealthChecksPaginator,
        ListClustersPaginator,
        ListControlPanelsPaginator,
        ListRoutingControlsPaginator,
        ListSafetyRulesPaginator,
    )

    session = Session()
    client: Route53RecoveryControlConfigClient = session.client("route53-recovery-control-config")

    list_associated_route53_health_checks_paginator: ListAssociatedRoute53HealthChecksPaginator = client.get_paginator("list_associated_route53_health_checks")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_control_panels_paginator: ListControlPanelsPaginator = client.get_paginator("list_control_panels")
    list_routing_controls_paginator: ListRoutingControlsPaginator = client.get_paginator("list_routing_controls")
    list_safety_rules_paginator: ListSafetyRulesPaginator = client.get_paginator("list_safety_rules")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssociatedRoute53HealthChecksRequestPaginateTypeDef,
    ListAssociatedRoute53HealthChecksResponseTypeDef,
    ListClustersRequestPaginateTypeDef,
    ListClustersResponseTypeDef,
    ListControlPanelsRequestPaginateTypeDef,
    ListControlPanelsResponseTypeDef,
    ListRoutingControlsRequestPaginateTypeDef,
    ListRoutingControlsResponseTypeDef,
    ListSafetyRulesRequestPaginateTypeDef,
    ListSafetyRulesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssociatedRoute53HealthChecksPaginator",
    "ListClustersPaginator",
    "ListControlPanelsPaginator",
    "ListRoutingControlsPaginator",
    "ListSafetyRulesPaginator",
)

if TYPE_CHECKING:
    _ListAssociatedRoute53HealthChecksPaginatorBase = Paginator[
        ListAssociatedRoute53HealthChecksResponseTypeDef
    ]
else:
    _ListAssociatedRoute53HealthChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedRoute53HealthChecksPaginator(_ListAssociatedRoute53HealthChecksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListAssociatedRoute53HealthChecks.html#Route53RecoveryControlConfig.Paginator.ListAssociatedRoute53HealthChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listassociatedroute53healthcheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedRoute53HealthChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedRoute53HealthChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListAssociatedRoute53HealthChecks.html#Route53RecoveryControlConfig.Paginator.ListAssociatedRoute53HealthChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listassociatedroute53healthcheckspaginator)
        """

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersResponseTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListClusters.html#Route53RecoveryControlConfig.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListClusters.html#Route53RecoveryControlConfig.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListControlPanelsPaginatorBase = Paginator[ListControlPanelsResponseTypeDef]
else:
    _ListControlPanelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListControlPanelsPaginator(_ListControlPanelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListControlPanels.html#Route53RecoveryControlConfig.Paginator.ListControlPanels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listcontrolpanelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListControlPanelsRequestPaginateTypeDef]
    ) -> PageIterator[ListControlPanelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListControlPanels.html#Route53RecoveryControlConfig.Paginator.ListControlPanels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listcontrolpanelspaginator)
        """

if TYPE_CHECKING:
    _ListRoutingControlsPaginatorBase = Paginator[ListRoutingControlsResponseTypeDef]
else:
    _ListRoutingControlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoutingControlsPaginator(_ListRoutingControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListRoutingControls.html#Route53RecoveryControlConfig.Paginator.ListRoutingControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listroutingcontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoutingControlsRequestPaginateTypeDef]
    ) -> PageIterator[ListRoutingControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListRoutingControls.html#Route53RecoveryControlConfig.Paginator.ListRoutingControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listroutingcontrolspaginator)
        """

if TYPE_CHECKING:
    _ListSafetyRulesPaginatorBase = Paginator[ListSafetyRulesResponseTypeDef]
else:
    _ListSafetyRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSafetyRulesPaginator(_ListSafetyRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListSafetyRules.html#Route53RecoveryControlConfig.Paginator.ListSafetyRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listsafetyrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSafetyRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListSafetyRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/paginator/ListSafetyRules.html#Route53RecoveryControlConfig.Paginator.ListSafetyRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/paginators/#listsafetyrulespaginator)
        """
