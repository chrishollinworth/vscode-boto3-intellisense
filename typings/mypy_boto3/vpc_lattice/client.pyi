"""
Type annotations for vpc-lattice service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_vpc_lattice.client import VPCLatticeClient

    session = Session()
    client: VPCLatticeClient = session.client("vpc-lattice")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccessLogSubscriptionsPaginator,
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
from .type_defs import (
    BatchUpdateRuleRequestTypeDef,
    BatchUpdateRuleResponseTypeDef,
    CreateAccessLogSubscriptionRequestTypeDef,
    CreateAccessLogSubscriptionResponseTypeDef,
    CreateListenerRequestTypeDef,
    CreateListenerResponseTypeDef,
    CreateResourceConfigurationRequestTypeDef,
    CreateResourceConfigurationResponseTypeDef,
    CreateResourceGatewayRequestTypeDef,
    CreateResourceGatewayResponseTypeDef,
    CreateRuleRequestTypeDef,
    CreateRuleResponseTypeDef,
    CreateServiceNetworkRequestTypeDef,
    CreateServiceNetworkResourceAssociationRequestTypeDef,
    CreateServiceNetworkResourceAssociationResponseTypeDef,
    CreateServiceNetworkResponseTypeDef,
    CreateServiceNetworkServiceAssociationRequestTypeDef,
    CreateServiceNetworkServiceAssociationResponseTypeDef,
    CreateServiceNetworkVpcAssociationRequestTypeDef,
    CreateServiceNetworkVpcAssociationResponseTypeDef,
    CreateServiceRequestTypeDef,
    CreateServiceResponseTypeDef,
    CreateTargetGroupRequestTypeDef,
    CreateTargetGroupResponseTypeDef,
    DeleteAccessLogSubscriptionRequestTypeDef,
    DeleteAuthPolicyRequestTypeDef,
    DeleteListenerRequestTypeDef,
    DeleteResourceConfigurationRequestTypeDef,
    DeleteResourceEndpointAssociationRequestTypeDef,
    DeleteResourceEndpointAssociationResponseTypeDef,
    DeleteResourceGatewayRequestTypeDef,
    DeleteResourceGatewayResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteRuleRequestTypeDef,
    DeleteServiceNetworkRequestTypeDef,
    DeleteServiceNetworkResourceAssociationRequestTypeDef,
    DeleteServiceNetworkResourceAssociationResponseTypeDef,
    DeleteServiceNetworkServiceAssociationRequestTypeDef,
    DeleteServiceNetworkServiceAssociationResponseTypeDef,
    DeleteServiceNetworkVpcAssociationRequestTypeDef,
    DeleteServiceNetworkVpcAssociationResponseTypeDef,
    DeleteServiceRequestTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTargetGroupRequestTypeDef,
    DeleteTargetGroupResponseTypeDef,
    DeregisterTargetsRequestTypeDef,
    DeregisterTargetsResponseTypeDef,
    GetAccessLogSubscriptionRequestTypeDef,
    GetAccessLogSubscriptionResponseTypeDef,
    GetAuthPolicyRequestTypeDef,
    GetAuthPolicyResponseTypeDef,
    GetListenerRequestTypeDef,
    GetListenerResponseTypeDef,
    GetResourceConfigurationRequestTypeDef,
    GetResourceConfigurationResponseTypeDef,
    GetResourceGatewayRequestTypeDef,
    GetResourceGatewayResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRuleRequestTypeDef,
    GetRuleResponseTypeDef,
    GetServiceNetworkRequestTypeDef,
    GetServiceNetworkResourceAssociationRequestTypeDef,
    GetServiceNetworkResourceAssociationResponseTypeDef,
    GetServiceNetworkResponseTypeDef,
    GetServiceNetworkServiceAssociationRequestTypeDef,
    GetServiceNetworkServiceAssociationResponseTypeDef,
    GetServiceNetworkVpcAssociationRequestTypeDef,
    GetServiceNetworkVpcAssociationResponseTypeDef,
    GetServiceRequestTypeDef,
    GetServiceResponseTypeDef,
    GetTargetGroupRequestTypeDef,
    GetTargetGroupResponseTypeDef,
    ListAccessLogSubscriptionsRequestTypeDef,
    ListAccessLogSubscriptionsResponseTypeDef,
    ListListenersRequestTypeDef,
    ListListenersResponseTypeDef,
    ListResourceConfigurationsRequestTypeDef,
    ListResourceConfigurationsResponseTypeDef,
    ListResourceEndpointAssociationsRequestTypeDef,
    ListResourceEndpointAssociationsResponseTypeDef,
    ListResourceGatewaysRequestTypeDef,
    ListResourceGatewaysResponseTypeDef,
    ListRulesRequestTypeDef,
    ListRulesResponseTypeDef,
    ListServiceNetworkResourceAssociationsRequestTypeDef,
    ListServiceNetworkResourceAssociationsResponseTypeDef,
    ListServiceNetworkServiceAssociationsRequestTypeDef,
    ListServiceNetworkServiceAssociationsResponseTypeDef,
    ListServiceNetworksRequestTypeDef,
    ListServiceNetworksResponseTypeDef,
    ListServiceNetworkVpcAssociationsRequestTypeDef,
    ListServiceNetworkVpcAssociationsResponseTypeDef,
    ListServiceNetworkVpcEndpointAssociationsRequestTypeDef,
    ListServiceNetworkVpcEndpointAssociationsResponseTypeDef,
    ListServicesRequestTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetGroupsRequestTypeDef,
    ListTargetGroupsResponseTypeDef,
    ListTargetsRequestTypeDef,
    ListTargetsResponseTypeDef,
    PutAuthPolicyRequestTypeDef,
    PutAuthPolicyResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    RegisterTargetsRequestTypeDef,
    RegisterTargetsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessLogSubscriptionRequestTypeDef,
    UpdateAccessLogSubscriptionResponseTypeDef,
    UpdateListenerRequestTypeDef,
    UpdateListenerResponseTypeDef,
    UpdateResourceConfigurationRequestTypeDef,
    UpdateResourceConfigurationResponseTypeDef,
    UpdateResourceGatewayRequestTypeDef,
    UpdateResourceGatewayResponseTypeDef,
    UpdateRuleRequestTypeDef,
    UpdateRuleResponseTypeDef,
    UpdateServiceNetworkRequestTypeDef,
    UpdateServiceNetworkResponseTypeDef,
    UpdateServiceNetworkVpcAssociationRequestTypeDef,
    UpdateServiceNetworkVpcAssociationResponseTypeDef,
    UpdateServiceRequestTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTargetGroupRequestTypeDef,
    UpdateTargetGroupResponseTypeDef,
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

__all__ = ("VPCLatticeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class VPCLatticeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VPCLatticeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#generate_presigned_url)
        """

    def batch_update_rule(
        self, **kwargs: Unpack[BatchUpdateRuleRequestTypeDef]
    ) -> BatchUpdateRuleResponseTypeDef:
        """
        Updates the listener rules in a batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/batch_update_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#batch_update_rule)
        """

    def create_access_log_subscription(
        self, **kwargs: Unpack[CreateAccessLogSubscriptionRequestTypeDef]
    ) -> CreateAccessLogSubscriptionResponseTypeDef:
        """
        Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon
        Kinesis Data Firehose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_access_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_access_log_subscription)
        """

    def create_listener(
        self, **kwargs: Unpack[CreateListenerRequestTypeDef]
    ) -> CreateListenerResponseTypeDef:
        """
        Creates a listener for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_listener)
        """

    def create_resource_configuration(
        self, **kwargs: Unpack[CreateResourceConfigurationRequestTypeDef]
    ) -> CreateResourceConfigurationResponseTypeDef:
        """
        Creates a resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_resource_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_resource_configuration)
        """

    def create_resource_gateway(
        self, **kwargs: Unpack[CreateResourceGatewayRequestTypeDef]
    ) -> CreateResourceGatewayResponseTypeDef:
        """
        Creates a resource gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_resource_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_resource_gateway)
        """

    def create_rule(self, **kwargs: Unpack[CreateRuleRequestTypeDef]) -> CreateRuleResponseTypeDef:
        """
        Creates a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_rule)
        """

    def create_service(
        self, **kwargs: Unpack[CreateServiceRequestTypeDef]
    ) -> CreateServiceResponseTypeDef:
        """
        Creates a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_service)
        """

    def create_service_network(
        self, **kwargs: Unpack[CreateServiceNetworkRequestTypeDef]
    ) -> CreateServiceNetworkResponseTypeDef:
        """
        Creates a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_service_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_service_network)
        """

    def create_service_network_resource_association(
        self, **kwargs: Unpack[CreateServiceNetworkResourceAssociationRequestTypeDef]
    ) -> CreateServiceNetworkResourceAssociationResponseTypeDef:
        """
        Associates the specified service network with the specified resource
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_service_network_resource_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_service_network_resource_association)
        """

    def create_service_network_service_association(
        self, **kwargs: Unpack[CreateServiceNetworkServiceAssociationRequestTypeDef]
    ) -> CreateServiceNetworkServiceAssociationResponseTypeDef:
        """
        Associates the specified service with the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_service_network_service_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_service_network_service_association)
        """

    def create_service_network_vpc_association(
        self, **kwargs: Unpack[CreateServiceNetworkVpcAssociationRequestTypeDef]
    ) -> CreateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Associates a VPC with a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_service_network_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_service_network_vpc_association)
        """

    def create_target_group(
        self, **kwargs: Unpack[CreateTargetGroupRequestTypeDef]
    ) -> CreateTargetGroupResponseTypeDef:
        """
        Creates a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/create_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#create_target_group)
        """

    def delete_access_log_subscription(
        self, **kwargs: Unpack[DeleteAccessLogSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_access_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_access_log_subscription)
        """

    def delete_auth_policy(
        self, **kwargs: Unpack[DeleteAuthPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_auth_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_auth_policy)
        """

    def delete_listener(self, **kwargs: Unpack[DeleteListenerRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_listener)
        """

    def delete_resource_configuration(
        self, **kwargs: Unpack[DeleteResourceConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_resource_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_resource_configuration)
        """

    def delete_resource_endpoint_association(
        self, **kwargs: Unpack[DeleteResourceEndpointAssociationRequestTypeDef]
    ) -> DeleteResourceEndpointAssociationResponseTypeDef:
        """
        Disassociates the resource configuration from the resource VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_resource_endpoint_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_resource_endpoint_association)
        """

    def delete_resource_gateway(
        self, **kwargs: Unpack[DeleteResourceGatewayRequestTypeDef]
    ) -> DeleteResourceGatewayResponseTypeDef:
        """
        Deletes the specified resource gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_resource_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_resource_gateway)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_resource_policy)
        """

    def delete_rule(self, **kwargs: Unpack[DeleteRuleRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_rule)
        """

    def delete_service(
        self, **kwargs: Unpack[DeleteServiceRequestTypeDef]
    ) -> DeleteServiceResponseTypeDef:
        """
        Deletes a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_service)
        """

    def delete_service_network(
        self, **kwargs: Unpack[DeleteServiceNetworkRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_service_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_service_network)
        """

    def delete_service_network_resource_association(
        self, **kwargs: Unpack[DeleteServiceNetworkResourceAssociationRequestTypeDef]
    ) -> DeleteServiceNetworkResourceAssociationResponseTypeDef:
        """
        Deletes the association between a service network and a resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_service_network_resource_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_service_network_resource_association)
        """

    def delete_service_network_service_association(
        self, **kwargs: Unpack[DeleteServiceNetworkServiceAssociationRequestTypeDef]
    ) -> DeleteServiceNetworkServiceAssociationResponseTypeDef:
        """
        Deletes the association between a service and a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_service_network_service_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_service_network_service_association)
        """

    def delete_service_network_vpc_association(
        self, **kwargs: Unpack[DeleteServiceNetworkVpcAssociationRequestTypeDef]
    ) -> DeleteServiceNetworkVpcAssociationResponseTypeDef:
        """
        Disassociates the VPC from the service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_service_network_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_service_network_vpc_association)
        """

    def delete_target_group(
        self, **kwargs: Unpack[DeleteTargetGroupRequestTypeDef]
    ) -> DeleteTargetGroupResponseTypeDef:
        """
        Deletes a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/delete_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#delete_target_group)
        """

    def deregister_targets(
        self, **kwargs: Unpack[DeregisterTargetsRequestTypeDef]
    ) -> DeregisterTargetsResponseTypeDef:
        """
        Deregisters the specified targets from the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/deregister_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#deregister_targets)
        """

    def get_access_log_subscription(
        self, **kwargs: Unpack[GetAccessLogSubscriptionRequestTypeDef]
    ) -> GetAccessLogSubscriptionResponseTypeDef:
        """
        Retrieves information about the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_access_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_access_log_subscription)
        """

    def get_auth_policy(
        self, **kwargs: Unpack[GetAuthPolicyRequestTypeDef]
    ) -> GetAuthPolicyResponseTypeDef:
        """
        Retrieves information about the auth policy for the specified service or
        service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_auth_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_auth_policy)
        """

    def get_listener(
        self, **kwargs: Unpack[GetListenerRequestTypeDef]
    ) -> GetListenerResponseTypeDef:
        """
        Retrieves information about the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_listener)
        """

    def get_resource_configuration(
        self, **kwargs: Unpack[GetResourceConfigurationRequestTypeDef]
    ) -> GetResourceConfigurationResponseTypeDef:
        """
        Retrieves information about the specified resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_resource_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_resource_configuration)
        """

    def get_resource_gateway(
        self, **kwargs: Unpack[GetResourceGatewayRequestTypeDef]
    ) -> GetResourceGatewayResponseTypeDef:
        """
        Retrieves information about the specified resource gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_resource_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_resource_gateway)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves information about the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_resource_policy)
        """

    def get_rule(self, **kwargs: Unpack[GetRuleRequestTypeDef]) -> GetRuleResponseTypeDef:
        """
        Retrieves information about the specified listener rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_rule)
        """

    def get_service(self, **kwargs: Unpack[GetServiceRequestTypeDef]) -> GetServiceResponseTypeDef:
        """
        Retrieves information about the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_service)
        """

    def get_service_network(
        self, **kwargs: Unpack[GetServiceNetworkRequestTypeDef]
    ) -> GetServiceNetworkResponseTypeDef:
        """
        Retrieves information about the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_service_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_service_network)
        """

    def get_service_network_resource_association(
        self, **kwargs: Unpack[GetServiceNetworkResourceAssociationRequestTypeDef]
    ) -> GetServiceNetworkResourceAssociationResponseTypeDef:
        """
        Retrieves information about the specified association between a service network
        and a resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_service_network_resource_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_service_network_resource_association)
        """

    def get_service_network_service_association(
        self, **kwargs: Unpack[GetServiceNetworkServiceAssociationRequestTypeDef]
    ) -> GetServiceNetworkServiceAssociationResponseTypeDef:
        """
        Retrieves information about the specified association between a service network
        and a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_service_network_service_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_service_network_service_association)
        """

    def get_service_network_vpc_association(
        self, **kwargs: Unpack[GetServiceNetworkVpcAssociationRequestTypeDef]
    ) -> GetServiceNetworkVpcAssociationResponseTypeDef:
        """
        Retrieves information about the specified association between a service network
        and a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_service_network_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_service_network_vpc_association)
        """

    def get_target_group(
        self, **kwargs: Unpack[GetTargetGroupRequestTypeDef]
    ) -> GetTargetGroupResponseTypeDef:
        """
        Retrieves information about the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_target_group)
        """

    def list_access_log_subscriptions(
        self, **kwargs: Unpack[ListAccessLogSubscriptionsRequestTypeDef]
    ) -> ListAccessLogSubscriptionsResponseTypeDef:
        """
        Lists the access log subscriptions for the specified service network or service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_access_log_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_access_log_subscriptions)
        """

    def list_listeners(
        self, **kwargs: Unpack[ListListenersRequestTypeDef]
    ) -> ListListenersResponseTypeDef:
        """
        Lists the listeners for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_listeners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_listeners)
        """

    def list_resource_configurations(
        self, **kwargs: Unpack[ListResourceConfigurationsRequestTypeDef]
    ) -> ListResourceConfigurationsResponseTypeDef:
        """
        Lists the resource configurations owned by or shared with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_resource_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_resource_configurations)
        """

    def list_resource_endpoint_associations(
        self, **kwargs: Unpack[ListResourceEndpointAssociationsRequestTypeDef]
    ) -> ListResourceEndpointAssociationsResponseTypeDef:
        """
        Lists the associations for the specified VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_resource_endpoint_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_resource_endpoint_associations)
        """

    def list_resource_gateways(
        self, **kwargs: Unpack[ListResourceGatewaysRequestTypeDef]
    ) -> ListResourceGatewaysResponseTypeDef:
        """
        Lists the resource gateways that you own or that were shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_resource_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_resource_gateways)
        """

    def list_rules(self, **kwargs: Unpack[ListRulesRequestTypeDef]) -> ListRulesResponseTypeDef:
        """
        Lists the rules for the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_rules)
        """

    def list_service_network_resource_associations(
        self, **kwargs: Unpack[ListServiceNetworkResourceAssociationsRequestTypeDef]
    ) -> ListServiceNetworkResourceAssociationsResponseTypeDef:
        """
        Lists the associations between a service network and a resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_service_network_resource_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_service_network_resource_associations)
        """

    def list_service_network_service_associations(
        self, **kwargs: Unpack[ListServiceNetworkServiceAssociationsRequestTypeDef]
    ) -> ListServiceNetworkServiceAssociationsResponseTypeDef:
        """
        Lists the associations between a service network and a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_service_network_service_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_service_network_service_associations)
        """

    def list_service_network_vpc_associations(
        self, **kwargs: Unpack[ListServiceNetworkVpcAssociationsRequestTypeDef]
    ) -> ListServiceNetworkVpcAssociationsResponseTypeDef:
        """
        Lists the associations between a service network and a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_service_network_vpc_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_service_network_vpc_associations)
        """

    def list_service_network_vpc_endpoint_associations(
        self, **kwargs: Unpack[ListServiceNetworkVpcEndpointAssociationsRequestTypeDef]
    ) -> ListServiceNetworkVpcEndpointAssociationsResponseTypeDef:
        """
        Lists the associations between a service network and a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_service_network_vpc_endpoint_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_service_network_vpc_endpoint_associations)
        """

    def list_service_networks(
        self, **kwargs: Unpack[ListServiceNetworksRequestTypeDef]
    ) -> ListServiceNetworksResponseTypeDef:
        """
        Lists the service networks owned by or shared with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_service_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_service_networks)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesRequestTypeDef]
    ) -> ListServicesResponseTypeDef:
        """
        Lists the services owned by the caller account or shared with the caller
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_services)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_tags_for_resource)
        """

    def list_target_groups(
        self, **kwargs: Unpack[ListTargetGroupsRequestTypeDef]
    ) -> ListTargetGroupsResponseTypeDef:
        """
        Lists your target groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_target_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_target_groups)
        """

    def list_targets(
        self, **kwargs: Unpack[ListTargetsRequestTypeDef]
    ) -> ListTargetsResponseTypeDef:
        """
        Lists the targets for the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/list_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#list_targets)
        """

    def put_auth_policy(
        self, **kwargs: Unpack[PutAuthPolicyRequestTypeDef]
    ) -> PutAuthPolicyResponseTypeDef:
        """
        Creates or updates the auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/put_auth_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#put_auth_policy)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches a resource-based permission policy to a service or service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#put_resource_policy)
        """

    def register_targets(
        self, **kwargs: Unpack[RegisterTargetsRequestTypeDef]
    ) -> RegisterTargetsResponseTypeDef:
        """
        Registers the targets with the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/register_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#register_targets)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#untag_resource)
        """

    def update_access_log_subscription(
        self, **kwargs: Unpack[UpdateAccessLogSubscriptionRequestTypeDef]
    ) -> UpdateAccessLogSubscriptionResponseTypeDef:
        """
        Updates the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_access_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_access_log_subscription)
        """

    def update_listener(
        self, **kwargs: Unpack[UpdateListenerRequestTypeDef]
    ) -> UpdateListenerResponseTypeDef:
        """
        Updates the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_listener)
        """

    def update_resource_configuration(
        self, **kwargs: Unpack[UpdateResourceConfigurationRequestTypeDef]
    ) -> UpdateResourceConfigurationResponseTypeDef:
        """
        Updates the specified resource configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_resource_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_resource_configuration)
        """

    def update_resource_gateway(
        self, **kwargs: Unpack[UpdateResourceGatewayRequestTypeDef]
    ) -> UpdateResourceGatewayResponseTypeDef:
        """
        Updates the specified resource gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_resource_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_resource_gateway)
        """

    def update_rule(self, **kwargs: Unpack[UpdateRuleRequestTypeDef]) -> UpdateRuleResponseTypeDef:
        """
        Updates a specified rule for the listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_rule)
        """

    def update_service(
        self, **kwargs: Unpack[UpdateServiceRequestTypeDef]
    ) -> UpdateServiceResponseTypeDef:
        """
        Updates the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_service)
        """

    def update_service_network(
        self, **kwargs: Unpack[UpdateServiceNetworkRequestTypeDef]
    ) -> UpdateServiceNetworkResponseTypeDef:
        """
        Updates the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_service_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_service_network)
        """

    def update_service_network_vpc_association(
        self, **kwargs: Unpack[UpdateServiceNetworkVpcAssociationRequestTypeDef]
    ) -> UpdateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Updates the service network and VPC association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_service_network_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_service_network_vpc_association)
        """

    def update_target_group(
        self, **kwargs: Unpack[UpdateTargetGroupRequestTypeDef]
    ) -> UpdateTargetGroupResponseTypeDef:
        """
        Updates the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/update_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#update_target_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_log_subscriptions"]
    ) -> ListAccessLogSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_listeners"]
    ) -> ListListenersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_configurations"]
    ) -> ListResourceConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_endpoint_associations"]
    ) -> ListResourceEndpointAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_gateways"]
    ) -> ListResourceGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_network_resource_associations"]
    ) -> ListServiceNetworkResourceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_network_service_associations"]
    ) -> ListServiceNetworkServiceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_network_vpc_associations"]
    ) -> ListServiceNetworkVpcAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_network_vpc_endpoint_associations"]
    ) -> ListServiceNetworkVpcEndpointAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_networks"]
    ) -> ListServiceNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_services"]
    ) -> ListServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_target_groups"]
    ) -> ListTargetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_targets"]
    ) -> ListTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client/#get_paginator)
        """
