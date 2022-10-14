"""
Type annotations for neptune service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_neptune import NeptuneClient
    from mypy_boto3_neptune.waiter import (
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
    )

    client: NeptuneClient = boto3.client("neptune")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")

class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/neptune.html#Neptune.Waiter.DBInstanceAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters.html#dbinstanceavailablewaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/neptune.html#Neptune.Waiter.DBInstanceAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters.html#dbinstanceavailablewaiter)
        """

class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/neptune.html#Neptune.Waiter.DBInstanceDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters.html#dbinstancedeletedwaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/neptune.html#Neptune.Waiter.DBInstanceDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/waiters.html#dbinstancedeletedwaiter)
        """
