"""
Main interface for elbv2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elbv2 import (
        Client,
        DescribeAccountLimitsPaginator,
        DescribeListenerCertificatesPaginator,
        DescribeListenersPaginator,
        DescribeLoadBalancersPaginator,
        DescribeRulesPaginator,
        DescribeSSLPoliciesPaginator,
        DescribeTargetGroupsPaginator,
        DescribeTrustStoreAssociationsPaginator,
        DescribeTrustStoreRevocationsPaginator,
        DescribeTrustStoresPaginator,
        ElasticLoadBalancingv2Client,
        LoadBalancerAvailableWaiter,
        LoadBalancerExistsWaiter,
        LoadBalancersDeletedWaiter,
        TargetDeregisteredWaiter,
        TargetInServiceWaiter,
    )

    session = Session()
    client: ElasticLoadBalancingv2Client = session.client("elbv2")

    load_balancer_available_waiter: LoadBalancerAvailableWaiter = client.get_waiter("load_balancer_available")
    load_balancer_exists_waiter: LoadBalancerExistsWaiter = client.get_waiter("load_balancer_exists")
    load_balancers_deleted_waiter: LoadBalancersDeletedWaiter = client.get_waiter("load_balancers_deleted")
    target_deregistered_waiter: TargetDeregisteredWaiter = client.get_waiter("target_deregistered")
    target_in_service_waiter: TargetInServiceWaiter = client.get_waiter("target_in_service")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_listener_certificates_paginator: DescribeListenerCertificatesPaginator = client.get_paginator("describe_listener_certificates")
    describe_listeners_paginator: DescribeListenersPaginator = client.get_paginator("describe_listeners")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    describe_rules_paginator: DescribeRulesPaginator = client.get_paginator("describe_rules")
    describe_ssl_policies_paginator: DescribeSSLPoliciesPaginator = client.get_paginator("describe_ssl_policies")
    describe_target_groups_paginator: DescribeTargetGroupsPaginator = client.get_paginator("describe_target_groups")
    describe_trust_store_associations_paginator: DescribeTrustStoreAssociationsPaginator = client.get_paginator("describe_trust_store_associations")
    describe_trust_store_revocations_paginator: DescribeTrustStoreRevocationsPaginator = client.get_paginator("describe_trust_store_revocations")
    describe_trust_stores_paginator: DescribeTrustStoresPaginator = client.get_paginator("describe_trust_stores")
    ```
"""

from .client import ElasticLoadBalancingv2Client
from .paginator import (
    DescribeAccountLimitsPaginator,
    DescribeListenerCertificatesPaginator,
    DescribeListenersPaginator,
    DescribeLoadBalancersPaginator,
    DescribeRulesPaginator,
    DescribeSSLPoliciesPaginator,
    DescribeTargetGroupsPaginator,
    DescribeTrustStoreAssociationsPaginator,
    DescribeTrustStoreRevocationsPaginator,
    DescribeTrustStoresPaginator,
)
from .waiter import (
    LoadBalancerAvailableWaiter,
    LoadBalancerExistsWaiter,
    LoadBalancersDeletedWaiter,
    TargetDeregisteredWaiter,
    TargetInServiceWaiter,
)

Client = ElasticLoadBalancingv2Client

__all__ = (
    "Client",
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
    "DescribeTrustStoreAssociationsPaginator",
    "DescribeTrustStoreRevocationsPaginator",
    "DescribeTrustStoresPaginator",
    "ElasticLoadBalancingv2Client",
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)
