# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for personalize-events service client

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize_events import PersonalizeEventsClient

    client: PersonalizeEventsClient = boto3.client("personalize-events")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_personalize_events.type_defs import EventTypeDef, ItemTypeDef, UserTypeDef

__all__ = ("PersonalizeEventsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class PersonalizeEventsClient:
    """
    [PersonalizeEvents.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client.generate_presigned_url)
        """

    def put_events(
        self, trackingId: str, sessionId: str, eventList: List[EventTypeDef], userId: str = None
    ) -> None:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client.put_events)
        """

    def put_items(self, datasetArn: str, items: List[ItemTypeDef]) -> None:
        """
        [Client.put_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client.put_items)
        """

    def put_users(self, datasetArn: str, users: List[UserTypeDef]) -> None:
        """
        [Client.put_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize-events.html#PersonalizeEvents.Client.put_users)
        """
