# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for docdb service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_docdb import DocDBClient
    from mypy_boto3_docdb.waiter import (
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
    )

    client: DocDBClient = boto3.client("docdb")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_docdb.type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
    """

    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable.wait)
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
    """

    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted.wait)
        """
