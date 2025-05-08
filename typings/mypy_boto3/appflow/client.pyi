"""
Type annotations for appflow service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appflow.client import AppflowClient

    session = Session()
    client: AppflowClient = session.client("appflow")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CancelFlowExecutionsRequestTypeDef,
    CancelFlowExecutionsResponseTypeDef,
    CreateConnectorProfileRequestTypeDef,
    CreateConnectorProfileResponseTypeDef,
    CreateFlowRequestTypeDef,
    CreateFlowResponseTypeDef,
    DeleteConnectorProfileRequestTypeDef,
    DeleteFlowRequestTypeDef,
    DescribeConnectorEntityRequestTypeDef,
    DescribeConnectorEntityResponseTypeDef,
    DescribeConnectorProfilesRequestTypeDef,
    DescribeConnectorProfilesResponseTypeDef,
    DescribeConnectorRequestTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeConnectorsRequestTypeDef,
    DescribeConnectorsResponseTypeDef,
    DescribeFlowExecutionRecordsRequestTypeDef,
    DescribeFlowExecutionRecordsResponseTypeDef,
    DescribeFlowRequestTypeDef,
    DescribeFlowResponseTypeDef,
    ListConnectorEntitiesRequestTypeDef,
    ListConnectorEntitiesResponseTypeDef,
    ListConnectorsRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListFlowsRequestTypeDef,
    ListFlowsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterConnectorRequestTypeDef,
    RegisterConnectorResponseTypeDef,
    ResetConnectorMetadataCacheRequestTypeDef,
    StartFlowRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowRequestTypeDef,
    StopFlowResponseTypeDef,
    TagResourceRequestTypeDef,
    UnregisterConnectorRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConnectorProfileRequestTypeDef,
    UpdateConnectorProfileResponseTypeDef,
    UpdateConnectorRegistrationRequestTypeDef,
    UpdateConnectorRegistrationResponseTypeDef,
    UpdateFlowRequestTypeDef,
    UpdateFlowResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("AppflowClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppflowClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#generate_presigned_url)
        """

    def cancel_flow_executions(
        self, **kwargs: Unpack[CancelFlowExecutionsRequestTypeDef]
    ) -> CancelFlowExecutionsResponseTypeDef:
        """
        Cancels active runs for a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/cancel_flow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#cancel_flow_executions)
        """

    def create_connector_profile(
        self, **kwargs: Unpack[CreateConnectorProfileRequestTypeDef]
    ) -> CreateConnectorProfileResponseTypeDef:
        """
        Creates a new connector profile associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/create_connector_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#create_connector_profile)
        """

    def create_flow(self, **kwargs: Unpack[CreateFlowRequestTypeDef]) -> CreateFlowResponseTypeDef:
        """
        Enables your application to create a new flow using Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/create_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#create_flow)
        """

    def delete_connector_profile(
        self, **kwargs: Unpack[DeleteConnectorProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables you to delete an existing connector profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/delete_connector_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#delete_connector_profile)
        """

    def delete_flow(self, **kwargs: Unpack[DeleteFlowRequestTypeDef]) -> Dict[str, Any]:
        """
        Enables your application to delete an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/delete_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#delete_flow)
        """

    def describe_connector(
        self, **kwargs: Unpack[DescribeConnectorRequestTypeDef]
    ) -> DescribeConnectorResponseTypeDef:
        """
        Describes the given custom connector registered in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector)
        """

    def describe_connector_entity(
        self, **kwargs: Unpack[DescribeConnectorEntityRequestTypeDef]
    ) -> DescribeConnectorEntityResponseTypeDef:
        """
        Provides details regarding the entity used with the connector, with a
        description of the data model for each field in that entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_connector_entity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector_entity)
        """

    def describe_connector_profiles(
        self, **kwargs: Unpack[DescribeConnectorProfilesRequestTypeDef]
    ) -> DescribeConnectorProfilesResponseTypeDef:
        """
        Returns a list of <code>connector-profile</code> details matching the provided
        <code>connector-profile</code> names and <code>connector-types</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_connector_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector_profiles)
        """

    def describe_connectors(
        self, **kwargs: Unpack[DescribeConnectorsRequestTypeDef]
    ) -> DescribeConnectorsResponseTypeDef:
        """
        Describes the connectors vended by Amazon AppFlow for specified connector types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connectors)
        """

    def describe_flow(
        self, **kwargs: Unpack[DescribeFlowRequestTypeDef]
    ) -> DescribeFlowResponseTypeDef:
        """
        Provides a description of the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_flow)
        """

    def describe_flow_execution_records(
        self, **kwargs: Unpack[DescribeFlowExecutionRecordsRequestTypeDef]
    ) -> DescribeFlowExecutionRecordsResponseTypeDef:
        """
        Fetches the execution history of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/describe_flow_execution_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_flow_execution_records)
        """

    def list_connector_entities(
        self, **kwargs: Unpack[ListConnectorEntitiesRequestTypeDef]
    ) -> ListConnectorEntitiesResponseTypeDef:
        """
        Returns the list of available connector entities supported by Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/list_connector_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_connector_entities)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Returns the list of all registered custom connectors in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/list_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_connectors)
        """

    def list_flows(self, **kwargs: Unpack[ListFlowsRequestTypeDef]) -> ListFlowsResponseTypeDef:
        """
        Lists all of the flows associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/list_flows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_flows)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags that are associated with a specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_tags_for_resource)
        """

    def register_connector(
        self, **kwargs: Unpack[RegisterConnectorRequestTypeDef]
    ) -> RegisterConnectorResponseTypeDef:
        """
        Registers a new custom connector with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/register_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#register_connector)
        """

    def reset_connector_metadata_cache(
        self, **kwargs: Unpack[ResetConnectorMetadataCacheRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets metadata about your connector entities that Amazon AppFlow stored in its
        cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/reset_connector_metadata_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#reset_connector_metadata_cache)
        """

    def start_flow(self, **kwargs: Unpack[StartFlowRequestTypeDef]) -> StartFlowResponseTypeDef:
        """
        Activates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/start_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#start_flow)
        """

    def stop_flow(self, **kwargs: Unpack[StopFlowRequestTypeDef]) -> StopFlowResponseTypeDef:
        """
        Deactivates the existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/stop_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#stop_flow)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies a tag to the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#tag_resource)
        """

    def unregister_connector(
        self, **kwargs: Unpack[UnregisterConnectorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Unregisters the custom connector registered in your account that matches the
        connector label provided in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/unregister_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#unregister_connector)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#untag_resource)
        """

    def update_connector_profile(
        self, **kwargs: Unpack[UpdateConnectorProfileRequestTypeDef]
    ) -> UpdateConnectorProfileResponseTypeDef:
        """
        Updates a given connector profile associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/update_connector_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_connector_profile)
        """

    def update_connector_registration(
        self, **kwargs: Unpack[UpdateConnectorRegistrationRequestTypeDef]
    ) -> UpdateConnectorRegistrationResponseTypeDef:
        """
        Updates a custom connector that you've previously registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/update_connector_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_connector_registration)
        """

    def update_flow(self, **kwargs: Unpack[UpdateFlowRequestTypeDef]) -> UpdateFlowResponseTypeDef:
        """
        Updates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow/client/update_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_flow)
        """
