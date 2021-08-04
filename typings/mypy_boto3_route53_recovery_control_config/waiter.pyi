"""
Type annotations for route53-recovery-control-config service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53_recovery_control_config import Route53RecoveryControlConfigClient
    from mypy_boto3_route53_recovery_control_config.waiter import (
        ClusterCreatedWaiter,
        ClusterDeletedWaiter,
        ControlPanelCreatedWaiter,
        ControlPanelDeletedWaiter,
        RoutingControlCreatedWaiter,
        RoutingControlDeletedWaiter,
    )

    client: Route53RecoveryControlConfigClient = boto3.client("route53-recovery-control-config")

    cluster_created_waiter: ClusterCreatedWaiter = client.get_waiter("cluster_created")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    control_panel_created_waiter: ControlPanelCreatedWaiter = client.get_waiter("control_panel_created")
    control_panel_deleted_waiter: ControlPanelDeletedWaiter = client.get_waiter("control_panel_deleted")
    routing_control_created_waiter: RoutingControlCreatedWaiter = client.get_waiter("routing_control_created")
    routing_control_deleted_waiter: RoutingControlDeletedWaiter = client.get_waiter("routing_control_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "ClusterCreatedWaiter",
    "ClusterDeletedWaiter",
    "ControlPanelCreatedWaiter",
    "ControlPanelDeletedWaiter",
    "RoutingControlCreatedWaiter",
    "RoutingControlDeletedWaiter",
)

class ClusterCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clustercreatedwaiter)
    """

    def wait(self, *, ClusterArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clustercreatedwaiter)
        """

class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clusterdeletedwaiter)
    """

    def wait(self, *, ClusterArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ClusterDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#clusterdeletedwaiter)
        """

class ControlPanelCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpanelcreatedwaiter)
    """

    def wait(self, *, ControlPanelArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpanelcreatedwaiter)
        """

class ControlPanelDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpaneldeletedwaiter)
    """

    def wait(self, *, ControlPanelArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.ControlPanelDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#controlpaneldeletedwaiter)
        """

class RoutingControlCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontrolcreatedwaiter)
    """

    def wait(self, *, RoutingControlArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontrolcreatedwaiter)
        """

class RoutingControlDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontroldeletedwaiter)
    """

    def wait(self, *, RoutingControlArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Waiter.RoutingControlDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/waiters.html#routingcontroldeletedwaiter)
        """
