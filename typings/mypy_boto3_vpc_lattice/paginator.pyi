"""
Type annotations for vpc-lattice service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_vpc_lattice import VPCLatticeClient
    from mypy_boto3_vpc_lattice.paginator import (
        ListAccessLogSubscriptionsPaginator,
        ListListenersPaginator,
        ListRulesPaginator,
        ListServiceNetworkServiceAssociationsPaginator,
        ListServiceNetworkVpcAssociationsPaginator,
        ListServiceNetworksPaginator,
        ListServicesPaginator,
        ListTargetGroupsPaginator,
        ListTargetsPaginator,
    )

    client: VPCLatticeClient = boto3.client("vpc-lattice")

    list_access_log_subscriptions_paginator: ListAccessLogSubscriptionsPaginator = client.get_paginator("list_access_log_subscriptions")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_service_network_service_associations_paginator: ListServiceNetworkServiceAssociationsPaginator = client.get_paginator("list_service_network_service_associations")
    list_service_network_vpc_associations_paginator: ListServiceNetworkVpcAssociationsPaginator = client.get_paginator("list_service_network_vpc_associations")
    list_service_networks_paginator: ListServiceNetworksPaginator = client.get_paginator("list_service_networks")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_target_groups_paginator: ListTargetGroupsPaginator = client.get_paginator("list_target_groups")
    list_targets_paginator: ListTargetsPaginator = client.get_paginator("list_targets")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import TargetGroupTypeType
from .type_defs import (
    ListAccessLogSubscriptionsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListRulesResponseTypeDef,
    ListServiceNetworkServiceAssociationsResponseTypeDef,
    ListServiceNetworksResponseTypeDef,
    ListServiceNetworkVpcAssociationsResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTargetGroupsResponseTypeDef,
    ListTargetsResponseTypeDef,
    PaginatorConfigTypeDef,
    TargetTypeDef,
)

__all__ = (
    "ListAccessLogSubscriptionsPaginator",
    "ListListenersPaginator",
    "ListRulesPaginator",
    "ListServiceNetworkServiceAssociationsPaginator",
    "ListServiceNetworkVpcAssociationsPaginator",
    "ListServiceNetworksPaginator",
    "ListServicesPaginator",
    "ListTargetGroupsPaginator",
    "ListTargetsPaginator",
)

class ListAccessLogSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListAccessLogSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listaccesslogsubscriptionspaginator)
    """

    def paginate(
        self, *, resourceIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessLogSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListAccessLogSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listaccesslogsubscriptionspaginator)
        """

class ListListenersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListListeners)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listlistenerspaginator)
    """

    def paginate(
        self, *, serviceIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListListenersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListListeners.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listlistenerspaginator)
        """

class ListRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listrulespaginator)
    """

    def paginate(
        self,
        *,
        listenerIdentifier: str,
        serviceIdentifier: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listrulespaginator)
        """

class ListServiceNetworkServiceAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkServiceAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkserviceassociationspaginator)
    """

    def paginate(
        self,
        *,
        serviceIdentifier: str = None,
        serviceNetworkIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceNetworkServiceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkServiceAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkserviceassociationspaginator)
        """

class ListServiceNetworkVpcAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkVpcAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkvpcassociationspaginator)
    """

    def paginate(
        self,
        *,
        serviceNetworkIdentifier: str = None,
        vpcIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceNetworkVpcAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkVpcAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkvpcassociationspaginator)
        """

class ListServiceNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkspaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicespaginator)
        """

class ListTargetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetgroupspaginator)
    """

    def paginate(
        self,
        *,
        targetGroupType: TargetGroupTypeType = None,
        vpcIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetgroupspaginator)
        """

class ListTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetspaginator)
    """

    def paginate(
        self,
        *,
        targetGroupIdentifier: str,
        targets: List["TargetTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetspaginator)
        """
