"""
Type annotations for route53-recovery-cluster service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/literals.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_cluster.literals import ListRoutingControlsPaginatorName

    data: ListRoutingControlsPaginatorName = "list_routing_controls"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListRoutingControlsPaginatorName", "RoutingControlStateType")

ListRoutingControlsPaginatorName = Literal["list_routing_controls"]
RoutingControlStateType = Literal["Off", "On"]
