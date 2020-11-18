# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for route53resolver service client

Usage::

    ```python
    import boto3
    from mypy_boto3_route53resolver import Route53ResolverClient

    client: Route53ResolverClient = boto3.client("route53resolver")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_route53resolver.paginator import (
    ListResolverEndpointIpAddressesPaginator,
    ListResolverEndpointsPaginator,
    ListResolverQueryLogConfigAssociationsPaginator,
    ListResolverQueryLogConfigsPaginator,
    ListResolverRuleAssociationsPaginator,
    ListResolverRulesPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_route53resolver.type_defs import (
    AssociateResolverEndpointIpAddressResponseTypeDef,
    AssociateResolverQueryLogConfigResponseTypeDef,
    AssociateResolverRuleResponseTypeDef,
    CreateResolverEndpointResponseTypeDef,
    CreateResolverQueryLogConfigResponseTypeDef,
    CreateResolverRuleResponseTypeDef,
    DeleteResolverEndpointResponseTypeDef,
    DeleteResolverQueryLogConfigResponseTypeDef,
    DeleteResolverRuleResponseTypeDef,
    DisassociateResolverEndpointIpAddressResponseTypeDef,
    DisassociateResolverQueryLogConfigResponseTypeDef,
    DisassociateResolverRuleResponseTypeDef,
    FilterTypeDef,
    GetResolverEndpointResponseTypeDef,
    GetResolverQueryLogConfigAssociationResponseTypeDef,
    GetResolverQueryLogConfigPolicyResponseTypeDef,
    GetResolverQueryLogConfigResponseTypeDef,
    GetResolverRuleAssociationResponseTypeDef,
    GetResolverRulePolicyResponseTypeDef,
    GetResolverRuleResponseTypeDef,
    IpAddressRequestTypeDef,
    IpAddressUpdateTypeDef,
    ListResolverEndpointIpAddressesResponseTypeDef,
    ListResolverEndpointsResponseTypeDef,
    ListResolverQueryLogConfigAssociationsResponseTypeDef,
    ListResolverQueryLogConfigsResponseTypeDef,
    ListResolverRuleAssociationsResponseTypeDef,
    ListResolverRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResolverQueryLogConfigPolicyResponseTypeDef,
    PutResolverRulePolicyResponseTypeDef,
    ResolverRuleConfigTypeDef,
    TagTypeDef,
    TargetAddressTypeDef,
    UpdateResolverEndpointResponseTypeDef,
    UpdateResolverRuleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53ResolverClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
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
    ThrottlingException: Type[BotocoreClientError]
    UnknownResourceException: Type[BotocoreClientError]


class Route53ResolverClient:
    """
    [Route53Resolver.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_resolver_endpoint_ip_address(
        self, ResolverEndpointId: str, IpAddress: IpAddressUpdateTypeDef
    ) -> AssociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.associate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_endpoint_ip_address)
        """

    def associate_resolver_query_log_config(
        self, ResolverQueryLogConfigId: str, ResourceId: str
    ) -> AssociateResolverQueryLogConfigResponseTypeDef:
        """
        [Client.associate_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_query_log_config)
        """

    def associate_resolver_rule(
        self, ResolverRuleId: str, VPCId: str, Name: str = None
    ) -> AssociateResolverRuleResponseTypeDef:
        """
        [Client.associate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.can_paginate)
        """

    def create_resolver_endpoint(
        self,
        CreatorRequestId: str,
        SecurityGroupIds: List[str],
        Direction: Literal["INBOUND", "OUTBOUND"],
        IpAddresses: List[IpAddressRequestTypeDef],
        Name: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateResolverEndpointResponseTypeDef:
        """
        [Client.create_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_endpoint)
        """

    def create_resolver_query_log_config(
        self, Name: str, DestinationArn: str, CreatorRequestId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateResolverQueryLogConfigResponseTypeDef:
        """
        [Client.create_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_query_log_config)
        """

    def create_resolver_rule(
        self,
        CreatorRequestId: str,
        RuleType: Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        DomainName: str,
        Name: str = None,
        TargetIps: List["TargetAddressTypeDef"] = None,
        ResolverEndpointId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateResolverRuleResponseTypeDef:
        """
        [Client.create_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_rule)
        """

    def delete_resolver_endpoint(
        self, ResolverEndpointId: str
    ) -> DeleteResolverEndpointResponseTypeDef:
        """
        [Client.delete_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_endpoint)
        """

    def delete_resolver_query_log_config(
        self, ResolverQueryLogConfigId: str
    ) -> DeleteResolverQueryLogConfigResponseTypeDef:
        """
        [Client.delete_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_query_log_config)
        """

    def delete_resolver_rule(self, ResolverRuleId: str) -> DeleteResolverRuleResponseTypeDef:
        """
        [Client.delete_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_rule)
        """

    def disassociate_resolver_endpoint_ip_address(
        self, ResolverEndpointId: str, IpAddress: IpAddressUpdateTypeDef
    ) -> DisassociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.disassociate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_endpoint_ip_address)
        """

    def disassociate_resolver_query_log_config(
        self, ResolverQueryLogConfigId: str, ResourceId: str
    ) -> DisassociateResolverQueryLogConfigResponseTypeDef:
        """
        [Client.disassociate_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_query_log_config)
        """

    def disassociate_resolver_rule(
        self, VPCId: str, ResolverRuleId: str
    ) -> DisassociateResolverRuleResponseTypeDef:
        """
        [Client.disassociate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.generate_presigned_url)
        """

    def get_resolver_endpoint(self, ResolverEndpointId: str) -> GetResolverEndpointResponseTypeDef:
        """
        [Client.get_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint)
        """

    def get_resolver_query_log_config(
        self, ResolverQueryLogConfigId: str
    ) -> GetResolverQueryLogConfigResponseTypeDef:
        """
        [Client.get_resolver_query_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config)
        """

    def get_resolver_query_log_config_association(
        self, ResolverQueryLogConfigAssociationId: str
    ) -> GetResolverQueryLogConfigAssociationResponseTypeDef:
        """
        [Client.get_resolver_query_log_config_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_association)
        """

    def get_resolver_query_log_config_policy(
        self, Arn: str
    ) -> GetResolverQueryLogConfigPolicyResponseTypeDef:
        """
        [Client.get_resolver_query_log_config_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_policy)
        """

    def get_resolver_rule(self, ResolverRuleId: str) -> GetResolverRuleResponseTypeDef:
        """
        [Client.get_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule)
        """

    def get_resolver_rule_association(
        self, ResolverRuleAssociationId: str
    ) -> GetResolverRuleAssociationResponseTypeDef:
        """
        [Client.get_resolver_rule_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_association)
        """

    def get_resolver_rule_policy(self, Arn: str) -> GetResolverRulePolicyResponseTypeDef:
        """
        [Client.get_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_policy)
        """

    def list_resolver_endpoint_ip_addresses(
        self, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListResolverEndpointIpAddressesResponseTypeDef:
        """
        [Client.list_resolver_endpoint_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoint_ip_addresses)
        """

    def list_resolver_endpoints(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverEndpointsResponseTypeDef:
        """
        [Client.list_resolver_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoints)
        """

    def list_resolver_query_log_config_associations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListResolverQueryLogConfigAssociationsResponseTypeDef:
        """
        [Client.list_resolver_query_log_config_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_config_associations)
        """

    def list_resolver_query_log_configs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListResolverQueryLogConfigsResponseTypeDef:
        """
        [Client.list_resolver_query_log_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_configs)
        """

    def list_resolver_rule_associations(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverRuleAssociationsResponseTypeDef:
        """
        [Client.list_resolver_rule_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rule_associations)
        """

    def list_resolver_rules(
        self, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverRulesResponseTypeDef:
        """
        [Client.list_resolver_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rules)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.list_tags_for_resource)
        """

    def put_resolver_query_log_config_policy(
        self, Arn: str, ResolverQueryLogConfigPolicy: str
    ) -> PutResolverQueryLogConfigPolicyResponseTypeDef:
        """
        [Client.put_resolver_query_log_config_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_query_log_config_policy)
        """

    def put_resolver_rule_policy(
        self, Arn: str, ResolverRulePolicy: str
    ) -> PutResolverRulePolicyResponseTypeDef:
        """
        [Client.put_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_rule_policy)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.untag_resource)
        """

    def update_resolver_endpoint(
        self, ResolverEndpointId: str, Name: str = None
    ) -> UpdateResolverEndpointResponseTypeDef:
        """
        [Client.update_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_endpoint)
        """

    def update_resolver_rule(
        self, ResolverRuleId: str, Config: ResolverRuleConfigTypeDef
    ) -> UpdateResolverRuleResponseTypeDef:
        """
        [Client.update_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_rule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_endpoint_ip_addresses"]
    ) -> ListResolverEndpointIpAddressesPaginator:
        """
        [Paginator.ListResolverEndpointIpAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_endpoints"]
    ) -> ListResolverEndpointsPaginator:
        """
        [Paginator.ListResolverEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_query_log_config_associations"]
    ) -> ListResolverQueryLogConfigAssociationsPaginator:
        """
        [Paginator.ListResolverQueryLogConfigAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_query_log_configs"]
    ) -> ListResolverQueryLogConfigsPaginator:
        """
        [Paginator.ListResolverQueryLogConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_rule_associations"]
    ) -> ListResolverRuleAssociationsPaginator:
        """
        [Paginator.ListResolverRuleAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRuleAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_rules"]
    ) -> ListResolverRulesPaginator:
        """
        [Paginator.ListResolverRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource)
        """
