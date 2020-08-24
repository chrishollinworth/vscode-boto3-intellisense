"""
Main interface for cloud9 service type definitions.

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import EnvironmentLifecycleTypeDef

    data: EnvironmentLifecycleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "TagTypeDef",
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
)

EnvironmentLifecycleTypeDef = TypedDict(
    "EnvironmentLifecycleTypeDef",
    {
        "status": Literal["CREATING", "CREATED", "CREATE_FAILED", "DELETING", "DELETE_FAILED"],
        "reason": str,
        "failureResource": str,
    },
    total=False,
)

EnvironmentMemberTypeDef = TypedDict(
    "EnvironmentMemberTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "type": Literal["ssh", "ec2"],
        "connectionType": Literal["CONNECT_SSH", "CONNECT_SSM"],
        "arn": str,
        "ownerArn": str,
        "lifecycle": "EnvironmentLifecycleTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateEnvironmentEC2ResultTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultTypeDef", {"environmentId": str}, total=False
)

CreateEnvironmentMembershipResultTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultTypeDef",
    {"membership": "EnvironmentMemberTypeDef"},
    total=False,
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {"memberships": List["EnvironmentMemberTypeDef"], "nextToken": str},
    total=False,
)

DescribeEnvironmentStatusResultTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultTypeDef",
    {
        "status": Literal[
            "error", "creating", "connecting", "ready", "stopping", "stopped", "deleting"
        ],
        "message": str,
    },
    total=False,
)

DescribeEnvironmentsResultTypeDef = TypedDict(
    "DescribeEnvironmentsResultTypeDef", {"environments": List["EnvironmentTypeDef"]}, total=False
)

ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef", {"nextToken": str, "environmentIds": List[str]}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateEnvironmentMembershipResultTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultTypeDef",
    {"membership": "EnvironmentMemberTypeDef"},
    total=False,
)
