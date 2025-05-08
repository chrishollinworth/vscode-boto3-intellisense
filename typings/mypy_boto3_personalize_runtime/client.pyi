"""
Type annotations for personalize-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_personalize_runtime.client import PersonalizeRuntimeClient

    session = Session()
    client: PersonalizeRuntimeClient = session.client("personalize-runtime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GetActionRecommendationsRequestTypeDef,
    GetActionRecommendationsResponseTypeDef,
    GetPersonalizedRankingRequestTypeDef,
    GetPersonalizedRankingResponseTypeDef,
    GetRecommendationsRequestTypeDef,
    GetRecommendationsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("PersonalizeRuntimeClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class PersonalizeRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#generate_presigned_url)
        """

    def get_action_recommendations(
        self, **kwargs: Unpack[GetActionRecommendationsRequestTypeDef]
    ) -> GetActionRecommendationsResponseTypeDef:
        """
        Returns a list of recommended actions in sorted in descending order by
        prediction score.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime/client/get_action_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#get_action_recommendations)
        """

    def get_personalized_ranking(
        self, **kwargs: Unpack[GetPersonalizedRankingRequestTypeDef]
    ) -> GetPersonalizedRankingResponseTypeDef:
        """
        Re-ranks a list of recommended items for the given user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime/client/get_personalized_ranking.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#get_personalized_ranking)
        """

    def get_recommendations(
        self, **kwargs: Unpack[GetRecommendationsRequestTypeDef]
    ) -> GetRecommendationsResponseTypeDef:
        """
        Returns a list of recommended items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime/client/get_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/client/#get_recommendations)
        """
