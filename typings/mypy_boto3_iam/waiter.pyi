"""
Type annotations for iam service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iam.client import IAMClient
    from mypy_boto3_iam.waiter import (
        InstanceProfileExistsWaiter,
        PolicyExistsWaiter,
        RoleExistsWaiter,
        UserExistsWaiter,
    )

    session = Session()
    client: IAMClient = session.client("iam")

    instance_profile_exists_waiter: InstanceProfileExistsWaiter = client.get_waiter("instance_profile_exists")
    policy_exists_waiter: PolicyExistsWaiter = client.get_waiter("policy_exists")
    role_exists_waiter: RoleExistsWaiter = client.get_waiter("role_exists")
    user_exists_waiter: UserExistsWaiter = client.get_waiter("user_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetInstanceProfileRequestWaitTypeDef,
    GetPolicyRequestWaitTypeDef,
    GetRoleRequestWaitTypeDef,
    GetUserRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)

class InstanceProfileExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/InstanceProfileExists.html#IAM.Waiter.InstanceProfileExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#instanceprofileexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetInstanceProfileRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/InstanceProfileExists.html#IAM.Waiter.InstanceProfileExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#instanceprofileexistswaiter)
        """

class PolicyExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/PolicyExists.html#IAM.Waiter.PolicyExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#policyexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/PolicyExists.html#IAM.Waiter.PolicyExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#policyexistswaiter)
        """

class RoleExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/RoleExists.html#IAM.Waiter.RoleExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#roleexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRoleRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/RoleExists.html#IAM.Waiter.RoleExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#roleexistswaiter)
        """

class UserExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/UserExists.html#IAM.Waiter.UserExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#userexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetUserRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/waiter/UserExists.html#IAM.Waiter.UserExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters/#userexistswaiter)
        """
