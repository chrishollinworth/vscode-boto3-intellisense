"""
Type annotations for personalize-events service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_personalize_events.client import PersonalizeEventsClient

    session = Session()
    client: PersonalizeEventsClient = session.client("personalize-events")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    EmptyResponseMetadataTypeDef,
    PutActionInteractionsRequestTypeDef,
    PutActionsRequestTypeDef,
    PutEventsRequestTypeDef,
    PutItemsRequestTypeDef,
    PutUsersRequestTypeDef,
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

__all__ = ("PersonalizeEventsClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class PersonalizeEventsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeEventsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#generate_presigned_url)
        """

    def put_action_interactions(
        self, **kwargs: Unpack[PutActionInteractionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records action interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/put_action_interactions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_action_interactions)
        """

    def put_actions(
        self, **kwargs: Unpack[PutActionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more actions to an Actions dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/put_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_actions)
        """

    def put_events(self, **kwargs: Unpack[PutEventsRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Records item interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/put_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_events)
        """

    def put_items(self, **kwargs: Unpack[PutItemsRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more items to an Items dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/put_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_items)
        """

    def put_users(self, **kwargs: Unpack[PutUsersRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more users to a Users dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events/client/put_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_users)
        """
