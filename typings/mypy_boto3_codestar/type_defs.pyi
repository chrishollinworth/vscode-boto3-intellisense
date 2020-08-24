"""
Main interface for codestar service type definitions.

Usage::

    ```python
    from mypy_boto3_codestar.type_defs import CodeCommitCodeDestinationTypeDef

    data: CodeCommitCodeDestinationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CodeCommitCodeDestinationTypeDef",
    "CodeDestinationTypeDef",
    "CodeSourceTypeDef",
    "GitHubCodeDestinationTypeDef",
    "ProjectStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "S3LocationTypeDef",
    "TeamMemberTypeDef",
    "ToolchainSourceTypeDef",
    "UserProfileSummaryTypeDef",
    "AssociateTeamMemberResultTypeDef",
    "CodeTypeDef",
    "CreateProjectResultTypeDef",
    "CreateUserProfileResultTypeDef",
    "DeleteProjectResultTypeDef",
    "DeleteUserProfileResultTypeDef",
    "DescribeProjectResultTypeDef",
    "DescribeUserProfileResultTypeDef",
    "ListProjectsResultTypeDef",
    "ListResourcesResultTypeDef",
    "ListTagsForProjectResultTypeDef",
    "ListTeamMembersResultTypeDef",
    "ListUserProfilesResultTypeDef",
    "PaginatorConfigTypeDef",
    "TagProjectResultTypeDef",
    "ToolchainTypeDef",
    "UpdateTeamMemberResultTypeDef",
    "UpdateUserProfileResultTypeDef",
)

CodeCommitCodeDestinationTypeDef = TypedDict("CodeCommitCodeDestinationTypeDef", {"name": str})

CodeDestinationTypeDef = TypedDict(
    "CodeDestinationTypeDef",
    {"codeCommit": "CodeCommitCodeDestinationTypeDef", "gitHub": "GitHubCodeDestinationTypeDef"},
    total=False,
)

CodeSourceTypeDef = TypedDict("CodeSourceTypeDef", {"s3": "S3LocationTypeDef"})

_RequiredGitHubCodeDestinationTypeDef = TypedDict(
    "_RequiredGitHubCodeDestinationTypeDef",
    {
        "name": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
    },
)
_OptionalGitHubCodeDestinationTypeDef = TypedDict(
    "_OptionalGitHubCodeDestinationTypeDef", {"description": str}, total=False
)


class GitHubCodeDestinationTypeDef(
    _RequiredGitHubCodeDestinationTypeDef, _OptionalGitHubCodeDestinationTypeDef
):
    pass


_RequiredProjectStatusTypeDef = TypedDict("_RequiredProjectStatusTypeDef", {"state": str})
_OptionalProjectStatusTypeDef = TypedDict(
    "_OptionalProjectStatusTypeDef", {"reason": str}, total=False
)


class ProjectStatusTypeDef(_RequiredProjectStatusTypeDef, _OptionalProjectStatusTypeDef):
    pass


ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef", {"projectId": str, "projectArn": str}, total=False
)

ResourceTypeDef = TypedDict("ResourceTypeDef", {"id": str})

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef", {"bucketName": str, "bucketKey": str}, total=False
)

_RequiredTeamMemberTypeDef = TypedDict(
    "_RequiredTeamMemberTypeDef", {"userArn": str, "projectRole": str}
)
_OptionalTeamMemberTypeDef = TypedDict(
    "_OptionalTeamMemberTypeDef", {"remoteAccessAllowed": bool}, total=False
)


class TeamMemberTypeDef(_RequiredTeamMemberTypeDef, _OptionalTeamMemberTypeDef):
    pass


ToolchainSourceTypeDef = TypedDict("ToolchainSourceTypeDef", {"s3": "S3LocationTypeDef"})

UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)

AssociateTeamMemberResultTypeDef = TypedDict(
    "AssociateTeamMemberResultTypeDef", {"clientRequestToken": str}, total=False
)

CodeTypeDef = TypedDict(
    "CodeTypeDef", {"source": "CodeSourceTypeDef", "destination": "CodeDestinationTypeDef"}
)

_RequiredCreateProjectResultTypeDef = TypedDict(
    "_RequiredCreateProjectResultTypeDef", {"id": str, "arn": str}
)
_OptionalCreateProjectResultTypeDef = TypedDict(
    "_OptionalCreateProjectResultTypeDef",
    {"clientRequestToken": str, "projectTemplateId": str},
    total=False,
)


class CreateProjectResultTypeDef(
    _RequiredCreateProjectResultTypeDef, _OptionalCreateProjectResultTypeDef
):
    pass


_RequiredCreateUserProfileResultTypeDef = TypedDict(
    "_RequiredCreateUserProfileResultTypeDef", {"userArn": str}
)
_OptionalCreateUserProfileResultTypeDef = TypedDict(
    "_OptionalCreateUserProfileResultTypeDef",
    {
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)


class CreateUserProfileResultTypeDef(
    _RequiredCreateUserProfileResultTypeDef, _OptionalCreateUserProfileResultTypeDef
):
    pass


DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef", {"stackId": str, "projectArn": str}, total=False
)

DeleteUserProfileResultTypeDef = TypedDict("DeleteUserProfileResultTypeDef", {"userArn": str})

DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": "ProjectStatusTypeDef",
    },
    total=False,
)

_RequiredDescribeUserProfileResultTypeDef = TypedDict(
    "_RequiredDescribeUserProfileResultTypeDef",
    {"userArn": str, "createdTimestamp": datetime, "lastModifiedTimestamp": datetime},
)
_OptionalDescribeUserProfileResultTypeDef = TypedDict(
    "_OptionalDescribeUserProfileResultTypeDef",
    {"displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)


class DescribeUserProfileResultTypeDef(
    _RequiredDescribeUserProfileResultTypeDef, _OptionalDescribeUserProfileResultTypeDef
):
    pass


_RequiredListProjectsResultTypeDef = TypedDict(
    "_RequiredListProjectsResultTypeDef", {"projects": List["ProjectSummaryTypeDef"]}
)
_OptionalListProjectsResultTypeDef = TypedDict(
    "_OptionalListProjectsResultTypeDef", {"nextToken": str}, total=False
)


class ListProjectsResultTypeDef(
    _RequiredListProjectsResultTypeDef, _OptionalListProjectsResultTypeDef
):
    pass


ListResourcesResultTypeDef = TypedDict(
    "ListResourcesResultTypeDef",
    {"resources": List["ResourceTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForProjectResultTypeDef = TypedDict(
    "ListTagsForProjectResultTypeDef", {"tags": Dict[str, str], "nextToken": str}, total=False
)

_RequiredListTeamMembersResultTypeDef = TypedDict(
    "_RequiredListTeamMembersResultTypeDef", {"teamMembers": List["TeamMemberTypeDef"]}
)
_OptionalListTeamMembersResultTypeDef = TypedDict(
    "_OptionalListTeamMembersResultTypeDef", {"nextToken": str}, total=False
)


class ListTeamMembersResultTypeDef(
    _RequiredListTeamMembersResultTypeDef, _OptionalListTeamMembersResultTypeDef
):
    pass


_RequiredListUserProfilesResultTypeDef = TypedDict(
    "_RequiredListUserProfilesResultTypeDef", {"userProfiles": List["UserProfileSummaryTypeDef"]}
)
_OptionalListUserProfilesResultTypeDef = TypedDict(
    "_OptionalListUserProfilesResultTypeDef", {"nextToken": str}, total=False
)


class ListUserProfilesResultTypeDef(
    _RequiredListUserProfilesResultTypeDef, _OptionalListUserProfilesResultTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagProjectResultTypeDef = TypedDict(
    "TagProjectResultTypeDef", {"tags": Dict[str, str]}, total=False
)

_RequiredToolchainTypeDef = TypedDict(
    "_RequiredToolchainTypeDef", {"source": "ToolchainSourceTypeDef"}
)
_OptionalToolchainTypeDef = TypedDict(
    "_OptionalToolchainTypeDef", {"roleArn": str, "stackParameters": Dict[str, str]}, total=False
)


class ToolchainTypeDef(_RequiredToolchainTypeDef, _OptionalToolchainTypeDef):
    pass


UpdateTeamMemberResultTypeDef = TypedDict(
    "UpdateTeamMemberResultTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)

_RequiredUpdateUserProfileResultTypeDef = TypedDict(
    "_RequiredUpdateUserProfileResultTypeDef", {"userArn": str}
)
_OptionalUpdateUserProfileResultTypeDef = TypedDict(
    "_OptionalUpdateUserProfileResultTypeDef",
    {
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)


class UpdateUserProfileResultTypeDef(
    _RequiredUpdateUserProfileResultTypeDef, _OptionalUpdateUserProfileResultTypeDef
):
    pass
