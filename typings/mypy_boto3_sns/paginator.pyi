# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sns service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sns import SNSClient
    from mypy_boto3_sns.paginator import (
        ListEndpointsByPlatformApplicationPaginator,
        ListPhoneNumbersOptedOutPaginator,
        ListPlatformApplicationsPaginator,
        ListSubscriptionsPaginator,
        ListSubscriptionsByTopicPaginator,
        ListTopicsPaginator,
    )

    client: SNSClient = boto3.client("sns")

    list_endpoints_by_platform_application_paginator: ListEndpointsByPlatformApplicationPaginator = client.get_paginator("list_endpoints_by_platform_application")
    list_phone_numbers_opted_out_paginator: ListPhoneNumbersOptedOutPaginator = client.get_paginator("list_phone_numbers_opted_out")
    list_platform_applications_paginator: ListPlatformApplicationsPaginator = client.get_paginator("list_platform_applications")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_subscriptions_by_topic_paginator: ListSubscriptionsByTopicPaginator = client.get_paginator("list_subscriptions_by_topic")
    list_topics_paginator: ListTopicsPaginator = client.get_paginator("list_topics")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sns.type_defs import (
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTopicsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListTopicsPaginator",
)


class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)
    """

    def paginate(
        self, PlatformApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsByPlatformApplicationResponseTypeDef]:
        """
        [ListEndpointsByPlatformApplication.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication.paginate)
        """


class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    """
    [Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPhoneNumbersOptedOutResponseTypeDef]:
        """
        [ListPhoneNumbersOptedOut.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut.paginate)
        """


class ListPlatformApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlatformApplicationsResponseTypeDef]:
        """
        [ListPlatformApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListPlatformApplications.paginate)
        """


class ListSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListSubscriptions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionsResponseTypeDef]:
        """
        [ListSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListSubscriptions.paginate)
        """


class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)
    """

    def paginate(
        self, TopicArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionsByTopicResponseTypeDef]:
        """
        [ListSubscriptionsByTopic.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic.paginate)
        """


class ListTopicsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListTopics)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicsResponseTypeDef]:
        """
        [ListTopics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sns.html#SNS.Paginator.ListTopics.paginate)
        """
