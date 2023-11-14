"""
Type annotations for route53-recovery-cluster service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53_recovery_cluster import Route53RecoveryClusterClient

    client: Route53RecoveryClusterClient = boto3.client("route53-recovery-cluster")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import RoutingControlStateType
from .paginator import ListRoutingControlsPaginator
from .type_defs import (
    GetRoutingControlStateResponseTypeDef,
    ListRoutingControlsResponseTypeDef,
    UpdateRoutingControlStateEntryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Route53RecoveryClusterClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EndpointTemporarilyUnavailableException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryClusterClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryClusterClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#generate_presigned_url)
        """
    def get_routing_control_state(
        self, *, RoutingControlArn: str
    ) -> GetRoutingControlStateResponseTypeDef:
        """
        Get the state for a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.get_routing_control_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#get_routing_control_state)
        """
    def list_routing_controls(
        self, *, ControlPanelArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingControlsResponseTypeDef:
        """
        List routing control names and Amazon Resource Names (ARNs), as well as the
        routing control state for each routing control, along with the control panel
        name and control panel ARN for the routing controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.list_routing_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#list_routing_controls)
        """
    def update_routing_control_state(
        self,
        *,
        RoutingControlArn: str,
        RoutingControlState: RoutingControlStateType,
        SafetyRulesToOverride: List[str] = None
    ) -> Dict[str, Any]:
        """
        Set the state of the routing control to reroute traffic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.update_routing_control_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#update_routing_control_state)
        """
    def update_routing_control_states(
        self,
        *,
        UpdateRoutingControlStateEntries: List["UpdateRoutingControlStateEntryTypeDef"],
        SafetyRulesToOverride: List[str] = None
    ) -> Dict[str, Any]:
        """
        Set multiple routing control states.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.update_routing_control_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#update_routing_control_states)
        """
    def get_paginator(
        self, operation_name: Literal["list_routing_controls"]
    ) -> ListRoutingControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Paginator.ListRoutingControls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/paginators.html#listroutingcontrolspaginator)
        """
