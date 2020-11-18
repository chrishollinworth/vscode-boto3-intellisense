# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for elasticbeanstalk service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_elasticbeanstalk import ElasticBeanstalkClient
    from mypy_boto3_elasticbeanstalk.waiter import (
        EnvironmentExistsWaiter,
        EnvironmentTerminatedWaiter,
        EnvironmentUpdatedWaiter,
    )

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")

    environment_exists_waiter: EnvironmentExistsWaiter = client.get_waiter("environment_exists")
    environment_terminated_waiter: EnvironmentTerminatedWaiter = client.get_waiter("environment_terminated")
    environment_updated_waiter: EnvironmentUpdatedWaiter = client.get_waiter("environment_updated")
    ```
"""
from datetime import datetime
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_elasticbeanstalk.type_defs import WaiterConfigTypeDef

__all__ = ("EnvironmentExistsWaiter", "EnvironmentTerminatedWaiter", "EnvironmentUpdatedWaiter")


class EnvironmentExistsWaiter(Boto3Waiter):
    """
    [Waiter.EnvironmentExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists)
    """

    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EnvironmentExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists.wait)
        """


class EnvironmentTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.EnvironmentTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated)
    """

    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EnvironmentTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated.wait)
        """


class EnvironmentUpdatedWaiter(Boto3Waiter):
    """
    [Waiter.EnvironmentUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated)
    """

    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EnvironmentUpdated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated.wait)
        """
