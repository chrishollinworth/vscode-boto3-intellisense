"""
Type annotations for cloud9 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/literals.html)

Usage::

    ```python
    from mypy_boto3_cloud9.literals import ConnectionTypeType

    data: ConnectionTypeType = "CONNECT_SSH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConnectionTypeType",
    "DescribeEnvironmentMembershipsPaginatorName",
    "EnvironmentLifecycleStatusType",
    "EnvironmentStatusType",
    "EnvironmentTypeType",
    "ListEnvironmentsPaginatorName",
    "ManagedCredentialsStatusType",
    "MemberPermissionsType",
    "PermissionsType",
)

ConnectionTypeType = Literal["CONNECT_SSH", "CONNECT_SSM"]
DescribeEnvironmentMembershipsPaginatorName = Literal["describe_environment_memberships"]
EnvironmentLifecycleStatusType = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
]
EnvironmentStatusType = Literal[
    "connecting", "creating", "deleting", "error", "ready", "stopped", "stopping"
]
EnvironmentTypeType = Literal["ec2", "ssh"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ManagedCredentialsStatusType = Literal[
    "DISABLED_BY_COLLABORATOR",
    "DISABLED_BY_DEFAULT",
    "DISABLED_BY_OWNER",
    "ENABLED_BY_OWNER",
    "ENABLED_ON_CREATE",
    "FAILED_REMOVAL_BY_COLLABORATOR",
    "FAILED_REMOVAL_BY_OWNER",
    "PENDING_REMOVAL_BY_COLLABORATOR",
    "PENDING_REMOVAL_BY_OWNER",
    "PENDING_START_REMOVAL_BY_COLLABORATOR",
    "PENDING_START_REMOVAL_BY_OWNER",
]
MemberPermissionsType = Literal["read-only", "read-write"]
PermissionsType = Literal["owner", "read-only", "read-write"]
