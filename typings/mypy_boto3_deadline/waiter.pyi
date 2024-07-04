"""
Type annotations for deadline service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_deadline import DeadlineCloudClient
    from mypy_boto3_deadline.waiter import (
        FleetActiveWaiter,
        JobCreateCompleteWaiter,
        LicenseEndpointDeletedWaiter,
        LicenseEndpointValidWaiter,
        QueueFleetAssociationStoppedWaiter,
        QueueSchedulingWaiter,
        QueueSchedulingBlockedWaiter,
    )

    client: DeadlineCloudClient = boto3.client("deadline")

    fleet_active_waiter: FleetActiveWaiter = client.get_waiter("fleet_active")
    job_create_complete_waiter: JobCreateCompleteWaiter = client.get_waiter("job_create_complete")
    license_endpoint_deleted_waiter: LicenseEndpointDeletedWaiter = client.get_waiter("license_endpoint_deleted")
    license_endpoint_valid_waiter: LicenseEndpointValidWaiter = client.get_waiter("license_endpoint_valid")
    queue_fleet_association_stopped_waiter: QueueFleetAssociationStoppedWaiter = client.get_waiter("queue_fleet_association_stopped")
    queue_scheduling_waiter: QueueSchedulingWaiter = client.get_waiter("queue_scheduling")
    queue_scheduling_blocked_waiter: QueueSchedulingBlockedWaiter = client.get_waiter("queue_scheduling_blocked")
    ```
"""

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "FleetActiveWaiter",
    "JobCreateCompleteWaiter",
    "LicenseEndpointDeletedWaiter",
    "LicenseEndpointValidWaiter",
    "QueueFleetAssociationStoppedWaiter",
    "QueueSchedulingWaiter",
    "QueueSchedulingBlockedWaiter",
)

class FleetActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.FleetActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#fleetactivewaiter)
    """

    def wait(self, *, farmId: str, fleetId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.FleetActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#fleetactivewaiter)
        """

class JobCreateCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.JobCreateComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#jobcreatecompletewaiter)
    """

    def wait(
        self, *, farmId: str, jobId: str, queueId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.JobCreateComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#jobcreatecompletewaiter)
        """

class LicenseEndpointDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointdeletedwaiter)
    """

    def wait(self, *, licenseEndpointId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointdeletedwaiter)
        """

class LicenseEndpointValidWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointValid)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointvalidwaiter)
    """

    def wait(self, *, licenseEndpointId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointValid.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointvalidwaiter)
        """

class QueueFleetAssociationStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueFleetAssociationStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queuefleetassociationstoppedwaiter)
    """

    def wait(
        self, *, farmId: str, fleetId: str, queueId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueFleetAssociationStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queuefleetassociationstoppedwaiter)
        """

class QueueSchedulingWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueScheduling)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingwaiter)
    """

    def wait(self, *, farmId: str, queueId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueScheduling.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingwaiter)
        """

class QueueSchedulingBlockedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueSchedulingBlocked)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingblockedwaiter)
    """

    def wait(self, *, farmId: str, queueId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueSchedulingBlocked.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingblockedwaiter)
        """
