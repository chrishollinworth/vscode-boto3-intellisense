"""
Type annotations for neptune service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_neptune.client import NeptuneClient
    from mypy_boto3_neptune.waiter import (
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
    )

    session = Session()
    client: NeptuneClient = session.client("neptune")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeDBInstancesMessageWaitExtraTypeDef,
    DescribeDBInstancesMessageWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")

class DBInstanceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceAvailable.html#Neptune.Waiter.DBInstanceAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters/#dbinstanceavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceAvailable.html#Neptune.Waiter.DBInstanceAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters/#dbinstanceavailablewaiter)
        """

class DBInstanceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceDeleted.html#Neptune.Waiter.DBInstanceDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters/#dbinstancedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceDeleted.html#Neptune.Waiter.DBInstanceDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters/#dbinstancedeletedwaiter)
        """
