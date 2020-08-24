# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codecommit service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codecommit import CodeCommitClient

    client: CodeCommitClient = boto3.client("codecommit")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codecommit.paginator import (
    DescribePullRequestEventsPaginator,
    GetCommentsForComparedCommitPaginator,
    GetCommentsForPullRequestPaginator,
    GetDifferencesPaginator,
    ListBranchesPaginator,
    ListPullRequestsPaginator,
    ListRepositoriesPaginator,
)
from mypy_boto3_codecommit.type_defs import (
    BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef,
    BatchDescribeMergeConflictsOutputTypeDef,
    BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef,
    BatchGetCommitsOutputTypeDef,
    BatchGetRepositoriesOutputTypeDef,
    ConflictResolutionTypeDef,
    CreateApprovalRuleTemplateOutputTypeDef,
    CreateCommitOutputTypeDef,
    CreatePullRequestApprovalRuleOutputTypeDef,
    CreatePullRequestOutputTypeDef,
    CreateRepositoryOutputTypeDef,
    CreateUnreferencedMergeCommitOutputTypeDef,
    DeleteApprovalRuleTemplateOutputTypeDef,
    DeleteBranchOutputTypeDef,
    DeleteCommentContentOutputTypeDef,
    DeleteFileEntryTypeDef,
    DeleteFileOutputTypeDef,
    DeletePullRequestApprovalRuleOutputTypeDef,
    DeleteRepositoryOutputTypeDef,
    DescribeMergeConflictsOutputTypeDef,
    DescribePullRequestEventsOutputTypeDef,
    EvaluatePullRequestApprovalRulesOutputTypeDef,
    GetApprovalRuleTemplateOutputTypeDef,
    GetBlobOutputTypeDef,
    GetBranchOutputTypeDef,
    GetCommentOutputTypeDef,
    GetCommentReactionsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetCommitOutputTypeDef,
    GetDifferencesOutputTypeDef,
    GetFileOutputTypeDef,
    GetFolderOutputTypeDef,
    GetMergeCommitOutputTypeDef,
    GetMergeConflictsOutputTypeDef,
    GetMergeOptionsOutputTypeDef,
    GetPullRequestApprovalStatesOutputTypeDef,
    GetPullRequestOutputTypeDef,
    GetPullRequestOverrideStateOutputTypeDef,
    GetRepositoryOutputTypeDef,
    GetRepositoryTriggersOutputTypeDef,
    ListApprovalRuleTemplatesOutputTypeDef,
    ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesForApprovalRuleTemplateOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LocationTypeDef,
    MergeBranchesByFastForwardOutputTypeDef,
    MergeBranchesBySquashOutputTypeDef,
    MergeBranchesByThreeWayOutputTypeDef,
    MergePullRequestByFastForwardOutputTypeDef,
    MergePullRequestBySquashOutputTypeDef,
    MergePullRequestByThreeWayOutputTypeDef,
    PostCommentForComparedCommitOutputTypeDef,
    PostCommentForPullRequestOutputTypeDef,
    PostCommentReplyOutputTypeDef,
    PutFileEntryTypeDef,
    PutFileOutputTypeDef,
    PutRepositoryTriggersOutputTypeDef,
    RepositoryTriggerTypeDef,
    SetFileModeEntryTypeDef,
    TargetTypeDef,
    TestRepositoryTriggersOutputTypeDef,
    UpdateApprovalRuleTemplateContentOutputTypeDef,
    UpdateApprovalRuleTemplateDescriptionOutputTypeDef,
    UpdateApprovalRuleTemplateNameOutputTypeDef,
    UpdateCommentOutputTypeDef,
    UpdatePullRequestApprovalRuleContentOutputTypeDef,
    UpdatePullRequestDescriptionOutputTypeDef,
    UpdatePullRequestStatusOutputTypeDef,
    UpdatePullRequestTitleOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeCommitClient",)


class Exceptions:
    ActorDoesNotExistException: Type[Boto3ClientError]
    ApprovalRuleContentRequiredException: Type[Boto3ClientError]
    ApprovalRuleDoesNotExistException: Type[Boto3ClientError]
    ApprovalRuleNameAlreadyExistsException: Type[Boto3ClientError]
    ApprovalRuleNameRequiredException: Type[Boto3ClientError]
    ApprovalRuleTemplateContentRequiredException: Type[Boto3ClientError]
    ApprovalRuleTemplateDoesNotExistException: Type[Boto3ClientError]
    ApprovalRuleTemplateInUseException: Type[Boto3ClientError]
    ApprovalRuleTemplateNameAlreadyExistsException: Type[Boto3ClientError]
    ApprovalRuleTemplateNameRequiredException: Type[Boto3ClientError]
    ApprovalStateRequiredException: Type[Boto3ClientError]
    AuthorDoesNotExistException: Type[Boto3ClientError]
    BeforeCommitIdAndAfterCommitIdAreSameException: Type[Boto3ClientError]
    BlobIdDoesNotExistException: Type[Boto3ClientError]
    BlobIdRequiredException: Type[Boto3ClientError]
    BranchDoesNotExistException: Type[Boto3ClientError]
    BranchNameExistsException: Type[Boto3ClientError]
    BranchNameIsTagNameException: Type[Boto3ClientError]
    BranchNameRequiredException: Type[Boto3ClientError]
    CannotDeleteApprovalRuleFromTemplateException: Type[Boto3ClientError]
    CannotModifyApprovalRuleFromTemplateException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ClientRequestTokenRequiredException: Type[Boto3ClientError]
    CommentContentRequiredException: Type[Boto3ClientError]
    CommentContentSizeLimitExceededException: Type[Boto3ClientError]
    CommentDeletedException: Type[Boto3ClientError]
    CommentDoesNotExistException: Type[Boto3ClientError]
    CommentIdRequiredException: Type[Boto3ClientError]
    CommentNotCreatedByCallerException: Type[Boto3ClientError]
    CommitDoesNotExistException: Type[Boto3ClientError]
    CommitIdDoesNotExistException: Type[Boto3ClientError]
    CommitIdRequiredException: Type[Boto3ClientError]
    CommitIdsLimitExceededException: Type[Boto3ClientError]
    CommitIdsListRequiredException: Type[Boto3ClientError]
    CommitMessageLengthExceededException: Type[Boto3ClientError]
    CommitRequiredException: Type[Boto3ClientError]
    ConcurrentReferenceUpdateException: Type[Boto3ClientError]
    DefaultBranchCannotBeDeletedException: Type[Boto3ClientError]
    DirectoryNameConflictsWithFileNameException: Type[Boto3ClientError]
    EncryptionIntegrityChecksFailedException: Type[Boto3ClientError]
    EncryptionKeyAccessDeniedException: Type[Boto3ClientError]
    EncryptionKeyDisabledException: Type[Boto3ClientError]
    EncryptionKeyNotFoundException: Type[Boto3ClientError]
    EncryptionKeyUnavailableException: Type[Boto3ClientError]
    FileContentAndSourceFileSpecifiedException: Type[Boto3ClientError]
    FileContentRequiredException: Type[Boto3ClientError]
    FileContentSizeLimitExceededException: Type[Boto3ClientError]
    FileDoesNotExistException: Type[Boto3ClientError]
    FileEntryRequiredException: Type[Boto3ClientError]
    FileModeRequiredException: Type[Boto3ClientError]
    FileNameConflictsWithDirectoryNameException: Type[Boto3ClientError]
    FilePathConflictsWithSubmodulePathException: Type[Boto3ClientError]
    FileTooLargeException: Type[Boto3ClientError]
    FolderContentSizeLimitExceededException: Type[Boto3ClientError]
    FolderDoesNotExistException: Type[Boto3ClientError]
    IdempotencyParameterMismatchException: Type[Boto3ClientError]
    InvalidActorArnException: Type[Boto3ClientError]
    InvalidApprovalRuleContentException: Type[Boto3ClientError]
    InvalidApprovalRuleNameException: Type[Boto3ClientError]
    InvalidApprovalRuleTemplateContentException: Type[Boto3ClientError]
    InvalidApprovalRuleTemplateDescriptionException: Type[Boto3ClientError]
    InvalidApprovalRuleTemplateNameException: Type[Boto3ClientError]
    InvalidApprovalStateException: Type[Boto3ClientError]
    InvalidAuthorArnException: Type[Boto3ClientError]
    InvalidBlobIdException: Type[Boto3ClientError]
    InvalidBranchNameException: Type[Boto3ClientError]
    InvalidClientRequestTokenException: Type[Boto3ClientError]
    InvalidCommentIdException: Type[Boto3ClientError]
    InvalidCommitException: Type[Boto3ClientError]
    InvalidCommitIdException: Type[Boto3ClientError]
    InvalidConflictDetailLevelException: Type[Boto3ClientError]
    InvalidConflictResolutionException: Type[Boto3ClientError]
    InvalidConflictResolutionStrategyException: Type[Boto3ClientError]
    InvalidContinuationTokenException: Type[Boto3ClientError]
    InvalidDeletionParameterException: Type[Boto3ClientError]
    InvalidDescriptionException: Type[Boto3ClientError]
    InvalidDestinationCommitSpecifierException: Type[Boto3ClientError]
    InvalidEmailException: Type[Boto3ClientError]
    InvalidFileLocationException: Type[Boto3ClientError]
    InvalidFileModeException: Type[Boto3ClientError]
    InvalidFilePositionException: Type[Boto3ClientError]
    InvalidMaxConflictFilesException: Type[Boto3ClientError]
    InvalidMaxMergeHunksException: Type[Boto3ClientError]
    InvalidMaxResultsException: Type[Boto3ClientError]
    InvalidMergeOptionException: Type[Boto3ClientError]
    InvalidOrderException: Type[Boto3ClientError]
    InvalidOverrideStatusException: Type[Boto3ClientError]
    InvalidParentCommitIdException: Type[Boto3ClientError]
    InvalidPathException: Type[Boto3ClientError]
    InvalidPullRequestEventTypeException: Type[Boto3ClientError]
    InvalidPullRequestIdException: Type[Boto3ClientError]
    InvalidPullRequestStatusException: Type[Boto3ClientError]
    InvalidPullRequestStatusUpdateException: Type[Boto3ClientError]
    InvalidReactionUserArnException: Type[Boto3ClientError]
    InvalidReactionValueException: Type[Boto3ClientError]
    InvalidReferenceNameException: Type[Boto3ClientError]
    InvalidRelativeFileVersionEnumException: Type[Boto3ClientError]
    InvalidReplacementContentException: Type[Boto3ClientError]
    InvalidReplacementTypeException: Type[Boto3ClientError]
    InvalidRepositoryDescriptionException: Type[Boto3ClientError]
    InvalidRepositoryNameException: Type[Boto3ClientError]
    InvalidRepositoryTriggerBranchNameException: Type[Boto3ClientError]
    InvalidRepositoryTriggerCustomDataException: Type[Boto3ClientError]
    InvalidRepositoryTriggerDestinationArnException: Type[Boto3ClientError]
    InvalidRepositoryTriggerEventsException: Type[Boto3ClientError]
    InvalidRepositoryTriggerNameException: Type[Boto3ClientError]
    InvalidRepositoryTriggerRegionException: Type[Boto3ClientError]
    InvalidResourceArnException: Type[Boto3ClientError]
    InvalidRevisionIdException: Type[Boto3ClientError]
    InvalidRuleContentSha256Exception: Type[Boto3ClientError]
    InvalidSortByException: Type[Boto3ClientError]
    InvalidSourceCommitSpecifierException: Type[Boto3ClientError]
    InvalidSystemTagUsageException: Type[Boto3ClientError]
    InvalidTagKeysListException: Type[Boto3ClientError]
    InvalidTagsMapException: Type[Boto3ClientError]
    InvalidTargetBranchException: Type[Boto3ClientError]
    InvalidTargetException: Type[Boto3ClientError]
    InvalidTargetsException: Type[Boto3ClientError]
    InvalidTitleException: Type[Boto3ClientError]
    ManualMergeRequiredException: Type[Boto3ClientError]
    MaximumBranchesExceededException: Type[Boto3ClientError]
    MaximumConflictResolutionEntriesExceededException: Type[Boto3ClientError]
    MaximumFileContentToLoadExceededException: Type[Boto3ClientError]
    MaximumFileEntriesExceededException: Type[Boto3ClientError]
    MaximumItemsToCompareExceededException: Type[Boto3ClientError]
    MaximumNumberOfApprovalsExceededException: Type[Boto3ClientError]
    MaximumOpenPullRequestsExceededException: Type[Boto3ClientError]
    MaximumRepositoryNamesExceededException: Type[Boto3ClientError]
    MaximumRepositoryTriggersExceededException: Type[Boto3ClientError]
    MaximumRuleTemplatesAssociatedWithRepositoryException: Type[Boto3ClientError]
    MergeOptionRequiredException: Type[Boto3ClientError]
    MultipleConflictResolutionEntriesException: Type[Boto3ClientError]
    MultipleRepositoriesInPullRequestException: Type[Boto3ClientError]
    NameLengthExceededException: Type[Boto3ClientError]
    NoChangeException: Type[Boto3ClientError]
    NumberOfRuleTemplatesExceededException: Type[Boto3ClientError]
    NumberOfRulesExceededException: Type[Boto3ClientError]
    OverrideAlreadySetException: Type[Boto3ClientError]
    OverrideStatusRequiredException: Type[Boto3ClientError]
    ParentCommitDoesNotExistException: Type[Boto3ClientError]
    ParentCommitIdOutdatedException: Type[Boto3ClientError]
    ParentCommitIdRequiredException: Type[Boto3ClientError]
    PathDoesNotExistException: Type[Boto3ClientError]
    PathRequiredException: Type[Boto3ClientError]
    PullRequestAlreadyClosedException: Type[Boto3ClientError]
    PullRequestApprovalRulesNotSatisfiedException: Type[Boto3ClientError]
    PullRequestCannotBeApprovedByAuthorException: Type[Boto3ClientError]
    PullRequestDoesNotExistException: Type[Boto3ClientError]
    PullRequestIdRequiredException: Type[Boto3ClientError]
    PullRequestStatusRequiredException: Type[Boto3ClientError]
    PutFileEntryConflictException: Type[Boto3ClientError]
    ReactionLimitExceededException: Type[Boto3ClientError]
    ReactionValueRequiredException: Type[Boto3ClientError]
    ReferenceDoesNotExistException: Type[Boto3ClientError]
    ReferenceNameRequiredException: Type[Boto3ClientError]
    ReferenceTypeNotSupportedException: Type[Boto3ClientError]
    ReplacementContentRequiredException: Type[Boto3ClientError]
    ReplacementTypeRequiredException: Type[Boto3ClientError]
    RepositoryDoesNotExistException: Type[Boto3ClientError]
    RepositoryLimitExceededException: Type[Boto3ClientError]
    RepositoryNameExistsException: Type[Boto3ClientError]
    RepositoryNameRequiredException: Type[Boto3ClientError]
    RepositoryNamesRequiredException: Type[Boto3ClientError]
    RepositoryNotAssociatedWithPullRequestException: Type[Boto3ClientError]
    RepositoryTriggerBranchNameListRequiredException: Type[Boto3ClientError]
    RepositoryTriggerDestinationArnRequiredException: Type[Boto3ClientError]
    RepositoryTriggerEventsListRequiredException: Type[Boto3ClientError]
    RepositoryTriggerNameRequiredException: Type[Boto3ClientError]
    RepositoryTriggersListRequiredException: Type[Boto3ClientError]
    ResourceArnRequiredException: Type[Boto3ClientError]
    RestrictedSourceFileException: Type[Boto3ClientError]
    RevisionIdRequiredException: Type[Boto3ClientError]
    RevisionNotCurrentException: Type[Boto3ClientError]
    SameFileContentException: Type[Boto3ClientError]
    SamePathRequestException: Type[Boto3ClientError]
    SourceAndDestinationAreSameException: Type[Boto3ClientError]
    SourceFileOrContentRequiredException: Type[Boto3ClientError]
    TagKeysListRequiredException: Type[Boto3ClientError]
    TagPolicyException: Type[Boto3ClientError]
    TagsMapRequiredException: Type[Boto3ClientError]
    TargetRequiredException: Type[Boto3ClientError]
    TargetsRequiredException: Type[Boto3ClientError]
    TipOfSourceReferenceIsDifferentException: Type[Boto3ClientError]
    TipsDivergenceExceededException: Type[Boto3ClientError]
    TitleRequiredException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]


class CodeCommitClient:
    """
    [CodeCommit.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client)
    """

    exceptions: Exceptions

    def associate_approval_rule_template_with_repository(
        self, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        [Client.associate_approval_rule_template_with_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.associate_approval_rule_template_with_repository)
        """

    def batch_associate_approval_rule_template_with_repositories(
        self, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef:
        """
        [Client.batch_associate_approval_rule_template_with_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.batch_associate_approval_rule_template_with_repositories)
        """

    def batch_describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        maxMergeHunks: int = None,
        maxConflictFiles: int = None,
        filePaths: List[str] = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> BatchDescribeMergeConflictsOutputTypeDef:
        """
        [Client.batch_describe_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.batch_describe_merge_conflicts)
        """

    def batch_disassociate_approval_rule_template_from_repositories(
        self, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef:
        """
        [Client.batch_disassociate_approval_rule_template_from_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.batch_disassociate_approval_rule_template_from_repositories)
        """

    def batch_get_commits(
        self, commitIds: List[str], repositoryName: str
    ) -> BatchGetCommitsOutputTypeDef:
        """
        [Client.batch_get_commits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.batch_get_commits)
        """

    def batch_get_repositories(
        self, repositoryNames: List[str]
    ) -> BatchGetRepositoriesOutputTypeDef:
        """
        [Client.batch_get_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.batch_get_repositories)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.can_paginate)
        """

    def create_approval_rule_template(
        self,
        approvalRuleTemplateName: str,
        approvalRuleTemplateContent: str,
        approvalRuleTemplateDescription: str = None,
    ) -> CreateApprovalRuleTemplateOutputTypeDef:
        """
        [Client.create_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_approval_rule_template)
        """

    def create_branch(self, repositoryName: str, branchName: str, commitId: str) -> None:
        """
        [Client.create_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_branch)
        """

    def create_commit(
        self,
        repositoryName: str,
        branchName: str,
        parentCommitId: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        putFiles: List[PutFileEntryTypeDef] = None,
        deleteFiles: List["DeleteFileEntryTypeDef"] = None,
        setFileModes: List["SetFileModeEntryTypeDef"] = None,
    ) -> CreateCommitOutputTypeDef:
        """
        [Client.create_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_commit)
        """

    def create_pull_request(
        self,
        title: str,
        targets: List[TargetTypeDef],
        description: str = None,
        clientRequestToken: str = None,
    ) -> CreatePullRequestOutputTypeDef:
        """
        [Client.create_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_pull_request)
        """

    def create_pull_request_approval_rule(
        self, pullRequestId: str, approvalRuleName: str, approvalRuleContent: str
    ) -> CreatePullRequestApprovalRuleOutputTypeDef:
        """
        [Client.create_pull_request_approval_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_pull_request_approval_rule)
        """

    def create_repository(
        self, repositoryName: str, repositoryDescription: str = None, tags: Dict[str, str] = None
    ) -> CreateRepositoryOutputTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_repository)
        """

    def create_unreferenced_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None,
    ) -> CreateUnreferencedMergeCommitOutputTypeDef:
        """
        [Client.create_unreferenced_merge_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.create_unreferenced_merge_commit)
        """

    def delete_approval_rule_template(
        self, approvalRuleTemplateName: str
    ) -> DeleteApprovalRuleTemplateOutputTypeDef:
        """
        [Client.delete_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_approval_rule_template)
        """

    def delete_branch(self, repositoryName: str, branchName: str) -> DeleteBranchOutputTypeDef:
        """
        [Client.delete_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_branch)
        """

    def delete_comment_content(self, commentId: str) -> DeleteCommentContentOutputTypeDef:
        """
        [Client.delete_comment_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_comment_content)
        """

    def delete_file(
        self,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> DeleteFileOutputTypeDef:
        """
        [Client.delete_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_file)
        """

    def delete_pull_request_approval_rule(
        self, pullRequestId: str, approvalRuleName: str
    ) -> DeletePullRequestApprovalRuleOutputTypeDef:
        """
        [Client.delete_pull_request_approval_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_pull_request_approval_rule)
        """

    def delete_repository(self, repositoryName: str) -> DeleteRepositoryOutputTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.delete_repository)
        """

    def describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        filePath: str,
        maxMergeHunks: int = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> DescribeMergeConflictsOutputTypeDef:
        """
        [Client.describe_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.describe_merge_conflicts)
        """

    def describe_pull_request_events(
        self,
        pullRequestId: str,
        pullRequestEventType: Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ] = None,
        actorArn: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribePullRequestEventsOutputTypeDef:
        """
        [Client.describe_pull_request_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.describe_pull_request_events)
        """

    def disassociate_approval_rule_template_from_repository(
        self, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        [Client.disassociate_approval_rule_template_from_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.disassociate_approval_rule_template_from_repository)
        """

    def evaluate_pull_request_approval_rules(
        self, pullRequestId: str, revisionId: str
    ) -> EvaluatePullRequestApprovalRulesOutputTypeDef:
        """
        [Client.evaluate_pull_request_approval_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.evaluate_pull_request_approval_rules)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.generate_presigned_url)
        """

    def get_approval_rule_template(
        self, approvalRuleTemplateName: str
    ) -> GetApprovalRuleTemplateOutputTypeDef:
        """
        [Client.get_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_approval_rule_template)
        """

    def get_blob(self, repositoryName: str, blobId: str) -> GetBlobOutputTypeDef:
        """
        [Client.get_blob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_blob)
        """

    def get_branch(
        self, repositoryName: str = None, branchName: str = None
    ) -> GetBranchOutputTypeDef:
        """
        [Client.get_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_branch)
        """

    def get_comment(self, commentId: str) -> GetCommentOutputTypeDef:
        """
        [Client.get_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_comment)
        """

    def get_comment_reactions(
        self,
        commentId: str,
        reactionUserArn: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetCommentReactionsOutputTypeDef:
        """
        [Client.get_comment_reactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_comment_reactions)
        """

    def get_comments_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetCommentsForComparedCommitOutputTypeDef:
        """
        [Client.get_comments_for_compared_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_compared_commit)
        """

    def get_comments_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetCommentsForPullRequestOutputTypeDef:
        """
        [Client.get_comments_for_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_pull_request)
        """

    def get_commit(self, repositoryName: str, commitId: str) -> GetCommitOutputTypeDef:
        """
        [Client.get_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_commit)
        """

    def get_differences(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetDifferencesOutputTypeDef:
        """
        [Client.get_differences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_differences)
        """

    def get_file(
        self, repositoryName: str, filePath: str, commitSpecifier: str = None
    ) -> GetFileOutputTypeDef:
        """
        [Client.get_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_file)
        """

    def get_folder(
        self, repositoryName: str, folderPath: str, commitSpecifier: str = None
    ) -> GetFolderOutputTypeDef:
        """
        [Client.get_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_folder)
        """

    def get_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
    ) -> GetMergeCommitOutputTypeDef:
        """
        [Client.get_merge_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_merge_commit)
        """

    def get_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        maxConflictFiles: int = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> GetMergeConflictsOutputTypeDef:
        """
        [Client.get_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_merge_conflicts)
        """

    def get_merge_options(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
    ) -> GetMergeOptionsOutputTypeDef:
        """
        [Client.get_merge_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_merge_options)
        """

    def get_pull_request(self, pullRequestId: str) -> GetPullRequestOutputTypeDef:
        """
        [Client.get_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_pull_request)
        """

    def get_pull_request_approval_states(
        self, pullRequestId: str, revisionId: str
    ) -> GetPullRequestApprovalStatesOutputTypeDef:
        """
        [Client.get_pull_request_approval_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_approval_states)
        """

    def get_pull_request_override_state(
        self, pullRequestId: str, revisionId: str
    ) -> GetPullRequestOverrideStateOutputTypeDef:
        """
        [Client.get_pull_request_override_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_override_state)
        """

    def get_repository(self, repositoryName: str) -> GetRepositoryOutputTypeDef:
        """
        [Client.get_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_repository)
        """

    def get_repository_triggers(self, repositoryName: str) -> GetRepositoryTriggersOutputTypeDef:
        """
        [Client.get_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.get_repository_triggers)
        """

    def list_approval_rule_templates(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListApprovalRuleTemplatesOutputTypeDef:
        """
        [Client.list_approval_rule_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_approval_rule_templates)
        """

    def list_associated_approval_rule_templates_for_repository(
        self, repositoryName: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef:
        """
        [Client.list_associated_approval_rule_templates_for_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_associated_approval_rule_templates_for_repository)
        """

    def list_branches(
        self, repositoryName: str, nextToken: str = None
    ) -> ListBranchesOutputTypeDef:
        """
        [Client.list_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_branches)
        """

    def list_pull_requests(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListPullRequestsOutputTypeDef:
        """
        [Client.list_pull_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_pull_requests)
        """

    def list_repositories(
        self,
        nextToken: str = None,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
    ) -> ListRepositoriesOutputTypeDef:
        """
        [Client.list_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_repositories)
        """

    def list_repositories_for_approval_rule_template(
        self, approvalRuleTemplateName: str, nextToken: str = None, maxResults: int = None
    ) -> ListRepositoriesForApprovalRuleTemplateOutputTypeDef:
        """
        [Client.list_repositories_for_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_repositories_for_approval_rule_template)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.list_tags_for_resource)
        """

    def merge_branches_by_fast_forward(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
    ) -> MergeBranchesByFastForwardOutputTypeDef:
        """
        [Client.merge_branches_by_fast_forward documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_fast_forward)
        """

    def merge_branches_by_squash(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None,
    ) -> MergeBranchesBySquashOutputTypeDef:
        """
        [Client.merge_branches_by_squash documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_squash)
        """

    def merge_branches_by_three_way(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None,
    ) -> MergeBranchesByThreeWayOutputTypeDef:
        """
        [Client.merge_branches_by_three_way documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_three_way)
        """

    def merge_pull_request_by_fast_forward(
        self, pullRequestId: str, repositoryName: str, sourceCommitId: str = None
    ) -> MergePullRequestByFastForwardOutputTypeDef:
        """
        [Client.merge_pull_request_by_fast_forward documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_fast_forward)
        """

    def merge_pull_request_by_squash(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None,
    ) -> MergePullRequestBySquashOutputTypeDef:
        """
        [Client.merge_pull_request_by_squash documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_squash)
        """

    def merge_pull_request_by_three_way(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None,
    ) -> MergePullRequestByThreeWayOutputTypeDef:
        """
        [Client.merge_pull_request_by_three_way documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_three_way)
        """

    def override_pull_request_approval_rules(
        self, pullRequestId: str, revisionId: str, overrideStatus: Literal["OVERRIDE", "REVOKE"]
    ) -> None:
        """
        [Client.override_pull_request_approval_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.override_pull_request_approval_rules)
        """

    def post_comment_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str = None,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None,
    ) -> PostCommentForComparedCommitOutputTypeDef:
        """
        [Client.post_comment_for_compared_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_compared_commit)
        """

    def post_comment_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None,
    ) -> PostCommentForPullRequestOutputTypeDef:
        """
        [Client.post_comment_for_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_pull_request)
        """

    def post_comment_reply(
        self, inReplyTo: str, content: str, clientRequestToken: str = None
    ) -> PostCommentReplyOutputTypeDef:
        """
        [Client.post_comment_reply documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.post_comment_reply)
        """

    def put_comment_reaction(self, commentId: str, reactionValue: str) -> None:
        """
        [Client.put_comment_reaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.put_comment_reaction)
        """

    def put_file(
        self,
        repositoryName: str,
        branchName: str,
        fileContent: Union[bytes, IO[bytes]],
        filePath: str,
        fileMode: Literal["EXECUTABLE", "NORMAL", "SYMLINK"] = None,
        parentCommitId: str = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> PutFileOutputTypeDef:
        """
        [Client.put_file documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.put_file)
        """

    def put_repository_triggers(
        self, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> PutRepositoryTriggersOutputTypeDef:
        """
        [Client.put_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.put_repository_triggers)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.tag_resource)
        """

    def test_repository_triggers(
        self, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> TestRepositoryTriggersOutputTypeDef:
        """
        [Client.test_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.test_repository_triggers)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.untag_resource)
        """

    def update_approval_rule_template_content(
        self,
        approvalRuleTemplateName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None,
    ) -> UpdateApprovalRuleTemplateContentOutputTypeDef:
        """
        [Client.update_approval_rule_template_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_content)
        """

    def update_approval_rule_template_description(
        self, approvalRuleTemplateName: str, approvalRuleTemplateDescription: str
    ) -> UpdateApprovalRuleTemplateDescriptionOutputTypeDef:
        """
        [Client.update_approval_rule_template_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_description)
        """

    def update_approval_rule_template_name(
        self, oldApprovalRuleTemplateName: str, newApprovalRuleTemplateName: str
    ) -> UpdateApprovalRuleTemplateNameOutputTypeDef:
        """
        [Client.update_approval_rule_template_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_name)
        """

    def update_comment(self, commentId: str, content: str) -> UpdateCommentOutputTypeDef:
        """
        [Client.update_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_comment)
        """

    def update_default_branch(self, repositoryName: str, defaultBranchName: str) -> None:
        """
        [Client.update_default_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_default_branch)
        """

    def update_pull_request_approval_rule_content(
        self,
        pullRequestId: str,
        approvalRuleName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None,
    ) -> UpdatePullRequestApprovalRuleContentOutputTypeDef:
        """
        [Client.update_pull_request_approval_rule_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_rule_content)
        """

    def update_pull_request_approval_state(
        self, pullRequestId: str, revisionId: str, approvalState: Literal["APPROVE", "REVOKE"]
    ) -> None:
        """
        [Client.update_pull_request_approval_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_state)
        """

    def update_pull_request_description(
        self, pullRequestId: str, description: str
    ) -> UpdatePullRequestDescriptionOutputTypeDef:
        """
        [Client.update_pull_request_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_description)
        """

    def update_pull_request_status(
        self, pullRequestId: str, pullRequestStatus: Literal["OPEN", "CLOSED"]
    ) -> UpdatePullRequestStatusOutputTypeDef:
        """
        [Client.update_pull_request_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_status)
        """

    def update_pull_request_title(
        self, pullRequestId: str, title: str
    ) -> UpdatePullRequestTitleOutputTypeDef:
        """
        [Client.update_pull_request_title documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_title)
        """

    def update_repository_description(
        self, repositoryName: str, repositoryDescription: str = None
    ) -> None:
        """
        [Client.update_repository_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_repository_description)
        """

    def update_repository_name(self, oldName: str, newName: str) -> None:
        """
        [Client.update_repository_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Client.update_repository_name)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pull_request_events"]
    ) -> DescribePullRequestEventsPaginator:
        """
        [Paginator.DescribePullRequestEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_compared_commit"]
    ) -> GetCommentsForComparedCommitPaginator:
        """
        [Paginator.GetCommentsForComparedCommit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_pull_request"]
    ) -> GetCommentsForPullRequestPaginator:
        """
        [Paginator.GetCommentsForPullRequest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_differences"]) -> GetDifferencesPaginator:
        """
        [Paginator.GetDifferences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_branches"]) -> ListBranchesPaginator:
        """
        [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pull_requests"]
    ) -> ListPullRequestsPaginator:
        """
        [Paginator.ListPullRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
