"""
Type annotations for codeguru-reviewer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.literals import AnalysisTypeType

    data: AnalysisTypeType = "CodeQuality"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalysisTypeType",
    "CodeReviewCompletedWaiterName",
    "EncryptionOptionType",
    "JobStateType",
    "ListRepositoryAssociationsPaginatorName",
    "ProviderTypeType",
    "ReactionType",
    "RecommendationCategoryType",
    "RepositoryAssociationStateType",
    "RepositoryAssociationSucceededWaiterName",
    "TypeType",
    "VendorNameType",
)

AnalysisTypeType = Literal["CodeQuality", "Security"]
CodeReviewCompletedWaiterName = Literal["code_review_completed"]
EncryptionOptionType = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
JobStateType = Literal["Completed", "Deleting", "Failed", "Pending"]
ListRepositoryAssociationsPaginatorName = Literal["list_repository_associations"]
ProviderTypeType = Literal[
    "Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer", "S3Bucket"
]
ReactionType = Literal["ThumbsDown", "ThumbsUp"]
RecommendationCategoryType = Literal[
    "AWSBestPractices",
    "AWSCloudFormationIssues",
    "CodeMaintenanceIssues",
    "ConcurrencyIssues",
    "DuplicateCode",
    "InputValidations",
    "JavaBestPractices",
    "PythonBestPractices",
    "ResourceLeaks",
    "SecurityIssues",
]
RepositoryAssociationStateType = Literal[
    "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
]
RepositoryAssociationSucceededWaiterName = Literal["repository_association_succeeded"]
TypeType = Literal["PullRequest", "RepositoryAnalysis"]
VendorNameType = Literal["GitHub", "GitLab", "NativeS3"]
