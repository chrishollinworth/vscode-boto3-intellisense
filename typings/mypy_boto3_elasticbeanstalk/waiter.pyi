"""
Type annotations for elasticbeanstalk service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html)

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
from typing import List, Union

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("EnvironmentExistsWaiter", "EnvironmentTerminatedWaiter", "EnvironmentUpdatedWaiter")

class EnvironmentExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentexistswaiter)
    """

    def wait(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: Union[datetime, str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentexistswaiter)
        """

class EnvironmentTerminatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentterminatedwaiter)
    """

    def wait(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: Union[datetime, str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentterminatedwaiter)
        """

class EnvironmentUpdatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentupdatedwaiter)
    """

    def wait(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: Union[datetime, str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentupdatedwaiter)
        """
