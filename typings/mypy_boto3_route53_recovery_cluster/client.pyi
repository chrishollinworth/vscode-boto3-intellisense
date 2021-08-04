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
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import RoutingControlStateType
from .type_defs import GetRoutingControlStateResponseTypeDef, UpdateRoutingControlStateEntryTypeDef

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryClusterClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#generate_presigned_url)
        """
    def get_routing_control_state(
        self, *, RoutingControlArn: str
    ) -> GetRoutingControlStateResponseTypeDef:
        """
        Get the state for a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.get_routing_control_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#get_routing_control_state)
        """
    def update_routing_control_state(
        self, *, RoutingControlArn: str, RoutingControlState: RoutingControlStateType
    ) -> Dict[str, Any]:
        """
        Set the state of the routing control to reroute traffic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.update_routing_control_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#update_routing_control_state)
        """
    def update_routing_control_states(
        self, *, UpdateRoutingControlStateEntries: List["UpdateRoutingControlStateEntryTypeDef"]
    ) -> Dict[str, Any]:
        """
        Set multiple routing control states.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client.update_routing_control_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client.html#update_routing_control_states)
        """
