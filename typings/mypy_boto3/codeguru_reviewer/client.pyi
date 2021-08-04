"""
Type annotations for codeguru-reviewer service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_reviewer import CodeGuruReviewerClient

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RepositoryAssociationStateType,
    TypeType,
)
from .paginator import ListRepositoryAssociationsPaginator
from .type_defs import (
    AssociateRepositoryResponseTypeDef,
    CodeReviewTypeTypeDef,
    CreateCodeReviewResponseTypeDef,
    DescribeCodeReviewResponseTypeDef,
    DescribeRecommendationFeedbackResponseTypeDef,
    DescribeRepositoryAssociationResponseTypeDef,
    DisassociateRepositoryResponseTypeDef,
    KMSKeyDetailsTypeDef,
    ListCodeReviewsResponseTypeDef,
    ListRecommendationFeedbackResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRepositoryAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RepositoryTypeDef,
)
from .waiter import CodeReviewCompletedWaiter, RepositoryAssociationSucceededWaiter

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

class CodeGuruReviewerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CodeGuruReviewerClient exceptions.
        """
    def associate_repository(
        self,
        *,
        Repository: "RepositoryTypeDef",
        ClientRequestToken: str = None,
        Tags: Dict[str, str] = None,
        KMSKeyDetails: "KMSKeyDetailsTypeDef" = None
    ) -> AssociateRepositoryResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#associate_repository)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#can_paginate)
        """
    def create_code_review(
        self,
        *,
        Name: str,
        RepositoryAssociationArn: str,
        Type: "CodeReviewTypeTypeDef",
        ClientRequestToken: str = None
    ) -> CreateCodeReviewResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.create_code_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#create_code_review)
        """
    def describe_code_review(self, *, CodeReviewArn: str) -> DescribeCodeReviewResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_code_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#describe_code_review)
        """
    def describe_recommendation_feedback(
        self, *, CodeReviewArn: str, RecommendationId: str, UserId: str = None
    ) -> DescribeRecommendationFeedbackResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_recommendation_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#describe_recommendation_feedback)
        """
    def describe_repository_association(
        self, *, AssociationArn: str
    ) -> DescribeRepositoryAssociationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#describe_repository_association)
        """
    def disassociate_repository(
        self, *, AssociationArn: str
    ) -> DisassociateRepositoryResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#disassociate_repository)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#generate_presigned_url)
        """
    def list_code_reviews(
        self,
        *,
        Type: TypeType,
        ProviderTypes: List[ProviderTypeType] = None,
        States: List[JobStateType] = None,
        RepositoryNames: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCodeReviewsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_code_reviews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#list_code_reviews)
        """
    def list_recommendation_feedback(
        self,
        *,
        CodeReviewArn: str,
        NextToken: str = None,
        MaxResults: int = None,
        UserIds: List[str] = None,
        RecommendationIds: List[str] = None
    ) -> ListRecommendationFeedbackResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendation_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#list_recommendation_feedback)
        """
    def list_recommendations(
        self, *, CodeReviewArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#list_recommendations)
        """
    def list_repository_associations(
        self,
        *,
        ProviderTypes: List[ProviderTypeType] = None,
        States: List[RepositoryAssociationStateType] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListRepositoryAssociationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#list_repository_associations)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#list_tags_for_resource)
        """
    def put_recommendation_feedback(
        self, *, CodeReviewArn: str, RecommendationId: str, Reactions: List[ReactionType]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.put_recommendation_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#put_recommendation_feedback)
        """
    def tag_resource(self, *, resourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/client.html#untag_resource)
        """
    def get_paginator(
        self, operation_name: Literal["list_repository_associations"]
    ) -> ListRepositoryAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/paginators.html#listrepositoryassociationspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["code_review_completed"]
    ) -> CodeReviewCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Waiter.CodeReviewCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters.html#codereviewcompletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["repository_association_succeeded"]
    ) -> RepositoryAssociationSucceededWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Waiter.RepositoryAssociationSucceeded)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/waiters.html#repositoryassociationsucceededwaiter)
        """
