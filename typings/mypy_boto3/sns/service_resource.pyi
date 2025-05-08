"""
Type annotations for sns service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sns.service_resource import SNSServiceResource
    import mypy_boto3_sns.service_resource as sns_resources

    session = Session()
    resource: SNSServiceResource = session.resource("sns")

    my_platform_application: sns_resources.PlatformApplication = resource.PlatformApplication(...)
    my_platform_endpoint: sns_resources.PlatformEndpoint = resource.PlatformEndpoint(...)
    my_subscription: sns_resources.Subscription = resource.Subscription(...)
    my_topic: sns_resources.Topic = resource.Topic(...)
```
"""

from __future__ import annotations

import sys

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import SNSClient
from .type_defs import (
    AddPermissionInputTopicAddPermissionTypeDef,
    ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef,
    CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef,
    CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef,
    CreateTopicInputServiceResourceCreateTopicTypeDef,
    PublishInputPlatformEndpointPublishTypeDef,
    PublishInputTopicPublishTypeDef,
    PublishResponseTypeDef,
    RemovePermissionInputTopicRemovePermissionTypeDef,
    SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef,
    SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef,
    SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef,
    SetTopicAttributesInputTopicSetAttributesTypeDef,
    SubscribeInputTopicSubscribeTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Dict, Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "PlatformApplication",
    "PlatformApplicationEndpointsCollection",
    "PlatformEndpoint",
    "SNSServiceResource",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "Subscription",
    "Topic",
    "TopicSubscriptionsCollection",
)

class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#SNS.ServiceResource.platform_applications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
    """
    def all(self) -> ServiceResourcePlatformApplicationsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#SNS.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> ServiceResourcePlatformApplicationsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

    def limit(self, count: int) -> ServiceResourcePlatformApplicationsCollection:
        """
        Return at most this many PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

    def page_size(self, count: int) -> ServiceResourcePlatformApplicationsCollection:
        """
        Fetch at most this many PlatformApplications per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

    def pages(self) -> Iterator[List[PlatformApplication]]:
        """
        A generator which yields pages of PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

    def __iter__(self) -> Iterator[PlatformApplication]:
        """
        A generator which yields PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/platform_applications.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourceplatformapplicationscollection)
        """

class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#SNS.ServiceResource.subscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
    """
    def all(self) -> ServiceResourceSubscriptionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#SNS.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> ServiceResourceSubscriptionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

    def limit(self, count: int) -> ServiceResourceSubscriptionsCollection:
        """
        Return at most this many Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

    def page_size(self, count: int) -> ServiceResourceSubscriptionsCollection:
        """
        Fetch at most this many Subscriptions per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

    def pages(self) -> Iterator[List[Subscription]]:
        """
        A generator which yields pages of Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

    def __iter__(self) -> Iterator[Subscription]:
        """
        A generator which yields Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/subscriptions.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcesubscriptionscollection)
        """

class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#SNS.ServiceResource.topics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
    """
    def all(self) -> ServiceResourceTopicsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#SNS.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> ServiceResourceTopicsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

    def limit(self, count: int) -> ServiceResourceTopicsCollection:
        """
        Return at most this many Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

    def page_size(self, count: int) -> ServiceResourceTopicsCollection:
        """
        Fetch at most this many Topics per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

    def pages(self) -> Iterator[List[Topic]]:
        """
        A generator which yields pages of Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

    def __iter__(self) -> Iterator[Topic]:
        """
        A generator which yields Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/topics.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#serviceresourcetopicscollection)
        """

class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#SNS.PlatformApplication.endpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
    """
    def all(self) -> PlatformApplicationEndpointsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#SNS.PlatformApplication.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> PlatformApplicationEndpointsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

    def limit(self, count: int) -> PlatformApplicationEndpointsCollection:
        """
        Return at most this many PlatformEndpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

    def page_size(self, count: int) -> PlatformApplicationEndpointsCollection:
        """
        Fetch at most this many PlatformEndpoints per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

    def pages(self) -> Iterator[List[PlatformEndpoint]]:
        """
        A generator which yields pages of PlatformEndpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

    def __iter__(self) -> Iterator[PlatformEndpoint]:
        """
        A generator which yields PlatformEndpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/endpoints.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationendpoints)
        """

class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#SNS.Topic.subscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
    """
    def all(self) -> TopicSubscriptionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#SNS.Topic.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ...
    ) -> TopicSubscriptionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

    def limit(self, count: int) -> TopicSubscriptionsCollection:
        """
        Return at most this many Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

    def page_size(self, count: int) -> TopicSubscriptionsCollection:
        """
        Fetch at most this many Subscriptions per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

    def pages(self) -> Iterator[List[Subscription]]:
        """
        A generator which yields pages of Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

    def __iter__(self) -> Iterator[Subscription]:
        """
        A generator which yields Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscriptions.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscriptions)
        """

class PlatformApplication(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/index.html#SNS.PlatformApplication)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplication)
    """

    arn: str
    endpoints: PlatformApplicationEndpointsCollection
    attributes: Dict[str, str]
    meta: SNSResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this PlatformApplication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationget_available_subresources-method)
        """

    def create_platform_endpoint(
        self,
        **kwargs: Unpack[
            CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef
        ],
    ) -> _PlatformEndpoint:
        """
        Creates an endpoint for a device and mobile app on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/create_platform_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationcreate_platform_endpoint-method)
        """

    def delete(self) -> None:
        """
        Deletes a platform application object for one of the supported push
        notification services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationdelete-method)
        """

    def set_attributes(
        self,
        **kwargs: Unpack[
            SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef
        ],
    ) -> None:
        """
        Sets the attributes of the platform application object for the supported push
        notification services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/set_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationset_attributes-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformapplication/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformapplicationreload-method)
        """

_PlatformApplication = PlatformApplication

class PlatformEndpoint(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/index.html#SNS.PlatformEndpoint)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpoint)
    """

    arn: str
    attributes: Dict[str, str]
    meta: SNSResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this PlatformEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointdelete-method)
        """

    def publish(
        self, **kwargs: Unpack[PublishInputPlatformEndpointPublishTypeDef]
    ) -> PublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic, a text message (SMS message) directly
        to a phone number, or a message to a mobile platform endpoint (when you specify
        the <code>TargetArn</code>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/publish.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointpublish-method)
        """

    def set_attributes(
        self, **kwargs: Unpack[SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef]
    ) -> None:
        """
        Sets the attributes for an endpoint for a device on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/set_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointset_attributes-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/platformendpoint/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#platformendpointreload-method)
        """

_PlatformEndpoint = PlatformEndpoint

class Subscription(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/index.html#SNS.Subscription)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscription)
    """

    arn: str
    attributes: Dict[str, str]
    meta: SNSResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscriptionget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscriptiondelete-method)
        """

    def set_attributes(
        self, **kwargs: Unpack[SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef]
    ) -> None:
        """
        Allows a subscription owner to set an attribute of the subscription to a new
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/set_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscriptionset_attributes-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscriptionload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/subscription/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#subscriptionreload-method)
        """

_Subscription = Subscription

class Topic(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/index.html#SNS.Topic)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topic)
    """

    arn: str
    subscriptions: TopicSubscriptionsCollection
    attributes: Dict[str, str]
    meta: SNSResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicget_available_subresources-method)
        """

    def add_permission(self, **kwargs: Unpack[AddPermissionInputTopicAddPermissionTypeDef]) -> None:
        """
        Adds a statement to a topic's access control policy, granting access for the
        specified Amazon Web Services accounts to the specified actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/add_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicadd_permission-method)
        """

    def confirm_subscription(
        self, **kwargs: Unpack[ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef]
    ) -> _Subscription:
        """
        Verifies an endpoint owner's intent to receive messages by validating the token
        sent to the endpoint by an earlier <code>Subscribe</code> action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/confirm_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicconfirm_subscription-method)
        """

    def delete(self) -> None:
        """
        Deletes a topic and all its subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicdelete-method)
        """

    def publish(self, **kwargs: Unpack[PublishInputTopicPublishTypeDef]) -> PublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic, a text message (SMS message) directly
        to a phone number, or a message to a mobile platform endpoint (when you specify
        the <code>TargetArn</code>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/publish.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicpublish-method)
        """

    def remove_permission(
        self, **kwargs: Unpack[RemovePermissionInputTopicRemovePermissionTypeDef]
    ) -> None:
        """
        Removes a statement from a topic's access control policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/remove_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicremove_permission-method)
        """

    def set_attributes(
        self, **kwargs: Unpack[SetTopicAttributesInputTopicSetAttributesTypeDef]
    ) -> None:
        """
        Allows a topic owner to set an attribute of the topic to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/set_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicset_attributes-method)
        """

    def subscribe(self, **kwargs: Unpack[SubscribeInputTopicSubscribeTypeDef]) -> _Subscription:
        """
        Subscribes an endpoint to an Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/subscribe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicsubscribe-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/topic/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#topicreload-method)
        """

_Topic = Topic

class SNSResourceMeta(ResourceMeta):
    client: SNSClient  # type: ignore[override]

class SNSServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/)
    """

    meta: SNSResourceMeta  # type: ignore[override]
    platform_applications: ServiceResourcePlatformApplicationsCollection
    subscriptions: ServiceResourceSubscriptionsCollection
    topics: ServiceResourceTopicsCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourceget_available_subresources-method)
        """

    def create_platform_application(
        self,
        **kwargs: Unpack[
            CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef
        ],
    ) -> _PlatformApplication:
        """
        Creates a platform application object for one of the supported push
        notification services, such as APNS and GCM (Firebase Cloud Messaging), to
        which devices and mobile apps may register.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/create_platform_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourcecreate_platform_application-method)
        """

    def create_topic(
        self, **kwargs: Unpack[CreateTopicInputServiceResourceCreateTopicTypeDef]
    ) -> _Topic:
        """
        Creates a topic to which notifications can be published.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/create_topic.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourcecreate_topic-method)
        """

    def PlatformApplication(self, arn: str) -> _PlatformApplication:
        """
        Creates a PlatformApplication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/PlatformApplication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourceplatformapplication-method)
        """

    def PlatformEndpoint(self, arn: str) -> _PlatformEndpoint:
        """
        Creates a PlatformEndpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/PlatformEndpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourceplatformendpoint-method)
        """

    def Subscription(self, arn: str) -> _Subscription:
        """
        Creates a Subscription resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/Subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourcesubscription-method)
        """

    def Topic(self, arn: str) -> _Topic:
        """
        Creates a Topic resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/service-resource/Topic.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/service_resource/#snsserviceresourcetopic-method)
        """
