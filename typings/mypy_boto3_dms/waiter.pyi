# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for dms service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_dms import DatabaseMigrationServiceClient
    from mypy_boto3_dms.waiter import (
        EndpointDeletedWaiter,
        ReplicationInstanceAvailableWaiter,
        ReplicationInstanceDeletedWaiter,
        ReplicationTaskDeletedWaiter,
        ReplicationTaskReadyWaiter,
        ReplicationTaskRunningWaiter,
        ReplicationTaskStoppedWaiter,
        TestConnectionSucceedsWaiter,
    )

    client: DatabaseMigrationServiceClient = boto3.client("dms")

    endpoint_deleted_waiter: EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
    replication_instance_available_waiter: ReplicationInstanceAvailableWaiter = client.get_waiter("replication_instance_available")
    replication_instance_deleted_waiter: ReplicationInstanceDeletedWaiter = client.get_waiter("replication_instance_deleted")
    replication_task_deleted_waiter: ReplicationTaskDeletedWaiter = client.get_waiter("replication_task_deleted")
    replication_task_ready_waiter: ReplicationTaskReadyWaiter = client.get_waiter("replication_task_ready")
    replication_task_running_waiter: ReplicationTaskRunningWaiter = client.get_waiter("replication_task_running")
    replication_task_stopped_waiter: ReplicationTaskStoppedWaiter = client.get_waiter("replication_task_stopped")
    test_connection_succeeds_waiter: TestConnectionSucceedsWaiter = client.get_waiter("test_connection_succeeds")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_dms.type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = (
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EndpointDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted.wait)
        """


class ReplicationInstanceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationInstanceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable.wait)
        """


class ReplicationInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted.wait)
        """


class ReplicationTaskDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted.wait)
        """


class ReplicationTaskReadyWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskReady.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady.wait)
        """


class ReplicationTaskRunningWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning.wait)
        """


class ReplicationTaskStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped.wait)
        """


class TestConnectionSucceedsWaiter(Boto3Waiter):
    """
    [Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TestConnectionSucceeds.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds.wait)
        """
