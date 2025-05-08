"""
Type annotations for elbv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elbv2.client import ElasticLoadBalancingv2Client

    session = Session()
    client: ElasticLoadBalancingv2Client = session.client("elbv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeAccountLimitsPaginator,
    DescribeListenerCertificatesPaginator,
    DescribeListenersPaginator,
    DescribeLoadBalancersPaginator,
    DescribeRulesPaginator,
    DescribeSSLPoliciesPaginator,
    DescribeTargetGroupsPaginator,
)
from .type_defs import (
    AddListenerCertificatesInputTypeDef,
    AddListenerCertificatesOutputTypeDef,
    AddTagsInputTypeDef,
    AddTrustStoreRevocationsInputTypeDef,
    AddTrustStoreRevocationsOutputTypeDef,
    CreateListenerInputTypeDef,
    CreateListenerOutputTypeDef,
    CreateLoadBalancerInputTypeDef,
    CreateLoadBalancerOutputTypeDef,
    CreateRuleInputTypeDef,
    CreateRuleOutputTypeDef,
    CreateTargetGroupInputTypeDef,
    CreateTargetGroupOutputTypeDef,
    CreateTrustStoreInputTypeDef,
    CreateTrustStoreOutputTypeDef,
    DeleteListenerInputTypeDef,
    DeleteLoadBalancerInputTypeDef,
    DeleteRuleInputTypeDef,
    DeleteSharedTrustStoreAssociationInputTypeDef,
    DeleteTargetGroupInputTypeDef,
    DeleteTrustStoreInputTypeDef,
    DeregisterTargetsInputTypeDef,
    DescribeAccountLimitsInputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeCapacityReservationInputTypeDef,
    DescribeCapacityReservationOutputTypeDef,
    DescribeListenerAttributesInputTypeDef,
    DescribeListenerAttributesOutputTypeDef,
    DescribeListenerCertificatesInputTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersInputTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancerAttributesInputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancersInputTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesInputTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesInputTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTagsInputTypeDef,
    DescribeTagsOutputTypeDef,
    DescribeTargetGroupAttributesInputTypeDef,
    DescribeTargetGroupAttributesOutputTypeDef,
    DescribeTargetGroupsInputTypeDef,
    DescribeTargetGroupsOutputTypeDef,
    DescribeTargetHealthInputTypeDef,
    DescribeTargetHealthOutputTypeDef,
    DescribeTrustStoreAssociationsInputTypeDef,
    DescribeTrustStoreAssociationsOutputTypeDef,
    DescribeTrustStoreRevocationsInputTypeDef,
    DescribeTrustStoreRevocationsOutputTypeDef,
    DescribeTrustStoresInputTypeDef,
    DescribeTrustStoresOutputTypeDef,
    GetResourcePolicyInputTypeDef,
    GetResourcePolicyOutputTypeDef,
    GetTrustStoreCaCertificatesBundleInputTypeDef,
    GetTrustStoreCaCertificatesBundleOutputTypeDef,
    GetTrustStoreRevocationContentInputTypeDef,
    GetTrustStoreRevocationContentOutputTypeDef,
    ModifyCapacityReservationInputTypeDef,
    ModifyCapacityReservationOutputTypeDef,
    ModifyIpPoolsInputTypeDef,
    ModifyIpPoolsOutputTypeDef,
    ModifyListenerAttributesInputTypeDef,
    ModifyListenerAttributesOutputTypeDef,
    ModifyListenerInputTypeDef,
    ModifyListenerOutputTypeDef,
    ModifyLoadBalancerAttributesInputTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    ModifyRuleInputTypeDef,
    ModifyRuleOutputTypeDef,
    ModifyTargetGroupAttributesInputTypeDef,
    ModifyTargetGroupAttributesOutputTypeDef,
    ModifyTargetGroupInputTypeDef,
    ModifyTargetGroupOutputTypeDef,
    ModifyTrustStoreInputTypeDef,
    ModifyTrustStoreOutputTypeDef,
    RegisterTargetsInputTypeDef,
    RemoveListenerCertificatesInputTypeDef,
    RemoveTagsInputTypeDef,
    RemoveTrustStoreRevocationsInputTypeDef,
    SetIpAddressTypeInputTypeDef,
    SetIpAddressTypeOutputTypeDef,
    SetRulePrioritiesInputTypeDef,
    SetRulePrioritiesOutputTypeDef,
    SetSecurityGroupsInputTypeDef,
    SetSecurityGroupsOutputTypeDef,
    SetSubnetsInputTypeDef,
    SetSubnetsOutputTypeDef,
)
from .waiter import (
    LoadBalancerAvailableWaiter,
    LoadBalancerExistsWaiter,
    LoadBalancersDeletedWaiter,
    TargetDeregisteredWaiter,
    TargetInServiceWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ElasticLoadBalancingv2Client",)

class Exceptions(BaseClientExceptions):
    ALPNPolicyNotSupportedException: Type[BotocoreClientError]
    AllocationIdNotFoundException: Type[BotocoreClientError]
    AvailabilityZoneNotSupportedException: Type[BotocoreClientError]
    CaCertificatesBundleNotFoundException: Type[BotocoreClientError]
    CapacityDecreaseRequestsLimitExceededException: Type[BotocoreClientError]
    CapacityReservationPendingException: Type[BotocoreClientError]
    CapacityUnitsLimitExceededException: Type[BotocoreClientError]
    CertificateNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DeleteAssociationSameAccountException: Type[BotocoreClientError]
    DuplicateListenerException: Type[BotocoreClientError]
    DuplicateLoadBalancerNameException: Type[BotocoreClientError]
    DuplicateTagKeysException: Type[BotocoreClientError]
    DuplicateTargetGroupNameException: Type[BotocoreClientError]
    DuplicateTrustStoreNameException: Type[BotocoreClientError]
    HealthUnavailableException: Type[BotocoreClientError]
    IncompatibleProtocolsException: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InvalidCaCertificatesBundleException: Type[BotocoreClientError]
    InvalidConfigurationRequestException: Type[BotocoreClientError]
    InvalidLoadBalancerActionException: Type[BotocoreClientError]
    InvalidRevocationContentException: Type[BotocoreClientError]
    InvalidSchemeException: Type[BotocoreClientError]
    InvalidSecurityGroupException: Type[BotocoreClientError]
    InvalidSubnetException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]
    LoadBalancerNotFoundException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    PriorRequestNotCompleteException: Type[BotocoreClientError]
    PriorityInUseException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RevocationContentNotFoundException: Type[BotocoreClientError]
    RevocationIdNotFoundException: Type[BotocoreClientError]
    RuleNotFoundException: Type[BotocoreClientError]
    SSLPolicyNotFoundException: Type[BotocoreClientError]
    SubnetNotFoundException: Type[BotocoreClientError]
    TargetGroupAssociationLimitException: Type[BotocoreClientError]
    TargetGroupNotFoundException: Type[BotocoreClientError]
    TooManyActionsException: Type[BotocoreClientError]
    TooManyCertificatesException: Type[BotocoreClientError]
    TooManyListenersException: Type[BotocoreClientError]
    TooManyLoadBalancersException: Type[BotocoreClientError]
    TooManyRegistrationsForTargetIdException: Type[BotocoreClientError]
    TooManyRulesException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    TooManyTargetGroupsException: Type[BotocoreClientError]
    TooManyTargetsException: Type[BotocoreClientError]
    TooManyTrustStoreRevocationEntriesException: Type[BotocoreClientError]
    TooManyTrustStoresException: Type[BotocoreClientError]
    TooManyUniqueTargetGroupsPerLoadBalancerException: Type[BotocoreClientError]
    TrustStoreAssociationNotFoundException: Type[BotocoreClientError]
    TrustStoreInUseException: Type[BotocoreClientError]
    TrustStoreNotFoundException: Type[BotocoreClientError]
    TrustStoreNotReadyException: Type[BotocoreClientError]
    UnsupportedProtocolException: Type[BotocoreClientError]

class ElasticLoadBalancingv2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElasticLoadBalancingv2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#generate_presigned_url)
        """

    def add_listener_certificates(
        self, **kwargs: Unpack[AddListenerCertificatesInputTypeDef]
    ) -> AddListenerCertificatesOutputTypeDef:
        """
        Adds the specified SSL server certificate to the certificate list for the
        specified HTTPS or TLS listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/add_listener_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#add_listener_certificates)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified Elastic Load Balancing resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/add_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#add_tags)
        """

    def add_trust_store_revocations(
        self, **kwargs: Unpack[AddTrustStoreRevocationsInputTypeDef]
    ) -> AddTrustStoreRevocationsOutputTypeDef:
        """
        Adds the specified revocation file to the specified trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/add_trust_store_revocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#add_trust_store_revocations)
        """

    def create_listener(
        self, **kwargs: Unpack[CreateListenerInputTypeDef]
    ) -> CreateListenerOutputTypeDef:
        """
        Creates a listener for the specified Application Load Balancer, Network Load
        Balancer, or Gateway Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/create_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#create_listener)
        """

    def create_load_balancer(
        self, **kwargs: Unpack[CreateLoadBalancerInputTypeDef]
    ) -> CreateLoadBalancerOutputTypeDef:
        """
        Creates an Application Load Balancer, Network Load Balancer, or Gateway Load
        Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/create_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#create_load_balancer)
        """

    def create_rule(self, **kwargs: Unpack[CreateRuleInputTypeDef]) -> CreateRuleOutputTypeDef:
        """
        Creates a rule for the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/create_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#create_rule)
        """

    def create_target_group(
        self, **kwargs: Unpack[CreateTargetGroupInputTypeDef]
    ) -> CreateTargetGroupOutputTypeDef:
        """
        Creates a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/create_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#create_target_group)
        """

    def create_trust_store(
        self, **kwargs: Unpack[CreateTrustStoreInputTypeDef]
    ) -> CreateTrustStoreOutputTypeDef:
        """
        Creates a trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/create_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#create_trust_store)
        """

    def delete_listener(self, **kwargs: Unpack[DeleteListenerInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_listener)
        """

    def delete_load_balancer(
        self, **kwargs: Unpack[DeleteLoadBalancerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified Application Load Balancer, Network Load Balancer, or
        Gateway Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_load_balancer)
        """

    def delete_rule(self, **kwargs: Unpack[DeleteRuleInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_rule)
        """

    def delete_shared_trust_store_association(
        self, **kwargs: Unpack[DeleteSharedTrustStoreAssociationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a shared trust store association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_shared_trust_store_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_shared_trust_store_association)
        """

    def delete_target_group(
        self, **kwargs: Unpack[DeleteTargetGroupInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_target_group)
        """

    def delete_trust_store(self, **kwargs: Unpack[DeleteTrustStoreInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/delete_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#delete_trust_store)
        """

    def deregister_targets(self, **kwargs: Unpack[DeregisterTargetsInputTypeDef]) -> Dict[str, Any]:
        """
        Deregisters the specified targets from the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/deregister_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#deregister_targets)
        """

    def describe_account_limits(
        self, **kwargs: Unpack[DescribeAccountLimitsInputTypeDef]
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        Describes the current Elastic Load Balancing resource limits for your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_account_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_account_limits)
        """

    def describe_capacity_reservation(
        self, **kwargs: Unpack[DescribeCapacityReservationInputTypeDef]
    ) -> DescribeCapacityReservationOutputTypeDef:
        """
        Describes the capacity reservation status for the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_capacity_reservation)
        """

    def describe_listener_attributes(
        self, **kwargs: Unpack[DescribeListenerAttributesInputTypeDef]
    ) -> DescribeListenerAttributesOutputTypeDef:
        """
        Describes the attributes for the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_listener_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_listener_attributes)
        """

    def describe_listener_certificates(
        self, **kwargs: Unpack[DescribeListenerCertificatesInputTypeDef]
    ) -> DescribeListenerCertificatesOutputTypeDef:
        """
        Describes the default certificate and the certificate list for the specified
        HTTPS or TLS listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_listener_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_listener_certificates)
        """

    def describe_listeners(
        self, **kwargs: Unpack[DescribeListenersInputTypeDef]
    ) -> DescribeListenersOutputTypeDef:
        """
        Describes the specified listeners or the listeners for the specified
        Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_listeners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_listeners)
        """

    def describe_load_balancer_attributes(
        self, **kwargs: Unpack[DescribeLoadBalancerAttributesInputTypeDef]
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        Describes the attributes for the specified Application Load Balancer, Network
        Load Balancer, or Gateway Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_load_balancer_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_load_balancer_attributes)
        """

    def describe_load_balancers(
        self, **kwargs: Unpack[DescribeLoadBalancersInputTypeDef]
    ) -> DescribeLoadBalancersOutputTypeDef:
        """
        Describes the specified load balancers or all of your load balancers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_load_balancers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_load_balancers)
        """

    def describe_rules(
        self, **kwargs: Unpack[DescribeRulesInputTypeDef]
    ) -> DescribeRulesOutputTypeDef:
        """
        Describes the specified rules or the rules for the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_rules)
        """

    def describe_ssl_policies(
        self, **kwargs: Unpack[DescribeSSLPoliciesInputTypeDef]
    ) -> DescribeSSLPoliciesOutputTypeDef:
        """
        Describes the specified policies or all policies used for SSL negotiation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_ssl_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_ssl_policies)
        """

    def describe_tags(
        self, **kwargs: Unpack[DescribeTagsInputTypeDef]
    ) -> DescribeTagsOutputTypeDef:
        """
        Describes the tags for the specified Elastic Load Balancing resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_tags)
        """

    def describe_target_group_attributes(
        self, **kwargs: Unpack[DescribeTargetGroupAttributesInputTypeDef]
    ) -> DescribeTargetGroupAttributesOutputTypeDef:
        """
        Describes the attributes for the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_target_group_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_target_group_attributes)
        """

    def describe_target_groups(
        self, **kwargs: Unpack[DescribeTargetGroupsInputTypeDef]
    ) -> DescribeTargetGroupsOutputTypeDef:
        """
        Describes the specified target groups or all of your target groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_target_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_target_groups)
        """

    def describe_target_health(
        self, **kwargs: Unpack[DescribeTargetHealthInputTypeDef]
    ) -> DescribeTargetHealthOutputTypeDef:
        """
        Describes the health of the specified targets or all of your targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_target_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_target_health)
        """

    def describe_trust_store_associations(
        self, **kwargs: Unpack[DescribeTrustStoreAssociationsInputTypeDef]
    ) -> DescribeTrustStoreAssociationsOutputTypeDef:
        """
        Describes all resources associated with the specified trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_trust_store_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_trust_store_associations)
        """

    def describe_trust_store_revocations(
        self, **kwargs: Unpack[DescribeTrustStoreRevocationsInputTypeDef]
    ) -> DescribeTrustStoreRevocationsOutputTypeDef:
        """
        Describes the revocation files in use by the specified trust store or
        revocation files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_trust_store_revocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_trust_store_revocations)
        """

    def describe_trust_stores(
        self, **kwargs: Unpack[DescribeTrustStoresInputTypeDef]
    ) -> DescribeTrustStoresOutputTypeDef:
        """
        Describes all trust stores for the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/describe_trust_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#describe_trust_stores)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyInputTypeDef]
    ) -> GetResourcePolicyOutputTypeDef:
        """
        Retrieves the resource policy for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_resource_policy)
        """

    def get_trust_store_ca_certificates_bundle(
        self, **kwargs: Unpack[GetTrustStoreCaCertificatesBundleInputTypeDef]
    ) -> GetTrustStoreCaCertificatesBundleOutputTypeDef:
        """
        Retrieves the ca certificate bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_trust_store_ca_certificates_bundle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_trust_store_ca_certificates_bundle)
        """

    def get_trust_store_revocation_content(
        self, **kwargs: Unpack[GetTrustStoreRevocationContentInputTypeDef]
    ) -> GetTrustStoreRevocationContentOutputTypeDef:
        """
        Retrieves the specified revocation file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_trust_store_revocation_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_trust_store_revocation_content)
        """

    def modify_capacity_reservation(
        self, **kwargs: Unpack[ModifyCapacityReservationInputTypeDef]
    ) -> ModifyCapacityReservationOutputTypeDef:
        """
        Modifies the capacity reservation of the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_capacity_reservation)
        """

    def modify_ip_pools(
        self, **kwargs: Unpack[ModifyIpPoolsInputTypeDef]
    ) -> ModifyIpPoolsOutputTypeDef:
        """
        [Application Load Balancers] Modify the IP pool associated to a load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_ip_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_ip_pools)
        """

    def modify_listener(
        self, **kwargs: Unpack[ModifyListenerInputTypeDef]
    ) -> ModifyListenerOutputTypeDef:
        """
        Replaces the specified properties of the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_listener)
        """

    def modify_listener_attributes(
        self, **kwargs: Unpack[ModifyListenerAttributesInputTypeDef]
    ) -> ModifyListenerAttributesOutputTypeDef:
        """
        Modifies the specified attributes of the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_listener_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_listener_attributes)
        """

    def modify_load_balancer_attributes(
        self, **kwargs: Unpack[ModifyLoadBalancerAttributesInputTypeDef]
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        Modifies the specified attributes of the specified Application Load Balancer,
        Network Load Balancer, or Gateway Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_load_balancer_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_load_balancer_attributes)
        """

    def modify_rule(self, **kwargs: Unpack[ModifyRuleInputTypeDef]) -> ModifyRuleOutputTypeDef:
        """
        Replaces the specified properties of the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_rule)
        """

    def modify_target_group(
        self, **kwargs: Unpack[ModifyTargetGroupInputTypeDef]
    ) -> ModifyTargetGroupOutputTypeDef:
        """
        Modifies the health checks used when evaluating the health state of the targets
        in the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_target_group)
        """

    def modify_target_group_attributes(
        self, **kwargs: Unpack[ModifyTargetGroupAttributesInputTypeDef]
    ) -> ModifyTargetGroupAttributesOutputTypeDef:
        """
        Modifies the specified attributes of the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_target_group_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_target_group_attributes)
        """

    def modify_trust_store(
        self, **kwargs: Unpack[ModifyTrustStoreInputTypeDef]
    ) -> ModifyTrustStoreOutputTypeDef:
        """
        Update the ca certificate bundle for the specified trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/modify_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#modify_trust_store)
        """

    def register_targets(self, **kwargs: Unpack[RegisterTargetsInputTypeDef]) -> Dict[str, Any]:
        """
        Registers the specified targets with the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/register_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#register_targets)
        """

    def remove_listener_certificates(
        self, **kwargs: Unpack[RemoveListenerCertificatesInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified certificate from the certificate list for the specified
        HTTPS or TLS listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/remove_listener_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#remove_listener_certificates)
        """

    def remove_tags(self, **kwargs: Unpack[RemoveTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Elastic Load Balancing resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/remove_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#remove_tags)
        """

    def remove_trust_store_revocations(
        self, **kwargs: Unpack[RemoveTrustStoreRevocationsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified revocation file from the specified trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/remove_trust_store_revocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#remove_trust_store_revocations)
        """

    def set_ip_address_type(
        self, **kwargs: Unpack[SetIpAddressTypeInputTypeDef]
    ) -> SetIpAddressTypeOutputTypeDef:
        """
        Sets the type of IP addresses used by the subnets of the specified load
        balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/set_ip_address_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#set_ip_address_type)
        """

    def set_rule_priorities(
        self, **kwargs: Unpack[SetRulePrioritiesInputTypeDef]
    ) -> SetRulePrioritiesOutputTypeDef:
        """
        Sets the priorities of the specified rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/set_rule_priorities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#set_rule_priorities)
        """

    def set_security_groups(
        self, **kwargs: Unpack[SetSecurityGroupsInputTypeDef]
    ) -> SetSecurityGroupsOutputTypeDef:
        """
        Associates the specified security groups with the specified Application Load
        Balancer or Network Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/set_security_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#set_security_groups)
        """

    def set_subnets(self, **kwargs: Unpack[SetSubnetsInputTypeDef]) -> SetSubnetsOutputTypeDef:
        """
        Enables the Availability Zones for the specified public subnets for the
        specified Application Load Balancer, Network Load Balancer or Gateway Load
        Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/set_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#set_subnets)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_listener_certificates"]
    ) -> DescribeListenerCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_listeners"]
    ) -> DescribeListenersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_load_balancers"]
    ) -> DescribeLoadBalancersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_rules"]
    ) -> DescribeRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ssl_policies"]
    ) -> DescribeSSLPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_target_groups"]
    ) -> DescribeTargetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["load_balancer_available"]
    ) -> LoadBalancerAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["load_balancer_exists"]
    ) -> LoadBalancerExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["load_balancers_deleted"]
    ) -> LoadBalancersDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["target_deregistered"]
    ) -> TargetDeregisteredWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["target_in_service"]
    ) -> TargetInServiceWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/client/#get_waiter)
        """
