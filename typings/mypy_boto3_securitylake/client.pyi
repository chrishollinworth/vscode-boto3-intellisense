"""
Type annotations for securitylake service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_securitylake import SecurityLakeClient

    client: SecurityLakeClient = boto3.client("securitylake")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AccessTypeType
from .paginator import (
    GetDataLakeSourcesPaginator,
    ListDataLakeExceptionsPaginator,
    ListLogSourcesPaginator,
    ListSubscribersPaginator,
)
from .type_defs import (
    AwsIdentityTypeDef,
    AwsLogSourceConfigurationTypeDef,
    CreateAwsLogSourceResponseTypeDef,
    CreateCustomLogSourceResponseTypeDef,
    CreateDataLakeResponseTypeDef,
    CreateSubscriberNotificationResponseTypeDef,
    CreateSubscriberResponseTypeDef,
    CustomLogSourceConfigurationTypeDef,
    DataLakeAutoEnableNewAccountConfigurationTypeDef,
    DataLakeConfigurationTypeDef,
    DeleteAwsLogSourceResponseTypeDef,
    GetDataLakeExceptionSubscriptionResponseTypeDef,
    GetDataLakeOrganizationConfigurationResponseTypeDef,
    GetDataLakeSourcesResponseTypeDef,
    GetSubscriberResponseTypeDef,
    ListDataLakeExceptionsResponseTypeDef,
    ListDataLakesResponseTypeDef,
    ListLogSourcesResponseTypeDef,
    ListSubscribersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LogSourceResourceTypeDef,
    NotificationConfigurationTypeDef,
    TagTypeDef,
    UpdateDataLakeResponseTypeDef,
    UpdateSubscriberNotificationResponseTypeDef,
    UpdateSubscriberResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SecurityLakeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class SecurityLakeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SecurityLakeClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#close)
        """
    def create_aws_log_source(
        self, *, sources: List["AwsLogSourceConfigurationTypeDef"]
    ) -> CreateAwsLogSourceResponseTypeDef:
        """
        Adds a natively supported Amazon Web Service as an Amazon Security Lake source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_aws_log_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_aws_log_source)
        """
    def create_custom_log_source(
        self,
        *,
        sourceName: str,
        configuration: "CustomLogSourceConfigurationTypeDef" = None,
        eventClasses: List[str] = None,
        sourceVersion: str = None
    ) -> CreateCustomLogSourceResponseTypeDef:
        """
        Adds a third-party custom source in Amazon Security Lake, from the Amazon Web
        Services Region where you want to create a custom source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_custom_log_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_custom_log_source)
        """
    def create_data_lake(
        self,
        *,
        configurations: List["DataLakeConfigurationTypeDef"],
        metaStoreManagerRoleArn: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateDataLakeResponseTypeDef:
        """
        Initializes an Amazon Security Lake instance with the provided (or default)
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_data_lake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_data_lake)
        """
    def create_data_lake_exception_subscription(
        self,
        *,
        notificationEndpoint: str,
        subscriptionProtocol: str,
        exceptionTimeToLive: int = None
    ) -> Dict[str, Any]:
        """
        Creates the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_data_lake_exception_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_data_lake_exception_subscription)
        """
    def create_data_lake_organization_configuration(
        self, *, autoEnableNewAccount: List["DataLakeAutoEnableNewAccountConfigurationTypeDef"]
    ) -> Dict[str, Any]:
        """
        Automatically enables Amazon Security Lake for new member accounts in your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_data_lake_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_data_lake_organization_configuration)
        """
    def create_subscriber(
        self,
        *,
        sources: List["LogSourceResourceTypeDef"],
        subscriberIdentity: "AwsIdentityTypeDef",
        subscriberName: str,
        accessTypes: List[AccessTypeType] = None,
        subscriberDescription: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateSubscriberResponseTypeDef:
        """
        Creates a subscription permission for accounts that are already enabled in
        Amazon Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_subscriber)
        """
    def create_subscriber_notification(
        self, *, configuration: "NotificationConfigurationTypeDef", subscriberId: str
    ) -> CreateSubscriberNotificationResponseTypeDef:
        """
        Notifies the subscriber when new data is written to the data lake for the
        sources that the subscriber consumes in Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.create_subscriber_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#create_subscriber_notification)
        """
    def delete_aws_log_source(
        self, *, sources: List["AwsLogSourceConfigurationTypeDef"]
    ) -> DeleteAwsLogSourceResponseTypeDef:
        """
        Removes a natively supported Amazon Web Service as an Amazon Security Lake
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_aws_log_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_aws_log_source)
        """
    def delete_custom_log_source(
        self, *, sourceName: str, sourceVersion: str = None
    ) -> Dict[str, Any]:
        """
        Removes a custom log source from Amazon Security Lake, to stop sending data from
        the custom source to Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_custom_log_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_custom_log_source)
        """
    def delete_data_lake(self, *, regions: List[str]) -> Dict[str, Any]:
        """
        When you disable Amazon Security Lake from your account, Security Lake is
        disabled in all Amazon Web Services Regions and it stops collecting data from
        your sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_data_lake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_data_lake)
        """
    def delete_data_lake_exception_subscription(self) -> Dict[str, Any]:
        """
        Deletes the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_data_lake_exception_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_data_lake_exception_subscription)
        """
    def delete_data_lake_organization_configuration(
        self, *, autoEnableNewAccount: List["DataLakeAutoEnableNewAccountConfigurationTypeDef"]
    ) -> Dict[str, Any]:
        """
        Turns off automatic enablement of Amazon Security Lake for member accounts that
        are added to an organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_data_lake_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_data_lake_organization_configuration)
        """
    def delete_subscriber(self, *, subscriberId: str) -> Dict[str, Any]:
        """
        Deletes the subscription permission and all notification settings for accounts
        that are already enabled in Amazon Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_subscriber)
        """
    def delete_subscriber_notification(self, *, subscriberId: str) -> Dict[str, Any]:
        """
        Deletes the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.delete_subscriber_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#delete_subscriber_notification)
        """
    def deregister_data_lake_delegated_administrator(self) -> Dict[str, Any]:
        """
        Deletes the Amazon Security Lake delegated administrator account for the
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.deregister_data_lake_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#deregister_data_lake_delegated_administrator)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#generate_presigned_url)
        """
    def get_data_lake_exception_subscription(
        self,
    ) -> GetDataLakeExceptionSubscriptionResponseTypeDef:
        """
        Retrieves the details of exception notifications for the account in Amazon
        Security Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.get_data_lake_exception_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#get_data_lake_exception_subscription)
        """
    def get_data_lake_organization_configuration(
        self,
    ) -> GetDataLakeOrganizationConfigurationResponseTypeDef:
        """
        Retrieves the configuration that will be automatically set up for accounts added
        to the organization after the organization has onboarded to Amazon Security
        Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.get_data_lake_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#get_data_lake_organization_configuration)
        """
    def get_data_lake_sources(
        self, *, accounts: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> GetDataLakeSourcesResponseTypeDef:
        """
        Retrieves a snapshot of the current Region, including whether Amazon Security
        Lake is enabled for those accounts and which sources Security Lake is collecting
        data from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.get_data_lake_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#get_data_lake_sources)
        """
    def get_subscriber(self, *, subscriberId: str) -> GetSubscriberResponseTypeDef:
        """
        Retrieves the subscription information for the specified subscription ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.get_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#get_subscriber)
        """
    def list_data_lake_exceptions(
        self, *, maxResults: int = None, nextToken: str = None, regions: List[str] = None
    ) -> ListDataLakeExceptionsResponseTypeDef:
        """
        Lists the Amazon Security Lake exceptions that you can use to find the source of
        problems and fix them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.list_data_lake_exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#list_data_lake_exceptions)
        """
    def list_data_lakes(self, *, regions: List[str] = None) -> ListDataLakesResponseTypeDef:
        """
        Retrieves the Amazon Security Lake configuration object for the specified Amazon
        Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.list_data_lakes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#list_data_lakes)
        """
    def list_log_sources(
        self,
        *,
        accounts: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
        regions: List[str] = None,
        sources: List["LogSourceResourceTypeDef"] = None
    ) -> ListLogSourcesResponseTypeDef:
        """
        Retrieves the log sources in the current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.list_log_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#list_log_sources)
        """
    def list_subscribers(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSubscribersResponseTypeDef:
        """
        List all subscribers for the specific Amazon Security Lake account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.list_subscribers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#list_subscribers)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags (keys and values) that are associated with an Amazon Security
        Lake resource: a subscriber, or the data lake configuration for your Amazon Web
        Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#list_tags_for_resource)
        """
    def register_data_lake_delegated_administrator(self, *, accountId: str) -> Dict[str, Any]:
        """
        Designates the Amazon Security Lake delegated administrator account for the
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.register_data_lake_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#register_data_lake_delegated_administrator)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or updates one or more tags that are associated with an Amazon Security
        Lake resource: a subscriber, or the data lake configuration for your Amazon Web
        Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags (keys and values) from an Amazon Security Lake
        resource: a subscriber, or the data lake configuration for your Amazon Web
        Services account in a particular Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#untag_resource)
        """
    def update_data_lake(
        self, *, configurations: List["DataLakeConfigurationTypeDef"]
    ) -> UpdateDataLakeResponseTypeDef:
        """
        Specifies where to store your security data and for how long.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.update_data_lake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#update_data_lake)
        """
    def update_data_lake_exception_subscription(
        self,
        *,
        notificationEndpoint: str,
        subscriptionProtocol: str,
        exceptionTimeToLive: int = None
    ) -> Dict[str, Any]:
        """
        Updates the specified notification subscription in Amazon Security Lake for the
        organization you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.update_data_lake_exception_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#update_data_lake_exception_subscription)
        """
    def update_subscriber(
        self,
        *,
        subscriberId: str,
        sources: List["LogSourceResourceTypeDef"] = None,
        subscriberDescription: str = None,
        subscriberIdentity: "AwsIdentityTypeDef" = None,
        subscriberName: str = None
    ) -> UpdateSubscriberResponseTypeDef:
        """
        Updates an existing subscription for the given Amazon Security Lake account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.update_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#update_subscriber)
        """
    def update_subscriber_notification(
        self, *, configuration: "NotificationConfigurationTypeDef", subscriberId: str
    ) -> UpdateSubscriberNotificationResponseTypeDef:
        """
        Updates an existing notification method for the subscription (SQS or HTTPs
        endpoint) or switches the notification subscription endpoint for a subscriber.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Client.update_subscriber_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/client.html#update_subscriber_notification)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_data_lake_sources"]
    ) -> GetDataLakeSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Paginator.GetDataLakeSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#getdatalakesourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_lake_exceptions"]
    ) -> ListDataLakeExceptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Paginator.ListDataLakeExceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listdatalakeexceptionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_log_sources"]) -> ListLogSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Paginator.ListLogSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listlogsourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribers"]
    ) -> ListSubscribersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/securitylake.html#SecurityLake.Paginator.ListSubscribers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/paginators.html#listsubscriberspaginator)
        """
