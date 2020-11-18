# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for ssm service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm import SSMClient
    from mypy_boto3_ssm.waiter import (
        CommandExecutedWaiter,
    )

    client: SSMClient = boto3.client("ssm")

    command_executed_waiter: CommandExecutedWaiter = client.get_waiter("command_executed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_ssm.type_defs import WaiterConfigTypeDef

__all__ = ("CommandExecutedWaiter",)


class CommandExecutedWaiter(Boto3Waiter):
    """
    [Waiter.CommandExecuted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Waiter.CommandExecuted)
    """

    def wait(
        self,
        CommandId: str,
        InstanceId: str,
        PluginName: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CommandExecuted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Waiter.CommandExecuted.wait)
        """
