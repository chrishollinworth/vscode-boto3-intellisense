"""
Type annotations for rekognition service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html)

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

from .type_defs import WaiterConfigTypeDef

__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")

class ProjectVersionRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversionrunningwaiter)
    """

    def wait(
        self,
        *,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversionrunningwaiter)
        """

class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversiontrainingcompletedwaiter)
    """

    def wait(
        self,
        *,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversiontrainingcompletedwaiter)
        """
