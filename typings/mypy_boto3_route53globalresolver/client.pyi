"""
Type annotations for route53globalresolver service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53globalresolver.client import Route53GlobalResolverClient

    session = Session()
    client: Route53GlobalResolverClient = session.client("route53globalresolver")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccessSourcesPaginator,
    ListAccessTokensPaginator,
    ListDNSViewsPaginator,
    ListFirewallDomainListsPaginator,
    ListFirewallDomainsPaginator,
    ListFirewallRulesPaginator,
    ListGlobalResolversPaginator,
    ListHostedZoneAssociationsPaginator,
    ListManagedFirewallDomainListsPaginator,
)
from .type_defs import (
    AssociateHostedZoneInputTypeDef,
    AssociateHostedZoneOutputTypeDef,
    BatchCreateFirewallRuleInputTypeDef,
    BatchCreateFirewallRuleOutputTypeDef,
    BatchDeleteFirewallRuleInputTypeDef,
    BatchDeleteFirewallRuleOutputTypeDef,
    BatchUpdateFirewallRuleInputTypeDef,
    BatchUpdateFirewallRuleOutputTypeDef,
    CreateAccessSourceInputTypeDef,
    CreateAccessSourceOutputTypeDef,
    CreateAccessTokenInputTypeDef,
    CreateAccessTokenOutputTypeDef,
    CreateDNSViewInputTypeDef,
    CreateDNSViewOutputTypeDef,
    CreateFirewallDomainListInputTypeDef,
    CreateFirewallDomainListOutputTypeDef,
    CreateFirewallRuleInputTypeDef,
    CreateFirewallRuleOutputTypeDef,
    CreateGlobalResolverInputTypeDef,
    CreateGlobalResolverOutputTypeDef,
    DeleteAccessSourceInputTypeDef,
    DeleteAccessSourceOutputTypeDef,
    DeleteAccessTokenInputTypeDef,
    DeleteAccessTokenOutputTypeDef,
    DeleteDNSViewInputTypeDef,
    DeleteDNSViewOutputTypeDef,
    DeleteFirewallDomainListInputTypeDef,
    DeleteFirewallDomainListOutputTypeDef,
    DeleteFirewallRuleInputTypeDef,
    DeleteFirewallRuleOutputTypeDef,
    DeleteGlobalResolverInputTypeDef,
    DeleteGlobalResolverOutputTypeDef,
    DisableDNSViewInputTypeDef,
    DisableDNSViewOutputTypeDef,
    DisassociateHostedZoneInputTypeDef,
    DisassociateHostedZoneOutputTypeDef,
    EnableDNSViewInputTypeDef,
    EnableDNSViewOutputTypeDef,
    GetAccessSourceInputTypeDef,
    GetAccessSourceOutputTypeDef,
    GetAccessTokenInputTypeDef,
    GetAccessTokenOutputTypeDef,
    GetDNSViewInputTypeDef,
    GetDNSViewOutputTypeDef,
    GetFirewallDomainListInputTypeDef,
    GetFirewallDomainListOutputTypeDef,
    GetFirewallRuleInputTypeDef,
    GetFirewallRuleOutputTypeDef,
    GetGlobalResolverInputTypeDef,
    GetGlobalResolverOutputTypeDef,
    GetHostedZoneAssociationInputTypeDef,
    GetHostedZoneAssociationOutputTypeDef,
    GetManagedFirewallDomainListInputTypeDef,
    GetManagedFirewallDomainListOutputTypeDef,
    ImportFirewallDomainsInputTypeDef,
    ImportFirewallDomainsOutputTypeDef,
    ListAccessSourcesInputTypeDef,
    ListAccessSourcesOutputTypeDef,
    ListAccessTokensInputTypeDef,
    ListAccessTokensOutputTypeDef,
    ListDNSViewsInputTypeDef,
    ListDNSViewsOutputTypeDef,
    ListFirewallDomainListsInputTypeDef,
    ListFirewallDomainListsOutputTypeDef,
    ListFirewallDomainsInputTypeDef,
    ListFirewallDomainsOutputTypeDef,
    ListFirewallRulesInputTypeDef,
    ListFirewallRulesOutputTypeDef,
    ListGlobalResolversInputTypeDef,
    ListGlobalResolversOutputTypeDef,
    ListHostedZoneAssociationsInputTypeDef,
    ListHostedZoneAssociationsOutputTypeDef,
    ListManagedFirewallDomainListsInputTypeDef,
    ListManagedFirewallDomainListsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessSourceInputTypeDef,
    UpdateAccessSourceOutputTypeDef,
    UpdateAccessTokenInputTypeDef,
    UpdateAccessTokenOutputTypeDef,
    UpdateDNSViewInputTypeDef,
    UpdateDNSViewOutputTypeDef,
    UpdateFirewallDomainsInputTypeDef,
    UpdateFirewallDomainsOutputTypeDef,
    UpdateFirewallRuleInputTypeDef,
    UpdateFirewallRuleOutputTypeDef,
    UpdateGlobalResolverInputTypeDef,
    UpdateGlobalResolverOutputTypeDef,
    UpdateHostedZoneAssociationInputTypeDef,
    UpdateHostedZoneAssociationOutputTypeDef,
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

__all__ = ("Route53GlobalResolverClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53GlobalResolverClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver.html#Route53GlobalResolver.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53GlobalResolverClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver.html#Route53GlobalResolver.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#generate_presigned_url)
        """

    def associate_hosted_zone(
        self, **kwargs: Unpack[AssociateHostedZoneInputTypeDef]
    ) -> AssociateHostedZoneOutputTypeDef:
        """
        Associates a Route 53 private hosted zone with a Route 53 Global Resolver
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/associate_hosted_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#associate_hosted_zone)
        """

    def batch_create_firewall_rule(
        self, **kwargs: Unpack[BatchCreateFirewallRuleInputTypeDef]
    ) -> BatchCreateFirewallRuleOutputTypeDef:
        """
        Creates multiple DNS firewall rules in a single operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/batch_create_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#batch_create_firewall_rule)
        """

    def batch_delete_firewall_rule(
        self, **kwargs: Unpack[BatchDeleteFirewallRuleInputTypeDef]
    ) -> BatchDeleteFirewallRuleOutputTypeDef:
        """
        Deletes multiple DNS firewall rules in a single operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/batch_delete_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#batch_delete_firewall_rule)
        """

    def batch_update_firewall_rule(
        self, **kwargs: Unpack[BatchUpdateFirewallRuleInputTypeDef]
    ) -> BatchUpdateFirewallRuleOutputTypeDef:
        """
        Updates multiple DNS firewall rules in a single operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/batch_update_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#batch_update_firewall_rule)
        """

    def create_access_source(
        self, **kwargs: Unpack[CreateAccessSourceInputTypeDef]
    ) -> CreateAccessSourceOutputTypeDef:
        """
        Creates an access source for a DNS view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_access_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_access_source)
        """

    def create_access_token(
        self, **kwargs: Unpack[CreateAccessTokenInputTypeDef]
    ) -> CreateAccessTokenOutputTypeDef:
        """
        Creates an access token for a DNS view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_access_token)
        """

    def create_dns_view(
        self, **kwargs: Unpack[CreateDNSViewInputTypeDef]
    ) -> CreateDNSViewOutputTypeDef:
        """
        Creates a DNS view within a Route 53 Global Resolver.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_dns_view)
        """

    def create_firewall_domain_list(
        self, **kwargs: Unpack[CreateFirewallDomainListInputTypeDef]
    ) -> CreateFirewallDomainListOutputTypeDef:
        """
        Creates a firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_firewall_domain_list)
        """

    def create_firewall_rule(
        self, **kwargs: Unpack[CreateFirewallRuleInputTypeDef]
    ) -> CreateFirewallRuleOutputTypeDef:
        """
        Creates a DNS firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_firewall_rule)
        """

    def create_global_resolver(
        self, **kwargs: Unpack[CreateGlobalResolverInputTypeDef]
    ) -> CreateGlobalResolverOutputTypeDef:
        """
        Creates a new Route 53 Global Resolver instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/create_global_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#create_global_resolver)
        """

    def delete_access_source(
        self, **kwargs: Unpack[DeleteAccessSourceInputTypeDef]
    ) -> DeleteAccessSourceOutputTypeDef:
        """
        Deletes an access source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_access_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_access_source)
        """

    def delete_access_token(
        self, **kwargs: Unpack[DeleteAccessTokenInputTypeDef]
    ) -> DeleteAccessTokenOutputTypeDef:
        """
        Deletes an access token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_access_token)
        """

    def delete_dns_view(
        self, **kwargs: Unpack[DeleteDNSViewInputTypeDef]
    ) -> DeleteDNSViewOutputTypeDef:
        """
        Deletes a DNS view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_dns_view)
        """

    def delete_firewall_domain_list(
        self, **kwargs: Unpack[DeleteFirewallDomainListInputTypeDef]
    ) -> DeleteFirewallDomainListOutputTypeDef:
        """
        Deletes a firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_firewall_domain_list)
        """

    def delete_firewall_rule(
        self, **kwargs: Unpack[DeleteFirewallRuleInputTypeDef]
    ) -> DeleteFirewallRuleOutputTypeDef:
        """
        Deletes a DNS firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_firewall_rule)
        """

    def delete_global_resolver(
        self, **kwargs: Unpack[DeleteGlobalResolverInputTypeDef]
    ) -> DeleteGlobalResolverOutputTypeDef:
        """
        Deletes a Route 53 Global Resolver instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/delete_global_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#delete_global_resolver)
        """

    def disable_dns_view(
        self, **kwargs: Unpack[DisableDNSViewInputTypeDef]
    ) -> DisableDNSViewOutputTypeDef:
        """
        Disables a DNS view, preventing it from serving DNS queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/disable_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#disable_dns_view)
        """

    def disassociate_hosted_zone(
        self, **kwargs: Unpack[DisassociateHostedZoneInputTypeDef]
    ) -> DisassociateHostedZoneOutputTypeDef:
        """
        Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/disassociate_hosted_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#disassociate_hosted_zone)
        """

    def enable_dns_view(
        self, **kwargs: Unpack[EnableDNSViewInputTypeDef]
    ) -> EnableDNSViewOutputTypeDef:
        """
        Enables a disabled DNS view, allowing it to serve DNS queries again.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/enable_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#enable_dns_view)
        """

    def get_access_source(
        self, **kwargs: Unpack[GetAccessSourceInputTypeDef]
    ) -> GetAccessSourceOutputTypeDef:
        """
        Retrieves information about an access source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_access_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_access_source)
        """

    def get_access_token(
        self, **kwargs: Unpack[GetAccessTokenInputTypeDef]
    ) -> GetAccessTokenOutputTypeDef:
        """
        Retrieves information about an access token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_access_token)
        """

    def get_dns_view(self, **kwargs: Unpack[GetDNSViewInputTypeDef]) -> GetDNSViewOutputTypeDef:
        """
        Retrieves information about a DNS view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_dns_view)
        """

    def get_firewall_domain_list(
        self, **kwargs: Unpack[GetFirewallDomainListInputTypeDef]
    ) -> GetFirewallDomainListOutputTypeDef:
        """
        Retrieves information about a firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_firewall_domain_list)
        """

    def get_firewall_rule(
        self, **kwargs: Unpack[GetFirewallRuleInputTypeDef]
    ) -> GetFirewallRuleOutputTypeDef:
        """
        Retrieves information about a DNS firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_firewall_rule)
        """

    def get_global_resolver(
        self, **kwargs: Unpack[GetGlobalResolverInputTypeDef]
    ) -> GetGlobalResolverOutputTypeDef:
        """
        Retrieves information about a Route 53 Global Resolver instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_global_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_global_resolver)
        """

    def get_hosted_zone_association(
        self, **kwargs: Unpack[GetHostedZoneAssociationInputTypeDef]
    ) -> GetHostedZoneAssociationOutputTypeDef:
        """
        Retrieves information about a hosted zone association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_hosted_zone_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_hosted_zone_association)
        """

    def get_managed_firewall_domain_list(
        self, **kwargs: Unpack[GetManagedFirewallDomainListInputTypeDef]
    ) -> GetManagedFirewallDomainListOutputTypeDef:
        """
        Retrieves information about an AWS-managed firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_managed_firewall_domain_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_managed_firewall_domain_list)
        """

    def import_firewall_domains(
        self, **kwargs: Unpack[ImportFirewallDomainsInputTypeDef]
    ) -> ImportFirewallDomainsOutputTypeDef:
        """
        Imports a list of domains from an Amazon S3 file into a firewall domain list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/import_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#import_firewall_domains)
        """

    def list_access_sources(
        self, **kwargs: Unpack[ListAccessSourcesInputTypeDef]
    ) -> ListAccessSourcesOutputTypeDef:
        """
        Lists all access sources with pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_access_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_access_sources)
        """

    def list_access_tokens(
        self, **kwargs: Unpack[ListAccessTokensInputTypeDef]
    ) -> ListAccessTokensOutputTypeDef:
        """
        Lists all access tokens for a DNS view with pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_access_tokens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_access_tokens)
        """

    def list_dns_views(
        self, **kwargs: Unpack[ListDNSViewsInputTypeDef]
    ) -> ListDNSViewsOutputTypeDef:
        """
        Lists all DNS views for a Route 53 Global Resolver with pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_dns_views.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_dns_views)
        """

    def list_firewall_domain_lists(
        self, **kwargs: Unpack[ListFirewallDomainListsInputTypeDef]
    ) -> ListFirewallDomainListsOutputTypeDef:
        """
        Lists all firewall domain lists for a Route 53 Global Resolver with pagination
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_firewall_domain_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_firewall_domain_lists)
        """

    def list_firewall_domains(
        self, **kwargs: Unpack[ListFirewallDomainsInputTypeDef]
    ) -> ListFirewallDomainsOutputTypeDef:
        """
        Lists all the domains in DNS Firewall domain list you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_firewall_domains)
        """

    def list_firewall_rules(
        self, **kwargs: Unpack[ListFirewallRulesInputTypeDef]
    ) -> ListFirewallRulesOutputTypeDef:
        """
        Lists all DNS firewall rules for a DNS view with pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_firewall_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_firewall_rules)
        """

    def list_global_resolvers(
        self, **kwargs: Unpack[ListGlobalResolversInputTypeDef]
    ) -> ListGlobalResolversOutputTypeDef:
        """
        Lists all Route 53 Global Resolver instances in your account with pagination
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_global_resolvers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_global_resolvers)
        """

    def list_hosted_zone_associations(
        self, **kwargs: Unpack[ListHostedZoneAssociationsInputTypeDef]
    ) -> ListHostedZoneAssociationsOutputTypeDef:
        """
        Lists all hosted zone associations for a Route 53 Global Resolver resource with
        pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_hosted_zone_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_hosted_zone_associations)
        """

    def list_managed_firewall_domain_lists(
        self, **kwargs: Unpack[ListManagedFirewallDomainListsInputTypeDef]
    ) -> ListManagedFirewallDomainListsOutputTypeDef:
        """
        Returns a paginated list of the AWS Managed DNS Lists and the categories for
        DNS Firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_managed_firewall_domain_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_managed_firewall_domain_lists)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags associated with a Route 53 Global Resolver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a Route 53 Global Resolver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a Route 53 Global Resolver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#untag_resource)
        """

    def update_access_source(
        self, **kwargs: Unpack[UpdateAccessSourceInputTypeDef]
    ) -> UpdateAccessSourceOutputTypeDef:
        """
        Updates the configuration of an access source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_access_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_access_source)
        """

    def update_access_token(
        self, **kwargs: Unpack[UpdateAccessTokenInputTypeDef]
    ) -> UpdateAccessTokenOutputTypeDef:
        """
        Updates the configuration of an access token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_access_token)
        """

    def update_dns_view(
        self, **kwargs: Unpack[UpdateDNSViewInputTypeDef]
    ) -> UpdateDNSViewOutputTypeDef:
        """
        Updates the configuration of a DNS view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_dns_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_dns_view)
        """

    def update_firewall_domains(
        self, **kwargs: Unpack[UpdateFirewallDomainsInputTypeDef]
    ) -> UpdateFirewallDomainsOutputTypeDef:
        """
        Updates a DNS Firewall domain list from an array of specified domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_firewall_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_firewall_domains)
        """

    def update_firewall_rule(
        self, **kwargs: Unpack[UpdateFirewallRuleInputTypeDef]
    ) -> UpdateFirewallRuleOutputTypeDef:
        """
        Updates the configuration of a DNS firewall rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_firewall_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_firewall_rule)
        """

    def update_global_resolver(
        self, **kwargs: Unpack[UpdateGlobalResolverInputTypeDef]
    ) -> UpdateGlobalResolverOutputTypeDef:
        """
        Updates the configuration of a Route 53 Global Resolver instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_global_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_global_resolver)
        """

    def update_hosted_zone_association(
        self, **kwargs: Unpack[UpdateHostedZoneAssociationInputTypeDef]
    ) -> UpdateHostedZoneAssociationOutputTypeDef:
        """
        Updates the configuration of a hosted zone association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/update_hosted_zone_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#update_hosted_zone_association)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_sources"]
    ) -> ListAccessSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_tokens"]
    ) -> ListAccessTokensPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dns_views"]
    ) -> ListDNSViewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_domain_lists"]
    ) -> ListFirewallDomainListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_domains"]
    ) -> ListFirewallDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_firewall_rules"]
    ) -> ListFirewallRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_global_resolvers"]
    ) -> ListGlobalResolversPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hosted_zone_associations"]
    ) -> ListHostedZoneAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_firewall_domain_lists"]
    ) -> ListManagedFirewallDomainListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53globalresolver/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/client/#get_paginator)
        """
