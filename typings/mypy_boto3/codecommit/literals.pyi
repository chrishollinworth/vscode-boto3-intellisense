"""
Type annotations for codecommit service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/literals.html)

Usage::

    ```python
    from mypy_boto3_codecommit.literals import ApprovalStateType

    data: ApprovalStateType = "APPROVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApprovalStateType",
    "ChangeTypeEnumType",
    "ConflictDetailLevelTypeEnumType",
    "ConflictResolutionStrategyTypeEnumType",
    "DescribePullRequestEventsPaginatorName",
    "FileModeTypeEnumType",
    "GetCommentsForComparedCommitPaginatorName",
    "GetCommentsForPullRequestPaginatorName",
    "GetDifferencesPaginatorName",
    "ListBranchesPaginatorName",
    "ListPullRequestsPaginatorName",
    "ListRepositoriesPaginatorName",
    "MergeOptionTypeEnumType",
    "ObjectTypeEnumType",
    "OrderEnumType",
    "OverrideStatusType",
    "PullRequestEventTypeType",
    "PullRequestStatusEnumType",
    "RelativeFileVersionEnumType",
    "ReplacementTypeEnumType",
    "RepositoryTriggerEventEnumType",
    "SortByEnumType",
)

ApprovalStateType = Literal["APPROVE", "REVOKE"]
ChangeTypeEnumType = Literal["A", "D", "M"]
ConflictDetailLevelTypeEnumType = Literal["FILE_LEVEL", "LINE_LEVEL"]
ConflictResolutionStrategyTypeEnumType = Literal[
    "ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"
]
DescribePullRequestEventsPaginatorName = Literal["describe_pull_request_events"]
FileModeTypeEnumType = Literal["EXECUTABLE", "NORMAL", "SYMLINK"]
GetCommentsForComparedCommitPaginatorName = Literal["get_comments_for_compared_commit"]
GetCommentsForPullRequestPaginatorName = Literal["get_comments_for_pull_request"]
GetDifferencesPaginatorName = Literal["get_differences"]
ListBranchesPaginatorName = Literal["list_branches"]
ListPullRequestsPaginatorName = Literal["list_pull_requests"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
MergeOptionTypeEnumType = Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]
ObjectTypeEnumType = Literal["DIRECTORY", "FILE", "GIT_LINK", "SYMBOLIC_LINK"]
OrderEnumType = Literal["ascending", "descending"]
OverrideStatusType = Literal["OVERRIDE", "REVOKE"]
PullRequestEventTypeType = Literal[
    "PULL_REQUEST_APPROVAL_RULE_CREATED",
    "PULL_REQUEST_APPROVAL_RULE_DELETED",
    "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
    "PULL_REQUEST_APPROVAL_RULE_UPDATED",
    "PULL_REQUEST_APPROVAL_STATE_CHANGED",
    "PULL_REQUEST_CREATED",
    "PULL_REQUEST_MERGE_STATE_CHANGED",
    "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
    "PULL_REQUEST_STATUS_CHANGED",
]
PullRequestStatusEnumType = Literal["CLOSED", "OPEN"]
RelativeFileVersionEnumType = Literal["AFTER", "BEFORE"]
ReplacementTypeEnumType = Literal["KEEP_BASE", "KEEP_DESTINATION", "KEEP_SOURCE", "USE_NEW_CONTENT"]
RepositoryTriggerEventEnumType = Literal[
    "all", "createReference", "deleteReference", "updateReference"
]
SortByEnumType = Literal["lastModifiedDate", "repositoryName"]
