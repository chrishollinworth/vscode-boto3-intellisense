"""
Type annotations for dms service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dms.client import DatabaseMigrationServiceClient
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

    session = Session()
    client: DatabaseMigrationServiceClient = session.client("dms")

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

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeConnectionsMessageWaitTypeDef,
    DescribeEndpointsMessageWaitTypeDef,
    DescribeReplicationInstancesMessageWaitExtraTypeDef,
    DescribeReplicationInstancesMessageWaitTypeDef,
    DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef,
    DescribeReplicationTasksMessageWaitExtraExtraTypeDef,
    DescribeReplicationTasksMessageWaitExtraTypeDef,
    DescribeReplicationTasksMessageWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

class EndpointDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/EndpointDeleted.html#DatabaseMigrationService.Waiter.EndpointDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#endpointdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/EndpointDeleted.html#DatabaseMigrationService.Waiter.EndpointDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#endpointdeletedwaiter)
        """

class ReplicationInstanceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationInstanceAvailable.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationinstanceavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationInstancesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationInstanceAvailable.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationinstanceavailablewaiter)
        """

class ReplicationInstanceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationInstanceDeleted.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationinstancedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationInstancesMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationInstanceDeleted.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationinstancedeletedwaiter)
        """

class ReplicationTaskDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskDeleted.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskDeleted.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskdeletedwaiter)
        """

class ReplicationTaskReadyWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskReady.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskreadywaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTasksMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskReady.html#DatabaseMigrationService.Waiter.ReplicationTaskReady.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskreadywaiter)
        """

class ReplicationTaskRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskRunning.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskrunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTasksMessageWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskRunning.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskrunningwaiter)
        """

class ReplicationTaskStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskStopped.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTasksMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/ReplicationTaskStopped.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#replicationtaskstoppedwaiter)
        """

class TestConnectionSucceedsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/TestConnectionSucceeds.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#testconnectionsucceedswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConnectionsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/waiter/TestConnectionSucceeds.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters/#testconnectionsucceedswaiter)
        """
