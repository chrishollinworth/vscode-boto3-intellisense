"""
Type annotations for sns service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sns import SNSClient

    client: SNSClient = boto3.client("sns")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import LanguageCodeStringType
from .paginator import (
    ListEndpointsByPlatformApplicationPaginator,
    ListOriginationNumbersPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListPlatformApplicationsPaginator,
    ListSMSSandboxPhoneNumbersPaginator,
    ListSubscriptionsByTopicPaginator,
    ListSubscriptionsPaginator,
    ListTopicsPaginator,
)
from .type_defs import (
    CheckIfPhoneNumberIsOptedOutResponseTypeDef,
    ConfirmSubscriptionResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreatePlatformApplicationResponseTypeDef,
    CreateTopicResponseTypeDef,
    GetEndpointAttributesResponseTypeDef,
    GetPlatformApplicationAttributesResponseTypeDef,
    GetSMSAttributesResponseTypeDef,
    GetSMSSandboxAccountStatusResultTypeDef,
    GetSubscriptionAttributesResponseTypeDef,
    GetTopicAttributesResponseTypeDef,
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListOriginationNumbersResultTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSMSSandboxPhoneNumbersResultTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTopicsResponseTypeDef,
    MessageAttributeValueTypeDef,
    PublishBatchRequestEntryTypeDef,
    PublishBatchResponseTypeDef,
    PublishResponseTypeDef,
    SubscribeResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SNSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationErrorException: Type[BotocoreClientError]
    BatchEntryIdsNotDistinctException: Type[BotocoreClientError]
    BatchRequestTooLongException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentAccessException: Type[BotocoreClientError]
    EmptyBatchRequestException: Type[BotocoreClientError]
    EndpointDisabledException: Type[BotocoreClientError]
    FilterPolicyLimitExceededException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidBatchEntryIdException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSecurityException: Type[BotocoreClientError]
    KMSAccessDeniedException: Type[BotocoreClientError]
    KMSDisabledException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KMSNotFoundException: Type[BotocoreClientError]
    KMSOptInRequired: Type[BotocoreClientError]
    KMSThrottlingException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    OptedOutException: Type[BotocoreClientError]
    PlatformApplicationDisabledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    StaleTagException: Type[BotocoreClientError]
    SubscriptionLimitExceededException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TooManyEntriesInBatchRequestException: Type[BotocoreClientError]
    TopicLimitExceededException: Type[BotocoreClientError]
    UserErrorException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    VerificationException: Type[BotocoreClientError]

class SNSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SNSClient exceptions.
        """
    def add_permission(
        self, *, TopicArn: str, Label: str, AWSAccountId: List[str], ActionName: List[str]
    ) -> None:
        """
        Adds a statement to a topic's access control policy, granting access for the
        specified Amazon Web Services accounts to the specified actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#add_permission)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#can_paginate)
        """
    def check_if_phone_number_is_opted_out(
        self, *, phoneNumber: str
    ) -> CheckIfPhoneNumberIsOptedOutResponseTypeDef:
        """
        Accepts a phone number and indicates whether the phone holder has opted out of
        receiving SMS messages from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.check_if_phone_number_is_opted_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#check_if_phone_number_is_opted_out)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#close)
        """
    def confirm_subscription(
        self, *, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ConfirmSubscriptionResponseTypeDef:
        """
        Verifies an endpoint owner's intent to receive messages by validating the token
        sent to the endpoint by an earlier `Subscribe` action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.confirm_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#confirm_subscription)
        """
    def create_platform_application(
        self, *, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> CreatePlatformApplicationResponseTypeDef:
        """
        Creates a platform application object for one of the supported push notification
        services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and
        mobile apps may register.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.create_platform_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#create_platform_application)
        """
    def create_platform_endpoint(
        self,
        *,
        PlatformApplicationArn: str,
        Token: str,
        CustomUserData: str = None,
        Attributes: Dict[str, str] = None
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates an endpoint for a device and mobile app on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.create_platform_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#create_platform_endpoint)
        """
    def create_sms_sandbox_phone_number(
        self, *, PhoneNumber: str, LanguageCode: LanguageCodeStringType = None
    ) -> Dict[str, Any]:
        """
        Adds a destination phone number to an Amazon Web Services account in the SMS
        sandbox and sends a one-time password (OTP) to that phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.create_sms_sandbox_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#create_sms_sandbox_phone_number)
        """
    def create_topic(
        self, *, Name: str, Attributes: Dict[str, str] = None, Tags: List["TagTypeDef"] = None
    ) -> CreateTopicResponseTypeDef:
        """
        Creates a topic to which notifications can be published.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.create_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#create_topic)
        """
    def delete_endpoint(self, *, EndpointArn: str) -> None:
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#delete_endpoint)
        """
    def delete_platform_application(self, *, PlatformApplicationArn: str) -> None:
        """
        Deletes a platform application object for one of the supported push notification
        services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.delete_platform_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#delete_platform_application)
        """
    def delete_sms_sandbox_phone_number(self, *, PhoneNumber: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Web Services account's verified or pending phone number from
        the SMS sandbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.delete_sms_sandbox_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#delete_sms_sandbox_phone_number)
        """
    def delete_topic(self, *, TopicArn: str) -> None:
        """
        Deletes a topic and all its subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.delete_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#delete_topic)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#generate_presigned_url)
        """
    def get_endpoint_attributes(self, *, EndpointArn: str) -> GetEndpointAttributesResponseTypeDef:
        """
        Retrieves the endpoint attributes for a device on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_endpoint_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_endpoint_attributes)
        """
    def get_platform_application_attributes(
        self, *, PlatformApplicationArn: str
    ) -> GetPlatformApplicationAttributesResponseTypeDef:
        """
        Retrieves the attributes of the platform application object for the supported
        push notification services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_platform_application_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_platform_application_attributes)
        """
    def get_sms_attributes(
        self, *, attributes: List[str] = None
    ) -> GetSMSAttributesResponseTypeDef:
        """
        Returns the settings for sending SMS messages from your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_sms_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_sms_attributes)
        """
    def get_sms_sandbox_account_status(self) -> GetSMSSandboxAccountStatusResultTypeDef:
        """
        Retrieves the SMS sandbox status for the calling Amazon Web Services account in
        the target Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_sms_sandbox_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_sms_sandbox_account_status)
        """
    def get_subscription_attributes(
        self, *, SubscriptionArn: str
    ) -> GetSubscriptionAttributesResponseTypeDef:
        """
        Returns all of the properties of a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_subscription_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_subscription_attributes)
        """
    def get_topic_attributes(self, *, TopicArn: str) -> GetTopicAttributesResponseTypeDef:
        """
        Returns all of the properties of a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.get_topic_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#get_topic_attributes)
        """
    def list_endpoints_by_platform_application(
        self, *, PlatformApplicationArn: str, NextToken: str = None
    ) -> ListEndpointsByPlatformApplicationResponseTypeDef:
        """
        Lists the endpoints and endpoint attributes for devices in a supported push
        notification service, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_endpoints_by_platform_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_endpoints_by_platform_application)
        """
    def list_origination_numbers(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListOriginationNumbersResultTypeDef:
        """
        Lists the calling Amazon Web Services account's dedicated origination numbers
        and their metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_origination_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_origination_numbers)
        """
    def list_phone_numbers_opted_out(
        self, *, nextToken: str = None
    ) -> ListPhoneNumbersOptedOutResponseTypeDef:
        """
        Returns a list of phone numbers that are opted out, meaning you cannot send SMS
        messages to them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_phone_numbers_opted_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_phone_numbers_opted_out)
        """
    def list_platform_applications(
        self, *, NextToken: str = None
    ) -> ListPlatformApplicationsResponseTypeDef:
        """
        Lists the platform application objects for the supported push notification
        services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_platform_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_platform_applications)
        """
    def list_sms_sandbox_phone_numbers(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListSMSSandboxPhoneNumbersResultTypeDef:
        """
        Lists the calling Amazon Web Services account's current verified and pending
        destination phone numbers in the SMS sandbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_sms_sandbox_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_sms_sandbox_phone_numbers)
        """
    def list_subscriptions(self, *, NextToken: str = None) -> ListSubscriptionsResponseTypeDef:
        """
        Returns a list of the requester's subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_subscriptions)
        """
    def list_subscriptions_by_topic(
        self, *, TopicArn: str, NextToken: str = None
    ) -> ListSubscriptionsByTopicResponseTypeDef:
        """
        Returns a list of the subscriptions to a specific topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_subscriptions_by_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_subscriptions_by_topic)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags added to the specified Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_tags_for_resource)
        """
    def list_topics(self, *, NextToken: str = None) -> ListTopicsResponseTypeDef:
        """
        Returns a list of the requester's topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.list_topics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#list_topics)
        """
    def opt_in_phone_number(self, *, phoneNumber: str) -> Dict[str, Any]:
        """
        Use this request to opt in a phone number that is opted out, which enables you
        to resume sending SMS messages to the number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.opt_in_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#opt_in_phone_number)
        """
    def publish(
        self,
        *,
        Message: str,
        TopicArn: str = None,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None
    ) -> PublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic, a text message (SMS message) directly to
        a phone number, or a message to a mobile platform endpoint (when you specify the
        `TargetArn` ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.publish)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#publish)
        """
    def publish_batch(
        self, *, TopicArn: str, PublishBatchRequestEntries: List["PublishBatchRequestEntryTypeDef"]
    ) -> PublishBatchResponseTypeDef:
        """
        Publishes up to ten messages to the specified topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.publish_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#publish_batch)
        """
    def remove_permission(self, *, TopicArn: str, Label: str) -> None:
        """
        Removes a statement from a topic's access control policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#remove_permission)
        """
    def set_endpoint_attributes(self, *, EndpointArn: str, Attributes: Dict[str, str]) -> None:
        """
        Sets the attributes for an endpoint for a device on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.set_endpoint_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#set_endpoint_attributes)
        """
    def set_platform_application_attributes(
        self, *, PlatformApplicationArn: str, Attributes: Dict[str, str]
    ) -> None:
        """
        Sets the attributes of the platform application object for the supported push
        notification services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.set_platform_application_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#set_platform_application_attributes)
        """
    def set_sms_attributes(self, *, attributes: Dict[str, str]) -> Dict[str, Any]:
        """
        Use this request to set the default settings for sending SMS messages and
        receiving daily SMS usage reports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.set_sms_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#set_sms_attributes)
        """
    def set_subscription_attributes(
        self, *, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        Allows a subscription owner to set an attribute of the subscription to a new
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.set_subscription_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#set_subscription_attributes)
        """
    def set_topic_attributes(
        self, *, TopicArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        Allows a topic owner to set an attribute of the topic to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.set_topic_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#set_topic_attributes)
        """
    def subscribe(
        self,
        *,
        TopicArn: str,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None
    ) -> SubscribeResponseTypeDef:
        """
        Subscribes an endpoint to an Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.subscribe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#subscribe)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add tags to the specified Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#tag_resource)
        """
    def unsubscribe(self, *, SubscriptionArn: str) -> None:
        """
        Deletes a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.unsubscribe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#unsubscribe)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from the specified Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#untag_resource)
        """
    def verify_sms_sandbox_phone_number(
        self, *, PhoneNumber: str, OneTimePassword: str
    ) -> Dict[str, Any]:
        """
        Verifies a destination phone number with a one-time password (OTP) for the
        calling Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Client.verify_sms_sandbox_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/client.html#verify_sms_sandbox_phone_number)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoints_by_platform_application"]
    ) -> ListEndpointsByPlatformApplicationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listendpointsbyplatformapplicationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_origination_numbers"]
    ) -> ListOriginationNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListOriginationNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listoriginationnumberspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_opted_out"]
    ) -> ListPhoneNumbersOptedOutPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listphonenumbersoptedoutpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_applications"]
    ) -> ListPlatformApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listplatformapplicationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sms_sandbox_phone_numbers"]
    ) -> ListSMSSandboxPhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListSMSSandboxPhoneNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listsmssandboxphonenumberspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listsubscriptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions_by_topic"]
    ) -> ListSubscriptionsByTopicPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listsubscriptionsbytopicpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_topics"]) -> ListTopicsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/sns.html#SNS.Paginator.ListTopics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators.html#listtopicspaginator)
        """
