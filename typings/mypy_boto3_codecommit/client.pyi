"""
Type annotations for codecommit service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codecommit import CodeCommitClient

    client: CodeCommitClient = boto3.client("codecommit")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ApprovalStateType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    SortByEnumType,
)
from .paginator import (
    DescribePullRequestEventsPaginator,
    GetCommentsForComparedCommitPaginator,
    GetCommentsForPullRequestPaginator,
    GetDifferencesPaginator,
    ListBranchesPaginator,
    ListPullRequestsPaginator,
    ListRepositoriesPaginator,
)
from .type_defs import (
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

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActorDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleContentRequiredException: Type[BotocoreClientError]
    ApprovalRuleDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleNameAlreadyExistsException: Type[BotocoreClientError]
    ApprovalRuleNameRequiredException: Type[BotocoreClientError]
    ApprovalRuleTemplateContentRequiredException: Type[BotocoreClientError]
    ApprovalRuleTemplateDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleTemplateInUseException: Type[BotocoreClientError]
    ApprovalRuleTemplateNameAlreadyExistsException: Type[BotocoreClientError]
    ApprovalRuleTemplateNameRequiredException: Type[BotocoreClientError]
    ApprovalStateRequiredException: Type[BotocoreClientError]
    AuthorDoesNotExistException: Type[BotocoreClientError]
    BeforeCommitIdAndAfterCommitIdAreSameException: Type[BotocoreClientError]
    BlobIdDoesNotExistException: Type[BotocoreClientError]
    BlobIdRequiredException: Type[BotocoreClientError]
    BranchDoesNotExistException: Type[BotocoreClientError]
    BranchNameExistsException: Type[BotocoreClientError]
    BranchNameIsTagNameException: Type[BotocoreClientError]
    BranchNameRequiredException: Type[BotocoreClientError]
    CannotDeleteApprovalRuleFromTemplateException: Type[BotocoreClientError]
    CannotModifyApprovalRuleFromTemplateException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientRequestTokenRequiredException: Type[BotocoreClientError]
    CommentContentRequiredException: Type[BotocoreClientError]
    CommentContentSizeLimitExceededException: Type[BotocoreClientError]
    CommentDeletedException: Type[BotocoreClientError]
    CommentDoesNotExistException: Type[BotocoreClientError]
    CommentIdRequiredException: Type[BotocoreClientError]
    CommentNotCreatedByCallerException: Type[BotocoreClientError]
    CommitDoesNotExistException: Type[BotocoreClientError]
    CommitIdDoesNotExistException: Type[BotocoreClientError]
    CommitIdRequiredException: Type[BotocoreClientError]
    CommitIdsLimitExceededException: Type[BotocoreClientError]
    CommitIdsListRequiredException: Type[BotocoreClientError]
    CommitMessageLengthExceededException: Type[BotocoreClientError]
    CommitRequiredException: Type[BotocoreClientError]
    ConcurrentReferenceUpdateException: Type[BotocoreClientError]
    DefaultBranchCannotBeDeletedException: Type[BotocoreClientError]
    DirectoryNameConflictsWithFileNameException: Type[BotocoreClientError]
    EncryptionIntegrityChecksFailedException: Type[BotocoreClientError]
    EncryptionKeyAccessDeniedException: Type[BotocoreClientError]
    EncryptionKeyDisabledException: Type[BotocoreClientError]
    EncryptionKeyNotFoundException: Type[BotocoreClientError]
    EncryptionKeyUnavailableException: Type[BotocoreClientError]
    FileContentAndSourceFileSpecifiedException: Type[BotocoreClientError]
    FileContentRequiredException: Type[BotocoreClientError]
    FileContentSizeLimitExceededException: Type[BotocoreClientError]
    FileDoesNotExistException: Type[BotocoreClientError]
    FileEntryRequiredException: Type[BotocoreClientError]
    FileModeRequiredException: Type[BotocoreClientError]
    FileNameConflictsWithDirectoryNameException: Type[BotocoreClientError]
    FilePathConflictsWithSubmodulePathException: Type[BotocoreClientError]
    FileTooLargeException: Type[BotocoreClientError]
    FolderContentSizeLimitExceededException: Type[BotocoreClientError]
    FolderDoesNotExistException: Type[BotocoreClientError]
    IdempotencyParameterMismatchException: Type[BotocoreClientError]
    InvalidActorArnException: Type[BotocoreClientError]
    InvalidApprovalRuleContentException: Type[BotocoreClientError]
    InvalidApprovalRuleNameException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateContentException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateDescriptionException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateNameException: Type[BotocoreClientError]
    InvalidApprovalStateException: Type[BotocoreClientError]
    InvalidAuthorArnException: Type[BotocoreClientError]
    InvalidBlobIdException: Type[BotocoreClientError]
    InvalidBranchNameException: Type[BotocoreClientError]
    InvalidClientRequestTokenException: Type[BotocoreClientError]
    InvalidCommentIdException: Type[BotocoreClientError]
    InvalidCommitException: Type[BotocoreClientError]
    InvalidCommitIdException: Type[BotocoreClientError]
    InvalidConflictDetailLevelException: Type[BotocoreClientError]
    InvalidConflictResolutionException: Type[BotocoreClientError]
    InvalidConflictResolutionStrategyException: Type[BotocoreClientError]
    InvalidContinuationTokenException: Type[BotocoreClientError]
    InvalidDeletionParameterException: Type[BotocoreClientError]
    InvalidDescriptionException: Type[BotocoreClientError]
    InvalidDestinationCommitSpecifierException: Type[BotocoreClientError]
    InvalidEmailException: Type[BotocoreClientError]
    InvalidFileLocationException: Type[BotocoreClientError]
    InvalidFileModeException: Type[BotocoreClientError]
    InvalidFilePositionException: Type[BotocoreClientError]
    InvalidMaxConflictFilesException: Type[BotocoreClientError]
    InvalidMaxMergeHunksException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidMergeOptionException: Type[BotocoreClientError]
    InvalidOrderException: Type[BotocoreClientError]
    InvalidOverrideStatusException: Type[BotocoreClientError]
    InvalidParentCommitIdException: Type[BotocoreClientError]
    InvalidPathException: Type[BotocoreClientError]
    InvalidPullRequestEventTypeException: Type[BotocoreClientError]
    InvalidPullRequestIdException: Type[BotocoreClientError]
    InvalidPullRequestStatusException: Type[BotocoreClientError]
    InvalidPullRequestStatusUpdateException: Type[BotocoreClientError]
    InvalidReactionUserArnException: Type[BotocoreClientError]
    InvalidReactionValueException: Type[BotocoreClientError]
    InvalidReferenceNameException: Type[BotocoreClientError]
    InvalidRelativeFileVersionEnumException: Type[BotocoreClientError]
    InvalidReplacementContentException: Type[BotocoreClientError]
    InvalidReplacementTypeException: Type[BotocoreClientError]
    InvalidRepositoryDescriptionException: Type[BotocoreClientError]
    InvalidRepositoryNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerBranchNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerCustomDataException: Type[BotocoreClientError]
    InvalidRepositoryTriggerDestinationArnException: Type[BotocoreClientError]
    InvalidRepositoryTriggerEventsException: Type[BotocoreClientError]
    InvalidRepositoryTriggerNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerRegionException: Type[BotocoreClientError]
    InvalidResourceArnException: Type[BotocoreClientError]
    InvalidRevisionIdException: Type[BotocoreClientError]
    InvalidRuleContentSha256Exception: Type[BotocoreClientError]
    InvalidSortByException: Type[BotocoreClientError]
    InvalidSourceCommitSpecifierException: Type[BotocoreClientError]
    InvalidSystemTagUsageException: Type[BotocoreClientError]
    InvalidTagKeysListException: Type[BotocoreClientError]
    InvalidTagsMapException: Type[BotocoreClientError]
    InvalidTargetBranchException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    InvalidTargetsException: Type[BotocoreClientError]
    InvalidTitleException: Type[BotocoreClientError]
    ManualMergeRequiredException: Type[BotocoreClientError]
    MaximumBranchesExceededException: Type[BotocoreClientError]
    MaximumConflictResolutionEntriesExceededException: Type[BotocoreClientError]
    MaximumFileContentToLoadExceededException: Type[BotocoreClientError]
    MaximumFileEntriesExceededException: Type[BotocoreClientError]
    MaximumItemsToCompareExceededException: Type[BotocoreClientError]
    MaximumNumberOfApprovalsExceededException: Type[BotocoreClientError]
    MaximumOpenPullRequestsExceededException: Type[BotocoreClientError]
    MaximumRepositoryNamesExceededException: Type[BotocoreClientError]
    MaximumRepositoryTriggersExceededException: Type[BotocoreClientError]
    MaximumRuleTemplatesAssociatedWithRepositoryException: Type[BotocoreClientError]
    MergeOptionRequiredException: Type[BotocoreClientError]
    MultipleConflictResolutionEntriesException: Type[BotocoreClientError]
    MultipleRepositoriesInPullRequestException: Type[BotocoreClientError]
    NameLengthExceededException: Type[BotocoreClientError]
    NoChangeException: Type[BotocoreClientError]
    NumberOfRuleTemplatesExceededException: Type[BotocoreClientError]
    NumberOfRulesExceededException: Type[BotocoreClientError]
    OverrideAlreadySetException: Type[BotocoreClientError]
    OverrideStatusRequiredException: Type[BotocoreClientError]
    ParentCommitDoesNotExistException: Type[BotocoreClientError]
    ParentCommitIdOutdatedException: Type[BotocoreClientError]
    ParentCommitIdRequiredException: Type[BotocoreClientError]
    PathDoesNotExistException: Type[BotocoreClientError]
    PathRequiredException: Type[BotocoreClientError]
    PullRequestAlreadyClosedException: Type[BotocoreClientError]
    PullRequestApprovalRulesNotSatisfiedException: Type[BotocoreClientError]
    PullRequestCannotBeApprovedByAuthorException: Type[BotocoreClientError]
    PullRequestDoesNotExistException: Type[BotocoreClientError]
    PullRequestIdRequiredException: Type[BotocoreClientError]
    PullRequestStatusRequiredException: Type[BotocoreClientError]
    PutFileEntryConflictException: Type[BotocoreClientError]
    ReactionLimitExceededException: Type[BotocoreClientError]
    ReactionValueRequiredException: Type[BotocoreClientError]
    ReferenceDoesNotExistException: Type[BotocoreClientError]
    ReferenceNameRequiredException: Type[BotocoreClientError]
    ReferenceTypeNotSupportedException: Type[BotocoreClientError]
    ReplacementContentRequiredException: Type[BotocoreClientError]
    ReplacementTypeRequiredException: Type[BotocoreClientError]
    RepositoryDoesNotExistException: Type[BotocoreClientError]
    RepositoryLimitExceededException: Type[BotocoreClientError]
    RepositoryNameExistsException: Type[BotocoreClientError]
    RepositoryNameRequiredException: Type[BotocoreClientError]
    RepositoryNamesRequiredException: Type[BotocoreClientError]
    RepositoryNotAssociatedWithPullRequestException: Type[BotocoreClientError]
    RepositoryTriggerBranchNameListRequiredException: Type[BotocoreClientError]
    RepositoryTriggerDestinationArnRequiredException: Type[BotocoreClientError]
    RepositoryTriggerEventsListRequiredException: Type[BotocoreClientError]
    RepositoryTriggerNameRequiredException: Type[BotocoreClientError]
    RepositoryTriggersListRequiredException: Type[BotocoreClientError]
    ResourceArnRequiredException: Type[BotocoreClientError]
    RestrictedSourceFileException: Type[BotocoreClientError]
    RevisionIdRequiredException: Type[BotocoreClientError]
    RevisionNotCurrentException: Type[BotocoreClientError]
    SameFileContentException: Type[BotocoreClientError]
    SamePathRequestException: Type[BotocoreClientError]
    SourceAndDestinationAreSameException: Type[BotocoreClientError]
    SourceFileOrContentRequiredException: Type[BotocoreClientError]
    TagKeysListRequiredException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    TagsMapRequiredException: Type[BotocoreClientError]
    TargetRequiredException: Type[BotocoreClientError]
    TargetsRequiredException: Type[BotocoreClientError]
    TipOfSourceReferenceIsDifferentException: Type[BotocoreClientError]
    TipsDivergenceExceededException: Type[BotocoreClientError]
    TitleRequiredException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class CodeCommitClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeCommitClient exceptions.
        """
    def associate_approval_rule_template_with_repository(
        self, *, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        Creates an association between an approval rule template and a specified
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.associate_approval_rule_template_with_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#associate_approval_rule_template_with_repository)
        """
    def batch_associate_approval_rule_template_with_repositories(
        self, *, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef:
        """
        Creates an association between an approval rule template and one or more
        specified repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.batch_associate_approval_rule_template_with_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_associate_approval_rule_template_with_repositories)
        """
    def batch_describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        maxMergeHunks: int = None,
        maxConflictFiles: int = None,
        filePaths: List[str] = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> BatchDescribeMergeConflictsOutputTypeDef:
        """
        Returns information about one or more merge conflicts in the attempted merge of
        two commit specifiers using the squash or three-way merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.batch_describe_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_describe_merge_conflicts)
        """
    def batch_disassociate_approval_rule_template_from_repositories(
        self, *, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef:
        """
        Removes the association between an approval rule template and one or more
        specified repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.batch_disassociate_approval_rule_template_from_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_disassociate_approval_rule_template_from_repositories)
        """
    def batch_get_commits(
        self, *, commitIds: List[str], repositoryName: str
    ) -> BatchGetCommitsOutputTypeDef:
        """
        Returns information about the contents of one or more commits in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.batch_get_commits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_get_commits)
        """
    def batch_get_repositories(
        self, *, repositoryNames: List[str]
    ) -> BatchGetRepositoriesOutputTypeDef:
        """
        Returns information about one or more repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.batch_get_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_get_repositories)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#close)
        """
    def create_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
        approvalRuleTemplateContent: str,
        approvalRuleTemplateDescription: str = None
    ) -> CreateApprovalRuleTemplateOutputTypeDef:
        """
        Creates a template for approval rules that can then be associated with one or
        more repositories in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_approval_rule_template)
        """
    def create_branch(self, *, repositoryName: str, branchName: str, commitId: str) -> None:
        """
        Creates a branch in a repository and points the branch to a commit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_branch)
        """
    def create_commit(
        self,
        *,
        repositoryName: str,
        branchName: str,
        parentCommitId: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        putFiles: List["PutFileEntryTypeDef"] = None,
        deleteFiles: List["DeleteFileEntryTypeDef"] = None,
        setFileModes: List["SetFileModeEntryTypeDef"] = None
    ) -> CreateCommitOutputTypeDef:
        """
        Creates a commit for a repository on the tip of a specified branch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_commit)
        """
    def create_pull_request(
        self,
        *,
        title: str,
        targets: List["TargetTypeDef"],
        description: str = None,
        clientRequestToken: str = None
    ) -> CreatePullRequestOutputTypeDef:
        """
        Creates a pull request in the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_pull_request)
        """
    def create_pull_request_approval_rule(
        self, *, pullRequestId: str, approvalRuleName: str, approvalRuleContent: str
    ) -> CreatePullRequestApprovalRuleOutputTypeDef:
        """
        Creates an approval rule for a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_pull_request_approval_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_pull_request_approval_rule)
        """
    def create_repository(
        self, *, repositoryName: str, repositoryDescription: str = None, tags: Dict[str, str] = None
    ) -> CreateRepositoryOutputTypeDef:
        """
        Creates a new, empty repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_repository)
        """
    def create_unreferenced_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: "ConflictResolutionTypeDef" = None
    ) -> CreateUnreferencedMergeCommitOutputTypeDef:
        """
        Creates an unreferenced commit that represents the result of merging two
        branches using a specified merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.create_unreferenced_merge_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_unreferenced_merge_commit)
        """
    def delete_approval_rule_template(
        self, *, approvalRuleTemplateName: str
    ) -> DeleteApprovalRuleTemplateOutputTypeDef:
        """
        Deletes a specified approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_approval_rule_template)
        """
    def delete_branch(self, *, repositoryName: str, branchName: str) -> DeleteBranchOutputTypeDef:
        """
        Deletes a branch from a repository, unless that branch is the default branch for
        the repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_branch)
        """
    def delete_comment_content(self, *, commentId: str) -> DeleteCommentContentOutputTypeDef:
        """
        Deletes the content of a comment made on a change, file, or commit in a
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_comment_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_comment_content)
        """
    def delete_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None
    ) -> DeleteFileOutputTypeDef:
        """
        Deletes a specified file from a specified branch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_file)
        """
    def delete_pull_request_approval_rule(
        self, *, pullRequestId: str, approvalRuleName: str
    ) -> DeletePullRequestApprovalRuleOutputTypeDef:
        """
        Deletes an approval rule from a specified pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_pull_request_approval_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_pull_request_approval_rule)
        """
    def delete_repository(self, *, repositoryName: str) -> DeleteRepositoryOutputTypeDef:
        """
        Deletes a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.delete_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_repository)
        """
    def describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        filePath: str,
        maxMergeHunks: int = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> DescribeMergeConflictsOutputTypeDef:
        """
        Returns information about one or more merge conflicts in the attempted merge of
        two commit specifiers using the squash or three-way merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.describe_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#describe_merge_conflicts)
        """
    def describe_pull_request_events(
        self,
        *,
        pullRequestId: str,
        pullRequestEventType: PullRequestEventTypeType = None,
        actorArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribePullRequestEventsOutputTypeDef:
        """
        Returns information about one or more pull request events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.describe_pull_request_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#describe_pull_request_events)
        """
    def disassociate_approval_rule_template_from_repository(
        self, *, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        Removes the association between a template and a repository so that approval
        rules based on the template are not automatically created when pull requests are
        created in the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.disassociate_approval_rule_template_from_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#disassociate_approval_rule_template_from_repository)
        """
    def evaluate_pull_request_approval_rules(
        self, *, pullRequestId: str, revisionId: str
    ) -> EvaluatePullRequestApprovalRulesOutputTypeDef:
        """
        Evaluates whether a pull request has met all the conditions specified in its
        associated approval rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.evaluate_pull_request_approval_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#evaluate_pull_request_approval_rules)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#generate_presigned_url)
        """
    def get_approval_rule_template(
        self, *, approvalRuleTemplateName: str
    ) -> GetApprovalRuleTemplateOutputTypeDef:
        """
        Returns information about a specified approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_approval_rule_template)
        """
    def get_blob(self, *, repositoryName: str, blobId: str) -> GetBlobOutputTypeDef:
        """
        Returns the base-64 encoded content of an individual blob in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_blob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_blob)
        """
    def get_branch(
        self, *, repositoryName: str = None, branchName: str = None
    ) -> GetBranchOutputTypeDef:
        """
        Returns information about a repository branch, including its name and the last
        commit ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_branch)
        """
    def get_comment(self, *, commentId: str) -> GetCommentOutputTypeDef:
        """
        Returns the content of a comment made on a change, file, or commit in a
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comment)
        """
    def get_comment_reactions(
        self,
        *,
        commentId: str,
        reactionUserArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentReactionsOutputTypeDef:
        """
        Returns information about reactions to a specified comment ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_comment_reactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comment_reactions)
        """
    def get_comments_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentsForComparedCommitOutputTypeDef:
        """
        Returns information about comments made on the comparison between two commits.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_compared_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comments_for_compared_commit)
        """
    def get_comments_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentsForPullRequestOutputTypeDef:
        """
        Returns comments made on a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comments_for_pull_request)
        """
    def get_commit(self, *, repositoryName: str, commitId: str) -> GetCommitOutputTypeDef:
        """
        Returns information about a commit, including commit message and committer
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_commit)
        """
    def get_differences(
        self,
        *,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetDifferencesOutputTypeDef:
        """
        Returns information about the differences in a valid commit specifier (such as a
        branch, tag, HEAD, commit ID, or other fully qualified reference).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_differences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_differences)
        """
    def get_file(
        self, *, repositoryName: str, filePath: str, commitSpecifier: str = None
    ) -> GetFileOutputTypeDef:
        """
        Returns the base-64 encoded contents of a specified file and its metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_file)
        """
    def get_folder(
        self, *, repositoryName: str, folderPath: str, commitSpecifier: str = None
    ) -> GetFolderOutputTypeDef:
        """
        Returns the contents of a specified folder in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_folder)
        """
    def get_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None
    ) -> GetMergeCommitOutputTypeDef:
        """
        Returns information about a specified merge commit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_merge_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_commit)
        """
    def get_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        maxConflictFiles: int = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> GetMergeConflictsOutputTypeDef:
        """
        Returns information about merge conflicts between the before and after commit
        IDs for a pull request in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_conflicts)
        """
    def get_merge_options(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None
    ) -> GetMergeOptionsOutputTypeDef:
        """
        Returns information about the merge options available for merging two specified
        branches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_merge_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_options)
        """
    def get_pull_request(self, *, pullRequestId: str) -> GetPullRequestOutputTypeDef:
        """
        Gets information about a pull request in a specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request)
        """
    def get_pull_request_approval_states(
        self, *, pullRequestId: str, revisionId: str
    ) -> GetPullRequestApprovalStatesOutputTypeDef:
        """
        Gets information about the approval states for a specified pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_approval_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request_approval_states)
        """
    def get_pull_request_override_state(
        self, *, pullRequestId: str, revisionId: str
    ) -> GetPullRequestOverrideStateOutputTypeDef:
        """
        Returns information about whether approval rules have been set aside
        (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of
        the user or identity that overrode the rules and their requirements for the pull
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_override_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request_override_state)
        """
    def get_repository(self, *, repositoryName: str) -> GetRepositoryOutputTypeDef:
        """
        Returns information about a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_repository)
        """
    def get_repository_triggers(self, *, repositoryName: str) -> GetRepositoryTriggersOutputTypeDef:
        """
        Gets information about triggers configured for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.get_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_repository_triggers)
        """
    def list_approval_rule_templates(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListApprovalRuleTemplatesOutputTypeDef:
        """
        Lists all approval rule templates in the specified AWS Region in your AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_approval_rule_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_approval_rule_templates)
        """
    def list_associated_approval_rule_templates_for_repository(
        self, *, repositoryName: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef:
        """
        Lists all approval rule templates that are associated with a specified
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_associated_approval_rule_templates_for_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_associated_approval_rule_templates_for_repository)
        """
    def list_branches(
        self, *, repositoryName: str, nextToken: str = None
    ) -> ListBranchesOutputTypeDef:
        """
        Gets information about one or more branches in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_branches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_branches)
        """
    def list_pull_requests(
        self,
        *,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: PullRequestStatusEnumType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListPullRequestsOutputTypeDef:
        """
        Returns a list of pull requests for a specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_pull_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_pull_requests)
        """
    def list_repositories(
        self, *, nextToken: str = None, sortBy: SortByEnumType = None, order: OrderEnumType = None
    ) -> ListRepositoriesOutputTypeDef:
        """
        Gets information about one or more repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_repositories)
        """
    def list_repositories_for_approval_rule_template(
        self, *, approvalRuleTemplateName: str, nextToken: str = None, maxResults: int = None
    ) -> ListRepositoriesForApprovalRuleTemplateOutputTypeDef:
        """
        Lists all repositories associated with the specified approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_repositories_for_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_repositories_for_approval_rule_template)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Gets information about AWS tags for a specified Amazon Resource Name (ARN) in
        AWS CodeCommit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_tags_for_resource)
        """
    def merge_branches_by_fast_forward(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None
    ) -> MergeBranchesByFastForwardOutputTypeDef:
        """
        Merges two branches using the fast-forward merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_fast_forward)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_fast_forward)
        """
    def merge_branches_by_squash(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: "ConflictResolutionTypeDef" = None
    ) -> MergeBranchesBySquashOutputTypeDef:
        """
        Merges two branches using the squash merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_squash)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_squash)
        """
    def merge_branches_by_three_way(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: "ConflictResolutionTypeDef" = None
    ) -> MergeBranchesByThreeWayOutputTypeDef:
        """
        Merges two specified branches using the three-way merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_three_way)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_three_way)
        """
    def merge_pull_request_by_fast_forward(
        self, *, pullRequestId: str, repositoryName: str, sourceCommitId: str = None
    ) -> MergePullRequestByFastForwardOutputTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified
        destination branch for that pull request at the specified commit using the fast-
        forward merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_fast_forward)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_fast_forward)
        """
    def merge_pull_request_by_squash(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: "ConflictResolutionTypeDef" = None
    ) -> MergePullRequestBySquashOutputTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified
        destination branch for that pull request at the specified commit using the
        squash merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_squash)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_squash)
        """
    def merge_pull_request_by_three_way(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: "ConflictResolutionTypeDef" = None
    ) -> MergePullRequestByThreeWayOutputTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified
        destination branch for that pull request at the specified commit using the
        three-way merge strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_three_way)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_three_way)
        """
    def override_pull_request_approval_rules(
        self, *, pullRequestId: str, revisionId: str, overrideStatus: OverrideStatusType
    ) -> None:
        """
        Sets aside (overrides) all approval rule requirements for a specified pull
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.override_pull_request_approval_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#override_pull_request_approval_rules)
        """
    def post_comment_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str = None,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None
    ) -> PostCommentForComparedCommitOutputTypeDef:
        """
        Posts a comment on the comparison between two commits.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_compared_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_for_compared_commit)
        """
    def post_comment_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None
    ) -> PostCommentForPullRequestOutputTypeDef:
        """
        Posts a comment on a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_for_pull_request)
        """
    def post_comment_reply(
        self, *, inReplyTo: str, content: str, clientRequestToken: str = None
    ) -> PostCommentReplyOutputTypeDef:
        """
        Posts a comment in reply to an existing comment on a comparison between commits
        or a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.post_comment_reply)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_reply)
        """
    def put_comment_reaction(self, *, commentId: str, reactionValue: str) -> None:
        """
        Adds or updates a reaction to a specified comment for the user whose identity is
        used to make the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.put_comment_reaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_comment_reaction)
        """
    def put_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        fileContent: Union[bytes, IO[bytes], StreamingBody],
        filePath: str,
        fileMode: FileModeTypeEnumType = None,
        parentCommitId: str = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None
    ) -> PutFileOutputTypeDef:
        """
        Adds or updates a file in a branch in an AWS CodeCommit repository, and
        generates a commit for the addition in the specified branch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.put_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_file)
        """
    def put_repository_triggers(
        self, *, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> PutRepositoryTriggersOutputTypeDef:
        """
        Replaces all triggers for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.put_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_repository_triggers)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or updates tags for a resource in AWS CodeCommit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#tag_resource)
        """
    def test_repository_triggers(
        self, *, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> TestRepositoryTriggersOutputTypeDef:
        """
        Tests the functionality of repository triggers by sending information to the
        trigger target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.test_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#test_repository_triggers)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes tags for a resource in AWS CodeCommit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#untag_resource)
        """
    def update_approval_rule_template_content(
        self,
        *,
        approvalRuleTemplateName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None
    ) -> UpdateApprovalRuleTemplateContentOutputTypeDef:
        """
        Updates the content of an approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_content)
        """
    def update_approval_rule_template_description(
        self, *, approvalRuleTemplateName: str, approvalRuleTemplateDescription: str
    ) -> UpdateApprovalRuleTemplateDescriptionOutputTypeDef:
        """
        Updates the description for a specified approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_description)
        """
    def update_approval_rule_template_name(
        self, *, oldApprovalRuleTemplateName: str, newApprovalRuleTemplateName: str
    ) -> UpdateApprovalRuleTemplateNameOutputTypeDef:
        """
        Updates the name of a specified approval rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_name)
        """
    def update_comment(self, *, commentId: str, content: str) -> UpdateCommentOutputTypeDef:
        """
        Replaces the contents of a comment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_comment)
        """
    def update_default_branch(self, *, repositoryName: str, defaultBranchName: str) -> None:
        """
        Sets or changes the default branch name for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_default_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_default_branch)
        """
    def update_pull_request_approval_rule_content(
        self,
        *,
        pullRequestId: str,
        approvalRuleName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None
    ) -> UpdatePullRequestApprovalRuleContentOutputTypeDef:
        """
        Updates the structure of an approval rule created specifically for a pull
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_rule_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_approval_rule_content)
        """
    def update_pull_request_approval_state(
        self, *, pullRequestId: str, revisionId: str, approvalState: ApprovalStateType
    ) -> None:
        """
        Updates the state of a user's approval on a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_approval_state)
        """
    def update_pull_request_description(
        self, *, pullRequestId: str, description: str
    ) -> UpdatePullRequestDescriptionOutputTypeDef:
        """
        Replaces the contents of the description of a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_description)
        """
    def update_pull_request_status(
        self, *, pullRequestId: str, pullRequestStatus: PullRequestStatusEnumType
    ) -> UpdatePullRequestStatusOutputTypeDef:
        """
        Updates the status of a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_status)
        """
    def update_pull_request_title(
        self, *, pullRequestId: str, title: str
    ) -> UpdatePullRequestTitleOutputTypeDef:
        """
        Replaces the title of a pull request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_title)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_title)
        """
    def update_repository_description(
        self, *, repositoryName: str, repositoryDescription: str = None
    ) -> None:
        """
        Sets or changes the comment or description for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_repository_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_repository_description)
        """
    def update_repository_name(self, *, oldName: str, newName: str) -> None:
        """
        Renames a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Client.update_repository_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_repository_name)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pull_request_events"]
    ) -> DescribePullRequestEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#describepullrequesteventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_compared_commit"]
    ) -> GetCommentsForComparedCommitPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforcomparedcommitpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_pull_request"]
    ) -> GetCommentsForPullRequestPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforpullrequestpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_differences"]) -> GetDifferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getdifferencespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_branches"]) -> ListBranchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listbranchespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pull_requests"]
    ) -> ListPullRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listpullrequestspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listrepositoriespaginator)
        """
