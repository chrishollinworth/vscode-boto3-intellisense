# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for codeguru-reviewer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_reviewer import CodeGuruReviewerClient

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_codeguru_reviewer.paginator import ListRepositoryAssociationsPaginator
from mypy_boto3_codeguru_reviewer.type_defs import (
    AssociateRepositoryResponseTypeDef,
    CodeReviewTypeTypeDef,
    CreateCodeReviewResponseTypeDef,
    DescribeCodeReviewResponseTypeDef,
    DescribeRecommendationFeedbackResponseTypeDef,
    DescribeRepositoryAssociationResponseTypeDef,
    DisassociateRepositoryResponseTypeDef,
    ListCodeReviewsResponseTypeDef,
    ListRecommendationFeedbackResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRepositoryAssociationsResponseTypeDef,
    RepositoryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruReviewerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeGuruReviewerClient:
    """
    [CodeGuruReviewer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_repository(
        self, Repository: RepositoryTypeDef, ClientRequestToken: str = None
    ) -> AssociateRepositoryResponseTypeDef:
        """
        [Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        """

    def create_code_review(
        self,
        Name: str,
        RepositoryAssociationArn: str,
        Type: CodeReviewTypeTypeDef,
        ClientRequestToken: str = None,
    ) -> CreateCodeReviewResponseTypeDef:
        """
        [Client.create_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.create_code_review)
        """

    def describe_code_review(self, CodeReviewArn: str) -> DescribeCodeReviewResponseTypeDef:
        """
        [Client.describe_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_code_review)
        """

    def describe_recommendation_feedback(
        self, CodeReviewArn: str, RecommendationId: str, UserId: str = None
    ) -> DescribeRecommendationFeedbackResponseTypeDef:
        """
        [Client.describe_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_recommendation_feedback)
        """

    def describe_repository_association(
        self, AssociationArn: str
    ) -> DescribeRepositoryAssociationResponseTypeDef:
        """
        [Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        """

    def disassociate_repository(self, AssociationArn: str) -> DisassociateRepositoryResponseTypeDef:
        """
        [Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        """

    def list_code_reviews(
        self,
        Type: Literal["PullRequest", "RepositoryAnalysis"],
        ProviderTypes: List[
            Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"]
        ] = None,
        States: List[Literal["Completed", "Pending", "Failed", "Deleting"]] = None,
        RepositoryNames: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCodeReviewsResponseTypeDef:
        """
        [Client.list_code_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_code_reviews)
        """

    def list_recommendation_feedback(
        self,
        CodeReviewArn: str,
        NextToken: str = None,
        MaxResults: int = None,
        UserIds: List[str] = None,
        RecommendationIds: List[str] = None,
    ) -> ListRecommendationFeedbackResponseTypeDef:
        """
        [Client.list_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendation_feedback)
        """

    def list_recommendations(
        self, CodeReviewArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        [Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendations)
        """

    def list_repository_associations(
        self,
        ProviderTypes: List[
            Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"]
        ] = None,
        States: List[Literal["Associated", "Associating", "Failed", "Disassociating"]] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListRepositoryAssociationsResponseTypeDef:
        """
        [Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        """

    def put_recommendation_feedback(
        self,
        CodeReviewArn: str,
        RecommendationId: str,
        Reactions: List[Literal["ThumbsUp", "ThumbsDown"]],
    ) -> Dict[str, Any]:
        """
        [Client.put_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.put_recommendation_feedback)
        """

    def get_paginator(
        self, operation_name: Literal["list_repository_associations"]
    ) -> ListRepositoryAssociationsPaginator:
        """
        [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        """
