"""
Type annotations for appconfig service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appconfig.client import AppConfigClient
    from mypy_boto3_appconfig.waiter import (
        DeploymentCompleteWaiter,
        EnvironmentReadyForDeploymentWaiter,
    )

    session = Session()
    client: AppConfigClient = session.client("appconfig")

    deployment_complete_waiter: DeploymentCompleteWaiter = client.get_waiter("deployment_complete")
    environment_ready_for_deployment_waiter: EnvironmentReadyForDeploymentWaiter = client.get_waiter("environment_ready_for_deployment")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetDeploymentRequestWaitTypeDef, GetEnvironmentRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DeploymentCompleteWaiter", "EnvironmentReadyForDeploymentWaiter")

class DeploymentCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/waiter/DeploymentComplete.html#AppConfig.Waiter.DeploymentComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/waiters/#deploymentcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetDeploymentRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/waiter/DeploymentComplete.html#AppConfig.Waiter.DeploymentComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/waiters/#deploymentcompletewaiter)
        """

class EnvironmentReadyForDeploymentWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/waiter/EnvironmentReadyForDeployment.html#AppConfig.Waiter.EnvironmentReadyForDeployment)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/waiters/#environmentreadyfordeploymentwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetEnvironmentRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/waiter/EnvironmentReadyForDeployment.html#AppConfig.Waiter.EnvironmentReadyForDeployment.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/waiters/#environmentreadyfordeploymentwaiter)
        """
