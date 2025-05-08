"""
Type annotations for mq service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mq.client import MQClient

    session = Session()
    client: MQClient = session.client("mq")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListBrokersPaginator
from .type_defs import (
    CreateBrokerRequestTypeDef,
    CreateBrokerResponseTypeDef,
    CreateConfigurationRequestTypeDef,
    CreateConfigurationResponseTypeDef,
    CreateTagsRequestTypeDef,
    CreateUserRequestTypeDef,
    DeleteBrokerRequestTypeDef,
    DeleteBrokerResponseTypeDef,
    DeleteConfigurationRequestTypeDef,
    DeleteConfigurationResponseTypeDef,
    DeleteTagsRequestTypeDef,
    DeleteUserRequestTypeDef,
    DescribeBrokerEngineTypesRequestTypeDef,
    DescribeBrokerEngineTypesResponseTypeDef,
    DescribeBrokerInstanceOptionsRequestTypeDef,
    DescribeBrokerInstanceOptionsResponseTypeDef,
    DescribeBrokerRequestTypeDef,
    DescribeBrokerResponseTypeDef,
    DescribeConfigurationRequestTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionRequestTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    DescribeUserRequestTypeDef,
    DescribeUserResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListBrokersRequestTypeDef,
    ListBrokersResponseTypeDef,
    ListConfigurationRevisionsRequestTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsRequestTypeDef,
    ListConfigurationsResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    PromoteRequestTypeDef,
    PromoteResponseTypeDef,
    RebootBrokerRequestTypeDef,
    UpdateBrokerRequestTypeDef,
    UpdateBrokerResponseTypeDef,
    UpdateConfigurationRequestTypeDef,
    UpdateConfigurationResponseTypeDef,
    UpdateUserRequestTypeDef,
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

__all__ = ("MQClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class MQClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MQClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#generate_presigned_url)
        """

    def create_broker(
        self, **kwargs: Unpack[CreateBrokerRequestTypeDef]
    ) -> CreateBrokerResponseTypeDef:
        """
        Creates a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/create_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#create_broker)
        """

    def create_configuration(
        self, **kwargs: Unpack[CreateConfigurationRequestTypeDef]
    ) -> CreateConfigurationResponseTypeDef:
        """
        Creates a new configuration for the specified configuration name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/create_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#create_configuration)
        """

    def create_tags(
        self, **kwargs: Unpack[CreateTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Add a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#create_tags)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#create_user)
        """

    def delete_broker(
        self, **kwargs: Unpack[DeleteBrokerRequestTypeDef]
    ) -> DeleteBrokerResponseTypeDef:
        """
        Deletes a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/delete_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#delete_broker)
        """

    def delete_configuration(
        self, **kwargs: Unpack[DeleteConfigurationRequestTypeDef]
    ) -> DeleteConfigurationResponseTypeDef:
        """
        Deletes the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/delete_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#delete_configuration)
        """

    def delete_tags(
        self, **kwargs: Unpack[DeleteTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/delete_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#delete_tags)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#delete_user)
        """

    def describe_broker(
        self, **kwargs: Unpack[DescribeBrokerRequestTypeDef]
    ) -> DescribeBrokerResponseTypeDef:
        """
        Returns information about the specified broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_broker)
        """

    def describe_broker_engine_types(
        self, **kwargs: Unpack[DescribeBrokerEngineTypesRequestTypeDef]
    ) -> DescribeBrokerEngineTypesResponseTypeDef:
        """
        Describe available engine types and versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_broker_engine_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_broker_engine_types)
        """

    def describe_broker_instance_options(
        self, **kwargs: Unpack[DescribeBrokerInstanceOptionsRequestTypeDef]
    ) -> DescribeBrokerInstanceOptionsResponseTypeDef:
        """
        Describe available broker instance options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_broker_instance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_broker_instance_options)
        """

    def describe_configuration(
        self, **kwargs: Unpack[DescribeConfigurationRequestTypeDef]
    ) -> DescribeConfigurationResponseTypeDef:
        """
        Returns information about the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_configuration)
        """

    def describe_configuration_revision(
        self, **kwargs: Unpack[DescribeConfigurationRevisionRequestTypeDef]
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        Returns the specified configuration revision for the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_configuration_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_configuration_revision)
        """

    def describe_user(
        self, **kwargs: Unpack[DescribeUserRequestTypeDef]
    ) -> DescribeUserResponseTypeDef:
        """
        Returns information about an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/describe_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#describe_user)
        """

    def list_brokers(
        self, **kwargs: Unpack[ListBrokersRequestTypeDef]
    ) -> ListBrokersResponseTypeDef:
        """
        Returns a list of all brokers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/list_brokers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#list_brokers)
        """

    def list_configuration_revisions(
        self, **kwargs: Unpack[ListConfigurationRevisionsRequestTypeDef]
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        Returns a list of all revisions for the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/list_configuration_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#list_configuration_revisions)
        """

    def list_configurations(
        self, **kwargs: Unpack[ListConfigurationsRequestTypeDef]
    ) -> ListConfigurationsResponseTypeDef:
        """
        Returns a list of all configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/list_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#list_configurations)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#list_tags)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResponseTypeDef:
        """
        Returns a list of all ActiveMQ users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#list_users)
        """

    def promote(self, **kwargs: Unpack[PromoteRequestTypeDef]) -> PromoteResponseTypeDef:
        """
        Promotes a data replication replica broker to the primary broker role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/promote.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#promote)
        """

    def reboot_broker(self, **kwargs: Unpack[RebootBrokerRequestTypeDef]) -> Dict[str, Any]:
        """
        Reboots a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/reboot_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#reboot_broker)
        """

    def update_broker(
        self, **kwargs: Unpack[UpdateBrokerRequestTypeDef]
    ) -> UpdateBrokerResponseTypeDef:
        """
        Adds a pending configuration change to a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/update_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#update_broker)
        """

    def update_configuration(
        self, **kwargs: Unpack[UpdateConfigurationRequestTypeDef]
    ) -> UpdateConfigurationResponseTypeDef:
        """
        Updates the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/update_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#update_configuration)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the information for an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#update_user)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_brokers"]
    ) -> ListBrokersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/client/#get_paginator)
        """
