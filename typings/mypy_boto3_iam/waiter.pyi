"""
Type annotations for iam service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMClient
    from mypy_boto3_iam.waiter import (
        InstanceProfileExistsWaiter,
        PolicyExistsWaiter,
        RoleExistsWaiter,
        UserExistsWaiter,
    )

    client: IAMClient = boto3.client("iam")

    instance_profile_exists_waiter: InstanceProfileExistsWaiter = client.get_waiter("instance_profile_exists")
    policy_exists_waiter: PolicyExistsWaiter = client.get_waiter("policy_exists")
    role_exists_waiter: RoleExistsWaiter = client.get_waiter("role_exists")
    user_exists_waiter: UserExistsWaiter = client.get_waiter("user_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)

class InstanceProfileExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#instanceprofileexistswaiter)
    """

    def wait(self, *, InstanceProfileName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.InstanceProfileExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#instanceprofileexistswaiter)
        """

class PolicyExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.PolicyExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#policyexistswaiter)
    """

    def wait(self, *, PolicyArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.PolicyExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#policyexistswaiter)
        """

class RoleExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.RoleExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#roleexistswaiter)
    """

    def wait(self, *, RoleName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.RoleExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#roleexistswaiter)
        """

class UserExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.UserExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#userexistswaiter)
    """

    def wait(self, *, UserName: str = None, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iam.html#IAM.Waiter.UserExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#userexistswaiter)
        """
