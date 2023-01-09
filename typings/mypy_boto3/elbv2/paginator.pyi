"""
Type annotations for elbv2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_elbv2 import ElasticLoadBalancingv2Client
    from mypy_boto3_elbv2.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeListenerCertificatesPaginator,
        DescribeListenersPaginator,
        DescribeLoadBalancersPaginator,
        DescribeRulesPaginator,
        DescribeSSLPoliciesPaginator,
        DescribeTargetGroupsPaginator,
    )

    client: ElasticLoadBalancingv2Client = boto3.client("elbv2")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_listener_certificates_paginator: DescribeListenerCertificatesPaginator = client.get_paginator("describe_listener_certificates")
    describe_listeners_paginator: DescribeListenersPaginator = client.get_paginator("describe_listeners")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    describe_rules_paginator: DescribeRulesPaginator = client.get_paginator("describe_rules")
    describe_ssl_policies_paginator: DescribeSSLPoliciesPaginator = client.get_paginator("describe_ssl_policies")
    describe_target_groups_paginator: DescribeTargetGroupsPaginator = client.get_paginator("describe_target_groups")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import LoadBalancerTypeEnumType
from .type_defs import (
    DescribeAccountLimitsOutputTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTargetGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
)

class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describeaccountlimitspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describeaccountlimitspaginator)
        """

class DescribeListenerCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describelistenercertificatespaginator)
    """

    def paginate(
        self, *, ListenerArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeListenerCertificatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describelistenercertificatespaginator)
        """

class DescribeListenersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describelistenerspaginator)
    """

    def paginate(
        self,
        *,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeListenersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describelistenerspaginator)
        """

class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describeloadbalancerspaginator)
    """

    def paginate(
        self,
        *,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describeloadbalancerspaginator)
        """

class DescribeRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describerulespaginator)
    """

    def paginate(
        self,
        *,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describerulespaginator)
        """

class DescribeSSLPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describesslpoliciespaginator)
    """

    def paginate(
        self,
        *,
        Names: List[str] = None,
        LoadBalancerType: LoadBalancerTypeEnumType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSSLPoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describesslpoliciespaginator)
        """

class DescribeTargetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describetargetgroupspaginator)
    """

    def paginate(
        self,
        *,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTargetGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators.html#describetargetgroupspaginator)
        """
