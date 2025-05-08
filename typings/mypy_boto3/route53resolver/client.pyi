"""
Type annotations for route53resolver service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53resolver.client import Route53ResolverClient

    session = Session()
    client: Route53ResolverClient = session.client("route53resolver")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListFirewallConfigsPaginator,
    ListFirewallDomainListsPaginator,
    ListFirewallDomainsPaginator,
    ListFirewallRuleGroupAssociationsPaginator,
    ListFirewallRuleGroupsPaginator,
    ListFirewallRulesPaginator,
    ListOutpostResolversPaginator,
    ListResolverConfigsPaginator,
    ListResolverDnssecConfigsPaginator,
    ListResolverEndpointIpAddressesPaginator,
    ListResolverEndpointsPaginator,
    ListResolverQueryLogConfigAssociationsPaginator,
    ListResolverQueryLogConfigsPaginator,
    ListResolverRuleAssociationsPaginator,
    ListResolverRulesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFirewallRuleGroupRequestTypeDef,
    AssociateFirewallRuleGroupResponseTypeDef,
    AssociateResolverEndpointIpAddressRequestTypeDef,
    AssociateResolverEndpointIpAddressResponseTypeDef,
    AssociateResolverQueryLogConfigRequestTypeDef,
    AssociateResolverQueryLogConfigResponseTypeDef,
    AssociateResolverRuleRequestTypeDef,
    AssociateResolverRuleResponseTypeDef,
    CreateFirewallDomainListRequestTypeDef,
    CreateFirewallDomainListResponseTypeDef,
    CreateFirewallRuleGroupRequestTypeDef,
    CreateFirewallRuleGroupResponseTypeDef,
    CreateFirewallRuleRequestTypeDef,
    CreateFirewallRuleResponseTypeDef,
    CreateOutpostResolverRequestTypeDef,
    CreateOutpostResolverResponseTypeDef,
    CreateResolverEndpointRequestTypeDef,
    CreateResolverEndpointResponseTypeDef,
    CreateResolverQueryLogConfigRequestTypeDef,
    CreateResolverQueryLogConfigResponseTypeDef,
    CreateResolverRuleRequestTypeDef,
    CreateResolverRuleResponseTypeDef,
    DeleteFirewallDomainListRequestTypeDef,
    DeleteFirewallDomainListResponseTypeDef,
    DeleteFirewallRuleGroupRequestTypeDef,
    DeleteFirewallRuleGroupResponseTypeDef,
    DeleteFirewallRuleRequestTypeDef,
    DeleteFirewallRuleResponseTypeDef,
    DeleteOutpostResolverRequestTypeDef,
    DeleteOutpostResolverResponseTypeDef,
    DeleteResolverEndpointRequestTypeDef,
    DeleteResolverEndpointResponseTypeDef,
    DeleteResolverQueryLogConfigRequestTypeDef,
    DeleteResolverQueryLogConfigResponseTypeDef,
    DeleteResolverRuleRequestTypeDef,
    DeleteResolverRuleResponseTypeDef,
    DisassociateFirewallRuleGroupRequestTypeDef,
    DisassociateFirewallRuleGroupResponseTypeDef,
    DisassociateResolverEndpointIpAddressRequestTypeDef,
    DisassociateResolverEndpointIpAddressResponseTypeDef,
    DisassociateResolverQueryLogConfigRequestTypeDef,
    DisassociateResolverQueryLogConfigResponseTypeDef,
    DisassociateResolverRuleRequestTypeDef,
    DisassociateResolverRuleResponseTypeDef,
    GetFirewallConfigRequestTypeDef,
    GetFirewallConfigResponseTypeDef,
    GetFirewallDomainListRequestTypeDef,
    GetFirewallDomainListResponseTypeDef,
    GetFirewallRuleGroupAssociationRequestTypeDef,
    GetFirewallRuleGroupAssociationResponseTypeDef,
    GetFirewallRuleGroupPolicyRequestTypeDef,
    GetFirewallRuleGroupPolicyResponseTypeDef,
    GetFirewallRuleGroupRequestTypeDef,
    GetFirewallRuleGroupResponseTypeDef,
    GetOutpostResolverRequestTypeDef,
    GetOutpostResolverResponseTypeDef,
    GetResolverConfigRequestTypeDef,
    GetResolverConfigResponseTypeDef,
    GetResolverDnssecConfigRequestTypeDef,
    GetResolverDnssecConfigResponseTypeDef,
    GetResolverEndpointRequestTypeDef,
    GetResolverEndpointResponseTypeDef,
    GetResolverQueryLogConfigAssociationRequestTypeDef,
    GetResolverQueryLogConfigAssociationResponseTypeDef,
    GetResolverQueryLogConfigPolicyRequestTypeDef,
    GetResolverQueryLogConfigPolicyResponseTypeDef,
    GetResolverQueryLogConfigRequestTypeDef,
    GetResolverQueryLogConfigResponseTypeDef,
    GetResolverRuleAssociationRequestTypeDef,
    GetResolverRuleAssociationResponseTypeDef,
    GetResolverRulePolicyRequestTypeDef,
    GetResolverRulePolicyResponseTypeDef,
    GetResolverRuleRequestTypeDef,
    GetResolverRuleResponseTypeDef,
    ImportFirewallDomainsRequestTypeDef,
    ImportFirewallDomainsResponseTypeDef,
    ListFirewallConfigsRequestTypeDef,
    ListFirewallConfigsResponseTypeDef,
    ListFirewallDomainListsRequestTypeDef,
    ListFirewallDomainListsResponseTypeDef,
    ListFirewallDomainsRequestTypeDef,
    ListFirewallDomainsResponseTypeDef,
    ListFirewallRuleGroupAssociationsRequestTypeDef,
    ListFirewallRuleGroupAssociationsResponseTypeDef,
    ListFirewallRuleGroupsRequestTypeDef,
    ListFirewallRuleGroupsResponseTypeDef,
    ListFirewallRulesRequestTypeDef,
    ListFirewallRulesResponseTypeDef,
    ListOutpostResolversRequestTypeDef,
    ListOutpostResolversResponseTypeDef,
    ListResolverConfigsRequestTypeDef,
    ListResolverConfigsResponseTypeDef,
    ListResolverDnssecConfigsRequestTypeDef,
    ListResolverDnssecConfigsResponseTypeDef,
    ListResolverEndpointIpAddressesRequestTypeDef,
    ListResolverEndpointIpAddressesResponseTypeDef,
    ListResolverEndpointsRequestTypeDef,
    ListResolverEndpointsResponseTypeDef,
    ListResolverQueryLogConfigAssociationsRequestTypeDef,
    ListResolverQueryLogConfigAssociationsResponseTypeDef,
    ListResolverQueryLogConfigsRequestTypeDef,
    ListResolverQueryLogConfigsResponseTypeDef,
    ListResolverRuleAssociationsRequestTypeDef,
    ListResolverRuleAssociationsResponseTypeDef,
    ListResolverRulesRequestTypeDef,
    ListResolverRulesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutFirewallRuleGroupPolicyRequestTypeDef,
    PutFirewallRuleGroupPolicyResponseTypeDef,
    PutResolverQueryLogConfigPolicyRequestTypeDef,
    PutResolverQueryLogConfigPolicyResponseTypeDef,
    PutResolverRulePolicyRequestTypeDef,
    PutResolverRulePolicyResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateFirewallConfigRequestTypeDef,
    UpdateFirewallConfigResponseTypeDef,
    UpdateFirewallDomainsRequestTypeDef,
    UpdateFirewallDomainsResponseTypeDef,
    UpdateFirewallRuleGroupAssociationRequestTypeDef,
    UpdateFirewallRuleGroupAssociationResponseTypeDef,
    UpdateFirewallRuleRequestTypeDef,
    UpdateFirewallRuleResponseTypeDef,
    UpdateOutpostResolverRequestTypeDef,
    UpdateOutpostResolverResponseTypeDef,
    UpdateResolverConfigRequestTypeDef,
    UpdateResolverConfigResponseTypeDef,
    UpdateResolverDnssecConfigRequestTypeDef,
    UpdateResolverDnssecConfigResponseTypeDef,
    UpdateResolverEndpointRequestTypeDef,
    UpdateResolverEndpointResponseTypeDef,
    UpdateResolverRuleRequestTypeDef,
    UpdateResolverRuleResponseTypeDef,
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

__all__ = ("Route53ResolverClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPolicyDocument: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnknownResourceException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53ResolverClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53ResolverClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html#Route53Resolver.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#generate_presigned_url)
        """

    def associate_firewall_rule_group(
        self, **kwargs: Unpack[AssociateFirewallRuleGroupRequestTypeDef]
    ) -> AssociateFirewallRuleGroupResponseTypeDef:
        """
        Associates a <a>FirewallRuleGroup</a> with a VPC, to provide DNS filtering for
        the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/associate_firewall_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#associate_firewall_rule_group)
        """

    def associate_resolver_endpoint_ip_address(
        self, **kwargs: Unpack[AssociateResolverEndpointIpAddressRequestTypeDef]
    ) -> AssociateResolverEndpointIpAddressResponseTypeDef:
        """
        Adds IP addresses to an inbound or an outbound Resolver endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/associate_resolver_endpoint_ip_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#associate_resolver_endpoint_ip_address)
        """

    def associate_resolver_query_log_config(
        self, **kwargs: Unpack[AssociateResolverQueryLogConfigRequestTypeDef]
    ) -> AssociateResolverQueryLogConfigResponseTypeDef:
        """
        Associates an Amazon VPC with a specified query logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/associate_resolver_query_log_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#associate_resolver_query_log_config)
        """

    def associate_resolver_rule(
        self, **kwargs: Unpack[AssociateResolverRuleRequestTypeDef]
    ) -> AssociateResolverRuleResponseTypeDef:
        """
        Associates a Resolver rule with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/associate_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#associate_resolver_rule)
        """

    def create_firewall_domain_list(
        self, **kwargs: Unpack[CreateFirewallDomainListRequestTypeDef]
    ) -> CreateFirewallDomainListResponseTypeDef:
        """
        Creates an empty firewall domain list for use in DNS Firewall rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_firewall_domain_list)
        """

    def create_firewall_rule(
        self, **kwargs: Unpack[CreateFirewallRuleRequestTypeDef]
    ) -> CreateFirewallRuleResponseTypeDef:
        """
        Creates a single DNS Firewall rule in the specified rule group, using the
        specified domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_firewall_rule)
        """

    def create_firewall_rule_group(
        self, **kwargs: Unpack[CreateFirewallRuleGroupRequestTypeDef]
    ) -> CreateFirewallRuleGroupResponseTypeDef:
        """
        Creates an empty DNS Firewall rule group for filtering DNS network traffic in a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_firewall_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_firewall_rule_group)
        """

    def create_outpost_resolver(
        self, **kwargs: Unpack[CreateOutpostResolverRequestTypeDef]
    ) -> CreateOutpostResolverResponseTypeDef:
        """
        Creates a Route 53 Resolver on an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_outpost_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_outpost_resolver)
        """

    def create_resolver_endpoint(
        self, **kwargs: Unpack[CreateResolverEndpointRequestTypeDef]
    ) -> CreateResolverEndpointResponseTypeDef:
        """
        Creates a Resolver endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_resolver_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_resolver_endpoint)
        """

    def create_resolver_query_log_config(
        self, **kwargs: Unpack[CreateResolverQueryLogConfigRequestTypeDef]
    ) -> CreateResolverQueryLogConfigResponseTypeDef:
        """
        Creates a Resolver query logging configuration, which defines where you want
        Resolver to save DNS query logs that originate in your VPCs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_resolver_query_log_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_resolver_query_log_config)
        """

    def create_resolver_rule(
        self, **kwargs: Unpack[CreateResolverRuleRequestTypeDef]
    ) -> CreateResolverRuleResponseTypeDef:
        """
        For DNS queries that originate in your VPCs, specifies which Resolver endpoint
        the queries pass through, one domain name that you want to forward to your
        network, and the IP addresses of the DNS resolvers in your network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/create_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#create_resolver_rule)
        """

    def delete_firewall_domain_list(
        self, **kwargs: Unpack[DeleteFirewallDomainListRequestTypeDef]
    ) -> DeleteFirewallDomainListResponseTypeDef:
        """
        Deletes the specified domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_firewall_domain_list)
        """

    def delete_firewall_rule(
        self, **kwargs: Unpack[DeleteFirewallRuleRequestTypeDef]
    ) -> DeleteFirewallRuleResponseTypeDef:
        """
        Deletes the specified firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_firewall_rule)
        """

    def delete_firewall_rule_group(
        self, **kwargs: Unpack[DeleteFirewallRuleGroupRequestTypeDef]
    ) -> DeleteFirewallRuleGroupResponseTypeDef:
        """
        Deletes the specified firewall rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_firewall_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_firewall_rule_group)
        """

    def delete_outpost_resolver(
        self, **kwargs: Unpack[DeleteOutpostResolverRequestTypeDef]
    ) -> DeleteOutpostResolverResponseTypeDef:
        """
        Deletes a Resolver on the Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_outpost_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_outpost_resolver)
        """

    def delete_resolver_endpoint(
        self, **kwargs: Unpack[DeleteResolverEndpointRequestTypeDef]
    ) -> DeleteResolverEndpointResponseTypeDef:
        """
        Deletes a Resolver endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_resolver_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_resolver_endpoint)
        """

    def delete_resolver_query_log_config(
        self, **kwargs: Unpack[DeleteResolverQueryLogConfigRequestTypeDef]
    ) -> DeleteResolverQueryLogConfigResponseTypeDef:
        """
        Deletes a query logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_resolver_query_log_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_resolver_query_log_config)
        """

    def delete_resolver_rule(
        self, **kwargs: Unpack[DeleteResolverRuleRequestTypeDef]
    ) -> DeleteResolverRuleResponseTypeDef:
        """
        Deletes a Resolver rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/delete_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#delete_resolver_rule)
        """

    def disassociate_firewall_rule_group(
        self, **kwargs: Unpack[DisassociateFirewallRuleGroupRequestTypeDef]
    ) -> DisassociateFirewallRuleGroupResponseTypeDef:
        """
        Disassociates a <a>FirewallRuleGroup</a> from a VPC, to remove DNS filtering
        from the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/disassociate_firewall_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#disassociate_firewall_rule_group)
        """

    def disassociate_resolver_endpoint_ip_address(
        self, **kwargs: Unpack[DisassociateResolverEndpointIpAddressRequestTypeDef]
    ) -> DisassociateResolverEndpointIpAddressResponseTypeDef:
        """
        Removes IP addresses from an inbound or an outbound Resolver endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/disassociate_resolver_endpoint_ip_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#disassociate_resolver_endpoint_ip_address)
        """

    def disassociate_resolver_query_log_config(
        self, **kwargs: Unpack[DisassociateResolverQueryLogConfigRequestTypeDef]
    ) -> DisassociateResolverQueryLogConfigResponseTypeDef:
        """
        Disassociates a VPC from a query logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/disassociate_resolver_query_log_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#disassociate_resolver_query_log_config)
        """

    def disassociate_resolver_rule(
        self, **kwargs: Unpack[DisassociateResolverRuleRequestTypeDef]
    ) -> DisassociateResolverRuleResponseTypeDef:
        """
        Removes the association between a specified Resolver rule and a specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/disassociate_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#disassociate_resolver_rule)
        """

    def get_firewall_config(
        self, **kwargs: Unpack[GetFirewallConfigRequestTypeDef]
    ) -> GetFirewallConfigResponseTypeDef:
        """
        Retrieves the configuration of the firewall behavior provided by DNS Firewall
        for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_firewall_config)
        """

    def get_firewall_domain_list(
        self, **kwargs: Unpack[GetFirewallDomainListRequestTypeDef]
    ) -> GetFirewallDomainListResponseTypeDef:
        """
        Retrieves the specified firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_firewall_domain_list)
        """

    def get_firewall_rule_group(
        self, **kwargs: Unpack[GetFirewallRuleGroupRequestTypeDef]
    ) -> GetFirewallRuleGroupResponseTypeDef:
        """
        Retrieves the specified firewall rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_firewall_rule_group)
        """

    def get_firewall_rule_group_association(
        self, **kwargs: Unpack[GetFirewallRuleGroupAssociationRequestTypeDef]
    ) -> GetFirewallRuleGroupAssociationResponseTypeDef:
        """
        Retrieves a firewall rule group association, which enables DNS filtering for a
        VPC with one rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_rule_group_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_firewall_rule_group_association)
        """

    def get_firewall_rule_group_policy(
        self, **kwargs: Unpack[GetFirewallRuleGroupPolicyRequestTypeDef]
    ) -> GetFirewallRuleGroupPolicyResponseTypeDef:
        """
        Returns the Identity and Access Management (Amazon Web Services IAM) policy for
        sharing the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_rule_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_firewall_rule_group_policy)
        """

    def get_outpost_resolver(
        self, **kwargs: Unpack[GetOutpostResolverRequestTypeDef]
    ) -> GetOutpostResolverResponseTypeDef:
        """
        Gets information about a specified Resolver on the Outpost, such as its
        instance count and type, name, and the current status of the Resolver.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_outpost_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_outpost_resolver)
        """

    def get_resolver_config(
        self, **kwargs: Unpack[GetResolverConfigRequestTypeDef]
    ) -> GetResolverConfigResponseTypeDef:
        """
        Retrieves the behavior configuration of Route 53 Resolver behavior for a single
        VPC from Amazon Virtual Private Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_config)
        """

    def get_resolver_dnssec_config(
        self, **kwargs: Unpack[GetResolverDnssecConfigRequestTypeDef]
    ) -> GetResolverDnssecConfigResponseTypeDef:
        """
        Gets DNSSEC validation information for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_dnssec_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_dnssec_config)
        """

    def get_resolver_endpoint(
        self, **kwargs: Unpack[GetResolverEndpointRequestTypeDef]
    ) -> GetResolverEndpointResponseTypeDef:
        """
        Gets information about a specified Resolver endpoint, such as whether it's an
        inbound or an outbound Resolver endpoint, and the current status of the
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_endpoint)
        """

    def get_resolver_query_log_config(
        self, **kwargs: Unpack[GetResolverQueryLogConfigRequestTypeDef]
    ) -> GetResolverQueryLogConfigResponseTypeDef:
        """
        Gets information about a specified Resolver query logging configuration, such
        as the number of VPCs that the configuration is logging queries for and the
        location that logs are sent to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_query_log_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_query_log_config)
        """

    def get_resolver_query_log_config_association(
        self, **kwargs: Unpack[GetResolverQueryLogConfigAssociationRequestTypeDef]
    ) -> GetResolverQueryLogConfigAssociationResponseTypeDef:
        """
        Gets information about a specified association between a Resolver query logging
        configuration and an Amazon VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_query_log_config_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_query_log_config_association)
        """

    def get_resolver_query_log_config_policy(
        self, **kwargs: Unpack[GetResolverQueryLogConfigPolicyRequestTypeDef]
    ) -> GetResolverQueryLogConfigPolicyResponseTypeDef:
        """
        Gets information about a query logging policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_query_log_config_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_query_log_config_policy)
        """

    def get_resolver_rule(
        self, **kwargs: Unpack[GetResolverRuleRequestTypeDef]
    ) -> GetResolverRuleResponseTypeDef:
        """
        Gets information about a specified Resolver rule, such as the domain name that
        the rule forwards DNS queries for and the ID of the outbound Resolver endpoint
        that the rule is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_rule)
        """

    def get_resolver_rule_association(
        self, **kwargs: Unpack[GetResolverRuleAssociationRequestTypeDef]
    ) -> GetResolverRuleAssociationResponseTypeDef:
        """
        Gets information about an association between a specified Resolver rule and a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_rule_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_rule_association)
        """

    def get_resolver_rule_policy(
        self, **kwargs: Unpack[GetResolverRulePolicyRequestTypeDef]
    ) -> GetResolverRulePolicyResponseTypeDef:
        """
        Gets information about the Resolver rule policy for a specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_resolver_rule_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_resolver_rule_policy)
        """

    def import_firewall_domains(
        self, **kwargs: Unpack[ImportFirewallDomainsRequestTypeDef]
    ) -> ImportFirewallDomainsResponseTypeDef:
        """
        Imports domain names from a file into a domain list, for use in a DNS firewall
        rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/import_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#import_firewall_domains)
        """

    def list_firewall_configs(
        self, **kwargs: Unpack[ListFirewallConfigsRequestTypeDef]
    ) -> ListFirewallConfigsResponseTypeDef:
        """
        Retrieves the firewall configurations that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_configs)
        """

    def list_firewall_domain_lists(
        self, **kwargs: Unpack[ListFirewallDomainListsRequestTypeDef]
    ) -> ListFirewallDomainListsResponseTypeDef:
        """
        Retrieves the firewall domain lists that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_domain_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_domain_lists)
        """

    def list_firewall_domains(
        self, **kwargs: Unpack[ListFirewallDomainsRequestTypeDef]
    ) -> ListFirewallDomainsResponseTypeDef:
        """
        Retrieves the domains that you have defined for the specified firewall domain
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_domains)
        """

    def list_firewall_rule_group_associations(
        self, **kwargs: Unpack[ListFirewallRuleGroupAssociationsRequestTypeDef]
    ) -> ListFirewallRuleGroupAssociationsResponseTypeDef:
        """
        Retrieves the firewall rule group associations that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_rule_group_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_rule_group_associations)
        """

    def list_firewall_rule_groups(
        self, **kwargs: Unpack[ListFirewallRuleGroupsRequestTypeDef]
    ) -> ListFirewallRuleGroupsResponseTypeDef:
        """
        Retrieves the minimal high-level information for the rule groups that you have
        defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_rule_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_rule_groups)
        """

    def list_firewall_rules(
        self, **kwargs: Unpack[ListFirewallRulesRequestTypeDef]
    ) -> ListFirewallRulesResponseTypeDef:
        """
        Retrieves the firewall rules that you have defined for the specified firewall
        rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_firewall_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_firewall_rules)
        """

    def list_outpost_resolvers(
        self, **kwargs: Unpack[ListOutpostResolversRequestTypeDef]
    ) -> ListOutpostResolversResponseTypeDef:
        """
        Lists all the Resolvers on Outposts that were created using the current Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_outpost_resolvers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_outpost_resolvers)
        """

    def list_resolver_configs(
        self, **kwargs: Unpack[ListResolverConfigsRequestTypeDef]
    ) -> ListResolverConfigsResponseTypeDef:
        """
        Retrieves the Resolver configurations that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_configs)
        """

    def list_resolver_dnssec_configs(
        self, **kwargs: Unpack[ListResolverDnssecConfigsRequestTypeDef]
    ) -> ListResolverDnssecConfigsResponseTypeDef:
        """
        Lists the configurations for DNSSEC validation that are associated with the
        current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_dnssec_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_dnssec_configs)
        """

    def list_resolver_endpoint_ip_addresses(
        self, **kwargs: Unpack[ListResolverEndpointIpAddressesRequestTypeDef]
    ) -> ListResolverEndpointIpAddressesResponseTypeDef:
        """
        Gets the IP addresses for a specified Resolver endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_endpoint_ip_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_endpoint_ip_addresses)
        """

    def list_resolver_endpoints(
        self, **kwargs: Unpack[ListResolverEndpointsRequestTypeDef]
    ) -> ListResolverEndpointsResponseTypeDef:
        """
        Lists all the Resolver endpoints that were created using the current Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_endpoints)
        """

    def list_resolver_query_log_config_associations(
        self, **kwargs: Unpack[ListResolverQueryLogConfigAssociationsRequestTypeDef]
    ) -> ListResolverQueryLogConfigAssociationsResponseTypeDef:
        """
        Lists information about associations between Amazon VPCs and query logging
        configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_query_log_config_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_query_log_config_associations)
        """

    def list_resolver_query_log_configs(
        self, **kwargs: Unpack[ListResolverQueryLogConfigsRequestTypeDef]
    ) -> ListResolverQueryLogConfigsResponseTypeDef:
        """
        Lists information about the specified query logging configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_query_log_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_query_log_configs)
        """

    def list_resolver_rule_associations(
        self, **kwargs: Unpack[ListResolverRuleAssociationsRequestTypeDef]
    ) -> ListResolverRuleAssociationsResponseTypeDef:
        """
        Lists the associations that were created between Resolver rules and VPCs using
        the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_rule_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_rule_associations)
        """

    def list_resolver_rules(
        self, **kwargs: Unpack[ListResolverRulesRequestTypeDef]
    ) -> ListResolverRulesResponseTypeDef:
        """
        Lists the Resolver rules that were created using the current Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_resolver_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_resolver_rules)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that you associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#list_tags_for_resource)
        """

    def put_firewall_rule_group_policy(
        self, **kwargs: Unpack[PutFirewallRuleGroupPolicyRequestTypeDef]
    ) -> PutFirewallRuleGroupPolicyResponseTypeDef:
        """
        Attaches an Identity and Access Management (Amazon Web Services IAM) policy for
        sharing the rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/put_firewall_rule_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#put_firewall_rule_group_policy)
        """

    def put_resolver_query_log_config_policy(
        self, **kwargs: Unpack[PutResolverQueryLogConfigPolicyRequestTypeDef]
    ) -> PutResolverQueryLogConfigPolicyResponseTypeDef:
        """
        Specifies an Amazon Web Services account that you want to share a query logging
        configuration with, the query logging configuration that you want to share, and
        the operations that you want the account to be able to perform on the
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/put_resolver_query_log_config_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#put_resolver_query_log_config_policy)
        """

    def put_resolver_rule_policy(
        self, **kwargs: Unpack[PutResolverRulePolicyRequestTypeDef]
    ) -> PutResolverRulePolicyResponseTypeDef:
        """
        Specifies an Amazon Web Services rule that you want to share with another
        account, the account that you want to share the rule with, and the operations
        that you want the account to be able to perform on the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/put_resolver_rule_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#put_resolver_rule_policy)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#untag_resource)
        """

    def update_firewall_config(
        self, **kwargs: Unpack[UpdateFirewallConfigRequestTypeDef]
    ) -> UpdateFirewallConfigResponseTypeDef:
        """
        Updates the configuration of the firewall behavior provided by DNS Firewall for
        a single VPC from Amazon Virtual Private Cloud (Amazon VPC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_firewall_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_firewall_config)
        """

    def update_firewall_domains(
        self, **kwargs: Unpack[UpdateFirewallDomainsRequestTypeDef]
    ) -> UpdateFirewallDomainsResponseTypeDef:
        """
        Updates the firewall domain list from an array of domain specifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_firewall_domains)
        """

    def update_firewall_rule(
        self, **kwargs: Unpack[UpdateFirewallRuleRequestTypeDef]
    ) -> UpdateFirewallRuleResponseTypeDef:
        """
        Updates the specified firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_firewall_rule)
        """

    def update_firewall_rule_group_association(
        self, **kwargs: Unpack[UpdateFirewallRuleGroupAssociationRequestTypeDef]
    ) -> UpdateFirewallRuleGroupAssociationResponseTypeDef:
        """
        Changes the association of a <a>FirewallRuleGroup</a> with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_firewall_rule_group_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_firewall_rule_group_association)
        """

    def update_outpost_resolver(
        self, **kwargs: Unpack[UpdateOutpostResolverRequestTypeDef]
    ) -> UpdateOutpostResolverResponseTypeDef:
        """
        You can use <code>UpdateOutpostResolver</code> to update the instance count,
        type, or name of a Resolver on an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_outpost_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_outpost_resolver)
        """

    def update_resolver_config(
        self, **kwargs: Unpack[UpdateResolverConfigRequestTypeDef]
    ) -> UpdateResolverConfigResponseTypeDef:
        """
        Updates the behavior configuration of Route 53 Resolver behavior for a single
        VPC from Amazon Virtual Private Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_resolver_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_resolver_config)
        """

    def update_resolver_dnssec_config(
        self, **kwargs: Unpack[UpdateResolverDnssecConfigRequestTypeDef]
    ) -> UpdateResolverDnssecConfigResponseTypeDef:
        """
        Updates an existing DNSSEC validation configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_resolver_dnssec_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_resolver_dnssec_config)
        """

    def update_resolver_endpoint(
        self, **kwargs: Unpack[UpdateResolverEndpointRequestTypeDef]
    ) -> UpdateResolverEndpointResponseTypeDef:
        """
        Updates the name, or endpoint type for an inbound or an outbound Resolver
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_resolver_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_resolver_endpoint)
        """

    def update_resolver_rule(
        self, **kwargs: Unpack[UpdateResolverRuleRequestTypeDef]
    ) -> UpdateResolverRuleResponseTypeDef:
        """
        Updates settings for a specified Resolver rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_resolver_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#update_resolver_rule)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_configs"]
    ) -> ListFirewallConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_domain_lists"]
    ) -> ListFirewallDomainListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_domains"]
    ) -> ListFirewallDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_rule_group_associations"]
    ) -> ListFirewallRuleGroupAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_rule_groups"]
    ) -> ListFirewallRuleGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_rules"]
    ) -> ListFirewallRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_outpost_resolvers"]
    ) -> ListOutpostResolversPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_configs"]
    ) -> ListResolverConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_dnssec_configs"]
    ) -> ListResolverDnssecConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_endpoint_ip_addresses"]
    ) -> ListResolverEndpointIpAddressesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_endpoints"]
    ) -> ListResolverEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_query_log_config_associations"]
    ) -> ListResolverQueryLogConfigAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_query_log_configs"]
    ) -> ListResolverQueryLogConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_rule_associations"]
    ) -> ListResolverRuleAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolver_rules"]
    ) -> ListResolverRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client/#get_paginator)
        """
