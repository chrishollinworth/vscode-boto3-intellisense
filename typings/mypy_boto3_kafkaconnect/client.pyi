"""
Type annotations for kafkaconnect service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kafkaconnect.client import KafkaConnectClient

    session = Session()
    client: KafkaConnectClient = session.client("kafkaconnect")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListConnectorOperationsPaginator,
    ListConnectorsPaginator,
    ListCustomPluginsPaginator,
    ListWorkerConfigurationsPaginator,
)
from .type_defs import (
    CreateConnectorRequestTypeDef,
    CreateConnectorResponseTypeDef,
    CreateCustomPluginRequestTypeDef,
    CreateCustomPluginResponseTypeDef,
    CreateWorkerConfigurationRequestTypeDef,
    CreateWorkerConfigurationResponseTypeDef,
    DeleteConnectorRequestTypeDef,
    DeleteConnectorResponseTypeDef,
    DeleteCustomPluginRequestTypeDef,
    DeleteCustomPluginResponseTypeDef,
    DeleteWorkerConfigurationRequestTypeDef,
    DeleteWorkerConfigurationResponseTypeDef,
    DescribeConnectorOperationRequestTypeDef,
    DescribeConnectorOperationResponseTypeDef,
    DescribeConnectorRequestTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeCustomPluginRequestTypeDef,
    DescribeCustomPluginResponseTypeDef,
    DescribeWorkerConfigurationRequestTypeDef,
    DescribeWorkerConfigurationResponseTypeDef,
    ListConnectorOperationsRequestTypeDef,
    ListConnectorOperationsResponseTypeDef,
    ListConnectorsRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListCustomPluginsRequestTypeDef,
    ListCustomPluginsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkerConfigurationsRequestTypeDef,
    ListWorkerConfigurationsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConnectorRequestTypeDef,
    UpdateConnectorResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("KafkaConnectClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class KafkaConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect.html#KafkaConnect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KafkaConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect.html#KafkaConnect.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#generate_presigned_url)
        """

    def create_connector(
        self, **kwargs: Unpack[CreateConnectorRequestTypeDef]
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a connector using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/create_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#create_connector)
        """

    def create_custom_plugin(
        self, **kwargs: Unpack[CreateCustomPluginRequestTypeDef]
    ) -> CreateCustomPluginResponseTypeDef:
        """
        Creates a custom plugin using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/create_custom_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#create_custom_plugin)
        """

    def create_worker_configuration(
        self, **kwargs: Unpack[CreateWorkerConfigurationRequestTypeDef]
    ) -> CreateWorkerConfigurationResponseTypeDef:
        """
        Creates a worker configuration using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/create_worker_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#create_worker_configuration)
        """

    def delete_connector(
        self, **kwargs: Unpack[DeleteConnectorRequestTypeDef]
    ) -> DeleteConnectorResponseTypeDef:
        """
        Deletes the specified connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/delete_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#delete_connector)
        """

    def delete_custom_plugin(
        self, **kwargs: Unpack[DeleteCustomPluginRequestTypeDef]
    ) -> DeleteCustomPluginResponseTypeDef:
        """
        Deletes a custom plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/delete_custom_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#delete_custom_plugin)
        """

    def delete_worker_configuration(
        self, **kwargs: Unpack[DeleteWorkerConfigurationRequestTypeDef]
    ) -> DeleteWorkerConfigurationResponseTypeDef:
        """
        Deletes the specified worker configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/delete_worker_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#delete_worker_configuration)
        """

    def describe_connector(
        self, **kwargs: Unpack[DescribeConnectorRequestTypeDef]
    ) -> DescribeConnectorResponseTypeDef:
        """
        Returns summary information about the connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/describe_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#describe_connector)
        """

    def describe_connector_operation(
        self, **kwargs: Unpack[DescribeConnectorOperationRequestTypeDef]
    ) -> DescribeConnectorOperationResponseTypeDef:
        """
        Returns information about the specified connector's operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/describe_connector_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#describe_connector_operation)
        """

    def describe_custom_plugin(
        self, **kwargs: Unpack[DescribeCustomPluginRequestTypeDef]
    ) -> DescribeCustomPluginResponseTypeDef:
        """
        A summary description of the custom plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/describe_custom_plugin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#describe_custom_plugin)
        """

    def describe_worker_configuration(
        self, **kwargs: Unpack[DescribeWorkerConfigurationRequestTypeDef]
    ) -> DescribeWorkerConfigurationResponseTypeDef:
        """
        Returns information about a worker configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/describe_worker_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#describe_worker_configuration)
        """

    def list_connector_operations(
        self, **kwargs: Unpack[ListConnectorOperationsRequestTypeDef]
    ) -> ListConnectorOperationsResponseTypeDef:
        """
        Lists information about a connector's operation(s).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/list_connector_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#list_connector_operations)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Returns a list of all the connectors in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/list_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#list_connectors)
        """

    def list_custom_plugins(
        self, **kwargs: Unpack[ListCustomPluginsRequestTypeDef]
    ) -> ListCustomPluginsResponseTypeDef:
        """
        Returns a list of all of the custom plugins in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/list_custom_plugins.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#list_custom_plugins)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all the tags attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#list_tags_for_resource)
        """

    def list_worker_configurations(
        self, **kwargs: Unpack[ListWorkerConfigurationsRequestTypeDef]
    ) -> ListWorkerConfigurationsResponseTypeDef:
        """
        Returns a list of all of the worker configurations in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/list_worker_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#list_worker_configurations)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#untag_resource)
        """

    def update_connector(
        self, **kwargs: Unpack[UpdateConnectorRequestTypeDef]
    ) -> UpdateConnectorResponseTypeDef:
        """
        Updates the specified connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/update_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#update_connector)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connector_operations"]
    ) -> ListConnectorOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connectors"]
    ) -> ListConnectorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_plugins"]
    ) -> ListCustomPluginsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_worker_configurations"]
    ) -> ListWorkerConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client/#get_paginator)
        """
