"""
Type annotations for appintegrations service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appintegrations import AppIntegrationsServiceClient

    client: AppIntegrationsServiceClient = boto3.client("appintegrations")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CreateDataIntegrationResponseTypeDef,
    CreateEventIntegrationResponseTypeDef,
    EventFilterTypeDef,
    GetDataIntegrationResponseTypeDef,
    GetEventIntegrationResponseTypeDef,
    ListDataIntegrationAssociationsResponseTypeDef,
    ListDataIntegrationsResponseTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ScheduleConfigurationTypeDef,
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

class AppIntegrationsServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppIntegrationsServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#close)
        """
    def create_data_integration(
        self,
        *,
        Name: str,
        Description: str = None,
        KmsKey: str = None,
        SourceURI: str = None,
        ScheduleConfig: "ScheduleConfigurationTypeDef" = None,
        Tags: Dict[str, str] = None,
        ClientToken: str = None
    ) -> CreateDataIntegrationResponseTypeDef:
        """
        Creates and persists a DataIntegration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.create_data_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#create_data_integration)
        """
    def create_event_integration(
        self,
        *,
        Name: str,
        EventFilter: "EventFilterTypeDef",
        EventBridgeBus: str,
        Description: str = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateEventIntegrationResponseTypeDef:
        """
        Creates an EventIntegration, given a specified name, description, and a
        reference to an Amazon EventBridge bus in your account and a partner event
        source that pushes events to that bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.create_event_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#create_event_integration)
        """
    def delete_data_integration(self, *, DataIntegrationIdentifier: str) -> Dict[str, Any]:
        """
        Deletes the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_data_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#delete_data_integration)
        """
    def delete_event_integration(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the specified existing event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_event_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#delete_event_integration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#generate_presigned_url)
        """
    def get_data_integration(self, *, Identifier: str) -> GetDataIntegrationResponseTypeDef:
        """
        Returns information about the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.get_data_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#get_data_integration)
        """
    def get_event_integration(self, *, Name: str) -> GetEventIntegrationResponseTypeDef:
        """
        Returns information about the event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.get_event_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#get_event_integration)
        """
    def list_data_integration_associations(
        self, *, DataIntegrationIdentifier: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.list_data_integration_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#list_data_integration_associations)
        """
    def list_data_integrations(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDataIntegrationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.list_data_integrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#list_data_integrations)
        """
    def list_event_integration_associations(
        self, *, EventIntegrationName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListEventIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of event integration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integration_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#list_event_integration_associations)
        """
    def list_event_integrations(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEventIntegrationsResponseTypeDef:
        """
        Returns a paginated list of event integrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#list_event_integrations)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#untag_resource)
        """
    def update_data_integration(
        self, *, Identifier: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the description of a DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.update_data_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#update_data_integration)
        """
    def update_event_integration(self, *, Name: str, Description: str = None) -> Dict[str, Any]:
        """
        Updates the description of an event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/appintegrations.html#AppIntegrationsService.Client.update_event_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/client.html#update_event_integration)
        """
