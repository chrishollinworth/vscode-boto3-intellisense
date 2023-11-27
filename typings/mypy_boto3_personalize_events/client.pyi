"""
Type annotations for personalize-events service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_events import PersonalizeEventsClient

    client: PersonalizeEventsClient = boto3.client("personalize-events")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    ActionInteractionTypeDef,
    ActionTypeDef,
    EventTypeDef,
    ItemTypeDef,
    UserTypeDef,
)

__all__ = ("PersonalizeEventsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class PersonalizeEventsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeEventsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#generate_presigned_url)
        """
    def put_action_interactions(
        self, *, trackingId: str, actionInteractions: List["ActionInteractionTypeDef"]
    ) -> None:
        """
        Records action interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.put_action_interactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#put_action_interactions)
        """
    def put_actions(self, *, datasetArn: str, actions: List["ActionTypeDef"]) -> None:
        """
        Adds one or more actions to an Actions dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.put_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#put_actions)
        """
    def put_events(
        self,
        *,
        trackingId: str,
        sessionId: str,
        eventList: List["EventTypeDef"],
        userId: str = None
    ) -> None:
        """
        Records item interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.put_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#put_events)
        """
    def put_items(self, *, datasetArn: str, items: List["ItemTypeDef"]) -> None:
        """
        Adds one or more items to an Items dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.put_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#put_items)
        """
    def put_users(self, *, datasetArn: str, users: List["UserTypeDef"]) -> None:
        """
        Adds one or more users to a Users dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/personalize-events.html#PersonalizeEvents.Client.put_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client.html#put_users)
        """
