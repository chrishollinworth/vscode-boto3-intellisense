"""
Type annotations for opsworkscm service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworkscm import OpsWorksCMClient
    from mypy_boto3_opsworkscm.waiter import (
        NodeAssociatedWaiter,
    )

    client: OpsWorksCMClient = boto3.client("opsworkscm")

    node_associated_waiter: NodeAssociatedWaiter = client.get_waiter("node_associated")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("NodeAssociatedWaiter",)

class NodeAssociatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/waiters.html#nodeassociatedwaiter)
    """

    def wait(
        self,
        *,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/waiters.html#nodeassociatedwaiter)
        """
