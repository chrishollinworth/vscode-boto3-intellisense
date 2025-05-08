"""
Type annotations for deadline service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_deadline.client import DeadlineCloudClient
    from mypy_boto3_deadline.waiter import (
        FleetActiveWaiter,
        JobCreateCompleteWaiter,
        LicenseEndpointDeletedWaiter,
        LicenseEndpointValidWaiter,
        QueueFleetAssociationStoppedWaiter,
        QueueLimitAssociationStoppedWaiter,
        QueueSchedulingBlockedWaiter,
        QueueSchedulingWaiter,
    )

    session = Session()
    client: DeadlineCloudClient = session.client("deadline")

    fleet_active_waiter: FleetActiveWaiter = client.get_waiter("fleet_active")
    job_create_complete_waiter: JobCreateCompleteWaiter = client.get_waiter("job_create_complete")
    license_endpoint_deleted_waiter: LicenseEndpointDeletedWaiter = client.get_waiter("license_endpoint_deleted")
    license_endpoint_valid_waiter: LicenseEndpointValidWaiter = client.get_waiter("license_endpoint_valid")
    queue_fleet_association_stopped_waiter: QueueFleetAssociationStoppedWaiter = client.get_waiter("queue_fleet_association_stopped")
    queue_limit_association_stopped_waiter: QueueLimitAssociationStoppedWaiter = client.get_waiter("queue_limit_association_stopped")
    queue_scheduling_blocked_waiter: QueueSchedulingBlockedWaiter = client.get_waiter("queue_scheduling_blocked")
    queue_scheduling_waiter: QueueSchedulingWaiter = client.get_waiter("queue_scheduling")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetFleetRequestWaitTypeDef,
    GetJobRequestWaitTypeDef,
    GetLicenseEndpointRequestWaitExtraTypeDef,
    GetLicenseEndpointRequestWaitTypeDef,
    GetQueueFleetAssociationRequestWaitTypeDef,
    GetQueueLimitAssociationRequestWaitTypeDef,
    GetQueueRequestWaitExtraTypeDef,
    GetQueueRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "FleetActiveWaiter",
    "JobCreateCompleteWaiter",
    "LicenseEndpointDeletedWaiter",
    "LicenseEndpointValidWaiter",
    "QueueFleetAssociationStoppedWaiter",
    "QueueLimitAssociationStoppedWaiter",
    "QueueSchedulingBlockedWaiter",
    "QueueSchedulingWaiter",
)

class FleetActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/FleetActive.html#DeadlineCloud.Waiter.FleetActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#fleetactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFleetRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/FleetActive.html#DeadlineCloud.Waiter.FleetActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#fleetactivewaiter)
        """

class JobCreateCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/JobCreateComplete.html#DeadlineCloud.Waiter.JobCreateComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#jobcreatecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetJobRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/JobCreateComplete.html#DeadlineCloud.Waiter.JobCreateComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#jobcreatecompletewaiter)
        """

class LicenseEndpointDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/LicenseEndpointDeleted.html#DeadlineCloud.Waiter.LicenseEndpointDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#licenseendpointdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetLicenseEndpointRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/LicenseEndpointDeleted.html#DeadlineCloud.Waiter.LicenseEndpointDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#licenseendpointdeletedwaiter)
        """

class LicenseEndpointValidWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/LicenseEndpointValid.html#DeadlineCloud.Waiter.LicenseEndpointValid)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#licenseendpointvalidwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetLicenseEndpointRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/LicenseEndpointValid.html#DeadlineCloud.Waiter.LicenseEndpointValid.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#licenseendpointvalidwaiter)
        """

class QueueFleetAssociationStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueFleetAssociationStopped.html#DeadlineCloud.Waiter.QueueFleetAssociationStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queuefleetassociationstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueueFleetAssociationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueFleetAssociationStopped.html#DeadlineCloud.Waiter.QueueFleetAssociationStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queuefleetassociationstoppedwaiter)
        """

class QueueLimitAssociationStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueLimitAssociationStopped.html#DeadlineCloud.Waiter.QueueLimitAssociationStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queuelimitassociationstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueueLimitAssociationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueLimitAssociationStopped.html#DeadlineCloud.Waiter.QueueLimitAssociationStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queuelimitassociationstoppedwaiter)
        """

class QueueSchedulingBlockedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueSchedulingBlocked.html#DeadlineCloud.Waiter.QueueSchedulingBlocked)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queueschedulingblockedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueueRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueSchedulingBlocked.html#DeadlineCloud.Waiter.QueueSchedulingBlocked.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queueschedulingblockedwaiter)
        """

class QueueSchedulingWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueScheduling.html#DeadlineCloud.Waiter.QueueScheduling)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queueschedulingwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueueRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/waiter/QueueScheduling.html#DeadlineCloud.Waiter.QueueScheduling.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters/#queueschedulingwaiter)
        """
