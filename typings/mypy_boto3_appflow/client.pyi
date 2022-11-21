"""
Type annotations for appflow service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appflow import AppflowClient

    client: AppflowClient = boto3.client("appflow")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ConnectionModeType, ConnectorTypeType
from .type_defs import (
    ConnectorProfileConfigTypeDef,
    ConnectorProvisioningConfigTypeDef,
    CreateConnectorProfileResponseTypeDef,
    CreateFlowResponseTypeDef,
    DescribeConnectorEntityResponseTypeDef,
    DescribeConnectorProfilesResponseTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeConnectorsResponseTypeDef,
    DescribeFlowExecutionRecordsResponseTypeDef,
    DescribeFlowResponseTypeDef,
    DestinationFlowConfigTypeDef,
    ListConnectorEntitiesResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListFlowsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetadataCatalogConfigTypeDef,
    RegisterConnectorResponseTypeDef,
    SourceFlowConfigTypeDef,
    StartFlowResponseTypeDef,
    StopFlowResponseTypeDef,
    TaskTypeDef,
    TriggerConfigTypeDef,
    UpdateConnectorProfileResponseTypeDef,
    UpdateConnectorRegistrationResponseTypeDef,
    UpdateFlowResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppflowClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConnectorAuthenticationException: Type[BotocoreClientError]
    ConnectorServerException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AppflowClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppflowClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#close)
        """
    def create_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectorType: ConnectorTypeType,
        connectionMode: ConnectionModeType,
        connectorProfileConfig: "ConnectorProfileConfigTypeDef",
        kmsArn: str = None,
        connectorLabel: str = None
    ) -> CreateConnectorProfileResponseTypeDef:
        """
        Creates a new connector profile associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.create_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#create_connector_profile)
        """
    def create_flow(
        self,
        *,
        flowName: str,
        triggerConfig: "TriggerConfigTypeDef",
        sourceFlowConfig: "SourceFlowConfigTypeDef",
        destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
        tasks: List["TaskTypeDef"],
        description: str = None,
        kmsArn: str = None,
        tags: Dict[str, str] = None,
        metadataCatalogConfig: "MetadataCatalogConfigTypeDef" = None
    ) -> CreateFlowResponseTypeDef:
        """
        Enables your application to create a new flow using Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.create_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#create_flow)
        """
    def delete_connector_profile(
        self, *, connectorProfileName: str, forceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        Enables you to delete an existing connector profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.delete_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#delete_connector_profile)
        """
    def delete_flow(self, *, flowName: str, forceDelete: bool = None) -> Dict[str, Any]:
        """
        Enables your application to delete an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.delete_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#delete_flow)
        """
    def describe_connector(
        self, *, connectorType: ConnectorTypeType, connectorLabel: str = None
    ) -> DescribeConnectorResponseTypeDef:
        """
        Describes the given custom connector registered in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connector)
        """
    def describe_connector_entity(
        self,
        *,
        connectorEntityName: str,
        connectorType: ConnectorTypeType = None,
        connectorProfileName: str = None,
        apiVersion: str = None
    ) -> DescribeConnectorEntityResponseTypeDef:
        """
        Provides details regarding the entity used with the connector, with a
        description of the data model for each field in that entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_connector_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connector_entity)
        """
    def describe_connector_profiles(
        self,
        *,
        connectorProfileNames: List[str] = None,
        connectorType: ConnectorTypeType = None,
        connectorLabel: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeConnectorProfilesResponseTypeDef:
        """
        Returns a list of `connector-profile` details matching the provided `connector-
        profile` names and `connector-types`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_connector_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connector_profiles)
        """
    def describe_connectors(
        self,
        *,
        connectorTypes: List[ConnectorTypeType] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeConnectorsResponseTypeDef:
        """
        Describes the connectors vended by Amazon AppFlow for specified connector types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connectors)
        """
    def describe_flow(self, *, flowName: str) -> DescribeFlowResponseTypeDef:
        """
        Provides a description of the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_flow)
        """
    def describe_flow_execution_records(
        self, *, flowName: str, maxResults: int = None, nextToken: str = None
    ) -> DescribeFlowExecutionRecordsResponseTypeDef:
        """
        Fetches the execution history of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.describe_flow_execution_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_flow_execution_records)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#generate_presigned_url)
        """
    def list_connector_entities(
        self,
        *,
        connectorProfileName: str = None,
        connectorType: ConnectorTypeType = None,
        entitiesPath: str = None,
        apiVersion: str = None
    ) -> ListConnectorEntitiesResponseTypeDef:
        """
        Returns the list of available connector entities supported by Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.list_connector_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_connector_entities)
        """
    def list_connectors(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        Returns the list of all registered custom connectors in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_connectors)
        """
    def list_flows(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListFlowsResponseTypeDef:
        """
        Lists all of the flows associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.list_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_flows)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags that are associated with a specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_tags_for_resource)
        """
    def register_connector(
        self,
        *,
        connectorLabel: str = None,
        description: str = None,
        connectorProvisioningType: Literal["LAMBDA"] = None,
        connectorProvisioningConfig: "ConnectorProvisioningConfigTypeDef" = None
    ) -> RegisterConnectorResponseTypeDef:
        """
        Registers a new custom connector with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.register_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#register_connector)
        """
    def start_flow(self, *, flowName: str) -> StartFlowResponseTypeDef:
        """
        Activates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.start_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#start_flow)
        """
    def stop_flow(self, *, flowName: str) -> StopFlowResponseTypeDef:
        """
        Deactivates the existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.stop_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#stop_flow)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies a tag to the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#tag_resource)
        """
    def unregister_connector(
        self, *, connectorLabel: str, forceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        Unregisters the custom connector registered in your account that matches the
        connector label provided in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.unregister_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#unregister_connector)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#untag_resource)
        """
    def update_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectionMode: ConnectionModeType,
        connectorProfileConfig: "ConnectorProfileConfigTypeDef"
    ) -> UpdateConnectorProfileResponseTypeDef:
        """
        Updates a given connector profile associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.update_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#update_connector_profile)
        """
    def update_connector_registration(
        self,
        *,
        connectorLabel: str,
        description: str = None,
        connectorProvisioningConfig: "ConnectorProvisioningConfigTypeDef" = None
    ) -> UpdateConnectorRegistrationResponseTypeDef:
        """
        Updates a custom connector that you've previously registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.update_connector_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#update_connector_registration)
        """
    def update_flow(
        self,
        *,
        flowName: str,
        triggerConfig: "TriggerConfigTypeDef",
        sourceFlowConfig: "SourceFlowConfigTypeDef",
        destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
        tasks: List["TaskTypeDef"],
        description: str = None,
        metadataCatalogConfig: "MetadataCatalogConfigTypeDef" = None
    ) -> UpdateFlowResponseTypeDef:
        """
        Updates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/appflow.html#Appflow.Client.update_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#update_flow)
        """
