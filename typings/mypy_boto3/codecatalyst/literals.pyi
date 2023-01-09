"""
Type annotations for codecatalyst service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/literals.html)

Usage::

    ```python
    from mypy_boto3_codecatalyst.literals import ComparisonOperatorType

    data: ComparisonOperatorType = "EQ"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ComparisonOperatorType",
    "DevEnvironmentSessionTypeType",
    "DevEnvironmentStatusType",
    "FilterKeyType",
    "InstanceTypeType",
    "ListAccessTokensPaginatorName",
    "ListDevEnvironmentsPaginatorName",
    "ListEventLogsPaginatorName",
    "ListProjectsPaginatorName",
    "ListSourceRepositoriesPaginatorName",
    "ListSourceRepositoryBranchesPaginatorName",
    "ListSpacesPaginatorName",
    "OperationTypeType",
    "UserTypeType",
)

ComparisonOperatorType = Literal["EQ", "GE", "GT", "LE", "LT"]
DevEnvironmentSessionTypeType = Literal["SSH", "SSM"]
DevEnvironmentStatusType = Literal[
    "DELETED", "DELETING", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPED", "STOPPING"
]
FilterKeyType = Literal["hasAccessTo"]
InstanceTypeType = Literal[
    "dev.standard1.large", "dev.standard1.medium", "dev.standard1.small", "dev.standard1.xlarge"
]
ListAccessTokensPaginatorName = Literal["list_access_tokens"]
ListDevEnvironmentsPaginatorName = Literal["list_dev_environments"]
ListEventLogsPaginatorName = Literal["list_event_logs"]
ListProjectsPaginatorName = Literal["list_projects"]
ListSourceRepositoriesPaginatorName = Literal["list_source_repositories"]
ListSourceRepositoryBranchesPaginatorName = Literal["list_source_repository_branches"]
ListSpacesPaginatorName = Literal["list_spaces"]
OperationTypeType = Literal["MUTATION", "READONLY"]
UserTypeType = Literal["AWS_ACCOUNT", "UNKNOWN", "USER"]
