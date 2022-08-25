"""
Type annotations for amp service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amp import PrometheusServiceClient
    from mypy_boto3_amp.waiter import (
        WorkspaceActiveWaiter,
        WorkspaceDeletedWaiter,
    )

    client: PrometheusServiceClient = boto3.client("amp")

    workspace_active_waiter: WorkspaceActiveWaiter = client.get_waiter("workspace_active")
    workspace_deleted_waiter: WorkspaceDeletedWaiter = client.get_waiter("workspace_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("WorkspaceActiveWaiter", "WorkspaceDeletedWaiter")

class WorkspaceActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/amp.html#PrometheusService.Waiter.WorkspaceActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspaceactivewaiter)
    """

    def wait(self, *, workspaceId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/amp.html#PrometheusService.Waiter.WorkspaceActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspaceactivewaiter)
        """

class WorkspaceDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/amp.html#PrometheusService.Waiter.WorkspaceDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspacedeletedwaiter)
    """

    def wait(self, *, workspaceId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/amp.html#PrometheusService.Waiter.WorkspaceDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspacedeletedwaiter)
        """
