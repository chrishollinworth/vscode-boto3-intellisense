"""
Main interface for vpc-lattice service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_vpc_lattice import (
        Client,
        ListAccessLogSubscriptionsPaginator,
        ListDomainVerificationsPaginator,
        ListListenersPaginator,
        ListResourceConfigurationsPaginator,
        ListResourceEndpointAssociationsPaginator,
        ListResourceGatewaysPaginator,
        ListRulesPaginator,
        ListServiceNetworkResourceAssociationsPaginator,
        ListServiceNetworkServiceAssociationsPaginator,
        ListServiceNetworkVpcAssociationsPaginator,
        ListServiceNetworkVpcEndpointAssociationsPaginator,
        ListServiceNetworksPaginator,
        ListServicesPaginator,
        ListTargetGroupsPaginator,
        ListTargetsPaginator,
        VPCLatticeClient,
    )

    session = Session()
    client: VPCLatticeClient = session.client("vpc-lattice")

    list_access_log_subscriptions_paginator: ListAccessLogSubscriptionsPaginator = client.get_paginator("list_access_log_subscriptions")
    list_domain_verifications_paginator: ListDomainVerificationsPaginator = client.get_paginator("list_domain_verifications")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    list_resource_configurations_paginator: ListResourceConfigurationsPaginator = client.get_paginator("list_resource_configurations")
    list_resource_endpoint_associations_paginator: ListResourceEndpointAssociationsPaginator = client.get_paginator("list_resource_endpoint_associations")
    list_resource_gateways_paginator: ListResourceGatewaysPaginator = client.get_paginator("list_resource_gateways")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_service_network_resource_associations_paginator: ListServiceNetworkResourceAssociationsPaginator = client.get_paginator("list_service_network_resource_associations")
    list_service_network_service_associations_paginator: ListServiceNetworkServiceAssociationsPaginator = client.get_paginator("list_service_network_service_associations")
    list_service_network_vpc_associations_paginator: ListServiceNetworkVpcAssociationsPaginator = client.get_paginator("list_service_network_vpc_associations")
    list_service_network_vpc_endpoint_associations_paginator: ListServiceNetworkVpcEndpointAssociationsPaginator = client.get_paginator("list_service_network_vpc_endpoint_associations")
    list_service_networks_paginator: ListServiceNetworksPaginator = client.get_paginator("list_service_networks")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_target_groups_paginator: ListTargetGroupsPaginator = client.get_paginator("list_target_groups")
    list_targets_paginator: ListTargetsPaginator = client.get_paginator("list_targets")
    ```
"""

from .client import VPCLatticeClient
from .paginator import (
    ListAccessLogSubscriptionsPaginator,
    ListDomainVerificationsPaginator,
    ListListenersPaginator,
    ListResourceConfigurationsPaginator,
    ListResourceEndpointAssociationsPaginator,
    ListResourceGatewaysPaginator,
    ListRulesPaginator,
    ListServiceNetworkResourceAssociationsPaginator,
    ListServiceNetworkServiceAssociationsPaginator,
    ListServiceNetworksPaginator,
    ListServiceNetworkVpcAssociationsPaginator,
    ListServiceNetworkVpcEndpointAssociationsPaginator,
    ListServicesPaginator,
    ListTargetGroupsPaginator,
    ListTargetsPaginator,
)

Client = VPCLatticeClient

__all__ = (
    "Client",
    "ListAccessLogSubscriptionsPaginator",
    "ListDomainVerificationsPaginator",
    "ListListenersPaginator",
    "ListResourceConfigurationsPaginator",
    "ListResourceEndpointAssociationsPaginator",
    "ListResourceGatewaysPaginator",
    "ListRulesPaginator",
    "ListServiceNetworkResourceAssociationsPaginator",
    "ListServiceNetworkServiceAssociationsPaginator",
    "ListServiceNetworkVpcAssociationsPaginator",
    "ListServiceNetworkVpcEndpointAssociationsPaginator",
    "ListServiceNetworksPaginator",
    "ListServicesPaginator",
    "ListTargetGroupsPaginator",
    "ListTargetsPaginator",
    "VPCLatticeClient",
)
