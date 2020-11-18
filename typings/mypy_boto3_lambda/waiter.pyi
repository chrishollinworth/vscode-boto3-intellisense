# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for lambda service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_lambda.waiter import (
        FunctionActiveWaiter,
        FunctionExistsWaiter,
        FunctionUpdatedWaiter,
    )

    client: LambdaClient = boto3.client("lambda")

    function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
    function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
    function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_lambda.type_defs import WaiterConfigTypeDef

__all__ = ("FunctionActiveWaiter", "FunctionExistsWaiter", "FunctionUpdatedWaiter")


class FunctionActiveWaiter(Boto3Waiter):
    """
    [Waiter.FunctionActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
    """

    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionActive.wait)
        """


class FunctionExistsWaiter(Boto3Waiter):
    """
    [Waiter.FunctionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
    """

    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionExists.wait)
        """


class FunctionUpdatedWaiter(Boto3Waiter):
    """
    [Waiter.FunctionUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
    """

    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionUpdated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated.wait)
        """
