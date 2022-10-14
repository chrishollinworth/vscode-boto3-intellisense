"""
Type annotations for codedeploy service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_codedeploy import CodeDeployClient
    from mypy_boto3_codedeploy.waiter import (
        DeploymentSuccessfulWaiter,
    )

    client: CodeDeployClient = boto3.client("codedeploy")

    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("DeploymentSuccessfulWaiter",)

class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/waiters.html#deploymentsuccessfulwaiter)
    """

    def wait(self, *, deploymentId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/waiters.html#deploymentsuccessfulwaiter)
        """
