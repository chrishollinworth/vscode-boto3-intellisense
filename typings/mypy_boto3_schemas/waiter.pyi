"""
Type annotations for schemas service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_schemas.client import SchemasClient
    from mypy_boto3_schemas.waiter import (
        CodeBindingExistsWaiter,
    )

    session = Session()
    client: SchemasClient = session.client("schemas")

    code_binding_exists_waiter: CodeBindingExistsWaiter = client.get_waiter("code_binding_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeCodeBindingRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CodeBindingExistsWaiter",)

class CodeBindingExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/waiter/CodeBindingExists.html#Schemas.Waiter.CodeBindingExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/waiters/#codebindingexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCodeBindingRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas/waiter/CodeBindingExists.html#Schemas.Waiter.CodeBindingExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/waiters/#codebindingexistswaiter)
        """
