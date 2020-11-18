# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for rekognition service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_rekognition import RekognitionClient
    from mypy_boto3_rekognition.waiter import (
        ProjectVersionRunningWaiter,
        ProjectVersionTrainingCompletedWaiter,
    )

    client: RekognitionClient = boto3.client("rekognition")

    project_version_running_waiter: ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
    project_version_training_completed_waiter: ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_rekognition.type_defs import WaiterConfigTypeDef

__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")


class ProjectVersionRunningWaiter(Boto3Waiter):
    """
    [Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
    """

    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ProjectVersionRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning.wait)
        """


class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    """
    [Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
    """

    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ProjectVersionTrainingCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted.wait)
        """
