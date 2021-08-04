"""
Type annotations for codecommit service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApprovalStateType,
    ChangeTypeEnumType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    ObjectTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    RelativeFileVersionEnumType,
    ReplacementTypeEnumType,
    RepositoryTriggerEventEnumType,
    SortByEnumType,
)

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
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsInputRequestTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsInputRequestTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesInputRequestTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictResolutionTypeDef",
    "ConflictTypeDef",
    "CreateApprovalRuleTemplateInputRequestTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateBranchInputRequestTypeDef",
    "CreateCommitInputRequestTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestInputRequestTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitInputRequestTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchInputRequestTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentInputRequestTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileEntryTypeDef",
    "DeleteFileInputRequestTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsInputRequestTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsInputRequestTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "DifferenceTypeDef",
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateInputRequestTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobInputRequestTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchInputRequestTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentInputRequestTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsInputRequestTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitInputRequestTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestInputRequestTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitInputRequestTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesInputRequestTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileInputRequestTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderInputRequestTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitInputRequestTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsInputRequestTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsInputRequestTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestInputRequestTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateInputRequestTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersInputRequestTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "IsBinaryFileTypeDef",
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesInputRequestTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsInputRequestTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LocationTypeDef",
    "MergeBranchesByFastForwardInputRequestTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashInputRequestTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayInputRequestTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "MergePullRequestByFastForwardInputRequestTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashInputRequestTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayInputRequestTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitInputRequestTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestInputRequestTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyInputRequestTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "PutCommentReactionInputRequestTypeDef",
    "PutFileEntryTypeDef",
    "PutFileInputRequestTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersInputRequestTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "ResponseMetadataTypeDef",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "TagResourceInputRequestTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersInputRequestTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApprovalRuleTemplateContentInputRequestTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentInputRequestTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdateDefaultBranchInputRequestTypeDef",
    "UpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusInputRequestTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleInputRequestTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
    "UpdateRepositoryDescriptionInputRequestTypeDef",
    "UpdateRepositoryNameInputRequestTypeDef",
    "UserInfoTypeDef",
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {
        "approvalRuleName": str,
        "approvalRuleId": str,
        "approvalRuleContent": str,
    },
    total=False,
)

ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
    },
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
    {
        "revisionId": str,
        "approvalStatus": ApprovalStateType,
    },
    total=False,
)

ApprovalTypeDef = TypedDict(
    "ApprovalTypeDef",
    {
        "userArn": str,
        "approvalState": ApprovalStateType,
    },
    total=False,
)

AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef = TypedDict(
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {
        "repositoryName": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": List[str],
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeMergeConflictsErrorTypeDef = TypedDict(
    "BatchDescribeMergeConflictsErrorTypeDef",
    {
        "filePath": str,
        "exceptionName": str,
        "message": str,
    },
)

_RequiredBatchDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "_RequiredBatchDescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalBatchDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "_OptionalBatchDescribeMergeConflictsInputRequestTypeDef",
    {
        "maxMergeHunks": int,
        "maxConflictFiles": int,
        "filePaths": List[str],
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)

class BatchDescribeMergeConflictsInputRequestTypeDef(
    _RequiredBatchDescribeMergeConflictsInputRequestTypeDef,
    _OptionalBatchDescribeMergeConflictsInputRequestTypeDef,
):
    pass

BatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "BatchDescribeMergeConflictsOutputTypeDef",
    {
        "conflicts": List["ConflictTypeDef"],
        "nextToken": str,
        "errors": List["BatchDescribeMergeConflictsErrorTypeDef"],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    {
        "repositoryName": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": List[str],
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCommitsErrorTypeDef = TypedDict(
    "BatchGetCommitsErrorTypeDef",
    {
        "commitId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchGetCommitsInputRequestTypeDef = TypedDict(
    "BatchGetCommitsInputRequestTypeDef",
    {
        "commitIds": List[str],
        "repositoryName": str,
    },
)

BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {
        "commits": List["CommitTypeDef"],
        "errors": List["BatchGetCommitsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoriesInputRequestTypeDef = TypedDict(
    "BatchGetRepositoriesInputRequestTypeDef",
    {
        "repositoryNames": List[str],
    },
)

BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryMetadataTypeDef"],
        "repositoriesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef",
    {
        "blobId": str,
        "path": str,
        "mode": str,
    },
    total=False,
)

BranchInfoTypeDef = TypedDict(
    "BranchInfoTypeDef",
    {
        "branchName": str,
        "commitId": str,
    },
    total=False,
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

ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "replaceContents": List["ReplaceContentEntryTypeDef"],
        "deleteFiles": List["DeleteFileEntryTypeDef"],
        "setFileModes": List["SetFileModeEntryTypeDef"],
    },
    total=False,
)

ConflictTypeDef = TypedDict(
    "ConflictTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
    },
    total=False,
)

_RequiredCreateApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreateApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateContent": str,
    },
)
_OptionalCreateApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreateApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateDescription": str,
    },
    total=False,
)

class CreateApprovalRuleTemplateInputRequestTypeDef(
    _RequiredCreateApprovalRuleTemplateInputRequestTypeDef,
    _OptionalCreateApprovalRuleTemplateInputRequestTypeDef,
):
    pass

CreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBranchInputRequestTypeDef = TypedDict(
    "CreateBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "commitId": str,
    },
)

_RequiredCreateCommitInputRequestTypeDef = TypedDict(
    "_RequiredCreateCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)
_OptionalCreateCommitInputRequestTypeDef = TypedDict(
    "_OptionalCreateCommitInputRequestTypeDef",
    {
        "parentCommitId": str,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "putFiles": List["PutFileEntryTypeDef"],
        "deleteFiles": List["DeleteFileEntryTypeDef"],
        "setFileModes": List["SetFileModeEntryTypeDef"],
    },
    total=False,
)

class CreateCommitInputRequestTypeDef(
    _RequiredCreateCommitInputRequestTypeDef, _OptionalCreateCommitInputRequestTypeDef
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
    },
)

CreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePullRequestInputRequestTypeDef = TypedDict(
    "_RequiredCreatePullRequestInputRequestTypeDef",
    {
        "title": str,
        "targets": List["TargetTypeDef"],
    },
)
_OptionalCreatePullRequestInputRequestTypeDef = TypedDict(
    "_OptionalCreatePullRequestInputRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
    },
    total=False,
)

class CreatePullRequestInputRequestTypeDef(
    _RequiredCreatePullRequestInputRequestTypeDef, _OptionalCreatePullRequestInputRequestTypeDef
):
    pass

CreatePullRequestOutputTypeDef = TypedDict(
    "CreatePullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryInputRequestTypeDef",
    {
        "repositoryDescription": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRepositoryInputRequestTypeDef(
    _RequiredCreateRepositoryInputRequestTypeDef, _OptionalCreateRepositoryInputRequestTypeDef
):
    pass

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUnreferencedMergeCommitInputRequestTypeDef = TypedDict(
    "_RequiredCreateUnreferencedMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalCreateUnreferencedMergeCommitInputRequestTypeDef = TypedDict(
    "_OptionalCreateUnreferencedMergeCommitInputRequestTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)

class CreateUnreferencedMergeCommitInputRequestTypeDef(
    _RequiredCreateUnreferencedMergeCommitInputRequestTypeDef,
    _OptionalCreateUnreferencedMergeCommitInputRequestTypeDef,
):
    pass

CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

DeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchInputRequestTypeDef = TypedDict(
    "DeleteBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)

DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef",
    {
        "deletedBranch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCommentContentInputRequestTypeDef = TypedDict(
    "DeleteCommentContentInputRequestTypeDef",
    {
        "commentId": str,
    },
)

DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileEntryTypeDef = TypedDict(
    "DeleteFileEntryTypeDef",
    {
        "filePath": str,
    },
)

_RequiredDeleteFileInputRequestTypeDef = TypedDict(
    "_RequiredDeleteFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "filePath": str,
        "parentCommitId": str,
    },
)
_OptionalDeleteFileInputRequestTypeDef = TypedDict(
    "_OptionalDeleteFileInputRequestTypeDef",
    {
        "keepEmptyFolders": bool,
        "commitMessage": str,
        "name": str,
        "email": str,
    },
    total=False,
)

class DeleteFileInputRequestTypeDef(
    _RequiredDeleteFileInputRequestTypeDef, _OptionalDeleteFileInputRequestTypeDef
):
    pass

DeleteFileOutputTypeDef = TypedDict(
    "DeleteFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "filePath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
    },
)

DeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repositoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "filePath": str,
    },
)
_OptionalDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeMergeConflictsInputRequestTypeDef",
    {
        "maxMergeHunks": int,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)

class DescribeMergeConflictsInputRequestTypeDef(
    _RequiredDescribeMergeConflictsInputRequestTypeDef,
    _OptionalDescribeMergeConflictsInputRequestTypeDef,
):
    pass

DescribeMergeConflictsOutputTypeDef = TypedDict(
    "DescribeMergeConflictsOutputTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePullRequestEventsInputRequestTypeDef = TypedDict(
    "_RequiredDescribePullRequestEventsInputRequestTypeDef",
    {
        "pullRequestId": str,
    },
)
_OptionalDescribePullRequestEventsInputRequestTypeDef = TypedDict(
    "_OptionalDescribePullRequestEventsInputRequestTypeDef",
    {
        "pullRequestEventType": PullRequestEventTypeType,
        "actorArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribePullRequestEventsInputRequestTypeDef(
    _RequiredDescribePullRequestEventsInputRequestTypeDef,
    _OptionalDescribePullRequestEventsInputRequestTypeDef,
):
    pass

DescribePullRequestEventsOutputTypeDef = TypedDict(
    "DescribePullRequestEventsOutputTypeDef",
    {
        "pullRequestEvents": List["PullRequestEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": "BlobMetadataTypeDef",
        "afterBlob": "BlobMetadataTypeDef",
        "changeType": ChangeTypeEnumType,
    },
    total=False,
)

DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef = TypedDict(
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

EvaluatePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

EvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    {
        "evaluation": "EvaluationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    {
        "absolutePath": str,
        "blobId": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

FileModesTypeDef = TypedDict(
    "FileModesTypeDef",
    {
        "source": FileModeTypeEnumType,
        "destination": FileModeTypeEnumType,
        "base": FileModeTypeEnumType,
    },
    total=False,
)

FileSizesTypeDef = TypedDict(
    "FileSizesTypeDef",
    {
        "source": int,
        "destination": int,
        "base": int,
    },
    total=False,
)

FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "treeId": str,
        "absolutePath": str,
        "relativePath": str,
    },
    total=False,
)

GetApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "GetApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

GetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlobInputRequestTypeDef = TypedDict(
    "GetBlobInputRequestTypeDef",
    {
        "repositoryName": str,
        "blobId": str,
    },
)

GetBlobOutputTypeDef = TypedDict(
    "GetBlobOutputTypeDef",
    {
        "content": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchInputRequestTypeDef = TypedDict(
    "GetBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
    total=False,
)

GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef",
    {
        "branch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentInputRequestTypeDef = TypedDict(
    "GetCommentInputRequestTypeDef",
    {
        "commentId": str,
    },
)

GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentReactionsInputRequestTypeDef = TypedDict(
    "_RequiredGetCommentReactionsInputRequestTypeDef",
    {
        "commentId": str,
    },
)
_OptionalGetCommentReactionsInputRequestTypeDef = TypedDict(
    "_OptionalGetCommentReactionsInputRequestTypeDef",
    {
        "reactionUserArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetCommentReactionsInputRequestTypeDef(
    _RequiredGetCommentReactionsInputRequestTypeDef, _OptionalGetCommentReactionsInputRequestTypeDef
):
    pass

GetCommentReactionsOutputTypeDef = TypedDict(
    "GetCommentReactionsOutputTypeDef",
    {
        "reactionsForComment": List["ReactionForCommentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentsForComparedCommitInputRequestTypeDef = TypedDict(
    "_RequiredGetCommentsForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
    },
)
_OptionalGetCommentsForComparedCommitInputRequestTypeDef = TypedDict(
    "_OptionalGetCommentsForComparedCommitInputRequestTypeDef",
    {
        "beforeCommitId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetCommentsForComparedCommitInputRequestTypeDef(
    _RequiredGetCommentsForComparedCommitInputRequestTypeDef,
    _OptionalGetCommentsForComparedCommitInputRequestTypeDef,
):
    pass

GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {
        "commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentsForPullRequestInputRequestTypeDef = TypedDict(
    "_RequiredGetCommentsForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
    },
)
_OptionalGetCommentsForPullRequestInputRequestTypeDef = TypedDict(
    "_OptionalGetCommentsForPullRequestInputRequestTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetCommentsForPullRequestInputRequestTypeDef(
    _RequiredGetCommentsForPullRequestInputRequestTypeDef,
    _OptionalGetCommentsForPullRequestInputRequestTypeDef,
):
    pass

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {
        "commentsForPullRequestData": List["CommentsForPullRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommitInputRequestTypeDef = TypedDict(
    "GetCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "commitId": str,
    },
)

GetCommitOutputTypeDef = TypedDict(
    "GetCommitOutputTypeDef",
    {
        "commit": "CommitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDifferencesInputRequestTypeDef = TypedDict(
    "_RequiredGetDifferencesInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitSpecifier": str,
    },
)
_OptionalGetDifferencesInputRequestTypeDef = TypedDict(
    "_OptionalGetDifferencesInputRequestTypeDef",
    {
        "beforeCommitSpecifier": str,
        "beforePath": str,
        "afterPath": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetDifferencesInputRequestTypeDef(
    _RequiredGetDifferencesInputRequestTypeDef, _OptionalGetDifferencesInputRequestTypeDef
):
    pass

GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {
        "differences": List["DifferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFileInputRequestTypeDef = TypedDict(
    "_RequiredGetFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "filePath": str,
    },
)
_OptionalGetFileInputRequestTypeDef = TypedDict(
    "_OptionalGetFileInputRequestTypeDef",
    {
        "commitSpecifier": str,
    },
    total=False,
)

class GetFileInputRequestTypeDef(
    _RequiredGetFileInputRequestTypeDef, _OptionalGetFileInputRequestTypeDef
):
    pass

GetFileOutputTypeDef = TypedDict(
    "GetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
        "fileSize": int,
        "fileContent": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFolderInputRequestTypeDef = TypedDict(
    "_RequiredGetFolderInputRequestTypeDef",
    {
        "repositoryName": str,
        "folderPath": str,
    },
)
_OptionalGetFolderInputRequestTypeDef = TypedDict(
    "_OptionalGetFolderInputRequestTypeDef",
    {
        "commitSpecifier": str,
    },
    total=False,
)

class GetFolderInputRequestTypeDef(
    _RequiredGetFolderInputRequestTypeDef, _OptionalGetFolderInputRequestTypeDef
):
    pass

GetFolderOutputTypeDef = TypedDict(
    "GetFolderOutputTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List["FolderTypeDef"],
        "files": List["FileTypeDef"],
        "symbolicLinks": List["SymbolicLinkTypeDef"],
        "subModules": List["SubModuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeCommitInputRequestTypeDef = TypedDict(
    "_RequiredGetMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalGetMergeCommitInputRequestTypeDef = TypedDict(
    "_OptionalGetMergeCommitInputRequestTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
    },
    total=False,
)

class GetMergeCommitInputRequestTypeDef(
    _RequiredGetMergeCommitInputRequestTypeDef, _OptionalGetMergeCommitInputRequestTypeDef
):
    pass

GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeConflictsInputRequestTypeDef = TypedDict(
    "_RequiredGetMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalGetMergeConflictsInputRequestTypeDef = TypedDict(
    "_OptionalGetMergeConflictsInputRequestTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "maxConflictFiles": int,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)

class GetMergeConflictsInputRequestTypeDef(
    _RequiredGetMergeConflictsInputRequestTypeDef, _OptionalGetMergeConflictsInputRequestTypeDef
):
    pass

GetMergeConflictsOutputTypeDef = TypedDict(
    "GetMergeConflictsOutputTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List["ConflictMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeOptionsInputRequestTypeDef = TypedDict(
    "_RequiredGetMergeOptionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalGetMergeOptionsInputRequestTypeDef = TypedDict(
    "_OptionalGetMergeOptionsInputRequestTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
    },
    total=False,
)

class GetMergeOptionsInputRequestTypeDef(
    _RequiredGetMergeOptionsInputRequestTypeDef, _OptionalGetMergeOptionsInputRequestTypeDef
):
    pass

GetMergeOptionsOutputTypeDef = TypedDict(
    "GetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[MergeOptionTypeEnumType],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestApprovalStatesInputRequestTypeDef = TypedDict(
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef",
    {
        "approvals": List["ApprovalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestInputRequestTypeDef = TypedDict(
    "GetPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
    },
)

GetPullRequestOutputTypeDef = TypedDict(
    "GetPullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestOverrideStateInputRequestTypeDef = TypedDict(
    "GetPullRequestOverrideStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef",
    {
        "overridden": bool,
        "overrider": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryTriggersInputRequestTypeDef = TypedDict(
    "GetRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "triggers": List["RepositoryTriggerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IsBinaryFileTypeDef = TypedDict(
    "IsBinaryFileTypeDef",
    {
        "source": bool,
        "destination": bool,
        "base": bool,
    },
    total=False,
)

ListApprovalRuleTemplatesInputRequestTypeDef = TypedDict(
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef(
    _RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef,
    _OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef,
):
    pass

ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBranchesInputRequestTypeDef = TypedDict(
    "_RequiredListBranchesInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListBranchesInputRequestTypeDef = TypedDict(
    "_OptionalListBranchesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListBranchesInputRequestTypeDef(
    _RequiredListBranchesInputRequestTypeDef, _OptionalListBranchesInputRequestTypeDef
):
    pass

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef",
    {
        "branches": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPullRequestsInputRequestTypeDef = TypedDict(
    "_RequiredListPullRequestsInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListPullRequestsInputRequestTypeDef = TypedDict(
    "_OptionalListPullRequestsInputRequestTypeDef",
    {
        "authorArn": str,
        "pullRequestStatus": PullRequestStatusEnumType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPullRequestsInputRequestTypeDef(
    _RequiredListPullRequestsInputRequestTypeDef, _OptionalListPullRequestsInputRequestTypeDef
):
    pass

ListPullRequestsOutputTypeDef = TypedDict(
    "ListPullRequestsOutputTypeDef",
    {
        "pullRequestIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRepositoriesForApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "_RequiredListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)
_OptionalListRepositoriesForApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "_OptionalListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef(
    _RequiredListRepositoriesForApprovalRuleTemplateInputRequestTypeDef,
    _OptionalListRepositoriesForApprovalRuleTemplateInputRequestTypeDef,
):
    pass

ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {
        "repositoryNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "nextToken": str,
        "sortBy": SortByEnumType,
        "order": OrderEnumType,
    },
    total=False,
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryNameIdPairTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "filePath": str,
        "filePosition": int,
        "relativeFileVersion": RelativeFileVersionEnumType,
    },
    total=False,
)

_RequiredMergeBranchesByFastForwardInputRequestTypeDef = TypedDict(
    "_RequiredMergeBranchesByFastForwardInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesByFastForwardInputRequestTypeDef = TypedDict(
    "_OptionalMergeBranchesByFastForwardInputRequestTypeDef",
    {
        "targetBranch": str,
    },
    total=False,
)

class MergeBranchesByFastForwardInputRequestTypeDef(
    _RequiredMergeBranchesByFastForwardInputRequestTypeDef,
    _OptionalMergeBranchesByFastForwardInputRequestTypeDef,
):
    pass

MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergeBranchesBySquashInputRequestTypeDef = TypedDict(
    "_RequiredMergeBranchesBySquashInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesBySquashInputRequestTypeDef = TypedDict(
    "_OptionalMergeBranchesBySquashInputRequestTypeDef",
    {
        "targetBranch": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)

class MergeBranchesBySquashInputRequestTypeDef(
    _RequiredMergeBranchesBySquashInputRequestTypeDef,
    _OptionalMergeBranchesBySquashInputRequestTypeDef,
):
    pass

MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergeBranchesByThreeWayInputRequestTypeDef = TypedDict(
    "_RequiredMergeBranchesByThreeWayInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesByThreeWayInputRequestTypeDef = TypedDict(
    "_OptionalMergeBranchesByThreeWayInputRequestTypeDef",
    {
        "targetBranch": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)

class MergeBranchesByThreeWayInputRequestTypeDef(
    _RequiredMergeBranchesByThreeWayInputRequestTypeDef,
    _OptionalMergeBranchesByThreeWayInputRequestTypeDef,
):
    pass

MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeHunkDetailTypeDef = TypedDict(
    "MergeHunkDetailTypeDef",
    {
        "startLine": int,
        "endLine": int,
        "hunkContent": str,
    },
    total=False,
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
        "mergeOption": MergeOptionTypeEnumType,
    },
    total=False,
)

MergeOperationsTypeDef = TypedDict(
    "MergeOperationsTypeDef",
    {
        "source": ChangeTypeEnumType,
        "destination": ChangeTypeEnumType,
    },
    total=False,
)

_RequiredMergePullRequestByFastForwardInputRequestTypeDef = TypedDict(
    "_RequiredMergePullRequestByFastForwardInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestByFastForwardInputRequestTypeDef = TypedDict(
    "_OptionalMergePullRequestByFastForwardInputRequestTypeDef",
    {
        "sourceCommitId": str,
    },
    total=False,
)

class MergePullRequestByFastForwardInputRequestTypeDef(
    _RequiredMergePullRequestByFastForwardInputRequestTypeDef,
    _OptionalMergePullRequestByFastForwardInputRequestTypeDef,
):
    pass

MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergePullRequestBySquashInputRequestTypeDef = TypedDict(
    "_RequiredMergePullRequestBySquashInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestBySquashInputRequestTypeDef = TypedDict(
    "_OptionalMergePullRequestBySquashInputRequestTypeDef",
    {
        "sourceCommitId": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "commitMessage": str,
        "authorName": str,
        "email": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)

class MergePullRequestBySquashInputRequestTypeDef(
    _RequiredMergePullRequestBySquashInputRequestTypeDef,
    _OptionalMergePullRequestBySquashInputRequestTypeDef,
):
    pass

MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergePullRequestByThreeWayInputRequestTypeDef = TypedDict(
    "_RequiredMergePullRequestByThreeWayInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestByThreeWayInputRequestTypeDef = TypedDict(
    "_OptionalMergePullRequestByThreeWayInputRequestTypeDef",
    {
        "sourceCommitId": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "commitMessage": str,
        "authorName": str,
        "email": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)

class MergePullRequestByThreeWayInputRequestTypeDef(
    _RequiredMergePullRequestByThreeWayInputRequestTypeDef,
    _OptionalMergePullRequestByThreeWayInputRequestTypeDef,
):
    pass

MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectTypesTypeDef = TypedDict(
    "ObjectTypesTypeDef",
    {
        "source": ObjectTypeEnumType,
        "destination": ObjectTypeEnumType,
        "base": ObjectTypeEnumType,
    },
    total=False,
)

OriginApprovalRuleTemplateTypeDef = TypedDict(
    "OriginApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
    },
    total=False,
)

OverridePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
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

_RequiredPostCommentForComparedCommitInputRequestTypeDef = TypedDict(
    "_RequiredPostCommentForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "content": str,
    },
)
_OptionalPostCommentForComparedCommitInputRequestTypeDef = TypedDict(
    "_OptionalPostCommentForComparedCommitInputRequestTypeDef",
    {
        "beforeCommitId": str,
        "location": "LocationTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)

class PostCommentForComparedCommitInputRequestTypeDef(
    _RequiredPostCommentForComparedCommitInputRequestTypeDef,
    _OptionalPostCommentForComparedCommitInputRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostCommentForPullRequestInputRequestTypeDef = TypedDict(
    "_RequiredPostCommentForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "content": str,
    },
)
_OptionalPostCommentForPullRequestInputRequestTypeDef = TypedDict(
    "_OptionalPostCommentForPullRequestInputRequestTypeDef",
    {
        "location": "LocationTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)

class PostCommentForPullRequestInputRequestTypeDef(
    _RequiredPostCommentForPullRequestInputRequestTypeDef,
    _OptionalPostCommentForPullRequestInputRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostCommentReplyInputRequestTypeDef = TypedDict(
    "_RequiredPostCommentReplyInputRequestTypeDef",
    {
        "inReplyTo": str,
        "content": str,
    },
)
_OptionalPostCommentReplyInputRequestTypeDef = TypedDict(
    "_OptionalPostCommentReplyInputRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class PostCommentReplyInputRequestTypeDef(
    _RequiredPostCommentReplyInputRequestTypeDef, _OptionalPostCommentReplyInputRequestTypeDef
):
    pass

PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "sourceCommitId": str,
        "destinationCommitId": str,
        "mergeBase": str,
    },
    total=False,
)

PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": PullRequestEventTypeType,
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
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": "MergeMetadataTypeDef",
    },
    total=False,
)

PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "mergeBase": str,
    },
    total=False,
)

PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {
        "pullRequestStatus": PullRequestStatusEnumType,
    },
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
        "pullRequestStatus": PullRequestStatusEnumType,
        "authorArn": str,
        "pullRequestTargets": List["PullRequestTargetTypeDef"],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List["ApprovalRuleTypeDef"],
    },
    total=False,
)

PutCommentReactionInputRequestTypeDef = TypedDict(
    "PutCommentReactionInputRequestTypeDef",
    {
        "commentId": str,
        "reactionValue": str,
    },
)

_RequiredPutFileEntryTypeDef = TypedDict(
    "_RequiredPutFileEntryTypeDef",
    {
        "filePath": str,
    },
)
_OptionalPutFileEntryTypeDef = TypedDict(
    "_OptionalPutFileEntryTypeDef",
    {
        "fileMode": FileModeTypeEnumType,
        "fileContent": Union[bytes, IO[bytes], StreamingBody],
        "sourceFile": "SourceFileSpecifierTypeDef",
    },
    total=False,
)

class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, _OptionalPutFileEntryTypeDef):
    pass

_RequiredPutFileInputRequestTypeDef = TypedDict(
    "_RequiredPutFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "fileContent": Union[bytes, IO[bytes], StreamingBody],
        "filePath": str,
    },
)
_OptionalPutFileInputRequestTypeDef = TypedDict(
    "_OptionalPutFileInputRequestTypeDef",
    {
        "fileMode": FileModeTypeEnumType,
        "parentCommitId": str,
        "commitMessage": str,
        "name": str,
        "email": str,
    },
    total=False,
)

class PutFileInputRequestTypeDef(
    _RequiredPutFileInputRequestTypeDef, _OptionalPutFileInputRequestTypeDef
):
    pass

PutFileOutputTypeDef = TypedDict(
    "PutFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryTriggersInputRequestTypeDef = TypedDict(
    "PutRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": List["RepositoryTriggerTypeDef"],
    },
)

PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    "ReactionValueFormatsTypeDef",
    {
        "emoji": str,
        "shortCode": str,
        "unicode": str,
    },
    total=False,
)

_RequiredReplaceContentEntryTypeDef = TypedDict(
    "_RequiredReplaceContentEntryTypeDef",
    {
        "filePath": str,
        "replacementType": ReplacementTypeEnumType,
    },
)
_OptionalReplaceContentEntryTypeDef = TypedDict(
    "_OptionalReplaceContentEntryTypeDef",
    {
        "content": Union[bytes, IO[bytes], StreamingBody],
        "fileMode": FileModeTypeEnumType,
    },
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
    "RepositoryNameIdPairTypeDef",
    {
        "repositoryName": str,
        "repositoryId": str,
    },
    total=False,
)

RepositoryTriggerExecutionFailureTypeDef = TypedDict(
    "RepositoryTriggerExecutionFailureTypeDef",
    {
        "trigger": str,
        "failureMessage": str,
    },
    total=False,
)

_RequiredRepositoryTriggerTypeDef = TypedDict(
    "_RequiredRepositoryTriggerTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": List[RepositoryTriggerEventEnumType],
    },
)
_OptionalRepositoryTriggerTypeDef = TypedDict(
    "_OptionalRepositoryTriggerTypeDef",
    {
        "customData": str,
        "branches": List[str],
    },
    total=False,
)

class RepositoryTriggerTypeDef(
    _RequiredRepositoryTriggerTypeDef, _OptionalRepositoryTriggerTypeDef
):
    pass

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

SetFileModeEntryTypeDef = TypedDict(
    "SetFileModeEntryTypeDef",
    {
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
    },
)

_RequiredSourceFileSpecifierTypeDef = TypedDict(
    "_RequiredSourceFileSpecifierTypeDef",
    {
        "filePath": str,
    },
)
_OptionalSourceFileSpecifierTypeDef = TypedDict(
    "_OptionalSourceFileSpecifierTypeDef",
    {
        "isMove": bool,
    },
    total=False,
)

class SourceFileSpecifierTypeDef(
    _RequiredSourceFileSpecifierTypeDef, _OptionalSourceFileSpecifierTypeDef
):
    pass

SubModuleTypeDef = TypedDict(
    "SubModuleTypeDef",
    {
        "commitId": str,
        "absolutePath": str,
        "relativePath": str,
    },
    total=False,
)

SymbolicLinkTypeDef = TypedDict(
    "SymbolicLinkTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "destinationReference": str,
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass

TestRepositoryTriggersInputRequestTypeDef = TypedDict(
    "TestRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": List["RepositoryTriggerTypeDef"],
    },
)

TestRepositoryTriggersOutputTypeDef = TypedDict(
    "TestRepositoryTriggersOutputTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List["RepositoryTriggerExecutionFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApprovalRuleTemplateContentInputRequestTypeDef = TypedDict(
    "_RequiredUpdateApprovalRuleTemplateContentInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "newRuleContent": str,
    },
)
_OptionalUpdateApprovalRuleTemplateContentInputRequestTypeDef = TypedDict(
    "_OptionalUpdateApprovalRuleTemplateContentInputRequestTypeDef",
    {
        "existingRuleContentSha256": str,
    },
    total=False,
)

class UpdateApprovalRuleTemplateContentInputRequestTypeDef(
    _RequiredUpdateApprovalRuleTemplateContentInputRequestTypeDef,
    _OptionalUpdateApprovalRuleTemplateContentInputRequestTypeDef,
):
    pass

UpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
    },
)

UpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateNameInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    {
        "oldApprovalRuleTemplateName": str,
        "newApprovalRuleTemplateName": str,
    },
)

UpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCommentInputRequestTypeDef = TypedDict(
    "UpdateCommentInputRequestTypeDef",
    {
        "commentId": str,
        "content": str,
    },
)

UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDefaultBranchInputRequestTypeDef = TypedDict(
    "UpdateDefaultBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "defaultBranchName": str,
    },
)

_RequiredUpdatePullRequestApprovalRuleContentInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "newRuleContent": str,
    },
)
_OptionalUpdatePullRequestApprovalRuleContentInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    {
        "existingRuleContentSha256": str,
    },
    total=False,
)

class UpdatePullRequestApprovalRuleContentInputRequestTypeDef(
    _RequiredUpdatePullRequestApprovalRuleContentInputRequestTypeDef,
    _OptionalUpdatePullRequestApprovalRuleContentInputRequestTypeDef,
):
    pass

UpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestApprovalStateInputRequestTypeDef = TypedDict(
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "approvalState": ApprovalStateType,
    },
)

UpdatePullRequestDescriptionInputRequestTypeDef = TypedDict(
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    {
        "pullRequestId": str,
        "description": str,
    },
)

UpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestStatusInputRequestTypeDef = TypedDict(
    "UpdatePullRequestStatusInputRequestTypeDef",
    {
        "pullRequestId": str,
        "pullRequestStatus": PullRequestStatusEnumType,
    },
)

UpdatePullRequestStatusOutputTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestTitleInputRequestTypeDef = TypedDict(
    "UpdatePullRequestTitleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
    },
)

UpdatePullRequestTitleOutputTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRepositoryDescriptionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRepositoryDescriptionInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalUpdateRepositoryDescriptionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRepositoryDescriptionInputRequestTypeDef",
    {
        "repositoryDescription": str,
    },
    total=False,
)

class UpdateRepositoryDescriptionInputRequestTypeDef(
    _RequiredUpdateRepositoryDescriptionInputRequestTypeDef,
    _OptionalUpdateRepositoryDescriptionInputRequestTypeDef,
):
    pass

UpdateRepositoryNameInputRequestTypeDef = TypedDict(
    "UpdateRepositoryNameInputRequestTypeDef",
    {
        "oldName": str,
        "newName": str,
    },
)

UserInfoTypeDef = TypedDict(
    "UserInfoTypeDef",
    {
        "name": str,
        "email": str,
        "date": str,
    },
    total=False,
)
