"""
Type annotations for personalize-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_runtime import PersonalizeRuntimeClient

    client: PersonalizeRuntimeClient = boto3.client("personalize-runtime")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    GetActionRecommendationsResponseTypeDef,
    GetPersonalizedRankingResponseTypeDef,
    GetRecommendationsResponseTypeDef,
    PromotionTypeDef,
)

__all__ = ("PersonalizeRuntimeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class PersonalizeRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeRuntimeClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#generate_presigned_url)
        """

    def get_action_recommendations(
        self,
        *,
        campaignArn: str = None,
        userId: str = None,
        numResults: int = None,
        filterArn: str = None,
        filterValues: Dict[str, str] = None
    ) -> GetActionRecommendationsResponseTypeDef:
        """
        Returns a list of recommended actions in sorted in descending order by
        prediction score.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_action_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#get_action_recommendations)
        """

    def get_personalized_ranking(
        self,
        *,
        campaignArn: str,
        inputList: List[str],
        userId: str,
        context: Dict[str, str] = None,
        filterArn: str = None,
        filterValues: Dict[str, str] = None,
        metadataColumns: Dict[str, List[str]] = None
    ) -> GetPersonalizedRankingResponseTypeDef:
        """
        Re-ranks a list of recommended items for the given user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_personalized_ranking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#get_personalized_ranking)
        """

    def get_recommendations(
        self,
        *,
        campaignArn: str = None,
        itemId: str = None,
        userId: str = None,
        numResults: int = None,
        context: Dict[str, str] = None,
        filterArn: str = None,
        filterValues: Dict[str, str] = None,
        recommenderArn: str = None,
        promotions: List["PromotionTypeDef"] = None,
        metadataColumns: Dict[str, List[str]] = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        Returns a list of recommended items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client.html#get_recommendations)
        """
