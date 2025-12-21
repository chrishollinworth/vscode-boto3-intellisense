"""
Type annotations for lambda service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lambda.client import LambdaClient
    from mypy_boto3_lambda.waiter import (
        FunctionActiveV2Waiter,
        FunctionActiveWaiter,
        FunctionExistsWaiter,
        FunctionUpdatedV2Waiter,
        FunctionUpdatedWaiter,
        PublishedVersionActiveWaiter,
    )

    session = Session()
    client: LambdaClient = session.client("lambda")

    function_active_v2_waiter: FunctionActiveV2Waiter = client.get_waiter("function_active_v2")
    function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
    function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
    function_updated_v2_waiter: FunctionUpdatedV2Waiter = client.get_waiter("function_updated_v2")
    function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")
    published_version_active_waiter: PublishedVersionActiveWaiter = client.get_waiter("published_version_active")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetFunctionConfigurationRequestWaitExtraExtraTypeDef,
    GetFunctionConfigurationRequestWaitExtraTypeDef,
    GetFunctionConfigurationRequestWaitTypeDef,
    GetFunctionRequestWaitExtraExtraTypeDef,
    GetFunctionRequestWaitExtraTypeDef,
    GetFunctionRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "FunctionActiveV2Waiter",
    "FunctionActiveWaiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedV2Waiter",
    "FunctionUpdatedWaiter",
    "PublishedVersionActiveWaiter",
)

class FunctionActiveV2Waiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionActiveV2.html#Lambda.Waiter.FunctionActiveV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionactivev2waiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionActiveV2.html#Lambda.Waiter.FunctionActiveV2.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionactivev2waiter)
        """

class FunctionActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionActive.html#Lambda.Waiter.FunctionActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionConfigurationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionActive.html#Lambda.Waiter.FunctionActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionactivewaiter)
        """

class FunctionExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionExists.html#Lambda.Waiter.FunctionExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionExists.html#Lambda.Waiter.FunctionExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionexistswaiter)
        """

class FunctionUpdatedV2Waiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionUpdatedV2.html#Lambda.Waiter.FunctionUpdatedV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionupdatedv2waiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionUpdatedV2.html#Lambda.Waiter.FunctionUpdatedV2.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionupdatedv2waiter)
        """

class FunctionUpdatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionUpdated.html#Lambda.Waiter.FunctionUpdated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionupdatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionConfigurationRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/FunctionUpdated.html#Lambda.Waiter.FunctionUpdated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#functionupdatedwaiter)
        """

class PublishedVersionActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/PublishedVersionActive.html#Lambda.Waiter.PublishedVersionActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#publishedversionactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetFunctionConfigurationRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/waiter/PublishedVersionActive.html#Lambda.Waiter.PublishedVersionActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters/#publishedversionactivewaiter)
        """
