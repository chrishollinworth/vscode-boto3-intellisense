# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for codecommit service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codecommit import CodeCommitClient
    from mypy_boto3_codecommit.paginator import (
        DescribePullRequestEventsPaginator,
        GetCommentsForComparedCommitPaginator,
        GetCommentsForPullRequestPaginator,
        GetDifferencesPaginator,
        ListBranchesPaginator,
        ListPullRequestsPaginator,
        ListRepositoriesPaginator,
    )

    client: CodeCommitClient = boto3.client("codecommit")

    describe_pull_request_events_paginator: DescribePullRequestEventsPaginator = client.get_paginator("describe_pull_request_events")
    get_comments_for_compared_commit_paginator: GetCommentsForComparedCommitPaginator = client.get_paginator("get_comments_for_compared_commit")
    get_comments_for_pull_request_paginator: GetCommentsForPullRequestPaginator = client.get_paginator("get_comments_for_pull_request")
    get_differences_paginator: GetDifferencesPaginator = client.get_paginator("get_differences")
    list_branches_paginator: ListBranchesPaginator = client.get_paginator("list_branches")
    list_pull_requests_paginator: ListPullRequestsPaginator = client.get_paginator("list_pull_requests")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codecommit.type_defs import (
    DescribePullRequestEventsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetDifferencesOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribePullRequestEventsPaginator",
    "GetCommentsForComparedCommitPaginator",
    "GetCommentsForPullRequestPaginator",
    "GetDifferencesPaginator",
    "ListBranchesPaginator",
    "ListPullRequestsPaginator",
    "ListRepositoriesPaginator",
)


class DescribePullRequestEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePullRequestEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePullRequestEventsOutputTypeDef]:
        """
        [DescribePullRequestEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents.paginate)
        """


class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    """
    [Paginator.GetCommentsForComparedCommit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)
    """

    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetCommentsForComparedCommitOutputTypeDef]:
        """
        [GetCommentsForComparedCommit.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit.paginate)
        """


class GetCommentsForPullRequestPaginator(Boto3Paginator):
    """
    [Paginator.GetCommentsForPullRequest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)
    """

    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetCommentsForPullRequestOutputTypeDef]:
        """
        [GetCommentsForPullRequest.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest.paginate)
        """


class GetDifferencesPaginator(Boto3Paginator):
    """
    [Paginator.GetDifferences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)
    """

    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetDifferencesOutputTypeDef]:
        """
        [GetDifferences.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)
    """

    def paginate(
        self, repositoryName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBranchesOutputTypeDef]:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches.paginate)
        """


class ListPullRequestsPaginator(Boto3Paginator):
    """
    [Paginator.ListPullRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)
    """

    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPullRequestsOutputTypeDef]:
        """
        [ListPullRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests.paginate)
        """


class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)
    """

    def paginate(
        self,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRepositoriesOutputTypeDef]:
        """
        [ListRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories.paginate)
        """
