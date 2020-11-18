# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for personalize-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_runtime import PersonalizeRuntimeClient

    client: PersonalizeRuntimeClient = boto3.client("personalize-runtime")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_personalize_runtime.type_defs import (
    GetPersonalizedRankingResponseTypeDef,
    GetRecommendationsResponseTypeDef,
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


class PersonalizeRuntimeClient:
    """
    [PersonalizeRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-runtime.html#PersonalizeRuntime.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.generate_presigned_url)
        """

    def get_personalized_ranking(
        self,
        campaignArn: str,
        inputList: List[str],
        userId: str,
        context: Dict[str, str] = None,
        filterArn: str = None,
        filterValues: Dict[str, str] = None,
    ) -> GetPersonalizedRankingResponseTypeDef:
        """
        [Client.get_personalized_ranking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_personalized_ranking)
        """

    def get_recommendations(
        self,
        campaignArn: str,
        itemId: str = None,
        userId: str = None,
        numResults: int = None,
        context: Dict[str, str] = None,
        filterArn: str = None,
        filterValues: Dict[str, str] = None,
    ) -> GetRecommendationsResponseTypeDef:
        """
        [Client.get_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_recommendations)
        """
