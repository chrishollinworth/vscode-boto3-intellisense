"""
Type annotations for vpc-lattice service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_vpc_lattice import VPCLatticeClient

    client: VPCLatticeClient = boto3.client("vpc-lattice")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AuthTypeType, ListenerProtocolType, TargetGroupTypeType
from .paginator import (
    ListAccessLogSubscriptionsPaginator,
    ListListenersPaginator,
    ListRulesPaginator,
    ListServiceNetworkServiceAssociationsPaginator,
    ListServiceNetworksPaginator,
    ListServiceNetworkVpcAssociationsPaginator,
    ListServicesPaginator,
    ListTargetGroupsPaginator,
    ListTargetsPaginator,
)
from .type_defs import (
    BatchUpdateRuleResponseTypeDef,
    CreateAccessLogSubscriptionResponseTypeDef,
    CreateListenerResponseTypeDef,
    CreateRuleResponseTypeDef,
    CreateServiceNetworkResponseTypeDef,
    CreateServiceNetworkServiceAssociationResponseTypeDef,
    CreateServiceNetworkVpcAssociationResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateTargetGroupResponseTypeDef,
    DeleteServiceNetworkServiceAssociationResponseTypeDef,
    DeleteServiceNetworkVpcAssociationResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTargetGroupResponseTypeDef,
    DeregisterTargetsResponseTypeDef,
    GetAccessLogSubscriptionResponseTypeDef,
    GetAuthPolicyResponseTypeDef,
    GetListenerResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRuleResponseTypeDef,
    GetServiceNetworkResponseTypeDef,
    GetServiceNetworkServiceAssociationResponseTypeDef,
    GetServiceNetworkVpcAssociationResponseTypeDef,
    GetServiceResponseTypeDef,
    GetTargetGroupResponseTypeDef,
    HealthCheckConfigTypeDef,
    ListAccessLogSubscriptionsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListRulesResponseTypeDef,
    ListServiceNetworkServiceAssociationsResponseTypeDef,
    ListServiceNetworksResponseTypeDef,
    ListServiceNetworkVpcAssociationsResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetGroupsResponseTypeDef,
    ListTargetsResponseTypeDef,
    PutAuthPolicyResponseTypeDef,
    RegisterTargetsResponseTypeDef,
    RuleActionTypeDef,
    RuleMatchTypeDef,
    RuleUpdateTypeDef,
    TargetGroupConfigTypeDef,
    TargetTypeDef,
    UpdateAccessLogSubscriptionResponseTypeDef,
    UpdateListenerResponseTypeDef,
    UpdateRuleResponseTypeDef,
    UpdateServiceNetworkResponseTypeDef,
    UpdateServiceNetworkVpcAssociationResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTargetGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("VPCLatticeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VPCLatticeClient exceptions.
        """
    def batch_update_rule(
        self, *, listenerIdentifier: str, rules: List["RuleUpdateTypeDef"], serviceIdentifier: str
    ) -> BatchUpdateRuleResponseTypeDef:
        """
        Updates the listener rules in a batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.batch_update_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#batch_update_rule)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#close)
        """
    def create_access_log_subscription(
        self,
        *,
        destinationArn: str,
        resourceIdentifier: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAccessLogSubscriptionResponseTypeDef:
        """
        Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon
        Kinesis Data Firehose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_access_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_access_log_subscription)
        """
    def create_listener(
        self,
        *,
        defaultAction: "RuleActionTypeDef",
        name: str,
        protocol: ListenerProtocolType,
        serviceIdentifier: str,
        clientToken: str = None,
        port: int = None,
        tags: Dict[str, str] = None
    ) -> CreateListenerResponseTypeDef:
        """
        Creates a listener for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_listener)
        """
    def create_rule(
        self,
        *,
        action: "RuleActionTypeDef",
        listenerIdentifier: str,
        match: "RuleMatchTypeDef",
        name: str,
        priority: int,
        serviceIdentifier: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_rule)
        """
    def create_service(
        self,
        *,
        name: str,
        authType: AuthTypeType = None,
        certificateArn: str = None,
        clientToken: str = None,
        customDomainName: str = None,
        tags: Dict[str, str] = None
    ) -> CreateServiceResponseTypeDef:
        """
        Creates a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_service)
        """
    def create_service_network(
        self,
        *,
        name: str,
        authType: AuthTypeType = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateServiceNetworkResponseTypeDef:
        """
        Creates a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_service_network)
        """
    def create_service_network_service_association(
        self,
        *,
        serviceIdentifier: str,
        serviceNetworkIdentifier: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateServiceNetworkServiceAssociationResponseTypeDef:
        """
        Associates a service with a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network_service_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_service_network_service_association)
        """
    def create_service_network_vpc_association(
        self,
        *,
        serviceNetworkIdentifier: str,
        vpcIdentifier: str,
        clientToken: str = None,
        securityGroupIds: List[str] = None,
        tags: Dict[str, str] = None
    ) -> CreateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Associates a VPC with a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_service_network_vpc_association)
        """
    def create_target_group(
        self,
        *,
        name: str,
        type: TargetGroupTypeType,
        clientToken: str = None,
        config: "TargetGroupConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateTargetGroupResponseTypeDef:
        """
        Creates a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.create_target_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#create_target_group)
        """
    def delete_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_access_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_access_log_subscription)
        """
    def delete_auth_policy(self, *, resourceIdentifier: str) -> Dict[str, Any]:
        """
        Deletes the specified auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_auth_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_auth_policy)
        """
    def delete_listener(self, *, listenerIdentifier: str, serviceIdentifier: str) -> Dict[str, Any]:
        """
        Deletes the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_listener)
        """
    def delete_resource_policy(self, *, resourceArn: str) -> Dict[str, Any]:
        """
        Deletes the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_resource_policy)
        """
    def delete_rule(
        self, *, listenerIdentifier: str, ruleIdentifier: str, serviceIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_rule)
        """
    def delete_service(self, *, serviceIdentifier: str) -> DeleteServiceResponseTypeDef:
        """
        Deletes a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_service)
        """
    def delete_service_network(self, *, serviceNetworkIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_service_network)
        """
    def delete_service_network_service_association(
        self, *, serviceNetworkServiceAssociationIdentifier: str
    ) -> DeleteServiceNetworkServiceAssociationResponseTypeDef:
        """
        Deletes the association between a specified service and the specific service
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network_service_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_service_network_service_association)
        """
    def delete_service_network_vpc_association(
        self, *, serviceNetworkVpcAssociationIdentifier: str
    ) -> DeleteServiceNetworkVpcAssociationResponseTypeDef:
        """
        Disassociates the VPC from the service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_service_network_vpc_association)
        """
    def delete_target_group(
        self, *, targetGroupIdentifier: str
    ) -> DeleteTargetGroupResponseTypeDef:
        """
        Deletes a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.delete_target_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#delete_target_group)
        """
    def deregister_targets(
        self, *, targetGroupIdentifier: str, targets: List["TargetTypeDef"]
    ) -> DeregisterTargetsResponseTypeDef:
        """
        Deregisters the specified targets from the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.deregister_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#deregister_targets)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#generate_presigned_url)
        """
    def get_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str
    ) -> GetAccessLogSubscriptionResponseTypeDef:
        """
        Retrieves information about the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_access_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_access_log_subscription)
        """
    def get_auth_policy(self, *, resourceIdentifier: str) -> GetAuthPolicyResponseTypeDef:
        """
        Retrieves information about the auth policy for the specified service or service
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_auth_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_auth_policy)
        """
    def get_listener(
        self, *, listenerIdentifier: str, serviceIdentifier: str
    ) -> GetListenerResponseTypeDef:
        """
        Retrieves information about the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_listener)
        """
    def get_resource_policy(self, *, resourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves information about the resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_resource_policy)
        """
    def get_rule(
        self, *, listenerIdentifier: str, ruleIdentifier: str, serviceIdentifier: str
    ) -> GetRuleResponseTypeDef:
        """
        Retrieves information about listener rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_rule)
        """
    def get_service(self, *, serviceIdentifier: str) -> GetServiceResponseTypeDef:
        """
        Retrieves information about the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_service)
        """
    def get_service_network(
        self, *, serviceNetworkIdentifier: str
    ) -> GetServiceNetworkResponseTypeDef:
        """
        Retrieves information about the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_service_network)
        """
    def get_service_network_service_association(
        self, *, serviceNetworkServiceAssociationIdentifier: str
    ) -> GetServiceNetworkServiceAssociationResponseTypeDef:
        """
        Retrieves information about the specified association between a service network
        and a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network_service_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_service_network_service_association)
        """
    def get_service_network_vpc_association(
        self, *, serviceNetworkVpcAssociationIdentifier: str
    ) -> GetServiceNetworkVpcAssociationResponseTypeDef:
        """
        Retrieves information about the association between a service network and a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_service_network_vpc_association)
        """
    def get_target_group(self, *, targetGroupIdentifier: str) -> GetTargetGroupResponseTypeDef:
        """
        Retrieves information about the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.get_target_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#get_target_group)
        """
    def list_access_log_subscriptions(
        self, *, resourceIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListAccessLogSubscriptionsResponseTypeDef:
        """
        Lists all access log subscriptions for the specified service network or service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_access_log_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_access_log_subscriptions)
        """
    def list_listeners(
        self, *, serviceIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        Lists the listeners for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_listeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_listeners)
        """
    def list_rules(
        self,
        *,
        listenerIdentifier: str,
        serviceIdentifier: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListRulesResponseTypeDef:
        """
        Lists the rules for the listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_rules)
        """
    def list_service_network_service_associations(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        serviceIdentifier: str = None,
        serviceNetworkIdentifier: str = None
    ) -> ListServiceNetworkServiceAssociationsResponseTypeDef:
        """
        Lists the associations between the service network and the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_network_service_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_service_network_service_associations)
        """
    def list_service_network_vpc_associations(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        serviceNetworkIdentifier: str = None,
        vpcIdentifier: str = None
    ) -> ListServiceNetworkVpcAssociationsResponseTypeDef:
        """
        Lists the service network and VPC associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_network_vpc_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_service_network_vpc_associations)
        """
    def list_service_networks(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServiceNetworksResponseTypeDef:
        """
        Lists the service networks owned by the caller account or shared with the caller
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_service_networks)
        """
    def list_services(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListServicesResponseTypeDef:
        """
        Lists the services owned by the caller account or shared with the caller
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_services)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_tags_for_resource)
        """
    def list_target_groups(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        targetGroupType: TargetGroupTypeType = None,
        vpcIdentifier: str = None
    ) -> ListTargetGroupsResponseTypeDef:
        """
        Lists your target groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_target_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_target_groups)
        """
    def list_targets(
        self,
        *,
        targetGroupIdentifier: str,
        maxResults: int = None,
        nextToken: str = None,
        targets: List["TargetTypeDef"] = None
    ) -> ListTargetsResponseTypeDef:
        """
        Lists the targets for the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.list_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#list_targets)
        """
    def put_auth_policy(
        self, *, policy: str, resourceIdentifier: str
    ) -> PutAuthPolicyResponseTypeDef:
        """
        Creates or updates the auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.put_auth_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#put_auth_policy)
        """
    def put_resource_policy(self, *, policy: str, resourceArn: str) -> Dict[str, Any]:
        """
        Attaches a resource-based permission policy to a service or service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#put_resource_policy)
        """
    def register_targets(
        self, *, targetGroupIdentifier: str, targets: List["TargetTypeDef"]
    ) -> RegisterTargetsResponseTypeDef:
        """
        Registers the targets with the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.register_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#register_targets)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#untag_resource)
        """
    def update_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str, destinationArn: str
    ) -> UpdateAccessLogSubscriptionResponseTypeDef:
        """
        Updates the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_access_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_access_log_subscription)
        """
    def update_listener(
        self, *, defaultAction: "RuleActionTypeDef", listenerIdentifier: str, serviceIdentifier: str
    ) -> UpdateListenerResponseTypeDef:
        """
        Updates the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_listener)
        """
    def update_rule(
        self,
        *,
        listenerIdentifier: str,
        ruleIdentifier: str,
        serviceIdentifier: str,
        action: "RuleActionTypeDef" = None,
        match: "RuleMatchTypeDef" = None,
        priority: int = None
    ) -> UpdateRuleResponseTypeDef:
        """
        Updates a rule for the listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_rule)
        """
    def update_service(
        self, *, serviceIdentifier: str, authType: AuthTypeType = None, certificateArn: str = None
    ) -> UpdateServiceResponseTypeDef:
        """
        Updates the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_service)
        """
    def update_service_network(
        self, *, authType: AuthTypeType, serviceNetworkIdentifier: str
    ) -> UpdateServiceNetworkResponseTypeDef:
        """
        Updates the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_service_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_service_network)
        """
    def update_service_network_vpc_association(
        self, *, securityGroupIds: List[str], serviceNetworkVpcAssociationIdentifier: str
    ) -> UpdateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Updates the service network and VPC association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_service_network_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_service_network_vpc_association)
        """
    def update_target_group(
        self, *, healthCheck: "HealthCheckConfigTypeDef", targetGroupIdentifier: str
    ) -> UpdateTargetGroupResponseTypeDef:
        """
        Updates the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Client.update_target_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/client.html#update_target_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_log_subscriptions"]
    ) -> ListAccessLogSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListAccessLogSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listaccesslogsubscriptionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListListeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listlistenerspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listrulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_network_service_associations"]
    ) -> ListServiceNetworkServiceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkServiceAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkserviceassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_network_vpc_associations"]
    ) -> ListServiceNetworkVpcAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworkVpcAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkvpcassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_networks"]
    ) -> ListServiceNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServiceNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicenetworkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_target_groups"]
    ) -> ListTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetgroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_targets"]) -> ListTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/vpc-lattice.html#VPCLattice.Paginator.ListTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/paginators.html#listtargetspaginator)
        """
