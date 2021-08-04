"""
Type annotations for route53-recovery-control-config service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53_recovery_control_config import Route53RecoveryControlConfigClient

    client: Route53RecoveryControlConfigClient = boto3.client("route53-recovery-control-config")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    AssertionRuleUpdateTypeDef,
    CreateClusterResponseTypeDef,
    CreateControlPanelResponseTypeDef,
    CreateRoutingControlResponseTypeDef,
    CreateSafetyRuleResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeControlPanelResponseTypeDef,
    DescribeRoutingControlResponseTypeDef,
    DescribeSafetyRuleResponseTypeDef,
    GatingRuleUpdateTypeDef,
    ListAssociatedRoute53HealthChecksResponseTypeDef,
    ListClustersResponseTypeDef,
    ListControlPanelsResponseTypeDef,
    ListRoutingControlsResponseTypeDef,
    ListSafetyRulesResponseTypeDef,
    NewAssertionRuleTypeDef,
    NewGatingRuleTypeDef,
    UpdateControlPanelResponseTypeDef,
    UpdateRoutingControlResponseTypeDef,
    UpdateSafetyRuleResponseTypeDef,
)
from .waiter import (
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    ControlPanelCreatedWaiter,
    ControlPanelDeletedWaiter,
    RoutingControlCreatedWaiter,
    RoutingControlDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Route53RecoveryControlConfigClient",)

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

class Route53RecoveryControlConfigClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryControlConfigClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#can_paginate)
        """
    def create_cluster(
        self, *, ClusterName: str, ClientToken: str = None
    ) -> CreateClusterResponseTypeDef:
        """
        Create a new cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#create_cluster)
        """
    def create_control_panel(
        self, *, ClusterArn: str, ControlPanelName: str, ClientToken: str = None
    ) -> CreateControlPanelResponseTypeDef:
        """
        Creates a new control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_control_panel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#create_control_panel)
        """
    def create_routing_control(
        self,
        *,
        ClusterArn: str,
        RoutingControlName: str,
        ClientToken: str = None,
        ControlPanelArn: str = None
    ) -> CreateRoutingControlResponseTypeDef:
        """
        Creates a new routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_routing_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#create_routing_control)
        """
    def create_safety_rule(
        self,
        *,
        AssertionRule: "NewAssertionRuleTypeDef" = None,
        ClientToken: str = None,
        GatingRule: "NewGatingRuleTypeDef" = None
    ) -> CreateSafetyRuleResponseTypeDef:
        """
        Creates a safety rule in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_safety_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#create_safety_rule)
        """
    def delete_cluster(self, *, ClusterArn: str) -> Dict[str, Any]:
        """
        Delete a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#delete_cluster)
        """
    def delete_control_panel(self, *, ControlPanelArn: str) -> Dict[str, Any]:
        """
        Deletes a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_control_panel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#delete_control_panel)
        """
    def delete_routing_control(self, *, RoutingControlArn: str) -> Dict[str, Any]:
        """
        Deletes a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_routing_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#delete_routing_control)
        """
    def delete_safety_rule(self, *, SafetyRuleArn: str) -> Dict[str, Any]:
        """
        Deletes a safety rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_safety_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#delete_safety_rule)
        """
    def describe_cluster(self, *, ClusterArn: str) -> DescribeClusterResponseTypeDef:
        """
        Display the details about a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#describe_cluster)
        """
    def describe_control_panel(
        self, *, ControlPanelArn: str
    ) -> DescribeControlPanelResponseTypeDef:
        """
        Displays details about a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_control_panel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#describe_control_panel)
        """
    def describe_routing_control(
        self, *, RoutingControlArn: str
    ) -> DescribeRoutingControlResponseTypeDef:
        """
        Displays details about a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_routing_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#describe_routing_control)
        """
    def describe_safety_rule(self, *, SafetyRuleArn: str) -> DescribeSafetyRuleResponseTypeDef:
        """
        Describes the safety rules (that is, the assertion rules and gating rules) for
        the routing controls in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_safety_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#describe_safety_rule)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#generate_presigned_url)
        """
    def list_associated_route53_health_checks(
        self, *, RoutingControlArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociatedRoute53HealthChecksResponseTypeDef:
        """
        Returns an array of all Amazon Route 53 health checks associated with a specific
        routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_associated_route53_health_checks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#list_associated_route53_health_checks)
        """
    def list_clusters(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResponseTypeDef:
        """
        Returns an array of all the clusters in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#list_clusters)
        """
    def list_control_panels(
        self, *, ClusterArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListControlPanelsResponseTypeDef:
        """
        Returns an array of control panels for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_control_panels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#list_control_panels)
        """
    def list_routing_controls(
        self, *, ControlPanelArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRoutingControlsResponseTypeDef:
        """
        Returns an array of routing controls for a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_routing_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#list_routing_controls)
        """
    def list_safety_rules(
        self, *, ControlPanelArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListSafetyRulesResponseTypeDef:
        """
        List the safety rules (the assertion rules and gating rules) that you've defined
        for the routing controls in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_safety_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#list_safety_rules)
        """
    def update_control_panel(
        self, *, ControlPanelArn: str, ControlPanelName: str
    ) -> UpdateControlPanelResponseTypeDef:
        """
        Updates a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_control_panel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#update_control_panel)
        """
    def update_routing_control(
        self, *, RoutingControlArn: str, RoutingControlName: str
    ) -> UpdateRoutingControlResponseTypeDef:
        """
        Updates a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_routing_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#update_routing_control)
        """
    def update_safety_rule(
        self,
        *,
        AssertionRuleUpdate: "AssertionRuleUpdateTypeDef" = None,
        GatingRuleUpdate: "GatingRuleUpdateTypeDef" = None
    ) -> UpdateSafetyRuleResponseTypeDef:
        """
        Update a safety rule (an assertion rule or gating rule) for the routing controls
        in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_safety_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client.html#update_safety_rule)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_created"]) -> ClusterCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clustercreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clusterdeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["control_panel_created"]
    ) -> ControlPanelCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpanelcreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["control_panel_deleted"]
    ) -> ControlPanelDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpaneldeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["routing_control_created"]
    ) -> RoutingControlCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontrolcreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["routing_control_deleted"]
    ) -> RoutingControlDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontroldeletedwaiter)
        """
