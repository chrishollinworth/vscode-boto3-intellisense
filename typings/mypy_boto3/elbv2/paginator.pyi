"""
Type annotations for elbv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elbv2.client import ElasticLoadBalancingv2Client
    from mypy_boto3_elbv2.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeListenerCertificatesPaginator,
        DescribeListenersPaginator,
        DescribeLoadBalancersPaginator,
        DescribeRulesPaginator,
        DescribeSSLPoliciesPaginator,
        DescribeTargetGroupsPaginator,
    )

    session = Session()
    client: ElasticLoadBalancingv2Client = session.client("elbv2")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_listener_certificates_paginator: DescribeListenerCertificatesPaginator = client.get_paginator("describe_listener_certificates")
    describe_listeners_paginator: DescribeListenersPaginator = client.get_paginator("describe_listeners")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    describe_rules_paginator: DescribeRulesPaginator = client.get_paginator("describe_rules")
    describe_ssl_policies_paginator: DescribeSSLPoliciesPaginator = client.get_paginator("describe_ssl_policies")
    describe_target_groups_paginator: DescribeTargetGroupsPaginator = client.get_paginator("describe_target_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAccountLimitsInputPaginateTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeListenerCertificatesInputPaginateTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersInputPaginateTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancersInputPaginateTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesInputPaginateTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesInputPaginateTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTargetGroupsInputPaginateTypeDef,
    DescribeTargetGroupsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
)

if TYPE_CHECKING:
    _DescribeAccountLimitsPaginatorBase = Paginator[DescribeAccountLimitsOutputTypeDef]
else:
    _DescribeAccountLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAccountLimitsPaginator(_DescribeAccountLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeAccountLimits.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describeaccountlimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccountLimitsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeAccountLimits.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describeaccountlimitspaginator)
        """

if TYPE_CHECKING:
    _DescribeListenerCertificatesPaginatorBase = Paginator[
        DescribeListenerCertificatesOutputTypeDef
    ]
else:
    _DescribeListenerCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeListenerCertificatesPaginator(_DescribeListenerCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeListenerCertificates.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describelistenercertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeListenerCertificatesInputPaginateTypeDef]
    ) -> PageIterator[DescribeListenerCertificatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeListenerCertificates.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describelistenercertificatespaginator)
        """

if TYPE_CHECKING:
    _DescribeListenersPaginatorBase = Paginator[DescribeListenersOutputTypeDef]
else:
    _DescribeListenersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeListenersPaginator(_DescribeListenersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeListeners.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describelistenerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeListenersInputPaginateTypeDef]
    ) -> PageIterator[DescribeListenersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeListeners.html#ElasticLoadBalancingv2.Paginator.DescribeListeners.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describelistenerspaginator)
        """

if TYPE_CHECKING:
    _DescribeLoadBalancersPaginatorBase = Paginator[DescribeLoadBalancersOutputTypeDef]
else:
    _DescribeLoadBalancersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLoadBalancersPaginator(_DescribeLoadBalancersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeLoadBalancers.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describeloadbalancerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancersInputPaginateTypeDef]
    ) -> PageIterator[DescribeLoadBalancersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeLoadBalancers.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describeloadbalancerspaginator)
        """

if TYPE_CHECKING:
    _DescribeRulesPaginatorBase = Paginator[DescribeRulesOutputTypeDef]
else:
    _DescribeRulesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRulesPaginator(_DescribeRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeRules.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describerulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRulesInputPaginateTypeDef]
    ) -> PageIterator[DescribeRulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeRules.html#ElasticLoadBalancingv2.Paginator.DescribeRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describerulespaginator)
        """

if TYPE_CHECKING:
    _DescribeSSLPoliciesPaginatorBase = Paginator[DescribeSSLPoliciesOutputTypeDef]
else:
    _DescribeSSLPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSSLPoliciesPaginator(_DescribeSSLPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeSSLPolicies.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describesslpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSSLPoliciesInputPaginateTypeDef]
    ) -> PageIterator[DescribeSSLPoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeSSLPolicies.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describesslpoliciespaginator)
        """

if TYPE_CHECKING:
    _DescribeTargetGroupsPaginatorBase = Paginator[DescribeTargetGroupsOutputTypeDef]
else:
    _DescribeTargetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTargetGroupsPaginator(_DescribeTargetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeTargetGroups.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describetargetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTargetGroupsInputPaginateTypeDef]
    ) -> PageIterator[DescribeTargetGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/paginator/DescribeTargetGroups.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/paginators/#describetargetgroupspaginator)
        """
