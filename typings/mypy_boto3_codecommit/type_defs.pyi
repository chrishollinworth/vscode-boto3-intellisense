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
from typing import Dict, List

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
    {"content": bytes, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
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

BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"],
    },
)

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
    },
    total=False,
)


class BatchDescribeMergeConflictsOutputTypeDef(
    _RequiredBatchDescribeMergeConflictsOutputTypeDef,
    _OptionalBatchDescribeMergeConflictsOutputTypeDef,
):
    pass


BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"],
    },
)

BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {"commits": List["CommitTypeDef"], "errors": List["BatchGetCommitsErrorTypeDef"]},
    total=False,
)

BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
    {"repositories": List["RepositoryMetadataTypeDef"], "repositoriesNotFound": List[str]},
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

CreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)

CreateCommitOutputTypeDef = TypedDict(
    "CreateCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List["FileMetadataTypeDef"],
        "filesUpdated": List["FileMetadataTypeDef"],
        "filesDeleted": List["FileMetadataTypeDef"],
    },
    total=False,
)

CreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputTypeDef", {"approvalRule": "ApprovalRuleTypeDef"}
)

CreatePullRequestOutputTypeDef = TypedDict(
    "CreatePullRequestOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {"repositoryMetadata": "RepositoryMetadataTypeDef"},
    total=False,
)

CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef", {"commitId": str, "treeId": str}, total=False
)

DeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputTypeDef", {"approvalRuleTemplateId": str}
)

DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef", {"deletedBranch": "BranchInfoTypeDef"}, total=False
)

DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef", {"comment": "CommentTypeDef"}, total=False
)

DeleteFileOutputTypeDef = TypedDict(
    "DeleteFileOutputTypeDef", {"commitId": str, "blobId": str, "treeId": str, "filePath": str}
)

DeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputTypeDef", {"approvalRuleId": str}
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef", {"repositoryId": str}, total=False
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
    {"nextToken": str, "baseCommitId": str},
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
    "_OptionalDescribePullRequestEventsOutputTypeDef", {"nextToken": str}, total=False
)


class DescribePullRequestEventsOutputTypeDef(
    _RequiredDescribePullRequestEventsOutputTypeDef, _OptionalDescribePullRequestEventsOutputTypeDef
):
    pass


EvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputTypeDef", {"evaluation": "EvaluationTypeDef"}
)

GetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputTypeDef", {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"}
)

GetBlobOutputTypeDef = TypedDict("GetBlobOutputTypeDef", {"content": bytes})

GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef", {"branch": "BranchInfoTypeDef"}, total=False
)

GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef", {"comment": "CommentTypeDef"}, total=False
)

_RequiredGetCommentReactionsOutputTypeDef = TypedDict(
    "_RequiredGetCommentReactionsOutputTypeDef",
    {"reactionsForComment": List["ReactionForCommentTypeDef"]},
)
_OptionalGetCommentReactionsOutputTypeDef = TypedDict(
    "_OptionalGetCommentReactionsOutputTypeDef", {"nextToken": str}, total=False
)


class GetCommentReactionsOutputTypeDef(
    _RequiredGetCommentReactionsOutputTypeDef, _OptionalGetCommentReactionsOutputTypeDef
):
    pass


GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {"commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"], "nextToken": str},
    total=False,
)

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {"commentsForPullRequestData": List["CommentsForPullRequestTypeDef"], "nextToken": str},
    total=False,
)

GetCommitOutputTypeDef = TypedDict("GetCommitOutputTypeDef", {"commit": "CommitTypeDef"})

GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {"differences": List["DifferenceTypeDef"], "NextToken": str},
    total=False,
)

GetFileOutputTypeDef = TypedDict(
    "GetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileSize": int,
        "fileContent": bytes,
    },
)

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
    },
    total=False,
)


class GetFolderOutputTypeDef(_RequiredGetFolderOutputTypeDef, _OptionalGetFolderOutputTypeDef):
    pass


GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {"sourceCommitId": str, "destinationCommitId": str, "baseCommitId": str, "mergedCommitId": str},
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
    "_OptionalGetMergeConflictsOutputTypeDef", {"baseCommitId": str, "nextToken": str}, total=False
)


class GetMergeConflictsOutputTypeDef(
    _RequiredGetMergeConflictsOutputTypeDef, _OptionalGetMergeConflictsOutputTypeDef
):
    pass


GetMergeOptionsOutputTypeDef = TypedDict(
    "GetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
    },
)

GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef", {"approvals": List["ApprovalTypeDef"]}, total=False
)

GetPullRequestOutputTypeDef = TypedDict(
    "GetPullRequestOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)

GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef", {"overridden": bool, "overrider": str}, total=False
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef", {"repositoryMetadata": "RepositoryMetadataTypeDef"}, total=False
)

GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
    {"configurationId": str, "triggers": List["RepositoryTriggerTypeDef"]},
    total=False,
)

ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)

ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef", {"branches": List[str], "nextToken": str}, total=False
)

_RequiredListPullRequestsOutputTypeDef = TypedDict(
    "_RequiredListPullRequestsOutputTypeDef", {"pullRequestIds": List[str]}
)
_OptionalListPullRequestsOutputTypeDef = TypedDict(
    "_OptionalListPullRequestsOutputTypeDef", {"nextToken": str}, total=False
)


class ListPullRequestsOutputTypeDef(
    _RequiredListPullRequestsOutputTypeDef, _OptionalListPullRequestsOutputTypeDef
):
    pass


ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {"repositoryNames": List[str], "nextToken": str},
    total=False,
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {"repositories": List["RepositoryNameIdPairTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"tags": Dict[str, str], "nextToken": str}, total=False
)

MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef", {"commitId": str, "treeId": str}, total=False
)

MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef", {"commitId": str, "treeId": str}, total=False
)

MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef", {"commitId": str, "treeId": str}, total=False
)

MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}, total=False
)

MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}, total=False
)

MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}, total=False
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
    },
    total=False,
)

PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef", {"comment": "CommentTypeDef"}, total=False
)

_RequiredPutFileEntryTypeDef = TypedDict("_RequiredPutFileEntryTypeDef", {"filePath": str})
_OptionalPutFileEntryTypeDef = TypedDict(
    "_OptionalPutFileEntryTypeDef",
    {
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileContent": bytes,
        "sourceFile": "SourceFileSpecifierTypeDef",
    },
    total=False,
)


class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, _OptionalPutFileEntryTypeDef):
    pass


PutFileOutputTypeDef = TypedDict(
    "PutFileOutputTypeDef", {"commitId": str, "blobId": str, "treeId": str}
)

PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef", {"configurationId": str}, total=False
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
    },
    total=False,
)

UpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)

UpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)

UpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    {"approvalRuleTemplate": "ApprovalRuleTemplateTypeDef"},
)

UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef", {"comment": "CommentTypeDef"}, total=False
)

UpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputTypeDef", {"approvalRule": "ApprovalRuleTypeDef"}
)

UpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)

UpdatePullRequestStatusOutputTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)

UpdatePullRequestTitleOutputTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputTypeDef", {"pullRequest": "PullRequestTypeDef"}
)
