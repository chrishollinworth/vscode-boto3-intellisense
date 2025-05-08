"""
Type annotations for securitylake service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_securitylake.client import SecurityLakeClient

    session = Session()
    client: SecurityLakeClient = session.client("securitylake")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetDataLakeSourcesPaginator,
    ListDataLakeExceptionsPaginator,
    ListLogSourcesPaginator,
    ListSubscribersPaginator,
)
from .type_defs import (
    CreateAwsLogSourceRequestTypeDef,
    CreateAwsLogSourceResponseTypeDef,
    CreateCustomLogSourceRequestTypeDef,
    CreateCustomLogSourceResponseTypeDef,
    CreateDataLakeExceptionSubscriptionRequestTypeDef,
    CreateDataLakeOrganizationConfigurationRequestTypeDef,
    CreateDataLakeRequestTypeDef,
    CreateDataLakeResponseTypeDef,
    CreateSubscriberNotificationRequestTypeDef,
    CreateSubscriberNotificationResponseTypeDef,
    CreateSubscriberRequestTypeDef,
    CreateSubscriberResponseTypeDef,
    DeleteAwsLogSourceRequestTypeDef,
    DeleteAwsLogSourceResponseTypeDef,
    DeleteCustomLogSourceRequestTypeDef,
    DeleteDataLakeOrganizationConfigurationRequestTypeDef,
    DeleteDataLakeRequestTypeDef,
    DeleteSubscriberNotificationRequestTypeDef,
    DeleteSubscriberRequestTypeDef,
    GetDataLakeExceptionSubscriptionResponseTypeDef,
    GetDataLakeOrganizationConfigurationResponseTypeDef,
    GetDataLakeSourcesRequestTypeDef,
    GetDataLakeSourcesResponseTypeDef,
    GetSubscriberRequestTypeDef,
    GetSubscriberResponseTypeDef,
    ListDataLakeExceptionsRequestTypeDef,
    ListDataLakeExceptionsResponseTypeDef,
    ListDataLakesRequestTypeDef,
    ListDataLakesResponseTypeDef,
    ListLogSourcesRequestTypeDef,
    ListLogSourcesResponseTypeDef,
    ListSubscribersRequestTypeDef,
    ListSubscribersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterDataLakeDelegatedAdministratorRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDataLakeExceptionSubscriptionRequestTypeDef,
    UpdateDataLakeRequestTypeDef,
    UpdateDataLakeResponseTypeDef,
    UpdateSubscriberNotificationRequestTypeDef,
    UpdateSubscriberNotificationResponseTypeDef,
    UpdateSubscriberRequestTypeDef,
    UpdateSubscriberResponseTypeDef,
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

__all__ = ("SecurityLakeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class SecurityLakeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake.html#SecurityLake.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SecurityLakeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake.html#SecurityLake.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#generate_presigned_url)
        """

    def create_aws_log_source(
        self, **kwargs: Unpack[CreateAwsLogSourceRequestTypeDef]
    ) -> CreateAwsLogSourceResponseTypeDef:
        """
        Adds a natively supported Amazon Web Services service as an Amazon Security
        Lake source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_aws_log_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_aws_log_source)
        """

    def create_custom_log_source(
        self, **kwargs: Unpack[CreateCustomLogSourceRequestTypeDef]
    ) -> CreateCustomLogSourceResponseTypeDef:
        """
        Adds a third-party custom source in Amazon Security Lake, from the Amazon Web
        Services Region where you want to create a custom source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_custom_log_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_custom_log_source)
        """

    def create_data_lake(
        self, **kwargs: Unpack[CreateDataLakeRequestTypeDef]
    ) -> CreateDataLakeResponseTypeDef:
        """
        Initializes an Amazon Security Lake instance with the provided (or default)
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_data_lake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_data_lake)
        """

    def create_data_lake_exception_subscription(
        self, **kwargs: Unpack[CreateDataLakeExceptionSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_data_lake_exception_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_data_lake_exception_subscription)
        """

    def create_data_lake_organization_configuration(
        self, **kwargs: Unpack[CreateDataLakeOrganizationConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Automatically enables Amazon Security Lake for new member accounts in your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_data_lake_organization_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_data_lake_organization_configuration)
        """

    def create_subscriber(
        self, **kwargs: Unpack[CreateSubscriberRequestTypeDef]
    ) -> CreateSubscriberResponseTypeDef:
        """
        Creates a subscriber for accounts that are already enabled in Amazon Security
        Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_subscriber.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_subscriber)
        """

    def create_subscriber_notification(
        self, **kwargs: Unpack[CreateSubscriberNotificationRequestTypeDef]
    ) -> CreateSubscriberNotificationResponseTypeDef:
        """
        Notifies the subscriber when new data is written to the data lake for the
        sources that the subscriber consumes in Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/create_subscriber_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#create_subscriber_notification)
        """

    def delete_aws_log_source(
        self, **kwargs: Unpack[DeleteAwsLogSourceRequestTypeDef]
    ) -> DeleteAwsLogSourceResponseTypeDef:
        """
        Removes a natively supported Amazon Web Services service as an Amazon Security
        Lake source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_aws_log_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_aws_log_source)
        """

    def delete_custom_log_source(
        self, **kwargs: Unpack[DeleteCustomLogSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a custom log source from Amazon Security Lake, to stop sending data
        from the custom source to Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_custom_log_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_custom_log_source)
        """

    def delete_data_lake(self, **kwargs: Unpack[DeleteDataLakeRequestTypeDef]) -> Dict[str, Any]:
        """
        When you disable Amazon Security Lake from your account, Security Lake is
        disabled in all Amazon Web Services Regions and it stops collecting data from
        your sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_data_lake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_data_lake)
        """

    def delete_data_lake_exception_subscription(self) -> Dict[str, Any]:
        """
        Deletes the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_data_lake_exception_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_data_lake_exception_subscription)
        """

    def delete_data_lake_organization_configuration(
        self, **kwargs: Unpack[DeleteDataLakeOrganizationConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Turns off automatic enablement of Amazon Security Lake for member accounts that
        are added to an organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_data_lake_organization_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_data_lake_organization_configuration)
        """

    def delete_subscriber(self, **kwargs: Unpack[DeleteSubscriberRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the subscription permission and all notification settings for accounts
        that are already enabled in Amazon Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_subscriber.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_subscriber)
        """

    def delete_subscriber_notification(
        self, **kwargs: Unpack[DeleteSubscriberNotificationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified subscription notification in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/delete_subscriber_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#delete_subscriber_notification)
        """

    def deregister_data_lake_delegated_administrator(self) -> Dict[str, Any]:
        """
        Deletes the Amazon Security Lake delegated administrator account for the
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/deregister_data_lake_delegated_administrator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#deregister_data_lake_delegated_administrator)
        """

    def get_data_lake_exception_subscription(
        self,
    ) -> GetDataLakeExceptionSubscriptionResponseTypeDef:
        """
        Retrieves the protocol and endpoint that were provided when subscribing to
        Amazon SNS topics for exception notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_data_lake_exception_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_data_lake_exception_subscription)
        """

    def get_data_lake_organization_configuration(
        self,
    ) -> GetDataLakeOrganizationConfigurationResponseTypeDef:
        """
        Retrieves the configuration that will be automatically set up for accounts
        added to the organization after the organization has onboarded to Amazon
        Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_data_lake_organization_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_data_lake_organization_configuration)
        """

    def get_data_lake_sources(
        self, **kwargs: Unpack[GetDataLakeSourcesRequestTypeDef]
    ) -> GetDataLakeSourcesResponseTypeDef:
        """
        Retrieves a snapshot of the current Region, including whether Amazon Security
        Lake is enabled for those accounts and which sources Security Lake is
        collecting data from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_data_lake_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_data_lake_sources)
        """

    def get_subscriber(
        self, **kwargs: Unpack[GetSubscriberRequestTypeDef]
    ) -> GetSubscriberResponseTypeDef:
        """
        Retrieves the subscription information for the specified subscription ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_subscriber.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_subscriber)
        """

    def list_data_lake_exceptions(
        self, **kwargs: Unpack[ListDataLakeExceptionsRequestTypeDef]
    ) -> ListDataLakeExceptionsResponseTypeDef:
        """
        Lists the Amazon Security Lake exceptions that you can use to find the source
        of problems and fix them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/list_data_lake_exceptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#list_data_lake_exceptions)
        """

    def list_data_lakes(
        self, **kwargs: Unpack[ListDataLakesRequestTypeDef]
    ) -> ListDataLakesResponseTypeDef:
        """
        Retrieves the Amazon Security Lake configuration object for the specified
        Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/list_data_lakes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#list_data_lakes)
        """

    def list_log_sources(
        self, **kwargs: Unpack[ListLogSourcesRequestTypeDef]
    ) -> ListLogSourcesResponseTypeDef:
        """
        Retrieves the log sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/list_log_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#list_log_sources)
        """

    def list_subscribers(
        self, **kwargs: Unpack[ListSubscribersRequestTypeDef]
    ) -> ListSubscribersResponseTypeDef:
        """
        Lists all subscribers for the specific Amazon Security Lake account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/list_subscribers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#list_subscribers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags (keys and values) that are associated with an Amazon
        Security Lake resource: a subscriber, or the data lake configuration for your
        Amazon Web Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#list_tags_for_resource)
        """

    def register_data_lake_delegated_administrator(
        self, **kwargs: Unpack[RegisterDataLakeDelegatedAdministratorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Designates the Amazon Security Lake delegated administrator account for the
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/register_data_lake_delegated_administrator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#register_data_lake_delegated_administrator)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates one or more tags that are associated with an Amazon Security
        Lake resource: a subscriber, or the data lake configuration for your Amazon Web
        Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags (keys and values) from an Amazon Security Lake
        resource: a subscriber, or the data lake configuration for your Amazon Web
        Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#untag_resource)
        """

    def update_data_lake(
        self, **kwargs: Unpack[UpdateDataLakeRequestTypeDef]
    ) -> UpdateDataLakeResponseTypeDef:
        """
        You can use <code>UpdateDataLake</code> to specify where to store your security
        data, how it should be encrypted at rest and for how long.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/update_data_lake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#update_data_lake)
        """

    def update_data_lake_exception_subscription(
        self, **kwargs: Unpack[UpdateDataLakeExceptionSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/update_data_lake_exception_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#update_data_lake_exception_subscription)
        """

    def update_subscriber(
        self, **kwargs: Unpack[UpdateSubscriberRequestTypeDef]
    ) -> UpdateSubscriberResponseTypeDef:
        """
        Updates an existing subscription for the given Amazon Security Lake account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/update_subscriber.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#update_subscriber)
        """

    def update_subscriber_notification(
        self, **kwargs: Unpack[UpdateSubscriberNotificationRequestTypeDef]
    ) -> UpdateSubscriberNotificationResponseTypeDef:
        """
        Updates an existing notification method for the subscription (SQS or HTTPs
        endpoint) or switches the notification subscription endpoint for a subscriber.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/update_subscriber_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#update_subscriber_notification)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_data_lake_sources"]
    ) -> GetDataLakeSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_lake_exceptions"]
    ) -> ListDataLakeExceptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_log_sources"]
    ) -> ListLogSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscribers"]
    ) -> ListSubscribersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client/#get_paginator)
        """
