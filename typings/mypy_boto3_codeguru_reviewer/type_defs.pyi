"""
Main interface for codeguru-reviewer service type definitions.

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import CodeCommitRepositoryTypeDef

    data: CodeCommitRepositoryTypeDef = {...}
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
    "CodeCommitRepositoryTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "RecommendationFeedbackTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryAnalysisTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "RepositoryAssociationTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "SourceCodeTypeTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "AssociateRepositoryResponseTypeDef",
    "CodeReviewTypeTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RepositoryTypeDef",
)

CodeCommitRepositoryTypeDef = TypedDict("CodeCommitRepositoryTypeDef", {"Name": str})

CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"],
        "State": Literal["Completed", "Pending", "Failed", "Deleting"],
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": Literal["PullRequest", "RepositoryAnalysis"],
        "PullRequestId": str,
        "MetricsSummary": "MetricsSummaryTypeDef",
    },
    total=False,
)

CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"],
        "State": Literal["Completed", "Pending", "Failed", "Deleting"],
        "StateReason": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": Literal["PullRequest", "RepositoryAnalysis"],
        "PullRequestId": str,
        "SourceCodeType": "SourceCodeTypeTypeDef",
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)

CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef", {"SourceCommit": str, "DestinationCommit": str}, total=False
)

MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef", {"MeteredLinesOfCodeCount": int, "FindingsCount": int}, total=False
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef", {"MeteredLinesOfCodeCount": int, "FindingsCount": int}, total=False
)

RecommendationFeedbackSummaryTypeDef = TypedDict(
    "RecommendationFeedbackSummaryTypeDef",
    {"RecommendationId": str, "Reactions": List[Literal["ThumbsUp", "ThumbsDown"]], "UserId": str},
    total=False,
)

RecommendationFeedbackTypeDef = TypedDict(
    "RecommendationFeedbackTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": List[Literal["ThumbsUp", "ThumbsDown"]],
        "UserId": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "FilePath": str,
        "RecommendationId": str,
        "StartLine": int,
        "EndLine": int,
        "Description": str,
    },
    total=False,
)

RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef", {"RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef"}
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": str,
        "ConnectionArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "ConnectionArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

RepositoryHeadSourceCodeTypeTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeTypeDef", {"BranchName": str}
)

SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": "CommitDiffSourceCodeTypeTypeDef",
        "RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef",
    },
    total=False,
)

ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef", {"Name": str, "ConnectionArn": str, "Owner": str}
)

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": "RepositoryAssociationTypeDef"},
    total=False,
)

CodeReviewTypeTypeDef = TypedDict(
    "CodeReviewTypeTypeDef", {"RepositoryAnalysis": "RepositoryAnalysisTypeDef"}
)

CreateCodeReviewResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseTypeDef", {"CodeReview": "CodeReviewTypeDef"}, total=False
)

DescribeCodeReviewResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseTypeDef", {"CodeReview": "CodeReviewTypeDef"}, total=False
)

DescribeRecommendationFeedbackResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseTypeDef",
    {"RecommendationFeedback": "RecommendationFeedbackTypeDef"},
    total=False,
)

DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {"RepositoryAssociation": "RepositoryAssociationTypeDef"},
    total=False,
)

DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": "RepositoryAssociationTypeDef"},
    total=False,
)

ListCodeReviewsResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseTypeDef",
    {"CodeReviewSummaries": List["CodeReviewSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRecommendationFeedbackResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List["RecommendationFeedbackSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {"RecommendationSummaries": List["RecommendationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List["RepositoryAssociationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "CodeCommit": "CodeCommitRepositoryTypeDef",
        "Bitbucket": "ThirdPartySourceRepositoryTypeDef",
        "GitHubEnterpriseServer": "ThirdPartySourceRepositoryTypeDef",
    },
    total=False,
)
