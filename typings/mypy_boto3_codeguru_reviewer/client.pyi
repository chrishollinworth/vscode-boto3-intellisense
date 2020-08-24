# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_codeguru_reviewer.paginator import ListRepositoryAssociationsPaginator
from mypy_boto3_codeguru_reviewer.type_defs import (
    AssociateRepositoryResponseTypeDef,
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


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class CodeGuruReviewerClient:
    """
    [CodeGuruReviewer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    """

    exceptions: Exceptions

    def associate_repository(
        self, Repository: RepositoryTypeDef, ClientRequestToken: str = None
    ) -> AssociateRepositoryResponseTypeDef:
        """
        [Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        """

    def describe_code_review(self, CodeReviewArn: str) -> DescribeCodeReviewResponseTypeDef:
        """
        [Client.describe_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_code_review)
        """

    def describe_recommendation_feedback(
        self, CodeReviewArn: str, RecommendationId: str, UserId: str = None
    ) -> DescribeRecommendationFeedbackResponseTypeDef:
        """
        [Client.describe_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_recommendation_feedback)
        """

    def describe_repository_association(
        self, AssociationArn: str
    ) -> DescribeRepositoryAssociationResponseTypeDef:
        """
        [Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        """

    def disassociate_repository(self, AssociationArn: str) -> DisassociateRepositoryResponseTypeDef:
        """
        [Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        """

    def list_code_reviews(
        self,
        Type: Literal["PullRequest"],
        ProviderTypes: List[
            Literal["CodeCommit", "GitHub", "Bitbucket", "GitHubEnterpriseServer"]
        ] = None,
        States: List[Literal["Completed", "Pending", "Failed", "Deleting"]] = None,
        RepositoryNames: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCodeReviewsResponseTypeDef:
        """
        [Client.list_code_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_code_reviews)
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
        [Client.list_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendation_feedback)
        """

    def list_recommendations(
        self, CodeReviewArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        [Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendations)
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
        [Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        """

    def put_recommendation_feedback(
        self,
        CodeReviewArn: str,
        RecommendationId: str,
        Reactions: List[Literal["ThumbsUp", "ThumbsDown"]],
    ) -> Dict[str, Any]:
        """
        [Client.put_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.put_recommendation_feedback)
        """

    def get_paginator(
        self, operation_name: Literal["list_repository_associations"]
    ) -> ListRepositoryAssociationsPaginator:
        """
        [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        """
