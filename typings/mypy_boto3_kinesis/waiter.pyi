# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for kinesis service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesis import KinesisClient
    from mypy_boto3_kinesis.waiter import (
        StreamExistsWaiter,
        StreamNotExistsWaiter,
    )

    client: KinesisClient = boto3.client("kinesis")

    stream_exists_waiter: StreamExistsWaiter = client.get_waiter("stream_exists")
    stream_not_exists_waiter: StreamNotExistsWaiter = client.get_waiter("stream_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_kinesis.type_defs import WaiterConfigTypeDef

__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")


class StreamExistsWaiter(Boto3Waiter):
    """
    [Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
    """

    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [StreamExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamExists.wait)
        """


class StreamNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
    """

    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [StreamNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists.wait)
        """
