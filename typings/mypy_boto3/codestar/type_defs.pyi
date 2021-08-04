"""
Type annotations for codestar service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar.type_defs import AssociateTeamMemberRequestRequestTypeDef

    data: AssociateTeamMemberRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateTeamMemberRequestRequestTypeDef",
    "AssociateTeamMemberResultTypeDef",
    "CodeCommitCodeDestinationTypeDef",
    "CodeDestinationTypeDef",
    "CodeSourceTypeDef",
    "CodeTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResultTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "CreateUserProfileResultTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResultTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeleteUserProfileResultTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResultTypeDef",
    "DescribeUserProfileRequestRequestTypeDef",
    "DescribeUserProfileResultTypeDef",
    "DisassociateTeamMemberRequestRequestTypeDef",
    "GitHubCodeDestinationTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResultTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResultTypeDef",
    "ListTagsForProjectRequestRequestTypeDef",
    "ListTagsForProjectResultTypeDef",
    "ListTeamMembersRequestRequestTypeDef",
    "ListTeamMembersResultTypeDef",
    "ListUserProfilesRequestRequestTypeDef",
    "ListUserProfilesResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagProjectRequestRequestTypeDef",
    "TagProjectResultTypeDef",
    "TeamMemberTypeDef",
    "ToolchainSourceTypeDef",
    "ToolchainTypeDef",
    "UntagProjectRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateTeamMemberRequestRequestTypeDef",
    "UpdateTeamMemberResultTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateUserProfileResultTypeDef",
    "UserProfileSummaryTypeDef",
)

_RequiredAssociateTeamMemberRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
        "projectRole": str,
    },
)
_OptionalAssociateTeamMemberRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTeamMemberRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "remoteAccessAllowed": bool,
    },
    total=False,
)

class AssociateTeamMemberRequestRequestTypeDef(
    _RequiredAssociateTeamMemberRequestRequestTypeDef,
    _OptionalAssociateTeamMemberRequestRequestTypeDef,
):
    pass

AssociateTeamMemberResultTypeDef = TypedDict(
    "AssociateTeamMemberResultTypeDef",
    {
        "clientRequestToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CodeCommitCodeDestinationTypeDef = TypedDict(
    "CodeCommitCodeDestinationTypeDef",
    {
        "name": str,
    },
)

CodeDestinationTypeDef = TypedDict(
    "CodeDestinationTypeDef",
    {
        "codeCommit": "CodeCommitCodeDestinationTypeDef",
        "gitHub": "GitHubCodeDestinationTypeDef",
    },
    total=False,
)

CodeSourceTypeDef = TypedDict(
    "CodeSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

CodeTypeDef = TypedDict(
    "CodeTypeDef",
    {
        "source": "CodeSourceTypeDef",
        "destination": "CodeDestinationTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "id": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
        "sourceCode": List["CodeTypeDef"],
        "toolchain": "ToolchainTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "id": str,
        "arn": str,
        "clientRequestToken": str,
        "projectTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
    },
)
_OptionalCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestRequestTypeDef",
    {
        "sshPublicKey": str,
    },
    total=False,
)

class CreateUserProfileRequestRequestTypeDef(
    _RequiredCreateUserProfileRequestRequestTypeDef, _OptionalCreateUserProfileRequestRequestTypeDef
):
    pass

CreateUserProfileResultTypeDef = TypedDict(
    "CreateUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteProjectRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "deleteStack": bool,
    },
    total=False,
)

class DeleteProjectRequestRequestTypeDef(
    _RequiredDeleteProjectRequestRequestTypeDef, _OptionalDeleteProjectRequestRequestTypeDef
):
    pass

DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef",
    {
        "stackId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
    },
)

DeleteUserProfileResultTypeDef = TypedDict(
    "DeleteUserProfileResultTypeDef",
    {
        "userArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "id": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
    },
)

DescribeUserProfileResultTypeDef = TypedDict(
    "DescribeUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTeamMemberRequestRequestTypeDef = TypedDict(
    "DisassociateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
    },
)

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
    "_OptionalGitHubCodeDestinationTypeDef",
    {
        "description": str,
    },
    total=False,
)

class GitHubCodeDestinationTypeDef(
    _RequiredGitHubCodeDestinationTypeDef, _OptionalGitHubCodeDestinationTypeDef
):
    pass

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResourcesRequestRequestTypeDef(
    _RequiredListResourcesRequestRequestTypeDef, _OptionalListResourcesRequestRequestTypeDef
):
    pass

ListResourcesResultTypeDef = TypedDict(
    "ListResourcesResultTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForProjectRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForProjectRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalListTagsForProjectRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForProjectRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTagsForProjectRequestRequestTypeDef(
    _RequiredListTagsForProjectRequestRequestTypeDef,
    _OptionalListTagsForProjectRequestRequestTypeDef,
):
    pass

ListTagsForProjectResultTypeDef = TypedDict(
    "ListTagsForProjectResultTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTeamMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListTeamMembersRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListTeamMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListTeamMembersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTeamMembersRequestRequestTypeDef(
    _RequiredListTeamMembersRequestRequestTypeDef, _OptionalListTeamMembersRequestRequestTypeDef
):
    pass

ListTeamMembersResultTypeDef = TypedDict(
    "ListTeamMembersResultTypeDef",
    {
        "teamMembers": List["TeamMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestRequestTypeDef = TypedDict(
    "ListUserProfilesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListUserProfilesResultTypeDef = TypedDict(
    "ListUserProfilesResultTypeDef",
    {
        "userProfiles": List["UserProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredProjectStatusTypeDef = TypedDict(
    "_RequiredProjectStatusTypeDef",
    {
        "state": str,
    },
)
_OptionalProjectStatusTypeDef = TypedDict(
    "_OptionalProjectStatusTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class ProjectStatusTypeDef(_RequiredProjectStatusTypeDef, _OptionalProjectStatusTypeDef):
    pass

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectId": str,
        "projectArn": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": str,
        "bucketKey": str,
    },
    total=False,
)

TagProjectRequestRequestTypeDef = TypedDict(
    "TagProjectRequestRequestTypeDef",
    {
        "id": str,
        "tags": Dict[str, str],
    },
)

TagProjectResultTypeDef = TypedDict(
    "TagProjectResultTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTeamMemberTypeDef = TypedDict(
    "_RequiredTeamMemberTypeDef",
    {
        "userArn": str,
        "projectRole": str,
    },
)
_OptionalTeamMemberTypeDef = TypedDict(
    "_OptionalTeamMemberTypeDef",
    {
        "remoteAccessAllowed": bool,
    },
    total=False,
)

class TeamMemberTypeDef(_RequiredTeamMemberTypeDef, _OptionalTeamMemberTypeDef):
    pass

ToolchainSourceTypeDef = TypedDict(
    "ToolchainSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

_RequiredToolchainTypeDef = TypedDict(
    "_RequiredToolchainTypeDef",
    {
        "source": "ToolchainSourceTypeDef",
    },
)
_OptionalToolchainTypeDef = TypedDict(
    "_OptionalToolchainTypeDef",
    {
        "roleArn": str,
        "stackParameters": Dict[str, str],
    },
    total=False,
)

class ToolchainTypeDef(_RequiredToolchainTypeDef, _OptionalToolchainTypeDef):
    pass

UntagProjectRequestRequestTypeDef = TypedDict(
    "UntagProjectRequestRequestTypeDef",
    {
        "id": str,
        "tags": List[str],
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

_RequiredUpdateTeamMemberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
    },
)
_OptionalUpdateTeamMemberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTeamMemberRequestRequestTypeDef",
    {
        "projectRole": str,
        "remoteAccessAllowed": bool,
    },
    total=False,
)

class UpdateTeamMemberRequestRequestTypeDef(
    _RequiredUpdateTeamMemberRequestRequestTypeDef, _OptionalUpdateTeamMemberRequestRequestTypeDef
):
    pass

UpdateTeamMemberResultTypeDef = TypedDict(
    "UpdateTeamMemberResultTypeDef",
    {
        "userArn": str,
        "projectRole": str,
        "remoteAccessAllowed": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
    },
)
_OptionalUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestRequestTypeDef",
    {
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
    },
    total=False,
)

class UpdateUserProfileRequestRequestTypeDef(
    _RequiredUpdateUserProfileRequestRequestTypeDef, _OptionalUpdateUserProfileRequestRequestTypeDef
):
    pass

UpdateUserProfileResultTypeDef = TypedDict(
    "UpdateUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
    },
    total=False,
)
