"""
Main interface for appintegrations service client

Usage::

    ```python
    import boto3
    from mypy_boto3_appintegrations import AppIntegrationsServiceClient

    client: AppIntegrationsServiceClient = boto3.client("appintegrations")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_appintegrations.type_defs import (
    CreateEventIntegrationResponseTypeDef,
    EventFilterTypeDef,
    GetEventIntegrationResponseTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("AppIntegrationsServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class AppIntegrationsServiceClient:
    """
    [AppIntegrationsService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.can_paginate)
        """

    def create_event_integration(
        self,
        Name: str,
        EventFilter: "EventFilterTypeDef",
        EventBridgeBus: str,
        Description: str = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateEventIntegrationResponseTypeDef:
        """
        [Client.create_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.create_event_integration)
        """

    def delete_event_integration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_event_integration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.generate_presigned_url)
        """

    def get_event_integration(self, Name: str) -> GetEventIntegrationResponseTypeDef:
        """
        [Client.get_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.get_event_integration)
        """

    def list_event_integration_associations(
        self, EventIntegrationName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListEventIntegrationAssociationsResponseTypeDef:
        """
        [Client.list_event_integration_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integration_associations)
        """

    def list_event_integrations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEventIntegrationsResponseTypeDef:
        """
        [Client.list_event_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integrations)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.untag_resource)
        """

    def update_event_integration(self, Name: str, Description: str = None) -> Dict[str, Any]:
        """
        [Client.update_event_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/appintegrations.html#AppIntegrationsService.Client.update_event_integration)
        """
