# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for iam service client waiters.

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

from mypy_boto3_iam.type_defs import WaiterConfigTypeDef

__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)


class InstanceProfileExistsWaiter(Boto3Waiter):
    """
    [Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)
    """

    def wait(self, InstanceProfileName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InstanceProfileExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.InstanceProfileExists.wait)
        """


class PolicyExistsWaiter(Boto3Waiter):
    """
    [Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.PolicyExists)
    """

    def wait(self, PolicyArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [PolicyExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.PolicyExists.wait)
        """


class RoleExistsWaiter(Boto3Waiter):
    """
    [Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.RoleExists)
    """

    def wait(self, RoleName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [RoleExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.RoleExists.wait)
        """


class UserExistsWaiter(Boto3Waiter):
    """
    [Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.UserExists)
    """

    def wait(self, UserName: str = None, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [UserExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Waiter.UserExists.wait)
        """
