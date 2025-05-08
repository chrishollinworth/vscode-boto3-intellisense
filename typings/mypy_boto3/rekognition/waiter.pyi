"""
Type annotations for rekognition service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rekognition.client import RekognitionClient
    from mypy_boto3_rekognition.waiter import (
        ProjectVersionRunningWaiter,
        ProjectVersionTrainingCompletedWaiter,
    )

    session = Session()
    client: RekognitionClient = session.client("rekognition")

    project_version_running_waiter: ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
    project_version_training_completed_waiter: ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeProjectVersionsRequestWaitExtraTypeDef,
    DescribeProjectVersionsRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")

class ProjectVersionRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/waiter/ProjectVersionRunning.html#Rekognition.Waiter.ProjectVersionRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters/#projectversionrunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeProjectVersionsRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/waiter/ProjectVersionRunning.html#Rekognition.Waiter.ProjectVersionRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters/#projectversionrunningwaiter)
        """

class ProjectVersionTrainingCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/waiter/ProjectVersionTrainingCompleted.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters/#projectversiontrainingcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeProjectVersionsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/waiter/ProjectVersionTrainingCompleted.html#Rekognition.Waiter.ProjectVersionTrainingCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters/#projectversiontrainingcompletedwaiter)
        """
