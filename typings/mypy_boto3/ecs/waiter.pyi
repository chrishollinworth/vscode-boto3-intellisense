"""
Type annotations for ecs service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ecs import ECSClient
    from mypy_boto3_ecs.waiter import (
        ServicesInactiveWaiter,
        ServicesStableWaiter,
        TasksRunningWaiter,
        TasksStoppedWaiter,
    )

    client: ECSClient = boto3.client("ecs")

    services_inactive_waiter: ServicesInactiveWaiter = client.get_waiter("services_inactive")
    services_stable_waiter: ServicesStableWaiter = client.get_waiter("services_stable")
    tasks_running_waiter: TasksRunningWaiter = client.get_waiter("tasks_running")
    tasks_stopped_waiter: TasksStoppedWaiter = client.get_waiter("tasks_stopped")
    ```
"""
import sys
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ServicesInactiveWaiter",
    "ServicesStableWaiter",
    "TasksRunningWaiter",
    "TasksStoppedWaiter",
)

class ServicesInactiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.ServicesInactive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesinactivewaiter)
    """

    def wait(
        self,
        *,
        services: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.ServicesInactive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesinactivewaiter)
        """

class ServicesStableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.ServicesStable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesstablewaiter)
    """

    def wait(
        self,
        *,
        services: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.ServicesStable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesstablewaiter)
        """

class TasksRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.TasksRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksrunningwaiter)
    """

    def wait(
        self,
        *,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.TasksRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksrunningwaiter)
        """

class TasksStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.TasksStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksstoppedwaiter)
    """

    def wait(
        self,
        *,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/ecs.html#ECS.Waiter.TasksStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksstoppedwaiter)
        """
