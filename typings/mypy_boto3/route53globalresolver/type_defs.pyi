"""
Type annotations for route53globalresolver service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53globalresolver/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_route53globalresolver.type_defs import AccessSourcesItemTypeDef

    data: AccessSourcesItemTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ConfidenceThresholdType,
    CRResourceStatusType,
    DnsAdvancedProtectionType,
    DnsProtocolType,
    DnsSecValidationTypeType,
    EdnsClientSubnetTypeType,
    FirewallBlockResponseType,
    FirewallRuleActionType,
    FirewallRulesFailOpenTypeType,
    HostedZoneAssociationStatusType,
    IpAddressTypeType,
    ProfileResourceStatusType,
    TokenStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessSourcesItemTypeDef",
    "AccessTokenItemTypeDef",
    "AssociateHostedZoneInputTypeDef",
    "AssociateHostedZoneOutputTypeDef",
    "BatchCreateFirewallRuleInputItemTypeDef",
    "BatchCreateFirewallRuleInputTypeDef",
    "BatchCreateFirewallRuleOutputItemTypeDef",
    "BatchCreateFirewallRuleOutputTypeDef",
    "BatchCreateFirewallRuleResultTypeDef",
    "BatchDeleteFirewallRuleInputItemTypeDef",
    "BatchDeleteFirewallRuleInputTypeDef",
    "BatchDeleteFirewallRuleOutputItemTypeDef",
    "BatchDeleteFirewallRuleOutputTypeDef",
    "BatchDeleteFirewallRuleResultTypeDef",
    "BatchUpdateFirewallRuleInputItemTypeDef",
    "BatchUpdateFirewallRuleInputTypeDef",
    "BatchUpdateFirewallRuleOutputItemTypeDef",
    "BatchUpdateFirewallRuleOutputTypeDef",
    "BatchUpdateFirewallRuleResultTypeDef",
    "CreateAccessSourceInputTypeDef",
    "CreateAccessSourceOutputTypeDef",
    "CreateAccessTokenInputTypeDef",
    "CreateAccessTokenOutputTypeDef",
    "CreateDNSViewInputTypeDef",
    "CreateDNSViewOutputTypeDef",
    "CreateFirewallDomainListInputTypeDef",
    "CreateFirewallDomainListOutputTypeDef",
    "CreateFirewallRuleInputTypeDef",
    "CreateFirewallRuleOutputTypeDef",
    "CreateGlobalResolverInputTypeDef",
    "CreateGlobalResolverOutputTypeDef",
    "DNSViewSummaryTypeDef",
    "DeleteAccessSourceInputTypeDef",
    "DeleteAccessSourceOutputTypeDef",
    "DeleteAccessTokenInputTypeDef",
    "DeleteAccessTokenOutputTypeDef",
    "DeleteDNSViewInputTypeDef",
    "DeleteDNSViewOutputTypeDef",
    "DeleteFirewallDomainListInputTypeDef",
    "DeleteFirewallDomainListOutputTypeDef",
    "DeleteFirewallRuleInputTypeDef",
    "DeleteFirewallRuleOutputTypeDef",
    "DeleteGlobalResolverInputTypeDef",
    "DeleteGlobalResolverOutputTypeDef",
    "DisableDNSViewInputTypeDef",
    "DisableDNSViewOutputTypeDef",
    "DisassociateHostedZoneInputTypeDef",
    "DisassociateHostedZoneOutputTypeDef",
    "EnableDNSViewInputTypeDef",
    "EnableDNSViewOutputTypeDef",
    "FirewallDomainListsItemTypeDef",
    "FirewallRulesItemTypeDef",
    "GetAccessSourceInputTypeDef",
    "GetAccessSourceOutputTypeDef",
    "GetAccessTokenInputTypeDef",
    "GetAccessTokenOutputTypeDef",
    "GetDNSViewInputTypeDef",
    "GetDNSViewOutputTypeDef",
    "GetFirewallDomainListInputTypeDef",
    "GetFirewallDomainListOutputTypeDef",
    "GetFirewallRuleInputTypeDef",
    "GetFirewallRuleOutputTypeDef",
    "GetGlobalResolverInputTypeDef",
    "GetGlobalResolverOutputTypeDef",
    "GetHostedZoneAssociationInputTypeDef",
    "GetHostedZoneAssociationOutputTypeDef",
    "GetManagedFirewallDomainListInputTypeDef",
    "GetManagedFirewallDomainListOutputTypeDef",
    "GlobalResolversItemTypeDef",
    "HostedZoneAssociationSummaryTypeDef",
    "ImportFirewallDomainsInputTypeDef",
    "ImportFirewallDomainsOutputTypeDef",
    "ListAccessSourcesInputPaginateTypeDef",
    "ListAccessSourcesInputTypeDef",
    "ListAccessSourcesOutputTypeDef",
    "ListAccessTokensInputPaginateTypeDef",
    "ListAccessTokensInputTypeDef",
    "ListAccessTokensOutputTypeDef",
    "ListDNSViewsInputPaginateTypeDef",
    "ListDNSViewsInputTypeDef",
    "ListDNSViewsOutputTypeDef",
    "ListFirewallDomainListsInputPaginateTypeDef",
    "ListFirewallDomainListsInputTypeDef",
    "ListFirewallDomainListsOutputTypeDef",
    "ListFirewallDomainsInputPaginateTypeDef",
    "ListFirewallDomainsInputTypeDef",
    "ListFirewallDomainsOutputTypeDef",
    "ListFirewallRulesInputPaginateTypeDef",
    "ListFirewallRulesInputTypeDef",
    "ListFirewallRulesOutputTypeDef",
    "ListGlobalResolversInputPaginateTypeDef",
    "ListGlobalResolversInputTypeDef",
    "ListGlobalResolversOutputTypeDef",
    "ListHostedZoneAssociationsInputPaginateTypeDef",
    "ListHostedZoneAssociationsInputTypeDef",
    "ListHostedZoneAssociationsOutputTypeDef",
    "ListManagedFirewallDomainListsInputPaginateTypeDef",
    "ListManagedFirewallDomainListsInputTypeDef",
    "ListManagedFirewallDomainListsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedFirewallDomainListsItemTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessSourceInputTypeDef",
    "UpdateAccessSourceOutputTypeDef",
    "UpdateAccessTokenInputTypeDef",
    "UpdateAccessTokenOutputTypeDef",
    "UpdateDNSViewInputTypeDef",
    "UpdateDNSViewOutputTypeDef",
    "UpdateFirewallDomainsInputTypeDef",
    "UpdateFirewallDomainsOutputTypeDef",
    "UpdateFirewallRuleInputTypeDef",
    "UpdateFirewallRuleOutputTypeDef",
    "UpdateGlobalResolverInputTypeDef",
    "UpdateGlobalResolverOutputTypeDef",
    "UpdateHostedZoneAssociationInputTypeDef",
    "UpdateHostedZoneAssociationOutputTypeDef",
)

AccessSourcesItemTypeDef = TypedDict(
    "AccessSourcesItemTypeDef",
    {
        "arn": str,
        "cidr": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "dnsViewId": str,
        "protocol": DnsProtocolType,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "name": NotRequired[str],
    },
)
AccessTokenItemTypeDef = TypedDict(
    "AccessTokenItemTypeDef",
    {
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "dnsViewId": str,
        "expiresAt": datetime,
        "globalResolverId": str,
        "status": TokenStatusType,
        "updatedAt": datetime,
        "name": NotRequired[str],
    },
)

class AssociateHostedZoneInputTypeDef(TypedDict):
    hostedZoneId: str
    resourceArn: str
    name: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchCreateFirewallRuleInputItemTypeDef(TypedDict):
    action: FirewallRuleActionType
    clientToken: str
    name: str
    dnsViewId: str
    blockOverrideDnsType: NotRequired[Literal["CNAME"]]
    blockOverrideDomain: NotRequired[str]
    blockOverrideTtl: NotRequired[int]
    blockResponse: NotRequired[FirewallBlockResponseType]
    confidenceThreshold: NotRequired[ConfidenceThresholdType]
    description: NotRequired[str]
    dnsAdvancedProtection: NotRequired[DnsAdvancedProtectionType]
    firewallDomainListId: NotRequired[str]
    priority: NotRequired[int]
    qType: NotRequired[str]

BatchCreateFirewallRuleResultTypeDef = TypedDict(
    "BatchCreateFirewallRuleResultTypeDef",
    {
        "action": FirewallRuleActionType,
        "clientToken": str,
        "name": str,
        "dnsViewId": str,
        "blockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "blockOverrideDomain": NotRequired[str],
        "blockOverrideTtl": NotRequired[int],
        "blockResponse": NotRequired[FirewallBlockResponseType],
        "confidenceThreshold": NotRequired[ConfidenceThresholdType],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "dnsAdvancedProtection": NotRequired[DnsAdvancedProtectionType],
        "firewallDomainListId": NotRequired[str],
        "id": NotRequired[str],
        "managedDomainListName": NotRequired[str],
        "priority": NotRequired[int],
        "queryType": NotRequired[str],
        "status": NotRequired[CRResourceStatusType],
        "updatedAt": NotRequired[datetime],
    },
)

class BatchDeleteFirewallRuleInputItemTypeDef(TypedDict):
    firewallRuleId: str

BatchDeleteFirewallRuleResultTypeDef = TypedDict(
    "BatchDeleteFirewallRuleResultTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CRResourceStatusType],
    },
)

class BatchUpdateFirewallRuleInputItemTypeDef(TypedDict):
    firewallRuleId: str
    action: NotRequired[FirewallRuleActionType]
    blockOverrideDnsType: NotRequired[Literal["CNAME"]]
    blockOverrideDomain: NotRequired[str]
    blockOverrideTtl: NotRequired[int]
    blockResponse: NotRequired[FirewallBlockResponseType]
    confidenceThreshold: NotRequired[ConfidenceThresholdType]
    description: NotRequired[str]
    dnsAdvancedProtection: NotRequired[DnsAdvancedProtectionType]
    name: NotRequired[str]
    priority: NotRequired[int]

BatchUpdateFirewallRuleResultTypeDef = TypedDict(
    "BatchUpdateFirewallRuleResultTypeDef",
    {
        "id": str,
        "action": NotRequired[FirewallRuleActionType],
        "blockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "blockOverrideDomain": NotRequired[str],
        "blockOverrideTtl": NotRequired[int],
        "blockResponse": NotRequired[FirewallBlockResponseType],
        "clientToken": NotRequired[str],
        "confidenceThreshold": NotRequired[ConfidenceThresholdType],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "dnsAdvancedProtection": NotRequired[DnsAdvancedProtectionType],
        "firewallDomainListId": NotRequired[str],
        "name": NotRequired[str],
        "priority": NotRequired[int],
        "dnsViewId": NotRequired[str],
        "queryType": NotRequired[str],
        "status": NotRequired[CRResourceStatusType],
        "updatedAt": NotRequired[datetime],
    },
)

class CreateAccessSourceInputTypeDef(TypedDict):
    cidr: str
    dnsViewId: str
    protocol: DnsProtocolType
    clientToken: NotRequired[str]
    ipAddressType: NotRequired[IpAddressTypeType]
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

TimestampTypeDef = Union[datetime, str]

class CreateDNSViewInputTypeDef(TypedDict):
    globalResolverId: str
    name: str
    clientToken: NotRequired[str]
    dnssecValidation: NotRequired[DnsSecValidationTypeType]
    ednsClientSubnet: NotRequired[EdnsClientSubnetTypeType]
    firewallRulesFailOpen: NotRequired[FirewallRulesFailOpenTypeType]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateFirewallDomainListInputTypeDef(TypedDict):
    globalResolverId: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateFirewallRuleInputTypeDef(TypedDict):
    action: FirewallRuleActionType
    name: str
    dnsViewId: str
    blockOverrideDnsType: NotRequired[Literal["CNAME"]]
    blockOverrideDomain: NotRequired[str]
    blockOverrideTtl: NotRequired[int]
    blockResponse: NotRequired[FirewallBlockResponseType]
    clientToken: NotRequired[str]
    confidenceThreshold: NotRequired[ConfidenceThresholdType]
    description: NotRequired[str]
    dnsAdvancedProtection: NotRequired[DnsAdvancedProtectionType]
    firewallDomainListId: NotRequired[str]
    priority: NotRequired[int]
    qType: NotRequired[str]

class CreateGlobalResolverInputTypeDef(TypedDict):
    name: str
    regions: Sequence[str]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    observabilityRegion: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

DNSViewSummaryTypeDef = TypedDict(
    "DNSViewSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "description": NotRequired[str],
    },
)

class DeleteAccessSourceInputTypeDef(TypedDict):
    accessSourceId: str

class DeleteAccessTokenInputTypeDef(TypedDict):
    accessTokenId: str

class DeleteDNSViewInputTypeDef(TypedDict):
    dnsViewId: str

class DeleteFirewallDomainListInputTypeDef(TypedDict):
    firewallDomainListId: str

class DeleteFirewallRuleInputTypeDef(TypedDict):
    firewallRuleId: str

class DeleteGlobalResolverInputTypeDef(TypedDict):
    globalResolverId: str

class DisableDNSViewInputTypeDef(TypedDict):
    dnsViewId: str

class DisassociateHostedZoneInputTypeDef(TypedDict):
    hostedZoneId: str
    resourceArn: str

class EnableDNSViewInputTypeDef(TypedDict):
    dnsViewId: str

FirewallDomainListsItemTypeDef = TypedDict(
    "FirewallDomainListsItemTypeDef",
    {
        "arn": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
FirewallRulesItemTypeDef = TypedDict(
    "FirewallRulesItemTypeDef",
    {
        "action": FirewallRuleActionType,
        "createdAt": datetime,
        "id": str,
        "name": str,
        "priority": int,
        "dnsViewId": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "blockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "blockOverrideDomain": NotRequired[str],
        "blockOverrideTtl": NotRequired[int],
        "blockResponse": NotRequired[FirewallBlockResponseType],
        "confidenceThreshold": NotRequired[ConfidenceThresholdType],
        "description": NotRequired[str],
        "dnsAdvancedProtection": NotRequired[DnsAdvancedProtectionType],
        "firewallDomainListId": NotRequired[str],
        "queryType": NotRequired[str],
    },
)

class GetAccessSourceInputTypeDef(TypedDict):
    accessSourceId: str

class GetAccessTokenInputTypeDef(TypedDict):
    accessTokenId: str

class GetDNSViewInputTypeDef(TypedDict):
    dnsViewId: str

class GetFirewallDomainListInputTypeDef(TypedDict):
    firewallDomainListId: str

class GetFirewallRuleInputTypeDef(TypedDict):
    firewallRuleId: str

class GetGlobalResolverInputTypeDef(TypedDict):
    globalResolverId: str

class GetHostedZoneAssociationInputTypeDef(TypedDict):
    hostedZoneAssociationId: str

class GetManagedFirewallDomainListInputTypeDef(TypedDict):
    managedFirewallDomainListId: str

GlobalResolversItemTypeDef = TypedDict(
    "GlobalResolversItemTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnsName": str,
        "name": str,
        "regions": List[str],
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": CRResourceStatusType,
        "ipv4Addresses": List[str],
        "observabilityRegion": NotRequired[str],
        "description": NotRequired[str],
    },
)
HostedZoneAssociationSummaryTypeDef = TypedDict(
    "HostedZoneAssociationSummaryTypeDef",
    {
        "id": str,
        "resourceArn": str,
        "hostedZoneId": str,
        "hostedZoneName": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": HostedZoneAssociationStatusType,
    },
)

class ImportFirewallDomainsInputTypeDef(TypedDict):
    domainFileUrl: str
    firewallDomainListId: str
    operation: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccessSourcesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Mapping[str, Sequence[str]]]

class ListAccessTokensInputTypeDef(TypedDict):
    dnsViewId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Mapping[str, Sequence[str]]]

class ListDNSViewsInputTypeDef(TypedDict):
    globalResolverId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFirewallDomainListsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    globalResolverId: NotRequired[str]

class ListFirewallDomainsInputTypeDef(TypedDict):
    firewallDomainListId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFirewallRulesInputTypeDef(TypedDict):
    dnsViewId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Mapping[str, Sequence[str]]]

class ListGlobalResolversInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListHostedZoneAssociationsInputTypeDef(TypedDict):
    resourceArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListManagedFirewallDomainListsInputTypeDef(TypedDict):
    managedFirewallDomainListType: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ManagedFirewallDomainListsItemTypeDef = TypedDict(
    "ManagedFirewallDomainListsItemTypeDef",
    {
        "id": str,
        "name": str,
        "managedListType": str,
        "description": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessSourceInputTypeDef(TypedDict):
    accessSourceId: str
    cidr: NotRequired[str]
    ipAddressType: NotRequired[IpAddressTypeType]
    name: NotRequired[str]
    protocol: NotRequired[DnsProtocolType]

class UpdateAccessTokenInputTypeDef(TypedDict):
    accessTokenId: str
    name: str

class UpdateDNSViewInputTypeDef(TypedDict):
    dnsViewId: str
    name: NotRequired[str]
    description: NotRequired[str]
    dnssecValidation: NotRequired[DnsSecValidationTypeType]
    ednsClientSubnet: NotRequired[EdnsClientSubnetTypeType]
    firewallRulesFailOpen: NotRequired[FirewallRulesFailOpenTypeType]

class UpdateFirewallDomainsInputTypeDef(TypedDict):
    domains: Sequence[str]
    firewallDomainListId: str
    operation: str

class UpdateFirewallRuleInputTypeDef(TypedDict):
    clientToken: str
    firewallRuleId: str
    action: NotRequired[FirewallRuleActionType]
    blockOverrideDnsType: NotRequired[Literal["CNAME"]]
    blockOverrideDomain: NotRequired[str]
    blockOverrideTtl: NotRequired[int]
    blockResponse: NotRequired[FirewallBlockResponseType]
    confidenceThreshold: NotRequired[ConfidenceThresholdType]
    description: NotRequired[str]
    dnsAdvancedProtection: NotRequired[DnsAdvancedProtectionType]
    name: NotRequired[str]
    priority: NotRequired[int]

class UpdateGlobalResolverInputTypeDef(TypedDict):
    globalResolverId: str
    name: NotRequired[str]
    observabilityRegion: NotRequired[str]
    description: NotRequired[str]

class UpdateHostedZoneAssociationInputTypeDef(TypedDict):
    hostedZoneAssociationId: str
    name: NotRequired[str]

AssociateHostedZoneOutputTypeDef = TypedDict(
    "AssociateHostedZoneOutputTypeDef",
    {
        "id": str,
        "resourceArn": str,
        "hostedZoneId": str,
        "hostedZoneName": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": HostedZoneAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessSourceOutputTypeDef = TypedDict(
    "CreateAccessSourceOutputTypeDef",
    {
        "arn": str,
        "cidr": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "name": str,
        "dnsViewId": str,
        "protocol": DnsProtocolType,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessTokenOutputTypeDef = TypedDict(
    "CreateAccessTokenOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "createdAt": datetime,
        "dnsViewId": str,
        "expiresAt": datetime,
        "name": str,
        "status": TokenStatusType,
        "value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDNSViewOutputTypeDef = TypedDict(
    "CreateDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFirewallDomainListOutputTypeDef = TypedDict(
    "CreateFirewallDomainListOutputTypeDef",
    {
        "arn": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "description": str,
        "domainCount": int,
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFirewallRuleOutputTypeDef = TypedDict(
    "CreateFirewallRuleOutputTypeDef",
    {
        "action": FirewallRuleActionType,
        "blockOverrideDnsType": Literal["CNAME"],
        "blockOverrideDomain": str,
        "blockOverrideTtl": int,
        "blockResponse": FirewallBlockResponseType,
        "confidenceThreshold": ConfidenceThresholdType,
        "createdAt": datetime,
        "description": str,
        "dnsAdvancedProtection": DnsAdvancedProtectionType,
        "firewallDomainListId": str,
        "id": str,
        "name": str,
        "priority": int,
        "dnsViewId": str,
        "queryType": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlobalResolverOutputTypeDef = TypedDict(
    "CreateGlobalResolverOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "createdAt": datetime,
        "description": str,
        "dnsName": str,
        "ipv4Addresses": List[str],
        "name": str,
        "observabilityRegion": str,
        "regions": List[str],
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccessSourceOutputTypeDef = TypedDict(
    "DeleteAccessSourceOutputTypeDef",
    {
        "arn": str,
        "cidr": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "name": str,
        "dnsViewId": str,
        "protocol": DnsProtocolType,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccessTokenOutputTypeDef = TypedDict(
    "DeleteAccessTokenOutputTypeDef",
    {
        "id": str,
        "status": TokenStatusType,
        "deletedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDNSViewOutputTypeDef = TypedDict(
    "DeleteDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallDomainListOutputTypeDef = TypedDict(
    "DeleteFirewallDomainListOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallRuleOutputTypeDef = TypedDict(
    "DeleteFirewallRuleOutputTypeDef",
    {
        "action": FirewallRuleActionType,
        "blockOverrideDnsType": Literal["CNAME"],
        "blockOverrideDomain": str,
        "blockOverrideTtl": int,
        "blockResponse": FirewallBlockResponseType,
        "confidenceThreshold": ConfidenceThresholdType,
        "createdAt": datetime,
        "description": str,
        "dnsAdvancedProtection": DnsAdvancedProtectionType,
        "firewallDomainListId": str,
        "id": str,
        "name": str,
        "priority": int,
        "dnsViewId": str,
        "queryType": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGlobalResolverOutputTypeDef = TypedDict(
    "DeleteGlobalResolverOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnsName": str,
        "observabilityRegion": str,
        "name": str,
        "description": str,
        "regions": List[str],
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": CRResourceStatusType,
        "ipv4Addresses": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableDNSViewOutputTypeDef = TypedDict(
    "DisableDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateHostedZoneOutputTypeDef = TypedDict(
    "DisassociateHostedZoneOutputTypeDef",
    {
        "id": str,
        "resourceArn": str,
        "hostedZoneId": str,
        "hostedZoneName": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": HostedZoneAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableDNSViewOutputTypeDef = TypedDict(
    "EnableDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessSourceOutputTypeDef = TypedDict(
    "GetAccessSourceOutputTypeDef",
    {
        "arn": str,
        "cidr": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "name": str,
        "dnsViewId": str,
        "protocol": DnsProtocolType,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessTokenOutputTypeDef = TypedDict(
    "GetAccessTokenOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "createdAt": datetime,
        "dnsViewId": str,
        "expiresAt": datetime,
        "globalResolverId": str,
        "name": str,
        "status": TokenStatusType,
        "updatedAt": datetime,
        "value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDNSViewOutputTypeDef = TypedDict(
    "GetDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallDomainListOutputTypeDef = TypedDict(
    "GetFirewallDomainListOutputTypeDef",
    {
        "arn": str,
        "globalResolverId": str,
        "clientToken": str,
        "createdAt": datetime,
        "description": str,
        "domainCount": int,
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "statusMessage": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallRuleOutputTypeDef = TypedDict(
    "GetFirewallRuleOutputTypeDef",
    {
        "action": FirewallRuleActionType,
        "blockOverrideDnsType": Literal["CNAME"],
        "blockOverrideDomain": str,
        "blockOverrideTtl": int,
        "blockResponse": FirewallBlockResponseType,
        "confidenceThreshold": ConfidenceThresholdType,
        "createdAt": datetime,
        "description": str,
        "dnsAdvancedProtection": DnsAdvancedProtectionType,
        "firewallDomainListId": str,
        "id": str,
        "name": str,
        "priority": int,
        "dnsViewId": str,
        "queryType": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlobalResolverOutputTypeDef = TypedDict(
    "GetGlobalResolverOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnsName": str,
        "observabilityRegion": str,
        "name": str,
        "description": str,
        "regions": List[str],
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": CRResourceStatusType,
        "ipv4Addresses": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostedZoneAssociationOutputTypeDef = TypedDict(
    "GetHostedZoneAssociationOutputTypeDef",
    {
        "id": str,
        "resourceArn": str,
        "hostedZoneId": str,
        "hostedZoneName": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": HostedZoneAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetManagedFirewallDomainListOutputTypeDef = TypedDict(
    "GetManagedFirewallDomainListOutputTypeDef",
    {
        "description": str,
        "id": str,
        "name": str,
        "managedListType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportFirewallDomainsOutputTypeDef = TypedDict(
    "ImportFirewallDomainsOutputTypeDef",
    {
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAccessSourcesOutputTypeDef(TypedDict):
    accessSources: List[AccessSourcesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAccessTokensOutputTypeDef(TypedDict):
    accessTokens: List[AccessTokenItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFirewallDomainsOutputTypeDef(TypedDict):
    domains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

UpdateAccessSourceOutputTypeDef = TypedDict(
    "UpdateAccessSourceOutputTypeDef",
    {
        "arn": str,
        "cidr": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "name": str,
        "dnsViewId": str,
        "protocol": DnsProtocolType,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessTokenOutputTypeDef = TypedDict(
    "UpdateAccessTokenOutputTypeDef",
    {
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDNSViewOutputTypeDef = TypedDict(
    "UpdateDNSViewOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnssecValidation": DnsSecValidationTypeType,
        "ednsClientSubnet": EdnsClientSubnetTypeType,
        "firewallRulesFailOpen": FirewallRulesFailOpenTypeType,
        "name": str,
        "description": str,
        "globalResolverId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ProfileResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFirewallDomainsOutputTypeDef = TypedDict(
    "UpdateFirewallDomainsOutputTypeDef",
    {
        "id": str,
        "name": str,
        "status": CRResourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFirewallRuleOutputTypeDef = TypedDict(
    "UpdateFirewallRuleOutputTypeDef",
    {
        "action": FirewallRuleActionType,
        "blockOverrideDnsType": Literal["CNAME"],
        "blockOverrideDomain": str,
        "blockOverrideTtl": int,
        "blockResponse": FirewallBlockResponseType,
        "confidenceThreshold": ConfidenceThresholdType,
        "createdAt": datetime,
        "description": str,
        "dnsAdvancedProtection": DnsAdvancedProtectionType,
        "firewallDomainListId": str,
        "id": str,
        "name": str,
        "priority": int,
        "dnsViewId": str,
        "queryType": str,
        "status": CRResourceStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlobalResolverOutputTypeDef = TypedDict(
    "UpdateGlobalResolverOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "clientToken": str,
        "dnsName": str,
        "observabilityRegion": str,
        "name": str,
        "description": str,
        "regions": List[str],
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": CRResourceStatusType,
        "ipv4Addresses": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHostedZoneAssociationOutputTypeDef = TypedDict(
    "UpdateHostedZoneAssociationOutputTypeDef",
    {
        "id": str,
        "resourceArn": str,
        "hostedZoneId": str,
        "hostedZoneName": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": HostedZoneAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class BatchCreateFirewallRuleInputTypeDef(TypedDict):
    firewallRules: Sequence[BatchCreateFirewallRuleInputItemTypeDef]

class BatchCreateFirewallRuleOutputItemTypeDef(TypedDict):
    firewallRule: BatchCreateFirewallRuleResultTypeDef
    code: int
    message: NotRequired[str]

class BatchDeleteFirewallRuleInputTypeDef(TypedDict):
    firewallRules: Sequence[BatchDeleteFirewallRuleInputItemTypeDef]

class BatchDeleteFirewallRuleOutputItemTypeDef(TypedDict):
    firewallRule: BatchDeleteFirewallRuleResultTypeDef
    code: int
    message: NotRequired[str]

class BatchUpdateFirewallRuleInputTypeDef(TypedDict):
    firewallRules: Sequence[BatchUpdateFirewallRuleInputItemTypeDef]

class BatchUpdateFirewallRuleOutputItemTypeDef(TypedDict):
    firewallRule: BatchUpdateFirewallRuleResultTypeDef
    code: int
    message: NotRequired[str]

class CreateAccessTokenInputTypeDef(TypedDict):
    dnsViewId: str
    clientToken: NotRequired[str]
    expiresAt: NotRequired[TimestampTypeDef]
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ListDNSViewsOutputTypeDef(TypedDict):
    dnsViews: List[DNSViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFirewallDomainListsOutputTypeDef(TypedDict):
    firewallDomainLists: List[FirewallDomainListsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFirewallRulesOutputTypeDef(TypedDict):
    firewallRules: List[FirewallRulesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListGlobalResolversOutputTypeDef(TypedDict):
    globalResolvers: List[GlobalResolversItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListHostedZoneAssociationsOutputTypeDef(TypedDict):
    hostedZoneAssociations: List[HostedZoneAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAccessSourcesInputPaginateTypeDef(TypedDict):
    filters: NotRequired[Mapping[str, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccessTokensInputPaginateTypeDef(TypedDict):
    dnsViewId: str
    filters: NotRequired[Mapping[str, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDNSViewsInputPaginateTypeDef(TypedDict):
    globalResolverId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFirewallDomainListsInputPaginateTypeDef(TypedDict):
    globalResolverId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFirewallDomainsInputPaginateTypeDef(TypedDict):
    firewallDomainListId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFirewallRulesInputPaginateTypeDef(TypedDict):
    dnsViewId: str
    filters: NotRequired[Mapping[str, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGlobalResolversInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHostedZoneAssociationsInputPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedFirewallDomainListsInputPaginateTypeDef(TypedDict):
    managedFirewallDomainListType: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedFirewallDomainListsOutputTypeDef(TypedDict):
    managedFirewallDomainLists: List[ManagedFirewallDomainListsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchCreateFirewallRuleOutputTypeDef(TypedDict):
    failures: List[BatchCreateFirewallRuleOutputItemTypeDef]
    successes: List[BatchCreateFirewallRuleOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteFirewallRuleOutputTypeDef(TypedDict):
    failures: List[BatchDeleteFirewallRuleOutputItemTypeDef]
    successes: List[BatchDeleteFirewallRuleOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateFirewallRuleOutputTypeDef(TypedDict):
    failures: List[BatchUpdateFirewallRuleOutputItemTypeDef]
    successes: List[BatchUpdateFirewallRuleOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
