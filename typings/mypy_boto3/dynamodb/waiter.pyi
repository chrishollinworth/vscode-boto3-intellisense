"""
Type annotations for dynamodb service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_dynamodb import DynamoDBClient
    from mypy_boto3_dynamodb.waiter import (
        TableExistsWaiter,
        TableNotExistsWaiter,
    )

    client: DynamoDBClient = boto3.client("dynamodb")

    table_exists_waiter: TableExistsWaiter = client.get_waiter("table_exists")
    table_not_exists_waiter: TableNotExistsWaiter = client.get_waiter("table_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("TableExistsWaiter", "TableNotExistsWaiter")

class TableExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tableexistswaiter)
    """

    def wait(self, *, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tableexistswaiter)
        """

class TableNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tablenotexistswaiter)
    """

    def wait(self, *, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tablenotexistswaiter)
        """
