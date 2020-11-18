# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for opsworks service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworks import OpsWorksClient
    from mypy_boto3_opsworks.waiter import (
        AppExistsWaiter,
        DeploymentSuccessfulWaiter,
        InstanceOnlineWaiter,
        InstanceRegisteredWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
    )

    client: OpsWorksClient = boto3.client("opsworks")

    app_exists_waiter: AppExistsWaiter = client.get_waiter("app_exists")
    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
    instance_online_waiter: InstanceOnlineWaiter = client.get_waiter("instance_online")
    instance_registered_waiter: InstanceRegisteredWaiter = client.get_waiter("instance_registered")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_opsworks.type_defs import WaiterConfigTypeDef

__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)


class AppExistsWaiter(Boto3Waiter):
    """
    [Waiter.AppExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.AppExists)
    """

    def wait(
        self,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AppExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.AppExists.wait)
        """


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful)
    """

    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DeploymentSuccessful.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful.wait)
        """


class InstanceOnlineWaiter(Boto3Waiter):
    """
    [Waiter.InstanceOnline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline)
    """

    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceOnline.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline.wait)
        """


class InstanceRegisteredWaiter(Boto3Waiter):
    """
    [Waiter.InstanceRegistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered)
    """

    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceRegistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered.wait)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped)
    """

    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped.wait)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated)
    """

    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated.wait)
        """
