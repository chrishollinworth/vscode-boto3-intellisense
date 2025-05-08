"""
Type annotations for ssm service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm.client import SSMClient
    from mypy_boto3_ssm.waiter import (
        CommandExecutedWaiter,
    )

    session = Session()
    client: SSMClient = session.client("ssm")

    command_executed_waiter: CommandExecutedWaiter = client.get_waiter("command_executed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetCommandInvocationRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CommandExecutedWaiter",)

class CommandExecutedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/waiter/CommandExecuted.html#SSM.Waiter.CommandExecuted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/waiters/#commandexecutedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetCommandInvocationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/waiter/CommandExecuted.html#SSM.Waiter.CommandExecuted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/waiters/#commandexecutedwaiter)
        """
