"""
Type annotations for cloudwatch service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudwatch.client import CloudWatchClient
    from mypy_boto3_cloudwatch.waiter import (
        AlarmExistsWaiter,
        CompositeAlarmExistsWaiter,
    )

    session = Session()
    client: CloudWatchClient = session.client("cloudwatch")

    alarm_exists_waiter: AlarmExistsWaiter = client.get_waiter("alarm_exists")
    composite_alarm_exists_waiter: CompositeAlarmExistsWaiter = client.get_waiter("composite_alarm_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeAlarmsInputWaitExtraTypeDef, DescribeAlarmsInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("AlarmExistsWaiter", "CompositeAlarmExistsWaiter")

class AlarmExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/waiter/AlarmExists.html#CloudWatch.Waiter.AlarmExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters/#alarmexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAlarmsInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/waiter/AlarmExists.html#CloudWatch.Waiter.AlarmExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters/#alarmexistswaiter)
        """

class CompositeAlarmExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/waiter/CompositeAlarmExists.html#CloudWatch.Waiter.CompositeAlarmExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters/#compositealarmexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAlarmsInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/waiter/CompositeAlarmExists.html#CloudWatch.Waiter.CompositeAlarmExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters/#compositealarmexistswaiter)
        """
