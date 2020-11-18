# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for sns service ServiceResource

Usage::

    ```python
    import boto3

    from mypy_boto3_sns import SNSServiceResource
    import mypy_boto3_sns.service_resource as sns_resources

    resource: SNSServiceResource = boto3.resource("sns")

    my_platform_application: sns_resources.PlatformApplication = resource.PlatformApplication(...)
    my_platform_endpoint: sns_resources.PlatformEndpoint = resource.PlatformEndpoint(...)
    my_subscription: sns_resources.Subscription = resource.Subscription(...)
    my_topic: sns_resources.Topic = resource.Topic(...)
```
"""
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_sns.type_defs import (
    MessageAttributeValueTypeDef,
    PublishResponseTypeDef,
    TagTypeDef,
)

__all__ = (
    "SNSServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [ServiceResource.platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    """

    def all(self) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def pages(self) -> Iterator[List["PlatformApplication"]]:
        pass

    def __iter__(self) -> Iterator["PlatformApplication"]:
        pass


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [ServiceResource.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    """

    def all(self) -> "ServiceResourceSubscriptionsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        pass

    def pages(self) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(self) -> Iterator["Subscription"]:
        pass


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [ServiceResource.topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.topics)
    """

    def all(self) -> "ServiceResourceTopicsCollection":
        pass

    def filter(self, NextToken: str = None) -> "ServiceResourceTopicsCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "ServiceResourceTopicsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceTopicsCollection":
        pass

    def pages(self) -> Iterator[List["Topic"]]:
        pass

    def __iter__(self) -> Iterator["Topic"]:
        pass


class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [PlatformApplication.endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.endpoints)
    """

    def all(self) -> "PlatformApplicationEndpointsCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def limit(self, count: int) -> "PlatformApplicationEndpointsCollection":
        pass

    def page_size(self, count: int) -> "PlatformApplicationEndpointsCollection":
        pass

    def pages(self) -> Iterator[List["PlatformEndpoint"]]:
        pass

    def __iter__(self) -> Iterator["PlatformEndpoint"]:
        pass


class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Topic.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.subscriptions)
    """

    def all(self) -> "TopicSubscriptionsCollection":
        pass

    def filter(self, NextToken: str = None) -> "TopicSubscriptionsCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "TopicSubscriptionsCollection":
        pass

    def page_size(self, count: int) -> "TopicSubscriptionsCollection":
        pass

    def pages(self) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(self) -> Iterator["Subscription"]:
        pass


class PlatformEndpoint(Boto3ServiceResource):
    """
    [PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [PlatformEndpoint.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [PlatformEndpoint.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.get_available_subresources)
        """

    def load(self) -> None:
        """
        [PlatformEndpoint.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.load)
        """

    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> PublishResponseTypeDef:
        """
        [PlatformEndpoint.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.publish)
        """

    def reload(self) -> None:
        """
        [PlatformEndpoint.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.reload)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [PlatformEndpoint.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformEndpoint.set_attributes)
        """


_PlatformEndpoint = PlatformEndpoint


class Subscription(Boto3ServiceResource):
    """
    [Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.Subscription)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [Subscription.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Subscription.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Subscription.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Subscription.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Subscription.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Subscription.load)
        """

    def reload(self) -> None:
        """
        [Subscription.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Subscription.reload)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Subscription.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Subscription.set_attributes)
        """


_Subscription = Subscription


class PlatformApplication(Boto3ServiceResource):
    """
    [PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
    """

    attributes: Dict[str, Any]
    arn: str
    endpoints: PlatformApplicationEndpointsCollection

    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, str] = None
    ) -> _PlatformEndpoint:
        """
        [PlatformApplication.create_platform_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.create_platform_endpoint)
        """

    def delete(self) -> None:
        """
        [PlatformApplication.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [PlatformApplication.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.get_available_subresources)
        """

    def load(self) -> None:
        """
        [PlatformApplication.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.load)
        """

    def reload(self) -> None:
        """
        [PlatformApplication.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.reload)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [PlatformApplication.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.PlatformApplication.set_attributes)
        """


_PlatformApplication = PlatformApplication


class Topic(Boto3ServiceResource):
    """
    [Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.Topic)
    """

    attributes: Dict[str, Any]
    arn: str
    subscriptions: TopicSubscriptionsCollection

    def add_permission(self, Label: str, AWSAccountId: List[str], ActionName: List[str]) -> None:
        """
        [Topic.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.add_permission)
        """

    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> _Subscription:
        """
        [Topic.confirm_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.confirm_subscription)
        """

    def delete(self) -> None:
        """
        [Topic.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Topic.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Topic.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.load)
        """

    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> PublishResponseTypeDef:
        """
        [Topic.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.publish)
        """

    def reload(self) -> None:
        """
        [Topic.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.reload)
        """

    def remove_permission(self, Label: str) -> None:
        """
        [Topic.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.remove_permission)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Topic.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.set_attributes)
        """

    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> _Subscription:
        """
        [Topic.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Topic.subscribe)
        """


_Topic = Topic


class SNSServiceResource(Boto3ServiceResource):
    """
    [SNS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource)
    """

    platform_applications: ServiceResourcePlatformApplicationsCollection
    subscriptions: ServiceResourceSubscriptionsCollection
    topics: ServiceResourceTopicsCollection

    def PlatformApplication(self, arn: str) -> _PlatformApplication:
        """
        [ServiceResource.PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        """

    def PlatformEndpoint(self, arn: str) -> _PlatformEndpoint:
        """
        [ServiceResource.PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        """

    def Subscription(self, arn: str) -> _Subscription:
        """
        [ServiceResource.Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.Subscription)
        """

    def Topic(self, arn: str) -> _Topic:
        """
        [ServiceResource.Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.Topic)
        """

    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> _PlatformApplication:
        """
        [ServiceResource.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        """

    def create_topic(
        self, Name: str, Attributes: Dict[str, str] = None, Tags: List["TagTypeDef"] = None
    ) -> _Topic:
        """
        [ServiceResource.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.create_topic)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        """
