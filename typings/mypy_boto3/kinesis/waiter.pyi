"""
Type annotations for kinesis service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html)

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

from .type_defs import WaiterConfigTypeDef

__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")

class StreamExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamexistswaiter)
    """

    def wait(
        self,
        *,
        StreamName: str = None,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        StreamARN: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis.html#Kinesis.Waiter.StreamExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamexistswaiter)
        """

class StreamNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamnotexistswaiter)
    """

    def wait(
        self,
        *,
        StreamName: str = None,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        StreamARN: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamnotexistswaiter)
        """
