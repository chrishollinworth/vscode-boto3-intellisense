# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for emr service client waiters.

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

from mypy_boto3_emr.type_defs import WaiterConfigTypeDef

__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")


class ClusterRunningWaiter(Boto3Waiter):
    """
    [Waiter.ClusterRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.ClusterRunning)
    """

    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.ClusterRunning.wait)
        """


class ClusterTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
    """

    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.ClusterTerminated.wait)
        """


class StepCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StepComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.StepComplete)
    """

    def wait(self, ClusterId: str, StepId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [StepComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/emr.html#EMR.Waiter.StepComplete.wait)
        """
