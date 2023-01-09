"""
Type annotations for codecommit service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html)

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    OrderEnumType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    SortByEnumType,
)
from .type_defs import (
    DescribePullRequestEventsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetDifferencesOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    PaginatorConfigTypeDef,
)

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#describepullrequesteventspaginator)
    """

    def paginate(
        self,
        *,
        pullRequestId: str,
        pullRequestEventType: PullRequestEventTypeType = None,
        actorArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePullRequestEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#describepullrequesteventspaginator)
        """

class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforcomparedcommitpaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCommentsForComparedCommitOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforcomparedcommitpaginator)
        """

class GetCommentsForPullRequestPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforpullrequestpaginator)
    """

    def paginate(
        self,
        *,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCommentsForPullRequestOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforpullrequestpaginator)
        """

class GetDifferencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getdifferencespaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDifferencesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getdifferencespaginator)
        """

class ListBranchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listbranchespaginator)
    """

    def paginate(
        self, *, repositoryName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBranchesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listbranchespaginator)
        """

class ListPullRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listpullrequestspaginator)
    """

    def paginate(
        self,
        *,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: PullRequestStatusEnumType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPullRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listpullrequestspaginator)
        """

class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listrepositoriespaginator)
    """

    def paginate(
        self,
        *,
        sortBy: SortByEnumType = None,
        order: OrderEnumType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listrepositoriespaginator)
        """
