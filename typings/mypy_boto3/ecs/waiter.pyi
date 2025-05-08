"""
Type annotations for ecs service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ecs.client import ECSClient
    from mypy_boto3_ecs.waiter import (
        ServicesInactiveWaiter,
        ServicesStableWaiter,
        TasksRunningWaiter,
        TasksStoppedWaiter,
    )

    session = Session()
    client: ECSClient = session.client("ecs")

    services_inactive_waiter: ServicesInactiveWaiter = client.get_waiter("services_inactive")
    services_stable_waiter: ServicesStableWaiter = client.get_waiter("services_stable")
    tasks_running_waiter: TasksRunningWaiter = client.get_waiter("tasks_running")
    tasks_stopped_waiter: TasksStoppedWaiter = client.get_waiter("tasks_stopped")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeServicesRequestWaitExtraTypeDef,
    DescribeServicesRequestWaitTypeDef,
    DescribeTasksRequestWaitExtraTypeDef,
    DescribeTasksRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ServicesInactiveWaiter",
    "ServicesStableWaiter",
    "TasksRunningWaiter",
    "TasksStoppedWaiter",
)

class ServicesInactiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/ServicesInactive.html#ECS.Waiter.ServicesInactive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#servicesinactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServicesRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/ServicesInactive.html#ECS.Waiter.ServicesInactive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#servicesinactivewaiter)
        """

class ServicesStableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/ServicesStable.html#ECS.Waiter.ServicesStable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#servicesstablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServicesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/ServicesStable.html#ECS.Waiter.ServicesStable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#servicesstablewaiter)
        """

class TasksRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/TasksRunning.html#ECS.Waiter.TasksRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#tasksrunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTasksRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/TasksRunning.html#ECS.Waiter.TasksRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#tasksrunningwaiter)
        """

class TasksStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/TasksStopped.html#ECS.Waiter.TasksStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#tasksstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTasksRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/waiter/TasksStopped.html#ECS.Waiter.TasksStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters/#tasksstoppedwaiter)
        """
