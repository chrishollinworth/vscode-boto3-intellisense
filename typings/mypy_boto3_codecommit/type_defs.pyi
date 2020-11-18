"""
Main interface for codecommit service type definitions.

Usage::

    ```python
    from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "ApprovalRuleTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictTypeDef",
    "DeleteFileEntryTypeDef",
    "DifferenceTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "IsBinaryFileTypeDef",
    "LocationTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "ResponseMetadata",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "UserInfoTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "ConflictResolutionTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PutFileEntryTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {"approvalRuleName": str, "approvalRuleId": str, "approvalRuleContent": str},
    total=False,
)

ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {"revisionId": str, "overrideStatus": Literal["OVERRIDE", "REVOKE"]},
    total=False,
)

ApprovalRuleTemplateTypeDef = TypedDict(
    "ApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ApprovalRuleTypeDef = TypedDict(
    "ApprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": "OriginApprovalRuleTemplateTypeDef",
    },
    total=False,
)

ApprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ApprovalStateChangedEventMetadataTypeDef",
    {"revisionId": str, "approvalStatus": Literal["APPROVE", "REVOKE"]},
    total=False,
)

ApprovalTypeDef = TypedDict(
    "ApprovalTypeDef", {"userArn": str, "approvalState": Literal["APPROVE", "REVOKE"]}, total=False
)

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)

BatchDescribeMergeConflictsErrorTypeDef = TypedDict(
    "BatchDescribeMergeConflictsErrorTypeDef",
    {"filePath": str, "exceptionName": str, "message": str},
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)

BatchGetCommitsErrorTypeDef = TypedDict(
    "BatchGetCommitsErrorTypeDef",
    {"commitId": str, "errorCode": str, "errorMessage": str},
    total=False,
)

BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef", {"blobId": str, "path": str, "mode": str}, total=False
)

BranchInfoTypeDef = TypedDict(
    "BranchInfoTypeDef", {"branchName": str, "commitId": str}, total=False
)

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
        "callerReactions": List[str],
        "reactionCounts": Dict[str, int],
    },
    total=False,
)

CommentsForComparedCommitTypeDef = TypedDict(
    "CommentsForComparedCommitTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comments": List["CommentTypeDef"],
    },
    total=False,
)

CommentsForPullRequestTypeDef = TypedDict(
    "CommentsForPullRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comments": List["CommentTypeDef"],
    },
    total=False,
)

CommitTypeDef = TypedDict(
    "CommitTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": "UserInfoTypeDef",
        "committer": "UserInfoTypeDef",
        "additionalData": str,
    },
    total=False,
)

ConflictMetadataTypeDef = TypedDict(
    "ConflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": "FileSizesTypeDef",
        "fileModes": "FileModesTypeDef",
        "objectTypes": "ObjectTypesTypeDef",
        "numberOfConflicts": int,
        "isBinaryFile": "IsBinaryFileTypeDef",
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": "MergeOperationsTypeDef",
    },
    total=False,
)

ConflictTypeDef = TypedDict(
    "ConflictTypeDef",
    {"conflictMetadata": "ConflictMetadataTypeDef", "mergeHunks": List["MergeHunkTypeDef"]},
    total=False,
)

DeleteFileEntryTypeDef = TypedDict("DeleteFileEntryTypeDef", {"filePath": str})

DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": "BlobMetadataTypeDef",
        "afterBlob": "BlobMetadataTypeDef",
        "changeType": Literal["A", "M", "D"],
    },
    total=False,
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "approved": bool,
        "overridden": bool,
        "approvalRulesSatisfied": List[str],
        "approvalRulesNotSatisfied": List[str],
    },
    total=False,
)

FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

FileModesTypeDef = TypedDict(
    "FileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

FileSizesTypeDef = TypedDict(
    "FileSizesTypeDef", {"source": int, "destination": int, "base": int}, total=False
)

FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

FolderTypeDef = TypedDict(
    "FolderTypeDef", {"treeId": str, "absolutePath": str, "relativePath": str}, total=False
)

IsBinaryFileTypeDef = TypedDict(
    "IsBinaryFileTypeDef", {"source": bool, "destination": bool, "base": bool}, total=False
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

MergeHunkDetailTypeDef = TypedDict(
    "MergeHunkDetailTypeDef", {"startLine": int, "endLine": int, "hunkContent": str}, total=False
)

MergeHunkTypeDef = TypedDict(
    "MergeHunkTypeDef",
    {
        "isConflict": bool,
        "source": "MergeHunkDetailTypeDef",
        "destination": "MergeHunkDetailTypeDef",
        "base": "MergeHunkDetailTypeDef",
    },
    total=False,
)

MergeMetadataTypeDef = TypedDict(
    "MergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

MergeOperationsTypeDef = TypedDict(
    "MergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)

ObjectTypesTypeDef = TypedDict(
    "ObjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)

OriginApprovalRuleTemplateTypeDef = TypedDict(
    "OriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {"repositoryName": str, "sourceCommitId": str, "destinationCommitId": str, "mergeBase": str},
    total=False,
)

PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ],
        "actorArn": str,
        "pullRequestCreatedEventMetadata": "PullRequestCreatedEventMetadataTypeDef",
        "pullRequestStatusChangedEventMetadata": "PullRequestStatusChangedEventMetadataTypeDef",
        "pullRequestSourceReferenceUpdatedEventMetadata": "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
        "pullRequestMergedStateChangedEventMetadata": "PullRequestMergedStateChangedEventMetadataTypeDef",
        "approvalRuleEventMetadata": "ApprovalRuleEventMetadataTypeDef",
        "approvalStateChangedEventMetadata": "ApprovalStateChangedEventMetadataTypeDef",
        "approvalRuleOverriddenEventMetadata": "ApprovalRuleOverriddenEventMetadataTypeDef",
    },
    total=False,
)

PullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    {"repositoryName": str, "destinationReference": str, "mergeMetadata": "MergeMetadataTypeDef"},
    total=False,
)

PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {"repositoryName": str, "beforeCommitId": str, "afterCommitId": str, "mergeBase": str},
    total=False,
)

PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": Literal["OPEN", "CLOSED"]},
    total=False,
)

PullRequestTargetTypeDef = TypedDict(
    "PullRequestTargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": "MergeMetadataTypeDef",
    },
    total=False,
)

PullRequestTypeDef = TypedDict(
    "PullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List["PullRequestTargetTypeDef"],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List["ApprovalRuleTypeDef"],
    },
    total=False,
)

ReactionForCommentTypeDef = TypedDict(
    "ReactionForCommentTypeDef",
    {
        "reaction": "ReactionValueFormatsTypeDef",
        "reactionUsers": List[str],
        "reactionsFromDeletedUsersCount": int,
    },
    total=False,
)

ReactionValueFormatsTypeDef = TypedDict(
    "ReactionValueFormatsTypeDef", {"emoji": str, "shortCode": str, "unicode": str}, total=False
)

_RequiredReplaceContentEntryTypeDef = TypedDict(
    "_RequiredReplaceContentEntryTypeDef",
    {
        "filePath": str,
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
    },
)
_OptionalReplaceContentEntryTypeDef = TypedDict(
    "_OptionalReplaceContentEntryTypeDef",
    {"content": Union[bytes, IO[bytes]], "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ReplaceContentEntryTypeDef(
    _RequiredReplaceContentEntryTypeDef, _OptionalReplaceContentEntryTypeDef
):
    pass


RepositoryMetadataTypeDef = TypedDict(
    "RepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)

RepositoryNameIdPairTypeDef = TypedDict(
    "RepositoryNameIdPairTypeDef", {"repositoryName": str, "repositoryId": str}, total=False
)

RepositoryTriggerExecutionFailureTypeDef = TypedDict(
    "RepositoryTriggerExecutionFailureTypeDef", {"trigger": str, "failureMessage": str}, total=False
)

_RequiredRepositoryTriggerTypeDef = TypedDict(
    "_RequiredRepositoryTriggerTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
)
_OptionalRepositoryTriggerTypeDef = TypedDict(
    "_OptionalRepositoryTriggerTypeDef", {"customData": str, "branches": List[str]}, total=False
)


class RepositoryTriggerTypeDef(
    _RequiredRepositoryTriggerTypeDef, _OptionalRepositoryTriggerTypeDef
):
    pass


ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SetFileModeEntryTypeDef = TypedDict(
    "SetFileModeEntryTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
)

_RequiredSourceFileSpecifierTypeDef = TypedDict(
    "_RequiredSourceFileSpecifierTypeDef", {"filePath": str}
)
_OptionalSourceFileSpecifierTypeDef = TypedDict(
    "_OptionalSourceFileSpecifierTypeDef", {"isMove": bool}, total=False
)


class SourceFileSpecifierTypeDef(
    _RequiredSourceFileSpecifierTypeDef, _OptionalSourceFileSpecifierTypeDef
):
    pass


SubModuleTypeDef = TypedDict(
    "SubModuleTypeDef", {"commitId": str, "absolutePath": str, "relativePath": str}, total=False
)

SymbolicLinkTypeDef = TypedDict(
    "SymbolicLinkTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

UserInfoTypeDef = TypedDict(
    "UserInfoTypeDef", {"name": str, "email": str, "date": str}, total=False
)

_RequiredBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "_RequiredBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"],
    },
)
_OptionalBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "_OptionalBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef(
    _RequiredBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef,
    _OptionalBatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef,
):
    pass


_RequiredBatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "_RequiredBatchDescribeMergeConflictsOutputTypeDef",
    {"conflicts": List["ConflictTypeDef"], "destinationCommitId": str, "sourceCommitId": str},
)
_OptionalBatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "_OptionalBatchDescribeMergeConflictsOutputTypeDef",
    {
        "nextToken": str,
        "errors": List["BatchDescribeMergeConflictsErrorTypeDef"],
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class BatchDescribeMergeConflictsOutputTypeDef(
    _RequiredBatchDescribeMergeConflictsOutputTypeDef,
    _OptionalBatchDescribeMergeConflictsOutputTypeDef,
):
    pass


_RequiredBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "_RequiredBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"],
    },
)
_OptionalBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "_OptionalBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef(
    _RequiredBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef,
    _OptionalBatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef,
):
    pass


BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {
        "commits": List["CommitTypeDef"],
        "errors": List["BatchGetCommitsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryMetadataTypeDef"],
        "repositoriesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "replaceContents": List["ReplaceContentEntryTypeDef"],
        "deleteFiles": List["DeleteFileEntryTypeDef"],
        "setFileModes": List["SetFileModeEntryTypeDef"],
    },
    total=False,
)

_RequiredCreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_RequiredCreateApprovalRuleTemplateOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)
_OptionalCreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_OptionalCreateApprovalRuleTemplateOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateApprovalRuleTemplateOutputTypeDef(
    _RequiredCreateApprovalRuleTemplateOutputTypeDef,
    _OptionalCreateApprovalRuleTemplateOutputTypeDef,
):
    pass


CreateCommitOutputTypeDef = TypedDict(
    "CreateCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List["FileMetadataTypeDef"],
        "filesUpdated": List["FileMetadataTypeDef"],
        "filesDeleted": List["FileMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredCreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "_RequiredCreatePullRequestApprovalRuleOutputTypeDef", {"approvalRule": "ApprovalRuleTypeDef"}
)
_OptionalCreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "_OptionalCreatePullRequestApprovalRuleOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreatePullRequestApprovalRuleOutputTypeDef(
    _RequiredCreatePullRequestApprovalRuleOutputTypeDef,
    _OptionalCreatePullRequestApprovalRuleOutputTypeDef,
):
    pass


_RequiredCreatePullRequestOutputTypeDef = TypedDict(
    "_RequiredCreatePullRequestOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
_OptionalCreatePullRequestOutputTypeDef = TypedDict(
    "_OptionalCreatePullRequestOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreatePullRequestOutputTypeDef(
    _RequiredCreatePullRequestOutputTypeDef, _OptionalCreatePullRequestOutputTypeDef
):
    pass


CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {"repositoryMetadata": "RepositoryMetadataTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef",
    {"commitId": str, "treeId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredDeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_RequiredDeleteApprovalRuleTemplateOutputTypeDef", {"approvalRuleTemplateId": str}
)
_OptionalDeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_OptionalDeleteApprovalRuleTemplateOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeleteApprovalRuleTemplateOutputTypeDef(
    _RequiredDeleteApprovalRuleTemplateOutputTypeDef,
    _OptionalDeleteApprovalRuleTemplateOutputTypeDef,
):
    pass


DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef",
    {"deletedBranch": "BranchInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef",
    {"comment": "CommentTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredDeleteFileOutputTypeDef = TypedDict(
    "_RequiredDeleteFileOutputTypeDef",
    {"commitId": str, "blobId": str, "treeId": str, "filePath": str},
)
_OptionalDeleteFileOutputTypeDef = TypedDict(
    "_OptionalDeleteFileOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DeleteFileOutputTypeDef(_RequiredDeleteFileOutputTypeDef, _OptionalDeleteFileOutputTypeDef):
    pass


_RequiredDeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "_RequiredDeletePullRequestApprovalRuleOutputTypeDef", {"approvalRuleId": str}
)
_OptionalDeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "_OptionalDeletePullRequestApprovalRuleOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeletePullRequestApprovalRuleOutputTypeDef(
    _RequiredDeletePullRequestApprovalRuleOutputTypeDef,
    _OptionalDeletePullRequestApprovalRuleOutputTypeDef,
):
    pass


DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {"repositoryId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredDescribeMergeConflictsOutputTypeDef = TypedDict(
    "_RequiredDescribeMergeConflictsOutputTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
        "destinationCommitId": str,
        "sourceCommitId": str,
    },
)
_OptionalDescribeMergeConflictsOutputTypeDef = TypedDict(
    "_OptionalDescribeMergeConflictsOutputTypeDef",
    {"nextToken": str, "baseCommitId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeMergeConflictsOutputTypeDef(
    _RequiredDescribeMergeConflictsOutputTypeDef, _OptionalDescribeMergeConflictsOutputTypeDef
):
    pass


_RequiredDescribePullRequestEventsOutputTypeDef = TypedDict(
    "_RequiredDescribePullRequestEventsOutputTypeDef",
    {"pullRequestEvents": List["PullRequestEventTypeDef"]},
)
_OptionalDescribePullRequestEventsOutputTypeDef = TypedDict(
    "_OptionalDescribePullRequestEventsOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribePullRequestEventsOutputTypeDef(
    _RequiredDescribePullRequestEventsOutputTypeDef, _OptionalDescribePullRequestEventsOutputTypeDef
):
    pass


_RequiredEvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "_RequiredEvaluatePullRequestApprovalRulesOutputTypeDef", {"evaluation": "EvaluationTypeDef"}
)
_OptionalEvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "_OptionalEvaluatePullRequestApprovalRulesOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class EvaluatePullRequestApprovalRulesOutputTypeDef(
    _RequiredEvaluatePullRequestApprovalRulesOutputTypeDef,
    _OptionalEvaluatePullRequestApprovalRulesOutputTypeDef,
):
    pass


_RequiredGetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_RequiredGetApprovalRuleTemplateOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)
_OptionalGetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "_OptionalGetApprovalRuleTemplateOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetApprovalRuleTemplateOutputTypeDef(
    _RequiredGetApprovalRuleTemplateOutputTypeDef, _OptionalGetApprovalRuleTemplateOutputTypeDef
):
    pass


_RequiredGetBlobOutputTypeDef = TypedDict(
    "_RequiredGetBlobOutputTypeDef", {"content": Union[bytes, IO[bytes]]}
)
_OptionalGetBlobOutputTypeDef = TypedDict(
    "_OptionalGetBlobOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetBlobOutputTypeDef(_RequiredGetBlobOutputTypeDef, _OptionalGetBlobOutputTypeDef):
    pass


GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef",
    {"branch": "BranchInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef",
    {"comment": "CommentTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetCommentReactionsOutputTypeDef = TypedDict(
    "_RequiredGetCommentReactionsOutputTypeDef",
    {"reactionsForComment": List["ReactionForCommentTypeDef"]},
)
_OptionalGetCommentReactionsOutputTypeDef = TypedDict(
    "_OptionalGetCommentReactionsOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetCommentReactionsOutputTypeDef(
    _RequiredGetCommentReactionsOutputTypeDef, _OptionalGetCommentReactionsOutputTypeDef
):
    pass


GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {
        "commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {
        "commentsForPullRequestData": List["CommentsForPullRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredGetCommitOutputTypeDef = TypedDict(
    "_RequiredGetCommitOutputTypeDef", {"commit": "CommitTypeDef"}
)
_OptionalGetCommitOutputTypeDef = TypedDict(
    "_OptionalGetCommitOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetCommitOutputTypeDef(_RequiredGetCommitOutputTypeDef, _OptionalGetCommitOutputTypeDef):
    pass


GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {
        "differences": List["DifferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredGetFileOutputTypeDef = TypedDict(
    "_RequiredGetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileSize": int,
        "fileContent": Union[bytes, IO[bytes]],
    },
)
_OptionalGetFileOutputTypeDef = TypedDict(
    "_OptionalGetFileOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetFileOutputTypeDef(_RequiredGetFileOutputTypeDef, _OptionalGetFileOutputTypeDef):
    pass


_RequiredGetFolderOutputTypeDef = TypedDict(
    "_RequiredGetFolderOutputTypeDef", {"commitId": str, "folderPath": str}
)
_OptionalGetFolderOutputTypeDef = TypedDict(
    "_OptionalGetFolderOutputTypeDef",
    {
        "treeId": str,
        "subFolders": List["FolderTypeDef"],
        "files": List["FileTypeDef"],
        "symbolicLinks": List["SymbolicLinkTypeDef"],
        "subModules": List["SubModuleTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class GetFolderOutputTypeDef(_RequiredGetFolderOutputTypeDef, _OptionalGetFolderOutputTypeDef):
    pass


GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredGetMergeConflictsOutputTypeDef = TypedDict(
    "_RequiredGetMergeConflictsOutputTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "conflictMetadataList": List["ConflictMetadataTypeDef"],
    },
)
_OptionalGetMergeConflictsOutputTypeDef = TypedDict(
    "_OptionalGetMergeConflictsOutputTypeDef",
    {"baseCommitId": str, "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetMergeConflictsOutputTypeDef(
    _RequiredGetMergeConflictsOutputTypeDef, _OptionalGetMergeConflictsOutputTypeDef
):
    pass


_RequiredGetMergeOptionsOutputTypeDef = TypedDict(
    "_RequiredGetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
    },
)
_OptionalGetMergeOptionsOutputTypeDef = TypedDict(
    "_OptionalGetMergeOptionsOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetMergeOptionsOutputTypeDef(
    _RequiredGetMergeOptionsOutputTypeDef, _OptionalGetMergeOptionsOutputTypeDef
):
    pass


GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef",
    {"approvals": List["ApprovalTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetPullRequestOutputTypeDef = TypedDict(
    "_RequiredGetPullRequestOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
_OptionalGetPullRequestOutputTypeDef = TypedDict(
    "_OptionalGetPullRequestOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class GetPullRequestOutputTypeDef(
    _RequiredGetPullRequestOutputTypeDef, _OptionalGetPullRequestOutputTypeDef
):
    pass


GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef",
    {"overridden": bool, "overrider": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {"repositoryMetadata": "RepositoryMetadataTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "triggers": List["RepositoryTriggerTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef",
    {"branches": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredListPullRequestsOutputTypeDef = TypedDict(
    "_RequiredListPullRequestsOutputTypeDef", {"pullRequestIds": List[str]}
)
_OptionalListPullRequestsOutputTypeDef = TypedDict(
    "_OptionalListPullRequestsOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListPullRequestsOutputTypeDef(
    _RequiredListPullRequestsOutputTypeDef, _OptionalListPullRequestsOutputTypeDef
):
    pass


ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {"repositoryNames": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryNameIdPairTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"tags": Dict[str, str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef",
    {"commitId": str, "treeId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef",
    {"commitId": str, "treeId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef",
    {"commitId": str, "treeId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef",
    {"pullRequest": "PullRequestTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef",
    {"pullRequest": "PullRequestTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef",
    {"pullRequest": "PullRequestTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PostCommentForComparedCommitOutputTypeDef = TypedDict(
    "PostCommentForComparedCommitOutputTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PostCommentForPullRequestOutputTypeDef = TypedDict(
    "PostCommentForPullRequestOutputTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef",
    {"comment": "CommentTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredPutFileEntryTypeDef = TypedDict("_RequiredPutFileEntryTypeDef", {"filePath": str})
_OptionalPutFileEntryTypeDef = TypedDict(
    "_OptionalPutFileEntryTypeDef",
    {
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileContent": Union[bytes, IO[bytes]],
        "sourceFile": "SourceFileSpecifierTypeDef",
    },
    total=False,
)


class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, _OptionalPutFileEntryTypeDef):
    pass


_RequiredPutFileOutputTypeDef = TypedDict(
    "_RequiredPutFileOutputTypeDef", {"commitId": str, "blobId": str, "treeId": str}
)
_OptionalPutFileOutputTypeDef = TypedDict(
    "_OptionalPutFileOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class PutFileOutputTypeDef(_RequiredPutFileOutputTypeDef, _OptionalPutFileOutputTypeDef):
    pass


PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef",
    {"configurationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef", {"repositoryName": str, "sourceReference": str}
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef", {"destinationReference": str}, total=False
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


TestRepositoryTriggersOutputTypeDef = TypedDict(
    "TestRepositoryTriggersOutputTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List["RepositoryTriggerExecutionFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredUpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "_RequiredUpdateApprovalRuleTemplateContentOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)
_OptionalUpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "_OptionalUpdateApprovalRuleTemplateContentOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateApprovalRuleTemplateContentOutputTypeDef(
    _RequiredUpdateApprovalRuleTemplateContentOutputTypeDef,
    _OptionalUpdateApprovalRuleTemplateContentOutputTypeDef,
):
    pass


_RequiredUpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "_RequiredUpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)
_OptionalUpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "_OptionalUpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateApprovalRuleTemplateDescriptionOutputTypeDef(
    _RequiredUpdateApprovalRuleTemplateDescriptionOutputTypeDef,
    _OptionalUpdateApprovalRuleTemplateDescriptionOutputTypeDef,
):
    pass


_RequiredUpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "_RequiredUpdateApprovalRuleTemplateNameOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)
_OptionalUpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "_OptionalUpdateApprovalRuleTemplateNameOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateApprovalRuleTemplateNameOutputTypeDef(
    _RequiredUpdateApprovalRuleTemplateNameOutputTypeDef,
    _OptionalUpdateApprovalRuleTemplateNameOutputTypeDef,
):
    pass


UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef",
    {"comment": "CommentTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredUpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "_RequiredUpdatePullRequestApprovalRuleContentOutputTypeDef",
    {"approvalRule": "ApprovalRuleTypeDef"},
)
_OptionalUpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "_OptionalUpdatePullRequestApprovalRuleContentOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdatePullRequestApprovalRuleContentOutputTypeDef(
    _RequiredUpdatePullRequestApprovalRuleContentOutputTypeDef,
    _OptionalUpdatePullRequestApprovalRuleContentOutputTypeDef,
):
    pass


_RequiredUpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "_RequiredUpdatePullRequestDescriptionOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
_OptionalUpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "_OptionalUpdatePullRequestDescriptionOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdatePullRequestDescriptionOutputTypeDef(
    _RequiredUpdatePullRequestDescriptionOutputTypeDef,
    _OptionalUpdatePullRequestDescriptionOutputTypeDef,
):
    pass


_RequiredUpdatePullRequestStatusOutputTypeDef = TypedDict(
    "_RequiredUpdatePullRequestStatusOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
_OptionalUpdatePullRequestStatusOutputTypeDef = TypedDict(
    "_OptionalUpdatePullRequestStatusOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdatePullRequestStatusOutputTypeDef(
    _RequiredUpdatePullRequestStatusOutputTypeDef, _OptionalUpdatePullRequestStatusOutputTypeDef
):
    pass


_RequiredUpdatePullRequestTitleOutputTypeDef = TypedDict(
    "_RequiredUpdatePullRequestTitleOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
_OptionalUpdatePullRequestTitleOutputTypeDef = TypedDict(
    "_OptionalUpdatePullRequestTitleOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdatePullRequestTitleOutputTypeDef(
    _RequiredUpdatePullRequestTitleOutputTypeDef, _OptionalUpdatePullRequestTitleOutputTypeDef
):
    pass
