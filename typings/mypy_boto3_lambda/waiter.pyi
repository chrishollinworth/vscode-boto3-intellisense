"""
Type annotations for lambda service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_lambda.waiter import (
        FunctionActiveWaiter,
        FunctionActiveV2Waiter,
        FunctionExistsWaiter,
        FunctionUpdatedWaiter,
        FunctionUpdatedV2Waiter,
    )

    client: LambdaClient = boto3.client("lambda")

    function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
    function_active_v2_waiter: FunctionActiveV2Waiter = client.get_waiter("function_active_v2")
    function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
    function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")
    function_updated_v2_waiter: FunctionUpdatedV2Waiter = client.get_waiter("function_updated_v2")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "FunctionActiveWaiter",
    "FunctionActiveV2Waiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedWaiter",
    "FunctionUpdatedV2Waiter",
)

class FunctionActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivewaiter)
    """

    def wait(
        self, *, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivewaiter)
        """

class FunctionActiveV2Waiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionActiveV2)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivev2waiter)
    """

    def wait(
        self, *, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionActiveV2.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivev2waiter)
        """

class FunctionExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionexistswaiter)
    """

    def wait(
        self, *, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionexistswaiter)
        """

class FunctionUpdatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedwaiter)
    """

    def wait(
        self, *, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedwaiter)
        """

class FunctionUpdatedV2Waiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionUpdatedV2)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedv2waiter)
    """

    def wait(
        self, *, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/lambda.html#Lambda.Waiter.FunctionUpdatedV2.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedv2waiter)
        """
