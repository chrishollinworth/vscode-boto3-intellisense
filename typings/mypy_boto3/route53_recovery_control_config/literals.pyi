"""
Type annotations for route53-recovery-control-config service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/literals.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_control_config.literals import ClusterCreatedWaiterName

    data: ClusterCreatedWaiterName = "cluster_created"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ClusterCreatedWaiterName",
    "ClusterDeletedWaiterName",
    "ControlPanelCreatedWaiterName",
    "ControlPanelDeletedWaiterName",
    "ListAssociatedRoute53HealthChecksPaginatorName",
    "ListClustersPaginatorName",
    "ListControlPanelsPaginatorName",
    "ListRoutingControlsPaginatorName",
    "ListSafetyRulesPaginatorName",
    "RoutingControlCreatedWaiterName",
    "RoutingControlDeletedWaiterName",
    "RuleTypeType",
    "StatusType",
)

ClusterCreatedWaiterName = Literal["cluster_created"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ControlPanelCreatedWaiterName = Literal["control_panel_created"]
ControlPanelDeletedWaiterName = Literal["control_panel_deleted"]
ListAssociatedRoute53HealthChecksPaginatorName = Literal["list_associated_route53_health_checks"]
ListClustersPaginatorName = Literal["list_clusters"]
ListControlPanelsPaginatorName = Literal["list_control_panels"]
ListRoutingControlsPaginatorName = Literal["list_routing_controls"]
ListSafetyRulesPaginatorName = Literal["list_safety_rules"]
RoutingControlCreatedWaiterName = Literal["routing_control_created"]
RoutingControlDeletedWaiterName = Literal["routing_control_deleted"]
RuleTypeType = Literal["AND", "ATLEAST", "OR"]
StatusType = Literal["DEPLOYED", "PENDING", "PENDING_DELETION"]
