"""
Type annotations for opsworks service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_opsworks.client import OpsWorksClient
    from mypy_boto3_opsworks.waiter import (
        AppExistsWaiter,
        DeploymentSuccessfulWaiter,
        InstanceOnlineWaiter,
        InstanceRegisteredWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
    )

    session = Session()
    client: OpsWorksClient = session.client("opsworks")

    app_exists_waiter: AppExistsWaiter = client.get_waiter("app_exists")
    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
    instance_online_waiter: InstanceOnlineWaiter = client.get_waiter("instance_online")
    instance_registered_waiter: InstanceRegisteredWaiter = client.get_waiter("instance_registered")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeAppsRequestWaitTypeDef,
    DescribeDeploymentsRequestWaitTypeDef,
    DescribeInstancesRequestWaitExtraExtraExtraTypeDef,
    DescribeInstancesRequestWaitExtraExtraTypeDef,
    DescribeInstancesRequestWaitExtraTypeDef,
    DescribeInstancesRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)

class AppExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/AppExists.html#OpsWorks.Waiter.AppExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#appexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAppsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/AppExists.html#OpsWorks.Waiter.AppExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#appexistswaiter)
        """

class DeploymentSuccessfulWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/DeploymentSuccessful.html#OpsWorks.Waiter.DeploymentSuccessful)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#deploymentsuccessfulwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDeploymentsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/DeploymentSuccessful.html#OpsWorks.Waiter.DeploymentSuccessful.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#deploymentsuccessfulwaiter)
        """

class InstanceOnlineWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceOnline.html#OpsWorks.Waiter.InstanceOnline)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceonlinewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceOnline.html#OpsWorks.Waiter.InstanceOnline.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceonlinewaiter)
        """

class InstanceRegisteredWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceRegistered.html#OpsWorks.Waiter.InstanceRegistered)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceregisteredwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceRegistered.html#OpsWorks.Waiter.InstanceRegistered.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceregisteredwaiter)
        """

class InstanceStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceStopped.html#OpsWorks.Waiter.InstanceStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instancestoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceStopped.html#OpsWorks.Waiter.InstanceStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instancestoppedwaiter)
        """

class InstanceTerminatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceTerminated.html#OpsWorks.Waiter.InstanceTerminated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceterminatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks/waiter/InstanceTerminated.html#OpsWorks.Waiter.InstanceTerminated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters/#instanceterminatedwaiter)
        """
