"""
Type annotations for emr service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_emr import EMRClient
    from mypy_boto3_emr.waiter import (
        ClusterRunningWaiter,
        ClusterTerminatedWaiter,
        StepCompleteWaiter,
    )

    client: EMRClient = boto3.client("emr")

    cluster_running_waiter: ClusterRunningWaiter = client.get_waiter("cluster_running")
    cluster_terminated_waiter: ClusterTerminatedWaiter = client.get_waiter("cluster_terminated")
    step_complete_waiter: StepCompleteWaiter = client.get_waiter("step_complete")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")

class ClusterRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.ClusterRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterrunningwaiter)
    """

    def wait(self, *, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.ClusterRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterrunningwaiter)
        """

class ClusterTerminatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterterminatedwaiter)
    """

    def wait(self, *, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.ClusterTerminated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterterminatedwaiter)
        """

class StepCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.StepComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#stepcompletewaiter)
    """

    def wait(
        self, *, ClusterId: str, StepId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/emr.html#EMR.Waiter.StepComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#stepcompletewaiter)
        """
